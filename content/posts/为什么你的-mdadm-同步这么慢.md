---
title: 为什么你的 mdadm 同步这么慢
date: 2019-11-15 20:20:03
tags:
- Linux
---


## 背景

自己一直通过 mdadm 在软件层面对多块磁盘进行 RAID1 配置，一个主要的原因是 mdadm 是 KickStart 默认软件。因为只是 RAID1，所以使用起来也是比较方便，虽然有些小坑，但总体来说还好。  
最近遇到一个问题， mdadm 在配置 RAID1 时，磁盘同步很慢。


## 现象

先说下磁盘构成，一般情况下是这样：

```bash
[root@yiran 20:23:48 ~]$lsblk
NAME      MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
sda         8:0    0  59.6G  0 disk
├─sda1      8:1    0   256M  0 part  /boot/efi
└─sda2      8:2    0   512M  0 part  /boot
sdb         8:16   0 223.6G  0 disk
└─sdb1      8:17   0    45G  0 part
  └─md127   9:127  0    45G  0 raid1 /
sdc         8:32   0 223.6G  0 disk
└─sdc1      8:33   0    45G  0 part
  └─md127   9:127  0    45G  0 raid1 /
```

两块 SSD 各自分区，并将第一个分区通过 mdadm 做 RAID1，保证系统分区高可用，分区大小是 45G，但是因为是 SSD 磁盘，所以速度也不会慢到哪去。

最近遇到的问题就是我觉得最不应该有问题的地方：同步速度很慢，非常慢，慢到离谱：

```bash
[root@yiran 20:28:00 ~]$mdadm -D /dev/md127
/dev/md127:
           Version : 1.2
     Creation Time : Thu Nov 14 10:06:52 2019
        Raid Level : raid1
        Array Size : 47153152 (44.97 GiB 48.28 GB)
     Used Dev Size : 47153152 (44.97 GiB 48.28 GB)
      Raid Devices : 2
     Total Devices : 2
       Persistence : Superblock is persistent

     Intent Bitmap : Internal

       Update Time : Fri Nov 15 20:28:01 2019
             State : clean, degraded, recovering
    Active Devices : 1
   Working Devices : 2
    Failed Devices : 0
     Spare Devices : 1

Consistency Policy : bitmap

    Rebuild Status : 0% complete

              Name : localhost:root
              UUID : 257cd7f6:effadd5a:3e16dac1:9a28362d
            Events : 90

    Number   Major   Minor   RaidDevice State
       0       8       17        0      active sync   /dev/sdb1
       1       8       33        1      spare rebuilding   /dev/sdc1
[root@yiran 20:28:04 ~]$cat /proc/mdstat
Personalities : [raid1]
md127 : active raid1 sdc1[1] sdb1[0]
      47153152 blocks super 1.2 [2/1] [U_]
      [>....................]  recovery =  0.0% (8832/47153152) finish=621.6min speed=1261K/sec
      bitmap: 1/1 pages [4KB], 65536KB chunk

unused devices: <none>
```


## 调查


确认硬件没问题之后，尝试通过 `/proc/mdstat` 可以看到同步速度只有 1M 左右，通过 `iostat` 命令看磁盘读写状态发现磁盘没有任何压力，使用率也是正常水平。

到这里没啥想法了，想到一点，系统是如何设置软 raid 同步速度的呢？

软 raid 在进行同步时，肯定会对磁盘进行大量的读写来保证磁盘数据正确性，如果是 RAID1 ，那就是完全的镜像了。如果 RAID 分区上正在进行非常重要的业务读写，但是 mdadm 又占用了比较大的读写带宽，肯定会影响到我们的业务，所以系统应该是存在一个上限值的。

经过搜索，查到了两个系统参数：

```
/proc/sys/dev/raid/speed_limit_max
/proc/sys/dev/raid/speed_limit_min
```

看一下系统默认值，发现 speed_limit_max 是200M，也就是说我现在的速度远远达不到上限，还有其他原因。

可惜的是，我查看了系统 /var/log/messages 和 dmesg ，都没有发现什么线索。


## 解决

因为这个问题虽然不重要，但是比较紧急，所以就在不知道原因的情况下先修复了它，我们可以在 `/etc/sysctl.conf` 中添加这两项配置来更改相应的数值。

```bash
[root@yiran 20:59:34 ~]$cat /etc/sysctl.conf
# sysctl settings are defined through files in
# /usr/lib/sysctl.d/, /run/sysctl.d/, and /etc/sysctl.d/.
#
# Vendors settings live in /usr/lib/sysctl.d/.
# To override a whole file, create a new file with the same in
# /etc/sysctl.d/ and put new settings there. To override
# only specific settings, add a file with a lexically later
# name in /etc/sysctl.d/ and put new settings there.
#
# For more information, see sysctl.conf(5) and sysctl.d(5).
#
dev.raid.speed_limit_min = 100000
dev.raid.speed_limit_max = 200000
[root@yiran 20:59:42 ~]$sysctl -p
dev.raid.speed_limit_min = 100000
dev.raid.speed_limit_max = 200000
```

在[这篇博客](https://www.cyberciti.biz/tips/linux-raid-increase-resync-rebuild-speed.html) 中还提到了其他方式能够提升软 raid 的同步速度，比如设置 read-ahead、条带大小、Bitmap 等，但是都不如 sysctl 调整系统参数来的方便，而且副作用也没有那么大。

## 总结

提交了一个不知道问题原因的修复 Patch，内心还是有些慌的，如果有读者看到并知道原因，麻烦留言告诉我，谢谢。

## 参考链接

* https://www.cyberciti.biz/tips/linux-raid-increase-resync-rebuild-speed.html