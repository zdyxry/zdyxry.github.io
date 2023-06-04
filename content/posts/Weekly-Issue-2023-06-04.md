---
title: Weekly Issue 2023-06-04
date: 2023-06-04
tags:
- Weekly
description: 大型网友见面会。
---


## 文章

### 技术


[Prometheus 的 Summary 和 Histogram](https://liqiang.io/post/summary-and-histogram-in-prometheus-zh)

[[prometheus]] 的 `Summary` 类型和 `Histogram` 类型。之前内部实现网络监控功能的时候，使用了 `Histogram` ，Bucket 的划分粒度比较重要，如果划分的不好那么结果的偏差可能会比较大。

---


[记一次 BUG 定位：时钟偏移引起 K8S 鉴权失败 | 三点水](https://lotabout.me/2022/k8s-jwt-and-clock-skew/)

[[kubernetes]] 节点时钟不一致导致的[[JWT]] 校验不通过问题。
> B 节点的时间比 A 节点快 1min30s;  
任务被调度到 B 节点，B 节点的 kubelet 为 Pod 生成 SA token，token 的 nbf 时间为 B 节点的当前时间。（这里应该是创建 token 的请求会发往 B 的 apiserver，目前没找到方法验证）;  
B 节点里需要访问 apiserver，会访问 kubernetes.default，请求被路由到节点 A;  
A 节点在校验 JWT 时发现 token 的 nbf 在 A 节点当前时间+ 1min 之后，拒绝请求;  

---

### 生活

[“移民”是第一生产力 -#35 - GeekPlux](https://geekplux.com/newsletters/35)

> **每个城市传递的信息不同，每个城市的价值观和氛围也不同，移来的人和城市互相影响，地理环境与人文环境相互作用，最终催生城市与人共同的进化。**  

---

[【结节性红斑/反应性关节炎】 诊断，治疗，康复和血泪史 - 玻璃齿轮 - SlassGear](https://blog.winkidney.com/index.php/archives/31/)

最近一个同事突然脚痛，无法步行上班的那种，去医院也查不出来原因，最后推给了[[痛风]]。就想起了[阿毛](https://blog.winkidney.com/) 的这篇博客，免疫系统疾病太可怕了，希望大家都能身体健康。

---

## 书影

《深入理解 Linux 网络》，本周没有继续读。

《聋哑时代》，在单向空间闲逛，本来想买《冬泳》，但是只有一本样书了，就买了这本，刚看了开头。

《蜘蛛侠：纵横宇宙》，精彩，画面呈现非常棒，目不暇接，很喜欢蜘蛛女与爸爸的两段沟通。（建议补一下第一部）

《蜘蛛侠：平行宇宙》，先看了纵横宇宙，后看了平行宇宙，发现应该先去补一下背景知识的，这样看起来比较顺畅。

## 碎碎念

周三到周六公司团建，上一次团建还是疫情前去三亚，属于大型网友见面会了，之前团建都是会开会老板说些什么，这次真的是符合我对团建的刻板印象，各种团队活动，确实可以很快的熟悉，也见到了平时交流比较多的同学，很开心。阿那亚是一个神奇的地方，很多外面的社会习惯在里面不适用：比如民宿登记无法拿到房卡、房卡只有一张、外卖无法适用饿了么/美团…… 

![](https://zdyxry.github.io/images/Aranya.jpg)