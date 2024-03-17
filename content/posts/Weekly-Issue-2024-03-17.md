---
title: Weekly Issue 2024-03-17
date: 2024-03-17
tags:
- Weekly
description:  
---


## 文章

### 技术

[JSON Canvas — An open file format for infinite canvas data.](https://jsoncanvas.org/)
[[Obsidian]] 的 [[Canvas]] 格式 spec，[GitHub - obsidianmd/jsoncanvas: An open file format for infinite canvas data.](https://github.com/obsidianmd/jsoncanvas)。

[[Obsidian]] 把自己的理念贯彻的比较彻底，虽然它自身不是开源软件，但是它的文件存储始终是文件文件，这点很重要。 File over app。

---

[用 Vite + DaisyUI 快速搭建前端工程 - Panda Home](https://old-panda.com/2023/02/12/how-to-quickly-setup-a-frontend-project-using-vite-and-daisyui/)
>作为第一次接触前端项目开发的初学者，我觉得还是有必要简单记录一下自己用 [Vite](https://vitejs.dev/) 和 [DaisyUI](https://daisyui.com/) 搭建项目框架的整个过程，虽然内容看起来非常初级，但对于一名前端新手来说却是必要的。

昨天和同事聊：

我：[GitHub - zauberzeug/nicegui: Create web-based user interfaces with Python. The nice way.](https://github.com/zauberzeug/nicegui) 这个看着不错  
同事：（我到现在都没理解写这类库的意义。。。我总觉得这条路是错的。。。Html 是一个非常好的用来表达 ui 的语言，为啥都想换掉它呢。。。  
我：现在存在这么多用 [[python]] 写 UI 的项目，都是因为前端项目的复杂度太高了。  
同事：用这种写出来的东西。。。可能 UI 也不需要太复杂的构建，需要复杂构建的，这类写出来也不一定好构建。。。真要觉得 ui 构建出来的东西麻烦。。。建议他们学习一下六七年前的我，document. CreateElement 来做动态页面  
我：现在一个随便起一个项目，vue/react ，就有多个配置文件了。。。   
同事：这些配置文件不需要你改实际上。。。   

---

[Acorn | Our new focus: developing an LLM app platform based on GPTScript technology](https://www.acorn.io/resources/blog/our-new-focus-developing-an-llm-app-platform-based-on-gpt-script-technology)

>A lot has happened since we started developing Acorn runtime 18 months ago. ChatGPT and LLMs changed the trajectory of infrastructure and application platform technologies. Since the majority of computing power, cost, and execution time will be spent on GPUs, we now have an opportunity to take a fresh look at the cloud native computing stack, from chips, data center, operating systems, cluster management, and application platforms. This is a once-in-a-generation opportunity for all of us.

>翻译：自从 18 个月前我们开始开发 Acorn 运行时以来，发生了很多事情。 ChatGPT 和 LLMs 改变了基础设施和应用程序平台技术的发展轨迹。由于大部分计算能力、成本和执行时间将花费在 GPU 上，因此我们现在有机会重新审视云原生计算堆栈，从芯片、数据中心、操作系统、集群管理和应用平台。这对我们所有人来说都是千载难逢的机会。

[[Acorn]] 是由 [[Rancher]] 的初创团队创立的公司，包括 CEO 和 CTO，在 2020 年 Rancher 被 SUSE 收购后，2022 年创立。[[Acorn]] 早期（截止到 2024 年 3 月之前）一直是将重点放在应用部署和管理上，但是最近将重点放在了 [[GPTScript]] 上，并且完全放弃了之前的所有项目。

---

[Structured logging: What it is and why you need it | New Relic](https://newrelic.com/blog/how-to-relic/structured-logging)

结构化日志的最佳实践：
- 保持一致的日志格式
- 使用标准的数据格式
- 包含所有的上下文和元数据：ID、时间戳、标签
- 保证日志是有用的
- 不要太冗长
- 遵循安全最佳实践：保证日志没有敏感数据
- 定期的监控分析日志

---






### 生活

[Do literally anything - Aaron Francis](https://aaronfrancis.com/2024/do-literally-anything/)
>You'll rarely discover "what's next" by standing still. Start working on _something_. Start tinkering. That will put you in motion to figure out what "the thing" is.

我们每天都有很多想做的事情，但是当想做的事情太多，选择太多，就会变拖延，可能不会开始任何意见事情。

这个时候，只需要做就可以了，做任何事情，有时候可能会想“一切都是不可能的，没有什么可以完成，宇宙中任何事情都是不可能完成的”，既然一切都不可能完成，那么就会担心所有事情，这个时候去做就可以了，任何事情。

---

[Site Unreachable](https://www.macrumors.com/2024/03/12/apple-announces-app-downloads-from-websites/)

[[Apple]] 允许欧盟开发者通过第三方应用商店上架自己的 app，还允许从网站上直接下载应用。

---

[Write issues not user stories - Linear Method](https://linear.app/method/write-issues-not-user-stories)

>When sharing a feature request or bug report, quote user feedback directly instead of summarizing it. Often, a customer describes the pain point more authentically than you could summarize it and it’s faster to copy and paste, too. Link to the customer conversation so that if more information is needed, it’s easy to get.

>Instead of building to mark a task done or check off a list of requirements, your focus is on the product or project deliverable.

在收集用户反馈时，不要中转，不要总结，直接有效的说出问题是什么，每个人会有自己的理解，从产品交付层面考虑功能本身，不要想着自己完成了一项 todo item。

---

[Be less precious](https://world.hey.com/dhh/be-less-precious-b20bf8c3)

[[DHH]] 暴论：你不应该太脆弱，如果你不想工作，那么请忍耐一下。不亏是资本家。

---


[周报 2024-03-08 -- 焦虑 - rxliuli blog](https://blog.rxliuli.com/p/017ba335b9cd4468ad5a70f621fba49f/)

作者列举了在[[日本]] [[京都]] 生活了半年之后，无法忍受的点：
- 被迫消费降级
	- > 吾辈的感觉是，如果之前在北京上海生活，并且来这边能够将收入提高到之前的 2 倍以上，来这边生活体验可能变化不大，否则就会被强制性的消费降级。
- 无法忍受的落差
	- 尊卑，包括敬语体系
	- 电子化程度低

---


## 书影


《多谈谈问题》，长篇采访合集，读了戴锦华的采访，其中关于《小丑》的全球流行的不解，是我之前没有思考的方向，我“自动”的觉得是“理所当然”的。

《一代宗师》，之前一直没看，不知道这么好看。

《泪之女王》，磕糖，又称《都敏俊入赘豪门悲痛欲绝》。



## 碎碎念

* >波音飞掉轮胎不知道发生在哪个州，毕竟有些州堕胎是非法的。地狱笑话。（背景：波音 777 在起飞过程中，轮胎掉落
* 在描述一个事物可靠的时候，如何定义可靠？
* >爱因斯坦曾说：“一个人提问的能力比回答的能力更重要。”
* Traefik 的文档格式很不友好，宽度很窄，信息密度很低，组织形式感觉也不太清晰，内容倒是全的，想找的东西总能找到
* 经过大半天的折腾，终于把自己的服务从 Cloudflare Tunnel -> Service ，改为了 Cloudflare Tunnel -> Traefik -> Service，可以在 Traefik 中做一些事情，比如 Basic Auth，感觉还可以



