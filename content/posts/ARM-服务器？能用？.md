---
title: ARM 服务器适配记录
date: 2019-11-01 22:12:00
tags:
- Linux
---


## 背景

最近各大 2B 厂家都在搞国产化，我司也不例外，花费了些时间折腾了下 ARM 服务器，记录下踩坑和使用感受。

本文所使用的开发环境为 CentOS7.6。

## 编译

使用的第一步是编译自己的软件，我日常使用的软件发布的最小粒度是 RPM，所以我们需要把自己在 X86 上的软件都重新编译一份 ARM64v8 的。

### Python

在预期中，Python 应该是最简单的，直接编译 RPM 就好，我在之前博客[《RPM 常用构建方式》](https://zdyxry.github.io/2018/07/28/RPM-%E5%B8%B8%E7%94%A8%E6%9E%84%E5%BB%BA%E6%96%B9%E5%BC%8F/) 中提到过，对于 Python 来说，最简单的是通过 `FPM` 来构建 RPM，但是这里有两个坑。

1. Python 软件是否依赖了 C/C++ ，如果依赖了，那么需要在 ARM 机器上使用 `FPM` 的时候编译构建 RPM
2. 从网上下载的 `noarch.rpm` ，是否真的是 `noarch` 的？需要仔细检查（别问我怎么知道的

在我以为一切搞定的时候，想起来还有个服务是需要机器学习等第三方库的，是使用 `conda` 安装的。
好嘛，完蛋了，折腾几个小时下来结论是 `conda` 对于 ARM64 几乎处于不支持的状态。最后也没搞定。


### Golang

最简单的莫过于 Golang 了，在 Golang 1.5 及之后版本，只需要设置 `GOOS` 和 `GOARCH` 这两个环境变量就能编译出目标平台的 Go binary 文件。

在官网中我们可以找到支持列表：

$GOOS | $GOARCH
--- | ---
... | ...
linux| 	386
linux|	amd64
linux|	arm
linux|	arm64
linux|	ppc64
linux|	ppc64le
linux|	mips
linux|	mipsle
linux|	mips64
linux|	mips64le
linux|	s390x
... | ...

比如我的目标平台是 Linux ARM64 ，那么我只需要设置 `GOOS=linux GOARCH=arm64 go build` 即可。

编译出 binary 文件后，构建 RPM 方式与 x86 差别不大，只需要在 `rpmbuild` 时增加参数 `--target aarch64` 就好。



### C/C++

这个是最难搞的，好在有 wenquan 同学帮助，在安装了 `devtoolset-7` 之后也成功构建出来了，顺便让我这个没写过 C/C++ 的人去了解了下 cmake,make,ninja 都是个啥东西（虽然现在又忘了）。

如果是自己写 Makefile 编译的同学，到这里应该就没有问题了。

但是，我需要编译 envoy，这东西很恶心的点在于只能用 bazel 编译，官方提供的编译容器镜像只提供了 x86 的，所以最后只能在物理服务器上安装 bazel ，尝试编译。这时候又发现 CentOS 7 上的 libstdc++ 不包含 C++11 的 ABI，所以只能尝试使用 docker 来运行，最后通过 Docker 采用 Ubuntu 18.04 镜像编译出来了，中间经历了无数曲折。


## 安装

该编译的都编译完了，接下来安装应该很容易吧，并没有。

首先，因为 CentOS 默认的 `libstdc++` 版本太低，导致 MongoDB 无法安装，致命伤，Ubuntu 18.04 和 CentOS8 应该都可以安装，但是因为 CentOS8 官方未发布 ARM64 容器镜像，只能使用 Ubuntu 18.04 镜像将 MongoDB 运行在容器中了。

因为我不想改动太多的业务代码，所以我使用容器时是采用的 `--network=host` 模式，假装它不存在。

其他的软件包大部分都可以在网上找到已有的 ARM64 版本，如果没有只能自己编译了，比如 Redis,Fluent-bit，Prometheus 等等，但是大多没什么问题，很容易解决。

## 使用

所有软件都安装上了，终于能开始使用了。因为我负责的服务需要获取硬件信息并展示，根据硬件信息进行相应的配置，发现了一些奇奇怪怪的问题。

### CPU

不知道是测试服务器的原因还是故意未暴露出来，友商的 CPU 信息可获取的很少，比如 CPU 主频、支持指令集、CPU Cache 大小等等。

无论是 `lscpu` ， `cpuinfo` 还是 `cat /proc/cpuinfo` 均无法得到，只能通过修改业务代码来临时运行起来。

### Dmidecode

与服务器硬件打交道比较多的同学应该都知道 `dmidecode` 的命令，它能获取到服务器的硬件信息，但是我手上这台能获取的信息也是有限的，下面贴一下 X86 服务器正常获取的信息：

```bash
[yiran@node 18:38:21 ~]$dmidecode 
# dmidecode 3.0
Getting SMBIOS data from sysfs.
SMBIOS 2.7 present.
125 structures occupying 5286 bytes.
Table at 0x000EC640.

Handle 0x0000, DMI type 0, 24 bytes
BIOS Information
	Vendor: American Megatrends Inc.
	Version: 3.0
	Release Date: 06/28/2013
	Address: 0xF0000
	Runtime Size: 64 kB
	ROM Size: 12288 kB
	Characteristics:
		PCI is supported
		BIOS is upgradeable
		BIOS shadowing is allowed
		Boot from CD is supported
		Selectable boot is supported
		BIOS ROM is socketed
		EDD is supported
		5.25"/1.2 MB floppy services are supported (int 13h)
		3.5"/720 kB floppy services are supported (int 13h)
		3.5"/2.88 MB floppy services are supported (int 13h)
		Print screen service is supported (int 5h)
		8042 keyboard services are supported (int 9h)
		Serial services are supported (int 14h)
		Printer services are supported (int 17h)
		ACPI is supported
		USB legacy is supported
		BIOS boot specification is supported
		Function key-initiated network boot is supported
		Targeted content distribution is supported
		UEFI is supported
	BIOS Revision: 3.0
```

### /dev/mem

`/dev/mem` 是物理内存的映像，可以直接通过它来访问物理内存，在代码运行中，发现服务器一直报错：

```bash
** COLLECTED WARNINGS **
Failed to open memory buffer (/dev/mem): No such file or directory
No SMBIOS nor DMI entry point found, sorry.
Permission denied to memory file/device (/dev/mem)
Permission denied to memory file/device (/dev/mem)
** END OF WARNINGS **
```

发现在服务器上没有 `/dev/mem` 设备，不知道 ARM 服务器是怎么处理这种情况的。

P.S. 最终查明是 `smartctl` 这个命令一直在读取 `/dev/mem`。

### KVM

ARM64v8 架构的 CPU 理论上是支持 KVM 虚拟化的，但是很可惜，我手上这台友商100 服务器不支持，据说 200 支持，但是没拿到，支持到什么级别不清楚了。（反正我不敢用

## 容器？银弹？

读到这里的可能会问，既然你 MongoDB 和 Envoy 都能运行在容器上，那你把其他服务一起运行在容器上不就薅了么？

嗯，不是没想过，对于我来说，这面临一个服务管理上的问题，成本太高不适合。

其次，容器真的就那么容易么？

大家在使用 Docker 的时候是否注意过自己使用的镜像架构是什么？反正我是没有。一般是 `docker pull` 拉下来直接用，而且 Docker 并没有提供某些命令或者参数让你能直接拉取其他架构下的镜像，你想知道自己的镜像是什么架构的？可以通过 `docker inspect` 查看：

```bash
[root@node ~]# docker pull centos
Using default tag: latest
latest: Pulling from library/centos
no matching manifest for linux/arm64/v8 in the manifest list entries # 如果没有当前架构下的，那么就会拉取报错
[root@node ~]# docker pull centos:7
7: Pulling from library/centos
4856e02b0d50: Pull complete 
Digest: sha256:307835c385f656ec2e2fec602cf093224173c51119bbebd602c53c3653a3d6eb
Status: Downloaded newer image for centos:7
docker.io/library/centos:7
[root@node ~]# docker inspect centos:7
...
        "Architecture": "arm64",
        "Os": "linux",
        "Size": 238639700,
        "VirtualSize": 238639700,
...
```

看着没啥问题，我也用起来了，但是某些镜像我发现很奇怪的一点，`docker pull` 下来的是 amd64 ，但是镜像中的文件是 aarch64 的，我很奇怪，以为自己搞错了，但是确实可以运行，这样的镜像还不少，比如 coredns：

```bash
[root@node ~]# docker images |grep coredns/coredns
coredns/coredns                                                      1.6.2               f937200cdbb2        2 months ago        42.2MB
[root@node ~]# docker inspect coredns/coredns:1.6.2 |grep -i amd
        "Architecture": "amd64",
[root@node ~]# docker run coredns/coredns:1.6.2
.:53
2019-11-01T10:40:29.192Z [INFO] CoreDNS-1.6.2
2019-11-01T10:40:29.192Z [INFO] linux/arm64, go1.12.8, 795a3eb
CoreDNS-1.6.2
linux/arm64, go1.12.8, 795a3eb
```

搞定了 Docker 是怎么玩的，接下来尝试 Kubernetes，发现国内的镜像源居然没有 ARM64 的版本，放弃了。


## 总结

国产化浪潮更大的意义是战略性的，真正要用起来，需要花费很大的精力去一点点适配兼容，如果你不想折腾，还是远离的好。


