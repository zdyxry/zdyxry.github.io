---
title: Weekly Issue 2022-09-04
date: 2022-09-04 10:50:00
tags:
- Weekly
description: 记录一下自己每周读过的文章，看过的电影，阅读过的书籍。
---


## 文章

### 技术

[什么时候你第一次读懂了「云技术」？](https://daily.zhihu.com/story/9752308)

通过具体的工业场景解释什么是云。

---

[wifi有关的一些问题](https://blog.shell909090.org/blog/archives/2886/)

关于 Wifi 概念以及计算方式的讲解。

---

[可扩展服务设计原则 checklist](http://sunisdown.me/ke-kuo-zhan-fu-wu-she-ji-yuan-ze-checklist.html)

开发应用的基本设计原则，包含基本原则、整体设计、自动化管理、依赖管理、发布周期、测试、审计、监控告警

---

[有赞TCP网络编程最佳实践](https://tech.youzan.com/you-zan-tcpwang-luo-bian-cheng-zui-jia-shi-jian/)

在`net.ipv4.tcp_retries2`默认配置下，可能还是一直等到15min左右才能感知到网络异常。

---


[Introducing vSphere 8!](https://www.yellow-bricks.com/2022/08/30/introducing-vsphere-8/)

问：当你安装了 vSphere 8，你实际安装了多少个 ESXi 和多少个虚拟机？

---

[Kubernetes 1.25: cgroup v2 graduates to GA](https://kubernetes.io/blog/2022/08/31/cgroupv2-ga-1-25/)

[[kubernetes]] 正式支持 [[cgroup]] v2 。kubelet 和 container runtime 使用 systemd 来做 cgroup 管理。
> cgroup v2 offers several improvements over cgroup v1, such as the following:      
* Single unified hierarchy design in API  
* Safer sub-tree delegation to containers  
* Newer features like Pressure Stall Information  
* Enhanced resource allocation management and isolation across multiple resources  
    * Unified accounting for different types of memory allocations (network and kernel memory, etc)    
    * Accounting for non-immediate resource changes such as page cache write backs

---
[Linux IO](http://sunisdown.me/linux-io.html "Permalink to Linux IO")

Linux File I/O，Mmap，Driect I/O read/write，Asynchronous direct I/O

---


[Operating system upgrades at LinkedIn’s scale](https://engineering.linkedin.com/blog/2022/operating-system-upgrades-at-linkedin-s-scale)

[[linkedin]] 关于如何进行系统升级 OSUA 的介绍。内部运行数十万台物理服务器，在服务器升级前，会将目标服务器上的服务进行驱逐，在服务控制组件中，定义每个服务可以容忍的故障比例，OSUA 会确保所有应用都可容忍后，再进行升级，否则等待。为了避免多个运维操作同时执行，内部开发了中心化的锁服务(多层级)，保证OSUA 操作独立。针对有状态应用(主要输数据层应用)，会调用外部组件 STORU 来触发集群管理组件，在预升级阶段进行数据迁移动作，减少升级影响。

---

[啊哈，一道有趣的Go并发题](https://colobu.com/2022/09/01/fizzbuzz-in-go/)

[[LeetCode]] fizzbuzz 并发题。使用单一 Channel 加多个 Goroutine 实现。

---

[Some ways to get better at debugging](https://jvns.ca/blog/2022/08/30/a-way-to-categorize-debugging-skills/)

阅读代码，了解系统，掌握工具，有足够的经验。

---



[What should be on a SLI dashboard](https://ali.sattari.me/posts/2021/what-should-be-on-a-sli-dashboard/)

[[SLI]] Dashboard 应该如何设置。

---

[Why we moved from Helm to Gitpod Installer](https://www.gitpod.io/blog/gitpod-installer)

[[Gitpod]] 从 [[Helm]] 切换到自己维护一个安装器。Helm 维护困难，很容易犯错，缺乏编辑器支持和静态检查支持。

---

[Day in the life of a package maintainer: Reproducible Go packages](https://shibumi.dev/posts/day-in-the-life-of-a-package-maintainer-reproducible-go-packages/)

作为一个 [[Arch]] 包管理维护者要做的事情，构建 Reproducible 的 Golang 包。

---

[Is SRE Just Ops with a New Name?](https://metrist.io/blog/is-sre-just-ops-with-a-new-name/)

关于类似的讨论真的太多了，我觉得很没有必要，就好像我司的 slogan 是 `Make IT Simple` ，我们最终让用户(无论是开发还是运维)感受到使用方便、快捷、高效就足够了。

---



[Histogram vs eCDF](https://brooker.co.za/blog/2022/09/02/ecdf.html)

eCDF 比直方图更直观，比如在观察部分占比时，CDF 也可以直接放大局部而不影响整体。

---




### 生活


[疫情改变了什么](https://www.toobug.net/article/life/2022/what-does-epidemic-changed.html)

> **疫情防控叠加经济下行，直接将很多人的需求打回了“生理需求”层次。**

---

[The Big Censored Theory](https://pudding.cool/2022/08/censorship/)

内容精彩，设计也精彩，赏心悦目。

---

[欧格玛教会与言论自由](https://www.kawabangga.com/posts/3671)

[Terminating Service for 8Chan](https://blog.cloudflare.com/terminating-service-for-8chan/)

[# Blocking Kiwifarms](https://blog.cloudflare.com/kiwifarms-blocked/)

[Cloudflare 的滥用处理政策和方法](https://blog.cloudflare.com/zh-cn/cloudflares-abuse-policies-and-approach-zh-cn/)

我不理解，这让我困惑，包括很多人的言论让我恍惚，我需要一些输入来帮助我产生自己的思考。(如果大家有推荐的书籍请告诉我)

---

[平台到底有什么价值](https://xargin.com/value-of-platform/)

> 滴滴和美团在南京短兵相接的时候，运营的弱点完全暴露出来了，双方都是财大气粗，准备了几亿现金要砸在优惠券上的，然而美团的活动往往能够在几天内全面开展，而滴滴的活动却需要半个月~一个月时间开发才能完成。美团只花了很短的时间，就吃下了南京市非常大的市场份额。
> 

> 滴滴在和别人正面竞争之后才发现虽然老板天天都在讲战役，真碰上牛叉对手了以后自己像是用大刀去砍大炮的小丑。这次滑铁卢一般的失败直接导致了滴滴解散了将近百人的运营技术部门，重新规划了新的运营系统。
> 

> 内卷并不能卷出好的结果，平台建设能够带来的生产力提升是数量级的，加班只不过能让昏庸的领导开心而已。路线对了，才能过上好日子。
> 

---

## 书影


《壮志凌云2：独行侠》，被称为美国战狼，剧情走向完全可以预测，但还是很精彩。

《日班猎人》，这个剧情如果换成国产电影，那么评分估计朝着 4分去了，不理解现在还有6.5 的原因。

《脱口秀大会 第五季》，当脱口秀不能带给我快乐，反而让我气愤的时候，就不应该再继续看他了。还是期待线下的单口喜剧吧，争取今年能看一个专场。





