---
title: Weekly Issue-Oncall好苦
date: "2025-07-20T00:00:00.000Z"
slug: "Weekly-Issue-Oncall好苦"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Tyblog | systemd has been a complete, utter, unmitigated success](https://blog.tjll.net/the-systemd-revolution-has-been-a-success/)

[systemd](/mentions/systemd) 得到了事实上的采用，这是毫无疑问的，当前的状态下谈论 `systemd` 往往谈论的不是 `systemd` 自身，`systemd` 现在太庞大了，在它还没有大一统的时候，我会尽可能的只用核心功能，而不去使用  `systemd-boot`, `systemd-resolved` 等功能。

如果最终有一个 Linux 发行版所有的服务都是 `systemd-` 提供的，我会去使用的。

---

[Telefónica DE shifts VMware support to Spinnaker due to cost • The Register](https://www.theregister.com/2025/07/11/telefnica_germany_shifts_vmware_support/)

> "We told them that we don't use all parts of the VCF. They offered us the whole solution, and it was very good, and it's a lot of things that we don't need, that was the main problem," he added.

> That number of virtual machines currently stands at 8752, running across 660 host servers.

这篇新闻的一些数字挺有趣的：
- 一家电信公司有多少服务器？660 台服务器，8752 虚拟机
- 他们在过去 3 年在虚拟化软件订阅上花了多少钱？500 w 到 800 w 欧元；
- 博通收购后的软件报价是客户预期的多少？5 倍，包含了 VCF 全家桶。

---

[＃4 - 和 RSS3 道别的这一周 👋](https://polebug.github.io/2025/07/15/plog_4_say_goodbye_to_rss3/)

> “还会继续待在 web 3 行业吗？”  
> 现在 web 3 的市场环境确实没有以前那么好了，用朋友的话说是 “完全空心化了”，但是我仍然打算继续在这个行业。   
> 最重要的一个原因是，我觉得 web3 这个行业的天花板足够高。   

---

[Rancher 社区双周报｜ 722 个版本的旅程，RKE 即将告别，未来交给 RKE2 与 K3s](https://archive.is/06ubL)

[Rancher](/mentions/rancher) [RKE](/mentions/rke) 完成了它的使命，20250731 正式 EOL，推荐使用 [RKE2](/mentions/rke2) 进行替代，重点提到了安全性：`增强安全性：默认配置即满足 CIS 基准，支持 FIPS 140-2 合规；`。

这里有一个热知识，就是 [RKE2](/mentions/rke2) 的自我介绍一直都是：    
> RKE 2, also known as **RKE Government**, is Rancher's next-generation Kubernetes distribution.     
> It is a fully conformant Kubernetes distribution that **focuses on security and compliance within the U.S. Federal Government sector.**    

最近刚好是护网期间，加上遇到了很多国密的需求，同事说完全不理解为什么要搞这个，这更多是话语权的问题，在现在的环境下不得不搞的事情。换一个说法，[Rancher](/mentions/rancher) 这些搞合法合规，可是遥遥领先。

---

[TiDB Observability: Moving from Prometheus to VictoriaMetrics](https://www.pingcap.com/blog/tidb-observability-migrating-prometheus-victoriametrics/)

[Pinterest](/mentions/pinterest) 运行这一个 96 core, 768 G 的 Prometheus 实例，频繁的发生 OOM：
- 超长的恢复时间，在 replay WAL 时可能会耗时 40 M，甚至可能会失败；
- 重复 OOM，在 replay WAL 期间也可能会触发 OOM；
- 因为 OOM 导致的停机导致监控中断活潜在的 metrics 丢失。

在进行评估后，最终决定将其从 [prometheus](/mentions/prometheus) 迁移到了 [VictoriaMetrics](/mentions/victoriametrics)，带来的好处是：
- 更好的资源利用率，CPU usage 降低 50%，内存使用率保持在 35% 以下，性能稳定；
- 更好的查询性能；
- 更低的资源消耗（但是这里好像没有写具体的磁盘使用率降低了多少，可能是现阶段无法给出的数字？

文章的最后给出了推荐的调整过的 [VictoriaMetrics](/mentions/victoriametrics) 配置：

```
`docker run -it -v {PATH}/victoria-metrics-data:/victoria-metrics-data \`
    `--network host -p 8428:8428 victoriametrics/victoria-metrics:v1.106.1 \`
    `-search.maxSeries=5000000 \`
    `-search.maxLabelsAPISeries=5000000 \`
    `-search.maxQueryDuration=1m \`
    `-promscrape.config=/victoria-metrics-data/vm.config \`
    `-promscrape.maxScrapeSize=400MB \`
    `-search.maxSamplesPerQuery=1000000000 \`
    `-search.logSlowQueryDuration=30s \`
    `-retentionPeriod=10d`
```

---

[Upcoming changes to the Bitnami catalog (effective August 28th, 2025) · Issue #35164 · bitnami/charts](https://github.com/bitnami/charts/issues/35164)

[All good things come to an end: Shutting down Clear Linux OS - General Discussion - Clear Linux OS Forum](https://community.clearlinux.org/t/all-good-things-come-to-an-end-shutting-down-clear-linux-os/10716)

博通不再维护 Bitnami Image 了，所有的现有镜像需要在 8 月份完成迁移（这个时间可真紧）。   
Intel 不再维护 Clear Linux 了，立即停止，没有缓冲期，不过好在 Clear Linux 用户量应该不大，影响范围还好，我之前还挺喜欢他们的 RPM bundle 概念的。    

再次警醒，谨慎选择非主要盈利方向的项目作为核心依赖，所有的 Image 最好在公司内部 mirror 一份。

---

[Building a Self-Bootstrapping Coding Agent in Python • Data Is Dead, Long Live Value.](https://psiace.me/posts/baby-step-coding-agent/)

作为了解 ReAct 流程是一个很好的开始。

---

[Debugging the One-in-a-Million Failure: Migrating Pinterest’s Search Infrastructure to Kubernetes | by Pinterest Engineering | Pinterest Engineering Blog | Jul, 2025 | Medium](https://medium.com/pinterest-engineering/debugging-the-one-in-a-million-failure-migrating-pinterests-search-infrastructure-to-kubernetes-bef9af9dabf4)

> meant we were dealing with a rare event — something that would occur with a one in a million chance for each request.

> On the clearbox side, we sampled CPU, memory, and network utilization, correlating them with latency spikes. We used perf to look at CPU scheduling events, comparing preemption rates between Kubernetes and current production. We also checked cache utilization between the two systems and kernel lock contentions.       
> 
>On the blackbox side, we isolated the Manas pod from other processes via CPU shielding using taskset and cpusets, eventually giving the main Manas leaf process dedicated access to almost all CPUs on the node. As mentioned, we also ran the Manas binary outside its container entirely, directly on the host, similarly shielded, eliminating the likelihood of cgroups throttling.
>

[GitHub - brendangregg/wss: Working Set Size tools](https://github.com/brendangregg/wss#wsspl-referenced-page-flag)

> This tool uses /proc/PID/clear_refs and /proc/PID/smaps, which can cause slightly higher application latency (eg, 10%) while the kernel walks page structures. For large processes (> 100 Gbytes) this duration of higher latency can last over 1 second, during which this tool is consuming system CPU time. Consider these overheads.   
> This also resets the referenced flag, which might confuse the kernel as to which pages to reclaim, especially if swapping is active. This also activates some old kernel code that may not have been used in your environment before, and which modifies page flags: I'd guess there is a risk of an undiscovered kernel panic (the Linux mm community may be able to say how real this risk is).   
> Test in a lab environment for your kernel versions, and consider this experimental: use at your on risk.

[Pinterest](/mentions/pinterest) 在整个 2024 年决定将自己的搜索系统迁移到了内部的 [kubernetes](/mentions/kubernetes) 集群，近期在进行验验收时遇到了部分请求超时的问题，进行了调查。在前期验收过程中，如果只关注指标的 `P99` 可能会忽略这个问题，之后需要注意下要了解集群最差情况。在排查过程中用了各种方式，最终还是黑盒二分来的彻底。

最终定位到是因为 [cadvisor](/mentions/cadvisor)， [cadvisor](/mentions/cadvisor) 的 `container_referenced_bytes` 是默认启用的，用来跟踪进程在每个测量周期内引用的内存总字节数，在官方文档中显式说明了这是一个侵入式采集，可能会影响内核 page 回收策略并增加延迟。

---



### 生活

[Adults don't exist - Blog by Simon Frey](https://simon-frey.com/blog/adults-dont-exist/)

> Some evenings, in quiet moments at home, even the most seemingly competent individuals remove their professional masks and sit, slightly bewildered, wondering how they’ve ended up responsible for mortgages or children or entire departments. They check their phones while brushing their teeth, rapidly scanning the messages, mentally racing to keep track of all the things they’ll have to be on top of the next day.

**Figure it out yourself, and do it. Not because you’ve become an adult, but because you’ve realized there never were any to begin with.**

想到周围一些 30 岁以下的同事对于 `30 岁` 的恐惧和迷茫，恐惧的主体并不是 `30岁`，而是如何面对一个社会意义上 “成年人” 的期望的恐惧。 不是因为他们是“成年人”所以有能力、自信、成熟，而是因为他们有能力、自信、成熟才获得了“成年人”的社会身份及社会认同。

---

### 书影播客

(啥也没看，Oncall 太苦了

(播客在我日常接收的媒介占比还是挺高的，打算增加一下播客的记录

《没理想编辑部-Vol.183 平和地苟着就很了不起》，主播林蓝采访金子，金子是“GQ 实验室” 的媒体负责人，最近写了一本书《还可以的金女士》，讲述自己的人生经历。挺喜欢金子的聊天状态的，很放松，不那么的精英，我以为这种资深媒体人聊天都会比较无趣，当然也有可能是他们精于聊天的技巧，以至于我没有感觉到。想了半天她聊天的状态和哪个主播比较像，可能是猫爷。


## 碎碎念

* 走在路上，突然闻到了小时候吃的老式饼干泡牛奶的味道。
* 掌控力很能说明一些问题。
* 大家好像都比我敏感，都敏锐的发现了一些情况
* 又到了季度大家争相发 IDC 市场份额的时候了，不得不说 IDC 公司真是躺着赚钱啊，自己制定规则，自己当裁判。   
搜了下 IDC 的黑历史：预测英特尔安腾架构的销售，预测Windows Phone 的市场份额。坟头早都不知道多高了。
* 一堆内部项目假设开发用户是 root ，无奈。
* Groq k2 的价格是官方的 7 倍。
* 呆的久留会面临一个场景，很多项目都多少改过一些代码。
* 被一些张口就来给气笑了。
*看到良渚自来水的新闻，不知道这次带来的信任危机需要多久才能修复。
* 看到 Intel 停掉了 Clear Linux 的消息，没钱就会砍砍砍。其实我看现在 VMware Photon 好像也没什么维护了，不知道是内部维护还是要被砍掉。
* 我不喜欢twitter 上面 @grok 的行为。
* moonshot 的计费延迟还挺严重的？20号还看不到 19 号的账单。
* 周一遇到了一个客户环境的问题，当时我说最好知道客户环境做了什么配置，可以问问客户。   
老板说：就是 blabla 吧，客户环境有什么特殊的么？   
我：em... 最好和客户环境保持一致再验证吧。   
事情最后，果然客户环境很特殊，特殊到内部无法复现，周末两天交代了。
* 远离中信银行，6 个月没交易记录就要去柜台重新开通，什么鬼。
* 冷知识： 西梅，酸角，雪莲果，通便。

