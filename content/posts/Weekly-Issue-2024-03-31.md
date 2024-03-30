---
title: Weekly Issue 2024-03-31
date: 2024-03-31
tags:
- Weekly
description:  清明假期。
---


## 文章

### 技术


[The RedMonk Programming Language Rankings: January 2024 – tecosystems](https://redmonk.com/sogrady/2024/03/08/language-rankings-1-24/)

[[RedMonk]] 2024/01 语言排名，[[Golang]] 从 16 位上升到了 12 位，TypeScript 从 7 位上升到 6 位，随着对类型安全的看重，后续可能继续上升。

---

[Autonomous hardware diagnostics and recovery at scale](https://blog.cloudflare.com/autonomous-hardware-diagnostics-and-recovery-at-scale)

[[CloudFlare]] 讲述如何管理服务器故障，这套系统叫 Phoenix，包括：自动发现、诊断、重新置备等动作，由于该工具是完全自动化的，所以合理的展示当前的工作状态非常重要，要保证可以清楚的了解当前在执行哪些动作。同时为了防止服务器短时间再次故障，设置了 Error Budgets，如果服务器故障超过先定额，那么就不会尝试恢复它。

- 周期性的扫描数据中心中异常的服务器
- 进行诊断，诊断是通过将待处理的服务器重新引导到特定的 Image 进行运行，并将运行结果保存，诊断动作包括
	- 带外连接检查
	- 节点验收测试，实现了一个内部工具  INAT (Integrated Node Acceptance Testing) ，该工具会运行各种测试用例，如 CPU、内存、存储等等。
- 恢复尝试
	- 将通过诊断的服务器重新置备
	- 置备成功后，重新标记起可用
- 手动修复
	- 如果诊断失败，后置备失败，则需要人工介入进行修复

---

[X 上的 妞和其他8964人觉得很赞：“这几天真的是被开源拖拉机创死了，metal3 的文档真的是比红帽的文档还烂上一百倍 红帽的文档是全但是无序，有时候做事情之前多往后读读可以节省好多后悔的时间 metal3 的文档不仅不全，而且差不多相同的事情在三篇文章里都在讲，每篇文章的做法都有一点点不一样……” / X](https://twitter.com/niuniu_8964/status/1772626798422982686)

关于 [[Metal3]] 的吐槽：文档质量、代码质量都不太行。

---

[coreDNS is going to fail you scale k8s | Faris | Medium](https://medium.com/@mohamedfaris2/coredns-is-going-to-fail-you-scale-k8s-2d5d9f14bc12)

[[kubernetes]] 900+ 节点，15k+ pod 的环境中，因为默认的 coreDNS 不足以支撑这个量级的请求，导致服务崩溃。建议为 coreDNS 配置 HPA，并针对内部关键组件进行监控。

---

[Everything I know about the XZ backdoor](https://boehs.org/node/everything-i-know-about-the-xz-backdoor)

[[xz]] 后门历史介绍，2021 年 Jia 创建了 Github 账号，2022 年 xz 缺少 maintainer，Jia 进行了提交并成为 Contributor，随后 Jia 逐渐成为 xz 的主要维护者。随后有一些其他的 Github 账号提交了带有后门的 PR，并有一些可以的账号推动带有后门的版本合并到主流的发行版中。

---






### 生活




## 书影

《香港旅游完全指南》，2010年的书，不知道里面有多少信息是过时的，等实际感受一下。


## 碎碎念

* 如果做一件事的成本不高，那就先行一步再说。
* 《孙子兵法》的英文名是《The Art Of War》
* Gemini 的幻觉有点严重， Claude Haiku 好不少
* 
