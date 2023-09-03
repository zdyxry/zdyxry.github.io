---
title: Weekly Issue 2023-09-03
date: 2023-09-03
tags:
- Weekly
description: 使用 Beancount 的第一天。
---


## 文章

### 技术

[Accessing host system systemd from container’s systemctl | by George Shuklin | OpsOps | Medium](https://medium.com/opsops/accessing-host-system-systemd-from-containers-systemctl-492a1a385102)

在 [[Container]] 内部操作宿主机的 [[systemd]]，除了配置 `privileged` 之外，还需要设置 `SYSTEMCTL_FORCE_BUS`

`SYSTEMCTL_FORCE_BUS=1 systemctl stop atop.service`

---


[Introducing vSAN Max | VMware](https://core.vmware.com/blog/introducing-vsan-max)

[[vmware]] 推出了基于 [[vsan]] 的独立存储产品。vSAN Max每台主机200TB起步，每个集群至少有6台主机。这意味着 vSAN Max 集群的起始容量为 1.2 PB。在撰写本文时，集群内的最大主机数量为 32 台（但建议的最大数量为 24 台主机），它将支持高达 8.6 PB 和约 340 万 IOPS。

[[HCI]] 解决了专有硬件、扩容不易、管理不便等问题，将计算和存储资源整合在一起，但是也面临一些新的问题：计算资源与存储资源无法独立扩容、一个集群资源提供给其他集群受到限制。许多客户都希望能够享受 HCI 的简化管理、增量可扩展性和使用商用硬件的优势，他们还希望在独立扩展存储和计算资源方面具有更高的敏捷性。存储资源从计算资源中分离出来，但实现方式是保持 HCI 的功能和优势，同时提供集中式共享存储所需的灵活性。

---

[OpenTF vs Terraform](https://twitter.com/iamvlaaaaaaad/status/1696521808143683812)

关于 [[terraform]] 的开源版本 [[OpenTF]] 的想法，其中提到了 [[hashicorp]] 在针对 [[terraform]] 的功能变更是非常克制的，且做了很多的背后的努力，而 [[OpenTF]] 的支持者对这个“社区”不了解，觉得忽略了 [[hashicorp]] 的努力，但是具体做了什么努力，什么工作因为一些原因无法公开。

---


[Socat 魔法：内网穿透 | 卡瓦邦噶！](https://www.kawabangga.com/posts/5324)

用 [[socat]] 实现内网穿透。

> Server 端的 socat 做一件事情：Listen `8075` 端口，一旦有连接建立，就开始 listen `5678` 端口，然后将所有 `8075` 端口收到的内容全部复制到 `5678` ，将 `5678` 的内容复制到 `8075`；
    `socat -d -d -d tcp-l:8075,reuseaddr,bind=0.0.0.0,fork tcp-l:5678,bind=0.0.0.0,reuseaddr,retry=10`

> Client 端的 socat 做一件事情：不断去尝试连接 `5.5.5.5:5678` 这个地址，一旦能够建立连接，就跟 `192.168.0.9:8000` （或者 `127.0.0.1` 建立连接），然后将 `5.5.5.5:5678` 的内容复制到 `192.168.0.9:8000` ，将 `192.168.0.9:8000` 的内容复制到 `5.5.5.5:5678`;
    `socat -d -d -d -v tcp:5.5.5.5:5678,forever,intervall=1,fork,reuseaddr tcp:192.168.0.9:8000`

---

[Postgres: The Graph Database You Didn't Know You Had](https://www.dylanpaulus.com/posts/postgres-is-a-graph-database/)

使用 [[Postgres]] 递归查询来模拟图数据库。

---

[Rethinking infrastructure as code from scratch | Nathan Peck](https://nathanpeck.com/rethinking-infrastructure-as-code-from-scratch/)

作者用 [[HTML]] 来类比当前的 [[IaC]] 状态，现在大家还处于手写 [[HTML]] 的状态，需要引入更高级的抽象来帮助完成一些资源的描述。而且现有的 [[YAML]] 只有数据没有类型，是无法很好的定义基础设施的， [[Pulumi]] 是一个不错的解决方案，但是 [[Pulumi]] 依赖于 [[terraform]] provider 的实现，也无法很好的处理 “易用” 和“完整配置” 之前的取舍。




### 生活


https://www.levels.fyi/community/thread/okEU9M/why-the-sudden-cut-in-hiring-entry-level-engineers

> 从来没有什么不同。工作岗位如此之少的原因是，绝大多数进入该领域的人根本不具备该领域的资格，因此人们认为自己需要离开教育的地方与公司希望他们去的地方之间存在巨大的脱节。  

这就跟谈恋爱一样，总需要前任教会一些东西。 from: @paula

---

[2023年夏云南自驾游 | 辛未羊的网络日志](https://panqiincs.me/2023/08/31/guimao-yunnan-trip/)

[[云南]][[游记]]。8 月末去云南看上去是个不错的选择。

> 逛完丽江古城后比较晚，在酒店门口的路上碰到了几个美女，叫我俩一人点一个。我们的酒店在繁华地段的巷子里，碰到这种事也比较无语，只能感叹生活不易，同时也意识到，男孩子在外面要好好保护自己。  

(自从上海小红楼事件发生之后，对于这些事情都能够想象了。

---

[每个人每天都只有24小时，希望我的选择真的是我的选择 | 枫言枫语](https://justinyan.me/post/5790)

值得反复阅读的关于[[自我]]的文章。个人需要在浪潮汹涌的现代社会中向内探索，找到内心真正想要的东西,而不是依靠外界规定的答案。每个人每天都只有24小时，如何利用时间是自己的选择。向内探索是一条弯弯曲曲的道路，会有许多试错，但可以慢慢建立自信,走出属于自己的人生道路。

---

[Social Media Decline: Ending for Twitter, Facebook, Instagram, TikTok](https://www.businessinsider.com/social-media-dead-instagram-tiktok-bereal-replaced-group-chats-messaging-2023-8)

大家越来越不喜欢在社交媒体上发布内容，转而开始真正与自己的朋友分享，这看上去是一件好事。

---

[We're Mostly Trying to Escape This Moment - zen habits zen habits](https://zenhabits.net/escape/)

很多时候，如果我们在做一些不喜欢做的事情，很容易去被任何小的、零碎的事情所吸引，无论那件事情是工作、娱乐还是其他，只要能让我们远离（逃避）不喜欢做的事情，我们就会本能的去做。

当我们试图逃避的时候，其实也是一种限制，对自己的限制，我们不能停留在一个让自己不舒服的状态，短时间可能没什么故障，但是如果做的越多，未来面对不舒服的事情能力越弱，应该尽可能的让自己保持在不舒服的状态，哪怕只是 10 分钟，也许此刻不能收获什么，但是下一次遇到类似的情况，我们可以更加从容的应对，多加练习。

---




## 书影


《计算机网络》，刚好看到微信读书上有这本，上班路上看一看。

《大宋少年志》，来自朋友的强烈安利。


## 碎碎念

终于下决心把记账 App 从随手记迁移到 Beancount 了，学习和迁移的时间耗时在 5h 左右。我自己之前记账分为两类：一类是每天日常开销的具体分类，比如吃喝、房租、旅行等；一类是每个月定期汇总各个账户数字，按月 review 自己的财务状况。这样带来的好处是，我可以分析自己过去几年的具体类别的支出，可以直观的看到自己是否因为某些原因导致的某些类别支出增加，比如 2022 年一整年我的休闲娱乐支出非常的少，2023 年截止到 9 月份休闲娱乐支出已经快达到心理预期的预算了。同时，按月 review 账单，也可以清晰的知道过去一个月整体的收入支出情况，以及各个账户的分配比例，可以更好的进行调整。

目前来看明确带来的改变是：
* 数据掌握在自己手里，单文件就可以保存所有数据；  
* 借款账户明确，可以很好的管理借款和还款；  
* 房租押金也是独立的资产账户，可以显式的管理；  

在之前的记账习惯中，两类账单通常是无法对齐的，会在第二类按月 review 的时候进行 padding。切换到 Beancount 也不会主动的追求对齐，前期计划按周进行 balance，感受一下具体的操作，如果可行的话后期计划按月进行 balance。