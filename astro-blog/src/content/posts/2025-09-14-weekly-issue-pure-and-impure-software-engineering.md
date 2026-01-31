---
title: Weekly Issue-Pure and impure software engineering
date: "2025-09-14T00:00:00.000Z"
slug: "Weekly-Issue-Pure-and-impure-software-engineering"
tags:
  - Weekly
description:
---

## 文章

### 技术

[ToB SaaS 服务之殇 - Jiajun的技术笔记](https://jiajunhuang.com/articles/2025_09_07-to_b_saas.md.html)

> 1. 多云，云之间的复杂度，又无法全部屏蔽掉，因此配置项更多
> 2. 很多客户不想用公有云，要赚钱，还得提供一套私有云部署，如果是私有云，debug 那叫一个难
> 3. 三大云厂商，产品大体相似，但又各种不同，要会的知识太多，细节太多；如果还要接入更小的云，那就更复杂了

为啥 [SaaS](/mentions/saas) 还要让客户感知是哪个云服务商？感觉可以把 `SaaS` 去掉。

---

[We all dodged a bullet - Xe Iaso](https://xeiaso.net/notes/2025/we-dodged-a-bullet/)

[npm debug and chalk packages compromised](https://www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised)

[DuckDB npm Account Compromised in Continuing Supply Chain At...](https://socket.dev/blog/duckdb-npm-account-compromised-in-continuing-supply-chain-attack)

这两天针对 [npm](/mentions/npm) 的钓鱼攻击影响范围确实太大了。依赖（的依赖）管理问题真是老大难。

---

[Issue #12786: Copr outage - build queue slow down (or halt) - fedora-infrastructure - Pagure.io](https://pagure.io/fedora-infrastructure/issue/12786)

尝试更新我维护的 [EasyTier](/mentions/easytier) Fedora RPM，发现 COPR 构建很慢，看到了已经存在的 Ticket ，发现这个项目的监控系统还在使用 Nagios，已经不记得上一次看到这个名词是什么时候了： "The copr-backend is running out of storage. I'm not sure why we didn't receive an early Nagios alert, or if we did, I missed it."

---

[A framework for pricing AI products](https://stripe.com/blog/a-framework-for-pricing-ai-products)

> 在 Stripe 最近的一项调查中，63% 的科技行业受访者表示他们目前提供人工智能产品或应用程序。也许更引人注目的是，31% 的非科技行业受访者也说了同样的话，另有 45% 的人计划在不久的将来提供人工智能产品。

关于当前各个产品中 AI 功能的定价讨论，一直觉得这方面波动很大，尤其是随着模型能力的变化以及需求场景的变化，无论是按量计费还是套餐制都会面临调整计价时候的用户吐槽。

如何给 （AI）产品定价：
1. 我的产品给客户带来了什么样的价值，是否可以以涵盖增量成本的方式收取费用？
2. 如何将此费用指标转换为鼓励客户采用和增长的定价模型，同时提供可预测的收入？
3. 定价模型会产生哪些额外的风险，如何控制风险？

目前主要有 3 类费用指标：
- 基于实际消费（API 调用、Token 消耗）：这种方式与底层基础设施成本直接相关，好处是成本是可预测的，坏处是很难与客户的具体商业价值联系起来。通常被模型公司使用。
- 基于工作流（每个已完成的任务）：该指标引入了成本可变性，但是与提供价值挂钩，公司对完成一系列任务收取固定价格，比如预定会议、分析 Excel 等具有明显节省时间的价值。客户很容易了解他们购买的是什么。
- 基于结构（每个成功的结果）：与实际业务结果最密切相关，只有当真正解决问题时收费。也是对交付的产品最有信息的一种计费模式？

---


[Keeping Secrets Out of Logs - allan.reyes.sh](https://allan.reyes.sh/posts/keeping-secrets-out-of-logs/)

如何避免敏感数据泄露到日志中，作者总结了集中常见的原因，如直接日志记录、异常处理、配置变更、嵌入到通用格式等。给出了多种解决方案，最终一种是“人”，但是感觉“人”是最不可靠的了。

可以试试：  [GitHub - mongodb/kingfisher: Kingfisher is a blazingly fast tool for secret detection and live validation across files, Git repos, S3, Docker images, Jira, Slack, and Confluence](https://github.com/mongodb/kingfisher)

---

[Pure and impure software engineering](https://www.seangoedecke.com/pure-and-impure-engineering/)

> Open-source work is often like this: some engineer wants to write the best HTTP requests library, or their ideal game engine.    
> The second kind - impure engineering - is interested in solving a real-world problem as efficiently as possible. Paid tech company work is often like this: engineers are asked to deliver some project or feature as well as they can do it by the deadline.

> Of course, any engineer can do both pure and impure work. But in my experience, engineers who are mainly interested in pure work do impure work badly: they struggle to compromise, they panic under deadlines, they aren’t as good as holding unwieldy codebases in their head, and so on. [As I keep saying](https://www.seangoedecke.com/how-to-ship), it takes a lot of skill to ship in a large tech company.     

> Likewise, engineers who are mainly interested in impure work (like me!) struggle with pure work: they’re too eager to settle for a working hacky solution, and they often don’t have the technical expertise to see the right path forward.

> With this in mind, I can see why pure engineers are baffled by the hype around AI. It must seem so strange: every time they try to use LLMs, they’re completely unhelpful. But I think this reflects a certain narrowness of vision.

---

[KDE launches its own distribution (again) [LWN.net]](https://lwn.net/SubscriberLink/1037166/caa6979c16a99c9e/)

> The root filesystem (/) is a read/write Btrfs volume, while /usr is a read-only [Enhanced Read-Only File System](https://docs.kernel.org/filesystems/erofs.html) (EROFS) volume backed by a single file. The system is updated atomically by swapping out the EROFS volume; currently KDE Linux caches up to five of the files to allow users to roll back to previous versions if the most recent updates are broken.

这周还看了一个 openSUSE 的介绍： [openSUSE Conference 2025 - Atomic OS Updates via OCI Images - YouTube](https://www.youtube.com/watch?v=u_9BoxsHQI8&t) ，大家好像都喜欢利用 Btrfs 的 subvolume 功能来实现类似需求。

---

[SSH session 到底会加载哪些环境变量？ | My Site](https://spencercjh.me/blog/ssh-session-env/)

[Shell startup scripts — flowblok’s blog](https://blog.flowblok.id.au/2013-02/shell-startup-scripts.html)

login/interactive/non-login/non-interactive 各个组合下，环境配置加载流程。

---




### 生活

[Chat Control Must Be Stopped, Act Now! - Privacy Guides](https://www.privacyguides.org/articles/2025/09/08/chat-control-must-be-stopped/)

我以为欧盟的 Chat Control 事情已经结束了，被否决了，没想到又重来了，9 月 12 日会最终确认是否通过。欧盟走火入魔了，这法案都违反他们自己的 GDPR 。

今天是 9 月 13 日，法案没有通过。

---

[Words are not violence](https://world.hey.com/dhh/words-are-not-violence-c751f14f)

> You could agree or not. Counter or be quiet. But the earnest exploration of the topics in a live exchange with another human is as fundamental to our civilization as Socrates himself.You could agree or not. Counter or be quiet. But the earnest exploration of the topics in a live exchange with another human is as fundamental to our civilization as Socrates himself.

> Don't give up, don't give in. Keep debating.

---

[信息爆炸时代，付费信息才是最好的过滤器 · 唐巧的博客](https://blog.devtang.com/2025/08/31/pay-your-information/)

> 最近几年，我观察到一个现象：几乎所有的免费财经内容，最终都指向商业变现。


付费当然是一种解决方式，我会用另一种解决方式，看一些“活人“的分享。“活人感”这个词我虽然不喜欢（没理想编辑部的编辑们很喜欢用这些词，我都是从他们那学来的），但是又找不到其他合适的词来形容了，我很看重“活人感”强烈的人，真实的分享，而不是为了“起号”。

突然想到了脱口秀综艺现在的状态，近年来，观察式喜剧不受欢迎了，至少相比几年前，大家更喜欢的是像“嘻哈”那样的，分享自己感受的，当你在舞台上去讲“诶，今天你有没有发现”就是不如“你骂我，老娘就是要弄死你”受欢迎。

---

[Some tips to travel in Shanghai // Shell's Home](https://blog.shell909090.org/blog/archives/2897/)

Shell Xu 写的上海旅游小贴士。原来现在所有的酒店都允许接待外国人了，只是需要填写额外的文件。如果和朋友住在一起，需要去当地的公安局登记。
国际驾照不允许在中国开车，需要领取临时驾照。

---

[清迈：一座有些矛盾的城市 | Joe 的折腾日记](https://houjoe.me/posts/chiang-mai-contradictory-city/)

> - 整个城市围绕清迈古城分布，想去什么地方，基本就是以古城为参照物，不过，虽说是古城，却不是刻板印象里的仿古风，最多算是城墙片段围起来的区域，古城内外差别不算大；   
> 唯一要纠结的安全就剩过马路了，对于初来乍到的游客来说，这是个不小的心理挑战，因为红绿灯不多，又是飞快的摩托车大军。

> 当我不知以什么角度向父母介绍这座城时，偶然看了邓丽君的故事，这是一个悲伤的往事，1995 年，因哮喘病突发，抢救不及时，她在这个城市病逝，这是妈妈最爱的歌手了，就这样，这个城市多了一个锚定物，突然与远处的人产生了关联。

[清迈](/posts/清迈)，想去。

---

[漫步台湾（上）：历史在城，烟火在人 - Simon's Blog](https://song.al/taiwan1)

[漫步台湾（下）：古意在南，云雾在山 - Simon's Blog](https://song.al/taiwan2)

想去 +1。

---

### 书影播客

《不开玩笑-209. 想赢就得拼，聊聊胜负心》，嘉宾有：贤鱼、小块、吴鼎、赵丽娜，这期嘉宾随便一个都可以撑起一期闲聊播客了，多了之后，就有点吵闹了。

《岛必叨-013.你以为人家真喜欢啊？展示一下自以为浪漫的行为和礼物》，这个播客确实很邪性，是喜剧闲聊类播客中少有的制作粗糙的了，感觉台上有两个《正经叭叭》的大盆在聊天，话题满天飞，主持人拉不回来。

《谐星聊天会-vol.82 怎么说呢？也可以这么说，还是这么说吧！》，这期挺有趣的，不在播客本身，而是在评论区。有一个女生分享了自己在健身房加了一个男生的微信，然后被自己男朋友看到了，说“不要让自己的「可得性」太高”，这个词肯定是不对的，评论区争论的点是这个女生自己是否有什么问题，说如果性别互换之后，会发生什么，吵的还挺厉害的。

《正经叭叭-vol.214 精致不昂贵，有半价电费》，这期很逗，嘉宾有 Max 哈正经，两口子的生活分享有意思。同时几个出了名的不精致的人在上海聊精致，实在是话题稀缺了。


## 碎碎念

* 国庆我能去哪呢
* Yaak 真不错。
* 有个同事问我 Celery Broker 的事情，我：建议不要用 Celery。
* 感谢爷商 $NTNX ，今天加鸡腿。
* AI 给的回答啊，要带着批判的眼光看。
* 之前中午吃饭和同事聊过几次，大家都无法明确什么是“预制菜”。