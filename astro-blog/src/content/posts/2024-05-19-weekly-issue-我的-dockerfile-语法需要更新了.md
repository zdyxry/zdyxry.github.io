---
title: Weekly Issue-我的 Dockerfile 语法需要更新了
date: "2024-05-19T00:00:00.000Z"
slug: "Weekly-Issue-我的-Dockerfile-语法需要更新了"
tags:
  - Weekly
description:
---

## 文章

### 技术

[从鹅厂大佬身上学技术 · 跬步](https://zhu327.github.io/2024/05/10/%E4%BB%8E%E9%B9%85%E5%8E%82%E5%A4%A7%E4%BD%AC%E8%BA%AB%E4%B8%8A%E5%AD%A6%E6%8A%80%E6%9C%AF/)

>能想到第几层实际就体现了技术能力哪里，技术能力是一种以解决某种问题为目标的思路、方法与执行手段，其本质就是解决问题的能力。在编程领域，就是对遇到的业务问题进行抽象、提炼以及逻辑的构建，通过研发工具以提升解决问题的效能，减低人工低效的重复工作。

>1. 有所坚持：有一些原则自己必须坚持，比如对代码的架构，代码的整洁
>2. 长期主义：项目可能会长时间的在自己手里维护，所以需要看远一点，否则坑的还是自己
>3. 向上汇报：要让leader知道你在做什么以及这么做的必要性，获取leader的支持

---

[Recent Docker BuildKit Features You're Missing Out On | Martin Heinz | Personal Website & Blog](https://martinheinz.dev/blog/111)

介绍了一些 [Dockerfile](/mentions/dockerfile) 的用法，我的知识需要更新一下：

```shell
# 在 Docker build 过程中如果失败，则自动进入到交互式 shell 中
export BUILDX_EXPERIMENTAL=1
docker buildx debug --invoke /bin/sh --on=error build .

# Docker build 完成后自动推送到 registry。
docker buildx build --output type=registry,\"name=docker.io/martinheinz/testimage,docker.io/martinheinz/testimage2\" .

# 自带了 imagetools 可以查看远端的 image 信息
docker buildx imagetools inspect alpine --format "{{json .Manifest}}" | jq .digest
"sha256:c5b1261d6d3e43071626931fc004f70149baeba2c8ec672bd4f27761f8e1ad6b"

# Here-docs 可以编写连续的代码块
# syntax = docker/dockerfile:1.3-labs
FROM debian
RUN <<eot bash
  apt-get update
  apt-get install -y vim
eot

# Same as:
RUN apt-get update && apt-get install -y vim

# COPY 可以指定 --parents 和 --exclude 
COPY --parents ./one/two/some.txt /parents/
COPY --exclude=*.txt ./some-dir/* ./some-dest

# Dockerfile 支持缩进
# syntax=docker/dockerfile:1
FROM golang:1.21
  WORKDIR /src

  COPY main.go .
  RUN go build -o /bin/hello ./main.go

FROM scratch
  COPY --from=0 /bin/hello /bin/hello
  CMD ["/bin/hello"]

```

---

[VMware Desktop Hypervisor Pro Apps Now Available for Personal Use - VMware Cloud Foundation (VCF) Blog](https://blogs.vmware.com/cloud-foundation/2024/05/14/vmware-desktop-hypervisor-pro-apps-now-available-for-personal-use/)

[vmware](/mentions/vmware) workstation pro 和 fusion pro 现在对个人用户免费试用了。但博通的门户网站太烂，所以作者写了一篇博客单独介绍如何下载试用： [Downloading VMware Fusion and Workstation Free for Personal Use | mikeroySoft.com](https://www.mikeroysoft.com/post/download-fusion-ws/) 

>"even a broken clock is right twice a day"

因为博通的门户网站交互太烂，有人写了一篇博客介绍有多烂，冲上了 HN 热搜： [The Worst Website In The Entire World](https://matduggan.com/the-worst-website-in-the-entire-world/)


---

[Meta is shutting down Workplace](https://world.hey.com/dhh/meta-is-shutting-down-workplace-3e24bca5)

[Meta](/mentions/meta) 关掉了 Workplace 产品。Meta 和 Google 这类公司的主要业务来钱太容易，以至于 Workplace 那么点用户带来的利润实在是不够看，任何一个策略转换随时可能被干掉。

不要使用所有大公司非核心产品。`非核心==非主要利润来源`。

---

[Ep 46. 你知道『赛博佛祖』Cloudflare 吗？ - 捕蛇者说](https://pythonhunter.org/episodes/ep46)

[CloudFlare](/mentions/cloudflare) 的 R2 产品名字，是要比 AWS [S3](/mentions/s3) 少一点，有趣。

---

[Get Involved with Fedora Bootable Containers - Fedora Magazine](https://fedoramagazine.org/get-involved-with-fedora-bootable-containers/)

感觉上 [Fedora](/mentions/fedora) 在积极的维护 Atomic Desktops 相关项目了，允许每个人都可以构建自己的发行版真的很吸引人，我一直想要尝试，可惜没有投入。

[bootc](/mentions/bootc) 项目的潜力感觉要比想象中的更大？

---




### 生活


[去东京 | 卡瓦邦噶！](https://www.kawabangga.com/posts/5943)

[去伊豆 | 卡瓦邦噶！](https://www.kawabangga.com/posts/5945)

>地铁站设计复杂。很多列车的两个反方向站台是只有一条路过去的，很容易坐反方向。不过我摸索出一个窍门，东京的地铁每一个线路都有编号，比如 G，JR，JT，等等，每一个站都有标号，比如 G9，G10，G11. 如果你要去一个地方，先查看目的地的编号，比如 G8，然后看当前位置，比如是 G4，那么找到站台之后，确认方向是数字变大的方向，就对了。

[日本](/posts/日本) [东京](/posts/东京) 和[伊豆](/posts/伊豆) [游记](/posts/游记)。

日本地铁哪怕是同一个站，但是不同的线路可能是无法连通的，因为东京的铁路是由不同的公司运营的。

---


[鱼跃 Anytime CT 15 血糖监测仪体验 & 个人心得分享 - 白宦成](https://www.ixiqin.com/2024/05/14/experience-of-fish-leap-anytime-ct-15-blood-glucose/)

[鱼跃](/posts/鱼跃)血糖检测仪使用体验。最近读完《控糖革命》之后，也萌生出要不要搞一个血糖检测仪来监控血糖的想法，但是又觉得有些麻烦，洗澡倒是没有影响，但是价格真的不便宜，一年需要 250 * （52/2） = 6500 元左右，这个是持续成本，可以说是非常高了。

---

## 书影

《恋爱兄妹》，唯一还在看的影视作品（如果综艺也算的话），如果你确定了对方是你想要找的那个人，过于直接是否会吓到对方？

## 碎碎念

* 突然冒出了，回家待一周的念头。
* 喝酒，聊天，可以很好的消解一些压抑。
* 呵呵的英文是什么？ interesting 。