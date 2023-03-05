---
title: CentOS 执行 grub2-mkconfig 导致磁盘只读
date: 2021-10-02 07:30:09
tags:
- Linux
---

## 背景

最近遇到了一个故障，在集群软件升级过程中，发现某一个磁盘分区变为只读，导致存储应用识别该磁盘不可用。调查发现集群升级过程中，会重新生成每个节点的 GRUB 配置文件，在执行 `grub2-mkconfig` 过程中导致的磁盘分区只读。记录下 `grub2-mkconfig` 命令执行到真正磁盘只读指令下发的流程。


## 调查

### `grub2-mkconfig` 

在执行 `grub2-mkconfig` 命令时，如果没有指定配置 `GRUB_DISABLE_OS_PROBER=true` 时，则 GRUB 会调用 os-prober （/etc/grub.d/30_os-prober）用于扫描其他操作系统进行后续配置。

### os-prober
  
os-prober 是用来探测其他磁盘中存在操作系统的情况。通常由各个发行版本提供，源码地址：https://salsa.debian.org/installer-team/os-prober 。

CentOS 默认包含的 os-prober 与源码版本并不相同，包含了一些额外的配置，通过 RPM changelog 可以查看：

```
Name        : os-prober
Version     : 1.58
Release     : 9.el7
Architecture: x86_64
Install Date: Wed 18 Aug 2021 03:44:43 PM CST
Group       : System Environment/Base
Size        : 97946
License     : GPLv2+ and GPL+
Signature   : RSA/SHA256, Mon 21 Nov 2016 03:50:19 AM CST, Key ID 24c6a8a7f4a80eb5
Source RPM  : os-prober-1.58-9.el7.src.rpm
Build Date  : Sun 06 Nov 2016 11:30:02 AM CST
Build Host  : worker1.bsys.centos.org
Relocations : (not relocatable)
Packager    : CentOS BuildSystem <http://bugs.centos.org>
Vendor      : CentOS
URL         : http://kitenet.net/~joey/code/os-prober/
Summary     : Probes disks on the system for installed operating systems
Description :
This package detects other OSes available on a system and outputs the results
in a generic machine-readable format. Support for new OSes and Linux
distributions can be added easily.
* Wed Sep 14 2016 rmarshall@redhat.com - 1.58-9
- Fix regular expression that missed a corner case when detecting
extended dos partitions.
Resolves: rhbz#1322957
        
* Wed Jul 06 2016 rmarshall@redhat.com - 1.58-8
- Resolve some coverity concerns with how the previous patch detected
whether or not a partition was a device mapper device.
Related: rhbz#1300262
        
* Tue Jul 05 2016 rmarshall@redhat.com - 1.58-7
- Do not resolve device mapper links when generating stanzas
for bootloader.
Resolves: rhbz#1300262
        
* Wed May 04 2016 rmarshall@redhat.com - 1.58-6
- Adding handling to skip probing extended dos partitions
Resolves: rhbz#1322957
- Improve Windows detection for dual boot and support Windows 10
Resolves: rhbz#1322956
- Suppress non-blocking dmraid sector size warning message
Resolves: rhbz#1198918
        
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.58-5
- Mass rebuild 2014-01-24
        
* Mon Jan 20 2014 Peter Jones <pjones@redhat.com> - 1.58-4
- Add man pages.
Resolves: rhbz#948848
```

通过下载 os-prober 的 source RPM 可以查看具体改动内容，查看 os-prober.spec 文件，查看额外的 Patch 列表：

```
Name:           os-prober
Version:        1.58
Release:        9%{?dist}
Summary:        Probes disks on the system for installed operating systems
            
Group:          System Environment/Base
# For more information about licensing, see copyright file.
License:        GPLv2+ and GPL+
URL:            http://kitenet.net/~joey/code/os-prober/
Source0:        http://ftp.de.debian.org/debian/pool/main/o/os-prober/%{name}_%{version}.tar.gz
# move newns binary outside of os-prober subdirectory, so that debuginfo
# can be automatically generated for it
Patch0001: 0001-Change-filepath-to-newns.patch
Patch0002: 0002-Don-t-count-dummy-mach_kernel-as-MacOS-X-811412.patch
Patch0003: 0003-Detect-OS-installed-to-mdraid-partition-752402.patch
Patch0004: 0004-Yaboot-allows-spaces-in-append-825041.patch
Patch0005: 0005-Detect-ld.so-after-usr-move-826754.patch
Patch0006: 0006-Use-shell-processing-instead-of-basename-875356.patch
Patch0007: 0007-Add-option-for-less-logging-893997.patch
Patch0008: 0008-Improve-btrfs-detection-support-888341.patch
Patch0009: 0009-Support-detection-on-btrfs-software-raid-906847.patch
Patch0010: 0010-Name-lvm-boot-partitions-by-fstab-entry-893472.patch
Patch0011: 0011-Set-correct-boot-partition-906886.patch
Patch0012: 0012-Factor-out-unnecessary-logger-calls-875356.patch
Patch0013: 0013-Issue-with-EFI-detection-in-logger-873207.patch
Patch0014: 0014-Man-pages-missing-948848.patch
Patch0015: 0015-Properly-handle-extended-dos-partitions-1322957.patch
Patch0016: 0016-Windows-detection-requires-binary-grep-1322956.patch
Patch0017: 0017-Add-Windows-10-detection-support-1322956.patch
Patch0018: 0018-Suppress-non-blocking-dmraid-error-info-1198918.patch
Patch0019: 0019-Do-not-resolve-device-mapper-symlinks-1300262.patch
Patch0020: 0020-Use-POSIX-shell-syntax-1300262.patch
Patch0021: 0021-Fix-extended-dos-partition-regex-1322957.patch
```


单独查看每一个 Patch 很麻烦，直接看操作系统上已经安装的 os-prober 相关文件：

```
$rpm -ql os-prober
/usr/bin/linux-boot-prober
/usr/bin/os-prober
/usr/libexec/linux-boot-probes
/usr/libexec/linux-boot-probes/50mounted-tests
/usr/libexec/linux-boot-probes/mounted
/usr/libexec/linux-boot-probes/mounted/40grub
/usr/libexec/linux-boot-probes/mounted/40grub2
/usr/libexec/linux-boot-probes/mounted/50lilo
/usr/libexec/linux-boot-probes/mounted/90fallback
/usr/libexec/newns
/usr/libexec/os-probes
/usr/libexec/os-probes/50mounted-tests
/usr/libexec/os-probes/init
/usr/libexec/os-probes/init/10filesystems
/usr/libexec/os-probes/mounted
/usr/libexec/os-probes/mounted/05efi
/usr/libexec/os-probes/mounted/10freedos
/usr/libexec/os-probes/mounted/10qnx
/usr/libexec/os-probes/mounted/20macosx
/usr/libexec/os-probes/mounted/20microsoft
/usr/libexec/os-probes/mounted/30utility
/usr/libexec/os-probes/mounted/40lsb
/usr/libexec/os-probes/mounted/70hurd
/usr/libexec/os-probes/mounted/80minix
/usr/libexec/os-probes/mounted/83haiku
/usr/libexec/os-probes/mounted/90linux-distro
/usr/libexec/os-probes/mounted/90solaris
/usr/libexec/os-probes/mounted/efi
/usr/libexec/os-probes/mounted/efi/10elilo
/usr/libexec/os-probes/mounted/efi/20microsoft
/usr/share/doc/os-prober-1.58
/usr/share/doc/os-prober-1.58/README
/usr/share/doc/os-prober-1.58/TODO
/usr/share/doc/os-prober-1.58/changelog
/usr/share/doc/os-prober-1.58/copyright
/usr/share/man/man1/linux-boot-prober.1.gz
/usr/share/man/man1/os-prober.1.gz
/usr/share/os-prober
/usr/share/os-prober/common.sh
/var/lib/os-prober
```

### grub2-mkconfig 调用 os-prober 流程

`grub2-mkconfig` 最终目的是生成 grub.cfg ，在执行过程中，会通过调用 `/etc/grub.d/` 路径下的配置脚本来依次执行，在 CentOS 存在 `/etc/grub.d/30_os-prober` 配置脚本。

执行 `os-prober` 的具体代码如下：
```
OSPROBED="`os-prober | tr ' ' '^' | paste -s -d ' '`"
if [ -z "${OSPROBED}" ] ; then
  # empty os-prober output, nothing doing
  exit 0
fi
```


### CentOS os-prober 执行流程
- 创建新的 namespace，在调试 os-prober 过程中建议注释掉该行为
- 确保所有的文件系统类型是支持的，执行 `/usr/libexec/os-prober/init/*`
- 获取节点处于已挂载分区信息、swap 分区信息、RAID 设备分区信息
- 获取节点所有 partition 信息
	- 如果 partition 已经存在于swap 分区信息或 RAID 设备分区信息中，则跳过
	- 通过 `blkid -o value -S type $path` 获取文件系统信息作为 type，比如：
		-
		  ```
		  $blkid -o value -s TYPE /dev/vdb1
		  xfs_external_log
		  ```
		- 如果 type == btrfs，则判断是否为 btrfs volume，如果是则过滤；如果不是，则使用 `/usr/libexec/os-probes/50mounted-tests` 针对该分区进行探测
		- 如果分区不在已挂载分区信息中，则使用 `/usr/libexec/os-probes/50mounted-tests` 路径下的所有方式进行探测，遍历执行
		- 如果分区处于已挂载分区信息中，则使用 `/usr/libexec/os-probes/50mounted-tests` 路径下的所有方式进行探测，遍历执行
- 探测结束

### CentOS `/usr/libexec/os-probes/50mounted-tests` 探测流程
- 参数校验，获取 partition 的 fs type 属性
	- 如果 type 处于未探测、空、LVM、swap、ctypto、ntfs则直接退出
- 如果 type == btrfs ，则针对 subvolume 进行探测流程
- 如果节点存在 grub-mount ，存在 grub2-probe 则判断 partition 是否被GRUB 挂载
- 如果上述分支都没有进入，则将分区置为只读
	- blockdev --setro $partition
	- 并通过 trap 设置信号处理函数，当接收到 EXIT,HUP,INT,QUIT,TERM 信号时，则将partition 重新置为可读可写
- 将分区根据当前 type 类型挂载到临时挂载点下，试用 `/usr/libexec/os-probes/mounted/` 路径下的探测方式进行探测，遍历执行
- 探测结束


## 总结

如果你的节点上存在处于未被挂载，且文件系统类型不为空的情况，那么建议通过设置 GRUB 配置：`GRUB_DISABLE_OS_PROBER=true` 来禁用 os-prober 的执行，防止磁盘分区变为只读。

## 参考链接

- https://tracker.ceph.com/issues/11298
- https://www.thegeekdiary.com/how-to-disable-os-prober-in-centos-rhel-7/