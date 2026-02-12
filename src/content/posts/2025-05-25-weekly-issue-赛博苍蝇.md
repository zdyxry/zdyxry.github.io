---
title: Weekly Issue-《赛博苍蝇》
date: "2025-05-25T00:00:00.000Z"
slug: "Weekly-Issue-赛博苍蝇"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Am I online?](https://antonz.org/is-online/)

原来有 `http://google.com/generate_204` 这种来专门用来检查网络连接的 API。

---

[X](https://x.com/mitchellh/status/1923422158463865009)
[x.com/mitchellh/status/1923424307084132770](https://x.com/mitchellh/status/1923424307084132770)

> "Every single person in this hallway is a Microsoft paid employee."

> "Microsoft sent suits. Amazon sent hoodies. Google sent nobody."

2B 的产品在后期功能趋同，对用户来说形成明显感知的都是服务。

---

[Zero-Touch Bare Metal at Scale](https://blog.railway.com/p/data-center-build-part-two)

> Since it’s 2025, we just ask Claude.
> There are probably more effective methods of achieving the same, but it costs us less than a dollar to provision 50 servers using Claude to screen-scrape every minute during the install.

我喜欢看到 [[Railway]] 分享自己从零开始构建自己的 [[BareMetal]] 产品线的博客，但是其中的一些细节感觉让人迷惑，OS 安装这样一个在 BareMetal 中高频且基础的动作，依赖于外部的 Claude API，并且这个 API 还是一个需要付费的 API，这不是一个稳定且可持续的事情，太奇怪了。

---

[The Lost Decade of Small Data? – DuckDB](https://duckdb.org/2025/05/19/the-lost-decade-of-small-data)

> History is full of “what if”s, what if something like DuckDB had existed in 2012? The main ingredients were there, vectorized query processing had [already been invented in 2005](https://www.cidrdb.org/cidr2005/papers/P19.pdf). Would the now somewhat-silly-looking move to distributed systems for data analysis have ever happened?

---


[Introducing Hardened Images | Docker](https://www.docker.com/blog/introducing-docker-hardened-images/)

[[Docker]] 出的这个 DHI 看着很不错啊，后面可以试试， 即使都是收费服务，感觉也会把 Wolfi 干掉。

---

[Python Tooling at Scale: LlamaIndex’s Monorepo Overhaul — LlamaIndex - Build Knowledge Assistants over your Enterprise Data](https://www.llamaindex.ai/blog/python-tooling-at-scale-llamaindex-s-monorepo-overhaul)

[[LlamaIndex]] 介绍自己从 [[poetry]] 迁移到了 [[uv]] 的背景，他们是一个巨大的 [[Monorepo]]。
PR： [Migrate repo to \`uv\` by masci · Pull Request #18524 · run-llama/llama\_index · GitHub](https://github.com/run-llama/llama_index/pull/18524)

---

[An Evaluation of "Deep Research" Performance | Science | AAAS](https://www.science.org/content/blog-post/evaluation-deep-research-performance)

> As with all LLM output, all of these things are presented in the same fluid, confident-sounding style: you have to know the material already to realize when your foot has gone through what was earlier solid flooring. That, to me, is one of their most pernicious features. I know that these things were not designed _per se_ to glide over or hide their weak points and their mistakes, but they do a terrific job of it, and that's not really what you want. So as much as I found some parts of the Deep Research output impressive, I found its deeper research problems hard to deal with.

---



### 生活

https://frostming.com/2025/henan/

> 拿到咖啡时的我眼泪差点掉下来，13 块钱的美式足足有一升！

> 但是清明上河园和万岁山武侠城这两个沉浸式复原古代生活场景的园区，绝对是能值回票价（那场打铁花和烟火表演，在我看过的所有里面都算顶级的，单这一场表演就能值 120 块），推荐一去。

[[河南]]记录，之前也看过一些 up 主去过“只有河南”，感觉可以错峰感受一下。

---
[Bus Stops Here: Shanghai Lets Riders Design Their Own Routes](https://www.sixthtone.com/news/1017072)

[[上海]]公交提供了定制功能，用户提交自己的需求，当需求达到一定人数，则开通对应线路，看了下当前线路，有些还挺有吸引力的。

---

[我的三天心动原则 | So!azy](https://blog.solazy.me/20250501/)

> 这个原则的核心是：如果我对一个原本没有采购计划、并非刚需的物件儿突然心动，想要购买，我不会立刻下单，而是给自己 3 天的冷静期。在这 3 天里，如果我每天想起这个物件儿时，依然觉得它很吸引、很需要，那么就可以考虑购买。反过来，如果这 3 天里我对它的热情减退，或者根本没怎么想起它，那就说明这东西可能只是让我一时上头，不值得买。

我本身没有那么多的购物冲动，但也会有类似的控制机制，这里提到的**连续**机制挺有趣的，可以采纳。

---
[网友怒喷峰哥：“峰哥你是不是不信中医？！”\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1kvJMzFEUg/)

>  [[中医]]有用，有什么用？证明老祖宗的智慧，证明我的老祖宗的智慧比你老祖宗的强，从而证明我比你强。

---

[No matter what you do, always leave a breadcrumb | Garrit's Notes](https://garrit.xyz/posts/2025-05-20-no-matter-what-you-do-always-leave-a-breadcrumb?utm_source=rss)

> Output always means value, even if it's not immediately apparent. Just keep on laying down those breadcrumbs.

喜欢这篇简短的文章，无论你做什么，可能有意义或者无意义，随时随地记录自己的想法，写下来，这是最真实的想法和感受。

---

[Joe 的折腾日记](https://houjoe.me/thoughts/how-to-reach-consensus/)

> 争论在工作和生活中不可避免，如何达成共识，有两个我觉得非常实用的方法：放慢语速，以及，始终聚焦不同点。

放慢语速是一个近些年学会的技巧，任何信息都是，多给自己一些思考的时间。

---
[The Future of Customer Support is Lies, I Guess](https://aphyr.com/posts/387-the-future-of-customer-support-is-lies-i-guess)

虽然随着模型的能力越来越强，我是相信 [[LLM]] 可以越来越好的完成客服的功能的，但是现阶段 (2025)，如果一家公司提供的产品能**方便**的联系到人工客服，那是真正的加分项。

---

[关于培训 | Oilbeater 的自习室](https://oilbeater.com/2025/05/24/about-training/)

> 主动学习的人会更多依赖自己思考来解决问题，而不是依赖老师的讲解，这个方法看似低效其实最终效果会更好。

---

[樱花特辑：东京圈赏樱指南 (上) - Simon's Blog](https://song.al/sakura_1)

[[日本]]观看 [[樱花]]指南。

---

[What is HDR, anyway?](https://www.lux.camera/what-is-hdr/)

有趣的 [[HDR]] 科普文章。

---

## 书影

《赛博苍蝇》，吴鼎的单口喜剧专场。这是他的第二个专场，我第一次看他线下的演出，之前对他的了解仅限于播客。我挺喜欢这个专场的，简单、直接、爆笑，不经意间的谐音梗让人冷不丁的笑出来。现在越来越多的演员想要通过单口来表达自己的观点和想法，不是说不能表达，是这个边界很难把握，很有可能变成一个说教、或者一个口号式的宣讲。演员们为了“红”，现在的演出中都会说一些“金句”，估计是为了今年的综艺在努力吧。

单口喜剧综艺让线下行业更好，更多的观众会去看单口，是一件好事，很多演员会在综艺节目上讲自己专场的内容，毕竟他们经过检验的段子数量就那么多。希望演员们在上综艺之前，能把自己的专场录制下来，作为独立的作品上传到平台上，好过一个个片段。一个段子线下可能讲 15 分钟，线上受限于内容限制或者时长限制，只能压缩再压缩，最后剩下 7 分钟，感觉从长期发展的角度，完整的作品比“金句”更有价值。

《机智住院医生生活》，应该是属于《机制的医生生活》的衍生剧，故事的主体从教授转移到了住院医身上，我的理解是医学生大概会经历：实习、规培、住院医、主治医，这样的过程，住院医是一个很初级的医生。这部剧的班味很浓，剧情设计的不那么合理，比如女主的工作机会、男主的存在感、反派角色的建立。

刚开始看，朋友说后面比较好看。



## 碎碎念

* 看到一篇公众号文章，明知道是文字游戏，但是没有找出来，有些挫败。
* 我要买一个板子，可以同时支持冰箱贴、胸针和书签
* 当看到真的有人把 LLM 作为基础设施来用的时候，这种感觉很奇怪，会不会太早了？
* 一个错误，叠加另一个错误，最终可以正常工作，且工作了很多年，也是幸运。
* 虽然根据之前阅读的一些文章，DuckDB 在处理 CSV 的时候兼容性很好，但是当我真的需要处理的时候，第一想法还是用 pandas，毕竟 AI 写 Python 实在是太快了。
* 最近接连有同事要出差，我已经不记得自己上一次出差是什么时候了。
* 看病是一个很消耗精力的事情，挂号，预约检查，复诊，预约检查，这中间的间隔非常长
* 之后还是应该早上来健身房跑步，没有人跟你逼逼