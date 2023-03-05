---
title: Weekly Issue 2023-01-22
date: 2023-01-22 19:00:00
tags:
- Weekly
description: 2023 年来了，新年快乐，希望大家都能身体健康。
---


## 文章

### 技术

[重构荷兰政府那个那个非常有效的代码](https://colobu.com/2023/01/20/The-refactoring-of-the-%E2%80%9CVery-efficient-Code%E2%80%9D-from-Dutch-DigiD-App/)   
最近的热门讨论，编写一个根据百分比生成进度条的函数。

---



[Cloud Spend Breakdown](https://matt-rickard.com/cloud-spend-breakdown)   
[[37Signals]] 发布了2022 公有云服务的账单，其中关于数据存储和数据相关服务占比达到了70% ，这部分是最难迁移出来了，期待后续。

---

[What's what with Wolfi, the Linux "undistribution," and ARM | Open Source Watch](https://opensourcewatch.beehiiv.com/p/what-s-what-with-wolfi-the-linux-undistribution-and-arm)   
对[[Wolf]] 项目的介绍，用来应对供应链攻击。

---



[State of Infrastructure-from-Code 2023 - Klotho](https://klo.dev/state-of-infrastructure-from-code-2023/)   
[[IaC]] 之后谈论[[IfC]] ，在IaC 场景下，开发人员通常需要考虑业务应用程序和基础设施两种应用。  
[[IfC]] 通过分析业务应用代码来推断所需的基础资源，然后自动创建并维护，不需要手动指定。目前已有的方向是通过 SDK、通过代码注释、两者结合、通过新的编程语言实现。预测 [[IfC]] 会在之后愈发流行。
[[IfC]] 创建的资源如何管理？如何保证应用程序没有滥用资源？

---



[How to use interfaces in Go | jordan orelli](https://jordanorelli.com/post/32665860244/how-to-use-interfaces-in-go)   
关于 [[Golang]] [[interface]] 使用上的总结。

---

[How to improve Python packaging, or why fourteen tools are at least twelve too many | Chris Warrick](https://chriswarrick.com/blog/2023/01/15/how-to-improve-python-packaging/)   
关于 [[Python]][[package]] 的详细介绍文章，并对比了 [[JavaScript]] 和 [[.NET]] 生态，来吐槽 Python 的一团糟。

---

[烧钱工作法 —— 远程开发是怎样提升我的效率？| Oilbeater 的自习室](https://oilbeater.com/2023/01/15/how-remote-coding-improve-productivity/)   
通过 [[Jetbrains]] [[gateway]] 配置 [[GCP]] 的 Spot 实例进行远程开发，因为 GCP 是实时计费，所以作者会（被迫）集中注意力到当前工作。

> 不过最直接的感受并不是以上那些，当启动机器的脚本启动后我这边就感觉点起了一个烧钱的火炉，由于 GCP 的计算资源是按秒计费的，那种感觉真的就是实时烧钱。所以基本上火炉一开就什么都顾不上了，注意里全部集中到了当前的任务上，根本不想分心。这段时间别人找我就根本不想理；要是有什么操作或者思路的错误导致耽误时间了，就想抽自己；之前懒得弄的一些脚本自动化，和一些工具的高效使用技巧，快捷键什么的也都开始研究了。由于这种被烧着工作的感觉过于刺激，有时候一些不想干又必须干的工作，并不是必须远程开发，比如文档什么的，我也会先把钱烧起来，然后就很刺激的完成了。

---

[用 BPF 动态追踪 Python 程序 | 卡瓦邦噶！](https://www.kawabangga.com/posts/4894)   
> 在网上查询和 Python 有关的 BPF 内容大部分都是“如何通过 Python（BCC）来使用 BPF”，而不是“如何用 BPF 去 profile Python 代码”。

---

[A 5,5 years retrospective of working with Bare Metal Kubernetes, or To there and back | Geek Culture](https://medium.com/geekculture/a-retrospective-of-working-with-bare-metal-kubernetes-or-to-there-and-back-1868c0356eff)    
使用 [[Bare Metal]] 管理 [[kubernetes]] 集群的回顾。作者选择[[kubespray]] 来部署集群，在早期使用感受是较好的，但是随着集群规模越来越大，[[kubespray]] 耗时随着节点数成正比，[[kubespray]] 带来的灵活性超出了作者想要的预期，带来的维护性翻倍，作者采用[[kubeadm]] 来重新实现自己所需的 ansible playbook。  
在管理过程中，随着对测试集群的要求，作者对各个公有云的 [[kubernetes]]服务置备方式进行了调研，最终目的是想要拉起置备 [[kubernetes]] 集群的操作，保证环境一致。

---

[Monitoring benchmark: how to generate 100 million samples/s of production-like data](https://victoriametrics.com/blog/benchmark-100m/)     
[[VictoriaMetrics]]如何进行监控数据 [[benchmark]]。数据集并不是完全随机的，博客中使用温度和电压举例。最后直接使用[[node-exporter]] 作为数据源，通过部署多个副本来提供实时数据。通过 [[VictoriaMetrics]]的一些优化配置，最后可以达到 2GB/s 的数据写入速度。

### 生活

[《风暴英雄》对我的意义 | Reorx’s Forge](https://reorx.com/essays/2023/01/what-hots-means-to-me/)   
游戏对我们意味着什么？带给了我们什么？

最近[[暴雪]]和[[网易]]合作到期，国服要关闭了，我玩暴雪的游戏不多，炉石传说无论是自己玩还是看直播，都是陪着我从大学到工作。

---

[M1 Pro 的 MacBook Pro 之一年体验记 | I'm TualatriX](https://imtx.me/blog/one-year-experience-of-m1-pro-macbook-pro/)    
家里的是年迈的 2017 MacBook Pro，电池已经不行了，在考虑如何处理。

---

[费曼学习法实践 / INDIGO 的信息获取与知识输出方法论](https://www.indigox.me/feynman-technique-in-practice/)   
如何平衡输入和输出的关系。

---


## 书影


《三体Ⅰ》，《三体Ⅱ》，最近《三体》动画和剧集都开始上线了，朋友中经常谈论这个，但是我一直没看过，趁着假期，先把小说读了。

《北京浮生记》，看到推上有人推荐，玩了玩，中关村水货大亨，靠着水货手机发家致富。

《相残》，很难描述，看完了很困惑，不理解，为什么。

