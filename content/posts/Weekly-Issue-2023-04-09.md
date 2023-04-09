---
title: Weekly Issue 2023-04-09
date: 2023-04-09
tags:
- Weekly
description: 远离工作的一周。
---


## 文章

### 技术

[Read Every Single Error | Pulumi Blog](https://www.pulumi.com/blog/reducing-our-error-rate/)

阅读每一条错误日志，人力是有限的，如果不能持续保持错误率的提高，那么随着 API 调用的增加，注定 Oncall 精力是不够的：`(API Call Volume) * (Error Rate) * (Time to Triage an Error) < On-Call Attention` 。SRE 模型和错误预算是高级时尚，而跳过步骤直接进入高级阶段并不总是有益的。相反，最好使用合适规模的工具和流程。

> Sure you can hire and split systems out into separate on-call rotations to increase capacity, but our goal is to scale exponentially with respect to humans, not linearly!  

引用[推友的话](https://twitter.com/lowstz/status/1642786327199612929):
> 最核心就是有人盯着这个事情，我们内部 sentry alert 数量从去年每分钟 300 多，今年变成 20 多，就是每周一把异常报错最多的 top5 项目拉出来，让项目负责的工程师看看具体是怎么回事。

---


[GitHub - dastergon/postmortem-templates: A collection of postmortem templates](https://github.com/dastergon/postmortem-templates/tree/master)

通常遇到问题并调查清楚之后都会进行事故分析，这里有很多模版。

---


[8 Immutable Linux Distributions for Those Looking to Embrace the Future](https://itsfoss.com/immutable-linux-distros/)

[[Immutable]] 发行版太多了，大家在 [[Container]] 领域已经卷不动了，现在卷发行版了。配合阅读： [Are We Getting Too Many Immutable Distributions? :: Linux Gaming Central](https://linuxgamingcentral.com/posts/are-we-getting-too-many-immutable-distros/)


### 生活

[人工智能和传统行业的思考。 - Xiaowen.Z Deployed](https://xiaowenz.com/blog/2023/04/decouple-your-time/)

> 传统产业的信息化建设之初，并非是「科技赋能业务」，而更像是「业务培育科技」。  
**准确：传统行业关心的首先是底线**  
人类对世界的积累，对逻辑的理解，对世界的抽象的平均水平和能力，其实惨不忍睹。  
大部分企业的现状其实是：业务部门经常认为研发部门开发的系统功能不好用，研发部门经常认为业务部门讲不清楚需求。  
按理说，大家都是人类，都用自然语言沟通，有啥讲不清楚的？但令人悲伤的事实就是如此，业务需求是对客观世界的抽象和归纳，功能实现是从原始的基础能力往上进行逐层具象和堆叠——他们从未对齐过。  


## 书影


《新宋》，100%，挺喜欢这个结局的，虽然有点草草收尾，但是想不到更好的方式了。

《请回答1987》，Storm 的脱口秀专场，有些人无法理解 Storm 的笑点，喜剧幽默是主观的，有时候不用勉强。

《他是谁》，烂剧。
