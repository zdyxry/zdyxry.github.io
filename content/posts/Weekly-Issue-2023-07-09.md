---
title: Weekly Issue 2023-07-09
date: 2023-07-09
tags:
- Weekly
description: 好潮湿啊
---


## 文章

### 技术

[Google Search's Death by a Thousand Cuts](https://matt-rickard.com/google-searchs-death-by-a-thousand-cuts)

上周在搜索的时候收到了 [[Reddit]] 事件的影响，互联网越来越封闭，如何有效的获取信息已经是一个有门槛的事情了。

---


https://blog.webp.se/golang-libvips-cgo-zh/

[[Golang]] 跨平台编译的问题以及解决方式。如果一定要用 CGO，还是提供 container 方式吧。

---

https://xeiaso.net/blog/nosleep

避免在[[单元测试]]中引入 `sleep` ，如果需要需要通知机制，可以使用其他方式，比如 channel。

---

[MPTCP: 一个在 Go 1.21中的被忽略的新特性](https://colobu.com/2023/07/03/mptcp-a-go-1-21-new-feature/)

[[Golang]] 1.21 增加 [[MPTCP]] 支持。
> 它允许一个连接同时使用多个网络接口。  
如果连接绑定到链路速度，则使用多个链接可能会增加连接的吞吐量。请注意，如果连接绑定到 CPU，则使用多个链路会导致连接性能下降。  
它提高对链接故障的恢复能力。  

---

[TCP 拥塞控制对数据延迟的影响 | 卡瓦邦噶！](https://www.kawabangga.com/posts/5181)

通过实际问题了解[[TCP]] [[拥塞控制]]。 通过人为使用 `ip route` 设置 `initcwnd` 调整。

---


[开源不等于免费：Red Hat 调整 CentOS 项目带来的思考](https://moelove.info/2023/07/05/%E5%BC%80%E6%BA%90%E4%B8%8D%E7%AD%89%E4%BA%8E%E5%85%8D%E8%B4%B9Red-Hat-%E8%B0%83%E6%95%B4-CentOS-%E9%A1%B9%E7%9B%AE%E5%B8%A6%E6%9D%A5%E7%9A%84%E6%80%9D%E8%80%83/)

继续 [[RedHat]] 事件，这篇文章写的很好，把 [[centos]] 背景，不同的产品带来的优势、对 RedHat 的影响都交代的很清楚。如果没有 [[centos]]， [[RHEL]]也不会有今天这样的影响力。

---

[Cloud Dependencies Need to Stop F-ing Us When They Go Down - The New Stack](https://thenewstack.io/cloud-dependencies-need-to-stop-f-ing-us-when-they-go-down/)

> 根据 Uptime Institute 的研究，所有主要 SaaS 中断中有 70% 与上游云依赖问题有关。事实上，根据产品或应用程序的不同，工程团队可能会发现所有可警报事件中的 25% 到 70% 来自第三方云依赖性问题。  

最近因为 BWG 的一些问题，也考虑想把我的 miniflux 实例搬到 fly.io 或类似的平台去薅羊毛，可以用 fly.io 配合 planetscale 来运行。但是想到如果出问题排查起来感觉很麻烦，要分别登录不同的 Dashboard 去查，还是算了吧。

---


### 生活

https://laike9m.com/blog/ren-sheng-tai-chang-she-jiao-wang-luo-tai-duan,151/

周末的时候因为[[Twitter]] 搞限流，于是被迫又去使用了[[Mastodon]] 了，社交关系的迁移真的是太麻烦了，我先过滤了一波关注列表的 profile 中提到了 Mastodon 的链接，然后通过关注的关注，不断的找到眼熟的，找了很久也不过找到了46个关注的人。

期待 [[Meta]] 的 [[Thread]]。至少 [[Meta]] 不会瞎折腾，他们还是看重用户的。

---

https://stephanango.com/file-over-app

避免 [[Vendor lock-in]] ，文件是永存的，现在使用各种应用会优先考虑格式和导出问题，如果不可导出的，那么就做好随时会遗弃的准备。

> If you want your writing to still be readable on a computer from the 2060s or 2160s, it’s important that your notes can be read on a computer from the 1960s.  

---

[正面连接｜如此打工30年](https://chinadigitaltimes.net/chinese/697904.html)

第一代进城务工人员已经老了，他们随时可能离去，但是他们一生都在劳作，为了什么呢？不知道为了什么，生孩子养孩子，养儿防老么？看这个统计是不防的，甚至还需要给儿子付出更多。忙忙碌碌一辈子，是哪里出了问题？

---

[Twitter 要去哪里。 - Xiaowen.Z Deployed](https://xiaowenz.com/blog/2023/07/twitter-is-evolving/)

> **数字化经营给了企业更精细的度量业务，管理业务的能力，也让企业容易迷失在不准确的业务架构指标模型中，追求错误的业务指标。**  
> **错误的业务指标很可能意味着错误的投入和成本背负，错误的增长甚至可能导致和营收并不直接相关的错误成本持续增长，给企业带来不必要的财务负担，但现代企业的激励机制，对应的却可能是部分中高管因为次级业务指标的突破而收到嘉奖和升迁。**  

---

[写给 Twitter 用户的 Fediverse 指南 | wzyboy’s blog](https://wzyboy.im/post/1513.html)

继续[[Twitter]] 难民故事，[[Meta]] 新推出的 [[Threads]] 计划支持 [[Fediverse]] ，已知的有[[Tumblr]] 和 [[WordPress]] ，感觉之后会因为个人站点的稳定性不足导致大家去迁移到[[Threads]]，毕竟可以共用 [[Instagram]] 账号。

---

[为什么「相互宝」要专门拿出来被监管提。。 - Xiaowen.Z Deployed](https://xiaowenz.com/blog/2023/07/ant-group-help-eachother/)

> 相互保对投保人来说是好东西。  
对蚂蚁来说是利大于弊（远大于）的产品，有极大的盈利和产生附加间接价值流的空间。  
运营模式存在重大金融风险，不可监管，不可复制。  

有一个亲人靠着相互宝续了命，在我看来是好东西。

---

[回形针解散两年了，他们怎么样了？ - 草台班子 (@amateurs)](https://matters.town/@amateurs/404541-%E5%9B%9E%E5%BD%A2%E9%92%88%E8%A7%A3%E6%95%A3%E4%B8%A4%E5%B9%B4%E4%BA%86-%E4%BB%96%E4%BB%AC%E6%80%8E%E4%B9%88%E6%A0%B7%E4%BA%86-bafybeifvvbkdcloazpuetjghzry7i2guljtqwnak6rfuiyas2v6uggr7gm)

可以做一个系列，那些被消失的人，现在在做什么？

## 书影

《飞行家》，开始继续看，双雪涛的故事真的惨，真的痛，每次看都需要缓一缓。

《犯罪都市3》，马东锡系列继续，没有什么是无法一拳击倒的，如果有，那就两拳。

（最近没有什么好看的剧，有点剧荒。