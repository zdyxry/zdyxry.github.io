---
title: Linux 安全清理 /boot 分区
date: 2018-08-09 15:00:25
tags:
- Linux
---


## 背景

众多 Linux 发行版中，很多为了稳定性要求，Kernel 的版本还处于比较低的版本，比如：3.10.0-xxx（说的就是 CentOS）。
在工作中难免因为某些需求要升级 Kernel，最近遇到多次升级 Kernel 后导致 `/boot` 分区被占满的情况，特此查找资料记录。


## 升级方式
在之前的博客中提到过多次，CentOS 发行版升级一般采用 `yum update` ，`Kernel` 因为没有相关依赖，也可以直接 `rpm -Uvh ` 的方式升级。


### yum update
举个例子，比如这台 Linux，目前情况如下：
```bash
[root@node111 14:25:10 ~]$uname -a
Linux node111 3.10.0-693.11.6.el7.smartx.1.x86_64 #1 SMP Tue Jan 16 22:09:10 CST 2018 x86_64 x86_64 x86_64 GNU/Linux
[root@node111 14:25:12 ~]$ll /boot/
total 124929
-rw-r--r--. 1 root root   140924 Jan 16  2018 config-3.10.0-693.11.6.el7.smartx.1.x86_64
drwxr-xr-x. 3 root root     1024 Jul  2 07:23 efi
drwxr-xr-x. 2 root root     1024 Jul  2 07:24 grub
drwx------. 5 root root     1024 Jul  2 07:31 grub2
-rw-------. 1 root root 57031976 Jul  2 07:29 initramfs-0-rescue-9b8f4b7a44fc4a1db2b125ee46f00892.img
-rw-------. 1 root root 17270634 Jul  2 07:30 initramfs-3.10.0-229.el7.x86_64.img
-rw-------. 1 root root 20958312 Jul  2 07:31 initramfs-3.10.0-693.11.6.el7.smartx.1.x86_64.img
-rw-------  1 root root 16575028 Jul  2 07:32 initramfs-3.10.0-693.11.6.el7.smartx.1.x86_64kdump.img
-rw-r--r--. 1 root root   610559 Jul  2 07:28 initrd-plymouth.img
drwx------. 2 root root    12288 Jul  2 07:23 lost+found
-rw-r--r--. 1 root root   293110 Jan 16  2018 symvers-3.10.0-693.11.6.el7.smartx.1.x86_64.gz
-rw-------. 1 root root  3232490 Jan 16  2018 System.map-3.10.0-693.11.6.el7.smartx.1.x86_64
-rwxr-xr-x. 1 root root  5889744 Jul  2 07:29 vmlinuz-0-rescue-9b8f4b7a44fc4a1db2b125ee46f00892
-rwxr-xr-x. 1 root root  5889744 Jan 16  2018 vmlinuz-3.10.0-693.11.6.el7.smartx.1.x86_64
```

我们要对它进行升级 Kernel 操作：

```bash
[root@node111 14:36:19 ~]$uname -a
Linux node111 3.10.0-693.11.6.el7.smartx.1.x86_64 #1 SMP Tue Jan 16 22:09:10 CST 2018 x86_64 x86_64 x86_64 GNU/Linux
[root@node111 14:36:22 ~]$yum update kernel
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
Resolving Dependencies
--> Running transaction check
---> Package kernel.x86_64 0:4.4.26-201.el7.centos will be installed
--> Processing Dependency: kernel-core-uname-r = 4.4.26-201.el7.centos.x86_64 for package: kernel-4.4.26-201.el7.centos.x86_64
--> Processing Dependency: kernel-modules-uname-r = 4.4.26-201.el7.centos.x86_64 for package: kernel-4.4.26-201.el7.centos.x86_64
--> Processing Dependency: xorg-x11-drv-vmmouse >= 14.0.0 for package: kernel-4.4.26-201.el7.centos.x86_64
--> Running transaction check
---> Package kernel-core.x86_64 0:4.4.26-201.el7.centos will be installed
---> Package kernel-headers.x86_64 0:3.10.0-862.3.3.el7 will be obsoleted
---> Package kernel-headers.x86_64 0:3.10.0-862.3.3.el7 will be updated
---> Package kernel-headers.x86_64 0:4.4.26-201.el7.centos will be obsoleting
---> Package kernel-modules.x86_64 0:4.4.26-201.el7.centos will be installed
--> Finished Dependency Resolution

Dependencies Resolved

=====================================================================================================================================================================================================================================================================
 Package                                                          Arch                                                     Version                                                                    Repository                                                Size
=====================================================================================================================================================================================================================================================================
Installing:
 kernel                                                           x86_64                                                   4.4.26-201.el7.centos                                                      kernel                                                    79 k
 kernel-headers                                                   x86_64                                                   4.4.26-201.el7.centos                                                      kernel                                                   1.0 M
     replacing  kernel-headers.x86_64 3.10.0-862.3.3.el7
Installing for dependencies:
 kernel-core                                                      x86_64                                                   4.4.26-201.el7.centos                                                      kernel                                                    20 M
 kernel-modules                                                   x86_64                                                   4.4.26-201.el7.centos                                                      kernel                                                    18 M

Transaction Summary
=====================================================================================================================================================================================================================================================================
Install  2 Packages (+2 Dependent packages)

Total download size: 40 M
Is this ok [y/d/N]: y
Downloading packages:
Delta RPMs disabled because /usr/bin/applydeltarpm not installed.
(1/4): kernel-4.4.26-201.el7.centos.x86_64.rpm                                                                                                                                                                                                |  79 kB  00:00:00     
(2/4): kernel-headers-4.4.26-201.el7.centos.x86_64.rpm                                                                                                                                                                                        | 1.0 MB  00:00:00     
(3/4): kernel-core-4.4.26-201.el7.centos.x86_64.rpm                                                                                                                                                                                           |  20 MB  00:00:00     
(4/4): kernel-modules-4.4.26-201.el7.centos.x86_64.rpm                                                                                                                                                                                        |  18 MB  00:00:00     
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                                                                                                                 50 MB/s |  40 MB  00:00:00     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
Warning: RPMDB altered outside of yum.
  Installing : kernel-core-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                          1/5 
  Installing : kernel-modules-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                       2/5 
  Installing : kernel-headers-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                       3/5 
  Installing : kernel-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                               4/5 
  Cleanup    : kernel-headers-3.10.0-862.3.3.el7.x86_64                                                                                                                                                                                                          5/5 
  Verifying  : kernel-core-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                          1/5 
  Verifying  : kernel-headers-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                       2/5 
  Verifying  : kernel-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                               3/5 
  Verifying  : kernel-modules-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                       4/5 
  Verifying  : kernel-headers-3.10.0-862.3.3.el7.x86_64                                                                                                                                                                                                          5/5 
  Verifying  : kernel-headers-3.10.0-862.3.3.el7.x86_64                                                                                                                                                                                                          6/5 

Installed:
  kernel.x86_64 0:4.4.26-201.el7.centos                                                                                         kernel-headers.x86_64 0:4.4.26-201.el7.centos                                                                                        

Dependency Installed:
  kernel-core.x86_64 0:4.4.26-201.el7.centos                                                                                      kernel-modules.x86_64 0:4.4.26-201.el7.centos                                                                                     

Replaced:
  kernel-headers.x86_64 0:3.10.0-862.3.3.el7                                                                                                                                                                                                                         

Complete!
```

可以看到，在升级之后 `/boot/` 分区下的老版本 Kernel 内核文件 `vmlinuz-3.10.0-693.11.6.el7.smartx.1.x86_64` 还在：

```bash
[root@node111 14:37:47 ~]$ll /boot/
total 151927
-rw-r--r--. 1 root root   140924 Jan 16  2018 config-3.10.0-693.11.6.el7.smartx.1.x86_64
-rw-r--r--  1 root root   169326 Oct 21  2016 config-4.4.26-201.el7.centos.x86_64
drwxr-xr-x. 3 root root     1024 Jul  2 07:23 efi
drwxr-xr-x. 2 root root     1024 Jul  2 07:24 grub
drwx------. 5 root root     1024 Aug  9 14:37 grub2
-rw-------. 1 root root 57031976 Jul  2 07:29 initramfs-0-rescue-9b8f4b7a44fc4a1db2b125ee46f00892.img
-rw-------. 1 root root 17270634 Jul  2 07:30 initramfs-3.10.0-229.el7.x86_64.img
-rw-------. 1 root root 20958312 Jul  2 07:31 initramfs-3.10.0-693.11.6.el7.smartx.1.x86_64.img
-rw-------  1 root root 16575028 Jul  2 07:32 initramfs-3.10.0-693.11.6.el7.smartx.1.x86_64kdump.img
-rw-------  1 root root 18060511 Aug  9 14:37 initramfs-4.4.26-201.el7.centos.x86_64.img
-rw-r--r--. 1 root root   610559 Jul  2 07:28 initrd-plymouth.img
drwx------. 2 root root    12288 Jul  2 07:23 lost+found
-rw-r--r--. 1 root root   293110 Jan 16  2018 symvers-3.10.0-693.11.6.el7.smartx.1.x86_64.gz
-rw-------. 1 root root  3232490 Jan 16  2018 System.map-3.10.0-693.11.6.el7.smartx.1.x86_64
-rw-------  1 root root  3265893 Oct 21  2016 System.map-4.4.26-201.el7.centos.x86_64
-rwxr-xr-x. 1 root root  5889744 Jul  2 07:29 vmlinuz-0-rescue-9b8f4b7a44fc4a1db2b125ee46f00892
-rwxr-xr-x. 1 root root  5889744 Jan 16  2018 vmlinuz-3.10.0-693.11.6.el7.smartx.1.x86_64
-rwxr-xr-x  1 root root  6148096 Oct 21  2016 vmlinuz-4.4.26-201.el7.centos.x86_64
```

### yum upgrade
刚刚我们用了 `yum update` 方式升级，发现没有自动清理掉旧的 Kernel ，在 Stack Overflow 上看到有人说可以使用 `upgrade` 方式，会自动清理，
现在我们换 `yum upgrade` 升级看看有何不同。

首先查看我们的环境状态：
```bash
[root@node112 14:41:11 ~]$ll /boot/
total 124884
-rw-r--r--. 1 root root   140924 Jan 16  2018 config-3.10.0-693.11.6.el7.smartx.1.x86_64
drwxr-xr-x. 3 root root     1024 May 31 10:55 efi
drwxr-xr-x. 2 root root     1024 May 31 10:56 grub
drwx------. 5 root root     1024 May 31 11:02 grub2
-rw-------. 1 root root 57008277 May 31 11:01 initramfs-0-rescue-00bf5adc700644d685733d8e76c21d42.img
-rw-------. 1 root root 17249662 May 31 11:01 initramfs-3.10.0-229.el7.x86_64.img
-rw-------. 1 root root 20945698 May 31 11:02 initramfs-3.10.0-693.11.6.el7.smartx.1.x86_64.img
-rw-------  1 root root 16586061 Jul  4 11:49 initramfs-3.10.0-693.11.6.el7.smartx.1.x86_64kdump.img
-rw-r--r--. 1 root root   610343 May 31 11:00 initrd-plymouth.img
drwx------. 2 root root    12288 May 31 10:55 lost+found
-rw-r--r--. 1 root root   293110 Jan 16  2018 symvers-3.10.0-693.11.6.el7.smartx.1.x86_64.gz
-rw-------. 1 root root  3232490 Jan 16  2018 System.map-3.10.0-693.11.6.el7.smartx.1.x86_64
-rwxr-xr-x. 1 root root  5889744 May 31 11:01 vmlinuz-0-rescue-00bf5adc700644d685733d8e76c21d42
-rwxr-xr-x. 1 root root  5889744 Jan 16  2018 vmlinuz-3.10.0-693.11.6.el7.smartx.1.x86_64
[root@node112 14:41:13 ~]$uname -a
Linux node112 3.10.0-693.11.6.el7.smartx.1.x86_64 #1 SMP Tue Jan 16 22:09:10 CST 2018 x86_64 x86_64 x86_64 GNU/Linux
```

进行升级：
```bash
[root@node112 14:42:34 ~]$yum upgrade kernel
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
Resolving Dependencies
--> Running transaction check
---> Package kernel.x86_64 0:4.4.26-201.el7.centos will be installed
--> Processing Dependency: kernel-core-uname-r = 4.4.26-201.el7.centos.x86_64 for package: kernel-4.4.26-201.el7.centos.x86_64
--> Processing Dependency: kernel-modules-uname-r = 4.4.26-201.el7.centos.x86_64 for package: kernel-4.4.26-201.el7.centos.x86_64
--> Processing Dependency: xorg-x11-drv-vmmouse >= 14.0.0 for package: kernel-4.4.26-201.el7.centos.x86_64
--> Running transaction check
---> Package kernel-core.x86_64 0:4.4.26-201.el7.centos will be installed
---> Package kernel-headers.x86_64 0:3.10.0-862.3.3.el7 will be updated
---> Package kernel-headers.x86_64 0:3.10.0-862.3.3.el7 will be obsoleted
---> Package kernel-headers.x86_64 0:4.4.26-201.el7.centos will be obsoleting
---> Package kernel-modules.x86_64 0:4.4.26-201.el7.centos will be installed
--> Finished Dependency Resolution

Dependencies Resolved

=====================================================================================================================================================================================================================================================================
 Package                                                          Arch                                                     Version                                                                    Repository                                                Size
=====================================================================================================================================================================================================================================================================
Installing:
 kernel                                                           x86_64                                                   4.4.26-201.el7.centos                                                      kernel                                                    79 k
 kernel-headers                                                   x86_64                                                   4.4.26-201.el7.centos                                                      kernel                                                   1.0 M
     replacing  kernel-headers.x86_64 3.10.0-862.3.3.el7
Installing for dependencies:
 kernel-core                                                      x86_64                                                   4.4.26-201.el7.centos                                                      kernel                                                    20 M
 kernel-modules                                                   x86_64                                                   4.4.26-201.el7.centos                                                      kernel                                                    18 M

Transaction Summary
=====================================================================================================================================================================================================================================================================
Install  2 Packages (+2 Dependent packages)

Total download size: 40 M
Is this ok [y/d/N]: y
Downloading packages:
Delta RPMs disabled because /usr/bin/applydeltarpm not installed.
(1/4): kernel-4.4.26-201.el7.centos.x86_64.rpm                                                                                                                                                                                                |  79 kB  00:00:00     
(2/4): kernel-headers-4.4.26-201.el7.centos.x86_64.rpm                                                                                                                                                                                        | 1.0 MB  00:00:00     
(3/4): kernel-modules-4.4.26-201.el7.centos.x86_64.rpm                                                                                                                                                                                        |  18 MB  00:00:00     
(4/4): kernel-core-4.4.26-201.el7.centos.x86_64.rpm                                                                                                                                                                                           |  20 MB  00:00:00     
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                                                                                                                 58 MB/s |  40 MB  00:00:00     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
Warning: RPMDB altered outside of yum.
  Installing : kernel-core-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                          1/5 
  Installing : kernel-modules-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                       2/5 
  Installing : kernel-headers-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                       3/5 
  Installing : kernel-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                               4/5 
  Cleanup    : kernel-headers-3.10.0-862.3.3.el7.x86_64                                                                                                                                                                                                          5/5 
  Verifying  : kernel-core-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                          1/5 
  Verifying  : kernel-headers-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                       2/5 
  Verifying  : kernel-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                               3/5 
  Verifying  : kernel-modules-4.4.26-201.el7.centos.x86_64                                                                                                                                                                                                       4/5 
  Verifying  : kernel-headers-3.10.0-862.3.3.el7.x86_64                                                                                                                                                                                                          5/5 
  Verifying  : kernel-headers-3.10.0-862.3.3.el7.x86_64                                                                                                                                                                                                          6/5 

Installed:
  kernel.x86_64 0:4.4.26-201.el7.centos                                                                                         kernel-headers.x86_64 0:4.4.26-201.el7.centos                                                                                        

Dependency Installed:
  kernel-core.x86_64 0:4.4.26-201.el7.centos                                                                                      kernel-modules.x86_64 0:4.4.26-201.el7.centos                                                                                     

Replaced:
  kernel-headers.x86_64 0:3.10.0-862.3.3.el7                                                                                                                                                                                                                         

Complete!
```

---
可以看到，仍然没有自动清理掉旧的 Kernel， `/boot` 分区的空间还是被占用了。

```bash
[root@node112 14:43:49 ~]$ll /boot/
total 151870
-rw-r--r--. 1 root root   140924 Jan 16  2018 config-3.10.0-693.11.6.el7.smartx.1.x86_64
-rw-r--r--  1 root root   169326 Oct 21  2016 config-4.4.26-201.el7.centos.x86_64
drwxr-xr-x. 3 root root     1024 May 31 10:55 efi
drwxr-xr-x. 2 root root     1024 May 31 10:56 grub
drwx------. 5 root root     1024 Aug  9 14:43 grub2
-rw-------. 1 root root 57008277 May 31 11:01 initramfs-0-rescue-00bf5adc700644d685733d8e76c21d42.img
-rw-------. 1 root root 17249662 May 31 11:01 initramfs-3.10.0-229.el7.x86_64.img
-rw-------. 1 root root 20945698 May 31 11:02 initramfs-3.10.0-693.11.6.el7.smartx.1.x86_64.img
-rw-------  1 root root 16586061 Jul  4 11:49 initramfs-3.10.0-693.11.6.el7.smartx.1.x86_64kdump.img
-rw-------  1 root root 18048069 Aug  9 14:43 initramfs-4.4.26-201.el7.centos.x86_64.img
-rw-r--r--. 1 root root   610343 May 31 11:00 initrd-plymouth.img
drwx------. 2 root root    12288 May 31 10:55 lost+found
-rw-r--r--. 1 root root   293110 Jan 16  2018 symvers-3.10.0-693.11.6.el7.smartx.1.x86_64.gz
-rw-------. 1 root root  3232490 Jan 16  2018 System.map-3.10.0-693.11.6.el7.smartx.1.x86_64
-rw-------  1 root root  3265893 Oct 21  2016 System.map-4.4.26-201.el7.centos.x86_64
-rwxr-xr-x. 1 root root  5889744 May 31 11:01 vmlinuz-0-rescue-00bf5adc700644d685733d8e76c21d42
-rwxr-xr-x. 1 root root  5889744 Jan 16  2018 vmlinuz-3.10.0-693.11.6.el7.smartx.1.x86_64
-rwxr-xr-x  1 root root  6148096 Oct 21  2016 vmlinuz-4.4.26-201.el7.centos.x86_64
```


## 正确清理方式

```bash
[root@node112 14:44:11 ~]$rpm -q kernel
kernel-3.10.0-693.11.6.el7.smartx.1.x86_64
kernel-4.4.26-201.el7.centos.x86_64
```

使用 `yum-utils` 中提供的 `package-cleanup` 工具：

```bash
[root@node112 14:48:02 ~]$rpm -qf `which package-cleanup`
yum-utils-1.1.31-42.el7.noarch
```

在我们重启过 OS，并确保已经使用升级后的 Kernel 后，进行如下操作：

```bash
[root@node112 14:53:44 ~]$uname -a
Linux node112 4.4.26-201.el7.centos.x86_64 #1 SMP Thu Oct 20 17:49:17 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
[root@node112 14:53:46 ~]$package-cleanup --oldkernels --count=1
Loaded plugins: fastestmirror, langpacks
--> Running transaction check
---> Package kernel.x86_64 0:3.10.0-693.11.6.el7.smartx.1 will be erased
--> Processing Dependency: kernel(__alloc_workqueue_key) = 0x43a53735 for package: kmod-mpt3sas-24.125.01.00_el7.4-1.x86_64
--> Processing Dependency: kernel(__bitmap_or) = 0x9f2bdaac for package: kmod-mpt3sas-24.125.01.00_el7.4-1.x86_64
--> Processing Dependency: kernel(__bitmap_weight) = 0x4cbbd171 for package: kmod-mpt3sas-24.125.01.00_el7.4-1.x86_64
--> Running transaction check
---> Package kmod-mpt3sas.x86_64 0:24.125.01.00_el7.4-1 will be erased
--> Finished Dependency Resolution

Dependencies Resolved

=====================================================================================================================================================================================================================================================================
 Package                                                      Arch                                                   Version                                                                         Repository                                                 Size
=====================================================================================================================================================================================================================================================================
Removing:
 kernel                                                       x86_64                                                 3.10.0-693.11.6.el7.smartx.1                                                    @anaconda                                                  60 M
Removing for dependencies:
 kmod-mpt3sas                                                 x86_64                                                 24.125.01.00_el7.4-1                                                            @anaconda                                                 5.3 M

Transaction Summary
=====================================================================================================================================================================================================================================================================
Remove  1 Package (+1 Dependent package)

Installed size: 65 M
Is this ok [y/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Erasing    : kmod-mpt3sas-24.125.01.00_el7.4-1.x86_64                                                                                                                                                                                                          1/2 
  Erasing    : kernel-3.10.0-693.11.6.el7.smartx.1.x86_64                                                                                                                                                                                                        2/2 
  Verifying  : kernel-3.10.0-693.11.6.el7.smartx.1.x86_64                                                                                                                                                                                                        1/2 
  Verifying  : kmod-mpt3sas-24.125.01.00_el7.4-1.x86_64                                                                                                                                                                                                          2/2 

Removed:
  kernel.x86_64 0:3.10.0-693.11.6.el7.smartx.1                                                                                                                                                                                                                       

Dependency Removed:
  kmod-mpt3sas.x86_64 0:24.125.01.00_el7.4-1                                                                                                                                                                                                                         

Complete!
```

现在我们来看下 `/boot` 分区情况：
```bash
[root@node112 14:54:41 ~]$ll /boot/
total 105878
-rw-r--r--  1 root root   169326 Oct 21  2016 config-4.4.26-201.el7.centos.x86_64
drwxr-xr-x. 3 root root     1024 May 31 10:55 efi
drwxr-xr-x. 2 root root     1024 May 31 10:56 grub
drwx------. 5 root root     1024 Aug  9 14:54 grub2
-rw-------. 1 root root 57008277 May 31 11:01 initramfs-0-rescue-00bf5adc700644d685733d8e76c21d42.img
-rw-------. 1 root root 17249662 May 31 11:01 initramfs-3.10.0-229.el7.x86_64.img
-rw-------  1 root root 18048069 Aug  9 14:43 initramfs-4.4.26-201.el7.centos.x86_64.img
-rw-r--r--. 1 root root   610343 May 31 11:00 initrd-plymouth.img
drwx------. 2 root root    12288 May 31 10:55 lost+found
-rw-------  1 root root  3265893 Oct 21  2016 System.map-4.4.26-201.el7.centos.x86_64
-rwxr-xr-x. 1 root root  5889744 May 31 11:01 vmlinuz-0-rescue-00bf5adc700644d685733d8e76c21d42
-rwxr-xr-x  1 root root  6148096 Oct 21  2016 vmlinuz-4.4.26-201.el7.centos.x86_64
```

可以旧的 Kernel 内核文件已经被清除了。


## 总结

在进行软件包卸载的时候，尤其是像 Kernel 这种会影响到服务器运行的软件包，我们操作一定要谨慎，不要轻易的执行 `rpm -e --nodeps` 或者 `yum -y remove ` 等操作。尽量保证服务器安全性。
