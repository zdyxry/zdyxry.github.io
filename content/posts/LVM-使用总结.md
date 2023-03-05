---
title: LVM 使用总结
date: 2019-03-29 22:42:27
tags:
- Linux
---


全称 Logical Volume Manager，逻辑卷管理，简单的说就是能将物理磁盘统一管理，在现在这个满大街都在谈论分布式存储的年代，已经很少有人关注和使用它了，毕竟如果买个公有云上的虚拟机，挂载磁盘都已经得到 TP999+ 的稳定性加持，扩容什么的也只是一句话的事，完全没必要使用 LVM 了。  
那么我今天为啥要写 LVM 呢，首先肯定是最近要使用它（清理它），其次，现在 RedHat 系列发行版仍将 LVM 作为系统安装的默认磁盘处理方式，对于我这种安装系统家常便饭的人，还是要了解下的。

本文不会包含 LVM 命令的使用。

## 概念

LVM 中有 3 个最重要的概念，分别是 PV，VG，LV，下面我分别来说一下：
### PV
Physical Volumes，物理卷，属于 LVM 中最底层的单元，通常介质为磁盘，或者磁盘上的某个分区，多个 PV 可以组成 VG（卷组）。

### VG
Volume Group，卷组，也是我们通常说的“池化”具体表现形式，VG 可以存在多个，我们可以根据具体的用途来划分 VG，来提供相应的性能保证，比如我们可以对 IO 密集型应用使用全 SSD 组成的 VG。

### LV
Logical Volume，逻辑卷，也就是 `LVM` 中的 `LV`，LVM 暴露出来供我们使用的逻辑（虚拟）卷。我们可以将其当做一个普通的磁盘使用，可以在其上进行分区，格式化，磁盘读写等操作。

## 优缺点

简单的介绍了 LVM 的概念，那么我们来说下 LVM 的优缺点：

### 优点：
* 随意扩（缩）容
* 在线迁移 LV（平时用处不多，主要在 P2V 场景下使用，也就是通常文章中提到的“企业上云”必要的操作）
* 快照，RAID 等高级功能

### 缺点

管理复杂，通常服务器上磁盘数量多，且磁盘类型未必能够统一（考虑大量公司中的利旧场景），那么我们管理起来就比较麻烦了，要针对所有磁盘创建 PV，然后加入到对应的 VG 中，最后再对外提供 LV，往往我们需要维护相应的功能来提供简单的借口供上层应用使用。


## LVM RAID vs mdadm

在上述的优点中，我们提到了 RAID 功能。相信大部分同学都了解 RAID 的概念，通常我们提到的 RAID 都是由相应硬件（存储控制器）来提供，如果没有硬件怎么办呢？我们可以通过 `mdadm` 来实现软 RAID， 可以达到相应的效果，只是根据 OS 版本不同，软 RAID 的稳定性堪忧（Ubuntu 18.04 存在 Bug）。

那么同样都提供了软 RAID 功能，LVM 与 mdadm 相比，有什么不同呢？

首先，LVM 实现了完整的 RAID 功能，且 RedHat 也提供了完整的文档来描述各个功能的使用，是可以确定获得了官方支持的，那么社区里是怎么评论的呢？

从使用上来说，LVM 作为一款逻辑卷管理软件，虽然支持完成的软 RAID 功能，但是社区支持并不好，大家还是习惯于（信任）mdadm，毕竟 `Do One Thing and Do It Well` 准没错。mdadm 虽然我在使用上觉得很糟糕，但是在线上环境的表现，还是很完美的，目前 RAID1 还没出过问题，稳。

而且从性能上说，有人对 LVM 和 mdadm 进行过[性能对比](https://www.fibrevillage.com/storage/429-performance-comparison-of-mdadm-raid0-and-lvm-striped-mapping)，总体来说 mdadm 综合表现还是要比 LVM 好一些的。

（最近在对 nvme 磁盘进行分区 raid1 时经常遇到失败的情况，现象是mdadm 进程自己退出，再次执行又 ok，还没仔细调研。）


## 总结

虽然现在分布式存储大火，各家云产品都在使用，但是单机磁盘管理上，LVM 还是很好用的，RedHat 也一直在单机磁盘管理上有所投入，比如在 RedHat7.5 上推出的 [VDO 功能](https://github.com/dm-vdo/vdo)，还是要持续关注了解的。

## 参考链接
* https://github.com/dm-vdo/vdo
* https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/logical_volume_manager_administration/
* https://serverfault.com/questions/217666/what-is-better-lvm-on-raid-or-raid-on-lvm
* https://www.fibrevillage.com/storage/429-performance-comparison-of-mdadm-raid0-and-lvm-striped-mapping
* https://www.reddit.com/r/linux/comments/2pkqh2/is_it_better_to_use_mdadm_raid_lvm_or_just/
* http://www.cyberphoton.com/questions/question/what-is-the-difference-between-lvm-and-raid
* https://unix.stackexchange.com/questions/140321/mixed-raid-types/140325#140325
* https://serverfault.com/questions/126851/linux-lvm-mirror-vs-md-mirror
* https://unix.stackexchange.com/questions/150644/raiding-with-lvm-vs-mdraid-pros-and-cons
