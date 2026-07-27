---
title: Weekly Issue-《八仙》
date: "2026-07-26:00:00.000Z"
slug: "Weekly-Issue-all-wishes-come-true"
tags:
  - Weekly
description:
---

## 文章

### 技术


[Shipyard: How We Built Slack's Next-Generation EC2 Platform | Engineering at Slack](https://slack.engineering/shipyard-how-we-built-slacks-next-generation-ec2-platform/)

[[Slack]] 介绍自己如何维护自己的 [[EC2]]，需要对他们的 Infra 有持续的了解才能更好的理解这篇文章。他们有数万个 EC2 实例，他们之前面临的问题就是服务部署管理、Infra 的配置漂移、跨层级变更（不知道是什么意思），他们有很多业务还是没办法迁移到容器上。

他们打造了 Shipyard，下一代 EC2 管理平台，解决问题的方式从配置管理改为了构建管理。支持多架构和多 OS，维护一个 Golden base image，其他服务基于这个 base image 来构建自己的 Image。之前他们会用 Chef 来检查系统配置、服务配置，如果发现有漂移则强制重置，现在选择相信 Image 构建阶段内置的配置，配置更多的是服务部署涉及到的少量配置。每个 EC2 都有有限的生命周期，定期自动轮转，保证实例配置是符合预期的，重建替代了原地更改，减少了配置漂移的风险。对于特殊情况，平台还是允许对实例进行配置变更的，等待上层的 Golden Image 更新之后，所有的下游服务自动更新，更新完成后，实例重建，配置漂移清除。 

查到了一个知识点：在读这篇文章的时候，就感觉 Slack 对 AWS 的组件依赖非常深，可以说是脱离了 AWS 就玩不转的状态。原来AWS 内部使用 Slack 办公的，Saleforce 和 Amazon 有深度合作，所以不需要考虑是否要跨云的问题，能用 AWS 就用 AWS，没毛病。

---

[Is a Pod the right deployment unit for an AI agent? | CNCF](https://www.cncf.io/blog/2026/07/14/is-a-pod-the-right-deployment-unit-for-an-ai-agent/)

[[kagent]] 觉得 Pod 在 Agent 场景下不好，虽然解决了隔离、网络策略等问题，但是资源利用率低、启动速度慢，他们选择建一个 pod pool，在一个 pod 内部运行 actor (agent)，actor 靠 gVisor 进行安全隔离。同一时间一个 pod 内部只跑一个 actor，actor 的资源隔离继承自 pod。

---

[Protecting our FLOSS commons from LLMs — Codeberg News](https://blog.codeberg.org/protecting-our-floss-commons-from-llms.html)
[Codeberg Divides | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2026/7/24/codeberg-divides/)

> However, we also need to be honest about certain use cases that might no longer be welcome on Codeberg. If you see yourself on this list, you don't need to move right away, but there might be [other places that better fit your needs](https://docs.codeberg.org/getting-started/what-is-codeberg/#alternatives-to-codeberg):
> - Projects that are created by LLM "agents" in autonomous ways
> - Projects written and maintained with heavy use of LLMs

不要试图用 [[Codeberg]] 作为 [[GitHub]] 替代品，基建规模不在一个量级，且作为一个非盈利性组织，注定在后续的功能/稳定性迭代上会慢一些的。

---

[mention-file-myth-in-code-agents](https://buzhanxian.vercel.app/posts/mention-file-myth-in-code-agents.html)

关于各个 Coding Agent 中 `@` 操作符的调查，其中 `pi`, `opencode`, `gemini-cli`, `grok-build` 会读取完整的内容，如果超出单次上限则自动忽略，`codex` 只发送文件路径，不发送文件内容。"The complexity was for my own satisfaction, not the model's."

---

[多实例启动的 bootstrap 并发问题：从悲观锁到 upsert | Chaney's MoonBook](https://chaneyzorn.github.io/codes/bootstrap-seeding-concurrency/)

> **绑定底层数据库选型**。`GET_LOCK` 是手写的 MySQL 方言，没有任何抽象层。PostgreSQL 虽有 `pg_advisory_lock`，但名称、语义、超时行为都不同，日后要兼容就是债务。

关于是否可能会存在兼容场景，我最初是老老实实抽象，后面总是在想，几乎不可能换 DB，不抽象也没事，现在又变成了，按照现在的国产化趋势没准一些信创场景真的需要换。

---

### 生活

[大模型是专利期十个月的制药生意](https://x.com/xleaps/status/2080660249145459052)

> DeepSeek 的 API 定价标准是：买一批设备回来，十个月收回成本。也就是十个月赚来的利润可以覆盖硬件上的投入。
> 十个月之后，你就完全不能以发布时的价格来收费了。这是竞争和产业链使然，你不降价，模型就不再有吸引力了。所以十个月看上去是一个选择，实际上不是一个选择，是一个由产业节奏反解出来的约束。你模型的回本周期必须短于溢价窗口。否则当你设备还没回本，定价权已经没了，这笔投资就不成立。

---

[Zero sum games · rakyll.org](https://rakyll.org/zero-sum-games/)

> The technologies that matter end up being commodity.

---

### 书影播客

《八仙！》，英文名《All Wishes Come True!》，工整的爆米花商业片，我觉得挺好看的，可能会被说公式化：主角遇到困难、拉帮结派、贵人相助、反派降智、结束反转。我就是带着这个预期来看的，所以我会推荐朋友去看。 八仙有八个人，感觉导演编剧控制不住剧情细节，部分主角团的角色定位非常的工具化，有和没有都无所谓。电影结束的时候，旁边有人说是在学习《哪吒》卖腐，我觉得不是影视本身卖腐，而是现在这个背景，很多观众会代入卖腐的情绪。《士兵突击》 也就是播出时间早，加上剧情本身的荣誉感和集体主义，大部分人会避讳，但还是有大量的 CP 粉在持续的讨论，躲不开的。


## 碎碎念

* ScyllaDB 的创始人是 KVM 创建者。
* 东北话科普：上海今天下雨的猛烈程度，可以说“下冒烟了”
* https://wplace.live/ 真的是很适合探索发呆。
* “想爸爸的时候，你就是个孩子。”
* 忙到疯狂。
* 看到 uncloud 作者对 https://zitadel.com/ 评价很高。
* 跑步中途被 oncall 电话中断了，太影响兴致了。
* 我好像发现了 raft/multica 的正确姿势了，我不应该妄图每个 issue 都进行详细的描述，期望它能够直接达到最终的效果，应该让 issue 先自行探索问题和方案，然后我再来介入。
* Notion 最近的一些更新我都看不太懂。
* IaC 场景下：VM 在创建 snapshot 时对应一份旧状态 S1。之后用户把 VM spec 改成 S2。如果此时 rollback snapshot，vSphere VM 会回到 S1。问题是：声明式配置里现在还是 S2，那么 rollback 后到底谁是 source of truth？
