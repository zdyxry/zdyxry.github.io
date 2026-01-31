---
title: Weekly Issue-Be Kind
date: "2025-04-27T00:00:00.000Z"
slug: "Weekly-Issue-Be-Kind"
tags:
  - Weekly
description:
---

## 文章

### 技术
[A Trip Down Memory Lane: How We Resolved a Memory Leak When pprof Failed Us - WarpStream](https://www.warpstream.com/blog/a-trip-down-memory-lane-how-we-resolved-a-memory-leak-when-pprof-failed-us)

[goroutine](/mentions/goroutine) 泄露调查，使用 `gcore` 生成 coredump，使用 viewcore 获取所有的 objects 信息及引用信息。

可以考虑使用 [GitHub - cloudwego/goref: Go heap object reference analysis tool](https://github.com/cloudwego/goref/tree/main) 来解决？

---

[Ansible: pure (only in its) pragmatism - Andrej's blog](https://andrejradovic.com/blog/ansible/)

虽然 [Ansible](/mentions/ansible) 自己有很多的问题，如果深度使用大概率需要自己写些插件，但是在庞大的用户社区面前，在大多数场景下还是比 [shell](/mentions/shell) + [SSH](/mentions/ssh) 作为更好的选择。

[Ansible](/mentions/ansible) 最佳实践文档：[Good Practices for Ansible - GPA](https://redhat-cop.github.io/automation-good-practices/#_naming_parameters)

---

[Tip of the week #1: Field names are forever](https://webflow.buf.build/blog/totw-1-field-names)  
[Tip of the week #2: Compress your Protos!](https://webflow.buf.build/blog/totw-2-compress-protos)  
[Tip of the week #3: Enum names need prefixes](https://webflow.buf.build/blog/totw-3-enum-names-need-prefixes)  

[protobuf](/mentions/protobuf) 的一些 tips：不要 rename 、Enum 加前缀。

---

[如何超越 OpenShift | Oilbeater 的自习室](https://oilbeater.com/2025/04/23/surpass-openshift/)

> 这些都是 OpenShift 在商业化与开源之间权衡后的选择，并没有对错之分，但这会给更开放的项目留出机会。如果新的产品能够降低参与门槛，收取更广泛的反馈，让更多的贡献者来参与创新，那么我认为它的上限将会超越 OpenShift。

> 早期可能还是一个优秀的方案，但由于 OpenShift 专属导致不开放，随着社区的发展，原先优势的方案反而变成了阻碍前进的障碍。  
> 在很多细分领域 OpenShift 已经并不是最先进的解决方案了，尤其是在那些由 OpenShift 专属组件提供服务的领域。

文章中对 [OpenShift](/mentions/openshift) 的评价是：“现在的 OpenShift 在我看来就是一个覆盖面积很广，但平庸且无趣的平台”，在我的理解里，如果代入用户视角，这几个词都是褒义词。

---
[请求为什么超时了？ | 卡瓦邦噶！](https://www.kawabangga.com/posts/6965)   
[请求为什么超时了？答案和解析 | 卡瓦邦噶！](https://www.kawabangga.com/posts/6969)

[TCP](/mentions/tcp) 连接因为较长时间没有传输内容被中间的网络设备丢弃，可通过 Keepalive 避免。

---

[IronCore · GitHub](https://github.com/ironcore-dev)

有趣，看着是 [SAP](/mentions/sap) 基于 [kubernetes](/mentions/kubernetes) 来管理 [BareMetal](/mentions/baremetal) 项目，看上去是完整的实现，该有的都有了，不过感觉组装起来不那么容易，一堆的 controller。

其中 [BMC](/mentions/bmc) 控制是基于 [GitHub - stmcginnis/gofish: Gofish is a Golang client library for DMTF Redfish and SNIA Swordfish interaction.](https://github.com/stmcginnis/gofish) 。

---

[Protecting NATS and the integrity of open source: CNCF’s commitment to the community | CNCF](https://www.cncf.io/blog/2025/04/24/protecting-nats-and-the-integrity-of-open-source-cncfs-commitment-to-the-community/)   
[Looking Ahead with Clarity and Purpose for NATS.io | Synadia](https://www.synadia.com/blog/synadia-response-to-cncf)

[NATS](/mentions/nats) 想要退出 [CNCF](/mentions/cncf)，并计划修改开源协议，不知道故事后续会如何发展。

如果想不清楚自己如何赚钱，还是不开源的好。

---

### 生活

[致全体外卖骑手兄弟们的公开信](https://archive.is/XhmOv)

[京东](/posts/京东)的这个声明，我的第一想法是：可以省一大笔广告费。

---

[On loyalty to your employer. I’ve just returned to London having… | by Stevie Buckley | HackerNoon.com | Medium](https://medium.com/hackernoon/on-loyalty-to-your-employer-c674c4b06b3a)

> Considering the average ‘ career ’ with each employer in the tech industry is a touch under three years, the idea of spending 30 years working for the same employer is mind boggling. 

> 你的雇主付钱让你花更多的时间和他们在一起，而不是和你的家人和/或爱人在一起。你的雇主是你心理健康的最大影响者之一。如果绝对必要，你的雇主可以并且将会毫不犹豫地取代你。

> 让我明确一点，你的雇主不是你的家人，他们也不是你的朋友。他们付钱让你做一份工作，你的责任是做好这份工作。
> - 不要为了迎合你的雇主而牺牲你与家人和朋友的关系。
> - 不要为了迎合你的雇主而牺牲你的心理健康。
> - 不要为了迎合你的雇主而牺牲你的尊严、价值观和道德。
> - 不要为了迎合你的雇主而相信“奋斗”的胡说八道。

（这篇文章背景颜色是纯绿色，有些闹眼睛。

---

[除了钱一无所有](https://changchen.me/blog/20250425/nothing_but_money/)

> 很难想象世界上还有比 Autodesk 更加舒适的公司，但与上家蚂蚁相比，如出一辙的组织结构与人性导致个体的_做事方式_几乎没有差异，例如好大喜功的 PPT 文化，部分故意被创造的“[狗屁工作](https://book.douban.com/subject/30437833/)”，以及暗流涌动的斗争。想起玉伯的一期播客：[160.对话玉伯：字节是我在阿里的第16年，今天是Last Day](https://www.xiaoyuzhoufm.com/episode/663dbcbdeb5653e14a4f814d)

去除滤镜的看，大家都差不多。

---

[请不要对我发动量子波动速读 | 螺莉莉的数据中心](https://roriri.one/2025/04/23/ai-reading)

> 这种不在同一时空下的「对话」其实比面对面交流更为特殊。创作者有充分的时间来提炼、打磨自己要传达的内容，而读者也可以随时暂停、回溯、反复咀嚼，让这种「同步」有机会变得更加深入和完整。在读到一段精彩的描写时，你可能会会不自觉放慢速度，或是遇到复杂的论述时会来回推敲 —— 这些都是在调整同步的节奏，以求更好地理解和共鸣。

现在认真写文章的人越来越少，要珍惜。

---

[我的朋友谢扬，他的 Fellou，以及这个时代的创业者 - 王登科-DK博客](https://greatdk.com/2074.html)

> 有一次吃饭，我问谢扬他每天几点下班，他说十一点到十二点，我继续问，你这么晚下班干啥呢，他的回答是，思考。从我的观察来看，谢扬的思考并不平静，他的思考和语速一样快，并且经常包含着焦虑，他说他经常睡不着，并且有时候会哭。和谢扬当朋友，显然好过当他的下属，他的下属要忍耐一个情绪并不稳定的老板，并且总是要求极高，亲力亲为。

我有时候看我司老板，也是这种感觉，在用很多的时间思考着什么。

---

[Be Kind](https://boz.com/articles/be-kind)

> I don’t think I was ever outright mean to anyone. I was just callously indifferent and on a long enough timeline that is indistinguishable from being mean. In a cruel twist of irony I thought that was what it meant to be professional. In retrospect it just seems inhuman. It will take me several posts to details the many mistakes that got me to this point, but my biggest lesson was the importance of kindness.

> Being kind is fundamentally about taking responsibility for your impact on the people around you. It requires you be mindful of their feelings and considerate of the way your presence affects them.

“从根本上说，善良就是要对自己对周围人的影响负责。它需要你注意他们的感受，并考虑你的存在对他们的影响。“

---




## 碎碎念

* 当我以为 CI 可以永久不动的时候： This is a scheduled Ubuntu 20.04 retirement. Ubuntu 20.04 LTS runner will be removed on 2025-04-15.
* 再一次遇到 IDC 中的服务器链接到 cloudflared QUIC timeout，果断换成 HTTP/2 了
* 如何选择产品名字，好不好听，好不好记，我都能接受，但是用一个之前已经使用过的完全其他领域的名字，除了让人混淆，没有作用。
* 有个需求可能有多种实现方式，我问 Gemini 如何选择，它其中一个角度是“学习价值和技术深度”，如果知道这个需求大概率无法落地，那这个角度的优先级应该要尽可能的提高。
* 佳明教练的训练计划进入到了进展期，增长肌肉质量和体积阶段会增加锻炼的强度，以提高您的有氧能力。
* 老板的 Calendar 有一个周期性的任务，每周日 8:00 -14:30 ，标题是 sleep well 。
* 再次看到有人说 tanzu 开源线被博通干掉的消息，想到我司产品对 tanzu 的几个开源组件有些依赖。。。选择合适的依赖是门技术。
* 你用 OSTree，我用 A/B 分区，大家都有光明的未来。

