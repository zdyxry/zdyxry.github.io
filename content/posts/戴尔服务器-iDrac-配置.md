---
title: 戴尔服务器 iDrac 配置
date: 2018-12-12 22:18:15
tags:
- Server
---

## 背景

之前介绍过超微的 IPMI 配置时提过，超微的 IPMI 是最简陋的，最近在用戴尔服务器的时候碰到了一个比较坑的事情，查了资料解决了，更加坚定之前的结论，IPMI 相应的配置尽量独立。

## 问题
在戴尔服务器安装 CentOS 后，可见网卡比预期要多出一块，物理服务器安装了两块 PCIe 网卡，一块千兆，一块万兆，每块网卡有两个网口，那么理应在服务器看到的应该是 4个网口，即 `ip ad ` 看到的应该是

```bash
root@node11 22:24:49 ~]$ip ad |grep enp
2: enp94s0f0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq master ovs-system state UP qlen 1000
3: enp24s0f0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq portid 3cfdfe6c9e10 state DOWN qlen 1000
4: enp24s0f1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq master ovs-system portid 3cfdfe6c9e12 state UP qlen 1000
5: enp94s0f1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN qlen 1000
```

但是安装完 OS，发现多出一块网口 `eno16` ，通过 `ethtool` 工具查看，发现该网口为千兆，且处于连接状态，最开始没多想，直接将该网口作为管理网络配置了，一切正常。

当我尝试通过该网口连接 IPMI 获取风扇信息时，发现无法获取，验证命令为：
`ipmitool -I lanplus -H <ipmi ip> -U <user name> -P <password> lan print`   
最开始以为是密码不对，后来发现是在 OS 内部无法 ping 通 IPMI IP，这就很奇怪了。

当时网络情况如下：

| 连通情况      | yiran's PC    |  IPMI IP | OS IP |
| --------- | -------- | ----- | -- |
| yiran's PC    | 1  | 1 |  1 |
| IPMI IP     |   1   |  1  |   0 |
| OS IP     | 1 |   0 |  1  |

因为没遇到过这种情况，根据经验，先检查了下 iDRAC 网络配置，发现当时 iDRAC 网卡选择的是 LOM1，也就是板载网卡，且该网卡处于 pass-through 状态，官方解释如下：

>板载网卡 (LAN On Motherboards, LOM)，如果您选择 Network Settings（网络设置）下的 Auto Dedicated NIC（自动专用 NIC），则当 iDRAC 将其 NIC 选择作为共享 LOM（1、2、3 或 4）并且在 iDRAC 专用 NIC 上检测到链接时，iDRAC 会更改其 NIC 选择来使用专用 NIC。如果在专用 NIC 上检 测不到链接，则 iDRAC 使用共享 LOM。从共享 NIC 切换到专用 NIC 的超时为五秒，而从专用 NIC 切换到共享 NIC 的超时为 30 秒。可以使用 RACADM 或 WS-MAN 配置此超时值。
如果选择 LOM 作为直通配置，并且使用专用模式连接服务器，则输入操作系统的 IPv4 地址。 注: 如果在共享的 LOM 模式下连接了服务器，则操作系统 IP 地址字段将禁用。

## 解决办法
将 iDRAC 网络配置从 LOM 改为 Dedicated 后，重启 OS 即可，注意，改为 Dedicated 后，OS 将无法识别到 LOM，需要重新配置网络。
