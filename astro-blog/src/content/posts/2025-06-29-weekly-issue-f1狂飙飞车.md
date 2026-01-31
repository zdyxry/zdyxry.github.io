---
title: Weekly Issue-《F1：狂飙飞车》
date: "2025-06-29T00:00:00.000Z"
slug: "Weekly-Issue-F1狂飙飞车"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Attach to a running container](https://code.visualstudio.com/docs/devcontainers/attach-container)

[vscode](/mentions/vscode) 在配合 [distrobox](/mentions/distrobox) 使用时，默认使用的是 `root` 用户，需要在 [vscode](/mentions/vscode) 本地配置中， `Dev Containers: Open Container Configuration File` 打开配置文件，指定 remoteUser 配置，配置示例：

```json
{
	"workspaceFolder": "/var/home/yiran/projects/xxx",
	"extensions": [
		"eamodio.gitlens",
		"github.copilot",
		"github.copilot-chat"
	],
    "remoteUser": "yiran",
}
```

---

[AI产品|AI 六小龙那些「活不过一年」的产品坟场](https://archive.is/SfK7y)

> **▶ MiniMax「万物追踪」：RSS+AI 的「伪效率」**
> - **初心：**帮用户聚合信息并生成摘要，对标 Feedly；
> - **现实：**82% 用户反馈「AI 摘要太冗长」，上线 6 个月后默默停运。

很难说是人不行还是产品不行。想到了某个同事的“总结性”周报，每次在 Slack 上都是一大篇，现在好像都快 1000 字了。  

"MiniMax 万物追踪停运前，竞品「Readwise」已迭代 3 次推荐算法，而万物追踪停留在初始版本；"，这里也挺奇怪的，[Feedly](/mentions/feedly) 和 [Readwise](/mentions/readwise) 面向的用户有重叠但是核心需求应该是不同的，印象中 [Readwise](/mentions/readwise) 在 AI 火爆之前就是热门产品了，现在说干不过 [Readwise](/mentions/readwise) 是因为推荐算法迭代速度赶不上，有点强行解释的意思。 

---

[JSON evolution in Go: from v1 to v2](https://antonz.org/go-json-v2/)

> Some notable Some notable **marshaling differences** include:
> - v1 marshals a nil slice to , v2 marshals to v1 marshals a nil slice to `null`, v2 marshals to `[]`. You can change it with the `FormatNilSliceAsNull` option.
> - v1 marshals a nil map to , v2 marshals to v1 marshals a nil map to `null`, v2 marshals to `{}`. You can change it with the `FormatNilMapAsNull` option.

读完就一个结论：别用 `v2`。

---

[Anthropic wins a major fair use victory for AI — but it’s still in trouble for stealing books](https://simonwillison.net/2025/Jun/24/anthropic-training/)

> Everyone reads texts, too, then writes new texts. They may need to pay for getting their hands on a text in the first instance. But to make anyone pay specifically for the use of a book each time they read it, each time they recall it from memory, each time they later draw upon it when writing new things in new ways would be unthinkable.  
>  For centuries, we have read and re-read books. We have admired, memorized, and internalized their sweeping themes, their substantive points, and their stylistic solutions to recurring writing problems.

[Anthropic](/mentions/anthropic) 在早期下载了大量的盗版书籍用于训练，后期为了避免法律风险，找到了负责 Google 图书扫描项目的合伙人，让他来获取"all the books in the world"，于是花了数百万美元买了大量二手书，进行拆解扫描得到 PDF。购买二手书籍用于训练目前被认为是合法的。

相关信息：20250131 Anna Archive（盗版资源站）发布博客，提到很多中国的 LLM 厂商与他们合作获取信息，希望美国能够改善版权管理。20250206 TorrentFreak 报道 Meta 通过 AnnaArchive 下载大量数据用于 AI 模型训练。

---

[Counter Service: How we rewrote it in Rust](https://engineering.grab.com/counter-service-how-we-rewrote-it-in-rust)

> Myth 1: Rust is blazingly fast! Faster than Golang!
> Myth 2: Rust is more efficient than Golang
> Myth 3: The learning curve of Rust is too high

[Grab](/mentions/grab) 将自己的 [Golang](/mentions/golang) Counter Service 用 [Rust](/mentions/rust) 重写了，最终得到的性能差不多，计算资源消耗是之前的 20%。这篇文章的叙事风格很舒服。

---

[How to Write Compelling Software Release Announcements · Refactoring English](https://refactoringenglish.com/chapters/release-announcements/)

> Release notes are not release announcements🔗

这篇教程很不错，发布公告是给用户看的，应该尽可能的以用户视角来编写，增加了哪些之前无法做到的功能、哪些使用体验上进行了改进。相对来说大部分用户不会去关注发布说明，发布说明某种意义上是给自己看的。

---

[How I Vibe Coding?](https://xuanwo.io/2025/03-how-i-vibe-coding/)

> Integrate AI into your existing workflow instead of adapting yourself to AI.

认同这句话，看到有些人在为了证明“现在的 AI 无法帮助我完成工作”而去使用，如果它无法帮助，那直接不用就好了，没必要硬要用。

---

[Kube-OVN 是如何自动修复 CVE 的 | Oilbeater 的自习室](https://oilbeater.com/2025/06/28/kube-ovn-autoupdate/)

> 存在上游新版本不稳定风险，目前两年内遇到过两次

疑问：如果遇到了 “不稳定” 的问题，在当前的自动更新流程中后续会咋处理呢，fix 到上一个版本然后周期性的观察问题是否有修复么？

作者回复： 
> 回到上一个版本，之前 dependantbot 可以用评论忽略掉某个版本，再就是看看有没有可能在自动化测试里发现这个问题了

全量自动更新的前提需要保证自动化测试覆盖率足够，分摊到平时挺好的，只是在版本管理阶段可能不好控制，比如在 LTS 场景中，通常是不期望有太多其他组件的功能变化的。对于一些基础组件（如 openSSH），从体感上来说一些漏洞都是高版本引入的，可能像 RHEL 那样维持在一个固定版本按需 patch 是一个更好的方式。

感觉适用场景还需要考虑。

---

[我对各种 AI Coding Agent 工具的看法 - XX's Blog](https://xxchan.me/ai/2025/06/08/ai-coding.html)

> Cursor 的创始人曾谈过他们对 “壁垒” 的看法：在这个发展过快，未来的想象空间也仍然很大的领域，**壁垒的本质就是 “快”**。只要你够快，就能领先。反之无论你当前的技术有多强、产品体验有多好，一旦你在某个阶段慢下来，就可能被超越、被取代，非常残酷。

> 简言之，**vibe coding 平台在严肃、复杂场景下的上限可能不足。** 如果只做简单的小项目或者 demo，价值肯定是有的，但有多少用户愿意为此买单，我就不懂了。这个故事，其实在 Vercel/Neon 这类主打 “开发者体验” 的 PaaS 平台上已经发生过：大家都说体验好，但等项目做大以后，很多人还是默默地迁移到了 AWS。

> 总的来说，现在所有的工具都处于一个 “still early, but already useful (if used correctly)” 的阶段。它们在简单的小活儿或生成 demo 上表现不错，但在复杂场景下，则非常考验使用者的 **“手艺”**。
> 这门 “手艺” 既包括 prompt engineering 的技巧，也包括对代码和 Agent 工作原理的理解。“了解 ai 能力边界” 也是个有点说烂了的东西。所以，未来能把 Agent 用得最好的，大概率还是专业人士。这就像专业摄影师和普通人的手机拍照，工具模糊了专业间的边界（比如工程师可以搞设计，PM 可以写 demo），但最终还是拉开了上限。

喜欢这篇文章的商业部分思考。

---




### 生活

[Design is compromise — Steph Ango](https://stephango.com/design-is-compromise)

> Appealing to everyone is impossible. If you make something that aims to be good across a broad range of capabilities, you are choosing not to be exceptional at anything in particular. That might be the right compromise for your audience, but it’s definitely a compromise.

---


[2025.5 俄罗斯胜利之旅](https://sides-hang-nca.craft.me/sDWvnvXAv7mzAV/b/5C785E1D-528F-4D3E-9DBF-80823D8117BA/Day1-%E5%8E%BB%E8%8E%AB%E6%96%AF%E7%A7%91)

bowen 同学的俄罗斯游记，边看边想，自己确实对俄罗斯有很多刻板印象，但是印象又很模糊。看完之后有了一些新的了解。



## 书影

《F1：狂飙飞车》，合格的商业类型片，值得去电影院看，156min 的时长，没有感觉很长，整体剧情推动很流程，剧情是老套的，没看就知道的结局，人物是刻板的，不掩盖电影本身的精彩。毕竟不是纪录片。

《二战新史-鲜血与废墟中的世界：1931-1945》，周末在上海图书馆吹空调看的书，历史总是相似的。人类从历史中学到的唯一教训，就是人类无法从历史中学到任何教训。



## 碎碎念

* 没想到 CNCF 是 Linux Foundation 的一部分，一直以为是平行关系。
* 记得刚工作的时候，同事们为了给产品起名字想的头都秃了，老板们还互相调侃对方是“起名小王子”，现在感觉时代变了。
* ghostty 的 terminfo 还是让我有些难受，暂时切回 wezterm 了。
* 用 TypeScript 写一个简单的命令工具，同事看完了，跟我说：`.... rollup `, ` ....minify ....`, `terser ....`, `tree-shaking ....`。 我只是想写一个命令工具，前端生态太可怕了。
* 最近感觉自己的肠胃好像和之前不一样了，难道是因为公司最近换牛奶了？可能要对照观察一下。
* 原来乐高是丹麦的公司，今天才知道。
* 做梦，梦到了我跑完步坐地铁回家，发现坐反了，然后进了一个陌生的家，用密码进去了，睡了一晚上，醒来的时候，发现不是我家。
* 现在有没有只专注于编程的小模型，便宜些的，感觉还是通用大模型赢家通吃的状态呢。Qwen Coder 貌似有阵子没更新了。
* 6月跑步 200km。