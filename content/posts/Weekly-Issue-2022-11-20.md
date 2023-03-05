---
title: Weekly Issue 2022-11-20
date: 2022-11-20 23:50:00
tags:
- Weekly
description: One -> Two is the hardest; Start with two if you can.
---


## 文章

### 技术


[K8S 生态周报| 基础库放弃维护，上游社区如何选择？ | MoeLove](https://moelove.info/2022/11/13/K8S-%E7%94%9F%E6%80%81%E5%91%A8%E6%8A%A5-%E5%9F%BA%E7%A1%80%E5%BA%93%E6%94%BE%E5%BC%83%E7%BB%B4%E6%8A%A4%E4%B8%8A%E6%B8%B8%E7%A4%BE%E5%8C%BA%E5%A6%82%E4%BD%95%E9%80%89%E6%8B%A9/)

`GoGo Protobuf` 停止维护(很久)了，很多 [[protobuf]] 的示例项目和生产项目都是使用这个。

---

[Welcome to the Supercloud (and Developer Week 2022)](https://blog.cloudflare.com/welcome-to-the-supercloud-and-developer-week-2022/)  
> Efficient compute and storage, a global network that’s everywhere everyone is, bound together by software that turns the globe into a single cloud. The Supercloud.

---

[Scaling Mastodon is Impossible | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2022/11/14/scaling-mastodon/)  
从中心化/去中心化，[[Mastodon]] 协议和托管者的法律风险角度，讨论 [[Mastodon]] 替代 [[Twitter]] 的可能性。

---

[Sapling: Source control that’s user-friendly and scalable](https://engineering.fb.com/2022/11/15/open-source/sapling-source-control-scalable/)  
[[Sapling]] 一个与 [[git]] 兼容的 client。看上去配合[[reviewstack]] 可以解决 [[github]] review 困难的问题。

---



[Halo 官方镜像源在 Serverless(Cloudflare Workers + R2) 上的实践](https://nova.moe/halo-mirror-serverless/)   
[[CloudFlare]] [[Workers]] 配合 [[R2]]的具体应用。(感觉可以参考下折腾折腾)。

---

[Introducing Tailscale Funnel · Tailscale](https://tailscale.com/blog/introducing-tailscale-funnel/)   
[[TailScale]] 类似于 [[CloudFlare]] [[Tunnel]] 的产品。后者是真的方便好用，如果 [[TailScale]] 支持自定义域名的话可以考虑都使用 [[TailScale]]。

---

[没来的请举手 | 卡瓦邦噶！](https://www.kawabangga.com/posts/4847)   
当监控数据源没有数据返回时将默认值置为 0.

---

[Why is the terminal input so weird? | Warp](https://www.warp.dev/blog/why-is-the-terminal-input-so-weird)   
[[warp]] 介绍如何在[[terminal]] 中实现类似 IDE 的效果。
普通终端可以使用`Ctrl + x + e` 来使用 [[vim]] 输入命令，也足够使用了。

---

[I was told ~1200 RPCs independently by several engineers at Twitter](https://twitter.com/elonmusk/status/1592176202873085952)   
[[马斯克]]提到 [[Twitter]] 时间线会发起 1200 个 RPC，引发了关于[[微服务]]的讨论：

[https://twitter.com/jasoncwarner/status/1592227285024636928?s=12&t=4ARnHN0FjEdS2pfUMSBEAA](https://twitter.com/jasoncwarner/status/1592227285024636928?s=12&t=4ARnHN0FjEdS2pfUMSBEAA)

[https://twitter.com/xuwenhao/status/1593469165892820992](https://twitter.com/xuwenhao/status/1593469165892820992)   
对于微服务带来的维护复杂度表示深深的赞同。

---

[Making a Go program 42% faster with a one character change • Harry Marr](https://hmarr.com/blog/go-allocation-hunting/)   
[[Golang]] 逃逸分析。

---

[Vulnerability Management at Lyft: Enforcing the Cascade - Part 1 | by Alex Chantavy | Nov, 2022 | Lyft Engineering](https://eng.lyft.com/vulnerability-management-at-lyft-enforcing-the-cascade-part-1-234d1561b994)   
[[Lyft]] 如何进行自动化安全漏洞管理。




### 生活

[The most important thing to understand about queues – Dan Slimmon](https://blog.danslimmon.com/2016/08/26/the-most-important-thing-to-understand-about-queues/)
> **As you approach maximum throughput, average queue size – and therefore average wait time – approaches infinity.**

套用工作任务来说，如果始终 100% 负荷，每个任务的平均等待时间是增多的，但是好像也不会有人从一个全局来观察每个人物的等待时间？可能 PM 会去关注？

---

[When efficiency hurts more than it helps – Dan Slimmon](https://blog.danslimmon.com/2015/07/09/when-efficiency-hurts-more-than-it-helps/)
当长时间处于 100% 负荷，任务大量积压时，会带给人很多负面感受：

- 队列变长了，这本身就令人沮丧。当人们觉得他们的工作没有带来改变时，他们的效率就会降低
- 任务到达和完成之间的平均等待时间 [随队列长度线性上升](https://en.wikipedia.org/wiki/Little's_law)。等待时间过长，你的价值就会流失：你将时间和精力投入到可能不再相关的想法上
- 由于您已经以满负荷或接近满负荷运行，您甚至无法部署额外的容量来减少这些队列：基本上不可能摆脱它们
- 队列中等待时间的增加导致反馈时间变长，从而抵消了敏捷技术的优势

---

## 书影


《100 Go Mistakes and How to Avoid Them》 ，本周读了第 20 - 26 个。

《可能性的艺术》，读了一半。

《伸冤人》，打打打杀杀杀，主角战力在看过的动作片中强的过分，上升了一个维度。
















