---
title: Weekly Issue 2023-04-02
date: 2023-04-02
tags:
- Weekly
description: 
---


## 文章

### 技术

[Weka Violates MinIO's Open Source Licenses](https://blog.min.io/weka-violates-minios-open-source-licenses/)

[[Minio]] 再次撤销许可，上一次是 [[Nutanix]]。这篇报道[We object! MinIO says no more open license for Weka – Blocks and Files](https://blocksandfiles.com/2023/03/26/we-object-minio-says-no-more-open-license-for-you-weka/) 中提到，有用户说 [[Minio]] 每年通过许可协议收取 7位数的收益。

---

[Why I Will Never Use Alpine Linux Ever Again | Martin Heinz | Personal Website & Blog](https://martinheinz.dev/blog/92)

不再使用 [[alpine]] 的原因：不支持 DNS-over-TCP；很多依赖 C 的工具/库都会受到 musl 和 glibc 差异的影响。

关于 [[alpine]] DNS 问题的另一篇文章： [Does Alpine resolve DNS properly? | Purplecarrot](https://purplecarrot.co.uk/post/2021-09-04-does_alpine-resolve_dns_properly/)

---

[我的AI阅读助手 · BMPI](https://www.bmpi.dev/self/my-gpt-reader/)

使用[[ChatGPT]] 自动将指定类型的资源信息进行总结，可以进行交互式问答，支持自定义 prompt。

---

[Reddit - Dive into anything](https://www.reddit.com/r/RedditEng/comments/11xx5o0/you_broke_reddit_the_piday_outage/)

[[Reddit]] [[事故分析]]，写的非常精彩。根本原因是这个集群存在一些没有人指导的变更动作，集群一直正常工作，这个变更动作依赖于 kubernetes `master` 标签，在升级到 1.24 版本时，这个标签被 `control-plane` 取代，导致变更动作无效，进而导致集群故障。

庆幸的是集群有做备份，但是也提到了回滚的艰辛，在 [[terraform]] apply 执行过程中，没有人敢轻易的cancel 掉，因为很容易处于一个未知的状态。

---

[Infrastructure as Code is Not the Answer! | by Luke Shaughnessy | Medium](https://lukeshaughnessy.medium.com/infrastructure-as-code-is-not-the-answer-cfaf4882dcba)

虽然这里针对[[IaC]] 提出了很多问题，但是不可否认的不可变带来的优势，交付标准化和变更自动化，在需要频繁变更的场景下，是很有优势的，没有人可以保证当前执行的动作不会执行第二次。

---


[VictoriaMetrics 一些不应该被忽视的细节 « damnever](https://drafts.damnever.com/2022/some-important-notes-about-victoriametrics.html)

自己只是很简单的使用 [[prometheus]]，读下来并没有特别深的感受，这里引用组里同事的评论：

> 关于 wal 的部分，victoriametrics 作者的文章说的是数据损坏比数据丢失更严重，更难以处理，因为总会有掉电，只能二选一，wal 机制本身不太能解决数据损坏的问题，prometheus 如此，pgsql 也是如此，内部依赖 pgseql 的应用当 pgsql 的 wal 不开 fsync 数据损坏直接启动不了，得人工介入；数据完整性校验这个，因为数据的写入要经过多个环节，从 os 到磁盘，victoriametrics 在很早的时候就说过这个问题用可靠的磁盘来解决，这样也能减少设计时候的考虑；其他问题，比如可维护性上用一下 thanos 和 cortex 就行了，这两个玩意功能少，组件多，运维复杂，而且 VictoriaMetrics 作者说过，能不用集群版就不用集群版。

>VictoriaMetrics 就是个技术大佬的个人项目，有非常浓厚的个人气质，你看下他写的 fasthttp 就知道了，产品策略就是你有的我都有，我做的还比你好一些，你没有的我也有，而且这些你没有的特性很多时候你还真没得选，只能选 victoriametrics。

>prometheus 是组织化的，有各种设计和代码上的审核，而且在设计上肯定是脱离了实际需求的，自然可以设计的很优雅，但是优雅的另一面就是不接地气。如果你真的用过 prometheus 和 victoriametrics 就不会吐槽 victoriametrics 的，真的太省心了，我作为一个 victoriametrics 的用户真的很难吐槽什么。

---

[Bicycle – Bartosz Ciechanowski](https://ciechanow.ski/bicycle/)

讲解自行车涉及到的力学知识，图文并茂，太厉害了。

---

[BeyondStorage: why we failed](https://xuanwo.io/2023/01-beyond-storage-why-we-failed/)

[[BeyondStorage]] 项目的目标是做一个通用的存储库，向下对接各个存储服务，向上封装数据迁移，备份，管理等多种应用。但是因为没有真正用户，且目标不清晰，在早期项目不明朗的阶段过与追求细节，导致持续一年没有明确的版本发布，最终导致失去金主。

---

[Reflections on 10,000 Hours of DevOps](https://matt-rickard.com/reflections-on-10-000-hours-of-devops)

关于 DevOps 的经验总结，应该设置一个循环提醒，每周看一次这篇文章。

---

[机器之心的进化 / 理解 AI 驱动的软件 2.0 智能革命](https://www.indigox.me/the-evolution-of-machine-intelligence/)

这篇文章写在 ChatGPT 大热之前。

> 本文将带你领略一次人工智能领域波澜壮阔的发展史，从关键人物推动的学术进展、算法和理念的涌现、公司和产品的进步、还有脑科学对神经网络的迭代影响，这四个维度来深刻理解“机器之心的进化”。先忘掉那些花里胡哨的图片生产应用，我们一起来学习点接近 AI 本质的东西。

---

[有关 MTU 和 MSS 的一切 | 卡瓦邦噶！](https://www.kawabangga.com/posts/4983)

不同层次的协议如何处理发送的内容不超过下层协议能承载的最大内容。

---

[谜案侦破-我在终端输入 `??` 后，Golang 蹦了出来 - Songkeys](https://song.xlog.app/qq-zh)

> **当我们使用 `??` 时，我们在寻找当前文件夹中恰好由两个字符组成的文件名或目录名。**

---


### 生活

[译：拥抱苦差事  | Piglei](https://www.piglei.com/articles/embrace-the-grind-cn-translation/)

> 如果某个魔术所需的时间、金钱或练习的次数，比你（或任何一个普通人）所愿意付出的更多，那你就会被骗到。
> 有时，编程就像魔法一样：你念出一些神秘的咒语，一队机器人就会听命于你。但也有时候，魔法其实平凡而乏味。如果你愿意拥抱苦差事，你就可以完成不可能完成的任务。

---

[Introduction | Engineering Ladders](https://www.engineeringladders.com/)

工程师成长路径指南。

---

[How to Run a Really Good Retrospective](https://tanzu.vmware.com/content/blog/how-to-run-a-really-good-retrospective)

如何有效的进行复盘，针对消极的事情需要明确后续的动作，而不只是一个设想or 计划，确定每个动作都是粒度足够小并且是可独立执行的。

---

[How to Setup Logseq for Long-Form Writing | appsntips](https://www.appsntips.com/learn/setup-logseq-for-long-form-writing/)

写作软件和笔记软件是有很大的不同的，写作需要专注，笔记通常需要的是快速查找，联动。通过引入一些设置来让[[logseq]] 更适合长文写作。


## 书影

《毫无意义》，伍迪艾伦的自传，引用豆瓣评论： “大概是一本一个没经历过什么挫折的虚无主义者的人生流水账吧”

《新宋》，50%，还是感慨太长了。

《杀死福顺》，打打打杀杀杀，东亚家庭困在里面了。

《宇宙探索编辑部》，荒诞现实，很多时候，事情真实的发生就已经很好笑了，“用真心”真的可以。