---
title: Weekly Issue 2023-08-20
date: 2023-08-20
tags:
- Weekly
description: 也许该试试暂停实验室？
---


## 文章

### 技术

[Hunting for Nginx Alias Traversals in the wild](https://labs.hakaioffsec.com/nginx-alias-traversal/)

[[Nginx]] 配置 `location` 和 `alias` 配合可能存在安全隐患，需要保证在 `localtion` 和 `alias` 中都以 `/` 结尾。

![](https://zdyxry.github.io/images/nginx_alias_traversals.png)

---

[OpenTF Foundation](https://opentf.org/)

[[hashicorp]] 改变了 [[License]] 之后，社区对于 [[terraform]] 的未来感到担忧，发起了宣言，期望 [[hashicorp]]可以将 [[License]]改回 [[MPL]]，最坏的打算是后续进行 fork 维护。

---

[同步近期 containerd 的高频问题 | fuweid](https://fuweid.com/post/2023-08-sync-containerd-issue/)

> Init-container rootfs 大部分都是可写模式的 overlayfs，如果 Init-container 是做数据预下载的话，那么 containerd 在删除 Init-container 时，内核一定会刷盘。在大部分场景下，同一个节点上的 Pod 共享同一块数据盘，这种不预期的刷盘很容易把系统打崩。  

---

https://pauley.me/post/2023/spot-price-trends/

[[AWS]] 的 [[Spot]] 实例价格上涨， [[Spot]] 的低价，是由那些租用了标准实例但是没有100% 使用的人支付的。


### 生活


[漫言文案排版规范 – 漫言 MangaTalk](https://mangatalk.net/typesetting/)

文案排版规范，日常聊天倒是不注意这些，但是写文档的时候还是需要尽量保证规范。

---


[Hire for Floors, not Ceilings - Jacob Kaplan-Moss](https://jacobian.org/2023/aug/16/floors-not-ceilings/)

> The mistake we make is putting too much weight on a candidate’s potential – their ceiling – and not looking at their consistency – their floor. Someone who mostly performs below average but occasionally has flashes of brilliance is, generally speaking, a lot less valuable in a team context than someone with consistently average performance. With the “streaky” performer, you’ll never know if a task will take them a week or a month, and you won’t know if you’ll get great code or a sloppy, bug-ridden mess. The downside is usually not worth the upside  

---

[Directly Responsible Individuals (DRI) | GitLab](https://about.gitlab.com/handbook/people-group/directly-responsible-individuals/)

[[Gitlab]] 关于 [[DRI]] 的解释说明。

> 虽然 DRI 是最终对任何特定项目的成功或失败负责的个人，但他们不一定是执行战术项目工作的个人。 DRI 应与所有相关团队和利益相关者进行协商和协作，以确保他们了解所有相关背景，收集其他人的意见/反馈，并在相关人员之间划分行动项目和任务。  
非常明确的是，DRI [GitLab] 不必解释他们为什么做出决定，而且他们绝对不必说服其他人。  
因此，您可以提供意见，但您无权在最终决策中感受到被倾听或被考虑。  

---

[What I am Chasing - STRRL's backyard](https://strrl.dev/post/2023/what-i-am-chasing/)

我自己追求的是什么呢？甚至在生活中感受到幸福的时刻都不多。


## 书影


《封神第一部》，同事推荐，场面宏大，剧情拉胯，但是总体还是鼓励的，部分场景能看到《寻龙诀》的影子。

《金牌保镖》，毛骗团队的网络大电影，感觉相对于上一部电影没有很明显的进度，如果只是这样下去，估计大家的热情会进一步降低了。很多地方都有《意外》的影子。

《假面女郎》，整个剧本，充斥着 AI 的痕迹，关键流行要素全部都有：男女关系、女女帮助、原生家庭、容貌焦虑、犯罪……但是还是觉得很奇怪。不推荐。

《效率脑科学》，书里介绍了很多脑部负责的具体职能，但是很难记得住。所以读完的感受就是把一些日常说的“老人言”场景化，告诉你为什么，我是记不住那些大脑的部位，只是能合理化的解释自己的一些行为：不是我的问题，是大脑正常工作导致的。
