---
title: Weekly Issue- 结构化拖延
date: 2024-08-04
tags:
- Weekly
description:  
---


## 文章

### 技术


[k2d - Kubernetes to Docker Translator | k2d.io Documentation](https://docs.k2d.io/)

>The translator is highly resource efficient, requiring CPU cycles only when it's actively translating commands, uses just 20MB of RAM (on top of the OS and Docker requirement of ~120MB), and produces negligible disk IO. Even a device with 512MB of RAM would have ~370MB of RAM available for running applications!

[[k2d]]，预期是解决在工业场景下节点配置很低，运行一个完整的 [[kubernetes]] 资源消耗过多的场景。
通过在本地 docker 环境中，运行 [[k2d]]，来暴露 : 6443 端口，对外提供一个 [[kubernetes]] API，支持有限的 Resources 和 Operations。

---

[Introducing Docker Build Checks: Optimize Dockerfiles with Best Practices | Docker](https://www.docker.com/blog/introducing-docker-build-checks/)

[[docker]] 支持了 Build Check，可以在构建的时候检查 Dockerfile ，`docker --debug build` 可以在构建阶段检查，并指向具体的 Dockerfile 行号及上下文位置，也可以直接使用 `docker build --check` 来运行检查。如果期望在 check 不过的时候 build 失败，可以在 Dockerfile 中增加 `check=error=true` 。

---


[GitHub - SummitRoute/aws\_breaking\_changes: List of changes announced for AWS that may break existing code](https://github.com/SummitRoute/aws_breaking_changes)

[[AWS]] 2024 年开始，有很多的服务下线和 breaking change 发生。

---


[SRE 线上操作指南 | 卡瓦邦噶！](https://www.kawabangga.com/posts/5452)

不只是线上操作，我日常如果走一些验证性的动作，都是打开一个 Note，操作一步写一步，便于后续追踪，后续也可以直接发给其他人 review。

---

[如果 Oracle 都不能在 JAVA 上赚钱，基础软件不如不做](https://mp.weixin.qq.com/s/NPpq0UoEyYSJ78FaBz23dw)

>如果最伟大的技术产品都不能挣钱，你的工作产出就一定能挣钱么？程序员消费的东西基本都是程序员生产的，程序员使用盗版或者鼓励自己服务的公司使用盗版其实都是底层互害。最后大家在付钱这个事上不作为的结果就是导致这个行业彻底消亡。通过劳动获取收入是劳动者的权利，而不是耻辱；通过销售商品获取收入对于商业机构也是一样。

前段时间把 Oracle JDK 换成 openJDK 就踩坑了。

---

[我回来了，Ruby on Rails | WildCat's Blog](https://blog.wildcat.io/2024/08/i-m-back-rails-zh/)

虽然各种新技术一直在更新，但是有时候把时间花在各种框架的选择上，确实不太值得。

---



### 生活

[Structured Procrastination](https://structuredprocrastination.com/)

>任何人都可以做任何数量的工作，只要这不是他当时应该做的工作。

结构化拖延，是指将需要完成的重要任务推迟，转而完成一些看似有意义但实际上不那么重要的任务。我发现自己可能会在不经意间处于这个状态，比如我需要做 A、B、C 三件事，从优先级的角度，我应该先做 A，但是我往往不想立即做 A，反而去做 B 和 C。

---

[This game would be perfect if it wasn't gacha - Xe Iaso](https://xeiaso.net/videos/2024/zzz-review/)

我本身很少玩游戏，玩的游戏也没怎么充钱，但是也听到周围很多喜爱游戏的朋友说，现在的游戏机制为了赚钱已经让游戏“带偏了”。

---

## 书影


《逆行人生》，程序员失业之后送外卖的故事，戏剧冲突太多，多到我无法忍受。

《魔女》，金多美和崔宇植主演的，如果我先看了《魔女》，然后再看《那年，我们的夏天》，应该会觉得更甜吧。

## 碎碎念

* 巴黎奥运会开幕式，为什么引起了如此大的讨论？大家的争议点是什么？
* Github Star 是不可靠的。你无法找到自己很久很久以前 star 过的项目，甚至无法查看。
* Claude sonnet 3.5 写脚本已经很可以了，一次就可运行。
* Edge Dev 版本不靠谱，有很多奇奇怪怪的行为，还是先切换到 Edge 来感受一下。
* 和同事聊起饿了么最近的红包比较多，于是展开聊到了如果我是店家，我是否应该只关心到手的钱？
如果我是店家，饿了么和美团，每一单我到手的钱是一样的，那我应该有倾向性么？同事觉得没有，因为实际上到手的钱是一样的，不关心用户付了多少，平台补贴了多少，骑手拿到了多少。  
我当时的回答是应该关注，因为我是店家，平台展示的是我提供的商品，在到手的钱都是 20 块，用户付了 30 块还是 40 块是明显不同的，我应该去关注这个显著差异。如果不去关注的话，那我就成了一个2B 的店家了？只是这个 B 是平台？平台只是一个中介，对外呈现的还是我的品牌，不关注是没有道理的。





