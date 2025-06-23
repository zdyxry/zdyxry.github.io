---
title: Weekly Issue-avoid negativity echo chambers
date: 2025-06-22
tags:
- Weekly
description:
---


## 文章

### 技术


[Why Generative AI Coding Tools and Agents Do Not Work For Me - miguelgrinberg.com](https://blog.miguelgrinberg.com/post/why-generative-ai-coding-tools-and-agents-do-not-work-for-me)

> The more you practice learning the easier and faster it gets!

---

[周思博 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E5%91%A8%E6%80%9D%E5%8D%9A)

[[StackOverflow]] 的创始人和 [[Trello]] 的创始人是同一个人，一直以为这是两个时代的软件。

---

[Pure, Ocient and Solidigm push back against Seagate-quoted SSD paper – Blocks and Files](https://blocksandfiles.com/2025/06/16/pure-ocient-and-solidigm-say-the-seagate-quoted-dirty-secrets-report-is-wrong/)

这些大公司的市场部真的是有钱又有闲，争论起 SSD 和 HDD 碳足迹这种东西。你排多少碳，关我用户什么事。都是生意。

---

[Quick takes on the GCP public incident write-up – Surfing Complexity](https://surfingcomplexity.blog/2025/06/14/quick-takes-on-the-gcp-public-incident-write-up/)

> This is the typical “we didn’t do X in this case and had we done X, this incident wouldn’t have happened, or wouldn’t have been as bad” sort of analysis that is very common in these write-ups. The problem with this is that it implies _sloppiness_ on the part of the engineers, that important work was simply overlooked. We don’t have any sense on how the development decisions made sense at the time.

“如果当时做了 X 就不会出现这个事故了”，为什么当时没有做 X？应该想为什么当时做了 Y。

---
[k8s的域名解析总是需要coredns吗？](https://ieevee.com/tech/2025/06/18/loopbackresolver.html)

> 问题：如果 kube-apiserver 通过普通的 Service IP 访问自己，可能依赖 DNS 解析、kube-proxy 或网络插件，这些组件可能未完全运行或存在网络延迟 / 异常。    
> 解决：Loopback 直接将请求回路短路到本地，从而绕过外部网络依赖。

---

[GitHub - psviderski/unregistry: Push docker images directly to remote servers without an external registry](https://github.com/psviderski/unregistry)

我喜欢这个项目，这个需求有很多的解法，但如何在有限的场景中无感的使用，是不容易的。

Docker 作者在 HN 上进行了回应：

>Docker creator here. I love this. In my opinion the ideal design would have been:  
>1. No distinction between docker engine and docker registry. Just a single server that can store, transfer and run containers as needed. It would have been a much more robust building block, and would have avoided the regrettable drift between how the engine & registry store images.
>2. Push-to-cluster deployment. Every production cluster should have a distributed image store, and pushing images to this store should be what triggers a deployment. The current status quo - push image to registry; configure cluster; individual nodes of the cluster pull from registry - is brittle and inefficient. I advocated for a better design, but the inertia was already too great, **and the early Kubernetes community was hostile to any idea coming from Docker.**


### 生活

[云风的 BLOG: 育儿的一些日常](https://blog.codingnow.com/2025/06/kids.html)

小孩子的快乐来的很简单。

---

[Rolling the ladder up behind us - Xe Iaso](https://xeiaso.net/blog/2025/rolling-ladder-behind-us/)

> Additionally, if this is such a transformational technology, why are key figures promoting it by talking down to people? Why wouldn't they be using this to _lift people up_?

---

[Waiting is risky | Bryan Braun - Frontend Developer](https://www.bryanbraun.com/2025/06/21/waiting-is-risky/)

> For one, sometimes **the world changes**, and your idea no longer makes sense.   
> But the other reason that waiting is risky, is that **you** change.   
> Maybe it’s good that I didn’t waste my time building some niche thing only to have it replaced by AI. Maybe I dodged a bullet by not committing to a business I would have grown out of.    
> But when I look at my freshest, most exciting ideas—it pains me to know that if I don’t build them now, I might never do it, because I’ll never feel as passionate about them as I do today.    

行动力非常难得。

---

[Career advice, or something like it - Marc's Blog](https://brooker.co.za/blog/2025/06/20/career.html)

> If I could offer you a single piece of career advice, it’s this: avoid negativity echo chambers.

> I recommend you choose one of two paths. If you want to move your career or industry forward, focus on the positive parts of your role, and spend energy making things better. Alternatively, if you don’t want to advance your career, spend the right amount of energy to stay where you are. Then, instead of joining that whiny waterhole, go home and mow the lawn, play with your dog, take a walk in the woods with your kids, or whatever you enjoy.

> My advice: find the yes, and communities, and spend time there. Find the people doing cool stuff you admire, and spend time with them. Find the people doing the work you want to do, or living the life you want to live, and find ways to learn from them.


这篇文章可以反复阅读，并按照文章建议执行。

---



## 碎碎念

* 随便让 AI 把一些已有项目的 README、帮助文档改一改，对易用性的提高就很大。
* 避免日常沟通中文字的滥用，比如”割韭菜“。
* 我发现自己几年前选择的技术路线是错的，突然汗毛就起来了。
* 一个许久不联系的朋友突然问了一个 ftp 问题，2025 年，ftp，哎。
* 和父母吵架，表面上是关心，实则是自己面子挂不住，拉黑了。
* 上海的天气一冷一热的，感冒了。
* 周末尝试跑了 15km， 历史新高。
