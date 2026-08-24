---
title: Weekly Issue-Harmless
date: "2026-08-23:00:00.000Z"
slug: "Weekly-Issue-Harmless"
tags:
  - Weekly
description:
---

## 文章

### 技术

[The August 17 outage, and the work ahead](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/)

[GitHub Status - Incident with GitHub.com](https://www.githubstatus.com/incidents/zkxwbgr0cnmx)

> Since April, monthly commits have grown from 1.4 billion to 2.9 billion. That growth explains the pressure on our systems, but it does not excuse these outages.

官方博客文章中只提到了 “capacity failures”，在 githubstatus 中提到了更多的细节，Istio sidecar 达到了自己的并发上限，HPA 只配置了 Host 粒度。上游重试最终导致关键的 4 个 HAProxy 节点达到上限，认证路径崩溃，全面崩盘。

---

[Traceroute the World | 卡瓦邦噶！](https://www.kawabangga.com/posts/7276#2134c4c9-df34-4771-8d35-583c568f17ed)

怎么找到最长的 traceoute 路径。参考链接的两个 reddit 帖子也很有趣，比如 [Traceroute reveals Star Wars Episode IV 'crawl' text](https://www.theregister.com/on-prem/2013/02/15/traceroute-reveals-star-wars-episode-iv-crawl-text/284088)

---

[Improving infrastructure efficiency for growing demand in the age of AI](https://dropbox.tech/infrastructure/improving-infrastructure-efficiency-for-growing-demand-in-the-age-of-ai)

> That system-level impact is also why total power consumption doesn't tell the full story of efficiency. As Dropbox grows and stores more customer data, overall energy use may increase even as the infrastructure becomes more efficient.   
> A more useful measure is watts per petabyte, or the amount of power required to support a petabyte of storage. Since 2020, watts per petabyte across our storage infrastructure have improved by more than 50%. Today, it takes less than half as much power to support the same amount of storage as it did in 2020.

[[Dropbox]] 每 PB 瓦数相较于 2020 年下降了 50%，不知道这里的 SMR 硬盘起到了多大的作用。

---

[How Tailscale helped find the SQLite WAL-Reset bug](https://tailscale.com/blog/sqlite-wal-reset-bug)

[[TailScale]] 发现并协助解决了一个 [[SQlite]] Bug，是在 3.51.3 版本之前，如果在 Checkpoint 过程中特定时间点执行写事务动作，可能会产生数据丢失的情况，TailScale 自己接管了 Checkpoint 动作的执行时机，提高了执行频率，导致虽然使用的是一个经过生产验证的场景，但还是遇到了一些别人没遇到过的问题。

---

### 生活

[When Was the Last Time You Lost It with Everyone in a Movie Theater?](https://blog.mrcroxx.com/posts/when-was-the-last-time-you-lost-it-with-everyone-in-a-movie-theater/)

> “When was the last time you lost it with everyone in a movie theater?”   
> When my friends asked why I would pay to see something as rough and amateurish as *Niu Lai* at the cinema, this was my answer.

对我来说，这个问题的答案可能是跨年夜看泰勒斯威夫特演唱会电影？当时很多人直接在前面跳舞，一起唱，很欢乐。

维基百科的介绍：邪典电影（英语：cult film），又称 Cult 片、靠片，是指那些在某层次圈子内被支持者热烈喜爱及推崇膜拜的电影，也可称为非主流电影或另类电影。最被人熟知符合这个设定的居然是《大话西游》？

---

### 书影播客

《Learning DevSecOps : A Practical Guide to Processes and Tools》，没必要看，目录都没必要看。

《代码之镜 : 算法时代的社会图景》，上周刚说完打算统计一下一周看了多少篇 AI 写的文章，这下好了， 感觉这本书都是 AI “润色” 的。

《 基本无害-Ep205 学习机、暑假作业和低学历总统山 ft.刘仁铖&王继业》，推荐这期播客，是毛冬对王继业和刘仁铖的对话。王继和和刘仁铖分别作为两档脱口秀节目中出色的演员，被大众所熟知，刘仁铖今年是喜单的编剧，王继业是脱友的演员。两个人都是传统意义上的“坏学生”，刘仁铖自己也很难说清楚，自己到底怎么就“稀里糊涂”的退学了，王继业在大专和三本之间，很庆幸自己选择了三本。两个人在脱口秀行业里的入行时间差别也很大，一个是行业早期 2018 年，一个是火爆之后的 2022 年，相同的是他们在入行之后的投入和努力，将其作为自己的一个明确的职业路线去对待。 选择大于努力，选择本身也需要很多的努力。

## 碎碎念

* Arc Browser 真是有魔力，见到不止一个同事还死守在上面。
* 如何培养直觉？ 刻意练习。
* 两档脱口秀综艺结束了，辽宁大胜利，林简七是辽宁抚顺，小奇是辽宁阜新。某种意义上，怎么不是一种喜剧传承呢？
在 2025 年第七届单立人原创喜剧大赛中，小奇是冠军，林简七是亚军，说是线下预演也不过分。让我们期待一下第八届单立人比赛的冠军贤鱼和亚军冯子豪明年的综艺表现。
* 重庆泼水节，让我想到了内涵段子是怎么没的。
* 这周的工作内容，如果资源是足够的话，可以从 5 人天缩小到 2 人天？
* 诶，CAPI 在引入 in-place 升级的时候，提到的用户故事是说，bare-metal/Edge/定制化场景下，能够原地升级，现在明显又增加了一个场景：哪怕是公有云，如果你创建了一个 H100 instance，最好就不要删掉它，因为你很有可能再也创建不出了。甚至可能不只是 GPU，一些特殊的 CPU 实例也是稀缺的了。
* 听同事讲跨城通勤，这一般人绝对受不了
* 再次发现自己两年前的选型是错误的，真难受。
* https://outbid.lol/ 飞轮能转起来，说明自带流量刷脸还是最靠谱的方式。
* 发现一个人一天的 token 分布是： input token 1.5B，output token 2.48M，真是奇怪的场景。
* 现代泡面是起源于日本大阪。
* 同事中午说过大结果之后，这个词频繁的出现