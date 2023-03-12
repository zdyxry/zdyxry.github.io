---
title: Weekly Issue 2023-03-12
date: 2023-03-12
tags:
- Weekly
description: 疲惫的一周。
---


## 文章

### 技术

[苹果：为了安全让 M2 吃灰 | 程序员的喵](https://catcoding.me/p/apple-perf/)

[[MacOS]] [[SIP]] 严重影响性能。

> **简而言之 `SIP` 会在我们跑任软件之前，把你的执行文件做一个校验和，然后通过网络请求发送到让人敬畏的苹果服务器，就是为了检测是否是恶意软件！**[谈谈我对 ChatGPT 应用的 prompt 的看法 |](https://reorx.com/makers-daily/004-prompts-and-parameters-transparancy/) 

---


[Python is two languages now, and that's actually great](https://threeofwands.com/python-is-two-languages-now-and-thats-actually-great/)

作者认为 [[Python]] 现在分为 **untyped Python** 和 **typed Python** ，并会永远的持续下去。最近公司的项目在从 [[Python2]] 迁移至[[Python3]] ，如果之后选择 library，那肯定会优先选择 type hints 的。

---

[The pains of GitOps 1.0 | Codefresh](https://codefresh.io/blog/pains-gitops-1-0/)

对于 [[GitOps]]管理的资源后续因为 auto-scale 等配置引发的不一致情况，[[Argo]] 通过[custom diff](https://github.com/argoproj/argo-cd/issues/2913) 来避免，[[terraform]] 通过 [ignore_changes](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle#ignore_changes) ，来避免。

---


[chdir to cwd: permission denied · Daniel Mangum](https://danielmangum.com/posts/runc-chdir-to-cwd/)

[[runc]] 在 [v1.0.0-rc93](https://bugzilla.redhat.com/show_bug.cgi?id=1934177) 的改动导致的 breaking change。在使用 `distroless/static:nonroot` 时，将用户设置为 `nonroot` UID 是`65532` ，并将工作目录设置为 `/home/nonroot` ，权限是 0700。
之前版本的 [[runc]] 会先 `chdir` 然后设置用户，在执行 `chdir` 的时候会以 `root` 来执行，所以不会因为权限而抛出错误。而 rc93 版本改为先设置用户，再 `chdir`，所以会遇到 permission denied 问题。runc 改动链接： [libctr/init_linux: reorder chdir · opencontainers/runc@d869d05 · GitHub](https://github.com/opencontainers/runc/commit/d869d05aba0fc2519060b3b20b679ac5a5068e78)
这个事情引发的另一个思考是，我理解 [[Crossplane]] 提供的产品已经是较为上层了，但是他们的客户遇到问题需要 OnCall 到 OCI 这一层，莫名的为我司 [[kubernetes]] 产品之后的运维成本担忧。

---

[5 production surprises worth investigating – Dan Slimmon](https://blog.danslimmon.com/2023/03/06/5-production-surprises-worth-investigating/)

日常遇到的偶发现象（问题），最后一定会在生产环境中遇到。
关注清单：Long running requests,Saturation,Crashes,Utilization spikes,Correlation between latency and throughput

---


[The SSD Edition: 2022 Drive Stats Review](https://www.backblaze.com/blog/ssd-edition-2022-drive-stats-review/)

> The Dell SSD (model: DELLBOSS VD) has zero failures for 2022 and has over 100,000 drive days for the year. The resulting AFR is excellent, but this is an M.2 SSD mounted on a PCIe card (half-length and half-height form factor) meant for server deployments, and as such it may not be generally available. By the way, BOSS stands for Boot Optimized Storage Solution.

我司一体机的型号之一是 [[Dell]] ，因为一些历史原因，所以[[DELLBOSS VD]] 只是用来做引导分区，平时完全没有读写，按照这个故障率，我们真的太奢侈了。

---

[垃圾腾讯云CDN：从入门到放弃](https://mp.weixin.qq.com/s/ANFnbDXwuhKI99fgYRZ9ug)

[[CDN]]预热需要回源请求，但是回源请求产生的流量需要收费，离谱。

> 听到这样的解释，我都要笑喷了。**我为什么买CDN？因为要省对象存储的流量钱。CDN 去刷新预热，这是云厂商自己系统内部的流量，为啥要挂在用户身上付费？但是你刷新预热一下，一下花掉了我直接走对象存储下载一年都用不了的钱。**


### 生活

[奇客Solidot | Google 失去了方向](https://www.solidot.org/story?sid=74149)

> 这是“广告”这个印钞机产生的自然结果，这台机器收入每年都在增长，从而掩盖了所有其它罪恶：没有使命，没有紧迫感，例外主义的妄想，以及管理不善。
> Google 狂热的关注风险，减轻风险胜于其他一切。每一行代码、每一次发布、隐性决定、协议的改变和分歧都是 Google 员工必须谨慎对待的风险。员工被困在一长串的审批、法律评估、绩效评估和会议中，创造力或真正的创新几乎没有空间。

---


[Reorx’s Forge](https://reorx.com/makers-daily/004-prompts-and-parameters-transparancy/)

提到了一些 [[Prompt]] 小技巧。昨天内部同事在 [[slack]] 接入了 [[ChatGPT]] ，在没有合适的 [[Prompt]] 情况下，几乎是不可用的。

---

[离婚推文合订本](https://disksing.com/story/divorce/)

提到了几次孩子让人觉得艰难，感觉更难是成年人，如果换位思考，我不知道拿什么来安慰自己。

---

[Planes aren't faster cars](https://about.sourcegraph.com/blog/planes-are-not-faster-cars)

> **If the time cost is so large that you’re never going to pay it, time-saving improvements are actually about making the effectively-impossible become possible.**

> **What’s exciting about time-saving improvements isn’t the time savings, it’s how they make the impossible become possible.**

---

[Q & A. Q：是不是因为你写的 eru 所以你对换 k8s… | by CMGS | Mar, 2023 | Medium](https://medium.com/@ilskdw/q-a-f6b68d074ef6)

> 搞技术，菜就是原罪，对于内源性产品的 Infra 来说，来自于外部驱动的产品负责人来做行不行，当然行，前提是你有产出，你落地了什么玩意降了什么本增了什么效又自动化了啥，否则，别什么斯坦福 MIT六边形，你就是菜

---



## 书影

《模范出租车 第二季》，剧情延续第一季故事，引入了第三方势力，格局大了。

《网络谜踪2》，模式与第一部相同，前期节奏有点慢，后续节奏快起来还是很吸引人的。

《黑暗荣耀 第二季》，美强惨。

《保你平安》，合格的商业片，有点好奇冯锵锵是怎么死的。

《不眠之夜》，趁着朋友来终于去看了，震撼，虽然没看懂，但是还是震撼。
