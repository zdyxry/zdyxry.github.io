---
title: Weekly Issue-回家过年
date: "2026-02-08T00:00:00.000Z"
slug: "Weekly-Issue- 回家过年"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Seven Years of Firecracker - Marc's Blog](https://brooker.co.za/blog/2025/09/18/firecracker.html)

感觉在 [[Agent]] 时代，[[Firecracker]] [[MicroVM]] 会越来越流行的，好像还没看到很多人使用的本地 [[Sandbox]] 项目。

看到另一个使用 [[Firecracker]] 的是： [GitHub - HACKE-RC/Bandsox: Sanboxes for AI agents and humans](https://github.com/hackE-RC/bandsox) 。

我自己用 [[libkrun]] 搞了一个sandbox，越搞越觉得，我可能要先想清楚我到底需要什么样粒度的隔离，我当前设想的是：
- 自动创建 repo 的 worktree，将 worktree 映射到 sandbox 的 /workspace 目录
- 映射当前主机的 UID/GID 到 sandbox 内部，保持权限一致；
- 只读方式映射 $HOME 目录到 sandbox 内部，保持用户配置文件可用；

但这样会有一些问题，都需要细粒度处理：
- 很多工具需要依赖于 $HOME 目录可写，比如 kimi-cli 需要在 `$HOME/.kimi/logs` 目录下写日志文件，$HOME 整体只读就有问题；
- 如果 [[Git]] 仓库在 $HOME 目录下，那么在 worktree 中修改文件想要提交时，又会遇到文件权限问题；

还是再看看一些已有的 [[sandbox]] 项目是怎么实现的，再结合自己需求搞。

---

[Life pro tip: a Steam Deck can be a bluetooth speaker - Xe Iaso](https://xeiaso.net/notes/2026/steam-deck-bluetooth-speaker/)

使用 Steam Deck 蓝牙连接其他的设备（笔记本/手机），由 Steam Deck 作为一个 Hub 来聚合输出。这绝对是一个可能有用的 tip。


---

[An Update on Heroku](https://www.heroku.com/blog/an-update-on-heroku/)
[An Update on Heroku | Hacker News](https://news.ycombinator.com/item?id=46913903)

[[Heroku]] 这个声明，是说完全不接收新的企业客户了？产品进入维护阶段，就到此结束了（可能早就结束了。

[[hacker news]] 评论区有前员工站出来说，是因为技术债和产品愿景不清晰，和 [[Salesforce]] 关系不大。评论区的另一句话太真实了，共勉：“Over time sales targets get met, but the product doesn't advance. By the time all existing customers that can convert have converted, the product is no longer competitive. Like bankruptcy, it comes gradually, then suddenly.”

---

[mistermorph 的 Agent 安全开发札记 | 歌词经理](https://blog.lyric.im/p/mistermorph-agent-security-development-notes?utm_source=twitter&utm_medium=social&utm_campaign=newsletter)

`auth_profile` 的安全机制感觉可以借鉴下，多层白名单控制，无需 [[MCP]] ，在 agent 层面就要求用户对所有的 [[SKILL]] 进行审查。还有 `guard` 关键词和脱敏机制来兜底。

---



### 生活

[腹股沟疝从发现到治疗（门诊确诊篇） | So!azy](https://blog.solazy.me/20260128/)

[腹股沟疝从发现到治疗（日间手术篇） | So!azy](https://blog.solazy.me/20260205/)

生病之后，还能保持冷静的分析太难得了，也可以看到 [[AI]] 在这种时候，会有不小的帮助。

---

[一个老牌机场的倒下…](https://t.me/gebaopiCloud/3555)

这是这周最头痛的事情，影响范围比我想象中要大很多，开发机、家里环境、自动化配置、全部收到了影响。可以说是完全瘫痪的状态，心情难免急躁。平静的生活总会出点意外。

---



### 书影播客

《其主之声》，波兰作家莱姆的作品，最近看到了很多次推荐，在回家飞机上读的，刚读了 4 章，前言就很有趣。


## 碎碎念
* 现在是上海的 2 月，野人先生（冰激凌）还在打广告，这个创始人不会是个东北人吧
* Docker sandbox 是 Desktop only 的。也可以理解。
* 聚酯纤维真好
* 工作 [[Slack]] 上发低俗的东西，自以为很幽默，素质有待提高。
* [[ampcode]] 最近 30 天，按照他们的计费使用了 $49，真不错。
* 感觉股四明显结实了很多。
* 感觉Strava 关注的几个人都可以在上班时间去跑步，神仙工作（我好像也可以）。
* 清理了微信联系人，N 年没联系的都删了。
* 一觉醒来，kimi-cli 用 [[Rust]] 重写了。
* 信息安全问题是意识形态冲突么？
* 年度抽奖，颗粒无收
* 春节回家机票 1620.
* [[openclaw]] 的热度一周就下去了，很多人意识到自己根本没有那么多场景，真正使用的人是少数。
* 看到了一个识别模型能力的方法，喂给他哈利波特全集，提取所有的魔咒。
* 太难了，人情世故太难了。
* 看着微信发的 “QQ 经典农场”，一阵恍惚。
* [[agentfs]] 期望的是 agent 工作完成后直接提交远端，不干扰本地的代码仓库，这样对么？
* 地铁站看到了吊牌不摘的人👀
* 火葬场开后门：专烧熟人。