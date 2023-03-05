---
title: 基于zeroconf实现节点自发现
date: 2018-08-22 16:07:11
tags:
- zeroconf
---

## 背景

通常我们使用联网的电子设备，都会配置一个 IP 地址用于通信，一般采用 DHCP 配置，DHCP 有 
lease 时间，如果超过 lease 时间又没有续约的话，产生的 IP 地址有可能发生改变，那么如何
自动识别我们的设备呢？ ZeroConf 是一个好的选择。

## ZeroConf

以下介绍摘录自维基百科：
> Zero-configuration networking (zeroconf) is a set of technologies that 
automatically creates a usable computer network based on the 
Internet Protocol Suite (TCP/IP) when computers or network peripherals are 
interconnected. It does not require manual operator intervention or special 
configuration servers. Without zeroconf, a network administrator must set up 
network services, such as Dynamic Host Configuration Protocol (DHCP) and 
Domain Name System (DNS), or configure each computer's network settings manually.
Zeroconf is built on three core technologies: automatic assignment of numeric 
network addresses for networked devices, automatic distribution and resolution 
of computer hostnames, and automatic location of network services, such as printing devices.  

简单来说我们可以通过 ZeroConf 进行服务自发现，日常使用最多的就是 Apple 家的产品及一些
打印设备。

## Avahi
如果我们想要在 Linux 中使用的话，我们可以选择 Avahi，配合 nss-mdns 一起使用可以在复杂网络场景下自动发现服务器，并获取 IPv4 或 IPv6 地址进行通信。

### 扫描节点安装
我们使用 yum 进行相应工具的安装：
```
yum install avahi-libs avahi-tools avahi-autoipd avahi nss-mdns 
```

### 扫描节点配置
安装完成后，我们修改配置文件，开启 IPv6 配置：

```bash
[root@yiran-pxe data]# cat /etc/nsswitch.conf |grep -v ^# |grep -v ^$
passwd:     files sss
shadow:     files sss
group:      files sss
hosts:      files mdns4_minimal [NOTFOUND=return] dns
bootparams: nisplus [NOTFOUND=return] files
ethers:     files
netmasks:   files
networks:   files
protocols:  files
rpc:        files
services:   files sss
netgroup:   files sss
publickey:  nisplus
automount:  files
aliases:    files nisplus
[root@yiran-pxe data]# cat /etc/avahi/avahi-daemon.conf  |grep -v ^# |grep -v ^$
[server]
use-ipv4=no
use-ipv6=yes            ## 开启 IPv6 
ratelimit-interval-usec=1000000
ratelimit-burst=1000
[wide-area]
enable-wide-area=yes
[publish]
[reflector]
[rlimits]
rlimit-core=0
rlimit-data=4194304
rlimit-fsize=0
rlimit-nofile=768
rlimit-stack=4194304
rlimit-nproc=3
```

配置完成后我们启动服务：
```bash
systemctl start avahi-daemon
```

### 被扫描节点配置

扫描节点可以通过制定的域名进行扫描，我们可以通过给被扫描节点配置特殊的主机名称，来实现自动识别被扫描节点具体是什么类型的服务器，比如我们可以通过 ipmitool 获取 IPMI IP，并配置主机名为 `node-192-168-67-173` 来实现识别，具体操作：
```bash
[root@node-192-168-67-173 ~]# cat /etc/hostname 
node-192-168-67-173
[root@node-192-168-67-173 ~]# hostname -F /etc/hostname
```

同样编辑 avahi 配置文件，开启 IPv6 配置：
```bash
[root@node-192-168-67-173 avahi]# cat avahi-daemon.conf |grep -v ^# |grep -v ^$
[server]
use-ipv4=yes
use-ipv6=yes
ratelimit-interval-usec=1000000
ratelimit-burst=1000
[wide-area]
enable-wide-area=yes
[publish]
publish-a-on-ipv6=yes
[reflector]
[rlimits]
rlimit-core=0
rlimit-data=4194304
rlimit-fsize=0
rlimit-nofile=768
rlimit-stack=4194304
rlimit-nproc=3
```

启动 avahi 服务：
```bash
systemctl start avahi-daemon
```

### 扫描节点发现节点

我们可以通过 `avahi-tools` 提供的 avahi-brower 工具进行持续扫描：
```bash
[root@yiran-pxe data]# avahi-browse -a
+ eno33559296 IPv6 node-192-168-67-173 [24:6e:96:7c:50:70]       Workstation          local
+ eno16780032 IPv6 node-192-168-67-173 [24:6e:96:7c:50:50]       Workstation          local
```

可以看到我们在扫描节点已经发现了被扫描节点的信息，那么我们接下来获取具体的 IP 地址：

```bash
[root@yiran-pxe data]# avahi-resolve --help 
avahi-resolve [options] -n <host name ...>
avahi-resolve [options] -a <address ... >

    -h --help            Show this help
    -V --version         Show version
    -n --name            Resolve host name
    -a --address         Resolve address
    -v --verbose         Enable verbose mode
    -6                   Lookup IPv6 address
    -4                   Lookup IPv4 address
[root@yiran-pxe data]# avahi-resolve -n node-192-168-67-173.local -4
node-192-168-67-173.local       127.0.0.1
[root@yiran-pxe data]# avahi-resolve -n node-192-168-67-173.local -6
node-192-168-67-173.local       fe80::266e:96ff:fe7c:5070
```

如果被扫描节点没有 IPv4 地址，则会显示 127.0.0.1，若有 IPv4 地址，则会正常显示。

### 远程通信

在得到具体的 IP 地址之后我们就可以按照上一篇博客提到的 IPv6 地址远程连接的方式进行通信了。

```bash
[root@yiran-pxe data]# ping6 fe80::266e:96ff:fe7c:5070%eno33559296
PING fe80::266e:96ff:fe7c:5070%eno33559296(fe80::266e:96ff:fe7c:5070) 56 data bytes
64 bytes from fe80::266e:96ff:fe7c:5070: icmp_seq=1 ttl=64 time=0.448 ms
64 bytes from fe80::266e:96ff:fe7c:5070: icmp_seq=2 ttl=64 time=0.338 ms
^C
--- fe80::266e:96ff:fe7c:5070%eno33559296 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 999ms
rtt min/avg/max/mdev = 0.338/0.393/0.448/0.055 ms
[root@yiran-pxe data]# ssh fe80::266e:96ff:fe7c:5070%eno33559296
root@fe80::266e:96ff:fe7c:5070%eno33559296's password: 
Last login: Wed Aug 22 15:44:17 2018 from fe80::250:56ff:fe9f:ef9c%eno3
[root@node-192-168-67-173 ~]# hostname
node-192-168-67-173
[root@node-192-168-67-173 ~]# logout
Connection to fe80::266e:96ff:fe7c:5070%eno33559296 closed.
```

## 总结
目前 Linux 发行版本都自动安装了 Avahi 服务，大家可以启用，方便远程连接控制。


