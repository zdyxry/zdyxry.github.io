---
title: Weekly Issue-《疯滑雪月》
date: "2026-05-24:00:00.000Z"
slug: "Weekly-Issue-Ski-Moonstruck"
tags:
  - Weekly
description:
---

## 文章

### 技术


[Anthropic acquires Stainless \\ Anthropic](https://www.anthropic.com/news/anthropic-acquires-stainless)

[[Anthropic]] 收购了 [[Stainless]]，[[Stainless]] 从成立开始就是盈利的，[[OpenAI]] 和 [[CloudFlare]] 接下会用其他产品替换么，感觉尬住了。

---

[Your Slop, My Sludge](https://justingarrison.com/blog/2026-05-19-your-slop-my-sludge/)

> You are still responsible for the quality of your output. There used to be a cultural standard: if I created crap, my work was crap.

---

[Linux is getting a security wake-up call - why it was inevitable and I'm not worried | ZDNET](https://www.zdnet.com/article/linux-security-wake-up-call-copy-fail-dirty-frag-why-inevitable/)

> As Microsoft announced in a blog post, "Today, more than [two-thirds of customer cores in Azure run Linux](https://opensource.microsoft.com/blog/2026/05/18/from-open-source-to-agentic-systems-microsoft-at-open-source-summit-north-america-2026/), and the platforms running Microsoft 365, GitHub, and OpenAI's ChatGPT all sit on Linux foundations. When ChatGPT scales across more than 10 million compute cores worldwide and serves a billion queries a day, Linux and Kubernetes are what make that possible."

[[Microsoft]] 发布 Azure Linux 4.0，基于 [[Fedora]] 迭代，还有 Azure Container Linux ，基于 [[Flatcar]] Container Linux 迭代。前者已经搞了几年了，后者为啥没考虑基于 Fedora CoreOS 来迭代呢？毕竟维护 Azure Linux 那一堆 Spec 可不是什么轻松活，复用基础 RPM 带来的优势还挺明显的。

一个可能的原因是 [[Microsoft]] 收购 [[Kinvolk]] 团队之后，已经基于 Flatcar Container Linux 有了很深的路径依赖了，现阶段强制引入可能没什么必要，自家产品后续迭代控制起来方便，不用看 [[RedHat]] 眼色。

看了下 [[Kinvolk]] 博客，最近一年的所有博客都是和 [[Headlamp]] 相关。

---

[打造适合自己的 AI Harness 工程：从开发流、E2E 测试到自动排障 · 跬步](https://zhu327.github.io/2026/05/09/%E6%89%93%E9%80%A0%E9%80%82%E5%90%88%E8%87%AA%E5%B7%B1%E7%9A%84-ai-harness-%E5%B7%A5%E7%A8%8B%E4%BB%8E%E5%BC%80%E5%8F%91%E6%B5%81e2e-%E6%B5%8B%E8%AF%95%E5%88%B0%E8%87%AA%E5%8A%A8%E6%8E%92%E9%9A%9C/)
[软件基本功没死，它在 AI 时代变得更值钱了](https://archive.is/vdQBy)

`/grill-me [客户需求文档]       -- 与 AI 建立共同的设计概念`  grill-me 这个动作绝对不能省：
> 以无情审问的方式采访我，直到我们达成共识。逐一追究设计树的每个分支，一个一个地解决依赖关系。对每个问题提供你的推荐答案。每次只问一个问题。

---

[Livin’ Kubernetes on the Immutable Edge with Kairos Project](https://www.spectrocloud.com/blog/livin-kubernetes-on-the-immutable-edge-with-kairos-project)

> But there are very important differences: Kairos is distribution-agnostic, Open Container Initiative (OCI)- based and [cloud-init](https://cloud-init.io/) first. Let’s take a look at what this means

[[Kairos]] 的理念是不感知发行版、OCI-Based、Cloud-init 优先。 `distribution-agnostic` 设计理念很好，在 systemd 的启动阶段引入了 `immucore` 来做 `rootfs` 的配置确实是一种方式。

对于一个需要支持多个发行版的产品来说，是否可以参考 Kairos 来改造一下，将产品发布物料统一为 OCI Image，启动阶段自动根据决定使用哪个 Image ？但是跨版本的服务配置可能不好处理，只能依赖于 hook 机制来修改配置文件？

另外 Ettore Di Giacinto 这个人的开源维护方式还挺有意思的， 开源的”产品“是在 Org 下的，但是”产品“的核心依赖是在个人账户下的，比如 Kairos 的核心配置方式 [GitHub - mudler/yip: Yaml Instructions Processor - Simply applies a cloud-init style yaml file to the system · GitHub](https://github.com/mudler/yip) 是挂在个人账户下的，之前在 [[Rancher]] 时期的 Elemental toolkit 的核心依赖 [GitHub - mudler/luet: :package: 0-dependency Container-based Package Manager using SAT solver and QLearning · GitHub](https://github.com/mudler/luet) 也是挂在个人账户下的。

---



### 生活

[我的欧洲生活 英国和爱尔兰 | 土豆不好吃](https://dmesg.app/europe-uk-ie.html)

> 大英博物馆里有很多展品，可能展品知名度赶不上卢浮宫，毕竟二者定位不同。卢浮宫的定位是 “西方艺术顶级收藏”，所以能看到非常多的名画；大英博物馆则是，我要把你的整个文明都搬过来，所以基本上有很多石头、陶片啥的。

---




### 书影播客


《疯滑雪月》，邱月单口专场，之前没看过她之前的综艺段子，听说今年再一次被淘汰了。真正的吉林人，吉林省吉林市人，东北话听着很亲切，东北人讲段子的节奏有些共同点，就是会阶段性的重复一个段子的最后一句，印象中子龙也是类似的。这个专场讲的是她的两段主要的职场：建筑工地和滑雪教练，中间穿插着去新西兰打工度假的经历，笑点没有想象中密集，更多的是对经历的自我开解，有点像一个小姨跟你讲述自己年轻时候的故事，小时候的你可能听的嘎嘎乐，长大之后再听就难免想到更多。



## 碎碎念

* 极度贫瘠的同理心和狭隘的认知。
* 本周尝试：将所有的 kimi 入口从 CLI 换成 web。
* review 了一个技术方案，deepseek-v4-pro 花了 2 毛钱。
* 对 postinstall 真是又爱又恨。
* 2026年，我还能看到有人在路边卖假表“表要不要”
* 光荣在于平淡，艰巨在于漫长。光荣个屁，艰巨个6啊。
* 爱数破产了。
* 胆结石变大了 ，11mm -> 13mm，按照这个速度，开刀不可避免啊。
* 昨天和朋友吃饭，聊到在办公室政治中被搞的很烦，感觉如果完全不了解甚至抵触，很容易吃亏。
* kimi-code 的 token 消耗速度要比 Kimi-cli 快不少，不知道是不是体感错误。
* 朋友的生日庆祝方式是徒步 100km，体力不好整不了这个。