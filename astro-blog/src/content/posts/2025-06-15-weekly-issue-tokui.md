---
title: Weekly Issue-tokui
date: "2025-06-15T00:00:00.000Z"
slug: "Weekly-Issue-tokui"
tags:
  - Weekly
description:
---

## 文章

### 技术
[Agents Need “State” Instead of “Memory”](https://blog.beautyyu.one/agents-need-states-zh#)

> 使用 memory 一词的时候我们不妨想想，到底有什么是值得记忆的？比如，作为终端用户来说，我希望我的 chatbot 能记住我们之间每一次对话的每个细节，这是一种 memory。但是如果我的 agent 要处理一个特定的任务，它一轮一轮地调用 tools，它用 memory 记住每一个 tool 的每一个具体输出，这有价值吗？

> 因此相比于 memory，我们应该换一个词称呼它：state。Agent 在每一轮运行过程中，它首先根据自己的 state 做出决策、调用工具，然后根据 tool output 更新自己所处的 state，再进入下一轮运行。就像一个寻路机器人要知道自己在迷宫中的位置及先前探索过的路线，然后据此做出下一步移动。

我最近也在考虑，如何处理我与各个 LLM 之间的记录数据，直接全量保存没有意义，很多时候一些对话只是简单问题，手动保存不现实，可能也没有必要。现在会把一些长对话，在得到阶段性答案后手动记录下来。

---

[Rust Week 2025 杂记 | CatCoding](https://catcoding.me/p/rust-week-notes/)

> 我发现一个编译器贡献排前三的大牛打字使用二指禅，有天早餐时他坐我对面，我问起为什么只用两个手指操作键盘，会不会效率不高。他说两个手指的速度已经够了，敲键盘能跟上我的思考速度就行。

---

[Typesense | Open Source Alternative to Algolia + Pinecone](https://typesense.org/)

[To Raise VC, or Not. Choosing The Road Less Travelled. | Typesense](https://typesense.org/blog/why-we-are-not-raising-funds/)

> We are concerned that “launching” a new “product line” (selling stocks) and bringing on a whole new group of customers (investors), would cause us to lose our precious bandwidth that could have otherwise been spent on our core search product that our primary group of users and customers expect from us. After all, the “company stock” product line would not exist without the core search product.

> When a large team congregates around work that cannot be parallelized, we’ve observed that new work gets created to keep everyone busy - new nice-to-have features get worked on. This ends up adding complexity to the product. New team routines are invented because there’s bandwidth available. This ends up adding communication overhead and layers between users and builders and slows down the pace of innovation. This sadly becomes a vicious cycle that dilutes the core product.

[[Typesense]] 是  [[Algolia]] , [[meilisearch]] 的开源替代品，这篇博客讲述了为什么没有接受风险投资的原因，在和很多 VC 进行沟通后，最终还是选择建立一家由客户收入支撑的公司，践行类似理念的还有 [[Obsidian]]。读完这篇文章，我就想试用一下他们的产品了。

---


[Cloudflare service outage June 12, 2025](https://blog.cloudflare.com/cloudflare-service-outage-june-12-2025/)

鸡蛋不要放在一个篮子里，如果多个篮子在同一辆车上呢？

---



### 生活

[中兴 F50 随身 Wi-Fi 体验记录 - 陪她去流浪](https://blog.twofei.com/1546/)

看上去这个 `F500` 400+ 的价格完全不可用，最近看到很多人在晒[[中兴]]的 `U60Pro` 随身 Wifi，2000+的价格，不知道实际使用怎么样。

---

[It must be worth it even if it doesn't work](https://world.hey.com/dhh/it-must-be-worth-it-even-if-it-doesn-t-work-1e7f49fc)

> The way to work without regrets is to pursue projects that'll have been worth your time even if they don't pan out. Projects that'll tickle your curiosity, flex your competency, and teach you something new regardless of where they ultimately end up. Projects that leave you better off, as a person, despite not being a commercial or critical success. If you work on projects like this, it's impossible to waste your time.

---




## 书影

《奇观》，小奇的单口喜剧专场。小奇是 2025 年单立人原创喜剧大赛的冠军，单立人比赛的含金量是在的，所以看到有专场直接来看了。小奇是一个中专生，讲述自己来到大城市之后看到的一些”奇观“，冠军是有道理的，段子很硬，梗翻的妙。这场的观看体验不好，观众有很多人一直在说话，声音很大。

## [tokui](https://github.com/zdyxry/tokui)

平时一直使用 `tokei` 来查看仓库的代码统计，`tokei` 默认输出如下：

```
[yiran@box tokui]> tokei
===============================================================================
 Language            Files        Lines         Code     Comments       Blanks
===============================================================================
 Go                     20         2185         1637          182          366
 Makefile                1           20           14            0            6
-------------------------------------------------------------------------------
 Markdown                1          117            0           86           31
 |- BASH                 1           19            8            7            4
 (Total)                            136            8           93           35
===============================================================================
 Total                  22         2322         1651          268          403
===============================================================================
```




一直有一个场景无法很好的处理，当 clone 下来一个仓库之后，如何找到当前仓库中代码量最大的目录？虽然 `tokei` 有 `-f` 的选项可以直接输出所有文件的统计信息，但是没有目录统计。laixintao 之前实现了 [tokei-pie](https://github.com/laixintao/tokei-pie)，是将 `tokei` 的输出转为旭日图，可以在浏览器中查看，可以满足我的需求，但我不想每次都打开浏览器，所以一直在找一个可以在终端中查看的方式/工具。

在 Todo 列表里面一直有一项任务是“基于 Textual 实现 Treemap”，Treemap 的交互形式一直没想好，优先级不高，一直就放在那里。上周突然看到了[noxdir](https://github.com/crumbyte/noxdir) 项目，一个用于查看磁盘空间使用率的 TUI，发现交互形式很好，看了看代码，主要的实现逻辑都在 bubbletea 和文件目录树的组织，只需要把磁盘空间使用率改为代码统计信息就可以。noxdir LICENSE 是 MIT，在代码中保留原作者的版权信息可以使用。

周末借助 Gemini Pro 2.5 和 Copilot，Vibe Coding 了一把，有了一个可用的版本： [tokui](https://github.com/zdyxry/tokui)。全部让 AI 生成，包含 README、CI 配置调整、代码注释等等。大概的流程是：把全量代码发给 Gemini Pro 2.5，同步发给它我的需求描述，让其返回目标代码结构和文件全量代码，得到全量代码后，让 Copilot 进行基本的编译调试。一点自己的使用经验：
* 如果代码体量不大，可以直接把所有代码发给 Gemini，效率很高；
* 需要批量修改很多文件时，Copilot 的 apply diff 效率较低，可以考虑使用 Roo Code；
* 可以通过调整 Copilot Agent Max Request 配置，来避免频繁确认；
* 最好显式说明需求中涉及到的所有概念；
* 当前 Copilot 无法调试 TUI



## 碎碎念

* 再次提醒自己，如果一件事情无法通过技术角度解读，那么可以从其他角度试试看。
* 每天使用很多设备，对于自己熟悉的系统，比如开发机，通常都会第一时间升级；对于自己不熟悉的系统，只要当前运行状态符合我的预期，我通常不会主动升级。
* 很多软件看似提供了很多数据，实际上没什么用。
* 一直以为 Linear 是一个小而美，没想到都 C轮融资了，看上去是为了这波 AI浪潮。
* 看到了一个工程师因为癌症去世的消息，在 Github 的提交停留在 2024 年 12 月。
* 如果关税战有 git commit，那这个 git log 一定很精彩。
* 我没有坐过波音 787。
* 自从开始 vibe coding ，睡得是一天比一天晚了
* RooCode 这类 vscode 插件存在是有道理的。

