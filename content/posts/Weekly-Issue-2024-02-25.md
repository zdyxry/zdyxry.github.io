---
title: Weekly Issue 2024-02-25
date: 2024-02-25
tags:
- Weekly
description:  春节正式的结束了。
---


## 文章

### 技术


[Retrospective After Two Years On The CNCF TOC | Code Engineered](https://codeengineered.com/blog/2024/retro-cncf-toc/)

作者在 [[CNCF]] TOC  两年回顾。
>在过去 3 年中，CNCF 的贡献者和提交者逐年减少。与此同时，项目数量不断增加。一些项目和项目领域正在努力留住维护人员。

---

[真实世界中的 PMTUD | 卡瓦邦噶！](https://www.kawabangga.com/posts/5816)

>PMTUD 就是处理这种情况的：它的原理很简单，当有丢包的时候，我尝试发送小包，看能不能收到 ACK，如果能，说明链路 path 的 MTU 比我想的要小，等用小一点的包发送。PMTUD 的全称是 Path MTU Discovery。

继续 [[MTU]] 系列。使用 iptables 进行丢包验证，注意需要把 GRO(Generic Receive Offload）关掉。不同的 PMTUD 的实现行为不一样。
[[ICMP]] type 3 表示目标不可达，其中 code 4 表示包太大，需要拆分。但实际上在公网场景下可能不生效。

---


[Announcing Linkerd 2.15: Support for VM workloads, native sidecars, SPIFFE, and a new way to get stable releases](https://buoyant.io/blog/announcing-linkerd-2-15-vm-workloads-spiffe-identities)

[[Linkerd]] 发布 2.15 版本，其中需要注意的是在发布形式上发生了重要变化：**从 2.15 开始，我们将不再生成开源稳定版本。**

[[Linkerd]] 自身是以开源项目来管理，但是不会提供构建支持，构建产物最终以 BEL(Buoyant Enterprise for Linkerd) 发布，需要注意 BEL 的免费使用限制：非生产环境。如果员工人数少于 50 人可以免费在生产环境中使用。

官方进行了补充说明： [Some clarifications and updates on the Linkerd 2.15 stable release announcement](https://buoyant.io/blog/clarifications-on-linkerd-2-15-stable-announcement)

>_The reality is that for the past eight years, billion-dollar businesses have been built on these public stable Linkerd releases without any reason to fund the project or contribute back in any way_.

---

[minikube，kind 和 k3d 大比拼 | Oilbeater 的自习室](https://oilbeater.com/2024/02/22/minikube-vs-kind-vs-k3d/)

需要在 CI 环境中运行 [[kubernetes]] 的话，先明确自己需要什么隔离需求，如果需求只需要一个 [[kubernetes]] 环境的话，那么 [[k3d]] 是最快的。

Kubernetes 自身的 CI 是用 Kind 跑的。我自己本地如果需要 k8s 环境的话，通常是直接在本地部署一个 k3s 了，原来现在 [[minikube]] 也提供了 Docker 作为 Driver。

---




### 生活

[@hayami 春节争吵](https://t.me/hayami_kiraa/926)

>爸爸的吵架从「没必要把小事闹大」，到「你们小孩倔什么」。也没吵很久，大概一分钟后，他就气得上了楼，说不跟你们说了睡觉去。

>所以这场吵架的根本，是我和弟弟代表的「契约精神」思维，与爸妈代表的「人情社会」思维的冲突。

---

[The Layoff - Xe Iaso](https://xeiaso.net/blog/2024/the-layoff/)

虚构的有趣的裁员[[故事]]，后续也许会成为现实的。

---

[Things Unexpectedly Named After People · Notes](https://notes.rolandcrosby.com/posts/unexpectedly-eponymous/)

意想不到的用人名命名的事物：
- PageRank
- MySQL
- Debian
- Snowflake

---

[X 上的 Ghost：“Incredible stuff happening at Dropbox lol https://t.co/DLSiCAQ6Yy” / X](https://twitter.com/ghosttyped/status/1760734197311000828)

[[Dropbox]] 员工爆料：自己老板通过阻塞其他组的工作进度，来展示出自己组的状态比较健康，包括不限于：给大量 comments、延迟 review、拒绝 PR、在其他人开发过程中进行大范围的重构，来使对方返工。。。


---

## 书影

《首尔之春》：
>“你以为社会是一台精密仪器，各行精英谨慎周密地维持其运转，但经历越多越发现这个社会就是个草台班子， 一小撮精英带一大帮混子，尽最大努力维持着社会的底线而已” 。

《第二十条》，不好看。

《飞驰人生2》，还可以，感觉可以搞一个支线电影，讲述叶经理的人生轨迹。


## 碎碎念

* 需求讨论总是要掺杂人力讨论，讨论到最后可能就是需求理不清。


