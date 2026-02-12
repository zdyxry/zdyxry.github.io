---
title: Weekly Issue-吃早饭！
date: "2025-04-20T00:00:00.000Z"
slug: "Weekly-Issue-吃早饭"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Why our 5.2k-star K8s platform struggles overseas while thriving in China? Need your brutal feedback : r/kubernetes](https://www.reddit.com/r/kubernetes/comments/1jvpqil/why_our_52kstar_k8s_platform_struggles_overseas/)

[[Rainbond]] 在海外推广遇到了困难，他们观察到的 3 个明显问题是：
- 声称自己是 "Heroku for Kubernetes" 替代品
- Open Source != Trust
- Deployment Culture Clash: 75% of Chinese clients demand air-gapped installs (even on edge nodes!), while Western teams expect SaaS-first.
	- 这好像几乎是国内特有的情况了？

评论区中提到了 [[Harbor]] 在世界范围内被采用，是因为他们隐藏了是中国地区开发的。我觉得可能不是主要原因，当时 Harbor 是顶着 [[vmware]] 的光环在的，大家看重的更多应该是 [[vmware]]。对于评论区中的产品选型原因，感觉和行业或者技术壁垒有直接关系，比如 [[TiDB]] 那么多海外用户，[[Clickhouse]] 背后的投资人 [[Yandex]] 是俄罗斯公司，[[Deepseek]] 的开源项目引起的轰动，他们会没有考虑中国/俄罗斯的政治风险么？我觉得肯定考虑了。

下面那篇 TiDB 的文章中，也提到了国际化：

> “最好的国际化，就是本地化。”  
> 不同地区的文化差异太大，技术再牛逼，客户支持做不好，客户一样骂你没商量。

---

[Storage suppliers stare down Trump slump after tariff mayhem – Blocks and Files](https://blocksandfiles.com/2025/04/14/storage-trump-slump/)

不确定性会阻碍公司进行长远计划（这句话印象中之前一直是用来描述大陆的），现在看由于关税影响，短期内的报价工作都无法正常进行了。。

---

[极限编程和命名](https://blog.winkidney.com/posts/2025/Mar/12/art-of-naming-in-software-engineering-XP/)

> 尝试去应对变化，而不是预测变化，因为你永远不知道明天的需求是什么。

---

[十年再出发：回顾我与 TiDB 的成长之旅](https://zhuanlan.zhihu.com/p/1896834371740210342)

值得反复阅读的经验总结。

---

[《The Mom Test》读后感](https://changchen.me/blog/20250418/mom_test_notes/)

关于如何做用户调研的一些技巧。我的总结是，如果带有预设的去聊，对方作为用户可能什么都要，但是这些并不是真正需要的，不能看对方说了什么，要看对方 **做过** 什么，从对方 **做过** 的事情来吸取经验。

---
[DuckDB's CSV Reader and the Pollock Robustness Benchmark: Into the CSV Abyss – DuckDB](https://duckdb.org/2025/04/16/duckdb-csv-pollock-benchmark.html)

[[DuckDB]] 尽可能的以兼容方式来读取 [[CSV]] 的方法：

```sql
FROM read_csv('cafes.csv',
    strict_mode = false,
    null_padding = true,
    quote = '"',
    escape = '"'
);
```

想到之前帮朋友处理一个奇奇怪怪数据的 Excel 的痛苦，当时好像用 [[pandas]] 手动处理了很多边界场景。

---
[Building OpenAPI Based REST API In Go Using HUMA Framework, With SurrealDB | by Shiju Varghese | Apr, 2025 | Medium](https://shijuvar.medium.com/building-openapi-based-rest-api-in-go-using-huma-framework-with-surrealdb-844ded6a856e)

这篇文章中推荐了 [GitHub - danielgtaylor/huma: Huma REST/HTTP API Framework for Golang with OpenAPI 3.1](https://github.com/danielgtaylor/huma) ，之前在做新项目的时候，考虑使用自动生成 [[openapi]] 文档的框架，不想在 Gin 里面手动写注释生成，当时的选型还有 [GitHub - go-fuego/fuego: Golang Fuego - Web framework generating OpenAPI 3 spec from source code - Pluggable to existing Gin & Echo APIs](https://github.com/go-fuego/fuego)，好像是因为在自定义错误码的处理上不灵活，最终都没有使用，选择了 [[grpc]] + grpc-gateway + buf 自动生成的方式。

---


[Automating Linux bare-metal server deployment in Hetzner with Ansible – Palark | Blog](https://blog.palark.com/ansible-hetzner-bare-metal-linux/)

最近因为一个内部 BeraMetal 相关项目的后续迭代方向进行了一些思考，做 BareMetal 太苦了，比如这篇文章中的实现方式，如果没有 [[Hetzner]] API，会非常痛苦。痛苦的点在于：
- 需要适配大量的服务器品牌（国内和国外是两套生态）
- 需要适配同一个服务器 BMC 的不同版本
	- 看似存在 Redfish 这样的通用协议，但是落地下来各有不同
- 需要支持多种引导方式：ISO、PXE、PXE with DHCP
- 很多操作需要重启才可生效，涉及到上层的业务交互


---


### 生活


[来美国的两年后 - GeekPlux](https://geekplux.com/posts/two-years-in-usa)

> 我发现我越来越喜欢用年为单位去描述事情，可能这就是时间加速感的体现。希望自己能在未来的日子里：
> - 保持好奇，保持谦逊，保持怀疑精神
> - 接受随机，接受老化，接受自我平庸

最近也在想，是否“需要”换一个城市生活，还没有想法。

---

[GitHub - jlevy/og-equity-compensation: Stock options, RSUs, taxes — read the latest edition: www.holloway.com/ec](https://github.com/jlevy/og-equity-compensation)

[[股权]]激励指南。 有需要的朋友可以看看，避免发生 zhihu 惨案。

---

[2025 清明凤凰经重装徒步 | Xigou Blog](https://xigou.github.io/blog/2025/04/10/Lantau-Trail)

看着确实太苦了，平时我都不徒步，重装徒步就更不可能了。

---

[我们高估了智力的重要性 | Randy's Blog](https://lutaonan.com/blog/oi/)

在知识获取越来越“容易”的时候，其他方面的影响被放大了。

---

[I'm Leaving Sentry | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2025/3/31/leaving/)

十年。

---



## 书影

《火锅艺术家》，一部典型的东北喜剧人电影。

《饥饿站台 2》，和朋友聊到才发现《饥饿站台》出了第二部，能够感受到创作团队想要表达的内容很多，但是最终呈现出来的效果不好。



## 碎碎念

* 发现自己之前写的单测完全没生效。。
* 买了水月雨的 pill 耳机，第一次用耳夹式耳机，使用感觉上还不错，跑步也没有要掉的感觉。耳机壳是败笔，很多人吹有多好“耍”，可以作为解压玩具，但是平时放在包里和裤兜中，经常自己就打开了，缺少固定锁。
* 吃早饭！不管如何，要吃早饭！