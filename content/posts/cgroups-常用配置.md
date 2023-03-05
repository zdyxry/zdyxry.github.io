---
title: cgroups 常用配置
date: 2018-09-23 11:40:19
tags:
- Linux
- cgroups
---


## 背景
在软件运行过程中，我们经常需要限制 CPU 、内存、磁盘的使用，方式程序超出了限定边界范围。在 Linux 中，我们可以通过 cgroups 来进行限制。

## cgroups
中文名称为控制组群，具体功能分类为：
*   资源限制：组可以被设置不超过设定的内存限制；这也包括虚拟内存。
*   优先级：一些组可能会得到大量的CPU或磁盘IO吞吐量。
*   结算：用来衡量系统确实把多少资源用到适合的目的上。
*   控制：冻结组或检查点和重启动。

下面来说下常见的使用方式

### CPU
RedHat 官方文档中描述 cgroups 在 RHEL7/CentOS7 之后的版本需要通过 systemd 配置，不再使用 libcgconfig 方式。
但是在 systemd 的配置中，CPU 相关的配置项比较简单，或者说 OS 自动配置了很多，没有暴露出来。所以我们这里还是采用 libcgconfig 的配置方式。

在进行 CPU 限制之前，我们需要了解一下 NUMA 结构。什么是 NUMA？ NUMA 是一种为多处理器的计算机设计的内存，内存访问时间取决于内存相对于处理器的位置。在NUMA下，处理器访问它自己的本地内存的速度比非本地内存快一些。
不同的 Thread 在同一个 Core 上也会发生抢占情况，具体可以通过 sysbench 进行测试。

相关概念定义：
1. Socket：物理服务器上的 CPU 插槽
2. Core：物理 CPU 核心数
3. Thread：超线程

简单的说就是如果你的程序是计算密集型，那么尽可能的要让 CPU 限制在同一个 NUMA node 上。
查看 NUMA node 方式：
```bash
[root@test 10:53:43 ~]$numactl -H
available: 2 nodes (0-1)
node 0 cpus: 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
node 0 size: 65221 MB
node 0 free: 52239 MB
node 1 cpus: 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31
node 1 size: 65536 MB
node 1 free: 57566 MB
node distances:
node   0   1
  0:  10  21
  1:  21  10
```

这台服务器的配置为 2(socket) * `Intel(R) Xeon(R) Silver 4110 CPU @ 2.10GHz` ，内存为 128 GB。观察 NUMA node  分配，可以看到分为两个 node，分别为 node 0 和 node 1。
那么 `node $index cpus` 字段代表的是什么意思呢？ 在这里对应的是两个 socket ，也就是两个物理插槽上的 CPU 对应的 Thread。 Thread 排序方式是优先按照不同 Core 排序的，比如 Thread 0 在 Core 0 上，Thread 2 在 Core 1 上，以此类推。
具体的 CPU 配置大家可以通过 `lscpu` ， 或者查看 `/proc/cpuinfo` 了解。

根据 NUMA 配置，我们可以选择将程序限制在 Thread 0,2,4,6,8 上。
那么我们编辑配置文件 `/etc/cgconfig.conf`  

```bash
[root@test 11:03:45 ~]$cat /etc/cgconfig.conf |head -n 25
# yiran cgroups configuration

group . {
    cpuset {
        cpuset.memory_pressure_enabled = "1";
    }
}

group yiran {
    cpuset {
        cpuset.cpus = "0,2,4,6,8";
        cpuset.mems = "0-1";
        cpuset.cpu_exclusive = "1";
        cpuset.mem_hardwall = "1";
    }
}

group yiran/flask {
    cpuset {
        cpuset.cpus = "0,2,4";
        cpuset.mems = "0-1";
        cpuset.cpu_exclusive = "0";
        cpuset.mem_hardwall = "1";
    }
}
```

 首先，我们定义了一个组，组名叫 `yiran`，我们又在 `yiran` 下创建了一个叫 `flask` 的组，限制 CPU在 `0,2,4` 上。
接下来我们重启 cgconfig 相关服务，注意遵守重启顺序：
```bash
[root@test 11:04:45 ~]systemctl restart cgconfig
[root@test 11:04:46 ~]systemctl restart cgred
```

我们可以通过 lscgroup 检测配置是否生效，或者通过查看 `/proc/$pid/cgroup` 检查。

### 内存

相对于 CPU，内存配置我们可以直接通过 systemd 配置，就简化很多了。
最简单的，如果我们想立即配置一个服务的内存限制，我们可以直接执行命令：
```bash
[root@test 11:05:50 ~]systemctl set-property <service name> MemoryLimit=500M
```

执行完这条命令后，系统会自动在该服务的 systemd 配置路径(`/etc/systemd/system/<service name>.d/` 下生成文件 `50-MemoryLimit.conf` ，文件内容为：
```bash
[Slice]
MemoryLimit=5368709120
```

当然我们如果直接在该路径下编写配置文件也是可以的，重启服务后生效。

#### Slice 配置
上面这种方式只是针对单一的服务配置，如果我们想创建一个组，控制多个服务计算资源总和的配置，我们就需要通过配置 Slice 完成。

**slice** —— 一组按层级排列的单位。slice 并不包含进程，但会组建一个层级，并将 scope 和 service 都放置其中。真正的进程包含在 scope 或 service 中。在这一被划分层级的树中，每一个 slice 单位的名字对应通向层级中一个位置的路径。小横线（"`-`"）起分离路径组件的作用。例如，如果一个 slice 的名字是：

_parent_-_name_.`slice`

这说明 _parent_-_name_.`slice` 是 _parent_.`slice` 的一个子 slice。这一子 slice 可以再拥有自己的子 slice，被命名为：_parent_-_name_-_name2_.`slice`，以此类推。

根 slice 的表示方式：`-.slice` 

我们在 `/etc/systemd/system/` 下创建一个组，名称还是 `yiran` ，创建 `flask` 在 `yiran` 下：
```bash
/etc/systemd/system
├── flask.service.d
│   └── cgroup.conf
├── system-yiran.slice
├── system-yiran.slice.d
│   └── 50-MemoryLimit.conf
```

配置完成后，我们重启 cgconfig 相关服务即可使能配置。


### 磁盘

如要降低 flask 服务读取某个目录 block IO 的权重，只需要修改该服务配置文件 增加 `BlockIODeviceWeight=/home/jdoe 750` 字段即可。

## 后续
日常用到最多的应该就是 CPU 和内存，如果很多对 IO 要求高的服务运行在一块磁盘上，那么可以先通过针对不同服务进行不同磁盘分区的方式（此方式不包括 lvm）验证，如果还不能解决的话，再考虑针对服务控制磁盘 IO。

为了追求性能，我们在 CPU 配置的时候给应用程序分配的 Thread 都位于同一个 Socket 上 CPU 的不同的 Core 上。 老板说还要考虑网卡、磁盘等 PCI 设备接入的 Socket ，如果应用程序分配在了 NUMA node0 上，但是网卡、磁盘等 PCI 设备连接在了 NUMA node1 上，还是会对性能有影响，还没找到相应配置，后续有时间再了解吧。

## 参考链接

* https://access.redhat.com/documentation/zh-cn/red_hat_enterprise_linux/7/html/resource_management_guide/
* https://www.kernel.org/doc/Documentation/cgroup-v1/
* https://www.kernel.org/doc/Documentation/cgroup-v2.txt
