---
title: Weekly Issue-安全跑步机
date: "2025-04-13T00:00:00.000Z"
slug: "Weekly-Issue-安全跑步机"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Avoid building a security treadmill](https://www.macchaffee.com/blog/2025/security-treadmill/)

作者自造词，安全跑步机：在安全方面，你需要不断的努力只是为了停留在原地，最终没有取得真正的进展。

故事背景是其他团队为了阻止人们使用免费的 GPU 资源来挖矿，所以提出在 [[kubernetes]] 集群中部署 [[Falco]]（Falco is a cloud native security tool that provides runtime security across hosts, containers, Kubernetes, and cloud environments. It is designed to detect and alert on abnormal behavior and potential security threats in real-time.），作者认为这个修复方式的复杂度先不谈，修复的方法/策略上是否可以改进？现在通过 [[Falco]] 来检查，后面如果矿工用了 [[VPN]]、[[proxy]]，需要部队的更新规则才能维持现在的安全状态。是否可以从其他的方式解决，比如：
- 收取 GPU 使用费用
- 限制网络访问，白名单形式开放
- 沙盒化运行，限制对文件系统的访问

我开发的产品功能，是否也是一个跑步机，要持续的投入才能停留在原地？

---


[It's five grand a day to miss our S3 exit](https://world.hey.com/dhh/it-s-five-grand-a-day-to-miss-our-s3-exit-b8293563)

[[DHH]] 分享公司即将迁移完成所有的 [[S3]]，预计 5 年内可以节省 500 w 美元。当前每年要在 [[S3]] 上花费 150w 美元。购买了 18PB 的 [[Pure Storage]] 产品，硬件费用是 150w 美元，五年的维保费用是 100w 美元，这里没有提到 [[Pure Storage]] 的软件费用？如果算上副本/EC，不知道这个价格是什么级别。国内和海外的硬件价格差别太大了。

---

[2025.03 云原生相关信息简报](https://quaily.com/cloud-native-ralated/p/2025-03-cloud-native-information-briefing)

同事在工作学习过程中整理的 [[kubernetes]] 相关信息简报，目前的更新频率是每月更新。

---


[Three chapters at Cloudflare: Programmer to CTO to Board of Directors](https://blog.cloudflare.com/three-chapters-at-cloudflare-programmer-to-cto-to-board-of-directors/)

> Curiosity and empathy are two core values at Cloudflare, and I am struck every week by how often we’re recognizing teams of people who are being thanked for helping with a sale, fixing a bug, responding to an incident, or helping build Cloudflare. That team spirit is part of what makes Cloudflare a special place to work.

好奇心和同理心。

---

[The Year on Linux](https://world.hey.com/dhh/the-year-on-linux-7f30279e)

> Humans are rigid in the short term, but flexible in the long term. Blessed are the few who can retain the grit to push through that early mental resistance and reach new maxima.  
  
> That is something that gets harder with age. I can feel it. It takes more of me now to wipe a mental slate clean and start over. To go back to being a beginner. But the reward for learning something new is as satisfying as ever.

---

[Great AI Steals](https://world.hey.com/dhh/great-ai-steals-280615be)

> AI has sped through the phase of cheap copies. It’s now firmly established in the realm of good copies. You’re a fool if you don’t believe originality is a likely next step. In all likelihood, it’s a matter of _when_, not _if_. (And we already have plenty of early indications that it’s actually already here, on the edges.)

我一直认为 “Copy” 是一个很好的学习过程，我现在看到感兴趣的项目，还是会花些时间去“抄”代码，不是找到某段逻辑去复制粘贴去解决工作问题，是从头开始一个项目，去 `mkdir` `touch` 一点点去“抄”，去想为什么模块要这么拆分，为什么数据结构这么设计。有些笨，对我有效就行。

---



[Self Hosting Like Its 2025 ::](https://kiranet.org/posts/self-hosting-like-its-2025/)

如果想要脱离 [[CloudFlare]] 的话，[GitHub - fosrl/pangolin: Tunneled Mesh Reverse Proxy Server with Identity and Access Control and Dashboard UI](https://github.com/fosrl/pangolin) 也许是一个可能的选择。

---

[The Wizard and His Shell :: Terminal Click — Bringing Dead Text to Life](https://terminal.click/posts/2025/04/the-wizard-and-his-shell/)

Terminal 的 Grid 能力，看着很有用啊。 "Why don’t other terminals have this? It’s modernity 101." 哈哈。

---

[Our Best Customers Are Now Robots · The Fly Blog](https://fly.io/blog/fuckin-robots/)

我比较好奇的是 [[Fly.io]] 如何识别自己的客户应用场景是机器人的？

---

[Senior Developer Skills in the AI Age: Leveraging Experience for Better Results • Manuel Kießling](https://manuel.kiessling.net/2025/03/31/how-seasoned-developers-can-achieve-great-results-with-ai-coding-agents/)

> So far, I’ve identified three critical measures that are required to work successfully in an AI-assisted coding setup:
> - Well-structured Requirements
> - Tool-based Guard Rails
> - File-based Keyframing

一段清晰的描述、尽早准备完善的 CI/测试套件、提供需求所需要的关键帧（不让 AI 从零创建文件，而是让 AI 在已有的框架下进行完善）

---
[LLMs: an operator's view - by James Stanier](https://theengineeringmanager.substack.com/p/llms-an-operators-view)

> And amongst a tricky economic environment, instead of staying same-sized and increasing output, there has been a trend in many organizations to reduce headcount and combine this with AI tooling to (sort of) _maintain_ the same level of output.

Reviews are more important than ever.

---

[Container CPU Requests & Limits Explained with GOMAXPROCS Tuning](https://victoriametrics.com/blog/kubernetes-cpu-go-gomaxprocs/)

[CPU throttling for containerized Go applications explained - Kanishk Singh](https://kanishk.io/posts/cpu-throttling-in-containerized-go-apps/)

[[VictoriaMetrics]] 关于 CPU Request、Limit、Weight 的介绍，相较于之前的一些讲述这个话题的博客，提到了 [[kubernetes]] 设置 Pod 的具体行为、 `cgroupv2` 的差异、以及 CPU time 的计算方式。

---





### 生活


[How Not to Disagree](https://boz.com/articles/disagree)

当团队领导不同意上级管理层的决策时，常见的错误做法是煽动团队对抗管理层。这种做法短期内可能增强团队凝聚力，但长期可能会造成团队成员的受害者心态、不信任感，最终导致人员流失。

读了两遍，边读边想我身边的 team leader 都是如何应对这种场景的。

---

[X](https://x.com/dieworkwear/status/1909741170953273353)

这条推特用耐克鞋子来举例，讲述关税的影响。

在亚洲生产一双鞋并运到美国大约需要 28.50 美元。这包括 25 美元的劳动力和工厂成本以及 1 美元的运费。运动鞋公司在各种管理费用上花费 15 美元，在税收上花费 2 美元，每双鞋的净利润为 4.50 美元（9%），然后以 50 美元的价格出售给批发商，例如体育用品商店。零售商将鞋子的价格提高 100% 至 100 美元，以弥补各种成本并产生利润，最终零售商赚到的利润大概是 6 美元。

如果提高关税到 104%，那么关税环节的成本会达到 26 美元。

---

[Shopify CEO's Memo Marks A Pivotal Moment For AI In The Workplace](https://www.searchenginejournal.com/shopify-memo-marks-pivotal-moment-for-ai-workplace-usage/543840/)

> “In my On Leadership memo years ago, I described Shopify as a red queen race based on the Alice in Wonderland story—you have to keep running just to stay still. In a company growing 20-40% year over year, you must improve by at least that every year just to re-qualify. This goes for me as well as everyone else.

太难。

---

[Why I don't discuss politics with friends](https://shwin.co/blog/why-i-dont-discuss-politics-with-friends)

要对任何特定问题有一个明智的见解，需要：
- 了解经济学、博弈论、哲学、销售、商业、军事战略、地缘政治、社会学、历史
- 能够理解并同情主题中涉及到的各种（通常是对立的）群体
- 检测并忽略他们自身的偏见

不只是朋友，不要和任何人聊政治。

---


[Knowing where your engineer salary comes from | sean goedecke](https://www.seangoedecke.com/where-the-money-comes-from/)

> **If your work isn’t clearly connected to company profit, your position is _unstable_  **

公司的所有产品/功能目标都非常明确，赚更多的钱，如何赚更多的钱，如何让更多的用户购买我们的产品。

---



## 书影


《流俗地》，黎紫书。讲述马来西亚锡都中一些小人物的一生，写的真好，作者说“我如果要写，就必须写只有我能写，并且我若不写以后也不会有别人写的作品”，这句话不知道是否有夸张的成分，书中的故事让我对马来西亚有了一些好奇。

《幸福伽菜子的快乐杀手生活》，看完了后面 3 集，原来还是一个漫改剧，那更合理了。一直以为能年玲奈是98/99 年的，和永野芽郁差不多大的，没想到是 93 年的，完全看不出年纪。

《梦的解》，单口演员好梦的专场。之前对好梦的了解是通过播客，身上的标签非常明显：辽宁人、中专、喜欢吃、没有上过线上比赛。这次看下来，他没有去线上节目，是正确的，特质可能不会被大多数人接受。他的段子好笑么？有好笑的。段子真诚么？有真诚的。两方面结合的不好，可能是之前看的演员结合的太好了？这场演出的主持人没有把场子热起来，后面靠着开场演员贤鱼好了一些，然后到好梦这里又有点凉了。观看体验不太好。

## 碎碎念

* ai.dev 现在指向了 google 的 aistudio，有钱就是好。
* 能找到一双合适的鞋子非常难，今天买了第三双特步行云 DC，但是它完全不耐磨，穿半年就不行了。
* Cursor 的ARR 增长率超过了 Wiz，好恐怖。
* 一句地狱笑话：如何区分大 s 还是小 s，逝者为大。
* 世界为什么变成了这样。
* 很久之前看发姐直播的时候，想的是，此时一起看直播的都是谁呢，现在发现，推特上很多人都看，这也算是一种“人以群分”？
* 家里人安排相亲，连对方的名字都不告诉我，多荒谬啊。
* 不记得我上一次认识新“朋友”是什么时候了。
