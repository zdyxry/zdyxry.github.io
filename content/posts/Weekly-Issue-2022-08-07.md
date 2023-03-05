---
title: Weekly Issue 2022-08-07
date: 2022-08-07 23:59:00
tags:
- Weekly
description: 记录一下自己每周读过的文章，看过的电影，阅读过的书籍。
---


## 文章

### 技术

[2022-30: 如何维护一个开源项目](https://xuanwo.io/reports/2022-30/)

明确自己的项目预期，后续的发展路线以及如何与开发者沟通。

---

[How Our Bare Metal Cloud Keeps up with All the New OS Releases](https://thenewstack.io/how-our-bare-metal-cloud-keeps-up-with-all-the-new-os-releases/)

[[Equinix]] 如何进行发行版的快速验证工作的介绍。之前一直是手动测试验证(无法想象)，现在通过 [[BuildKite]] ，通过 DSL 来描述 OS 内容，使用 [[virt-customize]] 来进行配置改动，改动完整后，推送到 S3，进行自动化测试，最终推送给客户。

采用 [[Buildkite]] 的原因：

- 支持动态 pipeline，可以进行条件判断
- 允许 pipeline 进行交互输入
- 可以自定义运行形态(环境)
- 不同架构可以共用一套 Pipeline

[[BuildKite]] 学习成本不低。

---

[程序 Hot reload config 的实现方式](https://www.kawabangga.com/posts/4756)

- 监听文件(我自己比较常用的方式)
- 每次都reload
- 监听HUP 信号

---


[10 Kubernetes Security Context settings you should understand](https://snyk.io/blog/10-kubernetes-security-context-settings-you-should-understand/)

关于 [[kubernetes]] 安全配置的一些方法(感觉大部分人都用不上)

---



[The people of the cloud](https://aeon.co/essays/downtime-is-not-an-option-meet-the-stewards-of-the-cloud)

云计算的另一个视角：工作在 IDC 的人们

---

[How the 1Password CLI makes DNS management easier](https://blog.1password.com/1password-cli-easier-dns-management/)

使用 [[1Password]] 配合 [DNSControl](https://stackexchange.github.io/dnscontrol/) 管理域名

---

[Using Firecracker and Go to run short-lived, untrusted code execution jobs](https://stanislas.blog/2021/08/firecracker/)

使用 [[Firecracker]] 来运行一些短生命周期的不可信任务。预先置备了VM pool，通过在 VM 中运行 Agent 来接收 Job，Job 执行完成后 VM 销毁，会自动置备新的 VM 加入到 VM pool 中。

---

[libyear](https://libyear.com/)

我们经常面对维护的项目依赖老旧的情况，平时很少去主动的更新依赖，当等到不得不更新的时候，通常要投入的精力非常大。其中我觉得一个比较重要的原因是我们无法评估当前项目的依赖管理是否处于一个相对”健康“ 的状态， [[libyear]] 提出通过一种可以量化的数字来检查当前项目的依赖情况，通过比较项目中每一个依赖当前版本与最新版本的发布时间差值之和，来评估项目状态。

按照 libyear 的算法，项目中的依赖越多， libyear 越大，感觉 libyear 可以作为一个参考，实际应用选择一个比例值比较好，比如平均依赖年限小于 3 ？

---

[ICMP, Ping, and Traceroute - What I Wish I Was Taught](https://xkln.net/blog/icmp-ping-and-traceroute--what-i-wish-i-was-taught/)

关于 [[ICMP]]， [[Ping]]， [[Traceroute]] 的实验和解释。

---

[The Many Jobs of JS Build Tools](https://www.swyx.io/jobs-of-js-build-tools)

关于前端构建工具的介绍

---

[Why does nobody seem to know what imperative and declarative actually mean?](https://leebriggs.co.uk/blog/2022/07/20/nobody-knows-what-declarative-is)

关于[[声明式]] 和 [[命令式]] 的讨论。**命令式有[控制流](https://en.wikipedia.org/wiki/Control_flow)，而声明式没有。**




### 生活



[有氧运动真的会掉肌肉吗？](https://daily.zhihu.com/story/9751345)

**总结起来，[[有氧运动]]对肌肉的抑制，除了总热量因素外，还应该补充的几个层面是：**

- 有氧运动消耗了的大多是糖，而不是脂肪；
- 糖类不足，会激活 AMPK、抑制肌肉合成；
- 糖类不足，人体分解肌肉（糖异生）来获得糖，用糖类配脂肪氧化，从而获得能量维持生存。

---

[9个写作技巧](https://twitter.com/coolXiao/status/1554667451203276801)

- 删掉“我觉得”，“我认为”，“我相信”，写出来的本身就代表个人观点，不需要重申
- 先写标题，写了标题就有了主旨，不会发散
- 短句很好，但是可以长短结合(虽然我还是觉得断句更好)
- 三合音，不经意的押韵可以起到奇妙的效果
- CTA：call to action，告诉读者如何行动
- 一寸相框：先写下眼前已经明确的，最想说的电子，不需要考虑全文最后的呈现
- 简单和清晰
- 不说副词，不要用副词描绘情势，用更生动的叙述替代
- 填满画布，在写草稿时，应该一鼓作气，先填满画布

---