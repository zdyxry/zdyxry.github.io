---
title: Weekly Issue 2023-07-30
date: 2023-07-30
tags:
- Weekly
description: 疲惫的一周。
---


## 文章

### 技术
[新的网络性能优化技术 —— BIG TCP |   Oilbeater 的自习室](https://oilbeater.com/2023/07/24/big-tcp/)

现有的 GRO 和 TSO 可以将数据包拆分和组装的工作交给网卡来做，内核按照64k 处理数据包，可以带来 10倍的性能提升。主流网卡驱动只支持 TCP 的 Offload。[[BIG TCP]] 要做的事情就是让内核里处理的这个数据包变的更大，之前内核处理的数据包大小为 64K 的主要限制在于 IP 包的头部有个长度字段，这个字段长度为 16bit，因此理论上一个 IP 包最大长度就是 64K。在 IPv6 通过 `hop-by-hop` 来获取数据包长度，在 IPv4 通过直接从内核的 `skb->len` 计算真实的数据包长度。

---

[Why is DNS still hard to learn?](https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/)

为什么 [[DNS]] 很难学习，日常工作中遇到 DNS 问题都很头痛，加上国内特色网络，更麻烦。

---

[Breaking: AWS Begins Charging For Public IPv4 Addresses - Last Week in AWS Blog](https://www.lastweekinaws.com/blog/breaking-aws-begins-charging-for-public-ipv4-addresses/)

[[Azure]]和[[GCP]] 之后，[[AWS]] 开始对 [[IPv4]] 地址收费。前段时间我的 [[bandwagonhost ]] VPS 续费了，续费的理由是，我已经在市面上找不到比它更便宜的 [[IPv4]] 地址了。


---

[2023-07-02 -- 2023-07-03 Tarsnap outage post-mortem](https://mail.tarsnap.com/tarsnap-announce/msg00050.html)
[[Tarsnap]] 的事故分析报告：
- 为了避免数据损坏，所以没有设置服务自启动；
- 服务恢复过程中没有发现磁盘性能限制导致的恢复速度很慢。

了解了一下 [[Tarsnap]]，这是只有一个人维护的备份 [[SaaS]]，所有的数据都在 [[AWS]] [[S3]] 。从这篇报告中看这个服务也是一个单点运行的服务，并且已经对外提供了10多年了，一共只出现过两次事故。像这种服务的用户会是谁呢？当作者发生了意外，该如何获取自己的数据，貌似没有什么好的办法。

### 生活

[[声冻计划]引子 - yzqzss|一座桥在水上’s Blog](https://blog.othing.xyz/archives/freeze_wave_project_start.html)

有趣的计划，用[[录音笔]] 记录自己每天的声音环境，并保存下来，在目前的技术发展下，应该后续很容易制作一个虚拟的自己。

---

[去爬黄山](https://www.kawabangga.com/posts/5246)

[[黄山]][[游记]]。自己之前一直想去黄山，又担心自己的体力无法支撑完整的爬下来。

>”猴子观海“：游客像猴子一样看雾海。

---

[用ChatGPT写日记 | CreativityOverflow](https://quail.ink/goldengrape/p/write-diary-with-chatgpt)

[[ChatGPT]] 很适合将非结构化的数据转换为结构化数据，用它来帮助自己将每天的零散想法，记录并整理下来，配合上一些笔记工具，看着不错，想尝试一下。

---

[上海、北京近六年工资水平涨幅最高！ | 猎聘数据](https://mp.weixin.qq.com/s/HkH3CbmT5-bysktGeKXYYA)

印尼成为中国人才出海工作的首选。新一线投递比例与一线接近，00后更倾向于新一线。



## 书影

《盐镇》，上周读的故事，想回家看看奶奶，这周读了几篇，期间也一直在用奶奶来对比，感觉我奶奶是那种什么事情都可以自己做主的性格，很要强。


《不完美受害人》，国产剧，里面讲述的内容是现在每天都在发生的，完全能够理解女主的心里变化，还是可以看的。



## 碎碎念

周末去了趟常州，去看子龙的单口喜剧专场《作乐》，很炸很好看，脏话含量确实高，完全一副东北大哥的样子，全程笑的口渴，一瓶水很快就喝完了。演出结束后合影，顺便问了上海开专场还有戏么？得到的回答是：没有。真奇怪，北京的演出已经完全恢复了，上海周末城市专场都安排的满满当当：苏州、杭州、无锡、湖州、常州……但是上海却无法演出专场，为啥呢？

另外，第一次在希尔顿看喜剧演出，有趣。