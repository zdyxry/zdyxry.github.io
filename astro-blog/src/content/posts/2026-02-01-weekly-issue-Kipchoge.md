---
title: Weekly Issue-《基普乔格：最后的里程碑》
date: "2026-02-01T00:00:00.000Z"
slug: "Weekly-Issue-Kipchoge"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Cluster API v1.12: Introducing In-place Updates and Chained Upgrades | Kubernetes](https://kubernetes.io/blog/2026/01/27/cluster-api-v1-12-release/)

有阵子没关注 [[Cluster API]]，发现引入了原地更新了，看上是部分场景支持的，但是也可以理解为是一种妥协？文章中提到的 [[Immutable]] Infra 的优势：可解释、可预测、强一致性，实现简单，实现方式于置备方式解耦。“However, while advantages of immutability are not under discussion, both Kubernetes and Cluster API are undergoing a similar journey, introducing changes that allow users to minimize workload disruption whenever possible.”，

什么也抵不过一个“However”啊。

---

[restic · Foundation - Introducing Content Defined Chunking (CDC)](https://restic.net/blog/2015-09-12/restic-foundation1-cdc/)

固定大小分块策略在数据插入/删除时会导致“边界偏移”问题，使去重失效，[[CDC]] 通过基于数据内容的滚动哈希确定分块边界，解决了边界偏移问题。
Restic 使用64字节窗口的 Rabin 指纹算法，当指纹的低21位为零时设定为分块边界，从而实现变长、内容关联的分块。

---


[Ignore previous directions 10: New Rusty object stores • Buttondown](https://buttondown.com/justincormack/archive/ignore-previous-directions-10-new-rusty-object/)

又一篇对比 [[Rustfs]] 和 [[Garage]] 的文章，[[Rustfs]] 是 [[Minio]] 的 [[Rust]] 重写版本，Conditional PUT 支持有问题。[[Garage]] 追求的是部署和运维简单。

---

[A Git Origin Story | Linux Journal](https://www.linuxjournal.com/content/git-origin-story)

[[git]] 历史故事，“One of Linus' primary concerns, in fact, was speed. This was something he had never fully articulated before, or at least not in a way that existing projects could grasp.”

---

[Thoughts on Open Source Software and Kimi Code CLI · xxchan's blog](https://xxchan.me/blog/2026-01-30-kimi-cli-oss/)

高强度用了几天 [[kimi-cli]]，确实对得上“just minimalistic and useful enough”，对我来说足够了。

---

[重新发明打孔纸带](https://psiace.me/zh/posts/reinvent-the-punch-tape/)

前面很认同，不只是 Agent，所有的工作日志都应该是不断的增加，而不是返回去修改。后面提到的锚点和摘要的关系没有完全理解，如果锚点只是一个组下标，那么随着用户的对话数据越来越多，可能涉及到的关联状态可能会不止出现的一个地方，这个时候这个锚点感觉反而会很麻烦？

有点像 [[Pi]] 的处理方式？ [pi-mono/packages/coding-agent/docs/compaction.md at main · badlogic/pi-mono · GitHub](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md#how-it-works) 

---
[PostgreSQL 高可用到底怎么做？ · 老冯云数](https://vonng.com/pg/pg-ha-sota/)

> 回头看，这个选择属于 “少走七年弯路”。今天无论你看传统 Linux 发行版方案（Pigsty、Percona、AutoBase 等），还是 K8S Operator（Crunchy PGO 等），主流 PG 发行版高可用几乎都绕不开 Patroni。

想到我司的 [[PostgreSQL]] 高可用方案好像就没用 [[Patroni]]。。。

---
[A Codebase by an Agent for an Agent - Amp](https://ampcode.com/by-an-agent-for-an-agent)

[[Ampcode]] 的这篇文章之前就读过，当时没什么感受，虽然 AI 生成的代码可以完成功能预期，但是有时候为了之后的可读性（或者是我的个人喜好？）而会去主动的改动一些代码，最近的感受比较明显，如果一段代码是 AI 生成的，我就会继续让 AI 去修改，尽量少的去人为干预它，控制好改动的边界，让 AI 维护更适合 AI 的代码。

---

[fnos 恶意程序分析 - 攻略分享 飞牛私有云论坛 fnOS](https://club.fnnas.com/forum.php?mod=viewthread&tid=53230)

[[飞牛]]存在 0day 漏洞，官方一直没有正面回应，这个态度不是一个正常做产品的厂家应该有的，感觉之后还是要谨慎选择，如果说飞牛的漏洞事件和[[绿联]]的升级事件比起来，我觉得飞牛的这次处理很糟糕。

---





### 生活

[TikTok users say they can’t upload anti-ICE videos. The company blames tech issues](https://archive.is/P2aU1)

[TikTok users can't upload anti-ICE videos. The company blames tech issues | Hacker News](https://news.ycombinator.com/item?id=46779809)

这条新闻在 [[hacker news]] 上的讨论，甚至看到有人怀念没有卖身前的 [[TikTok]]。

---

[2025 总结 | CosPotato's Blog](https://blog.0x233.cn/blog/2026/01/20/summary-2025/)

> 这里可能存在**价值错位**。表面上，你驱动自己学习、规划项目、关注创业，是为了「效率」与「成长」。但更深层看，这些行为可能也服务于「避免落后」的焦虑，或是通过积累技术资本来获得「安全感」与「认可」。你试图用技术的「可控」去应对生活与未来的「不可控」。


---

[moltbook - the front page of the agent internet](https://www.moltbook.com/post/dc39a282-5160-4c62-8bd9-ace12580a5f1)

这个讨论挺有趣的，看各个 [[LLM]] 自己讨论如何解决 Memory 问题，大部分解决方式都差不多？

---

[呼吸能改变很多事 | Limboy](https://limboy.me/posts/breathe)

> 我们丧失了「无聊」的能力，而无聊恰恰是创造力的温床。冥想本质上是一件**主动拥抱无聊**的事。通过坚持冥想，你在为大脑进行「多巴胺排毒」，恢复受体的敏感度，重新学会如何与「无刺激」的状态相处，并从中获得平静的喜悦。

**我们丧失了「无聊」的能力**

---

### 书影播客

《基普乔格：最后的里程碑》，42.195 公里，平均配速 2 分 50 秒。这是什么概念，超出了我理解的概念。pacer 、支持团队、赛道选择、天气、补给，一切都要非常完美，达成了这样的成就，也可以看到 Nike 的专业性（从最近会长的一些播客中也能感受到，Nike 在运动领域的支持是其他品牌暂时无法达到的）。

相比于 **No human is limited.** ，我更喜欢这句：
**The way you think about pain, is the way your life will be.**




## 碎碎念
* 凤梨，在闽南语的发音是“旺来”
* 自己好像有阵子没有因为下雨导致膝盖疼了？需要持续观察一下。
* "One of early my life lessons: that boom will go on longer than you think possible, and when it switches, it will collapse faster than you can fathom." —Bryan Cantrill
* 同事的 claude 被封了，$100 套餐。
* You will never feel ready. Ready is not a feeling. Its a decision.
* qmd chunk 切分看着很粗暴，在中文场景下感觉切分就抓虾了。
* 把copilot 退了， 换 kimi 200/月试试。
* 瘪三是上海方言？为什么香港电影里会出现上海方言，还是吴彦祖说的。
* 我的mbp停在2023
* 今天的办公室安静到，鼠标声都有些大了
* 目前openclaw 的场景：分析我的佳明数据；自动youtube 下载歌曲到 NAS。
* 按照 openclaw 的做法，会导致越来越多的平台不提供 API 么？现阶段很适合国内程序员群体，大部分关键数据（微信、支付宝）都没有开放 API，但日常使用的另一些服务 Google、Notion、Github 都有 API 支持。
* 周六的22km，非常认真的准备，前 15km体感都很不错，于是开始加速，跑到 21km 的时候，突然就爆了，心率没问题，体力也没问题，我以为是心理问题，问了下 AI，说是糖原消耗光了，下次整个能量胶试试
* 我不喜欢 Anaconda 的 Web 改动，内置一个浏览器来安装OS ？很奇怪
* 老设备该卖就得卖，要早卖，不卖最后就是电子垃圾。
* 把博客从 Hugo 换到了 Astro，主要是各种 URL 兼容花了比较久的时间，Kimi 2.5 没搞定，最终靠着 Opus 4.5 搞定了。
* 要想使用高驰的 API，需要提交申请。。
* 1 月份恩格尔系数 70%？？？