---
title: Weekly Issue-龙架构双周会
date: 2025-03-17
tags:
- Weekly
description:  
---


## 文章

### 技术

[Why Go? · microsoft/typescript-go · Discussion #411 · GitHub](https://github.com/microsoft/typescript-go/discussions/411)

[X](https://x.com/mitchellh/status/1900272945219723552)
> Snobbery looking down on anyone not using it and a completely irrational feeling culture of rewriting everything. As Steve says, this may be perception more than reality. It may be a small (but obnoxiously loud) minority. It really might. But it was enough that at the time it was my reality and I wanted nothing to do with it.


尽管已经给出了详细的原因，评论中的很多人还是充满了傲慢。

---

[踩坑异闻录——Windows 前端工具链之痛 - 三咲智子 Kevin Deng](https://xlog.sxzz.moe/nodejs-windows-compatibility)

身边用 [[Windows]] 开发的同事只有一个，如果只是兼容性问题还是好的，大部分项目中的 Makefile/Taskfile 等 setup 工具，有可能完全没有考虑 Windows 用户，经常会遇到一些只有他会遇到的问题。

---

[第 6 次龙架构双周会](https://www.kdocs.cn/l/ciib1cwuGm4x)

这个报告中的“浅评商业软件发型乱象”，如果是平时工作中涉及到一些 Linux 发行版内容的，强烈推荐阅读，看着看着就笑了，笑着笑着就哭了。里面提到了一些商业软件存在的问题：
- 明明程序对其他 so 有依赖，但是不在包管理器中指定；
	- “只要有群友教，没什么不可以解决的”
- 安装程序权限控制不明确，影响范围不可控
- 通过包管理器的 postinst 脚本来做一些隐蔽的事情
- 不使用系统提供的基础设施进行系统状态探测、随意猜测配置文件内容
- ...

只要是涉及到软件交付的，都会面临这样的问题，无论是 2C 还是 2B，2B 的单一软件还是软硬件一体，都面临这个问题。有时候以为自己交付的 OS 是自己可以控制的，所以做了一些hack 的事情，假设了用户不会对 OS 内部做变更，但最终软件是在用户环境中运行的，很多假设都是不成立的（也是不合理的），导致后续引发更多的问题。

平时都会吐槽外部的软件不遵循一些业内通用标准，其实公司内部的软件也没几个遵循的，“又不是不能用”的理念到处存在。最终只会导致软件越来越臃肿，一个又一个补丁，最终陷入恶性循环。

---


[从 DeepSeek LLM 到 DeepSeek R1 —— DeepSeek LLM | Oilbeater 的自习室](https://oilbeater.com/2025/03/14/deepseek-from-llm-to-r1/)

> 从论文的路径上来看就是 DeepSeek LLM -> DeepSeek MoE -> DeepSeek V2 -> DeepSeek V3 -> DeepSeek R1。在整理论文时我才发现，DeepSeek 第一篇对外发布的论文是在 2024 年的 1 月，当时他们刚发布第一版模型，即使在 AI 行业内也不被认为是个主要竞争者。然而仅仅一年后的 2025 年 1 月，就已经进化到了 R1 这种业界领先水平。都说 AI 一天，人间一年，但是当真看到人间一年的进展时，还是深深的被 DeepSeek 的速度所震撼。

---

[Yoke is really cool - Xe Iaso](https://xeiaso.net/blog/2025/yoke-k8s/)  
官方文档：  [| yoke](https://yokecd.github.io/docs/)  
示例代码：[yoke-stuff/within-website-app/v1/app.go at main · Xe/yoke-stuff · GitHub](https://github.com/Xe/yoke-stuff/blob/main/within-website-app/v1/app.go)   

[[Yoke]] 是一个 [[kubernetes]] 的包管理器，定位与 [[Helm]] 和 [[Timoni]] 相同，Yoke 的 Flights 相当于 Helm 的 Chart。主要的区别是 Yoke 不使用 YAML/CUE 等配置语言，而是使用通用的编程语言来描述资源，可能会想到 [[Pulumi]] ，与 [[Pulumi]] 不同的是，Pulumi 需要准备对应语言的 runtime 和 deps，Yoke Flights 的发布形态是 [[WASM]]，Flights 接收输入参数，输出 Kubernetes 资源描述，这里有点疑问，Flights 的接收参数如果过多，最终不会演进为需要一个配置文件的程度么？

Yoke 引入了 ATC 解决这个问题，ATC 是一个 Kubernetes controller，通过定义 CRD，并与对应的 Flights 进行关联，从而将用户声明的配置转换为 Flights 需要的输入，最终部署到集群中。相当于一个简化版的 Operator ？

Flights 的发布形式是 WASM，那其他人如何了解对应的 Flights 的定义？需要引入其他的文档描述？关于 WASM 的能力，官方文档提到 Yoke 暴露了 K8s lookup 接口，这个接口能力足够么，会是一个限制么？

---

[IO devices and latency — PlanetScale](https://planetscale.com/blog/io-devices-and-latency)

[[PlanetScale]] 的博客，图示生动形象。

---




### 生活

[《双影奇境》：一部无与伦比、超乎想象、精彩绝伦的双人游戏作品 - Simon's Blog](https://song.al/SplitFiction)

> 对于电子游戏，在很长一段时间里，我都陷入了“电子阳痿”的状态里：虽然我有switch、ps5、pc等一众游戏设备，但几乎对所有的游戏都提不起兴趣；在近几年中，我尝试玩过很多优秀的电子游戏大作，但没有任何一款游戏可以让我持续坐在电脑前面、全神贯注地游玩几天，直至通关。我得承认，随着年龄的增长，电子游戏似乎已经离我越来越远，我也对游戏的兴趣越来越少。

> 但《双影奇境》这款游戏让我前面所提到的一切负面状态近乎完全消失。《双影奇境》是近几年唯一让我能够废寝忘食地在电脑面前持续游玩了14.8小时，直至通关的游戏。

非常高的评价了。

---

[聊天也要讲逻辑 | So!azy](https://blog.solazy.me/20250226/)

> 对话中存在两种让我头疼的现象：一种是「驴唇不对马嘴」，另一种是对方把「两件事」揉在一起聊。这两种情况虽然有些相似，但本质上不太一样，却都会让我觉得沟通变得异常艰难。

> 这种对话让我反思，逻辑清晰真的很重要。不是每个人都要像科学家一样严谨，但如果连基本的事实和因果都串不起来，那得出的结论只能是空中楼阁。我不否认情绪和直觉有它的价值，可如果完全抛开理性，把毫不相关的碎片硬凑在一起，这样的沟通不仅解决不了问题，反而会制造更多误解。

一个可能得解决方式是，在无法清楚的表达自己想法的时候，保持沉默，思考，理清之后再回复。

---



## 书影

《流氓读书会》，漫改韩剧，下饭局，只有 10 集。武状元一心想当文秀才的故事。

《仁心俱乐部》，都市医疗剧，看的时候一直在想，为什么和《机智的医生生活》差距那么大，是哪些原因造成的？目前能够想到的是：编剧能力差距太大；对快节奏的变态追求。

## 碎碎念

* 买了佳明手表，感觉买晚了，应该早点买。
* "Mushroom 听起来像是天津人问 room 这个词“，有笑到。
* Narcissistic personality disorder，自恋型人格障碍。
* 2025 了，一个标准的服务配置居然不提供 container ，而是让我 dnf install mysqld ，有点离谱了。
* 很多时候大家都知道自己做的东西不好用，只是因为各种各样的原因改不动。
* 人总是倾向自己更喜欢的推论，老板也喜欢看，大家都开心
* 新室友是个社牛。
* 早上问了下写字楼楼下的保安，我所在的这个2号楼，每天上班的人数大概在1000左右。
* 高驰的表带贵是贵，舒服也是真舒服。
* 尝试用佳明训练制定了一个跑步计划，4 个月后看看效果
* 环球港也太大了，体验超大型商场需要充足的体力。



