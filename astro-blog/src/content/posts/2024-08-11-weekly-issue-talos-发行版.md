---
title: Weekly Issue-Talos 发行版
date: "2024-08-11T00:00:00.000Z"
slug: "Weekly-Issue-Talos-发行版"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Things you can do with codebases - by Thorsten Ball](https://registerspill.thorstenball.com/p/things-you-can-to-with-codebases)

[Github](/mentions/github) 上有 2 亿个仓库，几乎可以在里面找到所有你需要的代码，如果没找到，可能是你的搜索姿势不对。这篇文章的建议很有用，我现在大部分时间也是这样去了解一个项目的。

工作中我一直使用 `grep.app` 和 `cs.github.com` 来搜索代码，几乎每天都会使用，最常用的就是编写工具类的代码（Makefile、hack/shell 脚本），看看别人是如何实现的，拿过来用用。

---

[Roben Kleene: The Five-Year Rule of Software Transitions](https://blog.robenkleene.com/2023/06/19/software-transitions-the-five-year-rule/)

>一款新软件要么在大约五年内成为市场领导者，要么永远不会。

> Another factor that’s rarely mentioned in Figma’s success is that co-founder and former CTO [Evan Wallace](https://madebyevan.com/) appears to me to be a once in a generation programmer, deserving to be on a short list with the likes of [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson), [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds), and [John Carmack](https://en.wikipedia.org/wiki/John_Carmack).

>转变很少发生的原因是，要发生转变，需要满足两个条件：
>1. 市场领导者必须烦一个重大错误；
>2. 行业发生根本性的转变
>同事必须具备技术基础。

之前和同事聊到，说 [figma](/mentions/figma) 性能为什么那么好，操作很顺畅，记得当时的结论是因为他们技术太强。

---

https://williamlam.com/2024/08/nvme-tiering-in-vsphere-8-0-update-3-is-a-homelab-game-changer.html

[vSphere](/mentions/vsphere) 8.0 U 3 支持了 NVME Tiering 能力，可以将部分 NVME 空间当做内存来使用，看着很强大。不过如果已经有 PCI 直通或者预留全部内存的虚拟机，无法支持 NVME Tiering ，需要注意。

教练我想用 VMware。

---


https://github.com/kubernetes/kubernetes/blob/60c4c2b2521fb454ce69dee737e3eb91a25e0535/pkg/controller/volume/persistentvolume/pv_controller.go#L60-L92

>// PLEASE DO NOT ATTEMPT TO SIMPLIFY THIS CODE.
>// KEEP THE SPACE SHUTTLE FLYING.

“航天飞机风格”的编程风格，每一个分支都有明确的声明和注释，与思考路径是一一对应的。

---

https://kmcd.dev/posts/yall-are-sleeping-on-http3/

2024 年 [HTTP-3](/mentions/http-3) 的一些现状，目前主流浏览器都已经支持了 HTTP/3 协议，主流云厂商也已经支持，截止到 2024年 8 月，从使用率来看，HTTP/3 在快速接近 HTTP/2 。

日常使用中，有明显感知的 QUIC 的就是 Cloudflare Tunnel 了，现在默认是 QUIC，但是我家里的无法建立 UDP 连接，被迫切换回 HTTP/2 了。

---

https://github.com/ccbikai/BroadcastChannel/blob/main/README.zh-cn.md

将 [Telegram](/mentions/telegram) Channel 转换为 Blog 的项目，可以部署在 Cloudflare/Vercel 上，SEO 友好。需要将 Channel 公开。

---


https://sspai.com/post/90668
[济州岛](/posts/济州岛) [游记](/posts/游记)。躺平佛系在咖啡店待一天也不错。

---

https://www.v2ex.com/t/1063856

[Update components.md the length should be all to keep consisdence by cyy8 · Pull Request #47414 · kubernetes/website · GitHub](https://github.com/kubernetes/website/pull/47414#issuecomment-2277646230)

最近有人在小红书，发了自己给 [kubernetes](/mentions/kubernetes) 贡献了一个 PR，修复了一个文档样式问题，引发了大家的讨论。我觉得修复文档样式问题挺好的，很多项目看似很完整，但是当真正走一遍 Quick Start 的时候，多多少少会发现点问题，我都会顺手提一个 PR，毕竟你不修我不修，那就有更多人觉得项目不行。在了解了项目贡献指南之后，参照着指南来进行贡献是没有问题的。

感觉大家的讨论点是两个：是否要因为这样的小的修复去浪费维护人员的时间；是否有必要发小红书来宣传。在符合贡献指南要求的前提下，去贡献我不觉得是浪费维护人员的时间，因为改动很小，review 很快，同时看到有其他 PR 没有描述，维护人员也给了很友好的回复，这应该不是问题。
我觉得宣传自己也没什么问题，大家的戾气太重，去 PR 下刷一些无关的评论，多了很多无用的信息，明显会对社区正常的处理流程产生干扰，不好。

---

[「代码艺术家」不会被 AI 取代 | Randy's Blog | Randy's Blog](https://lutaonan.com/blog/code-artists/)

>我觉得「代码艺术家」是不会被 AI 取代的，因为**设计的起点和终点都是人类**，AI 可以给你 100 个设计上的答案，但只有人类最终能感知到现实和当下的环境和信息，创造出能触动另一群人类的产品。
>**AI 不会替代「代码艺术家」，因为 AI 是「代码艺术家」的喷射机**。

目前的感觉上来看，AI 会让厉害的人更厉害，平庸的人更平庸。这里的厉害和平庸不只是能力上的，还有绝对意义上的产出。

---



### 生活

https://anduin.aiursoft.cn/page/about

这个博客的 About 页面，真诚的让我感动。读完之后有一种很了解对方的错觉，我自己写不出这样的信息，总结不出自己的人生阶段。

---
https://blog.twofei.com/1463/

[小红书](/posts/小红书)找搭子，同事也有不少这样出行的，可行度全看运气。

---

## 书影

《浪漫的体质》，周末又重新开始看，在听播客的时候听到，原来韩国人口中的 30 岁，其实是 28 周岁。所以到了 30 岁也不会变好。


## 碎碎念

* “装作看不见”，这个能力可太重要了。
* 文科有什么用？什么是“用”？
* 写字楼电梯里放了很多花，我还在好奇是什么事情，结果是七夕。七夕好像跟我从来都没有关系啊。
* 降肝低氪，什么奇怪的组合名词。
* 昆明买东西说“斤”是指公斤。
* 我喜欢的作品，是与人相关的，展现一个人的性格特征。而不是社会学所强调的特征。

## Talos

https://www.talos.dev/ ，是一个专门为 Kubernetes 设计的发行版，安全，不可变，很小。在2021年调研 Container Optimized OS 的时候看过他，当时觉得项目不太成熟，于是没有投入。

所有的系统变更都是通过 API 来提供，经常在 Homelab 相关的信息中看到有人把自己家里的 Kubernetes 底座切换到了 Talos，也看到了很多 Demo 视频，感觉非常流畅，于是周末仔细看了看。

Talos 的代码量非常大，30w 行，且代码层级非常的深，直接开始看是会倒头就睡且会睡得非常香的量级。于是我开始搜索下 Talos 的背景，发现了 cosi-project 这个项目，项目本身几乎没有什么介绍性的文档，在 Youtube 上搜到了 https://www.youtube.com/watch?v=Jvp0Ud3mK4o ，讲解了 cosi-project 的背景以及现状，这个视频是 2021 年的，当时 cosi-project 处于一个非常非常早期的状态，但是理念是清晰的。


作者认为现在的各种 Linux 发行版，无论再怎么发展，都还是会基于 systemd + ssh 的方式进行管理，始终会与 K8s 之间夹着一层，不是真正的不可变基础设施，如果想要真正实现完全的管理，需要从头开始重新设计。于是有了 cosi-project 及 Talos，cosi-project 定义了 Spec：https://github.com/cosi-project/specification/tree/main/proto/v1alpha1 ， 包含 State,Resource,Metadata,Namespace 等，其中 State 定义了 RPC 接口，用来对 Resource 进行 CRUD。

https://github.com/cosi-project/runtime 是 Spec 的核心实现，粗略看了下和 K8s Controller 应该是类似的，只是该项目没有依赖 K8s 社区的基础库，完全是自己实现了一套机制。
Talos 在 cosi-project/runtime 的基础上实现了各个必要的 Controller，比如block.DisksController, cluster.MemberController,k8s.NodeIPController 等。

周末在使用 Talos 的时候，发现了一个很重要的问题，如果一切顺利，Talos 上手难度应该很低，但是，如果遇到了问题，如何 Debug？前面提到 Talos 所有的系统变更均通过 API，没有 Shell，也就是之前的所有 Debug 经验都不可用，需要去了解 Talos 的交互方式才可以，如果文档中没有搜索到的话，可能只好去 Github 提 Issue 寻求帮助了。

P.S.： 在不了解 cosi-project 的时候，感觉上与很久之前 Kris Nova 的 https://github.com/aurae-runtime/aurae 解决的问题类似，实际上打开 cosi-project 就能看到 Kris Nova 的身影。看到的时候瞬间有些难过，Kris Nova 离世快一年了，再次阅读她的最后一篇文章： https://krisnova.net/posts/ego-death/ ，一切还是如此。