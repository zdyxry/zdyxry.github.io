---
title: CentOS LiveCD 构建及修改方式
date: 2018-08-04 06:39:28
tags:
- Linux
- LiveCD
---

## 背景
Linux 作为目前服务器占比超过 60% 的操作系统，日常使用过程中，都是采用官方发布的 DVD ISO 安装，可以选择安装桌面版本还是 Minimal 版本。但是如果我们想要验证服务器硬件是否满足产品需求，就需要通过 Live CD 的方式先在内存中运行操作系统，然后进行硬件检测。通过这种方式可以在最小成本（无需安装操作系统到磁盘中）下完成硬件检测。目前 OpenStack 厂商 Mirantis 及云计算厂商 Nutanix 均采用该种方式进行产品安装前校验。要进行校验的第一步，就是构建属于我们自己的 Live CD ISO，下面以 CentOS 为例介绍如何构建和定制 Live CD ISO。

## 流程
1. 准备构建工具
2. 编写 KickStart 脚本
3. 准备软件源
4. 构建

### 构建工具
核心工具 [livecd-creator](https://github.com/livecd-tools/livecd-tools)。
构建环境为 CentOS 7。指定官方 yum repo：
```bash
root@yiran-30-250:/etc/yum.repos.d
 $ ll
总用量 56K
-rw-r--r--  1 root root 1.7K 1月  15 2018 CentOS-Base.repo
-rw-r--r--. 1 root root 1.3K 12月  9 2015 CentOS-CR.repo
-rw-r--r--. 1 root root  649 12月  9 2015 CentOS-Debuginfo.repo
-rw-r--r--. 1 root root  290 12月  9 2015 CentOS-fasttrack.repo
-rw-r--r--. 1 root root  630 12月  9 2015 CentOS-Media.repo
-rw-r--r--  1 root root  916 5月  23 2016 CentOS-SCLo-scl.repo
-rw-r--r--  1 root root  892 5月  23 2016 CentOS-SCLo-scl-rh.repo
-rw-r--r--. 1 root root 1.3K 12月  9 2015 CentOS-Sources.repo
-rw-r--r--. 1 root root 2.0K 12月  9 2015 CentOS-Vault.repo
-rw-r--r--  1 root root  951 10月  3 2017 epel.repo
-rw-r--r--  1 root root 1.1K 10月  3 2017 epel-testing.repo
-rw-r--r--  1 root root  306 7月   2 13:58 mcepl-vim8-epel-7.repo
-rw-r--r--  1 root root 3.2K 6月  23 19:00 smartx-idc.repo
```


通过 Yum 安装，会自动安装相应依赖软件包：
```bash
yum install -y livecd-tools
```

### KickStart 脚本
什么是 KickStart？许多系统管理员更愿意使用自动安装方法在其服务器上安装 Red Hat Enterprise Linux。为了满足这一需求，Red Hat 创建了 KickStart 安装方法。具体 KickStart 编写语法查看 [RedHat 官方](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/installation_guide/sect-kickstart-syntax)查看
这里我们可以先参考[官方样例](https://github.com/CentOS/sig-core-livemedia/blob/master/kickstarts/centos-7-livecd.cfg)，先确保通过官方样例可以构建成功，我们再来进行自己的定制操作。
将官方样例下载到本地，接下来看下面一节，不着急定制。

如果按照官方样例已经正确构建了自己的 ISO，那么我们下面来看如何进行简单的定制，如配置网络。
打开 KickStart.cfg 文件，我们可以看到除了特定的语法外，其他的都是 Shell 脚本，可见 KickStart 是兼容 Shell 语法的，那么我们就可以直接在 KickStart 内指定要进行的事情。
如启动之后配置网卡信息：
```bash
# config eth0
cat > /etc/sysconfig/network-scripts/ifcfg-eth0 << EOF
DEVICE=eth0
IPADDR=192.168.30.253
NETMASK=255.255.240.0
GATEWAY=192.168.16.1
ONBOOT=yes
NAME=eth0
EOF

ifup eth0
```

或者安装某指定软件并自动启动：
```bash
# install & start & enable dhcpd
yum install -y dhcpd
systemctl enable dhcpd
systemctl start dhcpd
tail -n 10 /var/lib/dhcpd/dhcpd.leases
```

### 准备软件源
在之前的博客中我们介绍过 RPM 及 Yum 等工具的概念及使用。
我们现在需要构建一个本地的 Yum Repo。通用做法为：
```bash
$cd /data/
$mkdir packages
$cp $some_packages packages
$createrepo .
```

这样我们就创建好了一个本地的 Yum repo，如何让本地 Yum 生效呢？
我们可以通过 http 或者 ftp 的方式配置，只需要将 /data/packages 这个路径允许通过文件方式访问。

上面这种方式通常用于定制化使用，我们此处为了简化操作，可以直接拷贝一个官方 ISO，挂载到本地的方式作为本地 Yum Repo。具体操作如下：
```bash
$cd /data/
$mkdir /data/centos7
$mount CentOS-7.4-x86_64-DVD-1708.iso /data/centos7
$mkdir /etc/yum.repos.d/bk
$mv /etc/yum.repos.d/*.repo /etc/yum.repos.d/bk/
$cat > /etc/yum.repos.d/local.repo << EOF
[local]
name=local
baseurl=file:///data/centos7
enabled=1
gpgcheck=0
EOF
$
```

我们就可以通过 yum 的方式安装软件包了。

### 构建 Live CD ISO
在一切准备好之后，我们开始构建 ISO。
编辑官方样例，将 17 & 18 行替换为如下文件，指定我们刚刚指定的本地 Yum repo：
```bash
repo --name=base --baseurl=file:///data/packages
```

使用 livecd-tools 构建名为 yiran-live.iso：
```bash
livecd-creator -v --config centos-7-livecd.cfg --cache /var/cache/livecd --name yiran-livecd
```

构建过程大概需要 5 ~ 10 分钟，构建完成后我们可以再当前路径下看到 yiran-livecd.iso，我们来看下 ISO 中的目录结构：
```bash
$mkdir /tmp/yiran-livecd
$mount yiran-livecd.iso /tmp/yiran-livecd
$tree /tmp/yiran-livecd
/tmp/yiran-livecd
├── isolinux
│   ├── boot.cat
│   ├── initrd0.img
│   ├── isolinux.bin
│   ├── isolinux.cfg
│   ├── vesamenu.c32
│   └── vmlinuz0
└── LiveOS
    ├── osmin.img
    └── squashfs.img
```

可以看到，用于启动引导的文件均在 isolinux 路径下，而设计到文件系统相关的文件均被打包压缩到 `squashfs.img` 中，如果想要更多的定制方式，我们就需要解压这个 img 文件并修改对应路径下的内容，然后再压缩重新制作 ISO，这里不深入介绍。


## 总结
构建属于自己的 ISO 可以很方便的在日常工作中开展工作，我们可以直接挂载 LiveCD 并直接查看磁盘内容，可以把我们常用的内置软件放到 ISO 中，减少重复的安装操作。

LiveCD 工作中用处不多，硬件检查是一项很符合 LiveCD 本职功能的需求，无论是时间成本还是实现成本都是很低的，推荐使用。
