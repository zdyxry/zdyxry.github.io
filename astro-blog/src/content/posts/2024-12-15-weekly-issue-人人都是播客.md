---
title: Weekly Issue-《人人都是播客》
date: "2024-12-15T00:00:00.000Z"
slug: "Weekly-Issue-人人都是播客"
tags:
  - Weekly
description:
---

## 文章

### 技术

[A letter to open-source maintainers](https://xuanwo.io/2024/10-a-letter-to-open-source-maintainers/)

> If you rely on this project to generate profit, consider not making it open source from the start. It’s entirely acceptable for someone to use your MIT-licensed projects to make money without even acknowledging your name. Don’t complain if others don’t compensate you for using your Apache 2.0 or MIT-licensed projects. Building a business is far more challenging than maintaining open-source projects.

 [[Xuanwo]] 写给开源维护者的一封信，真诚，真实。

---

[Google asks FTC to break up Microsoft's cloud deal with OpenAI, the Information says - CNA](https://www.channelnewsasia.com/business/google-asks-ftc-break-up-microsofts-cloud-deal-openai-information-says-4799626)

Google 要求 FTC 终止微软和 OpenAI 的独家协议。   
最近关于反垄断相关的新闻很多。根据我粗浅的理解，反垄断是为了创造更活跃的市场竞争关系。实际上落地可能就变成各大公司的手段了。

---
[Introducing Limbo: A complete rewrite of SQLite in Rust](https://turso.tech/blog/introducing-limbo-a-complete-rewrite-of-sqlite-in-rust)

> To complete the puzzle, we wanted to deterministically test the behavior of the database when interacting with the operating system and other components. To do that, we are partnering with [Antithesis](https://antithesis.com/), a company that provides a system-level Deterministic Simulation Testing framework, and can simulate all sorts of hardware and software failures. Antithesis does that by providing a deterministic hypervisor that runs many fuzzing threads in parallel, allowing us to quickly search the input space.

[[Turso]] 计划使用 Rust 来重写 [[SQlite]]。文中提到了 [Antithesis: autonomous software testing](https://antithesis.com/)，是 FoundationDB 的前工程师项目，解决自动化软件测试的问题。上一次看到 Antithesis 相关信息还是 2021 年。

---


[From where I left -antirez](https://antirez.com/news/144)

> I didn’t let Claude write a single line of the story or the plot: great use of AI is not making machines do what you can do better

---

[Gist of Go: Pipelines](https://antonz.org/go-concurrency/pipelines/)

[[Golang]] 中配合使用 `goroutine` 和 `channel` 的示例，包含了 cancel、merge、pipeline 的场景。在 merge 场景中，可以利用从 nil channel 读取时会永远阻塞的特性配合 `select` 处理输入 channel 关闭的场景。

---

[The Case for Shared Storage - WarpStream - Stream More, Manage Less](https://www.warpstream.com/blog/the-case-for-shared-storage#apache-kafka-and-other-data-streaming-systems)

[[WarpStream]] 关于 Shared Storage 文章，其中前面提到了 Shared Nothing 和 Shared Storage ，以及 WarpStream 采用 Shared Storage 虽然有相对更高的延迟（P 99 是几百毫秒），但是可以解决热点数据管理和 topic-partiton 限制。

---

[到底什么是时序数据库？ | Coding Husky](https://ericfu.me/what-exactly-is-timeseries-db/)

> 时序数据（time series）是一个由「时间戳 - 值」对组成的序列，通常表示某一个特定东西在时间上的变化。时间戳（timestamp）, 指标名称（metric name 或者 table）, 以及标签集合（label set），它们组合起来才能唯一确定一个数据点（value）。

> 有趣的是，你可以从两个视角来看待这个模型：
> 1. (name, labels) -> timeseries：在这个视角中，你通过 name 和 labels 找到一个（或一组） time series 向量，后续的操作也都作用于当前 time series 的所有数据点。这个视角更接近于传统的关系型数据库，例如 InfluxDB 的 InfluxQL 就是基于这个视角设计的。
> 2. (time) -> (table, labels, value)：在这个视角中，你先选定一个特定时间点的**切片**（snapshot），这个切片上面的 value 对应于所有 time series 在这个时间点的值。查询语言只需描述对单个时间切片的数据应该如何处理，因为每个切面都会重复完全一样的计算。Prometheus 的 PromQL 就是这样设计的。

---

[好了，现在你的知识也是我的了.jpg | Manjusaka](https://www.manjusaka.blog/posts/2024/12/06/ok-I-got-all-you-know/)

>我自己的宗旨是 “有些时候我不一定需要成为知识的生产者，而是成为知识的搬运者”

---






### 生活

[Good Title for Your Next Hacker News Post - laike9m's blog](https://laike9m.com/blog/popular-hackernews-title,162/)

如何起一个好标题，我理解好标题的基础是让文章目标受众想要点进去看看，如果能扩大受众就更好了：
- 乐趣与好奇心
- 痛点
- 关联性
- 深入的技术

---

[OldMapsOnline](https://www.oldmapsonline.org/zh#position=6/24/121)

世界历史地图，以时间轴的形式呈现，包含了历史背景，并且有维基百科相关的集成。制作的真不错。

---

[🟧 The new rules of media - One Thing](https://onethingnewsletter.substack.com/p/the-new-rules-of-media)

> Nothing matters more than the relationship between a person, brand, or publisher and their audience. Screentime has become a colosseum where everything is in competition with everything else: email from work competes with text from a friend competes with Instagram and Tiktok. Every second for the viewer is just that viral video where the person picks between two pop stars. You’re always deciding what to pay attention to. The relationship between person-who-makes and person-who-consumes is paramount to long-term success, because if you are winning that game then you will be able to survive.

关于社交媒体的一些新规则，虽然我用不上，但是套用自己关注的一些 UP/博客主播，还是觉得有些收获，自己的摘要总结：
- 第一条就很同意：“Everything is a personality cult”，人格魅力是一切的基础，要有亲和力。
- 当新平台出现时，及时的下场。不要把自己局限在单一平台或单一类型中，当老平台不再受宠时，去新平台玩老平台玩过的东西，有趣的东西就是好东西，即使他们已经“老了”，也是可以吸收很多关注的。
- 文字时代已经过去。保证自己的内容是可以迁移的，不要让平台绑架。明确自己的目的是什么。
- Parasocial interaction（准社会互动）很关键。（原来这是有专有名词的，比如我听很多播客几百个小时，我会自发的觉得自己和主播“很熟悉”，虽然这种熟悉是单方面的）。
- 将自己放在某个特定群体中有时候时好事，“An audience wants to feel like an in-group, like they’re in on the joke, even if that joke is just that the mayor of New York sucks.”

---



## 书影

《东京到京都》，孤独星球系列，2017 年出版。最近在准备签证，提前做做功课，这是一本工具参考书，由于是7 年前出版的，所以也不知道实际信息有了多少变化，当作介绍看看还是不错的。虽说“小蓝书终敌不过小红书“，但是实际上小红书的信息同质化严重，且随意抄袭，直接看孤独星球系列还是更有价值。

《数据化决策》，道格拉斯 W. 哈伯德，看了一半，需要进行一些思考整理。

《黑白厨师：料理阶级战争》，Netflix 出品的韩国综艺。邀请韩国的 100 位厨师来竞争，料理阶级战争。“阶级”这个词从综艺的第一集就有所体现，20 位已经功成名就（不知道这么说是否合适）的白厨师，80 位草根厨师，要先从 80位厨师中选出 20位黑厨师来和20 位百厨师竞争。白厨师站在高处看着 80位厨师竞争，对立关系就形成了。实际上大家的菜品差异很大，有非常精致的，有非常家常的，（有剧本不妨碍）拍的很精彩，精致餐厅的主厨都很有自己想法的，做出来的东西看着简单实际上很复杂，我其实不是很在意具体怎么做的，我只在意是否好吃。里面的米其林三星厨师安成宰会很重注菜品上的蔬菜熟度，他的要求是菜品上所有的东西都是为了让这道菜“更好吃”，而不是为了“更好看”。里面我比较喜欢的厨师是爱德华李、学生餐厨师、郑智善（但哈尔滨油泼面是什么鬼）。

《人人都是播客》，蒋祎娜，2023 年出版。作者之前在喜马拉雅负责主播生态运营，是行业内人士写的给入门主播的书。播客的起始时间比我想象中的晚，Podcast 这个词是 2004 年被创造的，Apple 2005 年增加了播客功能，2011 年国内的音频平台开始发展（比如常见的：蜻蜓、喜马拉雅、荔枝），即刻团队的小宇宙更是 2020 年才推出。今年算是播客的 20 周年？如果这么算的话，播客应该是近些年除了直播之外比较成功的媒介形式了？

书里介绍了一些播客的基本概念，分类，以及一些播客的案例。也介绍了如果想要制作属于自己的播客的话，如何开始，比如是单口、多人还是组合，如何选择合适的话题，以及制作播客的设备相关推荐等等。感觉上比《NPR 播客入门指南》更友好。

关于播客的选题，我一直觉得播客是一个强输出的形式，这里的强输出是相对于文本来说，不是说播客的信息密度比文本高（一定比文本低），而是落在文字的话，我们会仔细斟酌，反复修改，来保证我们最终表达的内容符合我们的预期。但是在播客中，（抛出剪辑）我们的表达是实时的，我们会表露出很多下意识的观点，不是每个人都能够对自己所有的话术都进行思考后再说出来。所以选题就会很重要，如果选题都是一些故事/观点类型的话，主播的储备量是无法支撑的，以我常听的播客来说，比如《谐星聊天会》、《基本无害》、《正经叭叭》、《没理想编辑部》，这些播客我基本上听了 200 小时以上，他们在最近的一些播客中，已经难免会说之前的播客中已经说过的信息了，这时候就需要有一些新的话题来支撑播客的继续。所以选题尤为重要，主播的日常输入也很重要，不然就会出现“重复”这种情况。有些播客主播自己已经耗尽了，就会找很多的嘉宾来支撑，比如《无聊斋》的见天地系列。


## 碎碎念

* 审美这东西真的很难改。写字楼去年搞了一个粉色的圣诞树，很土，今年搞了一个土豪金的摆饰，更土了
* AWS 是什么体量呢？是 2024 年 Q3 中的第二名 Azure 加上第三名 Google Cloud 才勉强超过 AWS。
* 如果一个订阅的 RSS feed 连续很多篇我都不感兴趣，要及时取消订阅。
* 朋友说：因为我没有车，出去可能影响到 dating，所以我现在都是打专车。
* BeanHub 发起了一个用户调查，其中一项是：“如果定价是你没有成为付费用户的原因，你认为什么价格是合理的”，现在 BeanHub 不同账户的直接限制是 Entry 数量，Pro 用户（每个月11刀）是 100,000 条。这是一个合理的设置么？现在浅显的想，如果不限制条目，提供更好的账户分析可能对我有吸引力一些。
* “嗯，我想了下自己成长为现在的样子也没人告诉我该怎么改，都是自己摸索，听人吐槽，不断琢磨”
* Obsidian web clipper 可用性已经很高了。
* 原来 “Vue”的名字是来自于法语的 “View”
* 在阅读一篇观点型博客时，博客的作者是谁很重要，期望能够有插件自动搜索并展示这个博客作者信息。
