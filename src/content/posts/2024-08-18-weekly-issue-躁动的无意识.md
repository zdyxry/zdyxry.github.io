---
title: Weekly Issue-《躁动的无意识》
date: "2024-08-18T00:00:00.000Z"
slug: "Weekly-Issue-躁动的无意识"
tags:
  - Weekly
description:
---

## 文章

### 技术

https://muratbuffalo.blogspot.com/2024/07/advice-to-young.html

[[Murat Demirbas]] (MongoDB Principal Research Scientist)给的一些建议：
- 很多知识是基础知识，不是理论知识
- 保持动手能力，只有真正写过才能了解其中的细节
	- 不产蜜的蜜蜂只是害虫。每周少量运动是防止肌肉萎缩的关键。
- 每周做一些事情，写一些内容，什么都可以
- 适当的寻求帮助
- 人际交往能力非常重要
- 通过刻意练习培养深度专注

---


https://ytch.xyz/

把 [[Youtube]] 中的视频封装为电视频道，像看电视那样看 Youtube 视频，感觉在家里播放是一个挺好的方式。做一个合格的沙发土豆。

---

https://www.cockroachlabs.com/blog/enterprise-license-announcement/

[[CockroachDB]] 调整了他们的开源许可，他们最早是 Apache 2.0 ，然后改到 BSL，再到现在。
如果你是想要使用 Enterprise 的版本，那么仅限于年收入 1000 万美元以下的企业免费。

越来越多的开源软件逐渐的从 "OpenSource" 变为了 "Source Available"。

[[VictoriaMetrics]] CTO 的评论：[VictoriaMetrics CTO here. I don't understand why pure open-source license such a... | Hacker News](https://news.ycombinator.com/item?id=41266819)

>不明白为什么开源软件要更换 License，如果现在大公司使用你的产品和你竞争，不给你付费，期望更改 License 之后就能收到付费，是不可能的。大公司只会 Fork 项目，用户会分散，更多的人会寻找新的替代品，产品会失去更多的用户和市场份额。

> PS 恕我直言，CocroachDB、Redis、Elasticsearch、MongoDB、TimescaleDB、Grafana 等产品更改许可证的主要原因是收入增长率疲软。股东错误地认为牌照变更可能有助于提高收入增长率，但我不明白为什么......

[508 - Whither CockroachDB? / RFD / Oxide](https://rfd.shared.oxide.computer/rfd/0508)

[[Oxide]] 决定自己 fork 并维护 [[CockroachDB]] ，以满足自身产品需求，不接受外部贡献。

---

https://coroot.com/blog/community/understanding-observability-what-we-can-observe/

当我们在说 observability 的时候，在说什么？

- 为什么需要可观测？Why
	- 性能
	- 可用性
	- 成本管理
	- 安全性
- 我们观测什么？What
	- 应用
		- APM
		- E2E
		- 业务指标
	- 基础设施
		- 公有/私有云的资源和服务
	- 网络
		- 网络性能
	- 数据库
		- 性能、查询优化、资源利用率
- 解决什么问题？
	- Reactive observability （被动，故障定位和优化）
		- Incident response（事故响应）
		- 性能优化
		- 根因分析
	- Proactive observability （主动，预防问题）
		- 异常检测
		- 预测性维护
		- 资源规划

---


[The unexpected emotional cost of being an indiehacker - laike9m's blog](https://laike9m.com/blog/the-unexpected-emotional-cost-of-being-an-indiehacker,158/)

维护开源软件和商业软件的感性部分，是否有会自责，前者可能不会，后者可能会。

也许这是 project 和 product 的区别？

---


### 生活

https://wdwnt.com/2024/08/disney-dismissal-wrongful-death-lawsuit/

>客人在迪斯尼乐园花生过敏死了，提出起诉。迪斯尼律师说你之前注册 Disney+ 时，同意条款里写着不许起诉迪斯尼公司，一切纠纷只能仲裁解决……

原文中提到购买买票中也有类似的条款。

---

## 书影

《黑猫警长》，小时候看动画都是零零碎碎看的，从来没有完整的看过一部什么动画，周末搜了搜，发现《黑猫警长》只有 5 集，每集 20min，掐头去尾的一共也就 80min ，小时候以为很长很长，豆瓣热评：“5集的时长，伴我不只五年的时光。“。其中的第三集的片头配乐，非常的惊喜，那种悬疑感拉满，但是好像只有这集有，其他的就又变成啊～啊～啊～黑猫警长！

《天道轮回》，也有翻译叫《因果报应》，印度悬疑片，我觉得挺精彩的，比《误杀瞒天记》好看，最近几年印度电影质量真不错，尤其是犯罪题材。评论都在说，陈思诚又有电影可以翻拍了。

《躁动的无意识》，作者之前写过《贪婪的多巴胺》，刚看了开头，几十页的样子。作者将人脑的意识氛围有意识和无意识，有意识的部分占比很少，通用无意识的部分会配合有意识的部分，但是如果不是配合而是对抗，就会导致有意识的部分无法按照预想中的顺利完成。比如我们经常看到有些人情绪激动之后，会做出一些平时不会做出的举动，事后还可能会说”我刚刚怎么了“，这可能就是无意识的部分。

我之前一直不理解身心灵，或者相关的事情，每当看到身心灵的新闻，都很不屑。因为我没有过那种感受，触动心灵，直击灵魂。同时也当然觉得自己是唯物主义者。但是我如果去寺庙，我的态度是来都来了，也会拜一拜，我拜的是谁呢？我内心的想法是：耶稣/菩萨/佛祖/仙人，你看我来都来了，拜也拜了，之后万一我有啥事，你如果看到了，帮我一把。

作者举了几个例子，挺有趣的：
- 找了一堆志愿者打高尔夫，告诉其中一部分人他们打的是”幸运球“，告诉另一部分人是”普通球”，“幸运球”的人的成绩要比“普通球”的好不少；
- 如果你用低于市场价格买到了一个房子，买完之后有人告诉你房子里面死过人，你是什么心情？
- 如果按下一个按钮，你会做某件事会成功，你会按么？如果按下一个按钮，你做某件事会失败，你会按么？


> 今天，我们不再相信超自然的生灵拥有无处不在的影响。我们认为头脑内部发生的事情完全有自己掌控，我们将这个功劳归于自己。我们倾向于认为，如果想改变自己的行为，只需要集中精力并且下定决心去做就可以了。自主类的那些书介绍了如何通过十个简单的步骤来获得自律，变得自信并且拥抱成功。这些书有用么？如果它们有用，那所有人都会是身材苗条、坐拥财富、幸福快乐的状态了。

## 碎碎念

* 工夫茶，是指费工夫做的茶。
* 播客重要的是人，不是播客本身。
* Kent Beck: for each desired change, make the change easy (warning: this may be hard), then make the easy change
