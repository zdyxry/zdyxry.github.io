---
title: Weekly Issue 2022-11-06
date: 2022-11-06 23:50:00
tags:
- Weekly
description: 虚拟社交这是一场浩大的社会实验，成本是作者的激情，代价是观众的生命和时间。
---


## 文章

### 技术


[编写可维护的单元测试代码](https://jiajunhuang.com/articles/2022_10_31-goconvey.md.html)  
介绍 GoConvey 和 testify 两种单测框架。公司内部用 Ginkgo 比较多。

---

[2022 年 10 月 25 日 Cloudflare 服务部分故障](https://blog.cloudflare.com/zh-cn/partial-cloudflare-outage-on-october-25-2022-zh-cn/)  
[[CloudFlare]] 故障复盘，在引入 opentracing 时清理了部分 header 信息，导致上游逻辑判断错误。

---

[Give Your Tail a Nudge](https://brooker.co.za/blog/2022/10/21/nudge.html)   
[[Nudge]] 对于 [[FCFS]] 的优化：
> The intuition behind the Nudge algorithm is that we’d like to basically stick to FCFS, which we know is great for handling the extreme tail (high 𝑡), while at the same time incorporating a little bit of prioritization of small jobs, which we know can be helpful for the mean and lower 𝑡.

> However, when a “small” job arrives and finds a “large” job immediately ahead of it in the queue, we swap the positions of the small and large job in the queue. The one caveat is that a job which has already swapped is ineligible for further swaps.

---

[Ops to Bots — Smartening incident recovery](https://engineering.razorpay.com/what-goes-behind-managing-production-alerts-204f186ce865)    
通过构建 Bot 来标准化事件处理流程，降低 MTTD(Mean time to Detect) 和 MTTE(Mean time to Engage) 时间。

---

[命令行的艺术](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md)    
了解一些工具的使用可以让工作效率提高一些，大部分都很常用，小部分可以随用随查。
> 在 Bash 中，同时重定向标准输出和标准错误：`some-command >logfile 2>&1` 或者 `some-command &>logfile`。通常，为了保证命令不会在标准输入里残留一个未关闭的文件句柄捆绑在你当前所在的终端上，在命令后添加 `</dev/null` 是一个好习惯。

---

[Python 3.11 micro-benchmark](https://kracekumar.com/post/micro-benchmark-python-311/)  
[[Python]] 3.11 发布说明提到有不小的性能提升： "Python 3.11 is between 10-60% faster than Python 3.10. On average, we measured a 1.25x speedup on the standard benchmark suite. See [Faster CPython](https://docs.python.org/3/whatsnew/3.11.html#whatsnew311-faster-cpython) for details."，作者针对一些常见场景进行了性能测试对比。

---



[Why MTTR should be a ‘business’ metric](https://blog.last9.io/why-mttr-should-be-a-business-metric/)   
> Ex: A practice from Last9 I love: 2 day auto-delete messages on personal DMs in slack, because you want to control the spread of tribal knowledge; forcing engineers to talk on public slack channels. (Full disclosure: I'm an investor in [Last9](https://bit.ly/3VnLp2k))

---

[Backblaze: Buying less reliable disk drives can make financial sense](https://blocksandfiles.com/2022/11/01/backblaze-disk-drives/)   
> 如果您对优化云存储平台的效率感兴趣，那么对这种模型的需求对我们的业务很重要。否则，仅仅通过机器人购买最昂贵或最便宜的驱动器就会对分类账的费用部分视而不见。

---

[Murre - the lightweight K8s metrics monitoring tool](https://www.groundcover.com/blog/murre)   
通过从 [[kubelet]] 直接获取 metric 来展示给用户，轻量的 [[kubernetes]] top.

---

[A Visual Guide to SSH Tunnels (with labs)](https://iximiuz.com/en/posts/ssh-tunnels/)   
[[SSH]] Tunnel 介绍。(把事情讲明白是一种能力啊)

---


[理解一下依赖注入，以及如何用wire](https://farer.org/2021/04/21/go-dependency-injection-wire/)   
通过 `google/wire` 实现 [[依赖注入]]。

---



[“Nobody could have known”: inclusive behaviors to counter short-termism | by Elizabeth Ayer | Oct, 2022 | Medium](https://medium.com/@ElizAyer/nobody-could-have-known-inclusive-behaviors-to-counter-a-culture-of-short-termism-cf662e1bab26)[There Is No Shame in Customer-Reported Incidents - The New Stack](https://thenewstack.io/there-is-no-shame-in-customer-reported-incidents/)   
给客户呈现完整实时的事件报告，可以建立用户信任，这里的前提应该不是 P0/P1 级别的故障。
当客户遇到故障后，应该：最快更新问题状态、持续沟通、承担责任。“honesty is the best policy”

---

[Golang gRPC 错误处理 - Jiajun的编程随想](https://jiajunhuang.com/articles/2022_11_04-grpc_error_handling.md.html)   
通过在 [[grpc]] 中间件将自定义错误转换为对应业务码，同时支持 gRPC 和 HTTP 状态码。

---

[Processing Large Files with Go (Golang) | by snassr | Oct, 2022 | Medium](https://medium.com/@snassr/processing-large-files-in-go-golang-6ea87effbfe2)   
使用 [[Golang]] 通过 [[goroutine]] 和 [[channel]] 并行处理大文件。

---

[HTTP Resource Leak Mysteries in Go - Coder](https://coder.com/blog/go-leak-mysteries)   
[[Golang]] 内存泄漏调查，原因是没有执行 `response.Body.Close()`




### 生活

[离开国产 SaaS](https://reorx.com/essays/2022/10/get-away-from-china-saas/)   
大部分时候不敢用国内的服务。

---
[How to communicate effectively as a developer](https://www.karlsutt.com/articles/communicating-effectively-as-a-developer/)   
换位思考，尽可能的详细的描述清楚所要表达的内容，在多人协作过程中体现的很明显。虽然很多时候自嘲每天都写小作文，但是小作文带来的优势是很久之后重新阅读相关的回复，可以很快的了解上下文，节省了不少时间。

---

[2022-43: 工作中的自我调适](https://xuanwo.io/reports/2022-43/)   
> 工作热情高涨的时候总是会提出各种宏大的重构方案和计划功能，遇到的各种挑战和困难感觉都不是个事儿；但是在低迷的时候就感觉千头万绪无从下手，很难鼓起勇气去开始第一步，充满了挫折感以及失败感。为了缓解这种情绪，我选择先把这些特别大的计划暂停下，从一些细小而具体的工作着手，通过稳定的交付来恢复自己的感觉。
> 工作中遇到状态不好的时候可以尝试从外部环境和工作本身两个方面进行调整，跟自己的朋友和爱人多聊天，积极调适坚持度过。祝愿大家都能早日走出难捱的时光，好日子还在后头哪～

---

[BO ZENG BBOC, My Escondido: 互联网的庸众](http://bboczeng.blogspot.com/2013/02/blog-post.html)   
> 虚拟社交这是一场浩大的社会实验，成本是作者的激情，代价是观众的生命和时间。

---

[Clay - Be more thoughtful with the people in your network.](https://clay.earth/)   
[[Clay]] 是面向个人用户的 [[CRM]]。肯能有人觉得有些“功利”，但是人际关系是需要认真维护的。

---




## 书影


《100 Go Mistakes and How to Avoid Them》 ，本周读了10个，推荐阅读。

《边缘世界 第一季》，有一种要烂尾的趋势。

《乐透大作战》，韩式喜剧，破记录都是有原因的。

《孤单又灿烂的神：鬼怪》，终于看完了，不得不说，现在的韩剧水平距离 2015/2016 年真的差太多了。

