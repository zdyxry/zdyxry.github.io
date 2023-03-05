---
title: Weekly Issue 2022-08-28
date: 2022-08-28 10:00:00
tags:
- Weekly
description: 记录一下自己每周读过的文章，看过的电影，阅读过的书籍。
---


## 文章

### 技术

[Steam Deck, Linux Container and the Arch Community](https://speakerdeck.com/suiong_ng/steam-deck-linux-container-and-the-arch-community)

关于 [[Steam Deck]] OS 的介绍，底层是 [[Arch]] Linux，采用的是 A/B 升级方式，应用采用 [[Flatpak]] 方式进行安装升级(保证安全性)。现在关于这种 OS 比较轻，应用采用容器化的模式应该是很成熟了。

---

[Global Code Time Report](https://www.software.com/reports/code-time-report)

编码时间报告。平均每天编码时间少于 1 小时，周三是编码时间最多的，很少有开发人员每天编码时间超过 2 小时。

---

[(A few) Ops Lessons We All Learn The Hard Way](https://www.netmeister.org/blog/ops-lessons.html)

一些“经验”教训。比如：在某个你没有在意过的服务，会解析 DNS来完成某项工作。关掉 TCP 53 可能会有奇怪的事情发生。正在查看的源代码不是在生产中运行的代码。如果一周内没有完成故障复盘，那有可能永远也无法完成。没有人知道你在做什么。

---

[Slacker: Fast Distribution with Lazy Docker Containers](https://www.usenix.org/conference/fast16/technical-sessions/presentation/harter)

76%的时间花费在镜像的拉取。容器真正运行需要的有效数据只占用镜像大小的 6%。

镜像大小中，低层级(<9)的数据占到了镜像大小的一半以上。

---

[Kubernetes 中 Descheduler 组件的使用与扩展](https://blog.tianfeiyu.com/2022/06/30/kubernetes_descheduler/)

Descheduler 通过触发 Pod 的驱逐，来保证集群内资源分布均衡，达到 DRS效果。作者提出了 Descheduler 改进后的评估方式。

---

[WHY YOUR WEBSITE SHOULD BE UNDER 14KB IN SIZE](https://endtimes.dev/why-your-website-should-be-under-14kb-in-size/)

将网页大小保持在 14KB 以下可以保证加载速度。

大多数服务器 TCP 慢启动算法从发送 10 个 TCP 数据包开始。TCP 数据包的最大大小为`1500 bytes`.

这个最大值不是由 TCP 规范设置的，它来自[以太网标准](https://en.wikipedia.org/wiki/Ethernet_frame)。每个 TCP 数据包在其标头中使用**40 个字节**[——16 个字节用于 IP](https://en.wikipedia.org/wiki/IPv4#Packet_structure)，另外[24 个字节用于 TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure)。每个 TCP 数据包剩下**1460 个字节。**`10 x 1460 = 14600 bytes`或大约 14kB。 [[QUIC]] 同样。

---

[Amazon SageMaker Is Responsible for My Surprise Bill](https://www.lastweekinaws.com/blog/sagemaker_is_responsible_for_my_surprise_bill/)

AWS 账单真的太复杂了，复杂到我不去使用它。

---

[Devs don’t want to do ops](https://www.infoworld.com/article/3669477/devs-don-t-want-to-do-ops.html)

关于开发人员和运维人员的讨论。事实上，根据[VMware 的《2022 年 Kubernetes 现状》报告](https://hello-tanzu.vmware.com/state-of-kubernetes-2022/)，776 名受访者中有 54% 的人表示，更好的开发人员效率是采用 Kubernetes 的关键原因，超过三分之一（37%）的人表示他们希望提高运维效率。

---

[The Value is in the API](https://matt-rickard.com/the-value-is-in-the-api)

关注于接口设计比关注实现更重要。

---

[Designing Developer Velocity](https://matt-rickard.com/developer-velocity-checklist)

如何提升开发效率，通常大家会从使用角度来进行分析，作者列出了一些最佳实践。

---

[The point of a dashboard isn't to use a dashboard](https://shkspr.mobi/blog/2022/08/the-point-of-a-dashboard-isnt-to-use-a-dashboard/)

Dashboard 的目的是可以让系统的所有组件都可以提供数据访问接口，让你知道你可以掌控这些原始数据。

---

[6 Best Practices for Effective Readiness and Liveness Probes](https://datree.io/resources/kubernetes-readiness-and-liveness-probes-best-practices)

关于 [[kubernetes]] 的 [[Readiness]] 和 [[Liveness]] 最佳实践。

根据应用实际情况适当的调整参数：`initialDelaySeconds`，`timeoutSeconds`, `periodSeconds`, `successThreshold`, `failureThreshold`

不要只检测 HTTP 200 返回码，应该检查应用所有的依赖，如数据库连接，缓存连接。

---

[Falling for Kubernetes](https://freeman.vc/notes/falling-for-kubernetes)

有时候在公有云使用 [[kubernetes]] 服务是一个更好的选择，但是这个前提是有人帮你维护 [[kubernetes]]，如果是私有环境，维护应该还是一个大问题。




### 生活

[不记账的个人财务管理说明书](https://xiaowenz.com/blog/2022/08/finance-management/)

个人日常会记录自己的每笔开销，每个月固定时间也会进行二次校正。但是我没有真正的进行预算的控制，只是每个月大概有个心理预期，可以尝试一下明确自己各项开销的预算设置，尝试一下。

---




## 书影


《非常律师禹英禑》，前半部很好，后半部不太行，父母的情感纠葛感觉完全没有必要，男主的存在或者动机显得有些突兀。








