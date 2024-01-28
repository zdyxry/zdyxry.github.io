---
title: Weekly Issue 2024-01-28
date: 2024-01-28
tags:
- Weekly
description:  疲惫，年后再说吧。
---


## 文章

### 技术

[[ih] Dave Mills has passed away](https://elists.isoc.org/pipermail/internet-history/2024-January/009265.html)

[[NTP]] 协议作者去世了。R.I.P.

---

[Which command did you run 1731 days ago? - by Thorsten Ball](https://registerspill.thorstenball.com/p/which-command-did-you-run-1731-days)

继上一篇聊 Shell 的启动速度之后，作者继续聊 Shell 的历史记录。

使用 Ctrl-r 配合 fzf 的使用体验是绝佳的，在自己的开发机上，可以快速地找到自己所有的历史记录。有些命令是低频但是复杂的，记录到笔记上当然可行，但又好像有点没必要。最近越来越觉得保留 Shell 历史记录是一件收益非常高的事情，推荐所有人都使用 [[Atuin]] 来保存自己的历史记录，或者直接用 Git Repo 来保存也可以。

如果你遇到 [[Atuin]] 配合 [[zsh]] 无法记录 `#` 前缀的命令，可以参考这个 Issue 来解决：[Add option to include commands that start with \`#\` in history · Issue #467 · atuinsh/atuin · GitHub](https://github.com/atuinsh/atuin/issues/467)

---


[High-speed 10Gbps full-mesh network based on USB4 for just $47.98 – Fang-Pen's coding note](https://fangpenlin.com/posts/2024/01/14/high-speed-usb4-mesh-network/)

作者使用 3 台  Miniforums 的 Venus UM790 Pro来搭建自己的 homelab 环境，存储网络使用 USB4 链接，最终可以达到 11 Gbps。

---

[2023：浏览器从 A 到 Z | Sukka's Blog](https://blog.skk.moe/post/2023-browser-from-a-to-z/)

依次在浏览器地址框中输入从 A 到 Z 字母，默认补全出来的是什么网站？

---

[Developer Relations Engineer · Fly](https://fly.io/jobs/developer-relations-engineer/)

可以通过[[Fly.io]] 的[[DevRel]] 的 JD，来感受一下什么是[[DevRel]] ，以及是做什么的。

擅于沟通，真诚，有想法，快速 PoC。

---

[GitHub - pi0/tired-maintainer: 🗒️ Notes from a tired maintainer](https://github.com/pi0/tired-maintainer)

[[开源软件]] 的维护者给出的建议。维护开源是一件很容易让人疲惫的事情。如果你的 PR/Issue 没有立即解决，请耐心等待一下；沟通的时候描述的事情尽可能的清晰完整，不要假设对方已经了解完整的上下文。

---



[Omitting dev dependencies in Go binaries | Redowan's Reflections](https://rednafi.com/go/omit_dev_dependencies_in_binaries/)

通过在 [[Golang]] 代码仓库中增加 tools.go 文件，在文件中声明依赖的工具，执行 `go mod tidy` 自动拉取相关依赖。[[kubernetes]] 示例：[kubernetes/hack/tools/tools.go at master · kubernetes/kubernetes · GitHub](https://github.com/kubernetes/kubernetes/blob/master/hack/tools/tools.go)

```
// go:build tools

package tools

import (
    // Dev dependencies
    _ "github.com/golangci/golangci-lint/cmd/golangci-lint"
    _ "mvdan.cc/gofumpt"
)

```

---



### 生活

[哄哄模拟器的完整复盘，火了，但一度让我很发愁 - 王登科-DK博客](https://greatdk.com/1962.html)

[[哄哄模拟器]] 作者的复盘。奇怪的流量入口居然是 QQ 群和 QQ 空间，这就是典型的私域流量了吧，真是神奇。最后因为腾讯的屏幕，导致流量急速下滑。

>值得注意的是，这些用户和我之前做产品所接触的用户完全不同，他们是以大学生，高中生和年轻人组成的，最大比例的年龄区间为16-20岁，我想这可能是一开始我用自己的渠道到处宣传效果并不好的原因，说到底，我已经快 30 岁了，我身边的很多人，也差不多这个年纪，30-40岁的用户，和十几二十岁的用户，感兴趣的点，需求，想法，都有很大不同。

>我听到了一种声音，可能带了一点情绪，我不确定，这种声音是：做这样不赚钱还亏钱的东西完全是浪费时间。首先我承认并且赞同人应该想办法赚钱过上更好的生活，同时我也认为我们应该保有更多的一些能力，例如感受趣味，它和赚钱不矛盾，但独立于赚钱这件事情。

---


## 书影

《好久没做》，韩剧，只有6集，之前是纯喜剧，靠着敲诈两个人来重新找回爱情的故事。


## 碎碎念

* 在给出建议前，先问一下为什么得到这样的结论，也许有一些自己没有考虑到的方面
* 不怕有问题，怕的是描述不清楚问题

