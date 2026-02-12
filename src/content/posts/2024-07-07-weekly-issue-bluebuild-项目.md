---
title: Weekly Issue-BlueBuild 项目
date: "2024-07-07T00:00:00.000Z"
slug: "Weekly-Issue-BlueBuild-项目"
tags:
  - Weekly
description:
---

## 文章

### 技术

[关于旅游期间博客再次被攻击一事 - 陪她去流浪](https://blog.twofei.com/1431/)

> 这些坏人好像非常熟悉我/非常清楚我的动向一样，偏偏选在我旅游/不方便的时间段。

想到了 xz 的攻击也是发生在作者在 internet break 的时候。。。朴实无华

---

[Ultra-small Ubuntu-based distroless containers - chiselled Ubuntu | Ubuntu](https://ubuntu.com/containers/chiselled)

[[ubuntu]] 提供了一个类似于 [[Distroless]] 的 container image，基于 [[Debian]] 包直接进行裁剪，通过 `chisel` 来构建（裁剪） image ，`chisel` 相当于是一个包管理器，只是这个包管理器的操作粒度是到文件级别。按照官方的介绍，最终 image 大小缩减的效果很好。

[[Canonical]] 提供 Chiselled Ubuntu 的 5 年免费支持和 10 年的付费支持。

---

[[翻译] 聚焦 VictoriaMetrics：一家乌克兰初创企业的故事](https://jiekun.dev/posts/one-to-watch-victoriametrics/)

>该公司有机地进行招聘，仅依靠 10 至 20 名员工运作，并广泛使用 Contractors。与硅谷一些热门的初创公司不同，它目前没有计划寻求大规模的融资。
>
“我们对来自企业业务的收入感到满意，” Khavronenko 说道。“这足以支持我们的团队扩张、发展和开发新的解决方案。”

---

[From bare metal to a 70B model: infrastructure set-up and scripts - imbue](https://imbue.com/research/70b-infrastructure/)

> As is typical in setting up large GPU clusters, we found that about 10% of the machines failed to boot, mostly due to physical issues with the servers. Some issues we encountered included: unconnected or miswired Ethernet cables, hardware issues in iDRAC, broken power supply units, bad NVME (nonvolatile memory express) drives, missing internal wires, and network cards or GPUs failing to show up.
> 
> A rule of thumb for GPU clusters using the newest hardware: expect about 3% of machines to break every week.


[[Imbue]] 介绍自己如何维护 511 台节点组成的训练集群，这套集群仅 GPU 价格就超过了 1 亿美元，大规模的 GPU 集群故障率有点太高了。

他们使用 [[MAAS]] 来置备服务器，但是 MAAS 与 BMC 的集成不可靠，所以提前通过 iDrac API 获取了没太服务器的 MAC 地址。

---

[Reasons to use your shell's job control](https://jvns.ca/blog/2024/07/03/reasons-to-use-job-control/)

日常好像很少使用 job control。其中使用的场景有一个终止不响应 Ctrl-C 的命令，好像很有用。

---

[The saddest "Just Ship It" story ever](https://www.kitze.io/posts/saddest-just-ship-it-story-ever)

很多时候因为想要做的更好而没有交付出实际的产品，最终可能想要做的东西也没有做出来。
有时候先搞出一个 MVP 出来，至少先用起来，可能不够好用，但是有了第一步，才有可能有后续。

---

[For the Love of God, Stop Using CPU Limits on Kubernetes (Updated) | Robusta](https://home.robusta.dev/blog/stop-using-cpu-limits)

[[kubernetes]] 如何设置 Pod 的 request 和 limit：
- CPU
	- 始终设置 CPU requests
	- 确保 CPU requests 正确性
	- 不要设置 CPU limits
- Memory
	- 始终设置 Memory limits
	- 始终设置 Memory requests
	- 始终设置 Memory requests 等于 limits （底线）

---

[Booting Linux off of Google Drive | Ersei 'n Stuff](https://ersei.net/en/blog/fuse-root)

作者将系统的 rootfs 放在 Google Drive 上，并在引导阶段在 initramfs 将起挂载。纯属娱乐。

---
[Aeon: openSUSE for lazy developers [LWN.net]](https://lwn.net/Articles/977987/)

[[openSUSE]] 的 [[Aeon]]（以前叫 MicroOS）近期更新了，Aeon 的目标是使用只读文件系统，进行原子化更新，来减轻维护负担。Aeon 使用 Cypper 和 Btrfs subvolume 来实现的。

对于这种将操作系统级别的动作依赖于 Btrfs 能力，如果用户想要在 Btrfs 上做更多的事情，是否会产生冲突？

---



### 生活

[With Nothing to Do - by Thorsten Ball - Register Spill](https://registerspill.thorstenball.com/p/with-nothing-to-do)

>It says: “I want my work to count. It should _matter_.”

作者 8 年前工作的公司，处于破产的边缘，当时大家无事可做，听上去很美好，有人发工资，你可以坐在电脑前做任何想做的事情，但实际上会让人产生空虚感。

---

[人人都能写英文博客 | Piglei](https://www.piglei.com/articles/everyone-can-write-eng-blog/)

>记得发布完第一篇英文文章后，深圳已经进入深夜，但因为时差原因，文章在 Reddit 和 Hacker News 的热度却在一路走高。看着 vote 数和评论数不断增长，我兴奋得完全无法入睡，几乎每隔三十分钟就要抓起手机，看一遍最新的访问数据。
>
>后来几经辗转，终于进入了梦乡。我已经忘了那晚梦见了什么，但我能想起的是，第二天早晨醒来后，我感受到了一种就像是刚刚学会写字时的喜悦。

使用 GPT 配合 DeepL 来将中文博客翻译为英文，收获了很多高质量的评论（讨论）。为啥中文博客没啥讨论氛围呢？ 

---


## 书影

《南洋大宝荐-神鬼传奇》，食贫道充电视频，通过采访佛教僧人、泰拳小孩、变性人来看泰国。是什么让人心安，是佛么？是金钱，如果恶魔能带来金钱，那么恶魔就能带来心安。


## 碎碎念

* 一件事物想要代替另一件事物，但是最终失败了的例子：电子书 vs 纸质书、胶片电影 vs 数码电影。
* 看到了一个地狱笑话：哪吒的骨灰是藕粉么
* 我很喜欢有“人味”的朋友，让我感觉大家是真实的，是有困扰的、是有不解的。那是个人啊，是个和我们大部分人同龄的人。
* 上海最近太热了，38 度，已经完全不适合生活了，加上最近洞庭湖决堤的新闻，发现选一个好的生活地点是很重要的，比如经常能听到新闻说发大水的地方，是不适合生活的。

### BlueBuild

https://blue-build.org/

周末想要基于 Fedora SilverBlue 来将自己的开发机 IaC 化，看到了 BlueBuild，项目整体处于非常早期的阶段，项目的背景是，由于 uBlue 整体都是采用 ContainerFile + fs config files 的方式来构建的，对于新手不友好，所以基于常用的操作，进行了一层封装，比如指定安装 RPM，指定安装 Flatpak 等等，可以让新人快速上手来得到一个自己的发行版。

项目目前在快速开发中，等开发完成并完善文档后，对新人可能会很友好。但是这类项目都有一个问题，就是抽象出来的东西，一旦无法覆盖自己想要完成的动作，最终还是会回退到 Containerfile 的方式，是不可避免的，只能去抽象更多的资源类型来适配。可能对于熟练的人来说，不如直接使用 Containerfile 了。