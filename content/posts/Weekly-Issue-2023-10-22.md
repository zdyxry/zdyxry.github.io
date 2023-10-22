---
title: Weekly Issue 2023-10-22
date: 2023-10-22
tags:
- Weekly
description: 《浪漫的体质》太好看了。
---


## 文章

### 技术

[HTTP/2 Rapid Reset：解构这场破纪录的攻击](https://blog.cloudflare.com/zh-cn/technical-breakdown-http2-rapid-reset-ddos-attack-zh-cn/)

[[CloudFlare]] 关于 [[HTTP-2]] 快速重置攻击 DDOS 分析。写的比 [[Google]] 这篇要好： [How it works: The novel HTTP/2 ‘Rapid Reset’ DDoS attack | Google Cloud Blog](https://cloud.google.com/blog/products/identity-security/how-it-works-the-novel-http2-rapid-reset-ddos-attack) 。


> 被取消的请求流会快速过渡整个流生命周期。 END_STREAM 标志设置为 1 的客户端 HEADERS 状态从**空闲状态**转换为**打开**状态再到**半关闭**状态，然后 RST_STREAM 立即导致从**半关闭**状态转换为**关闭**状态。
> 
> 回想一下，只有处于打开或半关闭状态的流才会影响流并发限制。当客户端取消流时，它立即能够在其位置打开另一个流，并可以立即发送另一个请求。这就是 [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487) 能够发挥作用的关键所在。

---

Better HTTP server routing in Go 1.22 - Eli Bendersky's website](https://eli.thegreenplace.net/2023/better-http-server-routing-in-go-122/)

[[Golang]] 1.22 中会引入一个增强了模式匹配能力的默认HTTP服务器多路复用器(http.ServeMux)。新的multiplexer 支持指定HTTP方法的匹配、路径通配符匹配、路径结束符匹配等，避免了路由冲突。

---

[The price of managed cloud services](https://world.hey.com/dhh/the-price-of-managed-cloud-services-4f33d67e)

[[37Signals]] 每个月要在搜索功能上花费 43333$ ，而切换到自建机房之后，只需要3个月就可以收回成本。并且切换回自建机房后，并没有扩大团队规模来支撑新的服务。

> The team it takes to run our scale of operations in the cloud wasn't any less than what it takes to run that same scale on our own hardware.

---


[开源软件有漏洞，作者需要负责吗？是的！](https://mp.weixin.qq.com/s/SGnh_nt81sImqPLnBYrAgw)

**服务**的提供者和**软件**的提供者，是有本质的区别的。哪个软件不是一堆软件堆起来的，属于供应链安全问题，最近看到 [[SBOM]] 提到的次数越来越多了，也都制定了相关的标准，在描述 [[SBOM]] 的时候经常能看到类似的话术： `After a software vendor creates an SBOM, it is their responsibility to maintain and update it SBOM as application components change.` 
但是这里的 responsibility 会有什么后果，好像没有看到具体的说明。

---


[A very stupid bug - Xe Iaso](https://xeiaso.net/blog/stupid-bug/)

任何动作都可能失败，在关键路径上尽可能的多打印一些日志。遇到问题之后作者的分析方式是值得学习的。

---

[PromQL 备忘 - Jiajun的技术笔记](https://jiajunhuang.com/articles/2023_10_17-prometheus_promql.md.html)

现在偶尔需要使用 [[PromQL]] 的话，通常是问[[ChatGPT]] 。

---

[building a cheaper kubernetes cluster at home-Devin's Blog](https://dwbrite.com/blog/post/building-a-cheaper-kubernetes-cluster-at-home)

在 [[Orange Pi]] 搭建 [[kubernetes]] ，看着折腾起来没什么坑，但是我选择虚拟机。

---


[We Have To Talk About Flask - miguelgrinberg.com](https://blog.miguelgrinberg.com/post/we-have-to-talk-about-flask)

[[Flask]] 在 3.0 版本中引入了不兼容的改动导致 `Flask-Login` 无法工作，作者总结了[[Flask]] 历史版本中不兼容的改动，以此来说明社区不重视向后兼容的问题。

向后兼容的保证太难了，公司内部的组件产品，几乎没有遵循 semver 的。

---



[My First Impressions of Nix · mtlynch.io](https://mtlynch.io/notes/nix-first-impressions/)

[[NixOS]] 使用体验记录，作者主要和 [[Ansible]] 来进行对比，虽然他们可以达到的目标是类似的，但是感觉不是一个层面的东西。根据已有的资料来看，目前最佳体验是在 `x86_64` 上使用，其他架构的不建议。周末也折腾了下，初步处于可用的状态。


### 生活

[Write more "useless" software | nicole@web](https://ntietz.com/blog/write-more-useless-software/)

工作已经很苦了，有时候编写一些无用的代码/项目，可以抽身出来，因为是玩具项目，所以也不需要有 ticket，单测，只要跑起来就好。

---

[聊聊读书 · Issue #275 · yihong0618/gitblog · GitHub](https://github.com/yihong0618/gitblog/issues/275)
  
最早读书是有强目的性的，后来觉得也许应该随缘，持续了一段时间，最近又有强目的性了：保持自己有长时间阅读的能力。今年读书的量太少了，最近应该都读读书。

---

[2023 美区 Apple ID 注册充值指南｜国内网络无需信用卡](https://blog.qust.me/appleid2023)

看上去当前 2023 注册还是很容易的，充值是选择支付宝美区买礼品卡。拥有一些美区的账号总是好的，可以不用，但是要有。

---

## 书影


《浪漫的体质》，太好看了，今年看过最好看的韩剧了。

《上瘾五百年》，讲解常见的让人上瘾的物品历史，英国是玩这方面的高手啊。