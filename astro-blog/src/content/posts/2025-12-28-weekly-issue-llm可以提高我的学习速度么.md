---
title: Weekly Issue-LLM可以提高我的学习速度么？
date: "2025-12-28T00:00:00.000Z"
slug: "Weekly-Issue-LLM可以提高我的学习速度么"
tags:
  - Weekly
description:
---

## 文章

### 技术


[Backing up Spotify - Anna’s Blog](https://annas-archive.li/blog/backing-up-spotify.html)

Anna-Archive 抓取了 [Spotify](/mentions/spotify) 的所有歌曲，大约 300TB。Spotify 拥有约 2.56 亿首曲目，超过 70% 的歌曲没人听，37% 的歌曲占了 99.6% 的收听量。

这件事情的另一个角度就是，按照 300TB 数据量来计算，如果都存储在 AWS 上，那么 Spotify 每个月只需要花 $7000 。

---

[Go ahead, self-host Postgres | Pierce Freeman](https://pierce.dev/notes/go-ahead-self-host-postgres#user-content-fn-1)

 一些关于 [Postgres](/mentions/postgres) 设置建议：
* 内存配置（Memory Configuration）：`shared_buffers` 设为 RAM 的 25%，`effective_cache_size` 设为 75%
* 连接管理：务必使用 PgBouncer 等连接池
* 存储调优：NVMe SSD 需调整 `random_page_cost` 为 1.1

---


[2025 was for AI what 2010 was for cloud (xpost) – charity.wtf](https://charity.wtf/2025/12/22/2025-was-for-ai-what-2010-was-for-cloud-xpost/)

对于普通用户来说，对 Cloud 迁移应该没有感知，但是 AI 对于普通用户却影响很大。如果真的从行业整体的角度来看，现在这些 AI 公司还能活跃 10 年么？感觉很难。

---


[Nobody knows how large software products work](https://www.seangoedecke.com/nobody-knows-how-software-products-work/)

> In fact, **the ability to answer questions about software is one of the core functions of an engineering team**.

> Because of all this, **the ability to accurately answer questions about large software systems is extremely valuable**.

很久之前，我投入了大量的精力在感兴趣的代码仓库中，那时候可以回答很多问题，随着精力的转移，慢慢的一些问题我也不确定了，就需要去读代码才能知道，后面发现随着产品复杂度增加，即使确定了一段代码的逻辑，但也不能给出用户看到的界面逻辑的准确说明。

很佩服一个测试同事，她总能清晰的记得所有细节，每次有相关的问题我都直接问她，很靠谱。

---

[How uv got so fast](https://nesbitt.io/2025/12/26/how-uv-got-so-fast.html)

> Uv is fast because of what it doesn’t do, not because of what language it’s written in. The standards work of PEP 518, 517, 621, and 658 made fast package management possible. Dropping eggs, pip. Conf, and permissive parsing made it achievable. Rust makes it a bit faster still.

其中提到的 `No pip.conf`，我最近在尝试把一个大型项目从 poetry 迁移到 uv 的时候，发现不会读取 `pip.conf`，还是有点麻烦的。

虽然目前迁移到 uv 的 patch CI 什么的都走通了，但是还是没有动力去推进合并，感觉要再加上 ty 检查之后，才算是一个明确的优化改进。

---

[Why Debian and RPM (source) packages are complicated](https://utcc.utoronto.ca/~cks/space/blog/linux/PackagesWhyComplicated)

我也想过为什么这些包管理器参数那么多，构建那么麻烦，后面以为 FPM 可以解决，至少可以解决大部分问题，然后发现 FPM 的参数也非常多，只要它还需要承担包管理器的预期，这个复杂度无法避免。

---



### 生活

[珍重 | Frost's Blog](https://frostming.com/posts/2025/take-care/)

> 能看出来，我很重感情，只是非常不擅于联络感情。最近《山河故人》重新上映，这是一部我很喜欢的电影，在某种程度上甚至塑造了我的人生观。它让我接受了每个人都是孤独的这件事，「每个人只能陪你走一段路」。所以我能接受这些遗憾，只能道声珍重，对那些还在联系，或者不再联系的朋友们。

---

[2025 重新定义的生活](https://diygod.cc/2025/)

> 这种替代感最刺痛的地方在于它并不只替代体力活。它在替代判断、套路、经验和熟练度，也在替代我曾经引以为傲的学习速度。我学到的知识在贬值，我积累的经验在贬值，我拥有的技能在贬值，甚至连智力和创造力都像在贬值，而且贬值速度似乎远高于我的成长速度。等程序员岗位真的消亡之后，我的价值在哪里。

> 经历这些事情之后，我开始重新审视开源对我而言究竟意味着什么。我对开源的态度，也从过去的绝对推崇，变成了一种带着警惕甚至轻微 PTSD 的复杂情绪。今后对开源的投入我应该也会更加兼顾现实、克制和有选择性。

---

[2025 年终小结](https://pacoxu.wordpress.com/2025/12/25/2025%e5%b9%b4%e7%bb%88%e5%b0%8f%e7%bb%93/)

> AI 焦虑，一方面来自 AI 发展的速度日新月异，新技术文章和项目如雨后春笋。学习速度远远跟不上 AI 发展速度，而且能感觉到越拉越多。

> 每个阶段 3-5 年，我们的焦虑点会有所不同，但似乎难以避免。

---

[2025 年我是怎么使用 AI 的 - 杰哥的{运维，编程，调板子}小笔记](https://jia.je/software/2025/12/25/my-ai-usage-2025/#vibe-coding)

> 高级编程语言出现了，那些写汇编的人去写高级语言，现在 Vibe Coding 来了，只是同一拨人又跑去做 Vibe Coding 罢了。持续学习才是最重要的。

> 总的下来，就是感叹自己也到了感慨科技进步的年纪了，十几年前学技术，虽然也能感觉到科技进步，但因为自己是从零开始，学的就是最新的科技，所以没有啥感觉。
> 但这几年，不断地把新的输入和已有的积累进行对比，就能感觉明显到技术潮流和技术栈的移动，也能感觉到自己对新技术的接受度开始有了略微的下降，这值得让我警醒。以前，我们总是嘲笑大人不追求潮流，不去学习手机等新技术，我们在这个时代长大的人，可也不能犯这样的错误呀。

---

[我的2025：一个凡人的修仙旅程](https://yage.ai/2025-year-end.html)

> 而有几个东西在 log 中非常稀少：
> - 纯粹属于伴侣的时间
> - 纯粹的朋友社交
> - 纯粹什么都不干，只是一个人呆着的时间。

全文读下来，感到可怕。这好像和我近些年追求的状态完全相反。

---


### 书影播客

《基本无害-Ep183 颜如晶的多重宇宙：永远做第二个吃螃蟹的人》，这期毛冬和颜如晶的聊天还挺有趣的，我对颜如晶了解很少，只知道她参加过《奇葩说》，跑过上马。一些记录：
- 觉得辩论水平上不去是因为自己是马来西亚人；
- 上马最痛苦的时候，期望的是收容车能够碾一下自己的脚；
- 执行力超强，要有自己的杀手锏，哪怕是I人，在酒局上不会说什么，但是能喝酒就是她的杀手锏；
- “我不会做第一个吃螃蟹的人，但是我有信心吃到第二个螃蟹”
- 又是一个可怕的J 人，因为自己当前没安排，第二天要去没去过的机场，所以会在当天去一次机场；


## LLM可以提高我的学习速度么？

我自认为学习新知识的速度不快，比如我学习某个概念，通常是找一个实际的项目，我完整的复刻一遍，在实现过程中去了解作者这里为什么这么做，这明显不是一个快速的方式，但对我来说是一个好的方式。我最近在了解 SELinux ，尝试给维护的系统开启 SELinux。

2025年了，LLM 时代了，日常解决问题大家第一个想到的都是LLM，那学习新东西呢？看到过一些关于 LLM 辅助学习的分享，自己也觉得理论上 LLM 是一个想问什么就问什么的“老师”，那应该很快？

这和 Vibe Coding 还不太一样，Vibe Coding ，用户关注的是最终产物，那么中间使用什么技术栈可能不关心（实际上我写项目的时候还是会明确的指定一些技术栈），或者因为完全不熟悉的领域无法关心，只要最终产物符合自己的需求就可以了。学习知识呢？我如何确定自己了解了？如何确定自己在面对问题的时候有一个明确的解决思路？

实际上手发现不是这么回事，我先让多个 DeepResearch 介绍背景，相关术语，实际的应用方式。ok，生成的文档看似什么都有了，但是无法串联起来，感觉是一堆抽象名词的集合，经过反复的对话，感觉自己像是那种只知道术语但是具体内容不知道的领导，张口就是subject、object、rule、policy、module，所有的概念都是理所当然的。真正上手的时候，还是懵的，因为我知道这些概念，也知道了一些常用的命令了，但是是漂浮在上空的，无法让我有信心，自己真的了解了。

最终我还是花了几天时间，老老实实的看完了官方文档，按照官方文档示例执行了大部分，去 Slideshare 上看了20个PPT 分享，了解在讲解的重点是什么，大家真正是怎么使用的，看完这些之后，尝试把自己记录的笔记整理下来。这时候我又想偷懒了，我都有这些笔记了，LLM 应该可以自动的总结一份文档了吧？不行，哪怕我说明了目标读者的背景，生成出来的文档还是很抽象，名词堆砌。它把我认为很重要的细节丢掉了，只给出了一些“结论”，有些过程是比结论更重要的，这些细节可以回答很多的“为什么”。

至少在2025年的12月，学习一个新东西，对我自己来说，还是读文档来的稳妥，当我依靠文档有一个完整的背景了解，实际上手的时候，遇到问题再去依靠 LLM 去解决。

## 碎碎念
* 尝试将一个巨大的 Python monorepo 从 poetry 迁移到 uv，终于走通了 happy path。
* RQrun 的会员真贵，完全是按照欧美价格定的。
* 361 爆沫 5，左脚有点压脚背，另外感觉有点软，能感受到缓震的效果，走路也能感受到一点点“滚动”的效果，尝试调整鞋带，看看是否能够好转。
* Kpop 好像很喜欢在歌曲给自己打水印？JYP、Blackpink，到现在的 ADP
* 圣诞了，歌曲都是经典的圣诞旋律了。
* 为什么开启 SELinux 会让人无比的痛苦呢？因为大家写代码都是乱来的。
* 什么时候需要专利，当你守不住秘密的时候。
* 最终还是得自己搞浏览器扩展，才最符合自己的阅读习惯。
* Mongobleed，什么人会在圣诞节前发漏洞啊，服了。
* 突然闻到了炸丸子的味道，好香啊，口水直流
* 宜家的衣柜，二次安装真是不容易，另外体力劳动和运动的差异真大，干了5h，累得不行。
