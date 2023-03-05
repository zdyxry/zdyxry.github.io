---
title: 调整 arp 参数提高网络稳定性
date: 2019-06-17 21:20:04
tags:
- Linux
---

## 背景


最近发现一直使用的机房网络不稳定，时常出现网络无法联通，过一会又可以联通的情况，今天又遇到了，要彻底解决它。


## 问题

在机房网络规划中，地区 A 和地区 B 是通过 OpenVPN 连接的，也就是说每个地区的网关是一台虚拟机，提供 DHCP 服务。
今天地区 A 的机器又无法连接地区 B 了，我登陆网关尝试从网关 ping 目标主机，发现直接提示 :

```bash
No buffer space available
```

根据这个提示，感觉像是某些系统参数配置的小了，于是查了一下，发现跟 arp 有关。什么是 arp ？ 

相信对网络稍微有些概念的同学都不陌生，这里我直接引用维基百科：
>地址解析协议（英语：Address Resolution Protocol，缩写：ARP）。在以太网协议中规定，同一局域网中的一台主机要和另一台主机进行直接通信，必须要知道目标主机的MAC地址。而在TCP/IP协议中，网络层和传输层只关心目标主机的IP地址。这就导致在以太网中使用IP协议时，数据链路层的以太网协议接到上层IP协议提供的数据中，只包含目的主机的IP地址。于是需要一种方法，根据目的主机的IP地址，获得其MAC地址。这就是ARP协议要做的事情。所谓地址解析（address resolution）就是主机在发送帧前将目标IP地址转换成目标MAC地址的过程。


> 另外，当发送主机和目的主机不在同一个局域网中时，即便知道对方的MAC地址，两者也不能直接通信，必须经过路由转发才可以。所以此时，发送主机通过ARP协议获得的将不是目的主机的真实MAC地址，而是一台可以通往局域网外的路由器的MAC地址。于是此后发送主机发往目的主机的所有帧，都将发往该路由器，通过它向外发送。这种情况称为委托ARP或ARP代理（ARP Proxy）。


## 解决


知道了原因，那么我们来调整参数就好：

```bash
gc_thresh1 (since Linux 2.2)
The minimum number of entries to keep in the ARP cache. The garbage collector will not run if there are fewer than this number of entries in the cache. Defaults to 128.
gc_thresh2 (since Linux 2.2)
The soft maximum number of entries to keep in the ARP cache. The garbage collector will allow the number of entries to exceed this for 5 seconds before collection will be performed. Defaults to 512.
gc_thresh3 (since Linux 2.2)
The hard maximum number of entries to keep in the ARP cache. The garbage collector will always run if there are more than this number of entries in the cache. Defaults to 1024.
```


```bash
yiran@test:~$ cat /etc/sysctl.conf |grep -v ^# |grep -v ^$
net.ipv4.tcp_congestion_control = bbr
net.core.default_qdisc = fq
net.ipv4.neigh.default.gc_thresh1 = 4096
net.ipv4.neigh.default.gc_thresh2 = 8192
net.ipv4.neigh.default.gc_thresh3 = 8192
yiran@test:~$ sudo sysctl -p
net.ipv4.tcp_congestion_control = bbr
net.core.default_qdisc = fq
net.ipv4.neigh.default.gc_thresh1 = 4096
net.ipv4.neigh.default.gc_thresh2 = 8192
net.ipv4.neigh.default.gc_thresh3 = 8192
```


