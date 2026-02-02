---
title: Weekly Issue-连云港特种兵
date: "2025-07-07T00:00:00.000Z"
slug: "Weekly-Issue-连云港特种兵"
tags:
  - Weekly
description:
---

## 文章

### 技术


[Thank you, Databend; Hello, LanceDB](https://xuanwo.io/2025/04-thank-you-databend-hello-lancedb/)

[New Chapter in 2025 | Hi, I'm Kante Yin 👋](https://www.kerthcet.com/posts/new_chapter_in_2025/)

[去做类似于 to B 的 Devin 的东西了](https://x.com/yetone/status/1939570458871111785)

在同一天看到了三个人从不同的公司（[[DaoCloud]], [[Databend]], [[BentoML]]）离职，加入了新的公司，共同点是新的公司都是 [[AI]] 方向。

---

[Next.js 15.1+ is unusable outside of Vercel | Omar Abid - Personal Blog](https://omarabid.com/nextjs-vercel)

>  **tl;dr**: Starting with version 15.1.8, Next.js might break metadata handling for non-Vercel deployments, potentially devastating your search rankings. This is not a [bug](https://github.com/vercel/next.js/issues/77519#issuecomment-2770488614).

---

[GitHub - m1k1o/neko: A self hosted virtual browser that runs in docker and uses WebRTC.](https://github.com/m1k1o/neko)

在 [[Container]] 中运行多种浏览器的方式，主要用来多人共享。貌似没有找到设置浏览器版本的配置。

---

[我的颈椎病康复之旅 - 关于选择的故事](https://blog.joway.io/posts/cervical-spondylosis/)

> 我人生大部分的经验都是在追逐目标，这些目标本身并非我自己设定，而是自然而然目标就自己立在了那里。更好的成绩，更大的职级，更高的工资，这些都是社会中毋庸置疑的目标，也有标准的追求目标的方法，直到有一天因为一些旁路发生的意外，被动的人生重新开始主动的思考，自己是为何来到了这里。

---

[Announcing PlanetScale for Postgres — PlanetScale](https://planetscale.com/blog/planetscale-for-postgres)

> We have made explicit sharding accessible to hundreds of thousands of users and it is time to bring this power to Postgres. We will not however be using Vitess to do this.

[[PlanetScale]] 增加了对 [[Postgres]] 的支持，看说明应该不会使用 [[Vitess]] 。结合前阵子这条信息： [Sugu Sougoumarane: Joining Supabase](https://x.com/ssougou/status/1932445665512284645): `For some time, I've been considering a Vitess adaptation for Postgres, and this feeling had been gradually intensifying.`

---

[PlanetScale's classy retirement](https://simonwillison.net/2025/Jul/1/classy-retirement/#atom-everything)

很多软件如果试用期结束后，那么会在结束前的一周或两周以邮件形式通知用户，还有 XX 天数据将被删除，请及时备份或购买新的套餐。[[PlanetScale]] 提供了一种新的方式，数据处于归档状态，用户可以选择激活 24h 来备份数据，而无需购买完整新的套餐。

2B 软件产品会怎么做？我已经不记得处理过多少没有维保但是找上来的客户问题了，万一呢，万一之后客户会复购呢，万一客户续保呢，服务一个购买过的客户感觉比服务一个潜在客户来的感觉好一些。

---

[Get in losers, we're moving to Linux!](https://world.hey.com/dhh/get-in-losers-we-re-moving-to-linux-5e1b93cd)

最近 [[DHH]] 开始推荐 [[ArchLinux]] 了，并将自己之前基于 [[ubuntu]] 的配置方式 [GitHub - basecamp/omakub: Opinionated Ubuntu Setup](https://github.com/basecamp/omakub) 同样应用到了 Arch： [GitHub - basecamp/omakub: Opinionated Ubuntu Setup](https://github.com/basecamp/omakub) 。

当一个有品味、有话语权、行动力拉满、存在争议的人出现来推动一件事情，而这件事情是之前很多年没有阶段性进展的状态，故事可能会出现一些转机。

---

[Deeplinks](https://manual.raycast.com/deeplinks)

[[Raycast]] 的所有 command 都有一个 deeplink，可以在 MacOS 上直接通过 `open` 来执行。

---

[Tools: Code Is All You Need | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2025/7/3/tools/)

让 [[LLM]] 去生成可以重复执行的代码，而不是让 [[MCP]] 去做，[[MCP]] 过于依赖推理。

---


### 生活


[[育儿] 婴幼儿睡眠学习笔记 👶](https://changchen.me/blog/20250620/baby_sleeping/)

看着就头大。

---


## 碎碎念

* 清早起床，现用个10w token 再说。
* 给上海同事听 Qwen 上海话TTS，细节出现了问题，上海话不会说“超级好看”，会说“老好看”。所以 TTS 在使用的时候需要先用大模型讲普通话文本转换为上海话文本。
* 营销是门生意，有时候确实是需要一些“手段”的
* uv 配合 PEP723 可太方便了。坏处就是要先安装 uv。
* asciinema 配合 agg 生成 gif 挺好用的，感觉比 vhs 好用些。
* 现在好像随便一个不是 Rust 写的项目出现漏洞，都会有人站出来说应该使用 Rust 编写的版本。基本法呢？
* 看最近的一些版本迭代，感觉 AI 发展给 K8s 续命了。
* 同事昨天上班期间突然视野缺失，去医院检查发现是脑动脉硬化，好可怕。
* Deepwiki 昨晚 18 点提交一个 repo，今天 11 点索引完成，排队 6338。
* Figma 一年收入$749m ，在 AWS 上的支出是 $110m。
* DeepSeek R1 到现在也才是半年的事o
* 周末需要去连云港参加表姐婚礼，行程非常特种兵，周六去周日回，单程3h40m。很累。
* 现代婚礼已经没有“管事儿的”人了，都是新郎新娘自己费尽心力，很慌乱。在很小的时候，有一个姥爷给我留下了很深的印象，是一个婚礼，他清楚地知道所有的流程，并且全程掌控，感觉婚礼的所有事情都在他的掌控。