---
title: Weekly Issue 2023-04-16
date: 2023-04-16
tags:
- Weekly
description: Celery 的社区真的不行。
---


## 文章

### 技术

[Database Architects: The Great CPU Stagnation](https://databasearchitects.blogspot.com/2023/04/the-great-cpu-stagnation.html)

[[CPU]] 性能的快速增长已经消失，作者分别通过 `Cores/$`, `(Cores*GHz * IPC)/$` 和 `B transistors/$` 来进行比较，验证近5年来的发展速度缓慢。

---

[个人网盘使用经验](https://liujiacai.net/blog/2023/02/25/cloud-storage/)

大家真的有那么多东西需要存储么？感觉我日常需要的更多的是备份场景，不需要一个随时可以读写的NAS。

---


[CodePilot | Synchronization Patterns in Go](https://code-pilot.me/synchronization-patterns-in-go)

[[Golang]] 中实现同步机制的一些方式，Mutex,Semaphore, Channel.

---

[David Klee - vNUMA and You - YouTube](https://www.youtube.com/watch?v=ORBzoVCUHwY)

合理的配置 [[vNUMA]]来保证应用可以更好的运行，前提是你明确的知道你的应用需要多少计算资源。

---

[实用 Web API 规范 | Log4D](https://blog.alswl.com/2023/04/web-api-guidelines/)

[[API]] 设计规范。之前也看过一些公司的设计规范，但是很难去实际实施。

---

[不想当作家的程序员写不出 Redis | 程序员的喵](https://catcoding.me/p/redis-antriez/)

[[redis]] 作者的一些故事。
> 运行良好的复杂系统往往由简单设计演化而来，而一个从开头设计的复杂系统往往不行，通过打补丁的方式通常也无法解决  

---

[Uptime Guarantees — A Pragmatic Perspective](https://world.hey.com/itzy/uptime-guarantees-a-pragmatic-perspective-736d7ea4)

应该追求什么级别的 [[SLA]]？理论上越高越好，但实际上从成本考虑，可能适合产品的才是最好的，需要评估宕机带来的直接损失，来确定自己可以容忍的时间，99.99% 比 99.5% 要付出的精力、成本多得多。有时候故障可能与技术实现无关，可能与运营有关。

实际的例子：Github Action Q1 故障次数达到了 55次，但是不影响大家持续的使用它，可能会带来抱怨，但是说带来的实际损失，可能也无法进行准确的评估。

---


[Ansible - State of the Community 2023](https://ansible.github.io/community/posts/state_of_the_community_2023.html)

日常使用 [[Ansible]] 比较多， [[Ansible]]社区整体是处于一个衰退的状态。除了文章中提到的点，作为用户，我感觉：

* 文档不友好，现在大家都追求单一 binary 发行的情况下，ansible 的依赖引入实在是太重了，而且通常 ansible 所以来的 Python 又是Linux发行版的重要依赖，层层引入导致了发行几乎无法统一。
* 异常处理不够友好，很多 Golang 项目甚至宁愿自己去写 SSH 执行命令，也不想用 Ansible。
* 进度展示，你不知道自己究竟执行到了什么阶段，百分比这个信息是无法获取的，虽然部分场景可以通过编写 plugin 来实现，但是终归不是官方方案。

受益于 Ansible 庞大的插件社区，一时半会也死不了。

---

[Fleek - Own your $HOME.](https://getfleek.dev/)

针对 [[Nix]]和 [[home-manager]] 进行封装，简化用户操作。

这个项目是属于 [[ublue-os]] 下的，感觉 [[ublue-os]] 的想法很好，但是实际上会不会有用户买单就很难说了。不过有了[[Fleek]] 之后易用性应该提高了不少。


---

[Optimizing TCP for high WAN throughput while preserving low latency](https://blog.cloudflare.com/optimizing-tcp-for-high-throughput-and-low-latency/)

TCP 接收窗口是发送方在任何时间点应传输的最大未确认用户负载字节数（传输中的字节数）。在 TCP 会话过程中，接收窗口的大小可以而且确实会上下变化。这是一种机制，如果由于接收缓冲区已满而无法成功接收发送的数据包，接收方可以告诉发送方停止发送。正是这个接收窗口经常限制高延迟网络的吞吐量。

Recv-Q 是本地应用程序尚未读取的用户负载字节数。

rcv_ssthresh 是窗口钳位，也就是最大接收窗口大小。发件人不知道此值。发送方仅通过 TCP 标头字段接收当前窗口大小。内核中一个密切相关的字段 tp->window_clamp 是基于可用内存量所允许的最大窗口大小。 rcv_ssthresh 是接收方慢启动阈值。

配合阅读： [窗口尚未完全开放时，TCP 堆栈能实现超预期的功能](https://blog.cloudflare.com/zh-cn/when-the-window-is-not-fully-open-your-tcp-stack-is-doing-more-than-you-think-zh-cn/)

---

[漫谈中断 | Soul Orbit](http://r12f.com/posts/interrupts/)

关于中断的讲解，包含中断分类，处理器如何知道中断请求来自于哪个设备，如何找到对应的中断处理例程，中断优先级，如何清除中断。

---


[20 Terraform Best Practices to Improve your TF workflow](https://spacelift.io/blog/terraform-best-practices)

[[terraform]] 的一些最佳实践。暂时还用不到，毕竟现在主要的 terraform 还是用于快速构建测试环境，线上也没什么机会使用。



### 生活

[面试底层逻辑整理](https://docs.google.com/document/d/1srnMc_hiOsyH7MuK196vExGGFjLJ0f-NDBih7jPJ2fE/mobilebasic)

> 说别人爱听的话，做自己认为正确的事。  
你要像个海王一样同时面试不同的公司岗位，在其中查漏补缺，包括技术，话术，绎术，但是一旦确定去了某家公司  
你就得像个直男一样，认真对待，不耍小心眼，做出成绩！  

---

[Dropbox Engineering Career Framework](https://dropbox.github.io/dbx-career-framework/overview.html)

[[Dropbox]] 的员工发展方向框架，配合 [Introduction | Engineering Ladders](https://www.engineeringladders.com/) 阅读。

---

## 书影

《Go语言设计模式》，还是要实际应用才能有更深的理解。

《深入理解 Linux 网络》，刚开始看。

《体能之巅：百人大挑战》，韩国综艺是真的拼，各种细分领域都渗透进去。

《至尊三十六计之偷天换日》，经典老片，梁家辉演得不错。

《饥渴游戏》，类似于《菜单》，大家都追求“不同凡响”，但是追求的过程中使用的方式/手段完全不同，感觉女主没有理解她的老师所讲述的故事，对于贵族而言，重要的是心理，而不是口感。

《超级马力欧兄弟大电影》，引用豆瓣评论：全是彩蛋，没有一点故事。

