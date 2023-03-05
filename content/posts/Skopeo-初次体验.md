---
title: Skopeo 初次体验
date: 2019-10-26 22:52:06
tags:
- Linux
---



## 背景

新一代容器工具体验系列已经完成了 Podman 和 Buildah 的介绍，今天来体验下三剑客中的 Skopeo。

容器工具体验系列：
* [Podman 初次体验](https://zdyxry.github.io/2019/10/12/Podman-%E5%88%9D%E6%AC%A1%E4%BD%93%E9%AA%8C/)
* [Buildah 初次体验](https://zdyxry.github.io/2019/10/19/Buildah-%E5%88%9D%E6%AC%A1%E4%BD%93%E9%AA%8C/)
* [Skopeo 初次体验](https://zdyxry.github.io/2019/10/26/Skopeo-初次体验/)


## What

Skopeo 的功能很简单，一句话描述就是：提供远程仓库的镜像管理能力。

功能列表：
* 复制镜像，无需特殊权限即可从不通仓库复制镜像
* 无需拉取镜像即可获取远程镜像仓库中的镜像属性（包括 layer）
* 删除镜像仓库中的镜像
* ...

支持镜像仓库类型：
* container-storage
* 本地路径
* docker registry 仓库
* docker 打包镜像文件
* 本地 docker 拉取的镜像文件
* OCI 镜像
* ...


**吐槽：Podman 和 Buildah 好歹都有自己的域名： podman.io 和 buildah.io ，Skopeo 虽然用的少但是也得搞个官网吧。。。**

## How

知道了 Skopeo 主要是对镜像仓库及镜像信息的获取，那么我们来看几个具体的例子，了解下 Skopeo 的使用。

### 镜像详情

```bash
root@yiran-workstation:~ 
 $ skopeo inspect docker://docker.io/fedora       
{
    "Name": "docker.io/library/fedora",
    "Digest": "sha256:8a91dbd4b9d283ca1edc2de5dbeef9267b68bb5dae2335ef64d2db77ddf3aa68",
    "RepoTags": [
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26-modular",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31",
        "32",
        "branched",
        "heisenbug",
        "latest",
        "modular",
        "rawhide"
    ],
    "Created": "2019-09-27T21:20:57.589955018Z",
    "DockerVersion": "18.06.1-ce",
    "Labels": {
        "maintainer": "Clement Verna \u003ccverna@fedoraproject.org\u003e"
    },
    "Architecture": "amd64",
    "Os": "linux",
    "Layers": [
        "sha256:9908e46907377e84bd6646bdb18abebeb4163b85135739e1cd60aae154d4557c"
    ]
}
```

我们可以直接从 Docker 官方仓库中查看远程镜像的信息，默认显示所有 RepoTags，也可以增加 tag 参数来显示具体的某个 Tag 镜像的信息。

来看下具体的镜像信息包含什么，包含镜像的创建时间、Docker 版本、标签信息、哈希值，包含镜像的 Layers 信息等，默认输出并没有镜像大小信息。

前段时间参加了 VMware Harbor 的一个沙龙，他们在 1.9.0 版本中增加了配额功能，据他们的研发说在关于镜像大小的计算上花费了很大的精力，因为镜像是分层的，在不通镜像之间的数据共享和计算上容易出现偏差，Skopeo 无法获取每层的大小，瞬间感觉使用价值不大了（- - 

### 镜像拷贝

将远端镜像拷贝到本地：

```bash
root@yiran-workstation:~ 
 $ mkdir fedora                                                                                                   1 ↵
root@yiran-workstation:~ 
 $ skopeo copy docker://fedora:32 dir:/root/fedora                                           
Getting image source signatures
Copying blob a39edc9e7bc3 done
Copying config e13031c001 done
Writing manifest to image destination
Storing signatures
root@yiran-workstation:~ 
 $ ls fedora 
a39edc9e7bc3a586926c94144a8c7ebc83dbfaa17c2a60f4ad56df7066cba285  manifest.json
e13031c001a8b4a574e3088e2d1ab331d72d821804ccacdd41bf5662ae02cc98  version
root@yiran-workstation:~ 
 $ ll fedora               
total 67M
-rw-r--r-- 1 root root  67M Oct 26 20:18 a39edc9e7bc3a586926c94144a8c7ebc83dbfaa17c2a60f4ad56df7066cba285
-rw-r--r-- 1 root root 2.0K Oct 26 20:18 e13031c001a8b4a574e3088e2d1ab331d72d821804ccacdd41bf5662ae02cc98
-rw-r--r-- 1 root root  529 Oct 26 20:18 manifest.json
-rw-r--r-- 1 root root   33 Oct 26 20:18 version
```

将远端镜像拷贝到其他镜像仓库：

```bash
root@yiran-workstation:~ 
 $ skopeo copy --dest-creds=zdyxry:xxxxxxxx docker://fedora:32 docker://zdyxry/fedora:32    
Getting image source signatures
Copying blob a39edc9e7bc3 skipped: already exists
Copying config e13031c001 done
Writing manifest to image destination
Storing signatures
root@yiran-workstation:~ 
 $ skopeo inspect --creds zdyxry:xxxxxxxx docker://zdyxry/fedora:32
{
    "Name": "docker.io/zdyxry/fedora",
    "Digest": "sha256:3f3fc6a4714e44fae9147bc2b9542ac627491c13c4a3375e5066bdddc7710c9e",
    "RepoTags": [
        "32"
    ],
    "Created": "2019-09-27T21:21:30.467123272Z",
    "DockerVersion": "18.06.1-ce",
    "Labels": {
        "maintainer": "Clement Verna \u003ccverna@fedoraproject.org\u003e"
    },
    "Architecture": "amd64",
    "Os": "linux",
    "Layers": [
        "sha256:a39edc9e7bc3a586926c94144a8c7ebc83dbfaa17c2a60f4ad56df7066cba285"
    ]
}

```

### 镜像删除

Skopeo 提供了命令可以直接删除远端镜像仓库中的镜像（Docker 官方仓库不支持该功能），这为 CI/CD 提供了更多的可能性。

```bash
$ skopeo delete docker://localhost:5000/imagename:latest
```

## Why

看过前面两篇文章的同学都知道，Podman 和 Buildah 其实是将 Docker 原有的功能进行了拆分和改进，使其使用上更友好，但是我相信大部分同学日常使用 Podman 和 Buildah 就足够了，那么为什么使用被宣称为三剑客的 Skopeo ？为了解决什么问题？

在 Quora 上搜到了这个问题，RedHat 容器运行时团队的 Leader Daniel Walsh 回答了这个问题，我整理了一下大概是以下几点原因：
* 最初向 Docker 提 PR 想增加 `docker inspect -remote` 功能，即不用拉取镜像就可以获取镜像信息，但是被拒绝了，官方建议自己实现该功能
* Skopeo 在希腊语中的意思是 **远程查看**，最初实现的功能就是远程查看镜像信息
* 后续扩展功能增加了镜像的拉取，推送，复制等功能

我自己日常在使用 Docker 的时候，通常是 `docker pull` 得到自己想要的镜像之后，通过 Dockerfile 构建自己的镜像，然后再通过 `docker push` 推送到镜像仓库，不太会关心镜像仓库的维护，而 Skopeo 就是负责这个事情。



## 参考链接
* https://www.systutorials.com/docs/linux/man/1-skopeo/
* http://saharsh.org/2019/01/18/buildah_podman_skopeo/
* https://www.quora.com/What-is-skopeo-and-why-it-is-used-in-containers 