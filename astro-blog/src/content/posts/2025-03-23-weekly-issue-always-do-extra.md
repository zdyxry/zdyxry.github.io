---
title: Weekly Issue-Always do Extra
date: "2025-03-23T00:00:00.000Z"
slug: "Weekly-Issue-Always-do-Extra"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Spegel 镜像分发介绍 | 卡瓦邦噶！](https://www.kawabangga.com/posts/6889)

Dragonfly 采用透明代理方式工作，会通过 [P2P](/mentions/p2p) 查找资源，如果找到，则通过 [P2P](/mentions/p2p) 进行下载，同时保存一份缓存，给其他节点请求提供文件。弊端：如果要对目标 IDC 服务进行扩容，同时扩容 100 个服务，100 个服务对应不同的镜像，就会全部请求到 Image Registry。此时要么事先同步所有 Image 到目标 IDC（浪费带宽），要么每次跨 IDC 拉取 Image（因为节点故障时，其他节点的缓存已经被删除）。

Nydus，把 image 进行文件级别的索引和分析，启动的时候只下载必要文件，其他的文件等 access 的时候再通过 P2P 网络下载。

Spegel 做了三件事：
- 暴露一个 HTTP 服务可以提供下载本机的 image；
- 对 containerd 做 image mirror，containerd 想要 pull image 的时候，会被 spegel 代理到去其他机器下载；
- 如何发现谁有什么镜像呢？服务发现是用的 P2P 网络，但是并没有用 P2P 来存储数据，本质上，只是用 P2P 来做了服务发现。Spegel 会定期把本地的 image 广播到 P2P 网络中，需要 image 的话，也会从 P2P 网络中寻找 Provider。

>  我会写一下如何从 0 启动并运行这个项目。读者可能会问，这不是按照项目的文档就能跑起来的吗？不是！这项目是云原生的，它居然没有文档，只有一个 Helm Charts[1](https://www.kawabangga.com/posts/6889#1aff1af1-566f-4e09-ac56-c868dc63a452)，命令行的参数看的云里雾里

想到了前阵子同事说 [GitHub - casdoor/casdoor](https://github.com/casdoor/casdoor)，启动 Server 需要同时准备 3 个不同的配置方式：命令行、server 配置文件（ini 格式）、init_data（json 格式）。 

---

[Build a Team that Ships](https://nav.al/build-a-team-that-ships)

> No tasks longer than one week. You have to ship something into live production every week – worst case, two weeks. If you just joined, ship something.

> If they can’t ship, release them. Our environment is wrong for them. They should go find someplace where they can thrive. There’s someplace for everyone.

> It’s not perfect. We ship too many features, many half-baked. The product is complex, with many blind alleys. It’s hard to integrate non-engineers – they aren’t valued.

> But, we ship.

---

[Introducing Starlite: A New Python Asynchronous API Framework | HackerNoon](https://hackernoon.com/introducing-starlite-a-new-python-asynchronous-api-framework)  
[Rise of the Pydantic Stack. What is the pydantic stack? | by Na'aman Hirschfeld | Python in Plain English](https://python.plainenglish.io/an-introduction-to-the-pydantic-stack-9e490d606c8d)  

[Starlite](/mentions/starlite) 的介绍，感觉后面如果有需求可以尝试一下。同时作者的另一篇关于 [Pydantic](/mentions/pydantic) 的文章，感觉现在这些框架的重点都是对 [Pydantic](/mentions/pydantic) 的支持。

---

[The Pain That is Github Actions](https://www.feldera.com/blog/the-pain-that-is-github-actions)

日常对 Github Actions 使用不多，基本上配置之后就没有关注过，所以文章内容本身没什么想法。Hacker News 的第一条评论非常认同：
* Write as much CI logic as possible in your own code. Does not really matter what you use (shell scripts, make, just, doit, mage, whatever) as long as it is proper, maintainable code.
* Invest time that your pipelines can run locally on a developer machine as well (as much as possible at least), otherwise testing/debugging pipelines becomes a nightmare.
* Avoid YAML as much as possible, period.
* Don't bind yourself to some fancy new VC-financed thing that will solve CI once and for all but needs to get monetized eventually (see: earthly, dagger, etc.)
* Always use your own runners, on-premise if possible

---

[LLM Agents are simply Graph — Tutorial For Dummies](https://zacharyhuang.substack.com/p/llm-agent-internal-as-a-graph-tutorial)

[Temporal for AI | Temporal](https://temporal.io/solutions/ai)

喜欢 [Temporal](/mentions/temporal) 的这句话：AI applications are inherently unreliable。

---


[Not all AI-assisted programming is vibe coding (but vibe coding rocks)](https://simonwillison.net/2025/Mar/19/vibe-coding/)

[X](https://x.com/karpathy/status/1886192184808149383)

突然在很多地方看到的词： `vibe coding`，直接理解就是 `完全依靠 LLM 进行编码`。

---

[I spent 181 minutes waiting for the Zig compiler this week](https://zackoverflow.dev/writing/i-spent-181-minutes-waiting-for-the-zig-compiler-this-week)

我日常好像没有统计过自己在一些常做操作的耗时，比如准备测试环境、等待 CI、等待编译时间。感觉可以统计一下看看。

---

[Always do Extra](https://www.bennorthrop.com/Essays/2021/always-do-extra.php)

> They all follow the same deliberate and dare-I-say selfish rule to how they approach their time: **Always do Extra**.

> The first rule is this: **Extra must be balanced against Normal Work**.
> The second rule of Extra is that **it must be aligned** with your Normal Work.

完全同意，Extra 和 More 是不同的，身边优秀的同事好像都有类似的特质。

---







### 生活

[Age is a problem at Apple](https://world.hey.com/dhh/age-is-a-problem-at-apple-f7ae6eca)

> Apple 董事会成员的平均年龄为 68 岁！近一半的人超过 70 岁，最年轻的 63 岁。高管团队的情况也好不到哪里去，平均年龄徘徊在 60 岁左右。

有趣。用 [Gemini](/mentions/gemini) 的 Deep Research 功能搜索了下其他科技公司的董事会的平均年龄：
- 苹果公司，67.38
- 英伟达公司，67.08
- 微软公司，61.17
- 亚马逊公司，66.17
- Alphabet (Google)，63.10
- Meta Platforms (Facebook)，44.33

---

[人生体验与记忆股息 - laike9m's blog](https://laike9m.com/blog/memory-dividend,163/)

> 首先，作者提到你可以把人生体验数值化。简单来说，就是给自己从体验中感受到的快乐打分。这样积累下来，就会有一个每年的分数。每个人对同一件事的感受大不相同，因此这个分数是完全主观的。

> 然后便可以引入『记忆股息』概念。股息是给股东定期派发的分红，即便股价不变，股息也能帮你积累财富。作者认为记忆带来的满足感亦是如此 —— 已经获得的快乐记忆，将随着时间推移持续带给你满足感。经过的时间越久，这些积累起来的满足感也就越大。因此可以知道，即便是同样的体验，越早获得收益也就越大。

> 说到底，在人生的最后，你拥有的只有回忆，是它决定了你对这一生是否满意。

有趣的总结。近些年和朋友的沟通中，能够感受到大家越来越在意自己的“体验”、“经历”。

---

[“男孩文化”，正在让这一代孩子经历“关系危机”？](https://archive.is/PYBx1)
> 韦认为，在我们的社会中，这种 “男孩文化” 随处可见。它的核心理念是：赚很多钱，买很多玩具，随心所欲地做事，而不考虑对他人的影响。这也是一种不重视友谊的文化，甚至将对人际关系的渴望定义为 “女性化的”。当下的社交媒体强化了这种文化：它们不断强调 “自我”，而非建立深层的联结。

> 2005 年时，中国的父母还不觉得男孩和女孩有什么差异。但他们如今不这样认为了。原因在于，我们愈渐生活在一个全球化的文化体系中，而这种文化很大程度上以个体为中心。我认为传统的中国文化并不是这样的，但如今，中国正在快速向这种高度个体化的方向转变，一切都围绕着 “我的成功、我的野心、我的赚钱能力” 展开。

---


## 书影


《最后的观星人》，艾米莉・莱维斯克（Emily Levesque），华盛顿大学天文学教授，讲述她自己和天文学的故事。是一本不错的科普读物，我对天文一无所知，看的津津有味。有些词语的翻译也很好。

《仁心俱乐部》，果然不行，编剧能力差距太大，弃了。

《梅西的世界杯：传奇崛起》，任何时候，运动体育都会带给我最简单直接的兴奋感。现在还会时不时的去看一些经典的夺冠记录。

《幸福伽菜子的快乐杀手生活》，不用猜，看名字就知道是日剧，爽剧，感觉这个剧如果放在大陆拍，就会被喷，放在日本拍又很合理，里面的一些吐槽也很可爱。



## 碎碎念

* 我的韶音是 2022 年 9 月买的，现在是 2025 年 3 月，电池已经不行了，用着用着就要充电了
* 如果你不知道自己是 i人还是e人， 你只需要认识一个真正的e人。
* 选择性忽略一些信息，果然会让生活变得更美好。
* 不吃早饭真的会得胆结石么？胆结石需要切除整个胆？我要开始吃早饭了。
* uv 使用自定义的 python 时，有些痛苦。
* 之前一直使用 grep.app 来进行代码搜索的，被 Vercel 收购之后改了 UI，感觉不好用了。
