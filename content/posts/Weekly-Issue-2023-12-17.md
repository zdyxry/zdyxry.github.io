---
title: Weekly Issue 2023-12-17
date: 2023-12-17
tags:
- Weekly
description:  2023 年单口专场告一段落。
---


## 文章

### 技术

[Open source forkers stick an OpenBao in the oven • The Register](https://www.theregister.com/2023/12/08/hashicorp_openbao_fork/)

[[hashicorp]] license 变更引发的 fork 运动还在持续，好奇这些项目的最终走向。

[[hashicorp]] 上周五股价跌了 16%，关联阅读：[MSN](https://www.msn.com/en-us/money/markets/why-hashicorp-stock-dropped-today/ar-AA1ldXMw?cvid=cb6eb32a86314fd19df2b9489a56c521&ei=16)

---

[从滴滴的故障中我们能学到什么](https://mp.weixin.qq.com/s/Oj4qGrYHq9-z87H2b9WDzg)

[[KubeBlocks]] CEO 的文章：
- 控制规模，用多个小规模 K8s 集群的联邦代替一个大 K8s
- 避免单点，一个 K8s 集群也应该被视作一个单点
- 拥抱重启，把重启和迁移视作常态
- 数据面的可用性和控制面要解耦

---

[“Human error” means they don’t understand how the system worked – Surfing Complexity](https://surfingcomplexity.blog/2023/12/10/human-error-means-they-dont-understand-how-the-system-worked/)

作者认为”人为错误“不存在，真正的原因是系统中的防御机制失效导致的系统故障。可靠的系统具有容错能力，通过演化和隐性的机制来抵御人们日常犯错的情况。当有人将故障归因于"人为错误"时，实际上是因为他们没有看到系统中的这些防御机制，也就意味着他们不了解系统是如何保持正常运行的。

但是具体应该呈现什么错误，如何解释那些错误还是分场合的。

---

[程序的 Metrics 优化——Prometheus 文档缺失的一章 | 卡瓦邦噶！](https://www.kawabangga.com/posts/5606)

如何“正确”的暴露 exporter metrics：
- label 必须可以枚举
- 适当增加针对性的 metrics 可以减少查询压力
- 使用 recording rule 定期聚合查询，多级聚合
- 使用 Stream aggregation 在采集 metrics 时进行聚合，需要注意聚合函数的使用

---

[WHAT IS 10GBIT LINE RATE?](ggfmad.io/blog/what-is-10g-line-rate)

10Gbps 如果传输1500 Byte ，最大带宽可以达到 9.85Gbps：
```
10.00e9 bits / (8bits * 1524 bytes) = 820,209 packets
820,209 packets * 1500 bytes * 8 bits = 9.85 Gbps
```

如果是 TCP 协议，在MTU 1500 的前提下，最大带宽可以达到 9.36 Gbps：
```
10.00e9 bits / (8bits * 1524 bytes) = 820,209 packets
820,209 packets * 1426 bytes * 8 bits = 9.36 Gbps
```

---


[command center: Simplicity](https://commandcenter.blogspot.com/2023/12/simplicity.html)

- 简单性优于复杂性：简单的事物更容易理解、构建、调试和维护。在软件开发和系统设计中，我们应该追求简化而不是复杂化。
- 简化带来的好处：简单的设计更易读，简单的代码更易于测试，简单的系统更易于解释和修复。简单的系统往往运行更快。
- 复杂性的成本：复杂性是指数级增长的，当一个系统的某个部分变得复杂时，其他组件也会反映出这种复杂性。应该控制复杂性的增长，并意识到复杂性带来的效率损失。
- 避免重复和过度复杂化：不要为了解决自己团队的问题而构建只针对特定问题的基础设施。要善于利用已有的系统和组件，避免重复造轮子，以简化整个系统的复杂性。

道理是这么个道理，真正实施上很困难，总要考虑很多的兼容性，很有可能吃力不讨好，但是总是要做出点改变的，不能一边说着这样不好，一边什么都不做，这样影响的只有自己。

---

[Sign in with GitHub in Go - Eli Bendersky's website](https://eli.thegreenplace.net/2023/sign-in-with-github-in-go/)

[[Golang]] 实现[[OAuth]] 示例，分别使用标准库，`x/oauth2` 和 `gologin` 来实现。

另外发现 [[github]] 的 OAuth Apps 得到的 access token 是不会过期的，震惊。来源：[whats the lifetime of Github OAuth API access token - Stack Overflow](https://stackoverflow.com/questions/26902600/whats-the-lifetime-of-github-oauth-api-access-token)

---

[Reclaiming the Web with a Personal Reader](https://olano.dev/2023-12-12-reclaiming-the-web-with-a-personal-reader/)

制作个人的阅读器。我需要一个一模一样的东西，目前是通过将感兴趣的来源转换为 RSS 来实现的，但是总感觉不可控，而且频率不好控制。

---


### 生活

[周奇墨-微博](https://weibo.com/3516836483/NwDki1NFu)

>我姑七十多了，跟我打电话的时候，总爱吐槽自己糊涂了。  
>“唉，真是老太太了。前两天我搁家看电视剧，看着看着，咋感觉里面这人有点眼熟呢。等快演完了才发现，妈呀，这集头天晚上看过。你说招笑不招笑？真是糊涂了。”  
>我说姑你别担心，我也有这症状。有时候一本书快看完了，才发现之前读过，几乎一点印象没有。还有的时候看一条新闻，觉得挺新鲜挺震惊的，等到有结果了，才发现这种事几年前就发生过，不止一次，但自己就是忘了。  
>人人都有点糊涂啊，姑，人人都有点糊涂。

---

[Pluralistic: "If buying isn't owning, piracy isn't stealing"](https://pluralistic.net/2023/12/08/playstationed/)

如果购买不是拥有，那么盗版就不是偷窃。[[DRM]] 对普通用户来说实在是太恶心了。

配合[[索尼]] 最近的新闻阅读：[PlayStation keeps reminding us why digital ownership sucks - The Verge](https://www.theverge.com/2023/12/5/23989290/playstation-digital-ownership-sucks)

---

[月亮落在燕晗山上](https://mp.weixin.qq.com/s/aS8ybS2M-vnwbfuye9Rweg)

>听着口号声，看着眼前无数你买不起的楼静静矗立，无数你买不起的车呼啸而过，你的灵魂就没有个安歇处，你的心就没有个落脚处，在那湿热的暖风中飘飘荡荡，就像是一只被扔到距离家2000公里之外弃养的狗。
>当你的心能够感受到一点什么东西的时候，无论是惊奇、悲伤、欢喜、绝望、同情还是对人性的感慨，虽然你没有得到任何可以拿在手里装进兜里带走的东西，但是你的心得到了润泽，莫名其妙就觉得它充盈了起来，可以在散场之后再次走入汹涌的生活，带着水汽带着温柔带着某种肯定。

一个人在其他城市，能让人安心的时候就是感受“人气”的时候。

配合阅读：[我来深圳这五年之生活篇 | 须臾之学](https://blog.xizhibei.me/2023/11/27/5yrs-in-shenzhen-life/)

---

[我看巴以的冲突](http://www.piginzoo.com/life/2023/11/13/israel-hamas)

>回顾下一个多月来，我自己的立场也几经变化：支持以色列，到同情巴勒斯坦，到重新支持以色列，到最后又演变为反对目前以色列的方式。这一个月来，我不断地了解、学习各种只是和信息，拼拼凑凑，不断地理清很多盲区，逐渐在脑海中还原出相对真实和完整的世界。我不避讳自己态度的兜兜转转，认识事物、认识一件事，就是一个复杂的过程，不是一蹴而就、非黑即白的简单，需要反复拉扯、反复否定、反复怀疑。
>无论如何，希望这场战争早日结束，消灭哈马斯、达成和平协议、以色列撤出加沙、巴勒斯坦人也可以放下仇恨、双方妥协、真正建立一个独立自主的巴勒斯坦国、让巴勒斯坦人可以真正过上平和幸福的生活。而，对我自己而言，也再次体会到，真真正正的认识这个世界，不是一个简单的事情，要时刻保持谦逊、保持良知、保持警惕、保持同理心、保持对这个世界的爱，好好的活着，努力的擦亮眼睛，守住作为普通人的底线和良知。

作为一个普通人，在面对战争新闻的时候，了解的通常是片面的，我也尝试着去了解一些背景，但是这些背景夹杂着各种政治因素在里面，最终就是观点不断地**被**刷新。现在我选择在了解大概之后，不去看这些，逃避虽可耻但有用。

---

[《第二性》读后感 | Xigou Blog](https://xigou.github.io/blog/2023/02/05/The-Second-Sex)

自己也读了一些相关话题的书籍，但对于《第二性》一直保持远离，可能是自己已经丧失了阅读大块头书籍的能力？要反思一下。

---

## 书影

《焦虑青年》，夏夏的专场，围绕着自身的心理疾病展开，夏夏天生带着一股愤怒，不只是语言上的重音，感觉她说的每一句话都非常的有力量。

