---
title: Weekly Issue-《精英的傲慢》
date: "2024-09-22T00:00:00.000Z"
slug: "Weekly-Issue-精英的傲慢"
tags:
  - Weekly
description:
---

## 文章

### 技术

[JavaScript™](https://javascript.tm/)

```
`<meta name="twitter:site" content="@deno_land">
<link rel="me" href="https://fosstodon.org/@deno_land">`
```

一封让 Oracle 释放 JavaScript 商标的公开信。

没有理解拉着人签署公开信的意义。公开信的正文内容几乎没有提到 Deno，HTML 中的 meta 和 link 指向的是 Deno，域名的 Owner OrgName 也是 Deno，一个商业公司，让另一个商业公司放弃商标，发表公开信，而不是走法律途径。如果这个公开信是个人名义发起的，感觉更令人信服？

>A previous [blog post](https://tinyclouds.org/trademark) addressed this issue, requesting that you, Oracle, release the trademark. Unsurprisingly, the request was met with silence.

正文中提到的之前请求 Oracle 释放商标博客，那只是一篇博客，不是什么正事的商业行为， `the request was met with silence` 也是可以理解的？

能够理解对方是 Oracle，双方存在体量上的差距，正常的走法律程序大概率会失败，现在拉着整个社区一起让 Oracle 先受到道德上的谴责，后续对法律程序也有帮助？很多人签署之前，应该没有注意到这个公开信的 Owner 是 Deno。

不知道什么时候开始，自己思考问题的方式变成这样了，不知道是好事还是坏事。

---

[Yet Another REST Client?](https://yaak.app/blog/yet-another-api-client)

[Why Not Open Source?](https://yaak.app/blog/why-not-open-source)

[Yaak Is Now Open Source](https://yaak.app/blog/now-open-source)

[[Yaak]] 是 [[Insomnia]] 作者创建的新的 REST Client。2014 年推出 [[Insomnia]] 后，获得了某种意义的成功，但随后作者陷入了大量的 issue 和讨论中，作者感到了倦怠（burnt out），于是将其出售给了 [[Kong]]。

作者加入 [[Railway]] 之后，发现自己工作中还需要一个 API client，于是先尝试 Insomnia，发现已经远离了自己的初衷，且发现市面上大部分 API Client 都 `but every tool left me wanting more.`。

于是又创建了 [[Yaak]]，但是没有公开发布。公开发布的契机是 [[Insomnia]] 的几个行为：添加了 Github star widget、强迫用户需要创建用户才可以使用。这两个行为甚至让作者觉得出售 [[Insomnia]] 是一个错误。于是公开发布了 [[Yaak]]。

其中关于 [[Yaak]] 是否应该开源，最初是不想开源的，因为觉得开源没什么收益，且会让自己再次陷入 [[Insomnia]] 的处境，但是后来发现可以开源但是不接受功能级别的 PR，还是决定开源，目前是 [[MIT]] 协议。

---

[Why Scrum is Stressing You Out - by Adam Ard](https://rethinkingsoftware.substack.com/p/why-scrum-is-stressing-you-out)

- Sprints never stop
- Sprints are involuntary
- Sprints Neglect Key Supporting Activities

其中提到的 Sprint 和 waterfall 两者的压力是完全不同的，Sprint 没有停止，结束了一个开始下一个，waterfall 是阶段性的。前者是持续性的中级压力，后者是阶段性的缓慢上升的压力，虽然后者的压力峰值会大于前者，但一个是中长期压力，一个是较高的短期压力。持续的中长期压力会带来很多负面影响。

其次 Sprint 如果从 PM 角度来看，一个功能结束之后，可以立即开始下一个功能，仿佛功能只需要组装就可以立即开始，不需要准备工作的。实际上 Sprint 也面临着 Release 的压力，所以可能会变成持续的中长期压力，随着 Release 到来，变成了较短的高级别压力，直到产品发布。

---


[News regarding your Pivotal Tracker subscription | Pivotal Tracker Blog](https://www.pivotaltracker.com/blog/2024-09-18-end-of-life)

>Pivotal Labs was acquired by EMC back in the day. They bundled it with some cloud foundry work and created Pivotal. When Dell acquired EMC they also acquired a big share of Pivotal. Dell then decided to squeeze more blood from the VMWare stone and forced them to acquire Pivotal before selling the whole thing off to Broadcom.

记得前阵子 [[Meta]] 也关闭了一个类似系统，导致大量用户迁移，现在 [[vmware]] [[Tanzu]] 也关闭了 Pivotal Tracker，又有很多用户需要迁移了。所以说 [[Jira]] 不好用是因为市面上没有能打的啊。

---

[Visual guide to SSH tunneling and port forwarding - ITTAVERN.COM](https://ittavern.com/visual-guide-to-ssh-tunneling-and-port-forwarding/)

SSH 端口转发图示。

---


### 生活

[从自然拼读看资本的力量 | 辛未羊的网络日志](https://panqiincs.me/2024/09/15/nonsense-phonics/)

>真正令我震惊的是这背后**资本的力量**，为了卖课程，竟然能动用如此多的资源反复轰炸用户。大量没有分辨能力的人很容易上当，不仅花了冤枉钱，还浪费了时间。多年来，许多看似正确但实际上错误的观念，不也是以这种方式深深固化在人们心中的吗？

永远不怀疑资本的影响。

---

[Nothing: Simply Do Nothing](https://usenothing.com/)

什么都不做，从生活中的一切摘出来，静静的发呆，享受此刻。

很难做到，感觉也属于某种意义的冥想。

---


[Update from Amazon CEO Andy Jassy on return-to-office plans and manager team ratio](https://www.aboutamazon.com/news/company-news/ceo-andy-jassy-latest-update-on-amazon-return-to-office-manager-team-ratio)

[[Amazon]] 要求员工每周在办公室工作 5 天。世界要恢复到疫情前的样子了么？

---

[在迈克尔·桑德尔笔下，看见精英的傲慢 - Stay Out Space](https://www.wuyi.space/2022/04/03/%E7%B2%BE%E8%8B%B1%E7%9A%84%E5%82%B2%E6%85%A2/)

>对于绝大多数寻常人来说，如果没有一个强大的精神内核，那么往往需要通过一些尺度来衡量自己，比如薪水的数值、房子的坐标或其他具备普遍共识的刻度。

>而建立精神内核，又是一件困难的事情。因为我们可能会在试图了解自己和社会的关系的过程中，对人们处理不同关系时所运用的不同逻辑感到矛盾与困惑。抑或在寻找自我的过程中，落入新自由主义的某些陷阱，成为一个孤独的偏执狂。

>另一个更常见的情况则是：没有接受精英教育，缺乏探索世界与掌控自我的智识，对于自己处在一个毫无权力的时代感到茫然失措。

>**“现代社会的基准体系限制人们不是从自身而是从各个层面去设计人生。”**我们就是这样被自己既不能理解又无法驾驭的力量所驱使着——这也是自我看社科类书籍以来的一大收获。

>看社会学&人类学的这两年，我经历了心态的转变，从最初的如饥似渴，到期间的“政治性抑郁”，再到后来逐渐沉静地生活。我发现，社会科学并不能给人们答案，也不能救赎失意的心。它只是把这混沌的世界，用一个个切片呈现出来，从一段段田野调查中，挖掘这个世界的精密与复杂。然后，你自己得完成对自己的解剖与救赎。

喜欢这个作者的文字。

---

## 书影

《精英的傲慢 : 好的社会该如何定义成功？》，迈克尔·桑德尔的书，提出了问题，但是没有给出解决的方式，或者说我觉得他给出的方式无法解决。书有些啰嗦，用同事的话说”美国人写的书，永远都很啰嗦“。

> **大学招生录取是优绩制的表现形式之一。优绩主义伦理的核心是，成功是凭借自己的努力和奋斗可以获得的东西，“英雄不问出处”，你哪怕出身贫贱，“只要努力，就能成功”，如果每个人都有平等的机会，那么成功者就应该获得奖赏。优绩主义其实本来蕴含着一种打破固定阶层、让社会流动的许诺，但现实情况是，它最终没有实现它所许诺的理想。**

> **这对年轻人来说是沉重的负担，也是对公民情感的腐蚀。因为我们越是认为自己是白手起家、自给自足的，就越难学会感恩和谦卑。而没有感恩和谦卑，我们就很难关心公共利益。**


> **精英阶层的傲慢反映了成功人士倾向于过度沉醉在自己的成功中，而不记得有助于他们成功的时机和好运。**

> **近几十年来劳动人民的经济和文化地位的下降并不是不可阻挡的力量的结果，而是主流政党和精英统治方式的结果。**

> **但即使是这种不平等的爆发，也不是民粹主义者愤怒的主要原因。长期以来，美国人一直容忍收入和财富的不平等，认为无论一个人的人生起点是什么，他都有可能从贫穷变得富有。这种对向上流动可能性的信念是美国梦的核心。**

> **“只要你努力，你就能成功”。这类箴言是双刃剑，在某种程度上鼓舞人心，另一方面却令人反感。优绩至上的观念祝贺成功者，却诋毁失败者，即使在失败者自己的眼中也是如此。对那些找不到工作或入不敷出的人来说，他们很难摆脱一种令人沮丧的想法：他们的失败是自己造成的，他们纯粹是无能或没有努力追求成功。**

> **如今，我们看待成功的方式就像清教徒看待救赎一样，我们认为成功不是靠运气或恩典，而是凭借自己的努力和奋斗。这是优绩至上理念的核心。**

> **个人的作为有多大作用，这个问题在基督教关于救赎的辩论中再次出现：信徒能否凭借遵守教义和善行主动求得救赎？或者，上帝只是在完全自由地决定拯救的对象，而不管人们选择如何生活吗？**

> **我注意到，大学生中的精英意识并不是美国独有的现象。2012年，我在中国东南沿海的厦门大学做了一次演讲，我的演讲主题是“市场的道德限度”​。近期的头条新闻报道了一名中国少年为了买iPhone（苹果手机）和iPad（苹果平板电脑）而卖掉了自己的一个肾，[1]我问学生们对这件事情的看法。在随后的辩论中，许多学生持自由主义观点：如果该少年在没有压力或胁迫的情况下自愿同意卖肾，那他有权这样做。也有一些学生不同意，认为富人可以通过从穷人那里购买肾脏延长自己的寿命，这是不公平的。大厅后面的一位学生提出：有钱人赚了钱，就是有功劳，所以应该活得更久。**

> **美国人比世界上大多数人更坚持这样的信念：努力工作才能成功，我们的命运掌握在自己手中。根据全球民意调查，大多数（77%）美国人相信人们只要努力就能成功，只有一半的德国人这么看。在法国和日本，大多数人认为努力工作并不能保证成功。[32]**

> **把大学文凭作为获得有尊严的工作和赢得社会尊重的条件，围绕这一理念构建政治，会对民主生活产生腐蚀作用。**


## 碎碎念

* 有时候感觉好像自己成为了少数派，很怕被“代表”。
* 听到了一个没听过的词：“未经教育的残忍”
* 偶尔无法连接 AI 的时候，发现没有补全还是会造成效率下降的，比如一些常见的基础代码补全。
* 为什么座右铭要叫座右铭呢
* 成长可能更多来自于处境的变化，而不是经历的增长
* 体制内和体制外真的是生殖隔离，屁股决定脑袋，已经无法沟通了。