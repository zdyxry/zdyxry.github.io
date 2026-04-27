---
title: Weekly Issue-《寄生首尔》
date: "2026-04-26:00:00.000Z"
slug: "Weekly-Issue-flowers-and-bread"
tags:
  - Weekly
description:
---

## 文章

### 技术

[The Delve Scandal: Fake SOC 2 Audits, Open-Source Code Theft, and Exit from Y Combinator - Captain Compliance](https://captaincompliance.com/news/the-delve-scandal-fake-soc-2-audits-open-source-code-theft-and-exit-from-y-combinator/)

希望 [[Delve]] 能让客户（前阵子的 LiteLLM，今天的 ContextAI）知道，为了合规而合规，最终得到的都是虚假的安全，别为难 2B 厂商了。

---



[Malicious Checkmarx Artifacts Found in Official KICS Docker ...](https://socket.dev/blog/checkmarx-supply-chain-compromise)

[[TeamPCP]] 团伙的近期第二起行动，也是安全工具自身被攻击了，上次是 [[Trivy]]。

---
[Equity for Europeans | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2026/4/23/equity-for-europeans/)

`equity` 这个词确实有些难理解，在 beancount 中，我一直没有使用这个类别。

---

[国内自建 Peer Relay 实现 Tailscale 加速：RTT 160ms → 30ms | 5km](https://5km.studio/blog/tailscale-peer-relay)

用不上，看看也好。

---

[Open source security at Astral](https://astral.sh/blog/open-source-security-at-astral)

[Hardening GitHub Actions: Lessons from Recent Attacks | Wiz Blog](https://www.wiz.io/blog/github-actions-security-guide)

[One CI to rule them all: a guide for pragmatic pipelines](https://abstraction.blog/2026/04/25/one-ci-to-rule-them-a-guide-for-pragmatic-pipelines)

最近的一些安全事件，突然多了很多关于 [[CI/CD]] 的配置管理文章：
- 禁用 `pull_request_target` `workflow_run` ；
- 发布流程隔离在专用环境，需要两人以上 Approved 才可以执行；
- 使用不可变版本进行发布： [不可变版本 - GitHub 文档](https://docs.github.com/zh/code-security/concepts/supply-chain-security/immutable-releases)
- 发布环境不使用 cache，避免通过 cache 投毒；
- 依赖指明具体 hash，禁止依赖库第一时间升级；
- 启用 Action 白名单机制；
- 谨慎使用 `secrets: inherit`
- 显式声明权限： `permissions: {}`

---

[Wisdom from the ancients](https://mp.weixin.qq.com/s/h5cfR0-crW1BRxAKguNJnw)

> 现如今做 Agent Infra 与其重新造轮子，不如看看历史中有没有好用的轮子。有些很有意思的设计，其实在很早之前就已经存在了。这些宝藏可能因为过于晦涩，或者不太符合普通用户的人体工学，以至于它们没有成为主流，但是在 Agent 成为用户的时候，马上就会大放异彩，最近这个 CLI 和 UNIX 哲学的复兴就是一个很好的例子。

> 这些设计在当年没有成为主流，很大程度上是因为它们不够“适合人”。   
> 但如果用户换成 Agent，情况就有点不一样了。

[[9P]], [[Gopher]], [[IRC]].

---

[Software engineering may no longer be a lifetime career](https://www.seangoedecke.com/software-engineering-may-no-longer-be-a-lifetime-career/)

> The career of a pro athlete has a maximum lifespan of around fifteen years. You have the opportunity to make a lot of money until around your mid-thirties, at which point your body just can’t keep up with it.   
> A common tragic figure today is the professional athlete who believes the show will go on forever and doesn’t prepare for the day they can’t do it anymore. We may be in the first generation of software engineers in the same position. If so, it’s probably a good idea to plan accordingly.

周五听了一个内部分享，某一个岗位现在的主要工作已经变为如何更好的服务 AI，当 AI 完全可以覆盖当前的需求后，这个岗位还会继续存在么？我觉得不会。以前觉得离人越近的地方，越值钱，比如销售直面客户，可是之后都是和 Agent 打交道了，这个说法还成立么，变成谁能让 Agent 工作的更好，更值钱？

最近看到一个说法：盘面真是太机智了，如果你把白酒、医药、美妆等等这些传统消费品，定义为“碳基生命”消费，把半导体、PCB、光模块这些定义为“硅基生命”消费，你会有一种感觉，人类已经失去了对股市、对互联网甚至未来的掌控，在这背后，实际的操作者已经变成我们创造出来的人工智能，引导资金向着它需要投入的地方去，而我们只不过是面上的“傀儡”。

---
[关东旅行](https://lynan.cn/kanto-travel-journal-2026/)

> 也许是因为今天是工作日的缘故，在路上没有见到一个游客，享受着这份惬意。

工作日哪怕什么都不做，就非常的惬意。

---



### 生活

[过度联想 - 且听书吟](https://yufan.me/posts/less-is-more)

> 它制造了大量本不存在的矛盾。朋友间一句无心的玩笑，被过度解读为“话里有话”；同事一个寻常的举动，被层层剖析出“深层意图”。本来相安无事，想着想着便琢磨出事来了，给自己徒增无数烦恼与戾气。   
> 更可怕的是，这种臆测出来的“真相”，往往成为攻击他人的武器——“你这么说是何居心”“你这么做一定有目的”。一场场网络骂战、人际冲突，很多时候并非源于真实的矛盾，而是源于我们丰富的“想象力”。    


---

[如何跟孩子讲学习的意义 – est の 输入 输出和出入](https://blog.est.im/2026/stderr-14)

> 不是说用脑就一定比用体力好，而是你会的东西越难、越少人会，你就越有主动权。学习只是其中一条比较稳定的路。  
> 你以后不管做什么，其实都在跟别人交换。学习不是让你一定变得更厉害，而是让你多一些别人需要的能力。你会的东西越特别、越不容易被替代，你就越有选择，而不是只能被安排。

补充说明：摘录的这段话是 [[ChatGPT]] 生成的。

---

[Tim Cook’s Impeccable Timing – Stratechery by Ben Thompson](https://stratechery.com/2026/tim-cooks-impeccable-timing/)

Tim Cook 卸任苹果 CEO，功过自有后人评。目前我还留着的自购产品应该只有 iPad Mini 了。

---

### 书影播客

《寄生首尔》，李惠美2023 年作品，作者是韩国日报的记者，有一句经典的话：“我还是来了首尔以后才知道，原来阳光也是要花钱买的”。这本书讲述的是韩国首尔的“蚁居房”居住情况，蚁居房租户不会主动报税，租住条件差，大部分情况下是为了不要露宿街头，冬天不开取暖设备的状态。在读这本书的时候，我一直在想我自己 2015 年刚到北京的时候，非常感激大学同学能够让我当时留宿过渡，那是一个在西北旺韩家川村的一个隔断单间，当时一个月好像是 550？生活逐渐稳定之后，我就从同学那搬走了，后面同学也离开了北京。当时我的想法和书中描述的想法一样，年轻嘛，觉得只是暂时的，后面会变好的，直到 2017 年北京大兴的那一场大火，让我想着，也许不能继续在北京待下去了，应该换一个地方。书中说，最低居住标准是 14 平米，这个对于刚刚进入大城市生活的人来说，多少有些奢侈，也许是因为经历过很低的下限，所以我对居住条件的容忍度很高，这么多年也是如此。



部分摘录：

作者在书中给“都市贫民”下了这样的定义：都市贫民虽是一群具有劳动能力和劳动意愿的“经济活动人口”，可从社会结构的层面来看，他们是一群徘徊在近代工资劳动体系之外的群体。也就是说，这些人即使努力劳动也还是摆脱不了贫穷的身份。

韩国法律对于人类维持尊严和基本生活需求这件事情，居然是有"最低居住标准"的。《基本居住法》规定了一人户家庭的最低居住标准:"面积为14平方米(约4.24坪)，包含厨房、独立卫生间和浴室等设施。"2015年制定的相关法律中，规定了公民具有"远离物理意义上和社会意义上的危险、居住在安全环境之下、过符合人类基本标准的生活的权利"，首次将国民的居住权纳人法律保护范围内。通过这条法律我们也可以看到，即使是能够躺下、能够遮风挡雨的地方，也并不能和"足以让人类生存的空间"画等号。不过这条既优雅又有威严的法律，并无法触及金字塔最底端的蚁居房。

电影《寄生虫》之所以会演变成悲剧，正是底层人士的"越线"所致。可我们社会的这条"线"到底画在何处?又是谁画的这条线呢?为何底层人士要流浪在线外，或是被隔离在名为蚁居村的特定贫民窟里呢?对此，判断的标准又是什么?是"金钱"和人的"用途"吗?又或者是电影里反复提到的穷人身上的味道呢....

在"贫穷即原罪"的社会中，这个问题确实让人不自在，因为它让被提问人不得不直面赤裸裸的现实。面对这些深层的烦恼以及真实的自我都并非易事。我在深度采访居住在沙斤洞的青年之后，都会抛出这句话作为最后的问题。当时所有的受访者都对这个问题感到不适，因为他们早已将"我不是穷人，之所以在当下身处这种境地，只是在为迎接美好的未来而坚持着"的想法深植于心。这之中很多人都提到了"精神胜利"一词，即便他们对自己目前的处境束手无策。虽然如此，他们依然以美好的未来为前提，甚至刻意忽视这个正在运作的却十分残忍的剥削结构。

即使是拥有这样条件的青年，也不得不委身于"新型蚁居房"这种恶劣环境，面对着利欲熏心、毫无责任感和道德感的"新型蚁居房"房东们压榨青年们血汗钱以积累财富这一现实，耳边甚至还不停萦绕着"年轻人要吃苦"这句所谓的警世名言。社会现实如此，到头来却让年轻人自己去承担社会问题强加给他们的压力。

"人就是得去首尔"这句话，让所有在外县市的大学都变成了"杂牌大学"。"首尔共和国"将所有外县市都变成了"殖民地"，仿佛只有首尔才是"正式的舞台"。到最后，外县市剩下的只有那些不知名公司的练习生，他们连参加节目的面试资格都没有。在这种如果不背井离乡就看不到任何希望的社会，青年们不惜承受残酷竞争的压力也要参加节目，只是为了可以站上舞台一次。前往首尔，前往首尔，朝着那个所有人都想登临的选秀舞台迈进。

越是年轻，就越能吃贫穷的苦。因抱着"只要等待，一切就会有所改善"的期望，很多人都不愿直面自己的贫穷，而是开始将它合理化。他们借着想象中的美好未来宽慰自己，并不认为自己是穷人。可就像之前文中提到的，我们社会的青年，每三人中至少有一人处于"正在工作或求职中"的贫穷状态。






## 碎碎念

* 机器人马拉松比赛补给：换冰块、换电池。
* 过了这周，就有同事陆陆续续过五一了。
* Shangri-La，香格里拉。
* 跟着 LLM Thinking 一路顺畅的进坑了，感觉沿着大脑的边缘就划过去了，非常的丝滑。
* 买了高驰 Apex4。
* A：你放通一下 80443。B：好的，那我放通一下 80443 端口。
* 郝雨的口头禅“不容易不容易”说的是吴鼎啊
* 看到有人说 Cursor 被收购了，查了一下原文是：“Cursor has also given SpaceX the right to acquire Cursor later this year for $60 billion or pay $10 billion for our work together”，AI 时代反转来的很快，要严谨些。
* 抖音上赛百味三明治只要 16.8 .
* 这周过得太过于紧张，以至于没有闲暇时间。
* ”不诱于誉，不恐于诽，率道而行，端然正己。“
* jira ticket 是 codex 生成的，方案评审是 codex 生成的 HTML，解决方案分享是 notebooklm 生成的 PPT。真是新时代啊。
* NAS 相册没有那年今日，不好不好
* 我需要在 Slack 和 Slock 之间有一个连接器。
* 好天气心情就好
* 上图新书书架有一本《AWK 程序设计语言》，10 年前读过，现在 2026 了，都忘光了，也用不到了
* 知春路高兴火锅关门了，我还吃过一次
* 逛了逛新六百，商场太小，即使重新装修感觉上限也不高。
* 跑了 2000km 了。
* 人类破二啦，2019 年基普乔格 2h 挑战，现在 2026 年，已经有两个人破了。