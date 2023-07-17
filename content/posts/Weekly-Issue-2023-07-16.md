---
title: Weekly Issue 2023-07-16
date: 2023-07-16
tags:
- Weekly
description: 我的周末：凌晨、骑车、摔倒、回家。
---


## 文章

### 技术

[Towards Technical CEOs](https://matt-rickard.com/towards-technical-ceos)

[[Shopify]] CEO 给 llama.cpp 项目提了一个 PR，技术型老板可以让他们看到更多信息，技术敏感很重要，可以快速了解当前的趋势。有一个技术型老板应该很开心吧。

---

https://ricardoanderegg.com/posts/makefile-python-project-tricks/

[[Python]] 项目中使用 [[Makefile]] 的一些技巧，如 `venv` 设置，help message 输出，`PYTHONPATH` 设置等。


---


[答案在代码中：“实现需求”的双重含义  | Piglei](https://www.piglei.com/articles/the-answer-is-in-the-code-fulfill-requirements/)

**是否能通过读代码来轻松还原需求** 的能力很重要，有时候写一些隐式的条件判断，很容易在后续修改的时候就产生 regression 。

---

[Building a tiny 6-drive M.2 NAS with the Rock 5 model B | Jeff Geerling](https://www.jeffgeerling.com/blog/2023/building-tiny-6-drive-m2-nas-rock-5-model-b)

使用 Rock5 配合 6个 M.2 的磁盘组成的小型 NAS。（我一直觉得没有那么多数据要存储

---

[RSS Vs Atom Feeds In 2023: Unveiling The Ultimate Winner](https://www.cjco.com.au/article/rss-vs-atom-feeds-the-shocking-truth-about-the-battle-for-internet-supremacy-in-2023-are-you-prepared/)

作为用户其实我不是很关心 rss /atom 具体差异，Atom 中提供了哪些新的属性对我来说改善真的不大，毕竟现在各个阅读器的阅读体验永远也比不了源站点，只要能稳定长久的提供就可以了，很多资源都没办法做到稳定长久的提供订阅地址，没有资格谈论 rss vs atom 这个话题。

---

[Technology Radar | An opinionated guide to technology frontiers | Thoughtworks](https://www.thoughtworks.com/radar)

[[thoughtworks]] 技术雷达，会定期更新，对技术/平台/趋势进行评估。

---

https://almalinux.org/blog/future-of-almalinux/
[[AlmaLinux]] 因为 [[RHEL]] 事件，放弃了与 [[RHEL]] 1:1 兼容，只保证 ABI 兼容。后续上游采用 CentOS Stream。

---

[Goodbye etcd, Hello PostgreSQL: Running Kubernetes with an SQL Database | by Martin Heinz | Jul, 2023 | Better Programming](https://betterprogramming.pub/goodbye-etcd-hello-postgresql-running-kubernetes-with-an-sql-database-7e1b2e9b5f8f)

使用[[PostgreSQL]] 配合 [[Kine]] 运行 [[kubernetes]]。其中 PG 通过 systemd 控制，Kine 通过 StaticPod 控制。应该只是看看就好，etcd 目前有了 Kubernetes SIG，开始积极维护中了。Kine 的问题也不少。

---

[Why We Replaced Firecracker with QEMU | Hocus Blog](https://hocus.dev/blog/qemu-vs-firecracker/)

[[Hocus]] 对比 [[Firecracker]] 与 [[QEMU]]，比最终选择[[QEMU]]， [[Firecracker]] 不支持 [[GPU]]，磁盘 IO 性能也不如 QEMU。  
其中提到 [[Firecracker]] 的 [[Ballooning]]  不可用，有点不符合预期。

---



### 生活

[我的北京个人房源获取攻略2023加强版](https://mp.weixin.qq.com/s?__biz=MzAxMTA1NDU3NQ==&mid=2651060397&idx=1&sn=70cce7df9a0ca0d0c9d6d609e52eff69&chksm=80b1a42db7c62d3b3d09552a589716760a29a0daa8e30f00d8958eaac05d4931701f74c7d7aa&token=1389249657&lang=zh_CN#rd)

[[租房]]经验，其中提到 [[小红书]] 是现在一个不错的方式了。

---

[电梯理论 - 知乎](https://zhuanlan.zhihu.com/p/113312424)

> 什么是电梯理论？  
一个人乘坐电梯到达了摩天大厦的顶楼，但在乘坐电梯的同时，他也在电梯里做了几个俯卧撑。  
到达顶楼后，他解释自己之所以可以到达顶楼，完全是自己努力做俯卧撑的结果。  
完全忽略了电梯的存在。  

要对自己有清晰的认知啊。

---

[dashing dog, searching for purpose | Derek Sivers](https://sive.rs/pdog)

> **Focus on what fascinates you**, no matter how uncharacteristic. **There is no purpose because there is no line connecting moments in time.** There is no plot. You are not a story.  

不要去追求"目标"和"目的",而是专注于当前自己真正在做的事情及感兴趣的事物，过分追求"目标"可能会限制我们的视野,忽略其他可能更有意义的事物，不要被"目标"和"目的"这些标签限制自己。"目标"可能更多的是为了满足我们社会化的需求,让自己显得有个"目的"和"方向"。但实际上,一个个有吸引力的工作任务,而不是个抽象的"目标",才是真正推动我们的力量。

---


## 书影


《运气的诱饵》，赌场中的一切设施、服务、规则都是为了一件事：让顾客去最方便最长时间的在赌桌上。每一个你能感受到的事务，都是经过了精心的设计，包括如何让顾客不那么的抵触，如果让顾客很舒服的去长时间坐着，都是一门学问。套用身边的例子，网吧可以想象为低配版的赌场。

《人生路不熟》，好久没看过这么难看的电影了，套路化严重，之前以为是最近的演员出了问题，现在看是导演和编剧出了问题，演员很卖力，但是方向错了再卖力也不讨好。

《羊毛战记》，属于设定决定剧情的剧，第一部注水严重，感觉为了10集而10集，如果第二部设定展开崩坏，那就会急转直下。

