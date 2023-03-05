---
title: Traceroute 简易实现
date: 2018-11-18 12:33:35
tags:
- Linux
- Network
---

## 背景

在平时遇到网络问题时，我们通常会使用 `ping`,`route`,`ip` 等命令去 debug，当我们确定我们本机的网络配置及服务没有问题后，我通常会使用 `traceroute` 来判断网络走向。

最近公司搬家之后，整体网络架构进行了改进，随着配置的复杂化，稳定性相较于原来有了很大的下降，导致最近频繁使用 `traceroute`，一直使用它却不知道是怎么工作的，研究了一下，作为总结。


## Traceroute 

先上维基百科的解释：
>traceroute，现代Linux系统称为tracepath，Windows系统称为tracert，是一种计算机网络工具。它可显示数据包在IP网络经过的路由器的IP地址。

我们通常使用无需特殊配置，直接用 traceroute 加上我们的目标地址即可，如：  

```bash
root@yiran-workstation:~ 
 $ traceroute 192.168.16.1
traceroute to 192.168.16.1 (192.168.16.1), 30 hops max, 60 byte packets
 1  gateway (192.168.8.1)  19.469 ms  19.089 ms  18.911 ms
 2  192.168.1.201 (192.168.1.201)  11.539 ms  11.423 ms  11.307 ms
 3  192.168.16.1 (192.168.16.1)  18.289 ms  18.184 ms  18.064 ms
```

当我们想设置 TTL 数值时，我们可以使用 `-m` 参数:  
```bash
root@yiran-workstation:~ 
 $ traceroute 192.168.16.1 -m 2
traceroute to 192.168.16.1 (192.168.16.1), 2 hops max, 60 byte packets
 1  gateway (192.168.8.1)  20.914 ms  20.700 ms  20.616 ms
 2  192.168.1.201 (192.168.1.201)  20.497 ms  20.465 ms  20.383 ms
```

实现原理：
> 主叫方首先发出 TTL=1 的数据包，第一个路由器将 TTL 减1得0后就不再继续转发此数据包，而是返回一个 ICMP 逾时报文，主叫方从逾时报文中即可提取出数据包所经过的第一个网关地址。然后又发出一个 TTL=2 的 ICMP 数据包，可获得第二个网关地址，依次递增 TTL 便获取了沿途所有网关地址。

>需要注意的是，并不是所有网关都会如实返回 ICMP 超时报文。出于安全性考虑，大多数防火墙以及启用了防火墙功能的路由器缺省配置为不返回各种 ICMP 报文，其余路由器或交换机也可被管理员主动修改配置变为不返回 ICMP 报文。因此 Traceroute 程序不一定能拿全所有的沿途网关地址。所以，当某个 TTL 值的数据包得不到响应时，并不能停止这一追踪过程，程序仍然会把 TTL 递增而发出下一个数据包。一直达到默认或用参数指定的追踪限制（maximum_hops）才结束追踪。

这里要说明一下，加入我们去 traceroute 最常用的 baidu.com，就会看到这个现象，traceroute 命令的结果中包含 `* * *` ，我也没有找到一个较为明确的解释，猜测这个节点禁止了 ping 或其他配置，无法返回 ICMP 超时报文，导致 traceroute 无法正常解析。

```bash
master ✗ $ traceroute  baidu.com -m 20 
traceroute to baidu.com (220.181.57.216), 20 hops max, 60 byte packets
 1  gateway (192.168.8.1)  18.535 ms  18.456 ms  29.185 ms
 2  10.1.1.1 (10.1.1.1)  6.599 ms  6.533 ms  6.378 ms
 3  106.38.14.1 (106.38.14.1)  28.707 ms  28.606 ms  28.514 ms
 4  5.0.142.219.broad.bj.bj.dynamic.163data.com.cn (219.142.0.5)  28.384 ms  28.305 ms  28.205 ms
 5  * * *
 6  36.110.244.46 (36.110.244.46)  37.131 ms  31.660 ms  31.489 ms
 7  * * *
 8  220.181.17.94 (220.181.17.94)  10.700 ms 220.181.17.146 (220.181.17.146)  10.511 ms 220.181.17.150 (220.181.17.150)  10.336 ms
 9  * * *
10  * * *
11  * * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
```

>依据上述原理，利用了 UDP 数据包的 Traceroute 程序在数据包到达真正的目的主机时，就可能因为该主机没有提供 UDP 服务而简单将数据包抛弃，并不返回任何信息。为了解决这个问题，Traceroute 故意使用了一个大于 30000 的端口号，因 UDP 协议规定端口号必须小于 30000 ，所以目标主机收到数据包后唯一能做的事就是返回一个“端口不可达”的 ICMP 报文，于是主叫方就将端口不可达报文当作跟踪结束的标志。

## 简易实现

源地址： https://github.com/dnaeon/pytraceroute
对整个实现中最重要的部分做下注释：

```python
# Copyright (c) 2015 Marin Atanasov Nikolov <dnaeon@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer
#    in this position and unchanged.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR(S) ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Core module

"""

import socket
import random
import struct
import time

__all__ = ['Tracer']


class Tracer(object):
    def __init__(self, dst, hops=30):
        """
        Initializes a new tracer object

        Args:
            dst  (str): Destination host to probe
            hops (int): Max number of hops to probe

        """
        self.dst = dst # 目标地址：域名或 IPv4 地址
        self.hops = hops 
        self.ttl = 1

        # Pick up a random port in the range 33434-33534
        # 对应上述解释，随机选择一个 > 30000 的端口用于连接
        self.port = random.choice(range(33434, 33535))

    def run(self):
        """
        Run the tracer

        Raises:
            IOError

        """
        try:
            dst_ip = socket.gethostbyname(self.dst) # 解析域名
        except socket.error as e:
            raise IOError('Unable to resolve {}: {}', self.dst, e)

        text = 'traceroute to {} ({}), {} hops max'.format(
            self.dst,
            dst_ip,
            self.hops
        )

        print(text)

        while True:
            startTimer = time.time()
            receiver = self.create_receiver() # 创建接收 socket 实例
            sender = self.create_sender() # 创建发送 socket 实例
            sender.sendto(b'', (self.dst, self.port)) # 向目标地址指定端口发送报文

            addr = None
            try:
                data, addr = receiver.recvfrom(1024) # 获取发送 ICMP 超时报文，并解析地址
                entTimer = time.time()
            except socket.error:
                pass
                # raise IOError('Socket error: {}'.format(e))
            finally:
                receiver.close()
                sender.close()

            if addr: # 如果获取到地址，则打印相应信息及用时
                timeCost = round((entTimer - startTimer) * 1000, 2)
                print('{:<4} {} {} ms'.format(self.ttl, addr[0]), timeCost)
                if addr[0] == dst_ip:
                    break
            else:
                print('{:<4} *'.format(self.ttl))

            self.ttl += 1 # 增加 TTL，获取下一跳地址

            if self.ttl > self.hops:
                break

    def create_receiver(self):
        """
        Creates a receiver socket

        Returns:
            A socket instance

        Raises:
            IOError

        """
        s = socket.socket(
            family=socket.AF_INET, # 指定 proto family 为 IPv4
            type=socket.SOCK_RAW, # 指定接收 socket 类型为 raw，这里是因为普通的 socket 类型无法处理 ICMP 报文
            proto=socket.IPPROTO_ICMP # 指定 socket 协议为 ICMP 协议，type 与 proto 需要特定的组合，不允许任意配置
        )

        timeout = struct.pack("ll", 5, 0)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)

        try:
            s.bind(('', self.port))
        except socket.error as e:
            raise IOError('Unable to bind receiver socket: {}'.format(e))

        return s

    def create_sender(self):
        """
        Creates a sender socket

        Returns:
            A socket instance

        """
        s = socket.socket(
            family=socket.AF_INET, # 指定 proto family 为 IPv4
            type=socket.SOCK_DGRAM, # 指定发送的类型为 UDP，即发送广播消息
            proto=socket.IPPROTO_UDP # 指定协议为 IP UDP 
        )

        s.setsockopt(socket.SOL_IP, socket.IP_TTL, self.ttl)

        return s

```



## 总结
了解了实现原理之后，希望之后排查网络问题应该也会得心应手一些吧。
也希望自己能更多的关注于 Why，而不是 How。


## 参考链接
* http://dnaeon.github.io/traceroute-in-python/
* https://www.nljb.net/default/SOCK_STREAM%E4%B8%8ESOCK_DGRAM%E7%9A%84%E5%8C%BA%E5%88%AB/
* https://stackoverflow.com/questions/1955198/when-is-ipproto-udp-required
* https://blog.csdn.net/newnewman80/article/details/8000404
* http://www.zmonster.me/notes/tcp-ip-socket-in-c.html
* http://courses.cs.vt.edu/cs4254/fall04/slides/raw_6.pdf
