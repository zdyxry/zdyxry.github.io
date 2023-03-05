---
title: 邻居发现协议（NDP）简易实现
date: 2019-12-11 21:29:59
tags:
- Linux
- Network
---


## 背景

在做节点管理时，经常面临节点自动扫描，自动关联等功能，这时候需要 NDP 来帮助我们来完成，关于 NDP 的实现有几种方式，今天来聊一下这个。

## 邻居发现协议（NDP）

引用维基百科的介绍：

> The Neighbor Discovery Protocol (NDP, ND)[1] is a protocol in the Internet protocol suite used with Internet Protocol Version 6 (IPv6). It operates at the link layer of the Internet model (RFC 1122), and is responsible for gathering various information required for internet communication, including the configuration of local connections and the domain name servers and gateways used to communicate with more distant systems.[2]

这里有两点需要关注：
1. 与 IPv6 一起使用
2. 工作在数据链路层（link layer）


### IPv6 地址

在 IPv6 中，无论我们的网络环境是否存在 DHCP Server，我们只要配置网卡启动 IPv6 选项，将网卡置为 active 状态，就能获取到对应的 IPv6 地址，这是因为 IPv6中支持 IP 自动配置，大概流程如下：

1. 根据 MAC 地址产生链路本地地址（link-local address）
2. 发出邻居发现请求，进行重复地址检测，如果重复，则停止配置
3. 链路本地地址生效，发送路由请求报文（RS）

#### 单播地址

单播地址中又分为三类：
1. 可聚合的全局单播地址，相当于公网 IPv4 地址
2. 链路本地地址，相当于IPv4里面的169.254.0.0/16地址，一般自动生成
3. 独特本地单播地址

#### 组播地址

IPv6 常用组播地址 | IPv4 常用组播地址 | 组播组
--- | --- | --- 
节点-本地范围 | 节点-本地范围| 节点-本地范围
FF01::1 | 224.0.0.1 | 所有-节点地址
FF01::2 | 224.0.0.2 | 所有-路由器地址
链路-本地范围 | 链路-本地范围 | 链路-本地范围
FF02::1 | 224.0.0.1 | 所有-节点地址
FF02::2 | 224.0.0.2 | 所有-路由器地址
FF02::5 | 224.0.0.5 | OSPF IGP
FF02::6 | 224.0.0.6 | OSPF IGP DR

#### 任播地址

在 IPv6 中，没有广播的概念，而是使用任播代替。在任播中，网络地址与网络节点之前存在一对多的关系：每一个地址对应一群接收节点，但是在任何给定时间，只有其中之一可以接收到传送端发来的信息。


邻居发现协议 NDP 是 IPv6 协议体系中一个重要的基础协议，替代了IPv4的 ARP 和 ICMP 路由器发现，定义了使用 ICMPv6 报文实现地址解析、跟踪邻居状态、重复地址检测、路由器发现以及重定向等功能。


## IPv6 地址发现

因为我本人也没有完整阅读过相应 RFC 文档，在这里也不详细描述每个报文的具体格式及每个字段是什么意思了，直接看看怎么实现。

### ping6 & 组播


如果我们知道了一个主机的 IPv6 地址，我们可以通过 `ping6` 来检测是否联通：

```shell
root@localhost:/tmp/nnn
 $ ping6 fe80::5054:ff:fe80:95d9%eth0
PING fe80::5054:ff:fe80:95d9%eth0(fe80::5054:ff:fe80:95d9%eth0) 56 data bytes
64 bytes from fe80::5054:ff:fe80:95d9%eth0: icmp_seq=1 ttl=64 time=0.045 ms
64 bytes from fe80::5054:ff:fe80:95d9%eth0: icmp_seq=2 ttl=64 time=0.055 ms
^C
--- fe80::5054:ff:fe80:95d9%eth0 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 999ms
rtt min/avg/max/mdev = 0.045/0.050/0.055/0.005 ms
```

那么有了这个 `ping6` 命令和上面提到的组播地址，我们就可以通过 `ping6` 直接 ping 组播地址就能知道那些地址可以联通了，那么应该选择哪个？应该选择 `FF01::1` ，因为我们想要实现的是获取 IPv6 地址：

```shell
root@localhost:/tmp/nnn
 $ ping6 -c1 -I eth0 'ff02::1%eth0'
PING ff02::1%eth0(ff02::1%eth0) from fe80::5054:ff:fe80:95d9%eth0 eth0: 56 data bytes
64 bytes from fe80::5054:ff:fe80:95d9%eth0: icmp_seq=1 ttl=64 time=0.045 ms

--- ff02::1%eth0 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.045/0.045/0.045/0.000 ms
```

因为我的实验环境里节点太多，这里使用 `-c` 参数限制发送 ECHO_REQUEST 包的数量为 1。

在发送组播之后，如果能够联通，那么系统会记录对应的 ARP 信息，我们可以通过 `ip` 命令直接获取：

```shell
root@localhost:/tmp/nnn
 $ ip -6 neighbor show dev eth0 | head -n 5
fe80::8c6e:a0ff:fe19:f146 lladdr 8e:6e:a0:19:f1:46 DELAY
fe80::8010:f1ff:fe02:af40 lladdr 82:10:f1:02:af:40 DELAY
fe80::baca:3aff:feec:fdac lladdr b8:ca:3a:ec:fd:ac DELAY
fe80::f11c:e35a:912:dbc9 lladdr 52:54:00:0a:b3:fc DELAY
fe80::570d:aa51:dc3b:1f02 lladdr 00:50:56:9b:f6:6c DELAY
```

这样就拿到了自己节点在二层联通的所有 IPv6 地址了。

#### Nmap

既然已经使用了 `ping6`，那么可以使用一些更高级的工具，比如 Nmap，Nmap可以检测目标主机是否在线、端口开放情况、侦测运行的服务类型及版本信息、侦测操作系统与设备类型等信息。 它通常用来评估网络系统安全。


```shell
root@localhost:/tmp/nnn
 $ nmap -6 "--script=targets-ipv6-multicast-*" | head -n 10

Starting Nmap 6.40 ( http://nmap.org ) at 2019-12-12 07:22 CST
Pre-scan script results:
| targets-ipv6-multicast-echo:
|   IP: fe80::e4a5:4fff:fea7:79af  MAC: e6:a5:4f:a7:79:af  IFACE: eth0
|   IP: fe80::250:56ff:fe85:647e   MAC: 00:50:56:85:64:7e  IFACE: eth0
|   IP: fe80::250:56ff:fe9e:2473   MAC: 00:50:56:9e:24:73  IFACE: eth0
|   IP: fe80::ae53:a418:ca0:83e8   MAC: 00:50:56:9f:43:ca  IFACE: eth0
|   IP: fe80::250:56ff:fe9e:bcb6   MAC: 00:50:56:9e:bc:b6  IFACE: eth0
|   IP: fe80::250:56ff:fe9f:6153   MAC: 00:50:56:9f:61:53  IFACE: eth0
WARNING: No targets were specified, so 0 hosts scanned.
```


## 更进一步

往往我们的需求不只是获取到 IP 这么简单，我们现在更进一步，我们要求扫描的结果中与我们预期的版本相同，那么此时就需要与对应节点进行通信了。

### HTTP

一个比较简单的实现，就是在目标节点开机的时候自动启动一个 API server，提供一个 Entrypoint，比如：

```python
#!/usr/bin/python

from flask import jsonify
from flask import Flask
app = Flask(__name__)

@app.route('/api/v1/version')
def version():
    return jsonify({"version":"v1.0.0"})

if __name__ == '__main__':
    app.run(host='::', port=5000, debug=True) # 要兼容 IPv6
```

然后我们可以在得到 IPv6 地址后，通过 curl 或者 Python urllib2 来发送对应的请求：

```shell
root@localhost:/tmp/nnn
 $ curl -g -6 'http://fe80::5054:ff:fe80:95d9%eth0:5000/api/v1/version'
{
  "version": "v1.0.0"
}#
```


```python
>>> import urllib2
>>> res = urllib2.urlopen("http://fe80::5054:ff:fe80:95d9%eth0:5000/api/v1/version")
>>> res.read()
'{\n  "version": "v1.0.0"\n}'
```

这样虽然可以达到我们想要的效果，但是效率太低了，要先后进行2次操作，一次是扫描对应的 IPv6 地址，一次是得到地址后进行 HTTP 请求。

### Socket

我们可以通过 socket 通信来达到类似的效果，与 HTTP 不同的是，我们可以直接使用 socket 发送组播，来进行消息传递，这样上面的两步就可以通过一步来解决了，这里给出对应的 server 和 client 代码示例：

#### Server

```python
import socket
import select
import json


def server():
    try:
        s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', 30000))
        s.setblocking(False)
        while True:
            rlist, _, _ = select.select([s], [], [s], 1)
            if rlist:
                string, address = s.recvfrom(20000)
                print string, address
                try:
                    data = json.loads(string)
                except Exception:
                    pass
                owner = data.get("owner")
                if owner == "yiran":
                    info = {"version": "v1.0",
                            "owner": "yiran",
                            "nic": address[0].split("%", 1)[1]}
                    s.sendto(json.dumps(info), address)
    except Exception:
        pass


if __name__ == "__main__":
    server()
```

#### Client

```python
import json
import select
import socket

from pprint import pprint


def client():
    s= socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 5000000)
    nics = socket.getaddrinfo("%s%%%s" % ('ff02::1', 'eth0'), 30000, socket.AF_INET6, socket.SOCK_DGRAM)
    data = {"owner": "yiran"}
    string = json.dumps(data)
    results = {}
    for i in range(10):
        for nic in nics:
            _, _, _, _, address = nic
            try:
                s.sendto(string, address)
            except Exception:
                pass

        rlist, _, _ = select.select([s], [], [s], 1)
        if rlist:
            json_string, address = s.recvfrom(10000)
            results[address] = json_string

    s.close()
    ips = []
    for address, json_test in results.iteritems():
        try:
            data = json.loads(json_test)
            if data.get("version", None) == "v1.0":
                info = {}
                info['ipv6_address'] = address[0]
                info['test'] = data

                ips.append(info)
        except Exception:
            pass

    return ips


if __name__ == "__main__":
    pprint(client())
```



## 参考链接

* http://www.ruijie.com.cn/fa/xw-hlw/83116/
* https://tools.ietf.org/html/rfc4861
* https://security.stackexchange.com/questions/12826/which-tool-apart-from-nmap-can-i-use-to-scan-a-range-of-ipv6-addresses