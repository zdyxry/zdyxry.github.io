---
title: OpenvSwitch Active-Backup failback 验证
date: 2018-09-24 17:36:22
tags:
- OpenvSwitch
---

## 背景
在虚拟化场景下，我们经常使用  OpenvSwitch 进行虚拟网络配置，最近看到有人问，Open vSwitch 的 bonding 模式 Avtice-Backup ，是否支持 failback 功能？ 虽然一直经常使用该模式，但是不知道当故障恢复后，是否会出现故障恢复？
看官方文档中描述感觉有些模糊，来验证下。

## 验证方式
### 配置 VDS
```bash
[root@node 17:14:54 ~]$ovs-vsctl show
b9956069-4101-4aab-a8a2-86db4f5ae390
    Bridge ovsbr-mgt
        Port bond-mgt
            Interface "eno2"
            Interface "eno1"
        Port port-mgt
            tag: 0
            Interface port-mgt
                type: internal
        Port ovsbr-mgt
            Interface ovsbr-mgt
                type: internal
    ovs_version: "2.3.1"
```

```bash
[root@node 17:14:59 ~]$ovs-appctl bond/list
bond	type	recircID	slaves
bond-mgt	active-backup	0	eno1, eno2
```

### 故障前流量检测

```bash
[root@node 17:15:58 ~]$ifconfig eno1
eno1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::ec4:7aff:fe0f:8f68  prefixlen 64  scopeid 0x20<link>
        ether 0c:c4:7a:0f:8f:68  txqueuelen 1000  (Ethernet)
        RX packets 10046643  bytes 1131705628 (1.0 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4182418  bytes 443990895 (423.4 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device memory 0xdfd20000-dfd3ffff

[root@node 17:16:45 ~]$ifconfig eno2
eno2: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 0c:c4:7a:0f:8f:69  txqueuelen 1000  (Ethernet)
        RX packets 100  bytes 10240 (100 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 100  bytes 10240 (100 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device memory 0xdfd00000-dfd1ffff
```

### 故障后流量检测

```bash
[root@node 17:15:58 ~]$ifconfig eno1
eno1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::ec4:7aff:fe0f:8f68  prefixlen 64  scopeid 0x20<link>
        ether 0c:c4:7a:0f:8f:68  txqueuelen 1000  (Ethernet)
        RX packets 10046643  bytes 1131705628 (1.0 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4182418  bytes 443990895 (423.4 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device memory 0xdfd20000-dfd3ffff

[root@node 17:16:45 ~]$ifconfig eno2
eno2: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 0c:c4:7a:0f:8f:69  txqueuelen 1000  (Ethernet)
        RX packets 22222222  bytes 2231705628 (1.0 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2231705628  bytes 2231705628 (1.0 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device memory 0xdfd00000-dfd1ffff
```

### 故障恢复后流量检测

```bash
[root@node 17:15:58 ~]$ifconfig eno1
eno1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::ec4:7aff:fe0f:8f68  prefixlen 64  scopeid 0x20<link>
        ether 0c:c4:7a:0f:8f:68  txqueuelen 1000  (Ethernet)
        RX packets 10046643  bytes 1131705628 (1.0 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4182418  bytes 443990895 (423.4 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device memory 0xdfd20000-dfd3ffff

[root@node 17:16:45 ~]$ifconfig eno2
eno2: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 0c:c4:7a:0f:8f:69  txqueuelen 1000  (Ethernet)
        RX packets 33333333  bytes 3331705628 (1.0 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3331705628  bytes 3331705628 (1.0 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device memory 0xdfd00000-dfd1ffff
```


## 结论
可以看到整体流程中流量占用网口情况，主要看 RX 和 TX packets 数量：
1. 故障前：eno1
2. 故障后：eno2
3. 故障恢复后：eno2

在 OpenvSwitch Active-Backup 场景下，未支持 failback 功能，我理解是因为这两块网卡完全等价，failback 在 Master-Slave 场景下更有用一些。




