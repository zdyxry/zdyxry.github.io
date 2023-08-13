---
title: Weekly Issue 2023-08-13
date: 2023-08-13
tags:
- Weekly
description: 回家好吃好喝的一周。
---


## 文章

### 技术

[不秃也变强：让 AI 当大师傅，编程和写作效率提升两三倍 | 歌词经理](https://quail.ink/lyric/p/not-bald-but-stronger-let-ai-be-the-master)

每当觉得 [[copilot]] 不行的时候，就去写一写单元测试，会感激他的。

最近非常喜欢用 [[ChatGPT]] 问一些 `vs` 问题，这个是在使用 [[Google]] 搜索时，一直使用的，当要了解一个东西 A 时，我通常看完这个东西自身的基本信息和文档之后，就去搜索 `A vs`，会看到很多同类的产品和对比，然后一篇一篇的看。现在有了 [[ChatGPT]] 之后，都是直接问：`A 和 B 相比，有什么差别，各自有什么优缺点，在什么场景下推荐使用 A？`，方便了许多。

---

[HashiCorp adopts Business Source License](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license)

[[hashicorp]] 决定将[[开源]] [[License]] 从Mozilla Public License v2.0 (MPL 2.0)切换到Business Source License (BSL) v1.1。 [[Pulumi]] 是可以直接使用 [[terraform]] provider 的，这些会收到影响么？

[[Pulumi]] CEO 说他们尝试贡献给[[terraform]] ，但是 [[hashicorp]] 不接受这些提交，只能 fork 单独维护。同时 [[Spacelift]] 联合创始人保证用户可以继续使用 [[Spacelift]]。

---

[Getting Friendly With CPU Caches](https://www.ardanlabs.com/blog/2023/07/getting-friendly-with-cpu-caches.html)

通过使用 slice 替代 array 来减少 CPU cache miss 的分析。  
`go test -c` 保留测试可执行未见，然后使用 `perf stat -e cache-misses ./users.test -test.bench . -test.benchtime=10s -test.count=5` 可以查看具体的缓存未命中数量。

### 生活

[跨平台日历同步：使用 CalDAV 和 Radicale 打造个人日历云服务 | MoeLove](https://moelove.info/2023/07/29/%E8%B7%A8%E5%B9%B3%E5%8F%B0%E6%97%A5%E5%8E%86%E5%90%8C%E6%AD%A5%E4%BD%BF%E7%94%A8-CalDAV-%E5%92%8C-Radicale-%E6%89%93%E9%80%A0%E4%B8%AA%E4%BA%BA%E6%97%A5%E5%8E%86%E4%BA%91%E6%9C%8D%E5%8A%A1/)

通过使用 CalDAV Server 来将多个日历平台进行同步，便于浏览安排个人时间。

---



## 书影

《OAuth 2实战》，断断续续读了很久，对 OAuth2.0 有了一些基本的了解，推荐同步阅读 Auth0 或者 Authing 的文档。

《孤注一掷》，是一部还算及格的宣传片，整部电影在宣发上应该花了很大的加钱，整体剧情很套路化，看样子会有第二部。赌博会让人的认知方式和思维方式发生生理性的变化，远离赌博。

《长相思》，朋友推荐，看了看，剧情不水，演技也还可以。

## 碎碎念

回老家待了一周，不得不说来回机票真的贵，路费就花了 3k。家里好吃好喝的，如果不催婚，那真不错。