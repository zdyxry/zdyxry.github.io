---
title: Weekly Issue 2023-07-23
date: 2023-07-23
tags:
- Weekly
description: 自动化所有需要重复2次以上的动作。
---


## 文章

### 技术

[Incident Review for Site-wide Outage for GitLab.com - Stale Terraform Pipeline #15997 (#15999) · Issues · GitLab.com / GitLab Infrastructure Team / production · GitLab](https://gitlab.com/gitlab-com/gl-infra/production/-/issues/15999)

[[Gitlab]] 对[[Terraform]] 使用不当导致故障的[[事故分析]]。在变更请求过程中,触发了一个过期的Terraform流水线。这导致一个过时的Terraform计划被应用到生产环境。同样的操作之前多次执行都没有问题。导致这次故障的原因是应用变更到生产环境有较长延迟(约3周)。用于资源重建的已知良好的流水线变得过时,并且由于最近的更改而导致配置漂移。

[[Atlantis]] 的存在是有道理的，它在前面拦一道，可以有效避免一些平时不容易注意到，但是一但发生会造成 S0 级别事故的 TF 灾难。 对抗人的不精确性的简单办法其实就是增加流程的安全性。 from: @kivinsae

额外的故事： [[Gitlab]] 因为自身故障，导致团队协作无法使用 [[Gitlab]]，只能去使用 Google Doc。

---

[A Failed SaaS Postmortem · Matt Layman](https://www.mattlayman.com/blog/2019/failed-saas-postmortem/)

作者在尝试做一个项目时，使用了自己不那么熟悉的技术栈，并且在软件依赖的更新上花费了大量的时间，又忽略了最终用户的感受，导致结果是不好的。在 MVP 阶段，应该保持技术栈简单，使用自己最熟悉的技术，来达到用户的期望。

---

https://www.redpoint.com/infrared/100/

[[Redpoint]] 选出的100 家做基础设施的[[公司]]。按类别划分：安全、数据 & AI、DevOps。

---

[Golang 中预分配 slice 内存对性能的影响| Oilbeater 的自习室](https://oilbeater.com/2023/07/19/pre-alloc-slice-for-golang/)

预分配 slice 容量，可以得到以下好处：

    1.  内存只需要一次分配，不需要反复分配。
    2.  不需要反复进行数据复制。
    3.  不需要反复对旧的 slice 进行垃圾回收。
    4.  内存准确分配，不存在动态分配导致的容量浪费。

结论：无论 slice 规模大小，预分配带来的性能提升都是非常明显的。

可以在 [[CI]] 中使用 [prealloc](https://github.com/alexkohler/prealloc/tree/master) 来自动检测。

---


[TCP 长连接 CWND reset 的问题分析 | 卡瓦邦噶！](https://www.kawabangga.com/posts/5217)

[[TCP]] `net.ipv4.tcp_slow_start_after_idle` 导致服务延迟高。

> 拥塞控制算法使用收到的 ACK 来确认网络质量从而避免拥塞，但是在 idle 了一段时间之后，没有 ACK 在传输，拥塞控制算法所保存的状态可能已经不能反映此时的网络情况了，比如发送了一波数据，直到发送完成的时候网络都比较空闲，然后连接 idle 了 10s，又要开始发数据，此时网络恰好负载比较高，如果 TCP 使用 10s 之前的知识去重新开始发送数据的话，就会造成拥塞；另外，10s 之后即使网络负载没变，网络环境可能变了（路由表切换之类的？），同样会造成 10s 之前的知识已经不适用了。  

---

[The day my ping took countermeasures](https://blog.cloudflare.com/the-day-my-ping-took-countermeasures/)

作者在ping一个地址时，看到了一个异常的“taking countermeasures”信息，这是由于计算机时钟向后调整导致的。在尝试复现问题时，使用 `LD_PRELOAD` 来加载一个自定义的 [[vdso]] 程序自定义获取时间方式（注意如果目标程序有 `suid` 权限，那么 `LD_PRELOAD` 会被忽略），并通过 strace 的 `Tampering` 能力进行故障注入模拟异常情况。

配合阅读： [Simulating Clock Skew in K8s Without Affecting Other Containers on the Node | Chaos Mesh](https://chaos-mesh.org/blog/simulating-clock-skew-in-k8s-without-affecting-other-containers-on-node/)

疑问，[[Ping]] 现在需要 `suid` 么？记得以前是需要的，现在好像不需要了，我看了眼自己的开发机（Arch Linux），已经不存在 `suid` 了，这是什么时候改的？与 `net.ipv4.ping_group_range` 有关么？与 `CAP_NET_RAW` 有关么？

答：最初 `ping` 是需要 `suid` 权限的，也会设置 `CAP_NET_RAW` 能力，因为需要使用 RAW Sockets 来发送和接收 ICMP ECHO 请求和回复，也就需要 root 权限，但是这引入了安全问题。
[[kernel]] 在 3.11 版本引入了`net.ipv4.ping_group_range` 参数，定义了一个用户组 ID 范围，在这个范围内的用不都可以发送 ICMP ECHO 请求，无需 root 权限。

### 生活

[伤口愈合的新理念——湿性愈合简介](https://m.thepaper.cn/baijiahao_19834121)

[我自己的亲身试验--伤口的湿性愈合 - 知乎](https://zhuanlan.zhihu.com/p/378092892)

[[湿性愈合]]，可以快速让伤口愈合，不经历结痂过程，看上去只有好处没有坏处？

---


[你是如何逐渐对曾经深信不疑的东西产生怀疑的？](https://www.zhihu.com/question/55504311/answer/145021306)

> 他们用自己的三十年的经历，深信不疑，只要敢于闯，敢于干，遍地都是机会，人人都能完成阶级跃迁。  
**正常的人生都要实现阶级跃迁，如果你没做到，那一定是你不努力，不够优秀。**  
**一个人的选择，忽略了对历史的行程的研究，注定是一个巨大的悲剧。**  

> 被这种作废的理念指导一步步求学，走上社会的85-95年龄段的子女们，都终将在人生二十多岁的年纪上经历一次深夜怀疑人生式的痛哭。  

---

[为什么国人的旅游方式普遍特别累？](https://www.zhihu.com/question/38890974/answer/3091786880?utm_id=0)

大部分看到的旅游分享，并不是那么悠闲的，而是带有极强的功利性的旅游，旅游不是一种休息，反而是另外一种竞争。我自己出门好像就有这个问题，总想在当地的时间多留意一些，生怕自己错过了些什么。

---

[Who do you do business with?](https://world.hey.com/jason/who-do-you-do-business-with-47c6c9d5)

选择你的业务伙伴时，要考虑他们是否关心长期关系和客户服务，而不仅仅是完成一笔交易。选择合适的人的重要性往往大于一笔生意。

---

[Calendar Defragmentation - Alex Ewerlöf Notes](https://blog.alexewerlof.com/p/calendar-defragmentation)

很多时候开会的时间不是自己所能决定的，都是被动开会，一天的时间被拆分的零零散散，我会尝试预留一些零碎的工作“塞”到对应的时间片，自我保证不会因为上下文频繁切换导致效率过低。

---




## 书影

《盐镇》，苦，太苦了，与《大医》的那种苦不同，这是《活着》的那种苦。我是在读《飞行家》的时候觉得有点苦，然后换了到《盐镇》，结果一比较，《飞行家》不算什么了。如果说东北作家写”苦难“是小刀割手，那么易小荷写”苦难“就是大刀斩头。目前只读了第一个故事，让我想家了，想回家看看奶奶。

《NPR 播客入门指南》，自己今年在播客上的时间很多，可能有大几百个小时，在收听的时候也时常在想，现在播客的制作方式、节目分类、听众目标是否已经固定（没有更多花活了），一些音乐电台类播客，是怎么处理版权问题的（事实证明他们是完全没有版权的，引用原曲15s 以上就可以构成侵权）。这本书是很合格的工具书，也解答了我的一些疑问，如果准备做播客的人看这本书应该收获不小。

《曾少年》，朋友推荐的国产剧，在大时代的背景下几个年轻人的生活日志，大家都面临各自的困难，其中有一些困难自己也将要面临了，不知道能否以平和的心态去面对。剧中千喜这个角色挺有趣的，很知道自己想要什么，同时也知道自己在得到的过程中会失去什么，也舍得去失去。

《芭比》，强烈推荐，这是一个喜剧，推荐的原因也是因为这是一个喜剧。