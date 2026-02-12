---
title: Weekly Issue-半马
date: "2026-01-18T00:00:00.000Z"
slug: "Weekly-Issue-半马"
tags:
  - Weekly
description:
---

## 文章

### 技术

[周报 4 —— 刷剧 | Oilbeater 的自习室](https://oilbeater.com/2026/01/11/weekly-4/)

> 但是 Go 在 1.18 之后的 runtime 里其实默认就带了 VCS 的相关信息，只需要使用 `go version -m xxx` 就可以从二进制文件里直接获取构建信息了

 `runtime/debug` 的 `ReadBuildInfo` 函数携带的，想到之前用过的一个项目，可以找到系统中所有用 [[Golang]] 编写的进程信息，并且可以显示编译版本，有用到： [gops/goprocess/goprocess\_1.18.go at master · google/gops · GitHub](https://github.com/google/gops/blob/master/goprocess/goprocess_1.18.go#L13)

---

[AI真的来了，经济扛得住吗？——“大空头”、“AI巨头”与“顶尖科技博主”的一场激辩 - 华尔街见闻](https://wallstreetcn.com/articles/3763040)

> 应用层收入尚未兑现，资本开支却已全面爆炸，传统软件公司被迫转型为资本密集型硬件企业。这种 “先布局基础设施再等需求” 的模式，在投资史上极为罕见。

---

[Open-Weight Models Are Getting Serious: GLM 4.7 vs MiniMax M2.1](https://blog.kilo.ai/p/open-weight-models-are-getting-serious)

[[Kilo]] 对 GLM  4.7 和 MiniMax 2.1 进行了比较，让他们实现同一个功能，从最终结论上来看，都实现了需求目标，只是实现期望上 GLM 倾向于模块化且有完整的说明文档，MiniMax 扁平，但 MiniMax 便宜了一半。

---


[Alternatives to MinIO for single-node local S3](https://rmoff.net/2026/01/14/alternatives-to-minio-for-single-node-local-s3/)

作者在寻找 [[Minio]] 的替代品，比较的维度不是性能、稳定性，而是从易用性的角度来对比，解决的是如果想要快速起一个 Demo，应该选择什么，从易用性这个角度，也能看出一些项目的状态了。

结论：首选 SeaweedFS。

---

[What I Tell Colleagues About Using LLMs for Engineering | Pierre Zemb's Blog](https://pierrezemb.fr/posts/llms-for-engineering/)

里面提到了一条“Clone Your Dependencies”，现在大部分人在开发的时候应该都是使用 Context7 或者 Exa 的 MCP 来获取对应的开发文档，这种直接本地克隆相关的依赖，感觉 context 会不够用。

---

[Shipping at Inference-Speed | Peter Steinberger](https://steipete.me/posts/2025/shipping-at-inference-speed)

在读这篇文章之前，必须要先看下作者的 Github 页面： [steipete (Peter Steinberger) · GitHub](https://github.com/steipete/) 
，比如这个项目： [GitHub - clawdbot/clawdbot: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞](https://github.com/clawdbot/clawdbot) 我知道看代码提交数量或者代码行数没有意义，但是到作者这个一个月百万行代码的量级，也太恐怖了。作者主要使用 Codex，配合 GPT-5.2 CodeX High 来使用。

---

[Genie: Uber’s Gen AI On-Call Copilot | Uber Blog](https://www.uber.com/en-HK/blog/genie-ubers-gen-ai-on-call-copilot/)

[[Uber]] 内部的 Copilot 系统，用于回复 Slack 中的用户问题，成果是：回答超7万个问题，帮助率48.9%，估计节省了1.3万工程小时。48.9% 这个数字初看可能觉得，还不到一半，但是即使不到 50%，那节省的时间也是巨大的。

---





### 生活


[尼泊尔布恩山小环线纪行](https://blog.joway.io/posts/trek_poon_hill/)

> 尼泊尔虽然基础设施落后，但是在徒步产业周边的基础设施还算是发展的良好，甚至比日本熊野古道周边发展的都要好许多，至少这里基本不用担心路上水短缺的问题，大部分住宿也可以直接 walk in 进去入住。

---

### 书影播客

《诡才之道》，一年前的电影，周末朋友又推荐了一次，终于看了。做鬼不易。如果这部电影压缩到 20分钟，放在喜人舞台上，会不会被批评“大底“？


## 半马

周六的训练计划是 20km，加上前后的热身，相当于跑了一个半马，开心。  
平均配速 6:47，平均心率135bpm。前 10km 配速 6:50，后 10km 逐渐加速，直到最后一公里 6:00，最高心率 150，还在 Z2 区间，感觉不错。因为上几次的 15km+ 跑到后面会饿，这次早饭是两个三明治，在 2 个半小时后进行跑步，现在不会饿了，但是准备一瓶电解质水好像不够，尤其到后期，会非常的口渴，下次要准备两瓶水。


## 碎碎念
* 代理服务造假肯定是避免不了的，能做到的就是尽可能不用。。
* How the fuck should I know?
* 我都初中毕业这么多年了，为什么还会梦到初中考试。
* 晚上梦到初中，早上就听到两个初中同学的消息：张XX妈妈住院了，韩YY妈妈脑梗刚出院。
* 给别人留下的印象中，蠢不可怕，坏就得思考下自己的行为了。
* Tenable：不要误会，我不是针对你，我是说在座的各位…… 都是垃圾。
* 偶尔我在想，我做事是不是太谨慎了，生怕自己做错，所以会不断的确认，不断的调查，直到确认这个问题真的是别人的问题，再去联系对方，而不是先直接联系对方，说这里有问题。
* 蓝V 为了推广，连自己写的项目都说是“最近发现了一个新项目”
* vm0 的迭代速度让人感到害怕，这就是 AI 速度么？
* 上海这个雾霾，太糟糕了。
* 邓宁 - 克鲁格效应（Dunning-Kruger Effect）是一种常见的认知偏差，指能力不足的人往往会高估自己的能力，产生虚幻的优越感，因为他们缺乏识别自身不足的元认知能力；而能力强的人，反而会低估自己，认为别人也能轻松做到。
* 各种 AI 总结，会让一些作者在文章中的小吐槽/玩梗被自动忽略掉。
* 上图上新了《念念远山》和《古道》，崭新，果断借出。
* 川渝地区有很多擦边互动秀，怎么过审的？
先表演喷火，再表演川剧变脸，最后表演互动秀。文旅局会判定这是宣传非物质文化遗产，宣扬传统文化，就会过审。