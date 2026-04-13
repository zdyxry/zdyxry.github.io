---
title: Weekly Issue-《飞行家》
date: "2026-04-12:00:00.000Z"
slug: "Weekly-Issue-Take-Off"
tags:
  - Weekly
description:
---

## 文章

### 技术


[The Future Isn't Model Agnostic · The Fly Blog](https://fly.io/blog/the-future-isn-t-model-agnostic/)

> Your users don’t care that your AI project is model-agnostic.

> Every startup pitch deck with ‘model-agnostic’ as a feature should become a red flag for investors who understand product-market fit. Stop putting ‘works with any LLM’ in your one-liner. It screams ‘we don’t know what we’re building.’

这里的一些观点和 [[Ampcode]] 是一样的。

---

[Stripe takes 2.9% + $0.30 per transaction. At $50K MRR that's $17,400/year. Is everyone just accepting this?](https://www.reddit.com/r/SaaS/comments/1s5rw0m/stripe_takes_29_030_per_transaction_at_50k_mrr/)

> $200 in Stripe fees when you're making $5K/mo doesn't register.  
> Crossed $50K MRR last quarter and actually looked at the number. $17,400/year. More than I spend on infrastructure. More than marketing some months.

哇哦，这个收费水平， [[Stripe]] 感觉是大赢家。

---

[Go Proverbs](https://go-proverbs.github.io/)

**A little copying is better than a little dependency.** Rob Pike 2015 年的这句话在 AI 时代可能有新的理解。

---

[EWD 667 · 阅读笔记](https://digest.soulhacker.me/digest/ewd-667/)

> 原文中可能最有趣的一点是 Dijkstra 在最后补的一段话，他说："我怀疑，那些能够用我们的母语——无论是荷兰语、英语、美式英语、法语、德语，还是斯瓦希里语——来编程的机器，不仅制造起来极其困难，用起来也同样困难。"   
> 他老人家可能没想到，这种机器（及其软件）在不到半个世纪之后就做出来了，现在用自然语言“编程”方便又快速，唯一问题是写出来的代码，就像他担心的，充满着各种风险。    
> 也许第二次软件危机真的就要来了。   

---
[身在 Kimi 的 800 天 | K.I.S.S](https://bigeagle.me/2026/04/800-days-at-kimi/)

> Kimi 并不独特，公司并不是没有管理，而是在当前的市场洞察和业务设计下，基于领导者的战略意图与价值观，自然演进出来的文化氛围与组织设计 (这段是为了证明我真的学过而故意不说人话)。说人话：AI 时代每周都有大变化，传统的季度/双月 OKR/KPI 拉通对齐那一套怎么可能跟的上。

> Kimi 并不独特，有人的地方就有政治，屁股决定脑袋是人类社会的必然规律。300 多个不同背景、不同经历、抱着不同目的的人，毫无隔阂相互完全理解，这不仅仅是天方夜谭，我愿称之为 1984/美丽新世界一般的反乌托邦恐怖场面。在相对粗放的管理状态下，不合适的 (意思就是我不喜欢的)人显然也有不少。

流传比较广的那篇公关稿的叙事风格非常的模板化。“Kimi 并不独特”。

---

[Eliminating the ‘Rego tax’: How AI orchestrators automate Kubernetes compliance - Red Hat Emerging Technologies](https://next.redhat.com/2026/03/20/eliminating-the-rego-tax-how-ai-orchestrators-automate-kubernetes-compliance/)

[[RedHat]] 的一篇如何利用 [[LLM]] 来解决自己维护 [[Rego]] 规则的文章。LLM 通过 MCP 从 K8s 集群获取信息，然后基于信息生成报告，由人类 review 最终要上线的规则。感觉这里之所以可以这么搞，很大的原因是黑名单机制，最差情况下，也就是有些禁止行为没有被限制，在有一些现有模板的情况且 dryrun 运行下，影响不大。如果是白名单机制，为了安全和灵活，规则数量爆炸，LLM 上下文出现幻觉的可能性增大，就玩不转了。

---

[The Friendship Recession: The Lost Art of Connecting — The Leadership & Happiness Laboratory](https://www.happiness.hks.harvard.edu/february-2025-issue/the-friendship-recession-the-lost-art-of-connecting)

文章中给了一种解决方式：拥抱不适，建立友谊需要冒险，不适感是冒险的组成部分，并需要持续的维护。

---

[Tailscale pricing update: clearer plans, more value](https://tailscale.com/blog/pricing-v4)

[[TailScale]] 个人版本现在支持 6 个用户，3 个 ACL groups，50 个 tag，无限制的设备。确实是大善人，虽然我主力已经切换到了 [[EasyTier]]，但是我还是会安装上 [[TailScale]] 以防万一。

---


### 生活

[Garmin authentication landscape (Garth, upstream issues, react branch)](https://github.com/bovreuil/garmin-collector/blob/master/docs/GARMIN_AUTH_LANDSCAPE.md)

手表选择 [[Garmin]]，很大一部分原因是社区有这完整的 API，隔壁[[高驰]]需要走申请渠道才行，现在这样搞，导致我的一些数据同步分析脚本都失效了，很难受。

---

[DNA、得意忘形与个体自由 | 默默小屋](https://www.gexiao.me/2026/04/02/live-in-love/)

> DNA 成员的流动性和丰富度是最好的，所以会给我一种贴近大地的感觉：在区块链行业牛市时日常看到的信息都是谁一天赚个几百万，没个 8 位数资产不好意思上桌说话，而在 DNA 一个月只花三千块也可以过得挺不错啥都不缺；   
> 见惯了大家高学历，进大厂，精致好看，丰盛一餐，野心勃勃，偶尔狂欢，而在 DNA 会感受到，比日咖夜酒更开心的，是日咖夜酒时旁边总坐着不会 judge 你的伙伴。

我看过很多次 DNA 的介绍，也几次试图去体验一次，但是总是迈不出那一步。

---

[我们的博客被腾讯爬了，一遍一遍又一遍 | 螺莉莉的数据中心](https://roriri.one/2026/04/03/tencent-scraping)

> 我间接性地把我的智慧分享给了所有人。虽然它被剪碎了，它变成了流体，里面没有我的名字，没人向我致以谢意。但 Again，我没那么在乎这个 Credit。我不觉得大语言模型剽窃了我什么东西，因为它是真的把我的东西学习走了，并且把我的思想传递出去了。只要它没有直接把我的工作 copy and paste，没有在做低端洗稿，对我来说这就不是剽窃，而是学习。作为一名教育工作者，我教育了一个非常伟大的东西，这是一件让我感到非常自豪的事。

---

[写在第一份工作的末尾 - lyle](https://lylex.substack.com/p/f57)

> 我问他们如果是这样为什么不把这两个概念做合并，他们说这个是**他们的产品经理设计的，但是他们的 PM 现在离职了所以成了遗留问题**…）。

> B 的产品建立在我的知识库之上，我原以为他们只是想让我们把召回的逻辑迁移掉，然后他们继续在我们现在都产品上构建其他业务，但是当我终于和另一个团队联调完数据迁移的差不多后，他们说后面就直接用另一个团队的产品了。   
> 我直接一个大无语，如果他们还在我的知识库上，我最起码还可以在产出上多写一条支撑 xxx 业务建设之类，合着纯纯是想着卸磨杀驴？生怕我不配合所以刚好卡在我差不多搞完后才说。

哎。

---





### 书影播客


《飞行家》，蒋奇明、李雪琴主演的电影，改编自双雪涛的同名小说。蒋奇明演的挺好的，“可做任何工种“的状态感觉和我现实生活中的不一样，现实中看到的更多是麻木。看完之后想再去看一遍《钢的琴》。

Davy 的主打秀，据说是他正式专场前的最后一场测试，内容确实不太行，最后只能靠口号来带动气氛了。这场只卖了 100 多张票。开场演员很不错，丹妮，现在很少有女单口演员追求纯粹的好笑了，互动效果很好，如果有她的专场我一定会去看。(20260413 追加：在今年的单立人原创喜剧大赛中，丹妮获得了季军)

《马拉松全方位科学训练指南》，长跑训练教科书。

《伤不起的崴脚》。总结：崴脚先去看医生，如果是小伤，那不会花多少时间；如果是大伤，早介入早治疗。

《自主可信计算技术体系》，周末在图书馆发现的新书，正常日常经常能看到：等保、可信、国产等需求，翻来看看，感觉是听了一个领导在开会，看的云里雾里。以下是一些摘录：

> 当前安全方案大多数由商业公司提出，存在以下局限性：体系化安全机制缺乏理论指引，更多从工程经验出发；安全机制各自为战，缺乏有机配合；商业炒作现象严重，缺少科学评估方法。

> 等保 2.0，全称是网络安全等级保护制度，以网络系统作为保护对象。等级保护 2.0 的理论基础就是可信 3.0。可信 3.0 是目前可从体系结构层面全面支持等级保护 2.0 的唯一技术。

> 在智能安全卡项目成功的基础上，考虑到当时我国政府机关的安全需求和大量使用微软 Windows 操作系统的状况，中软决定于美国微软在 Windows 网络安全方案上进行项目合作，由沈昌祥院士基于主动免疫可信计算的技术路线确定了安全方案。中软公司成立了中软华泰分公司，投入精英技术人员，在 21 世纪初完成了开发工作，产品设计方案巧妙，使用国产密码算法，性能优异。但当时美国将密码视为军火类产品，对软件的密码应用提出了严格限制。项目在结题前，微软引用美国法规，提出美国禁止开放密码接口，因此该项目不得不终止。

> 国产化信息系统是否更安全呢？答案是否定的。国内对应的国产化替代企业技术实力相对薄软、技术积累缺乏，产品版本的技术投入是国际同行的几十分之一甚至百分之一，也缺少安全生态环境的适配测试支持。

> 不同安全保护等级的要求：一级，自主保护；二级，指导保护；三级，监督检查；四级，强制监督检查；五级，专门监督检查。




## 碎碎念

* Google Doc 是 20 年前发布的产品
* 周末刚看到有人说有乙流的趋势，今天办公室就 2,3 个人感冒了。
* 微信给我推荐极光生发仪的广告？？
* 一个朋友的个性签名：保持新鲜。
* 乘数效应，是指经济活动中某一变量的变化导致经济总需求与其不成比例的变化。
* 4 月 1 日是愚人节。我不喜欢愚人节。
* 铁三为了追求成绩，会在跑步骑车游泳过程中，排尿
* 不看好IaS(kills)的做法，古早的运维经验，在 K8s 时代好不容易做到了 Operator 中，有一个明确的状态机管理，现在因为一些工具的阻碍试图让 LLM 根据已有的知识来选择特定的命令去执行，变成了执行过程驱动，不出事就怪了。
* 大米先生吃了 52，飘了。
* 我日常就是拿 kimi-cli 当做通用 Agent 来用的，有了 slock.ai ，更省事了，体验非常好。
* 我当舅舅了。
* 逛街看到了卖鞋垫的店可以测量脚型，终于知道了自己脚长宽是多少，左脚 276/115mm, 右脚 278/116mm，在正常直立站姿状态下，右脚的承受压力更大一些。
* 到了周末可以去世博公园草地上躺着的季节了。
* yukke 的vlog，信息量还挺大的，需要认真观看才行。
* 回来上班第一天，积压的消息感觉就需要处理到周末了。
* 知名喜剧播客听众“好莱坞记者”当黄牛倒卖门票，也不意外。
* 刚工作的时候，公司写字楼在融科，RedHat 在我们的楼上。
* 一大早就开始“不是。。而是。。”
* 好久没遇到过：无法稳定复现，复现步骤一次需要 40+min 的问题了。
* 一个人是否开心，那种状态真的是肉眼可见。
* 想去体验一下高驰，发现上海没有线下门店。