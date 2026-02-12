---
title: Weekly Issue-《坐在角落的人》
date: "2025-01-19T00:00:00.000Z"
slug: "Weekly-Issue-坐在角落的人"
tags:
  - Weekly
description:
---

## 文章

### 技术

[CPU 越多，延迟越高的问题排查 | 卡瓦邦噶！](https://www.kawabangga.com/posts/6793)

[【BPF网络篇系列-2】容器网络延时之 ipvs 定时器篇 | Head First eBPF](https://www.ebpf.top/post/ebpf_network_kpatch_ipvs/)

[[IPVS]] 的统计函数 `estimation_timer` 导致的网络延迟。

排查过程中提到的工具有：
- [GitHub - bytedance/trace-irqoff: Interrupts-off or softirqs-off latency tracer](https://github.com/bytedance/trace-irqoff)
- [ICMP packet tracer using BCC · GitHub](https://gist.github.com/DavadDi/62ee75228f03631c845c51af292c2b17)
- perf
- [perf-tools/bin/funcgraph at master · brendangregg/perf-tools · GitHub](https://github.com/brendangregg/perf-tools/blob/master/bin/funcgraph)

---

[Faith Driven Development](https://engineering.autotrader.co.uk/2023/07/11/faith-driven-development.html)

> We’ve defined FDD as “A development process in which modifications to the code are tested by pushing them straight in and seeing what happens.”. We are relying on little more than a developer’s faith in their own ability.

FDD，有时候想要快速修复一个问题而直接 push 代码，引发了更多的问题。想到了之前看过的另一篇文章： [The story of the one line fix | Dave Cheney](https://dave.cheney.net/2020/12/15/the-story-of-the-one-line-fix) 。

---

[Downtown Doug Brown » Why is my CPU usage always 100%? (Upgrading my Chumby 8 kernel part 9)](https://www.downtowndougbrown.com/2024/04/why-is-my-cpu-usage-always-100-upgrading-my-chumby-8-kernel-part-9/)

从 CPU Usage 去调查，先去调查 `top` 的计算方式，然后去看 `/proc/stat` 实现，最终调查到和硬件定时器相关。

---


[DBOS | Build Reliable Backends 10x Faster, Scale to Millions with 1 Click](https://www.dbos.dev/)

[[DBOS]]，基于 [[PostgreSQL]] 实现的代码框架，可以执行 workflow/task/job/.... 相较于 [[Temporal]] 需要 Server 和 Worker，DBOS 只是一个 Lib，目前提供了 TypeScript 和 Python 两个语言的 SDK。自身有 Cloud 服务，应该也可以本地化运行？

我尝试搜索 DBOS 名字的含义，本能的有些抗拒这个名字，像是蹭热度（即使 DB 或 OS 都不是啥大热点）。

---


[So You Want to Build Your Own Data Center](https://blog.railway.com/p/data-center-build-part-one)

> This all seems very far removed from software, DevOps, or what you’d typically think of as “infrastructure,” and that is very true — building a datacenter cage is probably closer to building a house than to deploying a Terraform stack.

[[Railway]] 最初是基于 GCP 构建的，之前写过博客吐槽 [[GCP]] 的体验很糟糕，这篇文章讲述了他们自建基础设施的故事（租用了数据中心的一个笼子），包含了网络、电力、制冷相关的考虑。很喜欢引用中的这句话，Infrastructure 这个词包含的范围超过想象。

对应岗位的 JD 中的一句话： “Delivered projects 0→N. Lead it, scaled it, seen your “brilliant solutions” become tech debt, etc”

---

[Benchmarking Gob vs JSON, XML & YAML | by Roman Sheremeta | Medium](https://rsheremeta.medium.com/benchmarking-gob-vs-json-xml-yaml-48b090b097e8)

[Benchmarking Gob vs Protobuf. This article is a Part 2 of my… | by Roman Sheremeta | Medium](https://rsheremeta.medium.com/benchmarking-gob-vs-protobuf-9dc36ea56ba4)

[[Golang]] 中常见的序列化方式性能比较。如果需要在 Gob 和 protobuf 中选择，直接选择 protobuf 就好。

---




### 生活

[I do NOT like message recall/replacement - Zhiqiang's backyard](https://strrl.dev/post/2024/i-do-not-like-message-recall-or-replace/)

如果自己发送出去的消息有问题，尽量不要“撤回”、“删除”、“替换”，应该保留编辑的痕迹。至少不会让同一个 thread 对话里面的其他人显得很傻。

---

[新疆二十日（下）：古道高原，南疆的冰与火之歌 - Simon's Blog](https://song.al/xinjiang2)

[[新疆]] [[游记]]，太美了，看照片已经心情变好。

---

[一个记录者眼中，真实的缅甸电诈、危险与人性](https://archive.is/9hbj7)

[我在泰缅边境调查电诈产业 200 天](https://archive.is/locIk)

> 王星事件之后，网上流传出千余名受害者家属联名求救的表格，我看了之后百感交集。在很多家长眼里，自己的小孩是很乖的，都是被骗过去的。不排除会有一些受害者，但我倾向于认为，大部分人不是被骗过去的。

> 可我想说的是，其实在很多案例中，蛇头和报名的人是心照不宣的。大家都不会直接说去做诈骗，但其实也都知道剧本只是用来自欺欺人。

> 其实电诈园区跟国内的一些科技园区（的设施）没什么区别，里面有生活区，有写字楼，也有配套的餐厅。小一点的电诈公司窝点就设在宾馆里，一般老板会把两三层楼承包下来，把它改成办公区，进行电诈活动。园区里还养活了许多餐饮、超市和娱乐场所，形成了完整的闭环生态。

> 从过去到现在，我们谈了很多年的电诈，但隐私问题却谈得很少。其实这些东西才是看不见的黑洞。
> 

最近缅甸诈骗的事情很火热，有些同事也在聊是否还会去泰国旅游，由于可能涉及到一些观点上的冲突，这个话题其实很难聊。从这两篇文章和花总的采访中，其实不难看出，一些“受害者”口中的“骗”，不是“诈骗”，更多的可能是利益不满足自己的期望。

---

[Shape Up 阅读笔记（2）- 基本工作模式](https://xiaowenz.com/blog/2025/01/shape-up-methodology-2/)   
[Shape Up 阅读笔记（3）- Shaping: 如何真正对需求负责](https://xiaowenz.com/blog/2025/01/shape-up-methodology-3/)   
[Shape Up 阅读笔记（4）- Betting: 决策最重要的是发生在正确的层级](https://xiaowenz.com/blog/2025/01/shape-up-methodology-4/)   
[Shape Up 阅读笔记（5）- Building: 软件项目应该有的样子](https://xiaowenz.com/blog/2025/01/shape-up-methodology-5/)   

> 整个公司不同产品线的研发工作，都强制使用同样的工作节奏。
>  - 原因：允许不同周期的项目并行，会导致资源的调配越来越复杂，最终项目管理工作变成了 Calendar 上的甘特图游戏，疲劳而无效 

> 整个公司不同产品线的研发工作，都强制使用同样的工作节奏。
>  - 原因：允许不同周期的项目并行，会导致资源的调配越来越复杂，最终项目管理工作变成了 Calendar 上的甘特图游戏，疲劳而无效。


> - 6 周时间的长度是价值和投入之间比较合适的比例。
>     - 更短的周期会导致需求太过碎片，太频繁的「Planning」会导致项目管理成本太高。

> - 当每个人只是对 Task 负责，没有人对整个事情有责任感，项目的效果往往会走样。因此 Building 的核心意义是：让团队对一个指定范围内的价值交付（Pitch）端到端负责。

---



## 书影


《冬泳》，班宇。本周读完了，最喜欢的三个故事是前三个：盘锦豹子、肃杀、冬泳。班宇好像对“水”有一些特殊的情感，试图用“水”来化解一切。

《坐在角落的人》，梁海源，单口喜剧专场。这个专场有两个版本，分别是《坐在角落的人》和《坐在角落的人2》，按照之前播客中的说法，在巡演过程中不断的迭代，最终两个版本的内容差别已经有一些了，所以加了 `2` ，专场线下全国巡演时我没抢到票，现在腾讯有了线上版本，线上和线下一定是有差距的，无论是观看氛围还是内容审核，是一定有缩水的，所以在豆瓣上有些差评可以理解。不同类型的专场差别很大，有些专场的内容，只适合看一遍，有些适合没事看看，这个专场就属于后者，像是一个多年没见的朋友跟你聊聊天。

《归途》，花总，柬埔寨缅甸，诈骗纪实拍摄。不要相信任何一个试图捞偏门的人说的话。

## 碎碎念

* 有些库如果定位是面向人类友好的，那么可能会会对严肃场合留下一些坑，比如 Python Rich 会自动根据 Console size 调整输出缩略。
* 现在可能真的是有点用户了，以前没感觉，一个觉得发生概率很低的问题，一年下来 case 也不少。
* 每当我想着，这个 PR 体量会不会有点大了？就去看看 Logseq 的 Database PR。嗯，不大，一点也不大。
* EOL 和 EOS 是两个不同的含义，EOL 表示产品停止更新（但是可能还会提供技术支持），EOS 表示产品不提供技术支持。
* 中午吃饭，被同事说我反思太多。我应该反思一下，是这样么？
* 有些书，阅读的时间非常重要，最好在适当的时候去阅读那些书，或早或晚收益差别会很大。“你知不知道什么叫做timing啊？”
* 迪卡侬补胎需要排队，理发店理发需要排队，年底了好像什么事情都多了起来。






