---
title: Weekly Issue-人分千里外，兴在一杯中
date: "2026-06-28:00:00.000Z"
slug: "Weekly-Issue-renfenqianliwai"
tags:
  - Weekly
description:
---

## 文章

### 技术


[从刀耕火种到 Zarf：air-gap Kubernetes 软件交付踩坑实录](https://spencercjh.me/blog/air-gapped-kubernetes-software-delivery/#sbom-%E6%98%AF%E5%85%8D%E8%B4%B9%E7%9A%84)

> Zarf 的做法很硬：直接拿 **ConfigMap 当运输层**。`registry:3` 压缩后大概还有 18MB，单个 ConfigMap 有 1MB 上限，塞不进去，就只能先打 tar，再切成很多块，分散塞进一堆 ConfigMap 里。

> 但把碎片送进去还不够，还得有人在集群里把它重新拼起来，再临时顶出一个能用的 registry。干这个活的是 `zarf-injector`。它本身是个 **不到 1MiB 的 Rust 二进制**，而且还是 MUSL 静态编译。这里偏偏没用 Go，不是风格问题，而是尺寸问题：它自己也得塞进 ConfigMap，Go 二进制太大，不合适，只能换更小的 Rust。    
> 还有一道坎也很现实：要跑 injector pod，总得先有个容器镜像。但这时候又没有地方拉镜像，所以 Zarf 不是去拉一个新的，而是想办法复用集群里原本就有的 `pause` 镜像。Kubernetes 不会直接把 pause 镜像地址告诉你，它就自己去猜：名字里带 `pause`、主版本号是 3 或 4、体积小于 1MiB，大体按这个范围去找。   
> 后面的流程就接起来了：先起一个用了 pause 镜像的 pod，把那堆 ConfigMap 挂进去；pod 里跑 injector，把那些碎片重新拼回 `registry:3`；再临时起一个只读的 seed registry。等 seed registry 活过来以后，真正的 `docker-registry` 才拿它当镜像来源把自己拉起来。正式 registry 起来以后，injector 和 seed registry 这一套临时结构就可以删掉了。

这篇文章即使是作者自己重新梳理在输出，也有一些 AI 味儿。我最开始以为是因为文章中出现了 13 个“而是”，现在想想可能不是，说不出来，同事说我有些妖魔化“而是”了。

---



[There Are No Instances in atproto — overreacted](https://overreacted.io/there-are-no-instances-in-atproto/)

[[ActivityPub]] 和 [[ATProto]] 的差异，视图可以很直观的了解两者区别。有人指出了文章中有意忽略了 Relay 组件的重要性，当前 BlueSky 主要还是使用的中心化的 Relay ，但是他们好像有意的忽略了当前 [[Meta]] 的 [[Threads]] 也是一个巨大的中心化的 [[ActivityPub]] 实例，使用 [[Threads]] 的普通用户想要订阅特定实例的用户消息，结果因为特定实例的管理员对 [[Meta]] 的抵制导致普通用户无法订阅，这是无法避免的问题。

朋友说 [[Threads]] 上面找到了 10 年前使用微博的快乐，活人感十足。

---

[都AI时代了，我为何还在学习前端基础知识？ «  张鑫旭-鑫空间-鑫生活](https://www.zhangxinxu.com/life/2026/06/ai-why-keep-study/)

> 注意，是不推荐学习嘎吱角落的细节，并不是不推荐大家去学习，在任何时候，学习总是没有错的，在实际的职业生涯发展中，决定最后高度的是人与人的竞争，而不是人与 AI，这个学习不仅仅是专业技术，包括沟通协作，业务推动，为人处事，都在这个范畴。

> 所以，我这把年纪了，还在不停地学习前端技术，无论是前沿新特性，还是各种精妙的实现技法。
> 这几年下来，一直保持着每周至少更新一篇技术文章的节奏，并积极在项目中应用自己学到的东西，积攒开发经验。
> 全都是为了在 AI 时代，走得更快更远。


---
[6倍速的Kimi K2.7 Code 高速版和普通版是同一个模型吗？ - 知乎](https://zhuanlan.zhihu.com/p/2050101239405450772)

最近 Kimi Code 的体验计划可以开启高速版本了，我实际开启了之后，发现在出活的场景下，199 套餐很容易触及 5h 额度的上限，然后不得不切换回正常速度，为了能用相对更多的额度。

这里就有一个问题，我是否应该选择高速版？高速版本相对于正常速度的倍率是 6x 速度，3x 消耗。也就是说，同样消耗 1h 额度，实际可用时间只有 20min，理论产出是原来的 2 倍？5h 的额度，对应的高速版本实际可用时间是 1.6h，实际对应的是 10h 工作量。

如果是为了更好的产出，虽然可能 5h 额度范围只能用 1.6h，但是从产出角度，这 1.6h 是高强度高专注的投入，因为速度真的很快，你很难会去抽时间去做其他的事情，就不会因为正常速度太慢导致经常要同时开多个任务去做，减少了很大的上下文切换成本。

最终我的方案：如果是一件非常明确的工作，那么直接用高速版，如果是一件需要你大量思考的工作，即使速度再快也需要你来不断的投入大量思考时间，那么用正常速度。

---

[失业了](https://nekocode.cn/weixin/%E5%A4%B1%E4%B8%9A%E4%BA%86-4e617505/)


> 我前老板用 OpenClaw 几天就 Vibe 出了一个 Dashboard，自此开始大肆追捧 OpenClaw、AI-First，以及类似 Peter 那样的「超级个体」概念。他认为 AI 已经带来了颠覆性的生产力提升，我们必须立刻跟进，于是递上投名状，说白了，就是一个人得干十个、甚至横跨不同职业的人的活，才算及格。

> 当然，这些要求，到部门最后解散也没人能做到 🌚，业务指标更是连影子都没见着。这段时间内唯一拿得出手、能向上汇报的指标，大概就只剩代码行数了 —— 不过这个倒确实挺吓人，每个月我们部门都能新增几十万行存活代码 🤣。

> 而我前老板，也因为这些超前的、或者说可能给公司带来降本增效 / 破局的理念，晋升了 Title，成了公司的 AI 总负责人。

---




### 生活
[高考随想](https://lutaonan.com/blog/gaokao/)

> 高考考得好固然好，但人生啊，不是一段解题的过程，而是一场终生的牌局。总结起来，人生无非四种玩法：一手好牌/打得稀烂；一手好牌/打出更大价值；一手烂牌/破罐破摔；一手烂牌/打成好牌。   
> 每个人都有不同的打法，只要打得让自己感到快乐，就是好的打法。如果同时还能让身边的人也感到快乐，那可算是功德圆满了。

---

[No-One Escapes the Permanent Underclass](https://borretti.me/article/no-one-escapes-the-permanent-underclass)

> Shall I end this life a pauper? If AI can do all work at human level or better, what stops corporations replacing us all with AI? This is the permanent underclass meme.

如果 [[AI]] 能够完成人类的所有工作，那么人类最终会变成什么样子，底层人民被淘汰，资本家就不会么？作者说最终所有与核武器发射密码有一度以上关系的人都是多余的。

---

### 书影播客

《金特务：本色回归》，苏志燮主演的漫改韩剧，还是爽剧，剧情有点老套。


## 碎碎念

* 上班没有搭子是一件很难的事情。
* 发现 Edge 的历史记录失效了，更新后恢复了。
* 几年没关注了，发现kubekey 自己实现了一个 mini ansible，兜兜转转。
* 提测质量差，原因是啥呢
* 人分千里外，兴在一杯中
* Notion Mail 关闭了，我完全找不到使用它的理由。
* 现在非遗的东西是不是有点太多了？怎么什么都是非遗啊？齐齐哈尔烤肉是非遗，包子也是非遗，菜饭也是非遗
* 台湾的台繁体字是臺，台州的台繁体字是台。
* 还是需要一些理想主义的。