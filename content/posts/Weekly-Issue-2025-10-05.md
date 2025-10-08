---
title: Weekly Issue-他们可能只是心情不好
date: 2025-10-05
tags:
- Weekly
description:
---


## 文章

### 技术

[Boring is good](https://jenson.org/boring/)

>  [A recent MIT report](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/) shows that 95% of companies implementing this technology have yet to see a positive outcome.

> LMs are also likely to significantly change as the technology and market matures. They will be used in much smaller, more focused, and, I’m afraid to say it, significantly more boring ways. This will only accelerate as people get tired of “hallucinations” and discover how powerful LLMs are when they’re kept focused on these smaller, more predictable language processing goals.

> Whenever there is hype, we shuffled into the easy path, forcing the tech into the product without understanding its weaknesses. We are more worried about being left behind than actually doing something of value.

We’re here to solve problems, not look cool..

---

[90% | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2025/9/29/90-percent/)

> The tools are powerful, but they don’t absolve you of responsibility.

文中提到了一些使用 LLM 生成代码的优势，其中大部分都和“试错”有关，LLM 可以让人快速试错，可以节省很多时间：
- Research + code, instead of research and code later
- Trying out things
- Constant refactoring
- Infrastructure
- Adopting new patterns
- SQL quality

---

[TiDB 源码阅读（一）：服务监听、请求处理流程概览 - Jiajun的技术笔记](https://jiajunhuang.com/articles/2025_10_01-tidb_source_code.md.html)

[TiDB 源码阅读（二）：MySQL协议概览 - Jiajun的技术笔记](https://jiajunhuang.com/articles/2025_10_02-tidb_source_code_mysql_protocol.md.html)

[TiDB 源码阅读（三）：插入数据 - Jiajun的技术笔记](https://jiajunhuang.com/articles/2025_10_03-tidb_source_code_insert.md.html)

[TiDB 源码阅读（四）：AST、逻辑计划、物理计划 - Jiajun的技术笔记](https://jiajunhuang.com/articles/2025_10_04-tidb_source_code_ast_and_plan.md.html)


好诶，久违的 jiajun 读代码系列又更新了。

---

[Cognition | Rebuilding Devin for Claude Sonnet 4.5: Lessons and Challenges](https://cognition.ai/blog/devin-sonnet-4-5-lessons-and-challenges)

昨天高强度的使用 Claude Sonnet 4.5 一天，感受与这篇文章中提到的完全一致：
- 更多次数的总结上下文；
- 生成很多的文档，几乎每个小任务都会生成一份文档，这些文档大部分内容都是相同的，这点在重构场景下有点烦人；
	- > In some cases, somewhat humorously, we've seen the agent spend more tokens writing summaries than actually solving the problem.
- 更多的测试
	- > In another case, when trying to fix a seemingly innocent error related to two local servers trying to run on the same port, the model ended up using this behavior to create an overly complicated custom script instead of addressing the root cause issue (terminating the process).

---

[What is "good taste" in software engineering?](https://www.seangoedecke.com/taste/)

坏的品味：在项目上下文不合适地坚持个人偏好，把“最佳实践”当作放之四海皆准的理由，缺乏灵活性，导致项目不匹配或维护成本上升。

---

[Development gets better with Age | All Things Distributed](https://www.allthingsdistributed.com/2025/10/better-with-age.html)

> Then you do exactly what you’ve always done. Have an in-depth conversation with your customer, listen, dive deep into their challenges, suggest architectures, migrations, and tools. And sometimes, the solution will be generative AI.

---

[G드라이브 전소…74개기관·19만 공무원 업무자료 858TB 소실(종합2보)](https://www.yna.co.kr/view/AKR20251001127752530)

>  据悉，国家信息资源院发生火灾，中央行政机关（部委）公务数据存储设施 “G Drive” 被彻底烧毁，74 个机关 19.1 万名国家公务员个人存储的公务数据全部丢失。
  
> 行政安全部于 2018 年制定了《G 盘使用指南》，规定 “所有产生和管理的工作数据都不应存储在 PC 上，而应存储在 G 盘上”。   
> 据报道，中央政府各部门对 G Drive 的使用情况差异很大。

> 不过，他补充说，由于 G Drive 是一个大容量、低性能的存储，因此外部备份很困难。

震惊，印象中韩国的网速在全世界排名靠前，以为他们的 IT 基建挺好的，这事故感觉在历史影响范围内都可以排的上名了。也许事后复盘，发现大部分数据没什么用，影响比想象中小很多。

---

[3 Critical TTL Patterns for In-Memory Caching](https://samuelberthe.substack.com/p/3-critical-ttl-patterns-for-in-memory)

感觉在大多数场景下，引入 Jitter 都没什么坏处。

---


[对国内地图坐标系统的一些观察 - 陪她去流浪](https://blog.twofei.com/1967/)

>1. 所有的 GPS 芯片（便宜到几块钱）（含手机相机相片）报告的地理位置都是原始准确的 GPS 坐标，“保密”/“安全” 了个啥？对着你的建筑拍一张发过去都能得到精确位置。   
> 2. 从卫星上还是能看到所有建筑啊，转换坐标又不能移动建筑。

莫名的想到了英剧《真相捕捉》，这里不剧透，第一季豆瓣评分 8.9，第二季豆瓣评分 9.3，是悬疑类英剧榜的第三名，推荐感兴趣的朋友看看，和这篇博客的内容以及疑问多少有点关系。

---





### 生活

[背刺者艾玛](https://archive.is/6aYjw)

> 一个人是个怎样的人，这才是最重要的。毕竟我们生活在人群中，我们和他人打交道的时候，并不能和性格打交道，和观点打交道，和价值观打交道，和政治立场打交道，我们是个一个个具体的人打交道，通过一件件具体的事打交道。一个具体的人如何具体对你，这是你得到支持和遭遇背刺之间的分别。

---

[PUBLIC I ran out of money a year ago, spent the last of my savings on a prostitute in Hong Kong, and became a commie.](https://docs.google.com/document/u/0/d/1Am8bYA1aoXuSGFg7w7NjlHXFZiSAEt_oAVITPYdNRGo/mobilebasic?tab=t.0)

> 然而，当我经济富裕时，我从未对世界感到如此深切的感激。   
> 我的许多朋友，无论多么成功，无论他们做过多少感恩的誓言，都感觉这个世界对他们漠不关心，甚至充满敌意，一旦他们不再有用，就会被抛弃。事实上，他们越成功，就越怀疑周围的人，这种感觉就越糟糕。   
> 如果说今年我至少学到了一件事，那就是即使我对这个世界一无是处，它也不会抛弃我。我唯一的愿望就是让每个人，无论他们是谁，无论身在何处，都能明白这一点。   

---

[Things I Believe | Lee Robinson](https://leerob.com/beliefs)

> They might just be having a bad day

**他们可能只是心情不好。** ，这句话突然击中了我，对啊，可能只是心情不好。

---

[金融科技十年血色史：千亿坏账、万企覆灭、1.2 万人入狱](https://archive.is/DU8Fm)

> 监管竞争导致 “底线比拼”，谁管得松，谁抢到的企业就多。
> 在地方的放水、加持、主推下，民企崛起了，属于民间金融的一个黄金大门，轰然洞开。

> 中央定调，但最终执行，还是需要各地金融办配合。
> 而很多早已经和金融平台牵手的地方政府，为保 GDP 和税收，依然纵容平台 “带病运营”。
> 《办法》要求银行存管，但地方推动不力，仅 6% 平台完成存管（2016 年底仅 98 家），某省金融办甚至协调本地城商行降低存管门槛。
> 制度性妥协之下，没有真正的监管者，只有利益的置换者。

> 这场剿灭背后，有太多真实且荒诞的故事和细节。
> 发达地区的，一边忙着收拾自己的桃园，一边提防着外地的来摘桃。
> 为了防止别人介入，他们就会提前立案，这里就出现了另一个词： **保护性抓捕**。

> 但是，他们的存活，也不是偶然，他们一直唯监管 “马首是瞻”，并懂得顺势而为，调转船头。

---

### 书影播客

《芯片制造：光刻巨头 ASML 传奇之路》，ASML 的故事，看了 1/3，这家公司的历史比我想象中还要久远。

《喜人奇妙夜 2》，能够感受到演员的累，那种使出浑身解数来搞笑。目前 4 集，和上一季差不多的是《旧警察故事》，我比较喜欢的作品是：《空城计》、《开学第一天》、《忘不了》。

其中争议比较大的是《技能五子棋》，这个作品我看了好几遍，我一直在用一个“正常人”的视角来看，直到我在播客中听到王继续说自己的经历：
> 我一只觉得自己是搞抽象，但是当我到了《喜人》节目，那里没有人，都不是没有正常人，他们太怪了，我作为一直演怪人的人，在哪里我只能演直人。

《二的三次方-vol:109 拜托，你怎么这么爱演！》，这期播客录制的时候，王继续还没有火，不知道喜人播完之后，他作为吐槽咖会不会受到更多的喜爱。另外刘洪伟讲述的向佐的故事，还挺有趣的，让我对这个人的了解多了一些，虽然抽象，但是是自己知道自己的抽象，也可以接受调侃。

《疯投圈-123. 掘金东南亚的机遇与挑战》，如果之前关注过李自然的视频，那么这期可以略过了，很多内容李自然之前已经讲过了，甚至是实践过，所以这期播客的内容并没有太多新意。

《42 章经-Mercor 高速增长的秘诀与其中的聪明人｜对谈 Mercor 首位中国员工虞快》，有趣，如何从一家 AI 招聘平台，转型为数据标注公司的。几个创始人都是大学辍学的，团队处于高速增长阶段，在绝对的增长面前，其他的事情都可以被“忽略”，期待几年之后这家公司会是什么状态。



## 碎碎念

* Wirth's law：软件变慢的速度比硬件变快的速度更快。
* 给公司项目添加了 AGENTS.md
* Google 家的产品，总给我一种做出来之后更新速度就明显变慢的感觉，他们是怎么做出 Workspace 的。。
* 突然感觉市面上强调Durable execution 的框架好像很多了。
* 看了一些 sora2 生成视频，感觉质量是参次不齐的，但是传播效果很好，是因为“创作者”在视频中的影响？
* 有没有那种 sandbox，把 git repo 作为 overlay 的lowerdir 来，然后定期 inotify upperdir 保留 diff 结果的，感觉比改造 git 要来的快。
* 中国人口中位数是 38 岁。
* 拼多多买机票的界面确实很朴实。
* 在父母的眼里，人活着就是为了生孩子。
* 原来有些小众货币，在一些二三线城市是换不到的。
* 如果一个人一直将自己放在道德的至高点，远离他。
* 水王的作品《新默剧》挺有趣的，大家对于“抽象”的接受程度是完全不同的。
* 2025年的 1000km，比计划迟了一个月。