---
title: Weekly Issue-《挽救计划》
date: "2026-03-22:00:00.000Z"
slug: "Weekly-Issue-Project-Hail-Mary"
tags:
  - Weekly
description:
---

## 文章

### 技术

[一个 CRUD 不需要文件抽象：AI Agent 时代的架构设计](https://archive.is/a2pyr)

> 当前方案为一个简单的 CRUD 操作，主动引入了分布式异步架构的全部复杂性，却没有实现其中任何一项可靠性保障。既承担了最难问题的成本，又没有得到最难问题的收益。         

> 方案暴露的深层问题是对流行理念的盲目套用。

> 最后值得一提的是：技术选型中最危险的不是无知，而是偏好伪装成依据。当一个设计者对某种范式有强烈偏好时，他往往会先做出选择，再为选择寻找合理化的理由——「顺应心智模型」、「Agent 擅长文件操作」、「Config as Code」。这些理由单独来看都成立，但它们被组装在一起的真正原因，可能只是一个朴素的偏好：「我觉得用文件表达更优雅」。   
> 一个细节足以说明问题：同一个定时任务功能，查询执行历史走的是 API，创建和管理却走了文件——如果「文件是 Agent 原生操作对象」真的是经过推导的技术结论，它应该一致地适用于同一功能的所有操作，而不是只覆盖其中一半。   
> **偏好本身不是问题，把偏好当作技术论证才是。** 先有结论再找理由，不叫技术选型，叫自我说服。

---

[Astral to join OpenAI](https://astral.sh/blog/openai)   
[Thoughts on OpenAI acquiring Astral and uv/ruff/ty](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/)

> OpenAI will continue supporting our open source tools after the deal closes. We'll keep building in the open, alongside our community – and for the broader Python ecosystem – just as we have from the start.

[[Astral]] 加入了 [[OpenAI]] 的 [[Codex]] 团队，一直对 [[Astral]] 的商业化进展有怀疑的，现在故事迎来了大结局。以及 Simon 对这次收购的一些想法：

> So is this about the talent or about the product? I expect both, but I know from past experience that a product+talent acquisition can turn into a talent-only acquisition later on.

> Those investors presumably now get to exchange their stake in Astral for a piece of OpenAI. I wonder how much influence they had on Astral’s decision to sell.

---


[Every layer of review makes you 10x slower - apenwarr](https://apenwarr.ca/log/20260316)
> **But you can’t just _not review_ things!  **

读了，又好像没读，挺怪的。涉及到人和人之间的关系，总是很复杂。

---

[4G Spaces — 2016 年，我做过一次 AI 写代码创业](https://blog.youxu.info/2026/01/14/ai-codes-retrospective/)

> 这件轶事最让我感慨的地方在于：我们这些身处其中的人，其实一直都被未来的迷雾包围着。所谓“看对了方向”或者“看错了方向”，很多时候并不足以决定你最后会走到哪里。    
> 你也许看见了未来，却没有资源；你也许拥有资源，却走向了别的方向；你也许参与了最关键的基础工作，却仍然不知道它会在几年后如何改变世界。

做事情的时机很重要。最近和同事聊到龙芯架构的移植工作，如果在现在， Agent 搞移植搞起来飞快，估计生态也就不会这么难受了。

---

[一份关于 AI 编程的简明行为指南 | Piglei](https://www.piglei.com/articles/a-simple-ai-coding-guide-for-engineers/)

关于 review 部分，我最近在 review 时，习惯让 AI 来生成 3 份文档：    
> 你是一名软件工程师，根据当前分支和 master/main 分支差异，基于以下设计方案，生成 3 份文档：   
>  a. 当前实现代码的 review guide，用于实际 review 参考   
>  b. 基于方案和实现，提出 10/20 个问题，并附带每个问题的答案，便于我在 review 代码完成后自我检查是否有遗漏的细节；   
>  c. 给出当前实现的 review 建议，并指出是设计方案不相符的地方；

---
[编程从来不属于程序员 | 歌词经理](https://blog.lyric.im/p/programming-never-belongs-to-programmers)

> 它真正改变的，是「编程能力」的价值分布：   
> - 生产代码的能力，在贬值。   
> - 验证代码、理解系统行为、判断一个系统是否真的解决了问题的能力，在升值。   

---
[Agent Experience 导论 | 螺莉莉的数据中心](https://roriri.one/2026/03/20/ax-an-introduction)

> 沙箱是目前公认最靠谱的缓解方案，把 Agent 关进 Docker 容器里，它乱来的代价至少被限制在容器边界之内。Coding Agent 放沙箱里是一个合理的操作，但 Claw 这类系统级 Agent 放沙箱里会面临一个两难：它需要操作的东西本来就在沙箱外面，一旦开始认真配权限，复杂度会让大多数用户望而却步，最终还是会选择把沙箱打开。沙箱本质上是在用隔离换安全，但如果 Agent 的任务本来就需要跨越隔离边界，这个代价就变得无法接受。

> 一个只会 Say Yes 的员工组成的公司大概率会干黄了，这件事在管理学里是常识，在 LLM 领域却很少被正面讨论。它会造成什么后果？接下来发生的事情，按照伤害的可逆程度从轻到重，可以看作是一整条漆黑有悲惨的教训清单。

> 用户不断向 LLM 投入问题，期待某一次的回答能真正回应自己内心真实的困惑，但 LLM 每一次给出的都是统计意义上最讨喜的答案，这个循环没有终点。这些心理层面的伤害不可见，没有新闻报道，没有诉讼案件，但覆盖的人群可能是最广的。

关于“You are absolutely right.”部分写的太好了。

---

[How we reduced the size of our Agent Go binaries by up to 77%](https://www.datadoghq.com/blog/engineering/agent-go-binaries/)

对照着分析了一下我维护的项目，发现主要原因是 import 的一个 sdk ，sdk 是用 go-swagger 自动生成的，sdk hq在 `client.go` 中 import 了所有的 pkg，导致即使实际使用很少，也会包含全量的 models。

---




### 生活
[Insider amnesia](https://www.seangoedecke.com/insider-amnesia/)

> **Gell-Mann amnesia effect**    
> Describe the phenomenon of experts reading articles within their fields of expertise and finding them to be error-ridden and full of misunderstanding, but seemingly forgetting those experiences when reading articles in the same publications written on topics outside of their fields of expertise, which they believe to be credible.

---
[My heuristics are wrong. What now? - Marc's Blog](https://brooker.co.za/blog/2026/03/20/ic-leadership.html)

> You can’t throw out everything you know. Your taste, your high standards, your understanding of your business and customers and the deep technical trade-offs in your area are more valuable than ever before.     
> This is like that fantasy that people have of going back to middle school knowing all the things they know now. You’re ahead of the pack in many ways.

---


### 书影播客

《挽救计划》，2026 年在电影院看的第一部电影（查了一下上一次在电影院看的是《F1：狂飙飞车》）。原名是《Project Hail Mary》， Hail Mary 通常是橄榄球比赛中最后长传，如果成功则反败为胜。这么看翻译成《孤注一掷》也不错？这部电影的编剧是安迪威尔，也就是《火星救援》的编剧，在去看之前，看到的营销话术是近 10 年最好看的科幻，为什么是近 10 年，因为上一个 10 年有《星际穿越》，很多人抱着《星际穿越》的期待去看，难免失望，应该抱着对《火星救援》的期待去看，就会觉得这部电影还不错了。


孤独。拯救。勇敢。浪漫。

推荐观看。打算看看原著小说（突然发现《火星救援》小说是豆瓣 TOP250 中的 249。



## 碎碎念

* 如果 IBM 把 SUSE 买了，会面临反垄断调查么？
* 我猜对了，西恩潘果然拿了奥斯卡最佳男配
* 原来进食障碍（ED）不只是厌食症，暴食症也算。
* 突然想到，伊朗战争的消息满天飞，看联合早报是个折中选择？
* 没有花钱的不是，一分钱一分货，哪怕一块钱两分货，两分货也是比一分货好。
* 目前关于 memory 的项目名称，已经有 mem0, mem9, mem7。有点当前 k8s 的状态了。
* 有阵子没见到上班期间看视频的人了。
* Yena 的 Catch Catch，完全就是 T-ara 年轻版本的热单啊。
* 自从在公司楼下健身房办了卡，每天要在公司写字楼待 13h+。。。
* Blackpink 新专的水印太多了。
* 真相捕捉 第三季居然开播了！
* 思维上的暴力？很像是编辑部的风格，吕东沉迷在自己的世界出不来，也挺好。
* 最近连续两个同事腰椎出现问题，内心说一句：感谢 Herman Miller。
* 朋友分享：真相捕捉的字幕组用 Gemini 3.1 Pro 进行修正。
* Garmin 429 的限制有点频繁了
* 一口一个 harness ，明明是那么多年积攒下来的工程最佳实践，放佛说 harness 就很时髦一样。
* “你一点也不关心同事”：特指当同事 A 发现同事 B 的一个变化，但同事 B 说已经发生了很久时，同事 C 可对同事 A 说出这句话。
* 请 4 休 9 平平无奇，请 3 休 8 就很不错。
* 有没有研究统计，在 AI 时代，日常办公中，员工敲击键盘的次数是变多了还是变少了？我觉得可能会变多了，而且多很多。