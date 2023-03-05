---
title: Weekly Issue 2022-07-17
date: 2022-07-18 22:03:36
tags:
- Weekly
description: 记录一下自己每周读过的文章，看过的电影，阅读过的书籍。
---


## 文章

[Side Project 成本最小化运维](https://www.kawabangga.com/posts/4718)

现成的 SaaS > 基于库实现 > 自己从软件方面实现 > 使用新的开源项目额外部署系统来实现。现在的各个 SaaS 已经非常成熟了，大部分场景都可以涵盖到，不建议把时间花费在运维维护工作上。

[Setting the Number of Cores per CPU in a Virtual Machine](https://www.nakivo.com/blog/the-number-of-cores-per-cpu-in-a-virtual-machine/)

关于 [[vmware]] ESXi 虚拟机 CPU 配置说明

- When you define the number of logical processors (vCPUs) for a VM, prefer the cores-per-socket configuration. Continue until the count exceeds the number of CPU cores on a single NUMA node on the ESXi server. Use the same logic until you exceed the amount of memory that is available on a single NUMA node of your physical ESXi server.
- Sometimes, the number of logical processors for your VM configuration is more than the number of physical CPU cores on a single NUMA node, or the amount of RAM is higher than the total amount of memory available for a single NUMA node. Consider dividing the count of logical processors (vCPUs) across the minimum number of NUMA nodes for optimal performance.
- Don’t set an odd number of vCPUs if the CPU count or amount of memory exceeds the number of CPU cores. The same applies in case memory exceeds the amount of memory for a single NUMA node on a physical server.
- Don’t create a VM that has a number of vCPUs larger than the count of physical processor cores on your physical host.

[Sockets vs Cores for ESXi VMs, which is better? Part 1](https://www.ewams.net/?date=2020/04/17&view=sockets_vs_cores_for_esxi_which_is_better)

关于 ESXi CPU 配置说明，结论是 socket 数量与 core 数量对于 CPU 性能几乎没有影响。

- Surprised to say, at least with this testing configuration, **there appears to be no impact to virtual machine performance with different cores and socket configurations**. Now NUMA might get you, depending on your application workload profile, so be careful. Y-cruncher obviously performs better the more vCPUs it has, but an 8-sockets-2-cores-per-socket system is going to perform the same as a VM with 4-sockets-4-cores-per-socket and the same as 1-socket-16-cores-per-socket since they all equal 16 vCPUs.

[Better Code: 关于接口的灵活性](https://wklken.me/posts/2022/07/08/better-code-5-flexible-api.html)

在暴露接口的时候要尽量克制，谨慎。

[The Day You Became A Better Writer](https://dilbertblog.typepad.com/the_dilbert_blog/2007/06/the_day_you_bec.html)

最关键的技巧是保持简洁。简洁的表达是有说服力的。一个五句话就能讲出来的不错的观点，比一个高明的一百句话的长篇大论，能说服更多的人。

简洁意味着去掉多余的词。如果你可以只写“他高兴”就不要写“他很高兴”。你觉得这个“很”字增加了一些效果。它没有。删减你的句子。

（以）幽默（为目的的）写作和商业写作有诸多相似。它也需要简洁。最大的区别在于词汇的选择。为了风趣，当你可以用“牛饮”就别说“喝”。

你的第一句要抓住读者。回顾一下我这篇文章的第一句话。我重写了好多次。它让你好奇，这是关键。

写短的句子。别在一句话里放好几个想法。读者可不像你想得那么聪明。

去了解大脑是如何组织想法的。 比起“球被男孩击打了”， 读者能更快地理解“男孩击打了球”。这两句话意思一样，但是理解主语先于动作会更容易。所有大脑都这样工作。（注意，我没说“这就是所有大脑工作的方式”）。

[A complete overview of SSL/TLS and its cryptographic system](https://dev.to/techschoolguru/a-complete-overview-of-ssl-tls-and-its-cryptographic-system-36pd)

关于 SSL/TLS 的介绍，图文并茂。

[How Google got to rolling Linux releases for Desktops](https://cloud.google.com/blog/topics/developers-practitioners/how-google-got-to-rolling-linux-releases-for-desktops)

Google 如何从 Ubuntu LTS 切换到基于 Debian 的滚动升级发行版；

在维护 LTS版本时，每两年都要花费一年的大部分时间来处理升级冲突和测试；

切换到滚动升级后，为了避免上游不稳定而导致内部重复工作，通过尽早的介入上游工作(也可以更好的回馈社区)，来保证上游稳定性；

[Hotelling's Law and Differentiation](https://matt-rickard.com/hotellings-law-differentiation/)

**竞争对手彼此靠近以最大化市场份额**

[房贷是对普通人的欺负](https://shuxiao.wang/posts/housing-load-is-a-bully/)

- 普通人对超过自己日常生活的数字是没有概念的。
    
    所以我觉得房贷就是肉食者、银行和房地产商联手对普通人的欺负，欺负他们无法理解太大的数，造下全天下都要买房的大势，利用他们的贪婪和无知，诓骗他们背上沉重而漫长的房贷，拿走这群普通到略显傻逼的人一生所能积攒的全部财富，唯独给他们留下一个很食之无味弃之可惜的旧房子。
    
    那普通人就一点错也没有了吗，也是有的，无知和贪婪都是其罪，不过这就是另一个话题了。
    

[How to Make Reviewers Love Your Big Pull Requests](https://ieftimov.com/posts/how-to-make-reviewers-love-your-big-pull-requests/)

保证提交的代码质量；

清晰的 commit msg；

[Atomic commits will help you git legit.](https://www.pauline-vos.nl/atomic-commits/)

保证每个 commit 都是原子的，包含完整上下文的。

[Image rebase and improved remote cache support in new BuildKit](https://www.docker.com/blog/image-rebase-and-improved-remote-cache-support-in-new-buildkit/)

关于 BUILDKIT 中的 `--link` 使用及示例，可以大大缩短构建时间。

[Remote Development at Slack](https://slack.engineering/remote-development-at-slack/)

[[Slack]] 远程开发环境介绍

- 痛点：拉取代码耗时，环境不统一，无法及时构建
- 改进：采用 AWS ASG 自动扩展实例，开发人员采用 VSCode 进行远程开发。
- 现状：开发环境成本翻倍；90% 切换到远程开发模式；内部效率提高明显。

[CHORIA APP Builder](https://github.com/choria-io/appbuilder)

在产品运维工作中，会包含大量的命令行、Shell 脚本、命令行拼接，比如 `kubectl blablabla | jq balblabla` ，通常我们会通过文档或者 Wiki 来提供使用说明，但是会面临一些问题：

- 暴露的命令又臭又长
- 变量参数传递不统一，部分支持环境变量，部分不支持，是否补全支持全靠命令行自身

这个工具提供了一种通用的方式来统一暴露入口

可能问题：

- 交互式命令处理？
- 命令边界模糊，什么应该是命令行内实现，什么应该放到 appbuilder 配置中？
- 在 YAML 中写 Shell 好像没好到哪里去？

[PROTECT YOUR DATA FROM RANSOMWARE WITH S3 OBJECT LOCK](https://blog.symops.com/2022/07/07/prevent-ransomware-s3-object-lock/)

可以使用 S3 版本控制和对象锁来避免勒索病毒。

[Let's talk about Kubernetes on the Internet](https://raesene.github.io/blog/2022/07/03/lets-talk-about-kubernetes-on-the-internet/)

扫描互联网上暴露的 Kubernetes，大部分是 EKS，AKS，GKE 暴露的。

有相当一部分 K8s 集群运行的版本是不再维护版本。

[Fallacies of Distributed Systems](https://architecturenotes.co/fallacies-of-distributed-systems/#the-network-is-reliable)

描述了在进行系统设计时常见的错误假设：

- 网络是可靠的
- 延迟为零
- 带宽无限
- 网络是安全的
- 网络拓扑不会改变
- 你可以控制一切
- 传输成本为零
- 网络(消息)是同质的

[A Practical Guide to Capturing Production Traffic with eBPF](https://www.seekret.io/blog/a-practical-guide-to-capturing-production-traffic-with-ebpf/)

使用 Golang 来演示 eBPF 如何抓取所需要的信息。

[https://github.com/seek-ret/ebpf-training](https://github.com/seek-ret/ebpf-training)

[Is there truth to the philosophy that you should sync; sync; sync; sync?](https://unix.stackexchange.com/questions/5260/is-there-truth-to-the-philosophy-that-you-should-sync-sync-sync-sync)

现在还真的需要 `sync;sync;sync;` 么？

也许这只是一个都市传说。


## 书影

《点球成金》，针对魔球理论的讲述，体育带给人的感动总是很直接。

《从零开始的女性主义》，起因是最近针对相关话题讨论真的多，而自己对相关背景了解太少，没有自己的想法和理解，果然还是读书带来的历史背景介绍比零散的文章/播客好不少。