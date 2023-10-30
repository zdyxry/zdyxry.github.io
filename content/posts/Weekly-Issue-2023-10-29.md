---
title: Weekly Issue 2023-10-29
date: 2023-10-29
tags:
- Weekly
description: 
---


## 文章

### 技术

[2023 年秋季学期迎新会 & TUNA 镜像站服务架构演进](https://www.youtube.com/watch?v=_xFuJApjFh4)

[[Tuna]] 镜像站架构演进，一直到 2018 年之前，都是不稳定的，感觉记忆出现了偏差。

---

[Analyzing multi-gigabyte JSON files locally | thenybble.de](https://thenybble.de/posts/json-analysis/)

作者有一个较大的 json 文件，使用 `jq` 配合 `parallel` 来处理，后来选择了 `Dask` 来处理，处理之后可以使用 Python 来进行数据操作。也许应该考虑 [[DuckDB]] 来操作，看过的例子都是不错。

---

[The Ruff Formatter: An extremely fast, Black-compatible Python formatter](https://astral.sh/blog/the-ruff-formatter)

[[Ruff]] 提供的 Formatter 的支持，99.9% 兼容 Black，但是比 Black 快30 倍以上。

---

[What DevRel means to me - Xe Iaso](https://xeiaso.net/blog/devrel/)

[[Xe]] 关于 [[DevRel]]  的想法，宣传公司的产品和技术，围绕该产品或技术建立和培育社区。DevRel 与开发者沟通首先需要真诚，建立社区和信任需要时间，但当积累到一定程度会产生爆发式增长，很难量化。

---

[You Can't Control Your Data in the Cloud](https://karl-voit.at/cloud/)

尽管各个大公司提供了安全措施，但将个人数据委托给第三方仍然可能导致隐私问题和失去控制权l。文中列举了 N 个大公司的黑历史，合订本。

---

[HashiCorp CEO predicts OSS-free Silicon Valley unless...](https://www.thestack.technology/hashicorp-ceo-predicts-oss-free-silicon-valley-unless-the-open-source-model-evolves/)

对公司来说，赚钱才是正道理，不赚钱什么开源不开源的，都是扯淡的。

---

[網站前端打 API 時把密碼加密，有意義嗎？ - Huli's blog](https://blog.huli.tw/2023/01/10/security-of-encrypt-or-hash-password-in-client-side/)

最近也收到了类似的需求，这篇文章总结的很好，无论是否有 HTTPS，在 client dr 发送密码前把密码加密或者 hash，确实能够增加安全性，实际上这么做的公司大部分都是金融系统。

---

[The Negative Impact of Mobile-First Web Design on Desktop](https://www.nngroup.com/articles/content-dispersion/)

移动优先设计的网页在桌面环境下,内容会变得过于扩散和拉长,图像和文字变大,页面变长需要更多滚动,这就是“内容扩散”。内容扩散是一种取舍，会增加交互成本，信息密度降低，相对的也可以让用户专注于部分具体内容。

---

[The Cloud Computer / Oxide](https://oxide.computer/blog/the-cloud-computer)

[[0xide]] 作为一个播客公司，终于发布自己的产品了，售卖整个机柜，包含服务器、机架、交换机，没有线缆（硬件的更换成本岂不是高到天际？）。所有的软件全部开源。

Hackernews 的评论：So just hyperconverged infrastructure with a cute name?

---

[sed 原地替换和符号连接的一个小坑 | 卡瓦邦噶！](https://www.kawabangga.com/posts/5462)

当 [[sed]] 操作的文件是软链接时，需要添加 `--follow-symlinks` 参数来保持链接正确。 类似的现象在其他的文本修改工具都存在。

---

[Announcing Project Bluefin](https://www.ypsidanger.com/announcing-project-bluefin/)

通过定制[[Fedora]] SilverBlue 的 OSTree ，结合一些如 [[Flatpak]], [[devbox]] 的发行版，包含了对一些驱动的支持，如果只是需要开发机的话，建议直接基于 SilverBlue 来自定义比较好，都是写 Dockerfile/Containerfile ，感觉上应该差不多。

---

[How Netflix's Container Platform Connects Linux Kernel Panics to Kubernetes Pods | Netflix TechBlog](https://netflixtechblog.com/kubernetes-and-kernel-panics-ed620b9c6225)

使用[[netconsole]] 来捕捉 kernel panic 发生时对 Pod 的影响。

---


[NixOS for the Impatient](https://borretti.me/article/nixos-for-the-impatient)

相较于其他的各种 [[NixOS]]的文章，作者的配置和说明朴实无华，非常的简单，Dotfiles 的目录结构也非常的清晰，适合参考。

---

### 生活
[赵本山 厨子与掌门](https://web.archive.org/web/20231023001417/https://mp.weixin.qq.com/s/I6gYyKAJ8LK6FT4B68u27w)

>伴着打打杀杀的背景音，鼾声响了起来。他没有看到剧终超现实的那幕，对话结束，大侠掌门的影像渐渐褪去，只剩厨子一个人坐着。

真诚。

---

[怎么让大公司不抄你 | 歌词经理](https://blog.lyric.im/p/how-to-prevent-big-companies-from-copying-you)

大公司追求变化是一件双刃剑，要考虑自身的影响力。需要让用户喜欢产品，喜欢产品所表达的氛围、文化、价值观。

>现在这个时代，追求共同价值观，即使在普通的消费决策中的角色，也变得越来越重要——大家不再仅仅追求产品或服务的功能性，也不仅仅看中价格，更开始在意的是与产品之间的情感连接、社群文化、共同价值观。

---



## 书影


《浪漫的体质》，中间有些疲软，没支撑起来，感觉如果女导演的戏份如果提前一些介入，会好很多。
