---
title: PingCAP tidb-ansible 源码阅读
date: 2019-04-20 11:50:41
tags:
- Ansible
---

了解我的同学应该知道，我目前负责公司产品的运维工具开发相关的工作，作为一款 2B 的产品，在产品运维过程中，总是有一些不愉快（又不能让客户知道）的繁琐操作：这些操作可能是为了防止过程中出现错误，而不断添加的检测条件；也有可能是历史问题，随着产品发布迭代而一直遗留至今。

所以我平时也在关注一些开源的 2B 产品的配套运维工具，比如 ZStack、PingCAP 之类的公司。

但是 ZStack 的开源生态不是很好，感觉只是在保持代码更新（不知道哪个分支）的状态。相比之下 PingCAP 就好很多了，可以很直接的从文档中看到差别，而且社区很活跃。

最近看到 PingCAP 的一个关于部署维护的 [视频讲解](https://university.pingcap.com/views/common/audition.html?courseId=240255&courseWareId=330983&designId=270990) ，可能时间有限，并没有很深入的讲解细节，有兴趣的同学可以看下。

在讲解过程中，一个比较核心的工具就是 Ansible，通过 Ansible Playbook 来定义各个步骤，我最近也在使用 Ansible 来进行二次开发，特此学习下 PingCAP 的 [tidb-ansible](https://github.com/pingcap/tidb-ansible) 。

## 安装方式

TiDB 目前支持 4 种安装方式：
1. Ansible Online
2. Ansible Offline
3. Docker
4. Docker compose

其中最佳实践应该是 Ansible Online 方式，通过控制机联网下载所需依赖及 TiDB binary 文件。当然如果所在环境无法访问互联网，那么只能采用 Offline 方式了。后两种部署方式，感觉只是用于开发测试或者给用户“看看”的情况。

如果要学习的话肯定要学习最佳实践了，那么我们来看看 Ansible Online 方式。

## 环境准备

TiDB 作为一个 **开源分布式关系型数据库** ，所需要的物理环境是很比较苛刻的，官方最佳实践的需求如下：

------
组件|CPU|内存|硬盘类型|网络|数量(最低要求)
--|---|--- |--- | --- | ---
TiDB | 16 | 32GB | SAS | 10GbE * 2 | 2
PD | 4 | 8GB | SSD | 10 GbE * 2 | 3
TiKV| 16 | 32GB | SSD | 10 GbE * 2 | 3
监控 | 8 | 16GB |  SAS | 1GbE * 1 | 1

对于 CPU、内存和磁盘的要求我们暂时忽略，这里注意网卡数量都是推荐的 2 块网卡，应该是会做 bonding，到时候看下代码中是否处理。

## 安装部署流程
* 控制节点安装依赖
* 配置普通用户（tidb）
    * 密码
    * sudu 权限
    * ssh key
    * ...
* 配置控制节点到被安装节点 SSH 免密登录
    * tidb 免密
* NTP
    * 各节点时钟同步
* CPU 调节器模式
    * performance
* 格式化磁盘
    * 推荐 ext4，支持 xfs
    * 挂载参数：nodelalloc 和 noatime 
* ansible inventory & TiDB 配置修改
    * inventory
    * tidb-ansible/conf/*
* 部署
    * local_prepare.yml
    * bootstrap.yml
    * deploy.yml
    * start.yml

## 具体步骤

### 软件依赖
这里 TiDB 依赖的第三方组件不多，安装方式猜测之所以直接用 pip 是因为要支持不同的发型版本，python 通用些。
其中如果部署 pump 并开启 binlog 的话，是需要安装 Kafka 集群的，这里在安装部署文档中没有见到更多的说明。

### 普通用户
这点很重要，一款软件的运行环境很重要，无须 root 权限的坚决不能给与 root 权限，否则之后的权限控制很难做。

### 时钟同步
这里采用的是 ntpd 同步，不知道为什么没有采用 chronyd，在 RHEL7 之后推荐采用 chronyd 来进行时钟同步，根据这篇[博客](https://www.thegeekdiary.com/centos-rhel-7-chrony-vs-ntp-differences-between-ntpd-and-chronyd/)中提到的，chronyd 应该占有绝对[优势](https://chrony.tuxfamily.org/comparison.html)的，不知道这里是出于什么考虑。

### CPU 调节器模式

这里 TiDB 推荐采用 performance 模式，但是如果你的 2B 产品卖点中有提到 **节省能耗** 相关字眼的，觉得还是要综合考虑才好。

### 格式化磁盘

推荐采用 ext4，在 RHEL7 之后默认的系统分区均为 xfs，这里出于什么考虑也没有透露。

在我个人使用过程中，xfs 在处理服务器掉电之后的处理很麻烦，经常是需要手动 xfs_repair 去修复磁盘分区。

TiDB 挂载参数强制要求 **nodelalloc** ，我们看下这个参数的意义：
```Disable delayed allocation.  Blocks are allocated
when the data is copied from userspace to the page cache, either via the write(2) system call or when an mmap'ed page which was previously unallocated is written for the first time.
```

### TiDB 参数
因为对 TiDB 无更多了解，此节忽略。

### 部署
终于到了我最想了解的地方了：ansible playbook。我们先看下代码结构：

```bash
yiran@zhouyirandeMacBook-Pro:~/Documents/git-repo/tidb-ansible
master ✔ $ tree -L 2 .
.
├── LICENSE
├── README.md
├── ansible.cfg
├── bootstrap.yml
├── clean_log_cron.yml
├── cloud
│   └── aws-ansible
├── collect_diagnosis.yml
├── common_tasks
│   ├── add_evict_leader_scheduler.yml
|   ...
│   └── transfer_pd_leader.yml
├── conf
│   ├── alertmanager.yml
|   ...
│   └── tikv.yml
├── create_users.yml
├── deploy.yml
├── deploy_drainer.yml
├── deploy_ntp.yml
├── excessive_rolling_update.yml
├── filter_plugins
│   └── tags.py
├── graceful_stop.yml
├── group_vars
│   ├── alertmanager_servers.yml
│   ├── all.yml
|   ...
│   ├── tidb_servers.yml
│   └── tikv_servers.yml
├── hosts.ini
├── inventory.ini
├── library
│   ├── coreos_facts
│   ├── docker_facts
│   └── wait_for_pid.py
├── local_prepare.yml
├── log
├── migrate_monitor.yml
├── requirements.txt
├── roles
│   ├── alertmanager
│   ├── blackbox_exporter
│   ├── bootstrap
|   ...
│   ├── tikv
│   ├── tikv_importer
│   └── tispark
├── rolling_update.yml
├── rolling_update_monitor.yml
├── scripts
│   ...
│   ├── check
│   ├── clsrun.sh
│   ├── disk_performance.json
│   ├── grafana-config-copy.py
|   ...
│   └── tikv_trouble_shooting.json
├── start.yml
├── start_drainer.yml
├── start_spark.yml
├── stop.yml
├── stop_drainer.yml
├── stop_spark.yml
├── templates
│   └── grafana.dest.json.j2
├── unsafe_cleanup.yml
├── unsafe_cleanup_container.yml
└── unsafe_cleanup_data.yml
```

一个标准的 Ansible Playbook 结构：在最外层暴露我们需要执行的 YAML 配置，所有具体的操作和配置文件都放到 roles 和 conf 中，下面我们来一点点看具体做了什么，哪些地方是我们需要注意的。

#### local_prepare.yml

在这里一共做了以下这么几件事情：
* 准备 binary 下载地址配置
* 检查网络(GFW)
* 下载 binary
* 准备 fio 软件
* 清理下载路径

主要都是做环境准备的工作，其中网络检测这没有用我们日常使用最多的 `ping` ，而是使用了 `curl` ，这里猜测是因为有时候机器是可以与互联网通信，但是没有配置 DNS 解析，导致后续的下载也会失败，所以直接 `curl baidu.com` 是一个不错的选择。

(这里还检查了 GFW - - )

用到的 Ansible 模块有：
* file
* shell （果然没人会去用 command 的
* template
* get_url
* ...

#### bootstrap.yml

* 基本环境配置参数检查（机器数、配置、OS发行版）
* python 环境准备，NTP 软件包安装
* 设置内核参数
* 检查系统配置（cpu 调节器配置如果不是performance， 非开发模式下会强制退出）
* fio 检测
    * psync ,bs=32k,iodepth=4,numjobs=4  randread iops不小于 40k
    * psync, bs=32k,iodepth=4,numjobs=4  randrw(100%r,0%w) iops均不低于 10k
    * psync, bs=32k, iodepth=1,numjobs=1  randrw(100%r,0%w) lat randread 不高于 0.25ms，write 不高于 30us

内核参数部分修改了如下配置：
* net.core.somaxconn=32768 # 最大 socket 连接数，默认为 128
* vm.swappiness=0 # 禁用 swap 空间
* net.ipv4.tcp_syncookies=0 # 关闭 synccookies，默认为关闭
* net.ipv4.tcp_tw_recycle=0 # TIME_WAIT 快速回收，默认关闭，关于 TIME_WAIT 状态可以在《TCP/IP 详解 卷一 协议》 中了解更多
* fs.file-max=1000000 # 最大文件数，默认为 1024
* irqbalance ONESHOT=yes # irqbalance 不以守护进程方式运行


关于 fio 检测，嗯，我还是太天真了，这个级别的磁盘延迟要求，估计只有 PCIe SSD 可以满足了吧。

#### deploy.yml 
这部分通用的东西比较少，都是内部的一些配置文件和服务。

#### start.yml
貌似 TiDB 服务的启动是有严格的依赖关系的，不知道这里如果启动顺序调整，是否会自动重试直到相应依赖服务启动完成。


## 滚动升级

在视频讲解中，提到 TiDB 支持滚动升级，这一点在一个 2B 产品功能中很重要，随着产品的开发迭代，能够无痛的给客户进行升级是很重要的。

在官方文档中，看到了两个升级文档，分别为 1.0 升级到 2.0 和 2.0 升级到 2.1。使用的滚动升级 YAML 文件为：rolling_update.yml
升级过程为滚动升级，步骤为：
1. pre check
2. upgrade
3. post upgrade

这里没搞懂为什么 pre check tidb-server 也要顺序执行，看上去只是检测了 TiDB 版本。

在 YAML 中指定的升级顺序为：
1. pd
2. tikv
3. pump
4. tidb

这里比较遗憾没有找到升级失败的处理方式，升级 PD 过程中检查健康状态连续 1分钟都未恢复正常，此时 Ansible 退出，PD 处于高版本状态，其他组件 tikv，tidb 还处于低版本状态，不知道这时如何处理，也许是产品上保证了兼容性？


## 总结
了解了 TiDB 的安装和升级，着重学习下 Ansible Playbook 的组织形式，在 tidb-ansible 中，所有的功能都拆分的很细，能采用 ansible 的都用 ansible 实现了，但是难免需要一些脚本配合（fio），这里的选择需要根据实际情况来进行相应修改。


## 吐槽
不知道为什么在代码中 scripts 下放置了许多json 配置文件。。。。

