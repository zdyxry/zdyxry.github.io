---
title: Linux 引导那些事儿
date: 2019-12-01 00:32:26
tags:
- Linux
---

## 背景

在平时工作中我自己可能80% 的时间都在使用 Linux 进行工作，无论是软件开发还是环境维护，那么对于 Linux 发行版自然也是有比较熟悉的，比如 RHEL 系列。平时大家可能多多少少都会听到或接触到一些命令（术语），比如：grub,chroot,isolinux,bios 等等。今天打算就用 CentOS 发行版的 ISO 来谈谈自己对于 Linux 系统引导，安装，启动的理解。

CentOS ISO 目录树如下：

```shell
├── CentOS_BuildTag
├── EFI
├── EULA
├── GPL
├── images
├── isolinux
├── LiveOS
├── Packages
├── repodata
├── RPM-GPG-KEY-CentOS-7
├── RPM-GPG-KEY-CentOS-Testing-7
└── TRANS.TBL
```

## isolinux

### ISO 9660

ISO 9660 是一种文件系统，也是一种规范，它规定了 ISO 文件应该是什么样子，常见的 Linux 发行版 ISO 都符合该规范。

### 引导

有了 ISO，有了计算机，那么我们需要使用 ISO 安装想要的操作系统，通常我们会将 ISO 通过光盘/USB/网络等方式挂载到计算机上，通过设置 BIOS/UEFI 选项，将启动项设置为 ISO，然后启动进行安装。接下来一个一个来说。

BIOS/UEFI 通常存放在闪存中，在计算机开机自检完成后，加载引导程序（bootloader），这个初始化过程称为引导。BIOS/UEFI 通常允许用户设置加载选项，即从系统的众多设备中按照顺序进行加载，常见的比如：硬盘、光盘、网络、USB 等。当第一个设备加载失败后，会尝试第二个设备，以此类推，如果最终所有设备都无法加载，那么系统处于开机但未引导状态。

#### 磁盘引导
如果从硬盘引导，那么计算机首先会读取 MBR（主引导记录 or 主引导扇区），MBR 在硬盘上的三维地址为（柱面，磁头，扇区）＝（0，0，1）。有时也将其开头的 446 字节内容特指为“主引导记录”（MBR），其后是4个16字节的“磁盘分区表”（DPT），以及2字节的结束标志（55AA）。

也就是说，如果我们的磁盘是一个包含 MBR 的磁盘，那么它的 446 字节到 446 + 16 * 4 = 510 字节部分是引导记录，而 510 字节地址记录的应该是 `55AA` 这个结束标志，我们来找个磁盘看下是否是这样：

```shell
root@yiran-30-250:/tmp
 $ dd if=/dev/vda of=a bs=512 count=1
记录了1+0 的读入
记录了1+0 的写出
512字节(512 B)已复制，0.000403482 秒，1.3 MB/秒
root@yiran-30-250:/tmp
 $ hexdump a
0000000 63eb 1090 d08e 00bc b8b0 0000 d88e c08e
...
00001f0 0000 0000 0000 0000 0000 0000 0000 aa55
0000200
```

在确认了磁盘可引导之后，BIOS 将 MBR 中的 446 字节内容复制到内存中，并将控制权转给引导设备（即磁盘），之后根据 MBR 中的引导程序（bootloader）进行后续工作。这里 UEFI 与 BIOS 略有不同，UEFI 是通过查找磁盘上 FAT 分区中加载 EFI loader 来进行引导，可以说 UEFI 是基于文件系统的。

到这里，我们已经进行了引导的第一步，也是最关键的一步，那么现在运行的 bootloader 是什么呢？Linux 常见的有两种：LILO 全称 LInux LOader，是一种 Linux 引导程序，它自身很简单，甚至说简陋，目前使用场景很少。GRUB 全称 GNU GRUB，是一种引导程序，它允许启动不同的操作系统或者不同的内核，目前大多数 Linux 发行版均采用 GRUB 作为引导程序。

当引导程序为 GRUB 时，因为 MBR 大小有限，因此存放在 MBR 中的内容是 boot.img，作用是加载真正的 GRUB core.img，GRUB 运行后，会根据 grub.cfg 选项来加载真正的内核映像，并进入到 OS 启动阶段。

GRUB 加载的文件有两个：vmlinuz 和 initrd.img 。

vmlinuz(vmlinux)，压缩后可引导的 Linux kernel 内核映像，VM 代表 Virtual Memory，通常是 bzImage 格式。

```shell
root@yiran-30-250:/boot
 $ file vmlinuz-3.10.0-693.11.6.el7.x86_64
vmlinuz-3.10.0-693.11.6.el7.x86_64: Linux kernel x86 boot executable bzImage, version 3.10.0-693.11.6.el7.x86_64 (builder@kbuilder.dev.centos.org) #1, RO-rootFS, swap_dev 0x5, Normal VGA
```

initramfs.img（init ramdisk.img），有了可引导的内核映像还不够，因为我们不能确保我们的硬件设备是 kernel 可以直接识别的，往往需要加载一些启动来保证硬件的识别，这时候就需要 initramfs.img 来提供一个临时文件系统，运行在内存中。

有时候我们也会看到 initrd.img 文件，initrd 是 initramfs 出现之前的方式，因为它内部有文件系统，运行在内存中造成了一定的空间浪费，而 initramfs 是 tmpfs，在使用上更方便。

```shell
root@yiran-30-250:/boot
 $ file initrd-plymouth.img
initrd-plymouth.img: gzip compressed data, from Unix, last modified: Wed Mar 28 13:41:54 2018, max compression
root@yiran-30-250:/boot
 $ file initramfs-3.10.0-693.11.6.el7.x86_64.img
initramfs-3.10.0-693.11.6.el7.x86_64.img: ASCII cpio archive (SVR4 with no CRC)
```

到这里已经比较清楚了，接下来就是挂载相应配置的文件系统，执行 systemd（pid 为1）的进程，这里不再详细描述。


#### 光盘引导

在介绍了常规的磁盘引导后，我们来看看光盘引导的流程。

根据 El-Torito 规范，BIOS 会读取 ISO 的准确地址进行判断，ISO 是否可以进行引导启动（在第 71 字节地址保存引导目录）。如果判断可引导，那么就加载对应的引导程序（bootloader）。

常见的引导程序有：SYSLINUX,ISOLINUX,PXELINUX,EXTLINUX 等，这些可以统称为 Syslinux，目前最常见的应该是 ISOLINUX。PXELINUX 用于从网络引导，EXTLINUX 用于 ext 系列文件系统引导。

注意：由于目前 UEFI 的普遍性，部分 LiveCD ISO 会同时带有 ISOLINUX 和 GRUB 两种引导程序。

我们来看看 ISO 中 isolinux 路径下放了什么文件：

```shell
 $ tree 
├── boot.cat # 启动目录
├── boot.msg # 启动信息
├── grub.conf # GRUB 配置文件
├── initrd.img # 临时文件系统
├── isolinux.bin # ISOLINUX 引导程序
├── isolinux.cfg # ISOLINUX 引导配置文件
├── memtest # 内存测试可执行文件
├── splash.png # ISOLINUX 引导背景图片
├── TRANS.TBL # 扩展文件名
├── vesamenu.c32 # Menu 配置
└── vmlinuz # 内核映像
```

根据以上文件信息及用途描述，我们来看下光盘引导的大概流程：
1. 加载 isolinux.bin
2. 加载 isolinux.cfg,vesamenu.c32,splash.png 生成启动菜单
3. 根据选项决定是否加载 vmlinuz, initrd.img 

关于 isolinux 目录和 Linux 引导部分大概是这样，主要是要理清楚整个流程。

## EFI

```shell
 $ tree 
.
├── BOOT
│   ├── BOOTIA32.EFI  # 32位系统 EFI 启动程序
│   ├── BOOTX64.EFI # 64位系统 EFI 启动程序
│   ├── fonts # 字体
│   │   ├── TRANS.TBL
│   │   └── unicode.pf2
│   ├── grub.cfg # GRUB 配置
│   ├── grubia32.efi # GRUB 32位引导程序
│   ├── grubx64.efi # GRUB 64位引导程序
│   ├── mmia32.efi # 内存测试 32 位执行程序
│   ├── mmx64.efi # 内存测试 64 位执行程序
│   └── TRANS.TBL
└── TRANS.TBL
```

有了前面 isolinux 关于引导部分的介绍，这里 EFI 完全可以一一对应，如果计算器启动模式为 BIOS，那么是通过 ISOLINUX 引导，如果启动模式是 UEFI，那么是通过 EFI（GRUB）引导。


## images

```shell
 $ tree 
├── efiboot.img
├── pxeboot
│   ├── initrd.img
│   ├── TRANS.TBL
│   └── vmlinuz
└── TRANS.TBL
```

这个路径文件很突兀，没有什么配置文件，看上去系统也没有用到，其实这里是为了文件复用而把 vmlinuz 和 initrd.img 提取出来了，在 EFI 路径下的 BOOT/grub.cfg 中有很多选项都是使用的 pxeboot/vmlinuz 。当然它最大的作用也是跟路径名一样，images，当你要配置一个发行版作为网络安装时，需要对应的 vmlinuz 和 initrd.img，那么可以从这个路径下获取，不会造成我要通过 PXELINUX 引导，却需要去 EFI 路径下获取文件的困扰。


## LiveOS

```shell
 $ tree 
├── squashfs.img
└── TRANS.TBL
```

LiveOS，字面意思就是运行在内存中的 OS，现在大多数发行版为了让用户第一时间不用安装到磁盘上即可体验发行版的某些功能，而支持将 OS 运行在内存中，简单快捷。

> squashfs.img，是一套供Linux核心使用的GPL 开源只读压缩档案系统。Squashfs能够为档案系统内的档案、inode及目录结构进行压缩，并支援最大1024 千位元组的区段，以提供更大的压缩比。

根据维基百科描述，squashfs.img 应该是包含了一个完整的 Linux映像的，我们来尝试挂载查看下：

```shell
root@yiran-30-250:/tmp
 $ ls squashfs.img
squashfs.img
root@yiran-30-250:/tmp
 $ file squashfs.img
squashfs.img: Squashfs filesystem, little endian, version 4.0, 368572502 bytes, 3 inodes, blocksize: 131072 bytes, created: Tue Sep  5 21:35:03 2017
root@yiran-30-250:/tmp
 $ mount -t squashfs squashfs.img /tmp/yiran
root@yiran-30-250:/tmp
 $ ls /tmp/yiran/LiveOS/rootfs.img
/tmp/yiran/LiveOS/rootfs.img
root@yiran-30-250:/tmp
 $ file /tmp/yiran/LiveOS/rootfs.img
/tmp/yiran/LiveOS/rootfs.img: Linux rev 1.0 ext4 filesystem data, UUID=e2fddbe2-a003-4b98-b272-3defe7b377c4, volume name "Anaconda" (extents) (64bit) (huge files)
root@yiran-30-250:/tmp
 $ mount /tmp/yiran/LiveOS/rootfs.img /tmp/yiran-root
root@yiran-30-250:/tmp
 $ ls /tmp/yiran-root
bin  dev  etc  firmware  lib  lib64  lost+found  mnt  modules  proc  root  run  sbin  sys  tmp  usr  var
```

既然是一个完整的 Linux 映像，我们可以直接通过 chroot 命令切换根目录：

```shell
[root@yiran-30-250 00:24:30 yiran-root]$pwd
/tmp/yiran-root
[root@yiran-30-250 00:24:31 yiran-root]$ls
bin  dev  etc  firmware  lib  lib64  lost+found  mnt  modules  proc  root  run  sbin  sys  tmp  usr  var
[root@yiran-30-250 00:24:32 yiran-root]$chroot .
bash: /var/log/bash.log: 只读文件系统
[root@yiran-30-250 16:24:34 /]$cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
bash: /var/log/bash.log: 只读文件系统
[root@yiran-30-250 16:24:36 /]$exit
```

因为文件系统是只读的，所以我们只是进行了简单的读取操作。


## 总结

通过 CentOS 发行版，我们一点点从计算机上电开始，走通整个流程，这只是一个最简单的流程，之前博客也多少提到过通过 KickStart 或者其他自动化方式安装等方式，这里不再描述。

在做事情之前最好把整个流程想通，再去研究细节部分。


## 参考链接
* https://wiki.osdev.org/ISO_9660#The_Boot_Record
* https://wiki.syslinux.org/wiki/index.php?title=Doc/isolinux
* https://wiki.osdev.org/El-Torito
* https://wiki.syslinux.org/wiki/index.php?title=ISOLINUX
* https://zh.wikipedia.org/wiki/SquashFS
* 