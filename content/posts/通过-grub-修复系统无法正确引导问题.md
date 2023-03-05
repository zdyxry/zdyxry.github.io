---
title: 通过 grub 修复系统无法正确引导问题
date: 2020-08-02 09:10:39
tags:
- Linux
---


## 背景

最近在将一个节点的 kernel 从 4.18 版本降级到 4.14 后，发现系统无法启动，直接进入到了 GRUB 提示符界面，记录下修复过程。

## 现象

因为 kernel 4.18 版本和 4.14 的 打包方式发生了比较大的变化，4.18 版本多出了 kernel-core 和 kernel-modules 两个 rpm：

> 4.14

```
[root@sh-workstation Packages]# ls |grep ^kernel
kernel-4.14.0-115.el7a.0.1.aarch64.rpm
kernel-headers-4.14.0-115.el7a.0.1.aarch64.rpm
kernel-tools-4.14.0-115.el7a.0.1.aarch64.rpm
kernel-tools-libs-4.14.0-115.el7a.0.1.aarch64.rpm
```

> 4.18

```
kernel-4.18.0-147.8.1.el7.aarch64.rpm
kernel-core-4.18.0-147.8.1.el7.aarch64.rpm
kernel-modules-4.18.0-147.8.1.el7.aarch64.rpm
kernel-tools-4.18.0-147.8.1.el7.aarch64.rpm
kernel-tools-libs-4.18.0-147.8.1.el7.aarch64.rpm
```

在没有官方 yum repo 的情况下，降级就比较麻烦，我直接尝试 `rpm -Uvh kernel-4.14*.rpm` ，然后将 4.18 的 kernel-core 和 kernel-modules 卸载掉，然后重启后，发现系统直接进入到了 GRUB 提示符界面，无法正常启动，只能寻求修复办法。


## 修复方式

当时系统启动后，显示的是 `grub>` 提示符，说明此时已经加载了 grub 程序，但是没有找到 grub.cfg 配置文件中的指定kernel 和 initramfs。

此时有两种修复思路：一种是在现有环境基础上，手动指定 grub 参数，先启动进入系统，然后再修复 grub 配置；一种是关机，在服务器上挂载一个 LiveCD OS，进入到 LiveCD 中，chroot 进行修复。

因为当时没有 LiveCD，所以选择第一种方式修复。


此时排查思路如下：
1. 需要找到 `/boot/` 分区所在磁盘，可以通过 `ls` 命令显示此时所有的磁盘分区情况，可以通过 `ls (hd0,msdos1)/` 方式查看磁盘分区下的文件，如果是 `/boot/` 分区，会看到 vmlinuz 和 initramfs 文件
2. 根据 `/boot` 分区文件系统类型，执行 `insmod` 命令加载对应的 module，比如 `insmod xfs`
3. 找到 `/boot/` 分区所在磁盘后，设置 `root` 变量，`root` 变量是指定的我们当前交互的根分区，指定我们找到的磁盘分区，`set root=(hd0,msdos1)` 
4. 加载 linux kernel，并指定系统根分区 `root`，这个 `root` 变量并不是我们在上一步所指定的，而是作为加载 kernel 的参数传递的，如果使用 lvm 配置，那么默认是 `/dev/mapper/centos-root` ，最终命令如 `linux /vmlinuz-4.14.0-115.el7a.0.1.aarch64 root=/dev/mapper/centos-root` 
5. 加载 initramfs，如 `initrd initramfs-4.14.0-115.el7a.0.1.aarch64.img` 
6. 此时所有引导的必要参数已经设置完成，输入 `boot` 命令即可正确引导
7. 系统引导后，检查 grub.cfg 配置，执行 `grub2-mkconfig -o ` 重新生成 grub 配置。


## 后续

在 kernel 升级的动作中，grub 会被自动更新，但是如果通过非常规方式进行 kernel 降级，就需要注意 grub 配置了，修复 grub 不是什么好的体验，慎重。



## 参考链接
* https://www.gnu.org/software/grub/manual/grub/grub.html
* https://help.ubuntu.com/community/Grub2/Troubleshooting
