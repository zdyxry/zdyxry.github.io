---
title: Weekly Issue-是商业行为还是厌女
date: 2024-08-25
tags:
- Weekly
description:  
---


## 文章

### 技术

[How To Force The 'true' Command To Return 'false'](https://blog.robertelder.org/force-true-command-to-return-false/)

`/usr/bin/true` 一定会返回 `True` 么？不一定。

当标准输出关闭时，调用 `help` 或 `version` flag 时，会返回 False。

---

[Becoming an SRE/Platform Engineer: A Comprehensive Guide](https://reliabilityengineering.substack.com/p/becoming-an-sreplatform-engineer)

SRE 工作指南，这里提到的点我觉得都还挺好的：
- 了解全局：在考虑问题时不止关注在单个工具，还要了解到完整的背景，多个服务之间是如何联通的，系统是如何串联起来的。
- 将内部工具当做产品来构建，用构建正式产品的心态来构建内部工具，内部工具不是一个玩具。

---

[Pop quiz: what is wrong with this tar command? - Xe Iaso](https://xeiaso.net/notes/2024/pop-quiz-tar/)

```bash
tar cf ../iosevka-iaso.tgz .
tar xzf iosevka-iaso.tgz # gzip: not a compressed stream
```

GNU tar 会查看文件扩展名来尝试确定用户的意图。如果执行 `tar xf foo.tgz` 或 `tar xf foo.tar.gz` ，它将调用 gzip 为您解压缩 tarball。这是预期的行为，当创建 tarball 时，不存在这个逻辑。

(MacOS 上好像不是这个行为？)

---

[Software estimates have never worked and never will](https://world.hey.com/dhh/software-estimates-have-never-worked-and-never-will-a41a9c71)

> 软件估时从未有效，也永远不会有效。伟大的软件都是在实施的同时做出权衡和让步的产物。

---


[x.com](https://x.com/kiwicopple/status/1825955571704508922)

[[Supabase]] 准备招聘自己的第一个 Product Manager，在 Requirements 中提到了 3 次 `Zero ego`，我理解这里可能的意思是：不以自我为中心、能够接受意见、友善合作？既要有想法，又不能太自我。

---

[uv: Unified Python packaging](https://astral.sh/blog/uv-unified-python-packaging)

属于 [[python]] 的 [[cargo]] 来了，[[uv]] 目前已经是一个完全的 Python 管理器，不只是 package，还包含 project、cmd、workspace 等等。是时候尝试从 [[poetry]] 切换到 [[uv]] 了。

[uv: Unified Python packaging](https://simonwillison.net/2024/Aug/20/uv-unified-python-packaging/)

由于官方的介绍博客内容很多，这是 Simon Willison 关于 [[uv]] 使用的一个快速说明。

---

[Amazon S3 now supports conditional writes](https://aws.amazon.com/cn/about-aws/whats-new/2024/08/amazon-s3-conditional-writes/)

> - If-None-Match — Upload the object only if no existing object with the same key name already exists in the specified bucket. Expects the * (asterisk) value.

[[AWS]] [[S3]] 支持条件写入，可以在创建对象之前检查对象是否存在。对象存储各家的基本操作一样，但是一些高级功能差异感觉还是挺大的。

[[Azure]] 很早就有了类似功能： [Specifying conditional headers for Blob service operations](https://learn.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations)

---


[I’m Tired of Fixing Customers’ AI Generated Code | by Tate Smith | Aug, 2024 | Medium](https://medium.com/@thetateman/im-tired-of-fixing-customers-ai-generated-code-94816bde4ceb)

>我确信这些挑战对于任何为 SAAS 业务提供支持的人来说听起来都很熟悉，但人工智能编程工具加剧了这个问题。帮助客户解决挑战通常是非常有价值的，但前提是我可以为可以自己完成大部分工作的客户消除障碍。当客户因为自己不具备这种能力而将软件工程转移给人工智能时，他们仍然需要找到开发人员来修复人工智能产生的错误。我不想成为那个开发者！

这篇文章的作者的一个产品提供了一些 API 用于提供加密货币交易的信息，这些 API 很简单，如果是一名开发人员会很快的使用它。但是作者最近收到的一些反馈通常是 LLM 生成的代码，其中有一篇很低级的错误。作者对于自己在这方便投入很多时间感觉到很不满。

感觉这个预期并不成立，如果没有 LLM，这些人也不会成为这个产品的客户。或者反过来考虑，这也说明这个方向是正确的，是有着一定的商业机会的？

---

[My IRC client runs on Kubernetes - Xe Iaso](https://xeiaso.net/blog/2024/k8s-irc-client/)

[My IRC client runs on Kubernetes | Hacker News](https://news.ycombinator.com/item?id=41332427)

[x.com](https://x.com/theprincessxena/status/1827103227256398215)

>A lot of the times when you're looking at someone else's infrastructure or a writeup of how they made something and why they made it that way, it's easy to see the end product and decry it as "overly complicated". Especially if it "seems simple" to you as you look at the end result in isolation.

> "simple/complex" is not the right paradigm. The real SRE controversy is "unique/standard". Yes, the standard approach is more complex. But it is better _in practice_ to have a single approach, rather than many individually-simpler, but in-aggregate-more-complex approaches.

Xe 在 Kubernetes 集群上配合 Kubevirt 和 Longhorn 使用 IRC Client，这篇文章本身分享的是 Xe 如何解决自己的问题，用的都是很成熟的技术，很多人不理解的是为什么要在 Kubernetes 上运行 VM。

如果从最终结果来看，评论给了很多方式，比如直接用虚拟机配合 systemd 管理、直接使用 container、或者其他。但是 Xe 此时已经存在了一个 Kubernetes 集群，并且所有的应用都在 Kubernetes 集群上运行，此时对于引入一个新的应用来说，继续使用 Kubernetes 明显是更好的选择，至少从应用统一的角度来说，已经存在“标准”，那么继续沿用已有的“标准”比为了一个应用而新增一种管理方式要好的多。

>Sometimes making things "complicated" really does make them "simple".

---

[What every SRE should know about GNU/Linux resolvers and Dual-Stack applications | Viacheslav Biriukov](https://biriukov.dev/docs/resolver-dual-stack-application/0-sre-should-know-about-gnu-linux-resolvers-and-dual-stack-applications/)

这篇关于 DNS 解析的教程写的非常的详细，完整阅读需要一些时间。

---

[Merchants of complexity](https://world.hey.com/dhh/merchants-of-complexity-4851301b)

都在追求简单，但是当真的要为简单付费的时候，又好像不太愿意（换位思考，我也不愿意）。只有特别的东西才能有溢价。

最近 [[Pieter Levels]] 说自己所有的服务都运行在 [[Digital Ocean]] 的一台 16c 64g  vps 上，一个月成本是 384 $，而运行在之上的服务一个月为他赚 200 万 $ ，大家争论的点是，是否真的需要复杂的技术栈。

---


[No, really: YAGNI - by Thorsten Ball - Register Spill](https://registerspill.thorstenball.com/p/no-really-yagni)

>You can't predict the future, no one can. What looks probable today might look laughable tomorrow and code added based on what's likely today might be dead code in a few months.

>Until then it's zombie code: code that isn't strictly dead — it _is_ executed — but it doesn’t affect functionality. It’s there because it _might_ affect functionality some day. And code — dead or alive or something in between — ain't free: it needs to be read, maintained, its tests need run. The less we have, the better off we are.

>If we can we remove it, let’s remove it, and if we know we could remove today, let’s not add it.

如果一段代码现在没用，那么就不要添加它。

---

[Changes to Chainguard Images developer tier](https://www.chainguard.dev/unchained/changes-to-chainguard-images-developer-tier)

>That means that some previously available Developer Images will no longer be freely available. We are doing this to make room for the investments in the Chainguard Production Images offering that represent the majority of what our customers want from us.

[[chainguard.dev]] 之后免费提供的 image 改为白名单机制，之后只提供一下内容：[Customer Notice: Free Image Tier Changes – Chainguard](https://support.chainguard.dev/hc/en-us/articles/28452542784667-Customer-Notice-Free-Image-Tier-Changes)

（想到之前组内分享 Chainguard 公司的时候，老板问了一句：这个公司的盈利模式是什么？现在知道了

---



### 生活

[“3A 大作不需要女性玩家”的背后，是游戏行业悠久的厌女历史](https://mp.weixin.qq.com/s/bE-VUGousVqV7dRE53_PWA)

[[游戏科学]]的一些言论，是带有男女刻板印象的，可能会造成女性受众不买他们的产品，或者抵制他们的产品，他们为自己的言论负责，好像没什么不妥？我不怎么玩游戏，之前在播客中听到某著名 XX 老师的言论：“她们玩的游戏和我玩的游戏不是一个游戏“类似的话术，不少人在评论区无法接受这些言论，他为自己的言论负责，承受了批评，好像没什么不妥？

如果女性的用户足够多，我相信会有厂商去赚这个钱的，比如《恋与制作人》？（这可能又是我的刻板印象）。想起之前 [【浮生一日】北京投资人的真实一天 -YouTube](https://www.youtube.com/watch?v=x2jl2PRlh0w) 中的男嘉宾的一句话：“巨多公司创业做低度酒，微醺的女孩都不够用了”，大家知道这是一个商机。

>“3A大作不需要女性玩家”的言论，本质上是男性玩家对女性越来越多涉入电玩圈核心的焦虑。**“3A”、“主机”这些标签意味着枪战凶杀等高度暴力的情节、对操作快节奏和高精度的要求，“硬核”游戏是男性气质展现的绝佳场合，是男性玩家的最后一片“圣土”。**

这个问题我之前也想过，有人说，女生无法买到合适的溯溪鞋，是对女生的歧视。我在想，如果真的有那么大的需求，厂商不是傻子，能赚钱为什么不赚呢？如果受众足够大，为什么没有厂商去赚这个钱呢？可能会因为固有的偏见而导致不去做这个市场么？还是这个市场可能存在的风险太大？这可能是一个商业行为而不是一个歧视行为？当然如果往上追溯，可能可以追溯到歧视吧。

关于言论部分，我从陈一发被举报的时候，就感受到了言论追溯的可怕，现在的风气已经变了。我开玩笑说，死刑犯的追诉期是 30 年，但是现在的言论追诉期是从你存在开始。只要你存在一天，你发表过的言论都会被追溯，无论是什么时期的你，无论你现在处于什么状态，只要你说过。这个潜在风险很可怕。

---

[Where at least I know I'm free](https://world.hey.com/dhh/where-at-least-i-know-i-m-free-da04f873)

> That's what the song is on about with "but at least I know I'm free"!

> I'd much rather live in a country that embraces everyone's right to BE FULL OF SHIT than one that pretends it can declare a priori what's true and what's false or one that makes false equivalences between violence and speech.

什么是[[自由]]，哪里是真正的[[自由]]，自由有其相对的成本，只要你能负担成本，那么就可以去享受自由。同时自由也是相对的，你需要明确的知道你用什么换到了什么。

---



[x.com](https://x.com/0065paula/status/1826444029321728449)

最近知名独立开发者 [[Pieter Levels]] 接受了采访，一个人觉得 levels 只是很幸运，自己很多年轻就做过类似的事情。Levels 恢复了一个截图，截图的内容是，2007 年 [[Dropbox]] 创始人在 Hackernews 上发布 Dropbox，标题是“My YC app: Dropbox - Throw away your USB drive”，但是在有一条评论：“对于 Linux 用户来说，可以直接通过 curlftpfs 来挂载 FTP 达到类似的目的，Windows 或者 Mac 也可以直接访问 FTP”。对于没有真正做出过一个完整产品的人来说，不要看一个人说了什么，要看一个人做了什么。有很多东西只有自己去做了，才会知道里面有多少坑。

配合 yihong 之前的一篇博客： [这玩意不是就\_\_ · Issue #291 · yihong0618/gitblog · GitHub](https://github.com/yihong0618/gitblog/issues/291) 

做一个善良的人。

---

[如何减少打断提升效率](https://wklken.me/posts/2024/08/25/how-to-reduce-interruptions-and-improve-efficiency.html)

统计、分析、总结、改善。实际上大部分都是通过文档来解决的，实施起来太难。

有时候也会想，为什么明明所有人都知道存在问题，都知道这个问题会影响所有员工的体验，但是老板不去解决呢？无论是老板还是老板的老板，都不会彻底的解决问题。私下闲聊偶尔也开玩笑说“老板到底是故意的，还是不小心？“。我唯一能想到的可能原因是因为老板上面也有老板，当业务压力强到一定程度，老板宁可继续维持现状运转下去，也不会做出大的改变。

---

[Kelly Johnson's 14 Rules of Management](https://en.wikipedia.org/wiki/Kelly_Johnson_(engineer) #Kelly_Johnson 's_14_Rules_of_Management)

>与该项目有任何关系的人数必须以近乎恶毒的方式受到限制。使用少量的优秀人才（与所谓的正常系统相比为 10% 至 25%）。

---

## 书影

《一级恐惧》，诺顿的演技真好。

《那年，我们的夏天》，二刷发现，故事并没有想象中的吸引我，可能是因为男女主分开的原因太单一，后面的故事走向又有些俗套。下一部打算看《没关系，是爱情啊》。

## 碎碎念

* 这两天深刻学习到的经验：项目开发的时候，最好公司名称、产品名称、项目名称、代码，这几个互相之间看不出任何关联。
* 什么叫“没苦硬吃” ？我自己有这种行为么？
* 如果一件事情很简单，那么保持简单就好，没必要描述的太复杂。
* 工作史就是脊椎各部位的疼痛史，劳动者在生产自身的苦难。
* 公司内部组和组之间的差别，太大了。
* 很多时候沟通很累，是因为对方描述不清楚问题。
