---
title: Weekly Issue 2022-09-18
date: 2022-09-18 23:50:00
tags:
- Weekly
description: 记录一下自己每周读过的文章，看过的电影，阅读过的书籍。
---


## 文章

### 技术



[Kubernetes overstretched](https://book.douban.com/review/14650160/)

这几年抱怨 k8s 的也不少. 一方面是 k8s 越来越成为事实上的标准(借“Cloud Native”之风), 在各大中小厂落地. 很多人被潮流裹挟不得不用, 心里未必愿意. 场景未必适合, 加上心不甘情不愿, 遇到麻烦就容易不满. 另一方面, 为了进一步提升适用范围和可定制性, k8s 开放出了越来越复杂的插件机制: custom apiserver, scheduler-extender, volume provisioner, federation, edge proxy, knative, etc.. 最初方便扩展的开放性, 反而带来了越来越高的复杂度. 在我看来, 在90%的场景下, 大部分开发者其实用不着, 也最好别碰这些东西; 剩下10%的特殊需求, 最好交给专门的云厂商做. 但不贴上高级词汇, 怎么向公司体现自身价值呢? 于是也跟在后面亦步亦趋, 做出不伦不类的东西, 结果越改越难用.如果要上升一下, 就是工具有自己的舒适区. 工具原来是为哪种场景设计的, 就最适合在相应的场景下使用. 突破界限做成一个普适的东西, 多半会增加痛苦. 然而古往今来能被滥用的技术, 就没有不被滥用的. 可扩展性越高越会被滥用, 就像性能越高越会被用户往死里捅一样. No good deed goes unpunished, as always.

---

[Traditional Packaging is not Suitable for Modern Applications](https://theevilskeleton.gitlab.io/2022/08/29/traditional-packaging-is-not-suitable-for-modern-applications.html#workarounds)

看似在讨论包管理器问题，实际上是在讨论环境隔离问题。

---



[停不下来的创业者——得知 Figma 被 Adobe 收购有感](https://reorx.com/essays/2022/09/startup-founders-never-stop/)

[[figma]] 被收购之后，我第一个想法也是类似的，认为核心团队可能与 [[Rancher]] 一样，在被 [[SUSE]] 收购之后，核心团队会再次选择一个方向从零开始。期待后续。

---

[System Design Mind Map For Building Distributed Systems](https://medium.com/vedcraft/system-design-mind-map-for-building-distributed-systems-b20a4f6943d0)

设计分布式系统的思维导图

---

[Why You Should Pay Attention to eBPF](https://redmonk.com/rstephens/2022/09/08/ebpf/)

The primary use cases of eBPF fall into three overarching buckets: networking, observability, and security.

---

[Why you need an incident timeline](https://incident.io/blog/why-you-need-incident-timelines)

在进行事故分析时，通常会采用时间线的方式，为什么需要时间线？很多时候遇到故障，会涉及到很多人介入，使用完整时间线可以让大家回想起在某个动作执行时是否遗漏了什么，也可以针对其中的某些重点进行讨论，为什么做了这样的动作，当时的上下文是怎样的。

**永远不**应该改变时间戳或动作发生的顺序来帮助你的叙述。保持事件时间表准确很重要，目标是在零背景下的一年时间内，仍然可以找到发生的事情和时间的原始事实，而无需任何修饰。如果为了表述的更加清楚，那可以通过在时间线之上增加背景章节来补充。

通过时间线可以发现一些容易遗漏的事情：为什么那个时间点没有更新，是否是大家的背景知识不一致？是否沟通不及时？

---

[The Harrowing Search for the Elusive Technical Answer](https://www.lastweekinaws.com/blog/the-harrowing-search-for-the-elusive-technical-answer/)

遇到问题之后如何进行有效的搜索，可以称为一项必要技能。

### 生活

[如何寻找一个理想的租房](https://reorx.com/essays/2022/09/how-to-find-a-good-apartment/)

通过贝壳进行初步地理位置筛选，然后通过[[小红书]] 来找转租。这个思路感觉不错。

---


## 书影


《暴雨下在病房里》：无法评价。

《小小姐们》：剧情走向有种会烂尾的感觉。