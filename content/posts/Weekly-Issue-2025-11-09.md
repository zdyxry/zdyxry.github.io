---
title: Weekly Issue-恭喜 Faker
date: 2025-11-09
tags:
- Weekly
description:
---


## 文章

### 技术

[Using Assisted-by commit footers instead of banning AI tools - Xe Iaso](https://xeiaso.net/notes/2025/assisted-by-footer/)  
[AI-Assisted Contributions Policy :: Fedora Docs](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/)

> Assisted-by: GPT-OSS 120b via OpenAI Codex (locally hosted)

> **Accountability**: You **MUST** take the responsibility for your contribution.
> **Transparency**: You **MUST** disclose the use of AI tools when the significant part of the contribution is taken from a tool without changes.
> **Contribution & Community Evaluation**: AI tools may be used to assist human reviewers by providing analysis and suggestions. You **MUST NOT** use AI as the sole or final arbiter in making a substantive or subjective judgment on a contribution, nor may it be used to evaluate a person’s standing within the community 

[[Fedora]] 这个策略说明和方式很不错，显式的告知使用的是什么模型、工具来辅助。

---
[Why we migrated from Python to Node.js](https://blog.yakkomajuri.com/blog/python-to-node)

[Python has had async for 10 years -- why isn't it more popular?](https://tonybaloney.github.io/posts/why-isnt-python-async-more-popular.html)
[Python concurrency: gevent had it right | Harshal Sheth](https://harshal.sheth.io/2025/09/12/python-async.html)

> We just did something crazy: we completely rewrote our backend from Python to Node just one week after our launch.

> Our initial benchmarks show we've gained ~3 x throughput out of the box and that's just with us running what is mostly sequential code in an async context.

不管咋说，用自己熟悉的技术栈都是有利于后续维护的。作者没有采用 [[Prisma]]。

---
[Why our website looks like an operating system - PostHog](https://posthog.com/blog/why-os)

[[PostHog]] 介绍自己为什么要这样设计网站，我作为用户不喜欢现在的状态，会让我有一种“失控”感。

> Often times, I’ll want to refer to different pages at the same time. So I’ll `CMD` + click “a couple times” while browsing around and before I know it, I have 12 new tabs open – all indistinguishable from each other because they share the same favicon.

这里提到的浏览方式是我之前经常使用的方式，甚至一度是我的搜索“屠龙记”「打开 Google 搜索，CMD 按住，点击前 10 个搜索，快速浏览页面找到自己想到的东西」，可惜这个方式在现在 [[LLM]] Research 时代已经用不到了。

---


[Absurd Workflows: Durable Execution With Just Postgres | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2025/11/3/absurd-workflows/)

[GitHub - earendil-works/absurd: An experiment in durability](https://github.com/earendil-works/absurd)

> _… because it's absurd how much you can over-design such a simple thing.  

万能的  `SELECT ... FOR UPDATE SKIP LOCKED `。最近在用 Temporal 的时候，业务本身都很简单，但一堆简单的业务 workflow 堆起来之后，代码组织感觉怪怪的，有时间得整理一下。

---

[You Should Write An Agent · The Fly Blog](https://fly.io/blog/everyone-write-an-agent/)

[[Fly.io]] 关于 [[Agent]] 的 101 文章，不如直接去看 [GitHub - PsiACE/bub: Bub it. Build it.](https://github.com/PsiACE/bub) 代码。

---

[Thinking Clearly – Daniel Lemire's blog](https://lemire.me/blog/2025/10/26/thinking-clearly/)

> Clear thinking demands precision.

> Too often, we accidentally hide behind overly abstract language. Not only does this harm how we think, but it also harms how we are perceived. People who avoid jargon are viewed as more honest, trustworthy and benevolent (Fick et al. 2025).

"我们常常不自觉地躲在过于抽象的语言背后。这不仅损害我们的思维方式，也影响他人对我们的观感。"

---

[Fu, Wei: Previewing Rebase Snapshots in containerd v2.2.0](https://fuweid.com/post/2025-containerd-220-rebase-snapshot/)

[[containerd]] v 2.2.0 版本中包含了 Rebase Snapshot 特性，可以提升大型镜像的下载效率。为了下载镜像速度做过的努力：
- 首先并发下载所有镜像层，然后按照层级关系依次解压。
	- 局限：解压每一层都需要先将所有祖先 snapshot 按照顺序 union mount，写放大。
- 直接将镜像层解压到对应的 snapshot 目录，避免为了解压而执行 union mount
- 下载与解压的并行处理，无需等待所有镜像层下载完毕，而是在任何一层下载完成后就立即启动解压任务
	- 局限：镜像层的解压必须严格按照其依赖的顺序进行，由于在大多数镜像结构中，较小或变更较少的层通常位于镜像的末尾，因此顺序依赖使得「并行解压」收益有限。
- 引入同一镜像层的并发下载能力
	- 局限：在网络质量可控的情况下，使用单连接的 HTTP/1.1 反而可能实现更高的吞吐性能。
- 允许在提交时，将一个没有 parent 的 active snapshot 绑定到指定的 committed snapshot 上，在下载镜像时，会同步解压所有镜像层，此时这些 Active snapshot 尚未指定父 snapshot。解压完成后，它们会按顺序提交，并关联到指定的父 snapshot，从而建立层之间的依赖关系。

---
[Fu, Wei: Previewing new mount manager in containerd v2.2.0](https://fuweid.com/post/2025-containerd-220-mount-manager/)

[[containerd]] Mount Manager 的背景知识，目标是解决现有 snapshotter 接口在处理复杂挂在场景时的问题，将挂载初始化动作从 snapshotter 中接口，并将挂载点的生命周期与容器绑定，可以及时清理。当前只有 EROFS snapshotter 集成了。

---



### 生活

[派派成长日记 #1 - Hello World 🐣](https://changchen.me/blog/20251103/paipai_hello_world/)

> 待产室是所有孕妇一起等待开指的大房间。在等待宫口完全开全的过程中，因为不清楚开指的速度，准爸爸一夜未眠，CC 更是辛苦，规律的宫缩带来了物理上无法想象的痛苦，然而心理上的煎熬更令人折磨。

各种意义上的不容易。

---


[阻止文明倒塌：JonathanBlow在莫斯科DevGAMM上的演讲 | 机核 GCORES](https://www.gcores.com/articles/110509)

[阻止文明倒塌：JonathanBlow在莫斯科DevGAMM上的演讲 | 机核 GCORES](https://www.gcores.com/articles/110509)

> Elon 认为，正好相反，科技在不付出巨大努力的情况下，是逐渐倒退的。在人类历史上，杰出的科技被完全遗忘，这件事经常发生。当代也一样。

> 这就是科技退步的原因。代际之间的交流和传承需要巨大的努力，这过程中有损失。如果代际的传承失败，文明就灭亡。

> Blow 的要点是：软件正在倒退，而人类空前依赖软件。Blow 给出了他对于 “软件明显在蓬勃发展” 之直观感受的解释：软件正在享受硬件能力提升的红利，它只是 “看上去” 蓬勃发展而已。Blow 认为，全行业的高抽象层次工作，多数人的 “高效率” 的另一面，是失去（或者从未拥有过）能力。

> 复杂性的提高，加速了知识的丢失：
> 1、知识总量更多，我们就让每个人知道的比例变得更小来应对。
> 2、『深知识』被『琐碎信息』替代。
> 3、好信息被噪音淹没。

> Blow 认为，显而易见的是，复杂性越高，我们承受灾难，或者体制性腐化（参考上文东罗马帝国），的能力就越差。而现在大家似乎相信，我们能承担的复杂性上限，是无限的。想象现在大公司里那种极少数能够透彻理解整个系统的工程师离退休之后后继无人、且很难把整套知识传递给年轻员工的情况，答案已经很明显了。

这是一篇 2019 年的文章，随着现代社会发展，工作细分是不可避免的，如果某种知识真的那么重要，那么人类可能早就灭绝了，既然人类现在还可以生存，就说明那种知识不是那么重要？软件的发展享受硬件的红利，这个放在 2025 年也是一种主流论调，硬件的发展不也是人类努力的结果么？

软件开发无论从哪个角度来看，都无法和人类社会的适应能力和恢复能力做比较。现在 LLM 时代，对于文章中提到的大部分角度，都会带来“加速”的效果，将其推向更极致的方向。反过来想，LLM 也可以作为强大的学习功能，部分知识可以更便利的传递，很多“体力劳动”可以略去，让人专心做当下“更有价值”的事情。

---
[我们的创业项目 Funes 在干嘛、以及怎么融到资的？ - by 汉洋 MasterPa - 汉洋滔天](https://hanyang.wtf/p/funes-d9c)

> 人类无法获得永恒，但我们总想对抗时间。这就是 Funes 存在的理由。 Funes 像是一个物理世界的 Github。我们和全球的用户一起，建模并存储一切人类的建筑与结构。

> 一个特定地方的价值本来就是不可估量的。它的重要性永远无法仅从社会角度来衡量。我们第一次约会的地点，我们与宠物散步的草地，我们曾经称之为家但如今不复存在的房间，我们对已不在身边的亲人怀有美好回忆的餐厅，我们开始职业生涯的办公室，以及我们最后坐过的教室 —— 这些地方可能不会引起历史学家的兴趣，但它们对我们所有人来说都具有巨大的价值，因为它们通过经历、感受和记忆定义了我们人类的存在。因此，保护这些看似无关紧要的空间同样至关重要。

> 走的时候他和我说，他是真的喜欢维基，但我接下来见大部分投资人最好换个对 Funes 的比喻，人人都说自己喜欢维基，但没有投资人想投维基。

我还记得自己第一次知道 Google Earth 时候的感觉，当时看世界上各种地方的街景看了很久。

---

[Collins’ Word of the Year 2025: AI meets authenticity as society shifts - Collins Dictionary Language Blog](https://blog.collinsdictionary.com/language-lovers/collins-word-of-the-year-2025-ai-meets-authenticity-as-society-shifts/?ref=selfh.st)

柯林斯词典的 2025 年度词汇是： `vibe coding`。这个词的受众有这么广么？

---

[When Stick Figures Fought - by Animation Obsessive Staff](https://animationobsessive.substack.com/p/when-stick-figures-fought)

火柴人 Flash 动画的一些历史，作者是朱志强，在 2000 年左右，作者凭借这火柴人系列大火，但无法带来收益，火柴人很难说是一个明确的 IP，在 2003 年耐克推出了火柴人广告系列之后，作者起诉了耐克，持续了多年，最后以败诉结束。

之后朱志强转行做程序员，现在在上海一家公司做游戏编辑器。

---

[泡温泉&跑步（别府篇） - luozhiyun\`s Blog](https://www.luozhiyun.com/archives/880)

> 但是我的观念最近在慢慢的改变，我觉得仪式感可能没什么不好。生活本质上是充满不确定性和混乱的。仪式感通过固定的程序和可预测的步骤，为我们创造了一个 “可控” 的心理空间，其实是一种对抗不确定性的方式。并且仪式感可以将平凡的日常行为转变为特殊且有意义的时刻，其实也蛮有意思。

---




### 书影播客

《正经叭叭-vol.222 是谁的命这么难算，到处都是正确答案》，这期聊玄学算命的，感觉每一个厉害的大师，都生活在 XX 省 YY 市 MM 区 NN 镇 FF 村 JJ 路口左转走 3 公里看到一个大树下，找他算命才准。

《二的三次方-vol:113 开局桌游领导来播客，被当场说破防了？》，脱口秀演员吴鼎、张灏喆在杭州开了一家桌游吧，11 月 8 日已经开业了，最近应该是为了宣传，录了很多播客，所有人都觉得他们干不了几年就会破产。

《没理想编辑部-Vol.199 成为自己的富婆》，聊到最后，还是“配得感”。

《无聊斋-vol.550 喜夜群英会｜聊聊晔乎不老王的儿时疯癫、上海滩往事、金牌销售史和劝学直播间》，再次印证了那个观点，当下在喜剧节目中看到的所有演员，都是专业的，无论是脱口秀还是 sketch，不要想着自己写几个段子上去就能演好，妄想。

## 碎碎念

* 习惯的力量太强了，有一个 CLI 已经被 deprecated 很久了，一线还在使用，为了他们的使用，还得继续维护。
* 最近经常在各个地方看到 Kata Containers，查了一下，原来 5 年前就用 Rust 重写了。
* All in EasyTier.
* 真割裂啊，有时候需要单独在微信里才能搜索到特定的文章。
* 每当觉得 LLM 已经行的时候，就会在一个简单的问题告诉你：我还不行。+2。
* 本身只是一个吐槽，突然接到了一个离谱的需求，没想到触碰到了推特上的热门流量关键词，吓得我锁推了。
* 看到新闻说，Apple 每年给 Google $1B 来将 Gemini 集成到 Siri 中，风水轮流转。
* 黄明志被通缉了，飘向北方还能唱么？
* 看到了一个“Vibe Hiring”，万物皆可 Vibe。
* 一个人说自己“看得懂”，建议是等他自己发现自己“看不懂”。
* 突然发现 slack 最近“老师”出现的频率有点高，玩梗么，不是什么好预兆。
* 大概数了一下，衣柜里的衣服中，公司发的比例超过了 50%🤔
* containerd/nerdbox 感觉不错，本身是一个 shim，使用 VM 作为运行环境。还处于非常早期的状态。
* 抽象的人做抽象的事。
* Faker 的剧本太完美了。

![2017 年鸟巢](https://oss.zdyxry.com/faker-2017.jpg)

![2025 年成都](https://oss.zdyxry.com/faker-2025.jpg)
