---
title: Weekly Issue-《欢迎来龙餐馆》
date: "2026-08-16:00:00.000Z"
slug: "Weekly-Issue-Once-Upon-a-Time-in-the-Middle-East"
tags:
  - Weekly
description:
---

## 文章

### 技术

[两块 Gen3 x4 NVMe，速度差了一倍 · fanyang](https://fuis.top/memos/nvme-pcie-path-performance/)

> PCIe 协商速率一样，经过三级桥的 NVMe 还是慢了一半。

做硬件拓扑检查是多么的重要。

---

[How to Manage Connections Efficiently in Postgres, or Any Database — brandur.org](https://brandur.org/postgres-connections)   
[Does anyone run Postgres without PgBouncer? — brandur.org](https://brandur.org/fragments/postgres-without-pgbouncer)    
[PgBouncer - PlanetScale](https://planetscale.com/docs/postgres/connecting/pgbouncer)

结论，**几乎**所有主流 [[PostgreSQL]] 提供商都使用 [[PgBouncer]]： **Connections from application servers should be made via PgBouncer whenever possible.** 看了下几个 PG 实例配置，感觉和最佳实践差距有点大。

---

[How I delegate the work, not my judgment](https://depot.dev/blog/delegating-work-not-judgment#im-responsible-for-judgment)

> The question I keep coming back to is "If I am mostly reading the final answer, when am I building the intuition to challenge it?"

---

[大公司与创业公司的 AI Coding 体验差异](https://blog.joway.io/posts/ai-coding-in-big-and-startup-company/)

> 如果环境允许你充分发挥自己的主观能动性，在质量与速度之间，发挥自己的审美和判断力来做取舍，这种工作的创造感其实远高于传统人工编码的时代，但也对实操人的素质提出了更高的要求。

这周的一个任务，Codex 大概花了 30min 完成了代码开发，因为涉及到很多场景，我又花了 1 天的时间在考虑各种边界情况，完整的 review 完了代码，发现了一个 bug，说快也快说慢也慢。

---

### 生活

[Joining Cursor](https://arslan.io/2026/08/10/joining-cursor/)

> But as with many things, the timing wasn't right. We were too early. Eventually the company closed

**你知唔知咩叫 timing 啊！**

---

[Nobody wants to read your shit](https://muratbuffalo.blogspot.com/2016/06/nobody-wants-to-read-your-shit.html)

> - Every story must be about something. It must have a theme.

Subject：讲了什么；Theme：中心思想。

---

[Mapping the AI economy](https://stripe.com/blog/mapping-the-ai-economy)

> Subscription businesses using Stripe’s Adaptive Pricing feature saw a 4.7% boost on average to initial conversion, and a 5.4% boost on average to lifetime subscription value.

采用当地货币可以带来更好的付费意愿提升和长期订阅意愿。

---


[丙午六月纪事：舟车劳顿](https://panqiincs.me/2026/08/12/bingwu-sixth/)

> 人太容易被网络舆论牵着走了，就像前面提到的阿根廷队被诋毁、北大数院被造谣这两件事。有人能及时醒悟，有人则死不悔改。我常常在不同人嘴里听到同样的论调，很多都是在网上刷屏的、明显错误的观点，稍微用逻辑和事实一对照就能看出来。   
> 散布这些言论的人，很多都是坏人，为了流量不择手段。大多数普通人则是人云亦云，别人说什么就信什么。错误的认知，小了影响个人选择，大了败坏社会风气。要学会获取优质信息，学会正确思考问题，不要做正常的傻瓜，被人牵着鼻子走。

---

### 书影播客

周末的两天时间，分别看了《欢迎来龙餐馆》 和《奥德赛》，在看之前对两部电影没有任何了解，只是朋友分享过几期播客简单的聊过一些，还挺庆幸自己是先看的《龙餐馆》后看的《奥德赛》。两部电影的核心表达都是反战，呈现的效果差别很大，龙餐馆是通过一个“局外人”的视角，奥德赛是通过参与并主导战争的视角来讲述。

作为外来者，徐福的菜一直被当地人老扎说偏咸，老扎去过中国，我猜偏咸和偏闲大概率是知道的，最初徐福只是想赚钱还债，还了债之后发现可以赚更多的钱时，他留下了，想赚更多的钱，他觉得战争和他没关系，他就是一个生意人，无论你是当地政府、美国大兵还是恐怖组织，只要你来消费，那都是我的上帝，后面这些人也真的成了他的“上帝”。马俊生说自己的胆子很小，只有一点点，但是胆子很小的人是不会去中东国家赚钱的，他自己是孤儿院长大，所以他对于当地的孤儿很照顾，女朋友也是孤儿院的老师，他以为他们和自己是相同的境遇。徐福和马俊生作为中国人，对于孤儿院长大的赛夫，都代入的是中国孤儿院的孩子，所以他们不理解为什么赛夫要主动去参战，没有参与过战争的人是无法理解战争的残酷，以及战争对于当地人留下的创伤，换一个角度，如果赛夫是马俊生的儿子，当马俊生死了，徐福看到赛夫去主动参战，徐福还会阻止么？当战争发生后，徐福和马俊生赚钱的时候，是否想过《潜伏》中的谢若林呢？他们早已是战争的一部分。

龙餐馆中国内的片段是发生在东北，徐福的台词感觉沈腾（齐齐哈尔人）做了很多生活化的改动，非常的东北，非常的黑龙江，我都能感受到那些台词从我爸口中说出来的样子，他在监狱中给家里打电话的那场戏，我觉得处理的不好，无论是女儿还是他，可能是我脑子里想的是《星际穿越》的片段，对比之下不好。蒋奇明演的很好，比沈腾好，印象最深的台词确实是他的那句“他妈的，没糊弄过去”。这是一部非常合格的商业类型片，文牧野对于观众情绪的把控是非常精准的，电影中第一个情绪高潮点，我看了下时间，刚刚好是 60min，我想到了李逗逗的那句“我是不是太要了”。最后，电影拍做饭什么时候能脱离《饮食男女》？

奥德赛的故事如果没有背景知识了解可能看的有些吃力，奥德修斯是国家的国王，他参与并制定了特洛伊木马方案，最终获得了特洛伊战争的胜利，在战争过程中，开始反思自己到底在做什么，此后的回家路途，他一直在想理清楚，但他自己就是那个参与到战争中的人，无法脱离，自己的妻子和儿子在家中面临的最大的威胁，恰恰就是自己，越想尽快越想不尽手段的回家，越深陷其中。在看的时候，我一直在想，神明真的存在么，所有人在说宙斯法则，宙斯法则生效过么？战争发起者就破坏了宙斯法则，如果说带走海伦最终的惩罚是国破人亡，那奥德修斯在回家途中也一次又一次的破坏了宙斯法则，得罪波塞冬、太阳神，但是最终他还是回到了自己的家乡，如果神明真的存在，为什么不让他命丧大海，而选择长时间的精神上的惩罚？神是有偏爱的么？奥德修斯相信神明么？我觉得是不信的。

电影有 170min，配合着非线性剪辑，有压迫感的配乐，作为观众已经感受到了奥德修斯回家的漫长。主演阵容太强大了，马特达蒙 1970，安妮海瑟薇 1982， 罗伯特帕丁森 1986， 荷兰弟 1996，几位主演的实际年龄和剧情刚好能对应的上，罗伯特感觉演的不好，坏的太扁平了。安妮海瑟薇感觉演的是最好的，尤其是和荷兰弟对话的那场戏，情感上的压抑，对丈夫的思念，对儿子的愤怒，太好了。

不管怎么说，两部电影都是值得看的好电影。



## 碎碎念

* 没想到有一天看一个超市的官网看的津津有味，可能也是因为之前在家乐福干过兼职，很熟悉： http://new.butsm.com/index.php?r=index
* 同事问一个问题，我说这篇文章讲的很清楚，你看看。同事转手就把文章发给 AI 让 AI 总结。
* 基建越好，迭代速度越快，包括不限于：文档、CI、CD、Dogfood。
* > Kubecon/KCD 明文要求三人及以上的联合演讲必须有女性
* 《佳里办》确实好看，放松，开心，吴鼎的出梗速度，目前是最顶级的了。
* 片假名的恐怖，见识到了，怎么区分 source 和 sauce ？role 和 roll ？
* 我在沈腾身上看到了我爸。
* 吴向东的 vlog 文案都是 GPT 生成的了。
* 突然想统计一下，自己一周会看到多少篇 AI 生成的文章。
* 大家在小红书上有郫县来指代豆瓣。
* 《独树不成林》被扒出洗稿，不意外，造神有多快，塌的就有多快。