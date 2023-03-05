---
title: Wireguard 体验
date: 2019-03-23 20:13:38
tags:
- Wireguard
---

从春节假期之后，因为一些原因，就没有再使用 SS 作为访问互联网的工具了，而是使用了 V2ray，使用 2个月下来，感受还是很好的，无论是速度还是稳定性都要比 SS 好很多。最近看到好多新闻说 Wireguard 客户端适配多了起来，比如 Win，Mac，Android，今天尝试一下。

## Wireguard

> WireGuard is a free and open-source software application and protocol that implements virtual private network (VPN) techniques to create secure point-to-point connections in routed or bridged configurations. It is run as a module inside the Linux kernel and aims for better performance than the IPsec and OpenVPN tunneling protocols.[2] 

Linus 的评价： `Maybe the code isn't perfect, but I've skimmed it, and compared
to the horrors that are OpenVPN and IPSec, it's a work of art.`  

## 服务端配置

### kernel 配置
环境配置为：`CentOS Linux release 7.6.1810 (Core)`  

Kernel 版本： `4.20.3-1.el7.elrepo.x86_64`

安装 `kernel-devel kernel-headers`，注意，如果使用的是 `elrepo` 源，则需要安装对应版本的 `kernel-ml-devel kernel-ml-headers` ， 安装后状态：

```bash
# rpm -qa |grep kernel  |grep "4.20"
kernel-ml-4.20.3-1.el7.elrepo.x86_64
kernel-ml-devel-4.20.3-1.el7.elrepo.x86_64
kernel-ml-headers-4.20.3-1.el7.elrepo.x86_64
```

### 安装 wireguard 

`yum install wireguard-dkms wireguard-tools`

加载 Kernel module

`modprobe wireguard && lsmod |grep wire`

### 编辑 wireguard 配置文件

通过 `ip ad` 查看本机网卡名称，以 `eth0` 为例：

```bash
#mkdir /etc/wireguard && cd /etc/wireguard
# wg genkey # 生成 Private Key
#cat > /etc/wireguard/wg0.conf << EOF
[Interface]
PrivateKey = <Private Key>
Address = 10.0.0.1/24 # 服务端 IP 地址
ListenPort = 11111 # 连接端口
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE; ip6tables -A FORWARD -i wg0 -j ACCEPT; ip6tables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE; ip6tables -D FORWARD -i wg0 -j ACCEPT; ip6tables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
SaveConfig = true

EOF
```

### 启动服务
```bash
#wg-quick up wg0
#wg
interface: wg0
  public key: YNyypVL5wmYA/aaaaaa/VOz4c7BGALHgo= # 后续配置客户端用到
  private key: (hidden)
  listening port: 11111

# ip ad
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 
3: wg0: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 1420 qdisc noqueue state UNKNOWN group default qlen 1000
    link/none
    inet 10.0.0.1/24 scope global wg0
       valid_lft forever preferred_lft forever
```

## 客户端配置

### 配置文件

```bash
# wg genkey # 生成客户端 PublicKey
[Interface]
PublicKey = <PublicKey>
Address = 10.0.0.2/24 # 客户端 IP 地址
DNS = 8.8.8.8 # 指定 DNS Server

[Peer]
PublicKey = YNyypVL5wmYA/aaaaaa/VOz4c7BGALHgo= # 服务端公钥
Endpoint = <Server ip>:11111 # 服务端公网 IP，端口为服务端配置端口
AllowedIPs = 0.0.0.0/0 # 允许 IP 段
```

### 服务端添加客户端信息

```bash
#wg set wg0 peer <客户端公钥> allowed-ips 10.0.0.2/24
## wg
interface: wg0
  public key: YNyypVL5wmYA/aaaaaa/VOz4c7BGALHgo=
  private key: (hidden)
  listening port: 11111

peer: QRcE0sLvJib8MhWxxxxxxxxx61L0IdZis=
  endpoint: xxxxxxx:yyy
  allowed ips: 10.0.0.0/24
  latest handshake: 1 minute, 9 seconds ago
  transfer: 3.61 MiB received, 92.67 MiB sent
```

## 检查

在服务端查看主机路由信息：
```bash
# ip route show
default via 111.111.111.1 dev eth0
10.0.0.0/24 dev wg0 proto kernel scope link src 10.0.0.1
```

可以看到已经添加的 wireguard 网络默认路由是通过 10.0.0.1，所以我们需要开启地址转发功能：
```bash
#cat /etc/sysctl.conf
net.ipv4.ip_forward = 1
# sysctl -p
```

此时在服务端 ping 客户端 IP，也就是 10.0.0.2 ，检查状态：
```bash
# ping 10.0.0.2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=334 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=335 ms
```

已经看到可以联通了。

整体上来说 Wireguard 配置上很简单，没有过多的配置文件，只是目前非 Linux 客户端都处于开发阶段，不推荐使用，尝鲜还是可以的。

## 配置文件示例

wg0

```
[Interface]
PrivateKey = 6G2jd1VVCRofQzkLxxxxxxxxxxxxx/3GJFTjzwxz62k=
Address = 10.0.0.1/24
PostUp   = echo 1 > /proc/sys/net/ipv4/ip_forward; iptables -A FORWARD -i wg0 -j ACCEPT; iptables -A FORWARD -o wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -D FORWARD -o wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
ListenPort = 11111
DNS = 8.8.8.8
MTU = 1420

[Peer]
PublicKey = nMUQDNdDMtMLslqmLpe/j9qqGNdJMxxxxxxxxxu5NjA=
AllowedIPs = 10.0.0.3/32
```


client.conf

```
[Interface]
PrivateKey = 8LnMNxNlvxZnnnBkMpd/hFl1xxxxxxxxxxW+5D4qUk=
Address = 10.0.0.3/24
DNS = 8.8.8.8
MTU = 1420

[Peer]
PublicKey = QWhJChuDG7HdNnSF4ximOoxxxxxxxxxxitl1mzIjo=
Endpoint = 114.187.221.217:11111
AllowedIPs = 0.0.0.0/0, ::0/0
PersistentKeepalive = 25
```
