---

title: CentOS 多网卡多网关配置

date: 2018-05-29 19:21:36

tags:
- Linux

---



### 背景

日常使用中，开发机通常只配置一块网卡，通常配置为 DHCP 自动获取 IP，这样就可以自动从 DHCP Server 获取 IP，网关，DNS Server 等配置，不用手动配置。

  

最近在工作中存在一种场景，一台服务器，多块网卡，需要对不同的网卡配置各自网关，查找了一些资料，也踩了一些坑，记录一下过程。

  

### 配置过程

1. 官方配置
尝试在 `/etc/sysconfig/network-scripts/ifcfg-<device>` 中增加 GATEWAY 自动使之生效，实际上来看，多张网卡都配置 GATEWAY 字段会产生冲突，只能放弃通过网卡配置文件方式，尝试通过给网卡配置静态路由方式添加。  
在 CentOS [官方网站](https://www.centos.org/docs/5/html/5.2/Deployment_Guide/s1-networkscripts-static-routes.html)查找配置静态路由方法，文档中提到通过编写网卡路由配置文件`/etc/sysconfig/network-scripts/route-_<interface>`  ，配置完成后重启网络可以自动生效。  
官方这种方式我尝试了两种文件编写方式，一种为`192.168.64.0/20 via <gateway> dev <device>`，一种为 `ADDRESS0=xxxxx; NETMASK0=xxxxx; GATEWAY0=xxxxx`。两种配置方式均没有生效，只能放弃。
   
2. 手动配置    
可以通过 `route add ` 命令临时给第二章网卡配置网关，通过 `route -n` 查看是可以生效。但是因为最终目标是让路由随着网络服务（公司内部未使用 NetworkManager）Network 启动而配置，因此在 /etc/rc.local 中假如 `route add` 类似命令无法走通。   

3. 上述方法要么无法生效，要么存在无法持久化问题，均无法完成需求。 只能通过查看 网卡服务启动脚本来查找，查看 `/etc/init.d/network` （systemd 服务控制也是执行该文件），该文件是一个 Shell 脚本，找到路由配置相关：  

```shell
    2     # Add non interface-specific static-routes.
    1     if [ -f /etc/sysconfig/static-routes ]; then
  141        if [ -x /sbin/route ]; then
    1            grep "^any" /etc/sysconfig/static-routes | while read ignore args ; do
    2                    /sbin/route add -$args
    3            done
    4        else
    5            net_log $"Legacy static-route support not available: /sbin/route not found"
    6        fi
    7     fi
```
可以看到，在网络服务 network 启动过程中，会判断 `/etc/sysconfig/static-routes` 文件是否存在，如果存在则会通过 `route` 命令对该文件中记录以 `any` 开头的路由进行添加，添加命令为 `/sbin/route add -$args`。  
根据上述脚本，尝试编写 static-routes 文件：  

```
any net 192.168.64.0/20 gw 192.168.64.1
any net 10.0.10.0/24 gw 10.0.10.222
```
编写完成后，重启网络服务 `systemctl restart network ` ，执行 `route -n` 查看是否生效：  

```bash
[root@scvm9 19:49:55 ~]$route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.64.1    0.0.0.0         UG    0      0        0 eth0
10.0.10.0       0.0.0.0         255.255.255.0   U     0      0        0 eth2
10.0.10.0       10.0.10.222     255.255.255.0   UG    0      0        0 eth2
169.254.0.0     0.0.0.0         255.255.0.0     U     1002   0        0 eth0
```   

看上去已经生效，因为实际环境中没有第二块网卡网关设备，临时指定一个不存在的 IP。
本以为已经搞定，结果在实际验证的时候，发现第二块网卡无法连接其他节点，哪怕其他节点与它二层联通；尝试将网关指定可以正常工作的 IP 节点，可以与其他节点联通，且 traceroute 也没有经过网关而是直接连接。

### 问题排查
1. 尝试将网关配置成可以正常工作的节点
	* 各个节点可以正确联通
	* traceroute 到其他节点未经过网关
2. 尝试将网关配置成不存在节点
	* 各个节点无法正确联通
3. 尝试将网关掩码配置为网卡掩码的超集
	* 各个节点可以正确联通
	* traceroute 到其他节点未经过网关

### 总结
红帽系列发行版本配置静态路由可通过 /etc/sysconfig/static-routes 配置生效，但要注意在 static-routes 文件中的路由添加要添加网关节点对应的掩码而不是本地节点网卡掩码，网关掩码为本地网卡掩码的超集。

