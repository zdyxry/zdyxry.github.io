---
title: cgroup 资源预留
date: 2018-12-18 21:15:33
tags:
- Linux
---

## cgroup 资源预留

## 背景
在之前的博客中，提到了 cgroup 中如何为自己的服务配置资源限制，比如 CPU，内存等，当时以为在 `cgroup.conf` 中配置的服务，那么相应绑定的 CPU 就归属于该服务，也就是资源预留，今天发现并不是这样，记录下如何通过 cgroup 做资源预留。

## 资源预留

在之前提到的博客中关于资源限制是这么配置的：
```bash
[root@node 20:56:49 ~]$cat /etc/cgconfig.conf
# yiran cgroups configuration

group . {
    cpuset {
        cpuset.memory_pressure_enabled = "1";
    }
}

group yiran {
    cpuset {
        cpuset.cpus = "0,1,2,3,4,5";
        cpuset.mems = "0-1";
        cpuset.cpu_exclusive = "1";
        cpuset.mem_hardwall = "1";
    }
}

group yiran/test {
    cpuset {
        cpuset.cpus = "0";
        cpuset.mems = "0-1";
        cpuset.cpu_exclusive = "1";
        cpuset.mem_hardwall = "1";
    }
}
```

我为 yiran 这个服务做了限制，其中分配给 `yiran/test` 的 CPU 是 `0`，并且配置了 `cpuset.cpu_exclusive` 选项。注意，这里的 exclusive 的意思并不是说分配到 `yiran/test` 中的服务独自占用该线程，而是说分配到 `yiran/test` 中的服务只会占用该线程，不会侵入到其他线程中，也就是通常我们说的 Limit。
可以通过 `stress` 命令来进行验证：
```bash
# 对一台配置好 cgroup 的物理服务器 CPU 加压
[root@node 21:05:37 ~]$stress -c 24
stress: info: [4033] dispatching hogs: 24 cpu, 0 io, 0 vm, 0 hdd
```

```bash
# 新开终端，执行 top 命令查看 CPU 情况
[root@node 21:05:37 ~]$top
top - 21:06:35 up 5 days,  9:03,  3 users,  load average: 32.58, 19.04, 15.43
Tasks: 449 total,  36 running, 412 sleeping,   0 stopped,   1 zombie
%Cpu0  : 89.0 us,  8.6 sy,  0.0 ni,  2.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu1  : 99.7 us,  0.3 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu2  : 90.4 us,  8.9 sy,  0.0 ni,  0.3 id,  0.3 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu3  : 95.4 us,  4.6 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu4  : 84.4 us, 13.6 sy,  0.3 ni,  1.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu5  : 46.5 us, 36.0 sy,  1.7 ni, 15.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu6  : 93.4 us,  6.6 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu7  : 94.4 us,  5.6 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu8  : 88.0 us, 12.0 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu9  : 88.7 us, 11.3 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu10 : 88.4 us, 10.9 sy,  0.0 ni,  0.3 id,  0.0 wa,  0.0 hi,  0.3 si,  0.0 st
%Cpu11 : 85.4 us, 13.9 sy,  0.7 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu12 : 98.7 us,  1.3 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu13 : 39.0 us, 12.0 sy,  0.0 ni, 49.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu14 : 92.7 us,  6.9 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.3 si,  0.0 st
%Cpu15 : 98.7 us,  1.3 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu16 : 97.0 us,  3.0 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu17 : 97.0 us,  2.3 sy,  0.0 ni,  0.3 id,  0.0 wa,  0.0 hi,  0.3 si,  0.0 st
%Cpu18 :100.0 us,  0.0 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu19 : 93.7 us,  6.3 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu20 : 88.4 us, 11.6 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu21 : 89.4 us, 10.6 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu22 : 88.1 us, 11.9 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu23 : 90.4 us,  9.6 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
```



那么我们如何确保自己的服务有足够的资源运行呢？ 比如像 vSphere ESXi 上面可以针对某些虚拟机进行具体的资源预留（CPU，内存，磁盘等）。
其实只要将其他资源也限制在一个 cgroup 中就可以了。  

1. 在 `/etc/cgconfig.conf` 中创建一个新的 cgroup，将系统上其余的资源分配给该 group，如创建 `yiran/others` 并分配 3个 线程；
2. 修改 `/etc/cgrules.conf` ，将系统其它所有服务分配到步骤1创建的 group 中，如：
```bash
*       cpuset       yiran/others
```

修改配置完成后，分别重启 `cgred` 和 `cgconfig` 使配置生效：
```bash
systemctl restart cgred
systemctl restart cgconfig
```

此时我们再通过 `stress` 进行验证
```bash
[root@node 21:09:29 ~]$stress -c 24
stress: info: [12475] dispatching hogs: 24 cpu, 0 io, 0 vm, 0 hdd
```

```bash
top - 21:11:58 up 5 days,  9:09,  3 users,  load average: 38.11, 30.37, 21.48
Tasks: 445 total,  38 running, 406 sleeping,   0 stopped,   1 zombie
%Cpu0  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu1  :100.0 us,  0.0 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu2  :  0.0 us,  0.0 sy,  0.3 ni, 99.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu3  :  0.0 us,  0.3 sy,  0.0 ni, 99.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu4  : 88.1 us, 11.9 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu5  : 81.9 us, 16.1 sy,  1.6 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.3 si,  0.0 st
%Cpu6  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu7  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu8  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu9  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu10 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu11 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu12 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu13 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu14 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu15 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu16 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu17 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu18 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu19 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu20 :  0.0 us,  0.0 sy,  0.3 ni, 99.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu21 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu22 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu23 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 13174792+total, 11522948+free,  6439344 used, 10079088 buff/cache
KiB Swap:        0 total,        0 free,        0 used. 12406676+avail Mem
```

  
我在 `yiran/others` 中配置了 3 个线程，那么此时哪怕我执行 `stress`  worker 为 24，也只会在这3个线程中，不会对其他 cgroup 服务产生干扰，从而达到了资源预留的效果。
