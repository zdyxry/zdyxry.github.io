---
title: BIOS vs UEFI
date: 2019-05-26 08:46:23
tags:
- Hardware
---

## 背景

大家应该都安装过操作系统，PC 或者服务器上。那么我们在安装操作系统时通常需要进入到 BIOS 或 UEFI 界面去安装。之前维护的一个 ISO 版本只支持 BIOS，最近有了支持 UEFI 安装的需求，今天来了解一下其中的差异，之后尝试编写一个支持 UEFI 的 KickStart 配置。


## Legacy BIOS

按照惯例，引用维基百科中（不同语言对于名词解释信息可能是完全不同的，最好直接看英文）的解释：
> BIOS (/ˈbaɪɒs/ BY-oss; an acronym for Basic Input/Output System and also known as the System BIOS, ROM BIOS or PC BIOS) is non-volatile firmware used to perform hardware initialization during the booting process (power-on startup), and to provide runtime services for operating systems and programs.[1] The BIOS firmware comes pre-installed on a personal computer's system board, and it is the first software to run when powered on. The name originates from the Basic Input/Output System used in the CP/M operating system in 1975.[2][3] The BIOS originally proprietary to the IBM PC has been reverse engineered by companies looking to create compatible systems. The interface of that original system serves as a de facto standard.

主要功能有：
* POST - 在加载操作系统之前， 检测硬件确保没有错误
* Bootstrap Loader - 寻找引导加载程序，并将控制权转
* BIOS 驱动程序 - 低级驱动程序，使计算机可以对计算机硬件进行基本操作控制
* BIOS/CMOS 设置 - 允许配置硬件设置，包括系统设置，如计算机密码，硬件时钟等


### BIOS vs CMOS

更改BIOS配置时，设置不会存储在BIOS芯片本身。相反，它们存储在一个特殊的存储芯片上，称为`CMOS`。

与大多数RAM芯片一样，存储BIOS设置的芯片使用CMOS工艺制造。它包含少量数据，通常为256 个字节。CMOS 芯片上的信息包括计算机上安装的磁盘驱动器类型，系统时钟的当前日期和时间以及计算机的引导顺序。

BIOS是非易失性的：即使计算机没电也会保留其信息，因为即使计算机已关闭，计算机也需要记住其BIOS设置。这就是为什么CMOS有自己的专用电源，即CMOS电池。 通常我们在使用电脑的时候，如果忘记了 BIOS 密码，无法更改 BIOS 设置时， 那么可以通过拔掉 CMOS 电池，再安装即可恢复。


## (U)EFI

> The Unified Extensible Firmware Interface (UEFI) is a specification that defines a software interface between an operating system and platform firmware. UEFI replaces the Basic Input/Output System (BIOS) firmware interface originally present in all IBM PC-compatible personal computers,[1][2] with most UEFI firmware implementations providing legacy support for BIOS services. UEFI can support remote diagnostics and repair of computers, even with no operating system installed.[3]

Intel 为了解决 BIOS 的一些缺点，提出了 EFI ，后来由于各种历史原因，EFI 转变为了 UEFI，其中的 U 是 `Unified` 。

那么 BIOS 有啥缺点呢？ 对于服务器级别来说，最大的缺点可能就是不支持 2TiB 以上空间的磁盘引导，关于为什么不支持大家可以自己查阅下 MBR vs GPT 相关资料，这里不详细解释。


那么老大哥提出了 UEFI，除了解决了引导磁盘的容量限制，还有如下优点（这几点看上去就跟普通用户没啥关系）：
* 独立于CPU的架构
* 独立于CPU的驱动程序
* 灵活的pre-OS环境，包括网络功能
* 模块化设计
* 向后和向前兼容性


## Linux 安装识别

了解了大概的概念，那么我们来实际看看 Linux 分别从 BIOS 启动和 UEFI 启动安装有什么不同吧，接下来示例以 CentOS 为例。

首先我们看下 CentOS ISO 中的目录结构：

```bash
[root@dell-r720xd-1 CentOS-7.4]# tree . -d 1
.
├── EFI # EFI 模式下引导程序路径
│   └── BOOT
│       └── fonts
├── images # 系统启动镜像
│   └── pxeboot
├── isolinux   # 默认引导程序路径，包括引导选项配置，引导背景图片，引导内核镜像等
├── LiveOS    # 临时加载镜像
├── Packages   # ISO 附带所有软件包，以 RPM 形式存放
└── repodata    # ISO 中 YUM Repo 配置文件，保存了在只做 YUM Repo 时指定的软件组，支持语言等信息
1 [error opening dir]

9 directories
```

### BIOS

我们来看下在 BIOS 下如何指定安装 KickStart 配置：

在 `isolinux/isolinux.cfg` 中指定即可
```
label linux
  menu label ^Install yiran'OS
  menu default
  kernel vmlinuz
  append initrd=initrd.img inst.stage2=hd:LABEL=YIRANOS-2 ks=hd:LABEL=YIRANOS-2:/ks_yiranos.cfg quiet
```


### UEFI

跟 BIOS 一样，只是换了一个配置位置，只需要在 `EFI/BOOT/grub.cfg` 中指定 KS 配置即可。

```
### BEGIN /etc/grub.d/10_linux ###
menuentry 'Install CentOS 7' --class fedora --class gnu-linux --class gnu --class os {
        linuxefi /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=CentOS\x207\x20x86_64 inst.ks=hd:LABEL=YIRANOS-2:/ks_yiranos.cfg quiet
        initrdefi /images/pxeboot/initrd.img
}
```


## 总结

随着越来越多服务器厂商将 UEFI 设置为默认模式，哪怕我们没有用到 UEFI 的高级功能，也最好将自己的 ISO 支持到 UEFI，避免因为 BIOS 的一些历史遗留问题导致后续技术支持出现困难。后续找时间写一下关于 UEFI 的 KickStart 配置文件。主要变化应该是在 `/boot` 分区部分有些变化，之后再说啦。
