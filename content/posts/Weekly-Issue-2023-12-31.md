---
title: Weekly Issue 2023-12-31
date: 2023-12-31
tags:
- Weekly
description:  
---


## 文章

### 技术

[我是如何实现快速部署的](https://capops.xyz/quick-start-poc)

对于部署系统来说，能够快速的本地化验证是非常关键的，无论是快速迭代，还是CICD，或者是产品层面上的架构改进。因为本地化可以让你始终明确的知道当前组件的最小依赖关系，当要引入某个中间件时，可以明确的感知到引入它带来的影响是什么。

---

[NetKit Device - Speaker Deck](https://speakerdeck.com/yutarohayakawa/netkit-device)

[[NetKit]] device 介绍，为了提升 Pod-Pod 之间的传输性能而引入，相较于 veth 的对称结构，NetKit 分为 Primary 和 Peer，可以通过 Primary 端将 eBPF 程序附加到 Peer 端中。

---

[从Adobe放弃收购figma开始说说-白鸦](https://mp.weixin.qq.com/s/PMQFzsBODNDonRkAoMVycw)

为什么 Adobe 要溢价收购 figma？因为 UX 市场很大，figma 定义了设计、协作流程。

为什么 UX 市场很大？因为产品在发展扩展期，需要壮大产品累加功能，需要大量的 UX 设计和实现。

为什么不愿意收购了？猜测是因为资本市场冷静，大量发展期公司选择”拉长发展扩张期“，降低风险。

ChatGPT 可能会对未来的交互产生全新的影响：“对话/命令后直接拿到结果”。

>UX设计将进入一个新的时代。一个图形用户界面和对话式界面混合使用的时代，一个软界面和现实空间融合交互的时代，更细微简单但也更讲究的人机交互，将让人们获得更好的使用体验。

配合阅读：[X 上的 yinggpx](https://twitter.com/yInggp7/status/1739689784640143799)
>设计师不讲究好看，而开始讲设计背后的理念和文化系统。那么就突破了一层。 
>设计师不讲究对象本身，开始讲使用她的人和环境，以及新体验和生活方式，那么又突破一层。
> 最终，认识到即使如此，自己也需要一个很好的团队配合，才能兑现价值，放下自我，那么才算是真正在这个世界自洽了。

---

[#ReadInPublic | Prashant Barahi | realpacific](https://prashantbarahi.com.np/blog/read-in-public)

这个博客实现的效果是我想要的，作者把自己每天阅读的文章作为热力图更新到博客中，并自动渲染了关联图谱。很炫酷，很好。

---


[Finished software](https://world.hey.com/dhh/finished-software-8ee43637)

>It solves their problem, and that’s enough.

这句话很对，能够解决部分人需求的产品，那么对这部分人来说，就是一个有价值的产品。

另一点就是，无论难易，如果做到了极致，就是成功的。

---

[Write inclusive documentation  |  Google developer documentation style guide  |  Google for Developers](https://developers.google.com/style/inclusive-documentation)

[[Google]] 教你如何编写包容性[[文档]]：
- 避免体能歧视的单词或短语，比如：crazy, insane, blind to, blind eye to, cripple, dumb；
- 避免不必要的性别语言，比如：`man-hours` -> `person-hours`；
- 避免使用不必要的暴力语言，比如：violent,hang,hit；
- 如果出现 whitelist , master , slave 等词语，在主体语句中使用描述性词语，在括号内部写明可能带有歧义的词语，比如：The configuration file helps you create a parent node (which is named `master` in the file)；

题外话，和同事聊到这个的时候，说：On-Call 算不算一种不友好？

---


[research!rsc: Semantic Import Versioning (Go & Versioning, Part 3)](https://research.swtch.com/vgo-import)

[[Golang]] 语义化版本管理背景，当需要发布不兼容的版本时，需要显式的切换 go mod 声明。

---

[家庭 Homelab 升级计划: v2 | Manjusaka](https://www.manjusaka.blog/posts/2023/12/28/how-do-I-build-homelab-part2/#V2-%E5%90%AF%E5%8A%A8)

使用 [[BGP]] 和 [[MetalLB]] 来给自己的 [[kubernetes]] 集群暴露服务，为了保证 openwrt 的可用性，引入了 keepalived 来实现 VIP。

>熟悉我的朋友都知道，我是个 SRE

我最近也在想，是不是家里也整点设备搞事情，虽然公司的资源很多，想搞事情很容易，但是总感觉不那么方便。

---






### 生活

[2023冬初关西之旅 - Lynan's Page](https://lynan.cn/journey-to-japan-2023/)
[[日本]] [[关西]] 游记，写的非常详细，很多景色通过图片看都很美好。

啥时候我能走出国门啊。

---

[在美国拥有一辆 Tesla 的成本 - GeekPlux](https://geekplux.com/posts/cost-of-tesla)

一辆 [[Tesla]] Model 3 第一年的成本大概在43k$ 。

前阵子年底聚餐的时候，同事说今年花的最值的一笔钱是买了车，买车和后续维护的成本真的不低啊。

---

[考驾照和买二手车 | Reimu's blog](https://blog.k8s.li/honda-civic.html)
身边同事自从买车了之后，每周末都出去徒步，看着是有些羡慕的。

>由于只请了半天的假，考完后就得赶紧回公司继续搬砖。而每次挂科后，回到公司的心情极差，尤其是同事问起考过没有，心里贼难受 😣。

（em.... 这说的应该是我，有点抱歉。。

---

[Choose optimism — Steph Ango](https://stephango.com/optimism)

>一种假设：如果事情可能出错，那么它们就会出错——恶意是普遍存在的。
>悲观主义者的生活是轻松的，但却是沉闷的。乐观主义者的生活是艰难的，但也是令人兴奋的。悲观很容易，因为它不需要任何成本。乐观是困难的，因为它必须不断得到重申。面对充满敌意、愤世嫉俗的世界，需要努力证明积极性的价值。
>只有乐观的人才能创造美好的未来。只有乐观主义者才能想象得到。只有乐观者才会付出努力来实现这一目标。如果你想创造美好的未来，请相信它可以实现。选择乐观。

---


[城市漫步指南：济州岛，更适合年轻人的短途免签旅行地 - 少数派](https://sspai.com/post/85237)

济州岛[[游记]]。 用同事的话说，济州岛是最方便的出国旅游的地方了。

---


## 书影

《父权制与资本主义》，里面的每一个概念都需要仔细的思考，好处就是很容易在生活中找到示例，还在读。

《赶时间的人 : 一个外卖员的诗》，2023年的最后一天，读完了这本，写父母、写孩子、写陌生人，看了难免感触，推荐。

《她对此感到厌烦》，目前读了 50%。关注豆瓣2023年度榜单的话，应该都能看到这本书，是奇幻·科幻类别的第一名。如果单纯的说奇幻·科幻，那这本书平平无奇，甚至有点差，无论是设定还是故事的呈现上，都没那么出彩，但是这本书的主人公是女主，而且是一个当代的女性穿越，我理解这个题材的受众是明确的，最终的评分之高也是可以想象的。这类书籍确实越多越好。  

（发现过去两周没有记录观影，补一下）

《拾荒者统治》，如果你觉得想象力匮乏，没有什么创造力，那么来看这部剧吧，有很多设定我觉得只有小孩子才能想出来。

《繁城之下》，算是2023年中很好的剧，剧集很克制，推荐。

《憋说话》，史妍的单口专场，从专场角度来看，不像是一个专场，更像是一些段子的集合，衔接处比较生硬。段子好笑，观点犀利，配上她的人格魅力，现场效果很不错。

《泰勒·斯威夫特：时代巡回演唱会 》，在2023年的最后一天，强行找点仪式感，买了跨年场，感觉是粉丝专场，大家都会应援，氛围很好。对霉霉的印象中，停留在学生时期的跟着专辑听，属于路人，但是这个电影，彻底刷新认知，连唱 3 小时，满场奔跑，这就是属于咱们这个时代的 Superstar 吧。在国内还在讨论xx倒嗓yy假唱的时候，差距太大了。