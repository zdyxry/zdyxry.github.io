---
title: Weekly Issue 2023-03-05
date: 2023-03-05
tags:
- Weekly
description: 迁移博客是个体力活。
---


## 文章

### 技术


[Coding 102: Writing code other people can read - Stack Overflow Blog](https://stackoverflow.blog/2023/02/13/coding-102-writing-code-other-people-can-read/)

关于代码风格的示例，写出可读代码。

---

[HTTPS 隐私安全的一些实践 | Laisky's Blog](https://blog.laisky.com/p/https-in-action/)

[[HTTPS]] 相关概念介绍。

---



[Introducing MRSK - YouTube](https://www.youtube.com/watch?v=LL1cV2FXZ5I)

[[MRSK]] 介绍，通过 DSL 和 [[docker]] 运行 [[container]] app。

> Kubernetes is a beast. Running it yourself on your own hardware is not for the faint of heart. It's a fine option if you want to run on someone else's platform, either transparently [like Render](https://thenewstack.io/render-cloud-deployment-with-less-engineering/) or explicitly on AWS/GCP, but if you'd like the freedom to move between cloud and your own hardware, or even mix the two, MRSK is much simpler. You can see everything that's going on, it's just basic Docker commands being called.

---

[Introducing ChatGPT and Whisper APIs](https://openai.com/blog/introducing-chatgpt-and-whisper-apis)

[[ChatGPT]] 开放 [[API]] 了，应该会有很多应用为了快速吸引用户而接入。

---

[Introducing the Determinate Nix Installer — Determinate Systems](https://determinate.systems/posts/determinate-nix-installer)

[[Nix]] 的安装器官方使用 [[Bash]] 来编写的，但是 [[Bash]] 对于环境兼容和适配工作是很繁琐的事情，[[Determinate Systems]] 使用[[Rust]] 重写了整个 安装器，并提供了完整的卸载功能。
对于 [[Nix]] 的安装失败/卸载/重复安装问题，提出了 `receipt` 的概念，用来记录安装过程中涉及到的所有动作：

> We introduced the concept of an installation **receipt**. This is a JSON file that indicates what has already been accomplished by the installer—and what hasn’t. It’s stored under `/nix` and keeps all the information the installer needs to *uninstall* Nix seamlessly. That means deleting all of the volumes, directories, files, users, and groups that the installer created as well as surgically undoing changes to files you need to keep around (like `bashrc`).

---

[Dashworks for Slack](https://www.dashworks.ai/for-slack)

[[Dashworks]] 集成在 [[Slack]] 中的 [[metasearch]]，可以快速检索分散在各处的信息并分析汇总。我感觉很需要这个，日常信息散落在 Slack/Jira/Github/GitLab/Google Drive.... 真的太烦了。

---


[Some notes on using nix](https://jvns.ca/blog/2023/02/28/some-notes-on-using-nix/)

[[Nix]] 101 。完全可以只把[[Nix]] 当做一个包管理器使用，最近在内部项目中使用了 [[devbox]] 作为环境依赖声明，使用起来很方便。

---

[Simulating NUMA Nodes for Nested ESXi Virtual Appliances - frankdenneman.nl](https://frankdenneman.nl/2023/03/02/simulating-numa-nodes-for-nested-esxi-virtual-appliances/)

使用[[vNUMA]] 配置来创建嵌套的 [[ESXi]] 节点。

---

[网络问题定位工具记录 - 轩脉刃 - 博客园](https://www.cnblogs.com/yjf512/p/17174669.html)

使用[[nstat]] 获取网络接口统计信息， `watch -d -n1 "nstat -a | grep -i -E 'drop|error|fail|loss|overflow'"`

---

[Prometheus 数据存储那些事儿 - luozhiyun`s Blog](https://www.luozhiyun.com/archives/725)

[[prometheus]] 数据存储介绍。

---


[How do Nix builds work?](https://jvns.ca/blog/2023/03/03/how-do-nix-builds-work-/)

看似是在介绍[[Nix]] build 是如何工作的，但是读下来的感觉就是在劝退。

---

[「 深蓝洞察 」2022 年度最“不可赦”漏洞](https://mp.weixin.qq.com/s/P_EYQxOEupqdU0BJMRqWsw)

大开眼界，有评论说是拼多多。

---

[go dns解析原理及调优  - Go语言中文网 - Golang中文社区](https://studygolang.com/topics/15021)

> go默认使用内置dns解析器，不依赖操作系统，跟基础镜像无关
go内置解析器会读取/etc/resov.conf配置，标准配置都有实现，手动修改配置5秒后生效
Go1.17之后可以禁用ipv6解析
go内置解析器解析过程默认是并行和串行结合的
相同域名的不同请求类型是并行的
不同域名之间是串行的

---

### 生活


[How Douyin Bootstrapped Its Flywheel](https://tieshunroquerre.com/blog/douyin)

关于[[抖音]]成功的猜想，其中提到运营起到了很大的作用。

---

[在碎片化的时代里生存——碎片时间使用说明书。 - Xiaowen.Z Deployed](https://xiaowenz.com/blog/2023/02/decouple-your-time/)

关于[[碎片化]]的思考，要保证自己的每个动作都是闭环的。
> 「**闭环**」的定义：内容明确，完成的时间可控，完成的条件是确定的可度量的。在很多GTD理论中，又称之为**Actionable**。

---

[Wrong Sequences For Startups](https://matt-rickard.com/wrong-sequences-for-startups)

用最熟悉最简单的方式来实现，贴近用户，搞清楚用户想要什么。

---

[Creating Value | Principal Engineering. Understanding how to create value as a… | by Kris Nóva | Sep, 2022 | Medium | Medium](https://web.archive.org/web/20220912061404/https://medium.com/@kris-nova/creating-value-as-a-principal-aa59c7986344)

好难啊，怎么样才算创造价值呢，自己想做的事情没有排期，怎么处理？感觉还是直接开始做起来比较重要。

---



## 书影

《当我们不再理解世界》，读完了，天才的世界不被人理解。

《模范出租车》，在现在的韩剧中算是很长的了，32集，每个故事大概4,5集的样子？ 确实爽，接下来看看第二季。

《的士判官》，经典电影，黄秋生的演技很棒。

## 游戏

《卧龙：苍天陨落》，作为一个没怎么玩过游戏的人，对我来说太难了，张梁打了很久也没打过去。。


