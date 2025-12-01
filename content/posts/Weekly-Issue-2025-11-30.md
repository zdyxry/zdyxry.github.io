---
title: Weekly Issue-《我们的箱根驿传》
date: 2025-11-30
tags:
- Weekly
description:
---



## 文章

### 技术

[How good are Chinese CPUs? Benchmarking the Loongson 3A6000 – Daniel Lemire's blog](https://lemire.me/blog/2025/11/23/how-good-are-chinese-cpus-benchmarking-the-loongson-3a6000/)

> Overall, I find these results quite good for the Loongson processor.
>  Chips and Cheese concluded “Engineers at Loongson have a lot to be proud of”: I agree.

Daniel Lemire 给 [[龙芯]] 3A6000进行了基础测试。

---


[Claude Opus 4.5, and why evaluating new LLMs is increasingly difficult](https://simonwillison.net/2025/Nov/24/claude-opus/)

> This represents a growing problem for me. My favorite moments in AI are when a new model gives me the ability to do something that simply wasn’t possible before. In the past these have felt a lot more obvious, but today it’s often very difficult to find concrete examples that differentiate the new generation of models from their predecessors.

这也是我最近的感受，我最近用 Amp 的次数可能超过了 Copilot，在中大型任务还是会优先使用 Copilot + Claude Sonnet 4.5，在一些较小的功能或者 bugfix 之类的，我会优先使用 Amp，因为我已经有了 “这么简单的任务 LLM 可以搞定的”观念。

[Why it takes months to tell if new AI models are good](https://www.seangoedecke.com/are-new-models-good/) 这篇文章也是类似的观点，真正要验证模型是否“好用”，还是需要“真正用”一段时间才能感受。

---

[一次性软件与被压缩的现实：AI Native 的本质是策略重构 | Superlinear Academy](https://www.superlinear.academy/c/ai-resources/ai-native-cost-structure-4e4d27)

> 换言之，当编写代码的成本接近于零时，以前离经叛道甚至匪夷所思的策略反而变成了最优策略：为了一个微小的临时需求，现场构建一个完善的专用工具。

---


[Migrating from GitHub to Codeberg ⚡ Zig Programming Language](https://ziglang.org/news/migrating-from-github-to-codeberg/)

[[Ziglang]] 从 [[github]] 迁移到了 [[Codeberg]]。我上一次用 [[Codeberg]] 是因为 [[ipmitool]], [[ipmitool]] 主要维护者是俄罗斯人，被 Github 禁掉了，当前只能在 [[Codeberg]] 维护了。

原来 [[Codeberg]] 是使用 [[Forgejo]] 来提供服务的： [#259 - Clustered Forgejo for Codeberg - Our journey and your knowledge - forgejo/discussions - Codeberg.org](https://codeberg.org/forgejo/discussions/issues/259) 。

---


[Wireshark tcptrace 图解读 | 三点水](https://lotabout.me/2025/wireshark-tcptrace/#fnref1)

包含了基本概念介绍，也有常见网络问题下的示例：丢包、吞吐受到接收方窗口限制、吞吐受到发送方窗口限制、网络状况很差等情况。

---

[Chris's Wiki :: blog/web/DoYouNeedCloudRequests](https://utcc.utoronto.ca/~cks/space/blog/web/DoYouNeedCloudRequests)

> If you only care about humans I strongly advise you to block every cloudhost subnet you can find, pretty easy given the effort they put into finding you. Most of the worst actors out there are living comfortably on Azure, GCP, Yandex and sometimes Huawei’s servers.

初看很认同，大部分来自于 Cloud 的请求都是垃圾，但转念一想，我大部分请求都是经过 [[VPN]] 的，我也会被屏蔽……

---

[Fun with incident data and statistical process control – Surfing Complexity](https://surfingcomplexity.blog/2025/11/27/fun-with-incident-data-and-statistical-process-control/)

> For a process that’s not under statistical control, a sample mean like MTTR isn’t informative: it has no predictive power, because the process itself is fundamentally unpredictable. Most incidents might be short, but then you hit a really tough one, that just takes you much longer to mitigate.

每次看到一些汇报 PPT 中的“平均解决时间”就很无力，不知道是想说明些啥。

Pyshewhart 这个 Python 库不错，感觉会用得上。

---

[Diving into Kubernetes' Watch Cache | Pierre Zemb's Blog](https://pierrezemb.fr/posts/diving-into-kubernetes-watch-cache/)

当缓存滞后于 etcd 的全局 revision 且资源长期无事件时，读取会在 `waitUntilFreshAndBlock()` 中最多等待 **3 秒**，超时则返回 “Too large resource version” 错误。通过实现 `RequestProgress` 来定期更新 revision ，解决超时问题。

---


### 生活

[after my dad died, we found the love letters | Jenneral HQ](https://www.jenn.site/after-my-dad-died-we-found-the-love-letters/)

作者在自己父亲去世后，发现父亲其实是一名同性恋，但是父亲在家中一直隐瞒着直到离去。不论作者父亲和 Edward 的感情再怎么好，文章最后一句是完全正确的： `he wasted his entire life, my mom said to me, the evening we found the love letters. his entire life, and mine as well.`

---

[[读后感]《美国儿科学会睡眠手册》](https://changchen.me/blog/20251124/sleep_what_every_parent_needs_to_know/)

> 假设你正在教孩子自己入睡，你已经每 10 分钟进来查看和安抚孩子。在孩子哭了 45 分钟之后，你感到精疲力竭，无法忍受了。于是你抱起孩子，带到你的床上。你刚刚教了孩子什么？**你只是教给他，如果他哭的时间足够长，你会进来抱起他**。

> 宝宝睡整觉是每个心力憔悴父母的终极目标，而该挑战的核心在于「自主入睡」能力的培养。当婴儿所有生理需求被满足后，请选择适当放手，在成长伴随的短暂阵痛后，换来的是整个家庭长期的幸福与健康。

---

[what I have learned from running](https://ciceroxiao.github.io/hong525/2025/11/25/what-I-have-learned-from-running.html)

> 就你做一件事，如果总是将借口丢给环境，那么，这当然轻松、可对自己没有什么实际好处的。

---
[how to keep writing/blogging](https://ciceroxiao.github.io/hong525/2025/11/17/how-to-keep-writing.html)

> 反正就是，写作 / 博客，是为了给自己一个认真活着的交代，而不是为了得到读者。活着是为了做喜欢的事情，而写作就是我喜欢的事情之一。如果分享出来的东西能够帮助到他人，那就是神的恩赐、我的幸运。

---

[Tech predictions for 2026 and beyond | All Things Distributed](https://www.allthingsdistributed.com/2025/11/tech-predictions-for-2026-and-beyond.html?utm_campaign=inbound&utm_source=rss)

> _孤独已达到流行病的程度， [全球每六个人中就有一人受其困扰](https://www.who.int/teams/social-determinants-of-health/demographic-change-and-healthy-ageing/social-isolation-and-loneliness) ，世界卫生组织已将其列为公共卫生危机。事实上，社交孤立会使死亡风险增加 [32%](https://www.bps.org.uk/research-digest/dying-company-loneliness-increases-mortality-risk-says-meta-analysis) ，与吸烟的风险相当；而孤独会使痴呆风险增加 31%，中风风险增加 30%。_

这么严重呢？

---
[爱达·魔都号邮轮攻略指北 | So!azy](https://blog.solazy.me/cruiseshiptips/)

[[游轮]]攻略，介绍的很清晰。

---


[派派成长日记 #8 - 憔悴的妈，崩溃的爸，兴奋的娃（150-180天）](https://changchen.me/blog/20251127/paipai_six_months/)

> 新的策略简单粗暴：“**什么也不做**” - 当孩子疲惫哭闹时，坚决不抱起，在旁边陪伴片刻，然后安静地离开房间耐心观察（每隔 5~10 分钟进入看一下宝宝）。

> 最终夜醒从 5-6 次，变为正常的稳定 2 次。哄睡时间从半小时起步，变为放在婴儿床上就行，甚至有时候忘记了他的存在。成长伴随的短暂阵痛，换来了整个家庭的长期幸福与健康。

太牛了，真的是从理论到实践。

---

[2025 年末收官战：神户马拉松 PB🥇](https://archive.is/eRNOp)

> 没有 35 公里后的「撞墙」，没有肠胃不适，没有肌肉酸痛，心率稳定，全程开心，最后还能冲刺。安静的起跑准备区，新鲜的空气，不时驶过的电车，阳光，大海，干净的赛道，负责的志愿者，热情但不嘈杂的氛围，秩序秩序秩序！太喜欢。对我来说是 2025 最完美的一场比赛。信心满满地进入冬训。

可遇不可求的理想状态啊。早上跟着 [神户马拉松《大电影》合二为一的奖牌\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV15gygBaEDL/) 视频，跑了 16km，神清气爽。

---

[二十六岁，长期主义与追星逐月 | 无辄的栈](https://www.zackwu.com/posts/2025-11-26-think-long-term-and-work-hard/)

> 我曾经一度相信：工作本身不需要有意义，只要能 WLB 且挣到足够的薪水，在工作之外做喜欢的事情追求意义即可。  

> 可是，当我因为其他原因的叠加而对工作产生倦怠的苗头时，价值感的缺失让我难以找到意义的锚点，从而越漂越远，直至看不见这艘船。

---
### 书影播客


《我们的箱根驿传》，作者是池井户润，最被人熟知的代表作应该是《半泽直树》。这部小说主要的视角放在了关东学生联合队，一直由未能进入决赛的大学各派出一名选手组成的队伍，他们可以参加箱根驿传，但是他们的成绩、名次都不会被正式记录。另一个视角放在了赛事转播的工作人员，如何让这个持续了 100+年，收视率在 25-30% 的节目，符合大众预期的完成。

书中的反派脸谱化很严重，也很刻板，没有任何的意料之外的情节，所有的情节都很“理应如此“的状态，但是体育类目就是有这种独特的魅力，真正读下来还是会沉浸在作者的世界中。这本书感觉会被影视改编，甚至知道作者之后，有一种这本书就是为了影视化而写的感觉。


《模范计程车 3》，这个爽剧出到第 3 部了，爽剧也不能无限的爽下去。


## 碎碎念

* 好像第一次见到 HTTP ERROR 451 。
* 空气不好、皮肤干燥、眼睛干涩、嘴唇开裂，不知道以为自己在 2016 年的北京呢。
* 知道了一个冷知识：旺旺和旺仔是两个形象！眼睛向上的是旺旺，眼睛看一边的是旺仔
* 看到了一个谐音梗：程式不足，Bash 有余。
* 中午吃饭，聊到 bolt 的中文释义，我记得是螺栓，同事记得是闪电，还分别都不记得对方的释义。
* > AI explores options, but can't tell you which is right. that's where specialization matters now – in judgment, not execution.
* 最近看到很多LLM 使用上的观点同质化严重，没学到什么东西。
* 疯狂动物城，第一部是和朋友一起看的，应该是在公主坟附近的电影院，可能是翠微？好久之前的事情了。
* “爆表”这个词，是来自于 AQI 上限是 500 么？
* 拿着 RHEL5 世代的合规要求做检测，难怪裁员先裁安全部门，这也不干活啊。
* Folo 凉了，也不意外。
* 今天是完美周五。
* 周日去观赛了上马，天气和给力。一共去了两个地方，分别是淮海中路 8.5km 和龙腾大道 35km。   
    * 淮海中路是从常熟路 2 号口出来，走到上海环贸路口，现场氛围很棒，沃尔沃还有拉拉队，放着 BGM，大家都很热情的给选手加油，感受到了世界顶尖选手从身边跑过的瞬间，真的就是一瞬间，太快了。很多选手会和观众击掌，给很多陌生人喊加油，人味很重。在这里本来想着能不能看到认识的选手，最后只看到了 [1124 酱](https://space.bilibili.com/9203468)。   
    * 龙腾大道是从龙耀路3 号口出来，走过去就是 34-35km处，这个是各个跑团私补（官方会有常规补给站点）的地方，看到了轻功、卢湾等跑团，有专人看到自己跑团的人会跟跑跟拍，同时也有很多的吃吃喝喝。有个跑团还搞了一个喇叭在喊：跑不动就吃点，这里有啤酒饮料快泉水，blabla。这个阶段的选手状态差距很大，我在的一小时看到腿部抽筋、膝盖受伤、乳贴掉了的选手就有不少，全靠意志力撑着。
