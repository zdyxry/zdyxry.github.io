---
title: Ansible 配置 IPv6 连接
date: 2018-08-17 13:43:40
tags:
- Ansible
---

## 背景

平时工作中因为通常需要远程操作较多 Linux 环境，引入了 Ansible，但是大都是通过 Ansible 远程命令的方式执行，少数的封装为 Playbook 也是很简单的配置。
最早的时候用过简单的 SaltStack，但是要安装 Agent，觉得不好用，在 16年早期的时候使用 Ansible，简单快捷（当然我对性能没有要求）。
最近需要把之前由 Shell & Python 拼装的一个服务统一用 Ansible 进行重写，又花了些时间看了看相关文档。发现大家操作远程机器无论是通过秘钥还是通过密码，都是基于 IPv4 的地址链接的，而有些机器是没有 IPv4 地址的，于是花费了些时间验证 Ansible IPv6 配置方式。


## IPv6
IPv6 维基百科的解释是：网际协议第6版（英文：Internet Protocol version 6，缩写：IPv6）是网际协议（IP）的最新版本，用作互联网的网络层协议，用它来取代IPv4主要是为了解决IPv4地址枯竭问题，不过它也在其他很多方面对IPv4有所改进。我们目前日常中使用的地址都是 IPv4 的地址（比如：192.168.1.1）。
使用 IPv6 有一个好处是，可以通过 NDP（Neighbor Discovery Protocol）扫描二层网络内的所有的 IPv6 地址，方便我们使用，那么我们如何判断 IPv6 是否可以连通呢？
可以通过 ping6 的方式判断，比如：
```Bash
[root@node111 14:00:44 ~]$ping6 fe80::2487:93ff:fe9a:c546%port-mgt
PING fe80::2487:93ff:fe9a:c546%port-mgt(fe80::2487:93ff:fe9a:c546%port-mgt) 56 data bytes
64 bytes from fe80::2487:93ff:fe9a:c546%port-mgt: icmp_seq=1 ttl=64 time=0.443 ms
64 bytes from fe80::2487:93ff:fe9a:c546%port-mgt: icmp_seq=2 ttl=64 time=0.488 ms
^C
--- fe80::2487:93ff:fe9a:c546%port-mgt ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.443/0.465/0.488/0.031 ms

```

注意这里的 IPv6 的格式，前面是 IPv6 地址，后面是本地网络接口名称，如果是物理网卡则接物理网卡名称，如果是 OVS Port，则接 Port 名称。

既然地址可以连通，那么我们思考如何进行远程控制。

## SSH 远程连接

通常我们通过 IPv4 地址链接远程 Linux，通过如下方式：
```Bash
[root@node111 14:01:23 ~]$ssh 192.168.30.112
root@192.168.30.112's password: 
Last login: Fri Aug 17 12:15:52 2018 from 192.168.16.1
[root@node112 14:03:46 ~]$
```

我们尝试将上面的 IPv4 地址替换为 IPv6 地址试试看：

```Bash
[root@node111 14:04:55 ~]$ssh fe80::2487:93ff:fe9a:c546
ssh: connect to host fe80::2487:93ff:fe9a:c546 port 22: Invalid argument
[root@node111 14:05:10 ~]$
```

直接指定 IPv6 地址是无法识别的，那么我们按照 ping6 规则，加上网络接口名称试试看：
```Bash
[root@node111 14:05:10 ~]$ssh fe80::2487:93ff:fe9a:c546%port-mgt
root@fe80::2487:93ff:fe9a:c546%port-mgt's password: 
Last login: Fri Aug 17 14:04:56 2018 from fe80::d4b7:acff:fe2f:604e%ovsbr-mgt
[root@node112 14:03:46 ~]$
```

一切顺利，我们成功的登录到了远程的机器上，我们知道 Ansible 是通过 SSH 的方式远程控制的，具体是调用 Python 的 (paramiko)[https://github.com/paramiko/paramiko/] ，我们接下来配置 Ansible。

## Ansible 远程连接

Ansible Inventory 标准格式是：`IP  options` ，比如：
```Bash
[cluster]
fe80::58d3:16ff:fe43:ce77%port-mgt ansible_ssh_user=root ansible_ssh_pass=abc123
```

验证 Ansible 远程控制：

```Bash
[root@node111 14:11:14 ~]$ansible cluster -m raw -a 'uptime'
fe80::58d3:16ff:fe43:ce77%port-mgt | SUCCESS | rc=0 >>
 14:11:22 up 7 days, 23:15,  2 users,  load average: 1.55, 1.39, 1.23
Shared connection to fe80::58d3:16ff:fe43:ce77%port-mgt closed.
```

## 总结
只要注意在 IPv6 地址后加上本地网络接口名称就可以正确配置 IPv6 远程控制了。
