---
title: Weekly Issue 2023-05-14
date: 2023-05-14
tags:
- Weekly
description: LazyVim 是个好东西。
---


## 文章

### 技术

[使用 FFMPEG 编辑视频](https://liqiang.io/post/edit-videos-with-ffmpeg-command-64584f81)

使用 [[ffmpeg]] 合并、裁剪视频。

---

[Cilium 基于 eBPF 实现 socket 加速](https://mp.weixin.qq.com/s/Zsml8bZV_nZPZYgVhTym1w)

使用`BPF_MAP_TYPE_SOCKHASH` 存储 socket 信息, `BPF_PROG_TYPE_SOCK_OPS` 拦截系统中 socket 建立连接操作 , `BPF_PROG_TYPE_SK_MSG` 拦截系统中 sendmsg 系统调用，提取 key，将数据直接重定向到对端 socket。

> 使用 eBPF socket 加速之后，吞吐量和发送消息大小呈线性关系。这是因为当应用程序发送较大的消息时，几乎没有额外的开销，但是当发送消息比较小时，使用 TCP/IP 协议栈，反而吞吐量会大于 eBPF socket 加速之后的吞吐量，这是由于 TCP/IP 栈默认开启了 Nagle 算法。Nagle 的算法是用来解决小数据包在慢速网络中泛滥导致拥塞的问题，在该算法中只要有一个 TCP 段在小于 TCP MSS 大小的情况下未被确认，就会进行批处理传输数据操作。这种批处理导致一次传输更多的数据并分摊开销，所以能超过 eBPF socket 加速之后吞吐量。但是随着发送消息越来越大，超过 MSS，TCP/IP 栈就会失去其批处理优势，在这些大数据包发送大小下，**eBPF socket 加速凭借其低开销远远超过启用 Nagle 算法的 TCP/IP 栈的吞吐量。**  

---

[你真的会使用 ChatGPT 吗？ | 第一章：Guidelines for Prompting](https://changchen.me/blog/20230502/chatgpt-prompt-eng-l2/)

感觉有点像 [How-To-Ask-Questions-The-Smart-Way/README-zh_CN.md at main · ryanhanwu/How-To-Ask-Questions-The-Smart-Way · GitHub](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md)，要把问题说清楚，也要说自己已经想到的一些方向（可行方向）。

---

[谈研发人员怎么专注](https://manateelazycat.github.io/think/2023/05/10/developer-focus.html)

各种意义上的要减少外界干扰，养成专注的习惯，一次只做一件事。

> 这就是佛家说的不要有杂念， 我这么多年看到太多天赋非常好的工程师心念不专注， 被比较之心、 膨胀之心、 贪念之心、 执着之心分走太多能量， 表面看起来很努力很勤奋， 实际内心的能量并没有专注在当前的过程中， 消耗很多能量却没有专注做事情是一个人最大的浪费呀。 所以， 专心吃饭、 专心走路、 专心做家务这些看似最和工程师无关的事情， 反而最容易锻炼我们专注当下的心念。  

---

[NixOS 与 Nix Flakes 新手入门 - This Cute World](https://thiscute.world/posts/nixos-and-flake-basics/)

[[NixOS]] 真正的 101，但是上手成本还是太高了。

---

[New talk: Learning DNS in 10 years](https://jvns.ca/blog/2023/05/08/new-talk-learning-dns-in-10-years/)

通过[[DNS]]作为例子，来介绍如何学习新的事物：使用、观察、保留疑问、调查、阅读规范，最后尝试自己实现一个简单的 demo 来更好的理解。

---


[SQLAlchemy 与 Pyright 相爱相杀的故事 | Henry Z's blog~](https://changchen.me/blog/20230503/python-type-hinting-stubs/)
> Try to resolve using stubs or inlined types found within installed packages.  
For a given package, try to resolve first using a stub package. Stub packages, as defined in PEP 561, are named the same as the original package but with “-stubs” appended.  

> 简而言之类似 java 中的泛型（generics），当 Column 的类型定义为 `Type[TypeEngine[_T]]` 时，强制约束返回的类型为 `T`。  

---
[Using buffers, windows, and tabs efficiently in Vim - DEV Community](https://dev.to/iggredible/using-buffers-windows-and-tabs-efficiently-in-vim-56jc)

[[vim]] 的 `window` `buffer` `tab` 的使用方式，已经他们之间的差异。最近重新体验了一下 Vim，使用 Neovim，发现现在的插件生态已经很好了。

---

[How I Made Twitter Back-end - DEV Community](https://dev.to/leoantony72/twitter-back-end-design-274b)

如何使用 [[Postgres]]，[[redis]]，[[Rabbitmq]] 构建一个[[Twitter]] 的 demo，针对[[timeline]] 进行特殊处理。

---

[Kubernetes Meets Event-Driven Ansible](https://www.ansible.com/blog/kubernetes-meets-event-driven-ansible)

[[事件驱动]][[Ansible]]，可以指定 Source，Rule和 Action 来进行一些自动化的处理，但是现在大部分涉及到 [[kubernetes]] 的场景应该都是独立的去实现 Operator 了吧，没想到什么场景会这么用。

另外这里的进程管理看上去也是一个问题。


### 生活

[这次在北京玩回来，在经历了景区排队，地铁先下后上，和有些景区的池塘不让喂小鱼但有人喂后。儿子问了我们一个看起来好回答但面对 5 岁多的孩子却不知道怎么回答才好的问题：
“妈妈，为什么别人都不遵守规则，但是但是，我们要遵守”](https://twitter.com/yihong0618/status/1656089584428802048)

[HowardSu](https://twitter.com/HowardSu) 的回复：这个问题有个标准范式供您参考，因为遵守社会[[规则]]意味着承担了相对少的风险，规则并不是绝对的，而是为了避免麻烦的，所以选择遵守规则就把遇到麻烦的概率降低了，不遵守规则提高了遇到麻烦的概率，这时候可以顺便提出数学期望这个概念，概率乘以收益等于数学期望。计算之后就会发现遵守规则收益高

---

[我的笔记管理法 | Randy's Blog](https://lutaonan.com/blog/how-do-i-take-note/)

不只是笔记管理，更多的是信息管理方式。我个人日常获取信息的渠道主要是 [[RSS]] 和 [[Twitter]]，如果看到感兴趣的，会直接保存到 [[Notion]]中，保存阶段不进行标记，定期的阅读整理 [[Notion]]中保存的文章，当阅读完成或了解完成后，进行 Tag 标记，并同步把文章链接和想法记录到 [[Logseq]] 中。

感觉如何做好笔记的 Tag 是一门学问。

## 书影

《深入理解 Linux 网络》，本周没有继续读。

《大医·日出篇》，看了开头。

《扑克脸 第一季》，看了第一集，感觉没有那么好看，反而烟嗓让我听着不是很舒服，应该不会继续看下去。
