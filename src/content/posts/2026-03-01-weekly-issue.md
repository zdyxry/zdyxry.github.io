---
title: Weekly Issue-Treeverse
date: "2026-03-01:00:00.000Z"
slug: "Weekly-Issue-Treeverse"
tags:
  - Weekly
description:
---

## 文章

### 技术

[An update on our model deprecation commitments for Claude Opus 3 \\ Anthropic](https://www.anthropic.com/research/deprecation-updates-opus-3)

我不理解这种强行给模型赋予人格化的行为，这篇文章提到的所有行为，都是 [[Anthropic]] 来决定的，这种强行体现人文关怀除了来自我表扬，还有什么用处？而且模型公司主动的体现出这种人格化的宣传，不会让一些用户产生错误的情感映射么？一个高度的巴纳姆效应和 ELIZA 效应最终可以产生什么结果，是很可怕的，具体可以参考 [Murder of Suzanne Adams](https://en.wikipedia.org/wiki/Murder_of_Suzanne_Adams)。

---
[What Claude Code Actually Chooses — Amplifying](https://amplifying.ai/research/claude-code-picks)

[[Claude Code]] 技术栈倾向性：[[Prisma]] 被 [[Drizzle]] 干掉，[[Celery]] 也几乎不被采用了。后端服务部署首选是 [[Railway]]。

---


### 生活

[My Eighth Year as a Bootstrapped Founder · mtlynch.io](https://mtlynch.io/bootstrapped-founder-year-8/)

> When I started the book, I thought I’d be done in six months. I typically write almost a book’s worth of blog posts per year, and that’s just from an hour of writing per day. If I focus on a book, I should be done in 1/8th the time!
> It turns out that even when all I have to do is write, I can still only write for about an hour per day. After that, I feel drained, and my writing degrades rapidly.

不要妄想自己在休假/辞职之后，可以全身心的投入到某项事情当中，如果你在最有热情的时候都没有投入更多的精力，在休假/辞职之后就更缺少动力了，长期持续的投入是更可靠的实现目标的方式。

---


### 书影播客

《爱情怎么翻译？》，高允真、金宣虎主演的韩剧，应该是近期维护不多高分 Melo 剧了，刚看了前两集，希望结局不要崩。高允真的脸部状态好像不如前几年了，隔壁的朴智贤还比她大两岁，状态相对好很多。

## Treeverse 

项目地址：https://github.com/zdyxry/x-treeverse

Treeverse 项目是一个基于 Twitter API 开发的，推文可视化的工具，以树状图的形式展示推文之间的关系，帮助用户更好的阅读。但是自从 Twitter 被收购后，API 访问收到了限制（2026 年重新以收费形式开放），Treeverse 项目也归档了，作者将 main 分支从 Twitter 的支持调整到了 Bluesky的支持。

我一直很喜欢这种可视化的工具，尤其是关于一个特定主题的讨论，比如这条关于 [Prometheus](https://x.com/ayanamist/status/1930287945392763139) 的推文，我关注的开发者针对这个话题进行了大量的讨论，但是因为大家互相评论回复，导致经常要在不同的推文之间来回跳转，跳着跳着就迷路了，Treeverse 树状图的形式就很好的解决了这个问题。所以自从项目归档之后，一直在陆陆续续关注一些基于 Twitter API 的项目，比如 https://github.com/rxliuli/mass-block-twitter 。

上周想着把这个事情搞一下，先让 Kimi 基于原项目进行可行性分析，确认可行后，在 Github 上搜索相关的示例代码，搜到了这个仓库 https://github.com/fa0311/TwitterInternalAPIDocument/blob/master/docs/markdown/GraphQL.md ，但是有些差异，后面调试的时候我让它在控制台打印很多日志然后复制给它进行调试，最终效果还不错，我去掉了一些不必要的功能，比如：回复时间显示、链接分享、自动展开等。也增加了基于当前信息复制为 Mermaid 的功能，便于留存。

有时间还是要去研究下怎么 Remote 开发浏览器插件，怎么配合 Playwright，现在效率还是有些低。


## 碎碎念

* 强迫自己 3 天完全没看 AI 的内容，感觉生活真美好。
* 发现自己最近的 typo 次数越来越多了，但是还是不想用 AI 输入法自动纠正。
* 上班第一天，同事：哎，一想到这样的生活还要过 30 年，就哎。
* 突然想到， Agents 就是加强版 IFTTT 啊
* 昨天健身房有个大哥步频 190，我跟着节奏跑了 6km，真舒服。
* 为了备份方便，也不要用 docker volume。
* 春节后，同事找看问题起手式：新年好，帮看下这个问题。
* 要记录一下，体感上 Kimi 的 OCR 能力不如 Gemini Flash。
* AI 太适合提 Quiz 了
* IVE 之前出过 BANG BANG 这种舞曲么？总是幻听 Jump，直井怜的 Rap 确实不错。
* 看到各种 Sandbox 为了 100ms 、200ms 来优化，结果有的 Agent CLI 自己启动就要 1s。说的就是 iflow。
* CoreWeave 股价跌 18%，感觉算力厂商夹在中间很难受：自己不搞别人就搞，自己没订单；上游硬件厂商定价强势，没有议价空间；去年的顶配硬件到今年就是标配，换不起又留不住；模型厂商的盈利达不到预期。国内呢？云厂商面临的问题是相同的？可能更恶劣一点？比如华为的芯片会有自家云的倾向性？不给算力厂商留空间？
* 模型一分钱一分货，用能力范围内最好的。
* 周末跑18km，尝试在10km 吃了一罐胶，体感确实好了很多，没有那种 17km 之后的不适感，不知道是不是心理作用？
* 单休还是不行，休息不过来。
* 为什么韩剧中的江之岛那么好看，我去的时候天气阴的不行。