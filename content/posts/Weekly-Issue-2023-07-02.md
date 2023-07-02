---
title: Weekly Issue 2023-07-02
date: 2023-07-02
tags:
- Weekly
description: 属于许三多和成才的一周。
---


## 文章

### 技术

[How to use GitHub Copilot: Prompts, tips, and use cases | The GitHub Blog](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)

[[copilot]] 的一些技巧，总结下来就是假象在结对编程，尽可能的细粒度告诉对方当下的想法。

---


[Monitoring is a Pain](https://matduggan.com/were-all-doing-metrics-wrong/)

关于 [[monitor]] 的一些思考，包含 Logs，Metrics，Traces 。

日志级别和格式混乱,没有共识。日志被用于各种用途,从调试到业务分析,使其变得极为关键，存储成本高昂,大多数日志从未被使用。

Metrics 很好，但是当前 [[prometheus]] 生态在后续的扩展上没有那么容易。

---

[Backup and Restore Containers With Kubernetes Checkpointing API | by Martin Heinz | Better Programming](https://betterprogramming.pub/backup-and-restore-of-containers-with-kubernetes-checkpointing-api-e310cf29cd4a)

[[kubernetes]] [[Pod]] checkpoint 方式，后续应该可以作为 Pod Live Migration 的前置动作。

---

[I'm done with Red Hat (Enterprise Linux) | Jeff Geerling](https://www.jeffgeerling.com/blog/2023/im-done-red-hat-enterprise-linux)

[[RedHat]] 事情继续发酵，目前官方态度很明确，不会进行改动。这篇文章有些后有趣的描述。比如：

> They would add magic sauce that makes it Red Hat Enterprise Linux  
> And please tell your employees to stop patronizing me, saying I should just use CentOS Stream. There’s a reason Rocky and Alma linux have been downloaded _millions_ of times. Stream is not a substitute for CentOS.  

但是他没有解释，为什么需要 magic sauce ， reason 是什么， 为什么不能是 substitute

---


[Keeping Open Source Open | Rocky Linux](https://rockylinux.org/news/keeping-open-source-open/)

[[Rocky]] Linux 计划从其他方式获取 [[RHEL]] SRPM： [[RedHat]] 官方发布的 container image、去付费使用[[公有云]]创建[[RHEL]]实例。

---

[Unlocking the Power of Cloudflare Tunnel: Secure, Scalable, and Simple Kubernetes Ingress Controller Implementation for Your Applications - STRRL's backyard](https://strrl.dev/post/2023/unlocking-the-power-of-cloudflare-tunnel-secure-scalable-and-simple-kubernetes-ingress-controller-implementation-for-your-applications/)

使用 [[Cloudflare]] [[Tunnel]] 来对外暴露 [[kubernetes]] 服务。

---

https://johncodes.com/posts/2023/06-29-on-maintaining-cobra/

> *“Why work on a CLI framework when you should be working on products?”* or *“This doesn’t seem critical to our bottom line.”*  
> Compare that to something like core Kubernetes ([*which in itself uses cobra*](https://github.com/kubernetes/kubernetes/blob/c78204dc06d5b0bc02fc2f6bb7dbf98552180d26/go.mod#L62)), a platform for running and managing containerized workloads and services in the cloud. Now *that* sounds like a product you can ship!  

作者是 `cobra` 的维护者，在公司层面上，相对于其他的 “product” 来说，一个 “CLI framework” 是不值得投入精力去维护，它不会带来明显的利润。

---


### 生活

[聊聊公益和助学 | Manjusaka](https://www.manjusaka.blog/posts/2023/06/25/love-and-hope-is-all-we-need/)

> 这个世界越来越操蛋，也越来越混沌了。这个时代是否如狄更斯所说 “这是一个最好的时代，也是一个最坏的时代”，我对前半句抱有怀疑。  
但是我依旧愿意去相信爱，光和奥特曼，人生苦短，总得做点什么，让这个 fucking ridiculous 的世界变得有那么彩色一点。  

---

[也值一个屁](https://www.douban.com/note/850727749/?_i=7927407jowl3CC)

> 我还见过很多这样的家长，总爱在外面说，“我砸锅卖铁也要让小孩怎么怎么样”……——我没见过一个小孩，因为父母砸锅卖铁过上幸福生活的。家里都到了砸锅卖铁的地步，小孩能幸福到哪里去？一个有良心的小孩，是不可能让父母砸锅卖铁供自己的，宁可学不上了。所以你就知道，这种语言或者行为，会给孩子造成一种什么效果：  
“咱们输不起。”  
“你考不出来，就对不起爹妈。”  
这是亲情的胁迫。哪怕是以最不动声色的方式。  


---


[“内卷”使用说明书 - 知乎](https://zhuanlan.zhihu.com/p/436485732)

> 这就是内卷的核心。所有人都付出了比原来更多的代价，但是**::集体::**的利益却没有增加。简而言之就是，大家花了更大力气去分蛋糕，但是蛋糕大小并没有变大。  
> 内卷并非用来形容个体，而是形容集体。  

---

[A few words on taking notes | All Things Distributed](https://www.allthingsdistributed.com/2023/06/a-few-words-on-taking-notes.html?utm_campaign=inbound&utm_source=rss)

关于记录笔记的思考，使用纸笔记录有时候确实留下的印象会更深一些。如果不知道如何整理笔记，那就先记录下来，按照现在的 AI 发展速度，应该很快就有 AI 来帮忙整理笔记了。

---

[溜达后的一点回顾](https://www.gexiao.me/2023/07/01/lets-wander/)

> 我的这份关心非常简单：确认朋友对自己的小环境并未失控；焦虑拿出来讲讲有人能给一点点理解和支持，在深层意识里可能就不那么孤单。「孤单并不发生在一个人喝酒，一个人吃饭，一个人搬家，一个人做手术这些屁大点儿的事情上，而是关键问题上的无人回应」。  

这篇文章写的真好。[[朋友]] 是需要维护的，我很喜欢自己和朋友在一起的状态，但是通常又不会主动的去迈出线下沟通的那一步，有些矛盾。

## 书影

《海妖的呼唤》，看完了，各个职业的特点都体现了，很棒的综艺。

《消失的她》，太过于套路化了，相对来说不好。

《八角笼中》，如果《摔跤吧，爸爸》是100分，那么这个电影就是60分，前者用了足足的 160分钟讲述了一个完整的舒适，王宝强想要在 120分钟以内讲一个一样的故事，事实证明做不到。现在电影 120分钟已经是常规操作了，为什么不考虑多加点铺垫呢。很多情节很生硬，交代人物心态变化有缺失，很多镜头已经在明着告诉观众：“此处可适当落泪”。 对于王宝强的上一部电影来说，是一个明显的进步。

《可是，我开的是书店》，作者非常的矛盾，作为一个很喜欢书店的人，读着读着都会被气到，不推荐。