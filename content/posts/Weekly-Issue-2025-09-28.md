---
title: Weekly Issue-笑果创作清单
date: 2025-09-28
tags:
- Weekly
description:
---


## 文章

### 技术

[有机的 LLM 人机交互: 不只是对话框 | Yanli 盐粒](https://blog.yanli.one/pycon-china-2025-llm-interaction-zh)

在日常和 LLM 交互中，感觉对话框是效率不高的，如果我在一个私密的环境，并且有一个比较好用的语音输入法，我可能会像当前老罗的 TNT 一样去使用。

---

[How I Vibe Coding? (Sept 2025 Edition)](https://xuanwo.io/2025/06-how-i-vibe-coding-sept-2025-edition/)

> Subscription is the future. Code Agent is designed to be token-intensive. Just subscribe to the best model you want instead of paying per request or token. It makes no sense anymore. I especially can’t understand why anyone pays over $200, even $1000, for Cursor or APIs. By simply switching to subscription-based services, you achieve massive cost savings.

订阅制确实让更多人上手成本可控，更愿意尝试，甚至 GLM 也凭借相对较低的价格（2 个月 Cursor 的价格可以买一年的订阅服务）吸引了很多人。但是很难说订阅制是 future，更像是当前阶段的特定能力下的选择。   
最开始模型不行的时候，会按照 token 直接计费，后面模型能力较强，token 消耗可控，推行订阅制，如果随着模型的能力更强，可以直接完成端到端任务，是否会回到按照完成特定任务收费，类似于外包？

---

[Cerebras - new datacenter in Oklahoma City](https://www.cerebras.ai/blog/okc)

> For agentic, real-time reasoning and instant code-generation workloads, our systems use about one-third the power of the fastest GPUs.

> We designed our hardware for direct-to-chip water cooling from day one.

哇哦。

---
[Zed's Pricing Has Changed: LLM Usage Is Now Token-Based — Zed's Blog](https://zed.dev/blog/pricing-change-llm-usage-is-now-token-based)

[[Zed]] 调整了计费模式，原因也很简单：**Current pricing is too expensive for Zed**，**Prompt-based pricing is decoupled from user value**。

---

[High-growth companies stand out with flexible pricing](https://stripe.com/blog/high-growth-companies-stand-out-with-flexible-pricing)

> 与低增长同行相比，增长最快的公司已经在三个重要方面展现出更强的灵活性：
> 1. 他们更频繁地改变定价模式。
> 2. 他们的模型更有可能包括基于使用情况的费用，他们会随着时间的推移进行调整以微调他们的定价。
> 3. 在考虑未来的价格变化时，他们对更广泛的选择持开放态度。

> 增长最快的公司在过去两年内调整价格三次或三次以上的可能性，是低增长公司的三倍。

有趣，可以和上面的 [[Zed]] 调整配合来看。作为用户来说，我是很不喜欢频繁的调整定价的行为。

---

[Write the damn code](https://antonz.org/write-code/)

> If, given the prompt, AI does the job perfectly on first or second iteration — fine. Otherwise, stop refining the prompt. Go write some code, then get back to the AI. You'll get much better results.

> Get your hands dirty. Write the code. It's what you are good at.

> You are a software engineer. Don't become a prompt refiner.

---
[Ubuntu 25.10's Move To Rust Coreutils Is Causing Major Breakage For Some Executables](https://www.phoronix.com/news/Ubuntu-25.10-Coreutils-Makeself)

> Sure enough, once replacing Rust Coreutils with GNU Coreutils on Ubuntu 25.10, the same exact files now ran successfully without MD5 errors. Looks like some subtle differences between md5sum from GNU Coreutils and Rust Coreutils is breaking files from at least Makeself.

每次看到 Ubuntu 25.10 关于 Coreutils 替换的新闻，都能让人笑出声。反过来，如果 25.10 成功发布，并且随着迭代可以快速让 Rust Coreutils 进入稳定期。

---

[Onward | Domenic Denicola](https://domenic.me/retirement/)

> I’m retired! I no longer need to work for money, and I’m going to take on the responsibility of figuring out what that looks like.

> Life has so much to offer, and I’m excited to live it more fully. I’ll be raising a puppy, seriously increasing my Japanese study time, and enjoying my backlog of video games, TV series, and novels. I’ll build small apps for myself to scratch an itch or learn a technology, and then decide whether to try polishing and publishing them.   

> More than anything, I plan to learn a lot: I want to deep-dive into the philosophy of [computation](https://plato.stanford.edu/entries/computation-physicalsystems/), [personal identity](https://plato.stanford.edu/entries/identity-personal/), and [consciousness](https://plato.stanford.edu/entries/consciousness/); I want to resume my studies of theoretical physics in general, and quantum gravity in particular; I want to learn [Lean](https://lean-lang.org/) and get involved in modern, often AI-assisted attempts to formalize mathematics. I’ll make new friends, start new hobbies, and travel to new places. I’m so excited.

---

[How Claude Code is built - by Gergely Orosz](https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built)

[回顾 Claude Code 的成功：天时地利人和+大道至简 - XX's Blog](https://xxchan.me/ai/2025/09/27/cc-reflection.html)

> 对于足够有产品 sense 和技术 sense，爱玩，**且有时间自己探索**，且主要精力花在**探索模型能力**，且**用模型不需要花钱**，且模型 agent 能力到了可用的时机，且有人一直用一直给反馈…… 的情况下，造出 Claude Code 仿佛是显然的。

---

### 生活

[最近想赞美闲暇 - Stay Out Space](https://www.wuyi.space/2024/08/11/%E6%9C%80%E8%BF%91%E6%83%B3%E8%B5%9E%E7%BE%8E%E9%97%B2%E6%9A%87/)

> 也许你会问：“你为什么不自己多问问你爸，还要从别人写的书里去试图想象这种生活？” 我也想过这个问题。   

> 这大概是一种刻意的回避，在相当长的一段时间里，我无法跟父母构建起极为亲密的关系，我对于 “辛劳但我无法改变、不公但我无法左右” 的事物常有无力的感受，因此靠近就是一种无形的暴力，会伤害到我。从心理健康的角度来看，我需要保持安全的距离。说白了，就是我玻璃心。是啊，就是这样。

---

[我们可以想要一些不同的东西 - Stay Out Space](https://www.wuyi.space/2025/08/23/%E6%88%91%E4%BB%AC%E5%8F%AF%E4%BB%A5%E6%83%B3%E8%A6%81%E4%B8%80%E4%BA%9B%E4%B8%8D%E5%90%8C%E7%9A%84%E4%B8%9C%E8%A5%BF/)

> **无目的地学习，无目的地思考，并努力为此创造尽可能多的空间，这不正是我们作为人类唯一的余地、唯一真正的自由吗？”**

---

[PyCome - Frost's Blog](https://frostming.com/2025/pycon/)

> 我说难道不是去咖啡馆集体 Coding 吗？我记得和程序员聚会都是这流程，就像过年回老家的固定节目是和同学连坐打 Dota 一样。
> yihong 表示，连坐？什么连坐？卧槽咱可以去连坐！

想到了某一年的团建，当时公司项目太无聊，于是几个人一起去了网鱼网咖打 LOL，由于大家账号都分散在各个区，现创建账号走新手教程，最后以连输几局结束。

---

[派派成长日记 #5 - 成为掌管睡眠的神（90-120天）](https://changchen.me/blog/20250924/paipai_four_months/)

> 没有最好的育儿方式，只有最合适的：每个孩子都是独一无二的，具备极大的差异性。有的儿童困了需要抱一会，哭闹或玩一阵子，有的孩子可能很快入睡，甚至同一个婴儿也一直在变化，我们不能强求他们始终处于一种睡眠状态。
> 当宝宝在你怀里迷迷糊糊，你便将他放到婴儿床上拍睡，可冰冷的婴儿床让他爆哭，抱起后他一边抽泣一边用小小的手紧紧的抓着你的衣领，不必强求，遵从内心选择最适合你们的相处模式即可。

---
### 书影播客

终于把之前看完的《单口喜剧进阶指南》的笔记补全了，这里整理一下“笑果”创作清单：

- 创作单口喜剧必须明确表达目的，即“我究竟想说什么”。
- 要好笑，但是不要去追求好笑，好笑是结果，不是目的。
- 态度能激发表达欲，所以让你产生态度的事才能成为创作素材。
- 所有态度都能成为创作素材，利用不常见的态度来创作更容易。
- 想找到“不常见”，既要向外观察世界，也要向内观察自己。
- 为了更好地利用素材，我们应该在态度的基础上思考，直到得出明确的观点。
- 在所有的段子中，演员内心的观点是十分重要的，即使它们没有被直接体现在段子里。
- 可以用“解释”和“解决”的思维方式来寻找衍生观点。
- 我们提供的并非操作方法，而是检修工具。
- 好笑是一种主观的感受，而喜剧是阐述人类生活真相的艺术。
- 喜剧的公式:喜剧讲的是一个普通人，在不具备获胜必备的技能和工具的情况下，与无法克服的困难做斗争，但从不放弃希望。
- 在单口喜剧中，你就是那个“普通人”，，可以有别的普通人，但只有你是必不可少的。
- “胜利”指的是在人物看来积极的或能使他实现目的的任何事。
- 人物的每一个行为都应该是为了获胜，而不是逗笑观众。
- 在获胜过程中能对人物产生阻碍的，应该是他的特质和弱点。
- 如果段子里有很多人物，那每一个人物都应该有自己的胜利，有自己的弱点，不同的目的和弱点造成了人物之间自然的喜剧冲突。 
- 非英雄指的是缺乏获胜必备的技能和工具的普通人。
- 非英雄并不是一无是处的，他们也具备一定的技能,但是对获胜来说远远不够。
- 做出非英雄的行为是因为只能这样做，除了这样做别无选择，而不是因为这样做好笑。
- 段子里的每一个人物都应该是非英雄，单口喜剧演员从任何维度上来说也都是非英雄。
- 非英雄缺乏的必备技能中有很重要的一项--信息,即非英雄不应该知道那么多，他们应该迷茫、困惑日愚蠢。
- 每个人都只能用自己的眼睛看到世界，所以无法对世界建立真实全面的认识。喜剧人物也只能从自己的眼中看到世界，人物必须有所不知。
- 叙述者必须比当事人知道得更多，观众知道的信息量则介于两者之间。
- 要努力维持“当事人(人物)<观众<叙述者(演员)“的动态平衡，要仔细地筛选信息，谨慎地给出信息要结合开放麦演出实践进行检验。
- 关系是人物存在的方式，人物的世界观要通过人物在关系中的表现来展示。
- 有所隐喻的人物关系揭示了人物眼中对关系本质的认知。
- 通过人物在表层关系中做出的不符合表层关系的言行，观众得以看到本质关系。所以，在有所隐喻的人物关系中，本体和喻体的共同点是人物的言行。
- 人物的言行必须既符合表层关系和当时的情境，又符合观众对本质关系的固有印象。
- 并非所有的人物关系都包含隐喻，不必强行构造有所隐喻的人物关系。
- 在塑造人物时不应该规定人物的行为特征，而是应在塑造人物时不应该规定人物的行为特征，让人物自然地在情境中做出该从其世界观出发，反应。
- 通过人物的行为表世界观取决于人物过往的经历，通过人物的行为表现出来，并对故事发生的环境和其他人物产生影响。
- 单口喜剧演员可以通过直接介绍或者讲述具体事件:在段子里展示自己碎片化的世界观。
- 段子中出现的其他配角人物，其行为必须具备独立性和一致性。
- 在一个故事中，要想让观众与人物更好地共情，可以展示人物的变化，也就是人物弧光。
- 人物弧光强调的是变化的过程，而非变化的方向。也就是说，人物弧光可以向四面八方延伸。
- 喜剧作品中可以展示人物追求变化最终失败的过程如果人物成功了，往往就会造就喜剧中的正剧时刻。
- 喜剧中允许出现正剧时刻。
- 单口喜剧可以展示人物在事件中的变化趋势。
- 通过信息量关系，单口喜剧演员可以让观众感受到人物的成长性。
- 直线指的是搞不清状况，无视问题，甚至是制造问题的状态;波浪线指的是清楚状况，非常努力地与状况做斗争，却屡战屡败的状态。
- 直线与波浪线是相对的而非绝对的状态，两个角色可以交替处于直线/波浪线的状态之中。
- 直线状态不等于毫无逻辑的混乱状态，直线角色依然有自己的逻辑和目的。
- 观众的情感聚焦点在于波浪线，因此我们要重点呈现的并非“好笑的行为”，而是人们对这一行为的反应。
- 直线(人物)<波浪线(人物)<观众<叙述者(演员)。
- 积极动作指的是，在人物眼中，能使人物的心理状况变得更好的动作。
- 积极动作不必以积极的形式呈现，也不必真的起到积极作用。
- 消极动作指的是非英雄失去希望时做出的动作，消极动作会造就正剧时刻。
- 自发情感能使观众更好地代入自身经验来理解作品
- 人物的自发情感要通过人物和情境的互动来展现。
- 单口喜剧演员为了更好地展示自发情感，就需要让自己在舞台上的状态无限接近自己在真实生活中的状态。
- 开放麦表演对展示自发情感有非常重要的作用。


《基本无害-Ep174 珀斯生存手册：知道这个行为不对，但我忍不住》珀斯的下期，还是很有趣的。

《晚点聊-134: Meta AI 人才动荡，上亿美元为何留不住人？| 与 Pokee AI 朱哲清盘点 AI 组织》，“所有公司事件中大致可以分为重要的 20% 和不重要的 80% 。如果所有人都在做重要的 20% ，还很忙，那没问题；但一旦有人在做 80% 的次要工作，他们就想变得重要。”

《非马非牛-怀想王小波：理想主义何处去》，人物更立体了一些。

《果壳时间-在青藏高原用烟花炸山，为什么激怒了所有人》，高山草甸的草毡层很薄很脆弱，但它是整个生态系统的基石，翻土 “修复”，只会造成二次伤害。


## 碎碎念

* Grapecity，听说是一家闷声发财的公司。
* 用 Logseq/Obsidian 也好几年了，还是不知道”关系图谱“有什么用处，现在看到基于图谱来展示 LLM Memory 的界面，还是不知道有什么用。
* 人数不能解决问题。
* 人物的这篇《靠送外卖减肥的年轻人》文章下面，有一个评论： 好害怕以后成为庸庸碌碌的大人。
* 看到直接用 cc 来帮助自己执行一些动作的分享，只能说胆子真大。
* Edge Copilot 是跨标签页的，有好处也有不好，我还是习惯每个标签页独立去对话。
* 国庆可以请 3 休 12，组内只有 2 个人请假，比我想象中少很多。
* 早上刚想说开发机最近挺稳的，结果就掉线了。