---
title: Weekly Issue-伪连接的时代
date: "2025-10-26T00:00:00.000Z"
slug: "Weekly-Issue-伪连接的时代"
tags:
  - Weekly
description:
---

## 文章

### 技术
[I Tried the Agentic Browsers - laike9m's blog](https://laike9m.com/blog/agentic-browser,169/)

> **Combine agents with old-school "record/replay" functionalities**, allowing users to create their own workflows more easily.

省流：截止到 2025 年 10 月，AI 浏览器都是垃圾。其实很多时候无法完成端到端任务，是在我当前的预期的，用户提供一些操作示范，然后 AI 基于示范操作进行批量化执行，感觉是一个不错的折中方案。

这篇文章刚好是 OpenAI Atlas 发布之前，不知道 Atlas 的表现怎么样。

---

[AI 救不了软件工程，也不需要救](https://archive.is/hviU1)

> **价值黑洞：你永远无法向老板证明「很有用」**    
> 付钱的老板们，不懂什么代码覆盖率、圈复杂度，他们只关心**收入、利润、市场份额**。你跟他说「我们提升了工程文化」，他只会问「所以，研发成本降低了多少？」。    
> 多数 AI4SE 工具，卖的都是锦上添花甚至有害的「保健品」**，而不是救命的「**止痛药」。在经济下行、企业降本增效的今天，「保健品」生意有多难做，不言而喻。    

> 例外当然有，比如 Cursor。它聪明就聪明在，彻底放弃了改造「工程」，只服务于**工程师个人** —— 帮我代码写快点，让我有更多时间摸鱼。它的价值立竿见影，完美绕开了所有管理和价值证明的深坑。

---

[x.com/m\_franceschetti/status/1980419272766583262](https://x.com/m_franceschetti/status/1980419272766583262)    
[x.com/mitsuhiko/status/1980768738837426643](https://x.com/mitsuhiko/status/1980768738837426643)

> The AWS outage has impacted some of our users since last night, disrupting their sleep. That is not the experience we want to provide and I want to apologize for it.

> What’s worse is they the failure state of the bed is not “turn off” but random other stuff. My eightsleep in both downtimes was heating to a setting that was never configured.

[AWS](/mentions/aws) 故障影响到的 Eight Sleep 床垫，无法正常工作，进而很多人睡不好？看了下他们的官网，2014 年成立的，主打的产品功能就是智能调节、健康数据监控，找名人背书，感觉目标用户挺精准的，对自身数据痴迷的用户。这个床垫每年要收 200 美元的订阅费，真赛博啊。感觉不如小米床垫 199 呢。

---

[Chris's Wiki :: blog/linux/NoKernelUpdatesWithoutReboot](https://utcc.utoronto.ca/~cks/space/blog/linux/NoKernelUpdatesWithoutReboot)

> We don't update kernels without immediately rebooting the machine

排查问题的第一步应该是确认软件版本。类似的还有更新了 binary 但是不重启服务，都会多少给后面的问题调查带来干扰。

---


[Docker release? · Issue #21647 · minio/minio](https://github.com/minio/minio/issues/21647#issuecomment-3418675115)

[Minio](/mentions/minio) 不提供 container image ，之前已经发布的版本如果存在安全问题，需要自行构建使用了。   
我看了下笔记中关于 [Minio](/mentions/minio) 的 link，发现几乎没有正面的消息，不是撤销了某个公司的许可证，就是去掉了社区功能。

---

[Fixing UUIDv7 (for database use-cases) - Marc's Blog](https://brooker.co.za/blog/2025/10/22/uuidv7.html)

针对 [UUID](/mentions/uuid) v 7 的一些问题的可能改进方式。我现在是都用 v 7 ，一把梭。

---

[Magpie 和 「AI 贼船」- 再谈 vibe coding，当代码变得廉价时... | OneV's Den](https://onevcat.com/2025/10/magpie-and-ai-ship/)

> 就算是 “随心所欲” 的独立开发者，在 AI 时代，最好也多多 “书写”（当然实际上肯定是 AI 代笔）人类和 AI 都能参考的程序设计文档。**未来的 AI 和未来的你，应该都会感激这个当初的决定。**

> 在 AI 时代，程序员的角色正在从 “代码编写者” 转变为 “代码验证者” 和 “需求定义者”。我们需要能够快速判断 AI 生成的代码是否满足需求，是否安全可靠，是否易于维护。这种验证能力，新时代里会比单纯的编码能力更加重要。而这正是当下的软件开发者相较其他直接所掌握的核心优势：我们理解 AI 的运作方式和我们自己产品的运作方式，这种验证天然是开发者的任务。

我之前如果长时间盯着一段代码，通常是在想怎么改，现在通常是在看 AI 生成的逻辑对不对。

---


[Summary of the Amazon DynamoDB Service Disruption in Northern Virginia (US-EAST-1) Region](https://aws.amazon.com/cn/message/101925/)

> The root cause of this issue was a latent race condition in the DynamoDB DNS management system that resulted in an incorrect empty DNS record for the service’s regional endpoint (**dynamodb. Us-east-1. Amazonaws. Com**) that the automation failed to repair.

> When this issue occurred at 11:48 PM PDT,....
> By 12:38 AM on October 20, our engineers had identified DynamoDB’s DNS state as the source of the outage.

> At this point, DWFM had entered a state of congestive collapse and was unable to make forward progress in recovering droplet leases. Since this situation had no established operational recovery procedure, engineers took care in attempting to resolve the issue with DWFM without causing further issues.

11:48 问题触发，12:38 问题定位，在没有既定操作手册的时候进行问题修复，谁的心都得多跳两下。

---

[为什么不用 gRPC-Go：VictoriaTraces 中实现 OTLP/gRPC 的幕后故事](https://jiekun.dev/posts/otlp-grpc-from-scratch/)

> 原因 1: Protoc 工具链不好用   
> 原因 2: easyproto 已经代替了 golang/protobuf   
> 邪门歪道: 用 HTTP / 2 Server 代替 gRPC Server    

针对原因 1 提到的 protoc 工具链不好用，普通用户强烈建议直接使用 [bufbuild](/mentions/bufbuild) 。用 [HTTP-2](/mentions/http-2) 来替代 gRPC Server 感觉也仅限于文章提到的这个特殊场景。

---

[Software Development Costs: Why AI Hasn’t Changed Prices - Vincent Schmalbach](https://www.vincentschmalbach.com/software-development-costs-why-ai-hasnt-changed-prices/)

AI 可以缩短很多任务耗时，同时大家的预期也在提高，原来可以 1 天做 3 件事，现在就要做 5 件。同时对于“足够好”的标准也在提高。

DeepSeek 给“Everything is Easier and Harder”这句话的翻译版本是：万物皆易亦皆难。

---

[Mistakes I see engineers making in their code reviews](https://www.seangoedecke.com/good-code-reviews/)

“Don’t just review the diff”，只看 diff 会有欺骗性，我们日常使用 Gerrit 做代码 review，在多轮 review 的时候，如果只看最近的 Patchset 的 diff，可能会遗漏掉一些整体上的偏差，尤其是在 patch 本身发生 rebase 的时候。

> This principle - that **you should bias towards approving changes** - is important enough that Google’s own [guide to code review](https://google.github.io/eng-practices/review/) begins with it, calling it ”_the_ senior principle among all of the code review guidelines” [4](https://www.seangoedecke.com/good-code-reviews/#fn-4).

这篇博客也提到了这个观点： [Why Optimistic Merging Works Better - Hintjens.com](http://hintjens.com/blog:106)

---

[The purpose of a system is what it does | Des Traynor](https://destraynor.com/writing/the-purpose-of-a-system-is-what-it-does/)

唯结果论。

---

[Are Hard Drives Getting Better? Let’s Revisit the Bathtub Curve](https://www.backblaze.com/blog/are-hard-drives-getting-better-lets-revisit-the-bathtub-curve/)

The TL;DR: Hard drives are getting better, and lasting longer.

---



### 生活

[Regulation Isn’t the European Trap — Resignation Is | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2025/10/21/eu-resigation/)

> The vibe is: “Because the system is slow, I can be slow. Because there are rules, I don’t need judgment. Because there’s risk, I don’t need initiative.” And then we all nod along and nothing moves.

> Select for agency. Choose partners who answer promptly when it’s material and who don’t confuse process with progress.

---



[伪连接的时代：我们如何在关系中失去彼此 | Cogitare](https://cogitare.pengzhaoxie.com/p/era-of-fake-connections-how-we-lose-each-other-in-relationships)


> 伪连接。这是一种看似稳定却没有真实情感交流的接触，是我们在焦虑时代中为了维持关系而发明的防御机制

> 这种现象在当代社会中如此普遍，以至于我们几乎察觉不到它的存在。我们抱怨工作、议论他人、焦虑于责任，用这些表层话题填满对话的空白。这些互动给了我们一种联结的错觉，但实际上只是在稳定关系的同时避免真正的情感暴露。

> 我们变得害怕沉默，害怕深度对话可能带来的不适，害怕暴露真实的自己后可能面临的拒绝。于是我们选择了安全的距离，在关系中保持一种礼貌的疏离。

> 我们越是避免深度交流，就越不知道如何进行深度交流。就像一块长期不使用的肌肉会萎缩，我们的情感表达能力也会在伪连接的舒适区中退化。更危险的是，伪连接会给我们一种关系良好的错觉。我们有定期的聚会，有频繁的消息往来，但这些互动的质量却在不断下降。我们可能拥有很多「朋友」，却感到深深的孤独。这种孤独更加可怕，因为它被社交活动的表象所掩盖，让我们难以识别问题的根源。

> 我们善于察言观色，善于说场面话，善于在不触及实质的前提下维持表面的和睦。这种社交能力在某些情境下是必要的，但当它渗透到所有关系中，包括最亲密的关系时，问题就出现了。

> 我尝试在自己的关系中实践这种真实性，发现最大的障碍不是别人的反应，而是我自己对暴露的恐惧。

> 说出这些话的时候，我能感觉到身体的紧张，仿佛我正在违背某种深层的禁忌。

> 数字时代的社交平台为伪连接提供了完美的温床。

> 社交媒体给了我们一种保持连接的错觉，让我们以为我们了解朋友们的生活，但这种了解是如此肤浅。我们知道他们去了哪里旅行、吃了什么美食，却不知道他们内心的挣扎和真实的困惑。

> 为什么真实的连接如此困难？

> 我认为还有一个更根本的原因：真实的连接要求我们面对自己的有限性。当我真诚地倾听另一个人，我必须承认我无法完全理解他们的经验，无法替他们解决问题，无法消除他们的痛苦。这种无力感是令人不安的。我们的文化教导我们要有用、要高效、要能解决问题，但在真实的人际连接中，这些都不是重点。重点是在场（presence），是陪伴，是愿意与他人共处于不确定和不完美之中。

> 如果我们不知道自己真正的感受和想法是什么，我们就无法分享它们。而在伪连接的习惯中，我们往往失去了与自己内在经验的联系。我们变得如此善于说那些应该说的话，以至于忘记了问自己：我真正想说什么？我真正的感受是什么？因此，通向真实连接的旅程必然也是一个向内探索的旅程。我们需要学会倾听自己，就像我们学会倾听他人一样。我们需要在独处时培养自我觉察，才能在与他人在一起时保持真实。

> 在这个充满噪音和连接的时代，我们如此容易失去彼此。我们可以和某人在同一个空间，却活在各自的世界里。我们可以每天说话，却从未真正交流。我们可以爱一个人，却从未真正看见他们。

> 我们不需要完美的关系，不需要时刻保持深度的连接。我们只需要保持对真实性的向往，保持在恰当时刻敞开的勇气。

> 这就是我们作为人的最深渴望，也是我们对抗孤独的最好武器 —— 不是更多的连接，而是更真的连接。

原谅我这里做了大规模的引用，这篇文章写的太好了，尤其是现在很多人“AI 味”很重的今天。反复读了 3 遍，希望大家都能保持对真实性的向往，保持在恰大时刻敞开的勇气。


---

### 书影播客

《渎》，子龙的单口喜剧专场，是他的第二个专场，第一个专场他已经放到了[流媒体平台](https://www.youtube.com/watch?v=agHOghdx7pE&t)。子龙是目前少数有自己专场但是没有参数线上脱口秀比赛的演员，他的口癖是“他妈的”，全场如果有录音统计的话，可能得说了几百次，也是因为这个我没有和同事推荐的原因，大家对于脏话的接受程度差异很大。这个专场讲述的是他作为一个中年人，得了腰间盘突出，在家躺了 8 个月之后的感受，感受围绕着之前玩摇滚乐的朋友们的现状做对比。专场特别像是一个东北老舅喝多了，在酒桌上和你忆往昔。想到了一个对比：和子龙相比，翟佳宁都和善了。

现场有很多脱口秀演员：何广智、陈述、毛豆、菜菜、Kid。其中子龙当着 Kid 的面聊自己对 Kid 行为的不理解，说 Kid 一定是和孙书恒搞对象了，才那么托举他（孙书恒），效果爆炸。

《首尔夏天》，食贫道充电视频。可以结合之前峰哥在韩国拍的视频一起看，或者看看这个人的 [vlog](https://space.bilibili.com/3546666542041956/lists/5960313?type=season)，拍摄的角度还是很重要的。卷生卷死，失去了什么，又得到了什么。

刚好今早看到了一条消息：
> 2023 年，上海交大招收了 3753 名博士；   
> 2024 年，上海交大招收了 3500 名博士，其中医学院就招了 700 多人   
> 2025 年，上海交大招收了 4000 名博士   
> 2026 年，招收 5000 名博士   

《二维吾码-AI 时代的知识管理：为什么 “记下来” 这个动作，无法被替代》，嘉宾是少楠（flomo 创始人），关于 AI 时代笔记相关的讨论，主播讲述自己从 flomo 迁移到 Blinko 的原因，是因为 Blinko 自带的 AI 评论功能，可以设置多个 Prompt，当自己发布一条笔记时，让 AI 来以多种角度评论，来增加自己的思考角度和深度，有点类似于之前提到的roast。尝试了下 Blinko 的 demo，发现也太卡了，不可用的状态。

少楠提到的一个点挺有趣的，大家在拍照之后，发社交媒体的照片，是否带有滤镜？发完之后真正存在手机里的照片，是否带有滤镜？他观察到大部分人前者有滤镜，后者没有。大家会倾向于对自己保留最真实的东西。


《基本无害-Ep175 霞慕尼归来，聊聊越野跑，UTMB 和观赛攻略》，
《基本无害-Ep177 UTMB 现场的海外越野跑比赛讨论（Ep175 资料片）》
毛冬讲述自己在霞慕尼参加 UTMB 的一些事情，介绍了越野跑以及 UTMB 的背景，如果对跑步没有兴趣的话，他其实是建议尝试越野跑的，其中一个因素是，越野跑在上坡的时候，大家都是走的，走的很心安，但是如果参加长距离马拉松，如果别人都在跑而你在走，你会觉得有些不舒服。

这期播客嘉宾有向付召，我只知道是一个很厉害的女子运动员。周末的时候我去世纪公园跑步，跑完之后想看看世纪公园这个上海比较出门的跑步地点，最厉害的人跑多快，在女子记录中看到了一个人的图标带有 **PRO** 字样，和其他人不一样，点进去一看，那个人就是向付召。世界真小啊。

《蜉蝣天地-大暄哥：赢家的饥饿、欲望与黑暗原力；做题家的一种人生解法》，朋友推荐的播客，主播是重轻，嘉宾我完全不了解。最开始讲解人生方法论的时候，我听的是有点害怕的，之后聊到工作职场感觉还好，嘉宾太追求极致了，“赢”对他很重要。之所以害怕，是因为我认同他的方法论，但是我做不到，我知道自己做不到，所以我听的时候，仿佛看到了一个超人在讲述这条路，令我害怕。





## 碎碎念

* 巴厘岛在南半球
* 卡巴斯基是俄罗斯的
* 同事真牛逼，2 人 2 天IDC 300+服务器搬家，搞完了
* 感觉最近 Folo 的抓取频率提高了不少。
* 开发机日常占用最多最多 CPU 的居然是 tailscaled。
* 不同人对 Reliability 的理解偏差也太大了。
* 一些人为了博关注也是拼了，老手段就是有用啊
* 往常都是 4 点钟醒了，然后玩会手机，等到 5 点出门跑步，今天 4 点直接出门跑步，感觉也不错，毕竟现在天短了，4 点和 5 点没啥差别。
* 每一步操作耗时久，重试成本高，用户心智负担重，用户操作更小心，慢上加慢。
* 早上浦东滨江跑步看到了颜如晶，几个人在训练。
* 用上了 Raycast Windows 版本，快捷键保持一致还是挺重要的。
* Tailscale 可以直接在控制台升级 Machine client 的版本，这里的权限控制总感觉会出问题呢？
* 世纪公园受欢迎是有道理的，跑起来确实舒服，5km PB 27m。