---
title: Weekly Issue-《疑犯追踪》
date: "2026-03-15:00:00.000Z"
slug: "Weekly-Issue-POI"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Agent 原生系统通知实现总结（Claude、Codex 等）](https://www.linw1995.com/agent-native-system-notifications/)

> 通过 **OSC 9**（Operating System Command sequences，操作系统命令序列）来触发系统通知

```bash
tty="$(tmux display-message -p '#{client_tty}' 2>/dev/null || true)"
printf '%b' "$(printf '\033]9;%s\a' "This is the notification text")" >"$tty"
```

好东西，解决了一个小困扰，日常远程开发，经常要执行完长时间命令的时候希望能得到一个通知，现在可以用 OSC 9 来实现。

----

[一个观察：实锤MacOS真的会偷跑流量 - 陪她去流浪](https://blog.twofei.com/2279/)

> 这玩意儿的输出倒是非常的清晰明了，一眼就看出了哪个进程在跑流量：其中一个名为“idleassetsd”的进程（现场已破坏）。但是……搞笑的事情出现了：此进程在活动监视器里面不存在，是一个被系统隐藏了的进程！（无论是按名字搜、还是 PID 排序后人肉搜。）

原来 [[MacOS]] 的“活动监视器”不能看到所有进程信息。

---

[Analyzing first-party fraud trends: Account, free trial, and refund abuse](https://stripe.com/blog/analyzing-first-party-fraud-trends-account-free-trial-and-refund-abuse)

>  In fact, AI startups that offer free trials with self-serve sign-ups and direct API access see 10x more attempted abuse than enterprise AI solutions.

[[Stripe]] 发布了 Radar 产品，用来检测用户支付方式是否存在滥用的行为，滥用包含：同一支付方式注册多个账号、重复申请试用、使用盗刷信用卡。根据 Stripe 的分析，AI 公司 7.4%的客户注册涉及多账户滥用。

还是绕不开的话题，传统 SaaS 的毛利率是很高的，获客成本的边际成本趋近于 0，滥用也就滥用了，至少账面上的数据是好看的； AI 公司的毛利率不高，每一次调用的算力成本是实打实的，每一次滥用都会直接放血，相应的获客方式也一定会发生改变。

---
[Anduin的CQE定理：为什么大型组织的采购永远在买电子垃圾 - Anduin Xue](https://anduin.aiursoft.com/post/2026/2/24/cqe)

嗯， **Nobody ever gets fired for buying IBM** 。

---


[对exec.Cmd.CombinedOutput的一点研究 - 陪她去流浪](https://blog.twofei.com/2280/)

```go
type Cmd struct {
	// If Stdout and Stderr are the same writer, and have a type that can
	// be compared with ==, at most one goroutine at a time will call Write.
	Stdout io.Writer
	Stderr io.Writer
}
```

虽然但是，我不喜欢（主动禁止）使用 CombinedOutput。

---

[Software companies buying software: a story of ecosystems and vendors · Erik Bernhardsson](https://erikbern.com/2026/02/25/software-companies-buying-software-from-software-companies.html)

[[Modal]] 老板的文章：越来越多公司倾向于从“自建”转向“采购”，公有云是这一切的起始，经济原因会让安全合规让步，vendor 通过向更多的用户提供解决方案，来更好的专注于解决单一问题，初创公司起步更快但利润率变低，要想将软件卖给客户，和客户离得近优势比想象中大。

---
[为什么现有的 Agent Infra 无法支撑生产级应用？](https://medium.com/@guanlan/%E4%B8%BA%E4%BB%80%E4%B9%88%E7%8E%B0%E6%9C%89%E7%9A%84-agent-infra-%E6%97%A0%E6%B3%95%E6%94%AF%E6%92%91%E7%94%9F%E4%BA%A7%E7%BA%A7%E5%BA%94%E7%94%A8-2191cec885df)

> **Agent 的执行是概率性的、长程的、带状态的。它的决策路径不可复现，副作用不可撤销，而且运行时间长到崩溃是统计必然**。   
>  **设计目标不应该是保证机器不挂，而是在故障发生时保住执行语义的正确性。**    
>  **Infra 不应该追求模型永远正确，而是让模型的错误变得可预测、可隔离、可挽回。在模型的不可预测性周围画出确定性的边界，用系统的确定性收敛模型的不确定性。**

读着读着确实想到了 [[Temporal]] 是否解决了部分问题，文章也解释了为什么不行：

> - 第一，**Temporal 的容错依赖 replay 机制，前提是代码是确定性的**。LLM 崩溃后重放，会走不同的决策路径。你必须把每次 LLM 调用的结果全部缓存，replay 时直接返回缓存结果。这时候你实际上是在 Temporal 之上自己实现了一套状态机，Temporal 的 replay 机制反而变成了额外的约束成本。
> - 第二，**Temporal 的最根本的基础假设，是代码逻辑本身是可信的，只是 Infra 会出错，比如网络抖动、进程崩溃、机器故障等**。但 Agent 的问题是 LLM 输出本身不可信，Temporal 会忠实地执行一个 prompt injection 攻击，因为从它的视角看，这就是 workflow 的正常逻辑。这意味着需要在 Temporal 的执行模型之外，独立构建类似 Capability Gateway 的能力隔离层 ，但 Temporal 没有这层预留集成点，它的 activity 边界是执行边界，不是信任边界。你需要自己在两套系统的接缝处维护一致性，而这个接缝处恰好是攻击面最大的地方。


---




### 生活

[蔚来季度盈利省钱措施\_新浪新闻](https://web.archive.org/web/20260313012055/https://www.sina.cn/news/detail/5275666425839882.html)

> 牛屋的绿植从每周一换的蝴蝶兰，改成便宜的绿球花，最后干脆开始使用不需要更换的假花；     
> 2023 年，蔚来为 3 万名员工累计举办了大大小小的 1740 场团建活动，到了 2024 年，这类活动骤减到全年 28 场，2025 年继续取消兴趣社团的活动经费；

不容易，都不容易。

---

[我也被北京呕吐了出来 | 螺莉莉的数据中心](https://roriri.one/2026/03/10/beijing-vomit)

> 随着就业市场不断的萎缩，很多难称行业翘楚的人都纷纷离开了这座城市，但是整个大环境就是这个鸟样子。这种经济的萎缩就像这座城市的胃不舒服一样，它一使劲就会把居民呕吐出去，从三环呕吐到四环、从四环呕吐到五环、或者直接喷回老家。    
> 从这个角度来看，这座城市对于外来人口没那么友善。这和上海那种本地人瞧不起外地人的不友善不一样，北京给人一种它公平地漠视所有人，没有任何情感，没有热情也没有厌恶。

回看我离开北京的决定，无论是从各个方面来评估，都无比正确。

---
[Kai丨【2025年眼镜的选择全攻略】v1.0.3 - 搞七捻三 - LINUX DO](https://linux.do/t/topic/103275/38)

又是一篇[[眼镜]]选购指南，感觉每一年或两年更换一次眼镜，对生活幸福感提升还挺明显的。

---
[肾结石的一周 | Oilbeater 的自习室](https://oilbeater.com/2026/03/15/kidney-stones/)

> 但凡看过就能发现后腰从上到下只有一个泌尿系统，但凡后腰疼大概率是肾的问题。    
> 我看有的疼痛等级指数介绍肾结石已经是最高级了，能和自然分娩坐一桌，想到可能还有一周整个人是崩溃的。当时都想直接去手术取出来了，不过想了想手术还是有创伤，理智战胜了冲动，还是打了针止痛回家了。

 大家多喝水，多运动。

---


### 书影播客

《疑犯追踪 第一季》，POI，2011 年播出的美剧，单元剧，即使不是连续观看，也不影响理解。讲述的是911 事件后，美国政府让一个纽约的亿万富翁，开发了一个 AI 系统，能够通过监控摄像头、电话记录、信用卡交易等数据进行分析，预测即将发生的犯罪事件。主角团负责营救的故事。

主角特征是传统的宅男加硬汉的组合，完美符合“美强惨“设定。2019 年的英剧《真相捕捉》还停留在监控视频的篡改，deepfake，2011 的 POI 是直接让 AI 来预测犯罪。站在 2026 年看 POI，大家一直谈论 LLM，理论上 POI 中的功能都已经实现了：全局监控识别，数据监听，行为预测。



## 碎碎念

* 居然有人在办公室茶水间吸电子烟，真是傻逼
* 安可舞台唱舞曲，真的需要信念感。
* 当下针对任务类型人工 route 模型是绝对必要的，无条件的 opus 只会耽误事啊。
* 难得的好天气
* 如何更好的应对利旧带来的潜在问题。
* 吃的少就跑不动。
* 一怒之下，怒了一下。
* 用 AI 得到的错误结论直接发给其他人，希望自己不要变成这样。
* 龙虾在各个 thread 里面满天飞，烦死了
* 我不是什么原教旨主义老古董，非要说 Slack的含义是："Searchable Log of All Conversation and Knowledge"。从事实角度， 在 Slack 你能搜到所有的事情上下文，一个功能的需求讨论，设计方向，细节确认，最终呈现，都能找到。   
现在各种 Bot 接入并侵入 Thread，就对其他人产生了极大的干扰，本身随着产品越来越复杂，一些 Thread 的讨论量已经不适合阅读了，此时再穿插着一些 Bot 的回复，至少从我的角度看完全没有任何的帮助。    
你自己用没问题，DM 用呗，没人在意。我甚至觉得这是基本的社交礼仪问题。     Vibe 了一个浏览器插件，自动模糊处理所有的 Slack bot 消息，支持 Bot 白名单： https://github.com/zdyxry/slack-anti-bot 
* 再买书籍盲盒，我就是狗。
* 我不怎么用 skill，是因为我觉得在现在一个“体力活”成本无限低的场景下，做一些以前觉得很“苦”的事情，哪怕看上去有些笨，但是也很有效。
* 线下看到了宇树机器人的宣传册，这么一个高集成度的机器人，保修期只有 8 个月，这让用户怎么买？
* 可怕的不是 AI 无法提效，而是老板认为你可以借助 AI 提效。
* GPT-5.4 口头禅：我不想靠猜。