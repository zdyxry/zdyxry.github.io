---
title: Weekly Issue-Pave The Road
date: "2026-08-30:00:00.000Z"
slug: "Weekly-Issue-Pave-The-Road"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Nutanix grows despite hardware price rises](https://www.blocksandfiles.com/hci/2026/08/27/nutanix-grows-despite-hardware-price-rises/5292962)   
[Nutanix built $20m AI cluster to reduce use of Copilot and Claude, expects ROI in a year](https://www.theregister.com/virtualization/2026/08/27/nutanix-built-20m-ai-cluster-to-reduce-use-of-copilot-and-claude-expects-roi-in-a-year/5292823)

> Setting that aside makes fy2025 net income $327.1 million, implying this year’s number for Fy2026 is 42.4 percent down.

> Nutanix [announced](https://ir.nutanix.com/sec-filings/sec-filing/8-k/0001193125-26-331661) a 5 percent workforce reduction earlier this month, meaning around 400 jobs would go.

> Nutanix is also porting its software to [Arm processors](https://www.theregister.com/virtualization/2026/08/27/nutanix-built-20m-ai-cluster-to-reduce-use-of-copilot-and-claude-expects-roi-in-a-year/5292823?utm_source=dlvr.it&utm_medium=twitter) as it wants to help lower its customers' hardware costs.

[[Nutanix]] 2026 财年净利润下降 42.4%，宣布裁员 5%(400 人)，将适配 Arm 服务器期望能降低用户成本。2027 年保持硬件价格继续上涨预期，交付周期可能会更长。

同时，他们花了$20M 来构建自己的本地 AI 集群，期望能够减少 Copilot 和 Claude 的使用，预计一年内回本。文章中有一句话：“He said Nutanix also continues to optimize the footprint of its stack”，软件自身的资源占用可能越来越被重视了。

---

[The Gravity of Ashburn, Virginia](https://kmcd.dev/posts/ashburn/)
[数据中心造就的五座城 · 卫星核查](https://madeye.github.io/datacenter-probe/)

刚好看到了两个关于数据中心选址的文章，Ashburn 公开的 IPv4 地址数量有 1.01 亿，远超过纽约、西雅图、芝加哥，是各种历史原因促成了这点，但是随着 AI 的需求变化，数据中心的主要依赖从网络变成了电力，Ashburn 后续的电力供应不足以应对更多的需求，新的数据中心集中地可能会变为其他地方。

另一篇是通过卫星地图来推测乌兰察布有多少规划、在建、建成的数据中心，可以看到数量不少，乌兰察布在内蒙中部平均气温 4.3，有丰富的风能和太阳能，电力便宜，加上距离北京非常近，高铁不到 2h，出差都能当天往返。

---

[Hummingbird - Fedora Project Wiki](https://fedoraproject.org/wiki/Hummingbird)

TLDR：基于 [[Fedora]] 的滚动发行版。
非常的极致，靠着 RedHat/Fedora 的基建来持续追踪上游社区 CVE，号称自己是 near zero CVEs，Distroless。整体看上去是看 Chainguard、Docker DHI 眼红，抢市场。

---

[私有化交付的 License 机制设计 | Chaney's MoonBook](https://chaneyzorn.github.io/codes/private-license-design/)

> 需要说明的是，garble 能正常编译 embed，但不会混淆 embed 文件的字节内容（验证见第 4 节）。所以从「内容是否被隐藏」的角度看，go: embed 并不比 `-ldflags` 更先进，两者都需要额外方式来保护内容（比如可逆变换）。   
> Go: embed 的优势在于分离更干净：公钥是一个独立文件，CI/CD 可以在构建前对它做清晰的预处理（变换、转换、注入），本地开发也更容易用临时文件替换，而不会被编译命令的复杂度牵制。

[GitHub - burrowers/garble: Obfuscate Go builds · GitHub](https://github.com/burrowers/garble)

---

[Pave The Road](https://ampcode.com/notes/pave-the-road)

> 世界上每个软件公司内部都贯穿着一张由土路组成的网络。这些道路曾经是拖拉机和 T 型车的天下，如今却挤满了各种各样的豪车，每一辆都比上一辆更快、性能更强、价格更高。   
> 然而，无论什么品牌，他们都只能在这条土路上颠簸前行，只能挂着二挡，因为这条路的设计根本就没考虑过这些车的路况。

> 毕竟，如果最新型号只需五分钟就能完成任务，但部署却需要五天时间，那又有什么用呢？   
> 自从一个月前我们发布了 Orbs 之后，我们的提交速度（本来就很快，毕竟我们是一家代码代理公司）提高了 65%，而且还在继续增长。现在，超过 85% 的代码提交都来自 Orbs。本地开发*虽然*还没完全消亡，但已经步入尾声，即将走向终结。

> 所以，我最后想说的是：只要你还在那些泥泞的道路上颠簸前行，下一代车型就无关紧要了。所以，先把路铺好，然后退后一步，好好看看这些东西究竟能做到什么。

这篇文章可以打印出来放在办公室里，反复阅读。新世界，旧世界。

---

[tison on X: "When Code Is Cheap"](https://x.com/tison1096/status/2092934388963275199)

> 那么，什么情况下我主动的不看代码呢？   
> 答案是以前写过充分的测试，软件 Scope 明确的代码，做重构的时候，可以不细看甚至不看。

> 因此，现在我的生产力最大的制约是身体健康，甚至不是时间。我在身体疲劳的情况下 reasoning effort 显著下降，结果就是无法阅读和引导 AI 的产出，软件产品处于一个 Plausible 而非 Convincing 的状态。因为我大脑罢工了，无法判断将 Plausible 的内容认证或改造成 Convincing 的内容。

> 反面例子就是，如果你说不清楚自己要什么，不知道实现路径上的关键点如何决策，即使有 AI 支持，很可能也做不出来。

---

### 生活


[午夜备忘：关于爱、自由与未来](https://innei.in/notes/2026/8/24/midnight-memo-love-freedom-future)

> 相亲时气氛比较尴尬，总得找点话题去挖掘对方的一些想法。整个饭局下来，大部分时间也都是我在创造话题、提问和倾听。我会尝试问一些直击灵魂的问题，也许是因为我更倾向于能够有灵魂上的共鸣。   
> 我不想即便在这种情况下，也依旧过着平庸乏味的生活——比如环游世界之后就再也没有想做的事情，一直宅着，心里也不再有想探索和学习的渴望。

> 老实说，我也很迷茫。Gemini 给我的评价是：这是典型的“高知/高收入理工男/大厂程序员思维”——既极度渴望高质量亲密关系，又极度害怕被传统婚姻套牢吸血；理论模型一套一套，实战经验严重不足。

> 我更追求灵魂的共鸣，而不只是每天嘘寒问暖——“吃了吗？”“睡了吗？”“在干什么？”这种毫无意义的表达和关怀。

嘘寒问暖不是毫无意义，甚至很有意义，“唉！你会不会肚子饿，我下碗面给你吃”的杀伤力有多大，也许某个夜深人静的时候能体会到。阳春白雪固然值得追求，下里巴人也不低人一等，把两者看成是对立面是扭曲的。

---

### 书影播客


《藏锋》，冲着士兵突击演员去的，结果发现是营销，主要是段奕宏自己的戏，还没看出什么吸引人的戏份，段奕宏演的还行，把一个一心想升职的副处演的挺好。


## 碎碎念

* Unix domain socket 长度限制是 104 - 108 字节，如果在 SSH Config ControlPath 中主机名/用户名很长，就会导致连接复用失败。
* 同事给了一瓶酸奶，写的山东泉城，指的是山东济南。
* 支持文件上传功能但是没有 checksum 支持，真是耍流氓啊
* 我想用 python lazy import。
* 不喜欢 DigitalOcean 的新的设计，丢失了自己的特色。
* 2026年8月27日下午发现了一根白发
* GitHubAction 今天的 schedule 延后了 8h 才开始执行，越来越夸张了。
* 不知道是不是错觉，kimi-code 不太好用了，尤其是 tasks 场景下，遇到了一些显示不一致的问题。
* 认识到自己精力是有限的，也是一种进步
* 还是觉得演示 LLM 能力用复刻商用软件不合适。
* 正大集团是泰国的，1921年成立的，小时候看正大综艺一直以为是中国的品牌，上一次知道类似的还是金龙鱼是新加坡的。
* 一个 pick 冲突，同样的 prompt，Codex 5.5 xhigh review 各种绕圈，kimi k3 解决的非常利落。
* 上海话，看山水，是阅读空气的意思。
* 看到一些观众心疼上中国的脱口秀演员了，说多么多么不容易，国内的脱口秀综艺就是考试，无论是单科成绩出彩还是总分排名靠前，都是曝光机会，美国有多少演员还在地下带着呢。