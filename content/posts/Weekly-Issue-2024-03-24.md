---
title: Weekly Issue 2024-03-24
date: 2024-03-24
tags:
- Weekly
description:  难。
---


## 文章

### 技术

[字节跳动新型网络装机方案HTTPBOOT(Linux)，轻松解决运维困扰 - 知乎](https://zhuanlan.zhihu.com/p/686954625)

[[字节跳动]] 网络安装操作系统方案，采用 LinuxRoot 配合 u-root 来实现。


---


[In Defense of Shell Scripts](https://certomodo.io/best-practices/in-defense-of-shell-scripts.html)

对于 [[shell]] 所能做到的事情，一直是毫不怀疑的，甚至如果日常中有什么需要快速实现的，我也会选择 [[shell]]，但是如果要产品化的话，选择其他编程语言是一个正确的选择。

我在工作中维护的组件涉及到很多与磁盘交互的功能，比如分区、格式化，这些是符合作者所说的“When CLI tools are available, and APIs aren’t”，随着功能的迭代，分支的增多，无法快速的编写单测，现在带来的测试负担已经非常重了。

---

[Fragments | Docker Docs](https://docs.docker.com/compose/compose-file/10-fragments/)

[[docker]] [[compose]] 的 Fragments 能力，可以用来创建复用的配置。示例：

```
services:
  first:
    image: my-image:latest
    environment: &env
      - CONFIG_KEY
      - EXAMPLE_KEY
      - DEMO_VAR
  second:
    image: another-image:latest
    environment: *env
```

---


[Recent troubleshooting cases from our SREs, part 5. An unexpected crash due to unrelated software changes – Palark | Blog](https://blog.palark.com/sre-troubleshooting-ceph-systemd-containerd/)

[[Palark]] 内部 [[kubernetes]] 集群 [[事故分析]]。

内部的日志存储系统运行在 [[kubernetes]] 上，依赖于 [[S3]]，[[S3]] 由使用 [[Rook]] 部署的 [[Ceph]] 集群提供。这套部署模式一致在不同的虚拟化环境和不同的发行版之间进行部署，都没有遇到问题。

[[Rook]] 在部署 Ceph 时，发现 Ceph 没有正常工作，Operator log 中包含大量的超时请求，日志中没有明显的错误，Monitor 只有在某个时刻收到的 TERM 信号。

尝试把 probe 禁掉，但是只是停止了重新启动，并没有更多用处。（通常如果我遇到被外部检测 kill 的情况，第一时间也会选择禁用外部检测，来看看是否只是因为某些其他原因 timeout。）

接着检查 infra 相关指标，比如硬盘状态、网络、防火墙、等等，没有发现。

接着排查 ROOK 自身，发现是 `ceph osd pool create` 命令导致的。

同时在 Github Issue 中找到了具体的原因：[Ceph monitors in crash loop · Issue #10110 · rook/rook · GitHub](https://github.com/rook/rook/issues/10110#issuecomment-1464898937)：

最终是在 `containerd.service` 中添加 `LimitNOFILE=1048576` 作为临时方案。

为什么其他发行版没有这个问题？因为它们针对 systemd 打了相关的 patch。

---

[X](https://twitter.com/realhashbreaker/status/1770161965006008570)

[[md5]] 碰撞的真实例子，是可打印的 ASCII 发生冲突。

md5("TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak") = md5("TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak")

---

[Stripe’s 2023 annual letter](https://stripe.com/en-ca/annual-updates/2023)

[[Stripe]] 的年终总结，处理了 1 万亿美元，相当于全球 GDP 的 1%。

Stripe 核心 API 服务每天会发生 400 次的变更，提交代码后，就会通过 140 万次测试进行验证。每天使用 50 万个 CPU 核心执行超过 60 亿次测试运行。测试范围不断扩大：从简单的样式检查，到单独验证每个组件的单元测试，再到验证端到端系统是否按预期工作的集成测试。如果更改未通过任何测试，则部署停止。

---

[Redis Adopts Dual Source-Available Licensing | Redis](https://redis.com/blog/redis-adopts-dual-source-available-licensing/)

[[redis]] 更改了相关开源协议的说明。对于提供 [[redis]] 竞争服务的公司，无法继续使用后续版本的 [[redis]]。

---

[Linux Crisis Tools](https://www.brendangregg.com/blog//2024-03-24/linux-crisis-tools.html)

[[Linux]] debug 必备的工具集：包含基本的 ps, vmstate, lsblk, iostat, tcpdump 等等，还建议包含 bcc-tools 和 bpftrace 相关工具集。

可能有人问，是否可以在需要的时候再进行安装？大部分生产环境中想要安装这些工作都不太容易：网络、权限、系统配置等等因素导致的。

---

[The Basics - by Thorsten Ball - Register Spill](https://registerspill.thorstenball.com/p/the-basics)

一些基础知识，或者说规则：
- 手动测试一下，当写完代码之后，手动测试一下，确保基本的功能是符合预期的
- 考虑边缘情况，及时不需要立即处理，也需要有一个完整的概念
- 确保当前的 PR 不包含不相关的更改
- 确保 PR 与主分支保持同步
- 在评论某件事情之前，先完整的了解这件事情
- 在开会之前需要做好准备
- 了解您正在解决什么问题。了解你为什么要做某事是了解你是否真正解决问题的必要条件
- 接受有时你不得不做一些你觉得不有趣或令人兴奋或不能给你带来快乐的事情。有时这只是工作
- 在发出提问时，要写清楚背景、做了什么、发生了什么、期望发生什么、做了什么尝试
- 阅读粗无信息、文档、手册、说明
- 要准时
- 知道为什么你的修复是一个修复
- 添加测试时，要实际验证这个测试是否会失败
- 做你说过要做的事。如果由于某种原因你不能，让假设你正在做某事的人知道这件事
- 当你从不审查别人的代码时，不要要求“快速”审查
- 始终留意错误
- 让他人愿意与你合作作为一个目标

---




### 生活

[X 上的 Nikita Bier：“At Facebook, I coined a term called Filipino Product Market-Fit: Every year a product manager would observe their new product getting intense adoption in the Phillipines and proclaim their idea was working. Directors would quickly staff the team and alert their VPs of the…” / X](https://twitter.com/nikitabier/status/1768304243620880766)


在 Facebook，我创造了一个术语“菲律宾产品市场契合度”： 每年，产品经理都会观察到他们的新产品在菲律宾得到广泛采用，并宣称他们的想法正在发挥作用。主管们会迅速为团队配备人员，并向副总裁通报这一新发现，结果却发现这种模式在其他国家无法重现。菲律宾是世界上上网时间最长的国家之一，他们会在几天内尝试任何事情。

---

[Musk’s Neuralink Shows First Patient Playing Chess With Mind](https://www.bloomberg.com/news/articles/2024-03-20/musk-s-neuralink-gives-update-on-first-brain-implant-patient)

[[Neuralink]] 脑机接口已经可以玩游戏了，感觉是跨时代的发展。

---

[美团骑手转职指南 | 地瓜的博客](https://digua.moe/posts/20240311-meituan-rider.html)

作者本职工作是一名程序员，在周末体验了两天美团骑手。
- 不要点过于便宜的外卖：
	- 第一天抢到一个猪脚饭的单子，顾客实付 23.38，我拿到 10.7 的配送费，震惊到我，外加 4.7 元的配送奖励，相当于我从这单里赚了 15.4 元。

---



## 书影

《炸鸡块奇遇记》，很难评。


## 碎碎念

* 如果你期待大众都理解你 那你得愚昧成什么样。
* XG（ Xtraordinary Girls 的缩写）是一个总部位于韩国的日本女子组合。Cocona 的 RAP 真好听啊
* 
