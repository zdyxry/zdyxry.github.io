---
title: Weekly Issue 2022-08-21
date: 2022-08-21 23:00:00
tags:
- Weekly
description: 记录一下自己每周读过的文章，看过的电影，阅读过的书籍。
---


## 文章

### 技术

[与 CentOS 社区委员对话后 CentOS 时代](https://linux.cn/article-14927-1.html)

[[centos]] stream 之前的阶段，用户很难参与到 [[RHEL]] 的研发阶段，无法直接通过 [[centos]] 贡献代码，来保证下一个版本的 [[centos]] 包含自己所发现的问题修复，只能通过贡献给组件自身，然后由 RedHat 开发人员决定是否包含在下一个版本中。在 [[centos stream]] 之后的阶段，用户可以直接贡献给 [[centos]]，保证 [[centos]] 包含问题修复，至于 [[RHEL]] 是否修复，由 RedHat 自身决定。

**关于 Fedora、Stream，还有 RHEL 未来的发展计划是什么？**

- 从社会组织的维度：  
	- 1.  Fedora：主题是如何提高对 Fedora 的贡献，如何使得社区更多样化；  
	- 2.  CentOS Stream：和 Fedora 差不多，提高社区贡献和使社区更多样化，另外就是发展 SIG（特殊兴趣小组），充分发挥 SIG 的作用；  
	- 3.  RHEL：进一步繁荣包括社区、合作伙伴、客户的 RHEL 生态  
- 从代码的维度：  
	- Fedora：  
		- 集成上游社区最新最好的代码，功能最丰富，做业界的引领者；  
		- 面向特定的场景，做特色的发行版，如 Fedora IoT 就是面向物联网场景的 Fedora 操作系统。  
	- CentOS Stream：  
		- RHEL 稳定可靠的持续交付版，用户可以提前看到即将发布的 RHEL 版本；  
		- 基于稳定的代码基础，通过社区发展 SIG，在特定领域创新。  
	- RHEL：  
		- 我们面向客户的销售团队有很多关于产品的介绍，但我今天不是来为产品做广告的。我相信红帽大中华区的同事们可以给您很好的支持。  

---

[面试题：开发新功能和重构老代码之间怎么选？](https://chinese.catchen.me/2022/08/interview-question-ship-new-feature-or-refactor-old-code.html?utm_source=dlvr.it&utm_medium=feed&utm_campaign=catchen)

对于所有商业公司来说，第一原理永远是商业，不是产品也不是技术。

---
[X-Y PROBLEM](https://coolshell.cn/articles/10804.html)

1）有人想解决问题X2）他觉得Y可能是解决X问题的方法3）但是他不知道Y应该怎么做4）于是他去问别人Y应该怎么做？**没有去问怎么解决问题X，而是去问解决方案Y应该怎么去实现和操作**。
X-Y Problem最大的严重的问题就是：**在一个根本错误的方向上浪费他人大量的时间和精力。



---



[Nomad, Kubernetes, and a Pragmatic Look at Choosing Orchestrators](https://www.hashicorp.com/blog/nomad-kubernetes-a-pragmatic-look-at-choosing-orchestrators)

什么场景下使用 Nomad，什么场景下使用 Kubernetes？

---


[用 Wireshark 分析 TCP 吞吐瓶颈](https://www.kawabangga.com/posts/4794)

手把手教学

---

[常见分布式应用系统设计图解（十四）：日志系统](https://www.raychase.net/7087)

日志系统组件设计。

---

[No observability without theory](https://blog.danslimmon.com/2019/05/03/no-observability-without-theory/)

- Data is just data until theory makes it signal.The next time you need to build an observable system, or make a system more observable, take the time to consider not just what data the system produces, but how to surface a coherent theory of the system’s workings. Remember that observability is about delivering _meaning_, not just data.

理论和数据是互相影响的关系，无论是缺少理论还是缺少数据，都无法让我们对系统进行很好的观测。在创建图表时，需要明确的知道这个图表的含义以及数值波动所产生的影响。在创建报警条目时，除了产生报警，还应该显示对应的图表和操作说明。

---

[How to Handle Kubernetes Health Checks](https://doordash.engineering/2022/08/09/how-to-handle-kubernetes-health-checks/)

一次因为 K8s 健康检查错误配置导致的事故复盘。作者使用 Spring Boot 框架的默认健康检查配置作为应用的检查，有些与应用无关的异常导致了应用健康检查不通过，进而导致应用程序 Pod 被干掉。

应用默认的 Metric,Tracing, Log 都没有健康检查的记录，导致排查起来很困难，最终通过eBPF agent 的日志来辅助排查。

---

[SHOULD YOU PAY FOR CI/CD IN 2022?](https://blog.symops.com/2022/08/10/pay-for-continuous-integration/)

我们是否应该为 CI/CD 付费？文中介绍了 CI/CD 的发展，提到自建 CI/CD 的维护工作是隐形的，我们很难准确的评估这部分的成本到底有多大。

---

[SSH Tips and Tricks](https://carlosbecker.dev/posts/ssh-tips-and-tricks/)

关于 SSH 的一些技巧，其中`ControlMaster` 和 `ServerAliveInterval` 很有用。


### 生活


[The 1-1 Agenda](https://about.gitlab.com/handbook/leadership/1-1/#transitioning-1-1s)

[[Gitlab]] 关于 1-1 的介绍。个人1-1 次数很少，每次也不知道聊些什么。

---


[这可能是知乎最全的一篇中东烤肉介绍](https://daily.zhihu.com/story/9751840)

吃（虽然感觉烤肉好像味道都差不多）。

---

[社交网络名存实亡 -#28](https://geekplux.com/newsletters/28)

我更在意的是人，是能真正产生对话的、能够进行美好事物分享的人。我的微信朋友圈是我认真维护的，大部分屏蔽掉了，剩下的都是会分享生活的，比如晒娃的、游玩的、分享想法的。“朋友”圈应该是朋友，不应该是一个圈。

---


## 书影

《分手的决心》

一部很美好的爱情电影。











