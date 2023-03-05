---
title: Cloud-init 无需重启执行配置
date: 2019-11-29 21:35:26
tags:
- Linux
---

## 背景

最近在折腾 Cluster API 的时候，因为目前社区中比较成熟的方案是通过 Cloud-init 执行 kubeadm 命令部署 k8s ，因此需要使用 Cloud-init 进行功能验证，但是 Cloud-init 通常执行的前提条件是系统初次启动时，自动执行配置，这点对于调试很不友好，因此需要找到一个无需重启即可执行 Cloud-init 配置的方式。

## Cloud-init

使用过公有云或者私有云的同学应该都知道在创建虚拟机的时候可以传递一个脚本用于在机器置备的时候执行某些动作，尤其在批量执行的时候，通常会很方便。这个其实就是 Cloud-init 所做的工作，就跟它的名字一样，针对 Cloud 场景执行 init 动作。

引用官网介绍：
> Cloud-init is the industry standard multi-distribution method for cross-platform cloud instance initialization. It is supported across all major public cloud providers, provisioning systems for private cloud infrastructure, and bare-metal installations. 


## NoCloud

Cloud-init 官方支持云平台种类很多常见的公有云如 Aliyun、AWS、Azure，常见的私有云解决方案如 OpenStack、ZStack、OVF 等都有支持。

但是如果我不使用已经支持的私有云，而是自己通过 Libvirt 配合 Ceph 实现了一套虚拟化平台，想要使用 Cloud-init，则可以使用 ConfigDrive 或者 NoCloud 方式。本文采用的是 NoCloud 方式。

### 配置文件

使用默认配置就好，Cloud-init 在没有指定 Datasource 的情况下，会自己依次尝试：

```bash
[root@localhost ~]# cat /etc/cloud/cloud.cfg
users:
 - default

disable_root: 1
ssh_pwauth:   0

mount_default_fields: [~, ~, 'auto', 'defaults,nofail,x-systemd.requires=cloud-init.service', '0', '2']
resize_rootfs_tmp: /dev
ssh_deletekeys:   0
ssh_genkeytypes:  ~
syslog_fix_perms: ~
disable_vmware_customization: false
```

### Metadata

这里我们指定 NoCloud 的路径，并配置 Metadata 文件：

```shell
[root@localhost nocloud]# pwd
/var/lib/cloud/seed/nocloud
[root@localhost nocloud]# cat meta-data
instance-id: yiran
hostname: yiran
```

### Userdata

我们在 Cloud-init 自动配置时，执行命令 echo 保存信息到文件中

```she l l
[root@localhost nocloud]# pwd
/var/lib/cloud/seed/nocloud
[root@localhost nocloud]# cat user-data
## template: jinja
#cloud-config

runcmd:
  - 'echo yiran test cloud-init with nocloud > /root/file'
```

## 手动执行 Cloud-init

在了解 Cloud-init 工作流程后执行比较简单，因此这里直接贴出操作步骤：


```shell
[root@localhost ~]# pwd
/root
[root@localhost ~]# ls
anaconda-ks.cfg
[root@localhost ~]# cloud-init init
Cloud-init v. 18.5 running 'init' at Fri, 29 Nov 2019 14:02:10 +0000. Up 635.10 seconds.
ci-info: +++++++++++++++++++++++++++++++++++++++Net device info+++++++++++++++++++++++++++++++++++++++
ci-info: +--------+------+------------------------------+---------------+--------+-------------------+
ci-info: | Device |  Up  |           Address            |      Mask     | Scope  |     Hw-Address    |
ci-info: +--------+------+------------------------------+---------------+--------+-------------------+
ci-info: |  eth0  | True |        192.168.77.158        | 255.255.240.0 | global | 52:54:00:2f:d9:44 |
ci-info: |  eth0  | True | fe80::108b:ab9c:1a1a:9ab8/64 |       .       |  link  | 52:54:00:2f:d9:44 |
ci-info: |   lo   | True |          127.0.0.1           |   255.0.0.0   |  host  |         .         |
ci-info: |   lo   | True |           ::1/128            |       .       |  host  |         .         |
ci-info: +--------+------+------------------------------+---------------+--------+-------------------+
ci-info: +++++++++++++++++++++++++++++++Route IPv4 info+++++++++++++++++++++++++++++++
ci-info: +-------+--------------+----------------+---------------+-----------+-------+
ci-info: | Route | Destination  |    Gateway     |    Genmask    | Interface | Flags |
ci-info: +-------+--------------+----------------+---------------+-----------+-------+
ci-info: |   0   |   0.0.0.0    | 192.168.64.215 |    0.0.0.0    |    eth0   |   UG  |
ci-info: |   1   | 192.168.64.0 |    0.0.0.0     | 255.255.240.0 |    eth0   |   U   |
ci-info: +-------+--------------+----------------+---------------+-----------+-------+
ci-info: +++++++++++++++++++Route IPv6 info+++++++++++++++++++
ci-info: +-------+-------------+---------+-----------+-------+
ci-info: | Route | Destination | Gateway | Interface | Flags |
ci-info: +-------+-------------+---------+-----------+-------+
ci-info: |   9   |  fe80::/64  |    ::   |    eth0   |   U   |
ci-info: |   10  |  fe80::/64  |    ::   |    eth0   |   U   |
ci-info: |   14  |   ff00::/8  |    ::   |    eth0   |   U   |
ci-info: +-------+-------------+---------+-----------+-------+
[root@localhost ~]# cloud-init modules -m config
Cloud-init v. 18.5 running 'modules:config' at Fri, 29 Nov 2019 14:02:18 +0000. Up 643.31 seconds.
[root@localhost ~]# cloud-init modules -m final
Cloud-init v. 18.5 running 'modules:final' at Fri, 29 Nov 2019 14:02:21 +0000. Up 646.27 seconds.
ci-info: no authorized ssh keys fingerprints found for user centos.
Cloud-init v. 18.5 finished at Fri, 29 Nov 2019 14:02:21 +0000. Datasource DataSourceNoCloudNet [seed=/var/lib/cloud/seed/nocloud][dsmode=net].  Up 646.44 seconds
[root@localhost ~]# ls
anaconda-ks.cfg  file
[root@localhost ~]# cat file
yiran test cloud-init with nocloud
```



## 参考链接
* https://cloudinit.readthedocs.io/en/latest/