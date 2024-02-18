---
title: Weekly Issue 2024-02-18
date: 2024-02-18
tags:
- Weekly
description:  假期结束。
---


## 文章

### 技术

[What it was like working for GitLab](https://yorickpeterse.com/articles/what-it-was-like-working-for-gitlab/)

>GitLab also had a tendency to listen more to complaints on Hacker News than internal complaints. This lead to an internal running joke that it if you wanted something to change, you'd have better luck complaining about it anonymously on Hacker News instead of bringing it up through the proper channels.

>It's well known that adding more people to a project doesn't necessarily improve productivity and results (see also "The Mythical Man-Month"), and yet almost every western startup with venture capital seems to ignore this, hiring hundreds of developers even if the product doesn't need nearly that many developers.

作者在 [[Gitlab]]工作 6 年多，这篇文章是在保密协议过期之后的回忆，记录了在这几年所做的内容，能感受到期间的挣扎。
作者学到了什么：
- 可扩展性需要成为公司文化的一部分
	- gitlab.com 不是 [[Gitlab]] 的主要盈利方式，所以不受重视，gitlab.com 遇到的问题的解决方式通常也无法应用在 self-hosted 版本上。
- 让团队变为数据和开发人员驱动
- 如果没有数据，无法确定什么是“最小可行”
	- 没有数据支撑的需求描述，很有可能最后做出来没人用的功能
- SaaS 版本和 self-hosted 版本分叉
- 更多的研发人员不等于更好的结果
- 对于 RoR 的困惑
	- RoR 太过于灵活，导致比较容易写出性能略差的代码
- 良好的 CI/CD 很重要
- 基于工作地点的工资具有歧视性

---

[Compensation as a Reflection of Values / Oxide](https://oxide.computer/blog/compensation-as-a-reflection-of-values)

[[0xide]] 的薪资水平说明，所有人都是相同的薪水。

>The truth is that companies pay people less in other geographies for a simple reason: because they can. We at Oxide just don’t agree with this; we pay people the same regardless of where they pick up their mail.

---

[云厂商眼中的客户：又穷又闲又缺爱](https://mp.weixin.qq.com/s/N8AYreKZ5OzNGWFb3m0EsQ)

>云计算的用户是谁？本来是一个很简单的问题，主流厂商的画像都很一致，几乎没有分歧。开发者。

公有云如果不能给开发者提供一个良好的技术理念或标准，感觉确实不太行。最近工作中有一个例子，国内厂商的解决方案，与 GCP/AWS 可以说差别非常大。国内的解决方案无法符合安全条例，但是好像没人在意。

---

[Feeding a Hungry Mouse Using Chromedp and Golang](https://www.pacenthink.io/post/feeding-a-hungry-mouse-using-chromedp-and-golang/)

通过 [[Chromedp]] 来使用 [[Golang]] 操作 [[Chrome]] 示例，其中一些关键的地方需要使用 [[JavaScript]] 配合 `chromedp.Evaluate` 实现。[[Chromedp]] 是 [[Chrome]] only 的，所以如果真的需要做一些浏览器自动化的事情，感觉还是使用 [[Playwright]] 好一些。

---

[jsonfile: a quick hack for tinkering](https://crawshaw.io/blog/jsonfile)

>But software is not building a house or traveling the world. You can realize a dream with the tools you have on you now, in a few spare hours. This is the great joy of it, you are free from physical and economic constraint.

当做一些小的项目开发时，可以直接使用 `json` 文件来作为数据库使用，并给出了一个示例实现。

---

[Go can only read 1GiB per Read call](https://kgrz.io/go-file-read-max-size-buffer.html)

[[Golang]] 对 `os.File` 对象的单个 `Read` 调用上限是 1 GiB，即使设置 buffer size 是 2GiB，也会一次只读取 1GiB。最早修复是将限制设置为 2GiB-1Bytes，修复 MacOS、FreeBSD 上读取大于等于 2GiB 大小失败问题；随后将限制设置为 1GiB，来保证数据对齐。

---

[uv: Python packaging in Rust](https://astral.sh/blog/uv)

[[Astral]] 公司开发的 [[Python]] 工具链，用来替代 [[pip]] ，与 [[Ruff]] 一样，[[uv]] 专注于性能，在没有缓存的情况快可以比 pip 快 8-10 倍。最终的目标是打造成 [[Python]] 的 [[cargo]]。

 现在 [[Rust]] 对 [[JavaScript]] 和 [[Python]] 的生态改善是明显的，重写一切。

---

[The Three Virtues of a GREAT Programmer](https://thethreevirtues.com/)

[[Perl]] 作者认为的三大美德：懒惰、不耐烦和傲慢。
- 懒惰：编写实用的程序，文档化需要频繁回复其他人的问题；
- 不耐烦：当编写的程序很慢时感到不耐烦，从而进行优化；
- 傲慢：保持代码“洁癖”，这样代码不会被别人说坏话

---

[一次网络问题排查 | 卡瓦邦噶！](https://www.kawabangga.com/posts/5803)

容器内访问 [[HTTPS]] 会卡主，访问 [[HTTP]] 没问题， Host 访问 [[HTTPS]] 和 [[http]] 都没问题。
抓包发现 server 443 返回的包 length == 0 ，猜测是包 MTU 太大导致被丢弃。
MTU 异常，是 [[TCP]] [[MSS]] 协商有问题，于是检查网卡的 MTU 配置，发现 Host 是 1450，Container 内部是 1500。
解决方式：
- [[iptables]] 设置 TCP 握手的 MSS 值
	- `iptables -I FORWARD -p tcp -m tcp --tcp-flags SYN,RST SYN -j TCPMSS --set-mss 1410`
- 配置 docker container interface 的 MTU：
	- `dockerd --default-network-opt=bridge=com.docker.network.driver.mtu=1234`
---

[Matthew Sanabria - Start With the Go Standard Library](https://matthewsanabria.dev/posts/start-with-the-go-standard-library/)

作者建议尽量使用[[Golang]] 标准库来作为初始实现，以 `log/slog` , `net/http`, `database/sql` 举例说明。

>**Go has a great standard library, and you should start with it.  

---


[Why irate from Prometheus doesn't capture spikes | by Aliaksandr Valialkin | Medium](https://valyala.medium.com/why-irate-from-prometheus-doesnt-capture-spikes-45f9896d7832)

作者认为 [[prometheus]] 的 `irate` 无法正确的捕获峰值数据，因为 `irate` 只计算当前区间的最后两个点，可能会丢失其他峰值数据，具体是否有效取决于 start 和 end 以及 step 数值。

作者建议使用 [[VictoriaMetrics]] 的 `rollup_rate` 。

---



### 生活

[My Sixth Year as a Bootstrapped Founder · mtlynch.io](https://mtlynch.io/solo-developer-year-6/)

[[TinyPilot]] 作者的 2023 总结。一人公司的典范。

---


[在 Autodesk 工作是怎样一番体验？ | Henry Z's blog\~](https://changchen.me/blog/20240217/why-did-i-join-autodesk/)

>第二个遗憾有点类似，即“我希望我工作别那么努力”。这实际上是韦尔的男性病人最遗憾的事。这与我宣扬的理念不谋而合。韦尔写道：“所有我照顾的男性都深深地悔恨自己在人生中太多时间都只是一部工作机器。”女性也会有这样的遗憾，但是韦尔指出，她的病人都是上一辈的人，当时外出工作的女性还比较少。并且，当人们说后悔工作那么努力时，他们不是指那种抚养小孩的艰辛“工作”，而是指为养家糊口、支付账单而从事的工作，他们因此错过孩子的成长以及陪伴伴侣。

---


## 书影

《杀人者的难堪》，节奏紧凑，剧情有点不讨喜，如果喜欢孙锡久或者崔宇植的话，可以看看。

《请和我的老公结婚》，韩式重生爽剧，看到 12 集就好。


## 碎碎念

* 春节在家被催婚，问我，对方年龄有什么倾向，比你大的可以么？我说，没什么想法。我爷爷：找小的，大的可不行。

