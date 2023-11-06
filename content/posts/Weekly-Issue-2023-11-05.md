---
title: Weekly Issue 2023-11-05
date: 2023-11-05
tags:
- Weekly
description: 
---


## 文章

### 技术

[Avoid Load-bearing Shell Scripts | Ben Congdon](https://benjamincongdon.me/blog/2023/10/29/Avoid-Load-bearing-Shell-Scripts/)

尽量避免使用[[Shell]] 来实现某些功能，虽然在 demo or 早起阶段，[[Shell]] 可以非常快速的实现一些功能，但是随着时间的推移，它会变得非常庞大，且无法测试，迟早需要重写它，重写的越晚，成本就越高。

拿我们内部的功能举例，我们需要进行磁盘的管理，早期的时候，因为磁盘分区比较简单，所以直接使用 shell & lsblk &  parted  就可以工作，而且工作的还不错，后来慢慢的，加了更多的分区类型，shell 维护起来就非常的痛苦了，我们需要进行大量的命令行解析的工作，且要处理大量的异常场景，比如某个磁盘的某个属性的值不存在。中间配合 sed & awk 做了很多黑魔法，虽然它现在工作的很好，我们也围绕这个功能写了大量的端到端测试，但是我对这部分代码仍然是没有底。

---

[crates.io Postmortem: Broken Crate Downloads | Inside Rust Blog](https://blog.rust-lang.org/inside-rust/2023/07/21/crates-io-postmortem.html)

[[crates.io]] [[事故分析]]，一个错误的 PR 导致 13min 宕机，其中分析为什么的阶段，连续的 Why 的答案也很无奈，大家都一样（此处不能用“草台班子”）：没有单元测试、没有 reviewer、没有测试环境、全手动测试。

因为在社交媒体上使用了“草台班子”有所不妥，此处说明，我理解的草台与人无关，特指流程上的草台。此处是我的臆想，如果一个人说：我所在的公司，（部分代码）没有单元测试、没有 reviewer 直接合并代码、全手工测试，可能会被大家叫草台班子吧。

---


[Top 10 common Dockerfile linting issues](https://depot.dev/blog/dockerfile-linting-issues)

使用 hadolint 遇到的常见 [[Dockerfile]] lint 问题，其中大部分都是包管理器的使用问题，什么时候应该使用 cache，什么时候不应该使用 cache。其中 DL3027 推荐使用 `apt-get/apt-cache` 替代 `apt` ，理由是 `apt` 是面向最终用户的接口，可能会发生变化，前者更稳定。

`apt-get install --no-install-recommends`, `pip install --no-cache-dir`。

---

[How I Bluefin: Using the ultimate developer Linux](https://brian.dev/how-i-bluefin/)

使用[[Bluefin]] 配合 [[Fleek]] 来管理自己的开发机器，其中提到的 `~` 代替 `/` 是 [[ostree]] 场景下不得不的事情。（上周尝试了 [[Bluefin]] 还有些问题，也许应该自己基于 [[FCOS]] 来维护一个 [[ostree]]。

---

[Tracking SQLite Database Changes in Git | Garrit's Notes](https://garrit.xyz/posts/2023-11-01-tracking-sqlite-database-changes-in-git)

通过自定义[[git]] `diff` ，来显示 [[SQLite]] 文本化差异。

```gitconfig
[diff "sqlite3"]
        binary = true
        textconv = "echo .dump | sqlite3"
```

```.gitattributes
*.sqlite diff=sqlite3
```

---

[Ready for Flight: Announcing Finch 1.0 GA! | AWS Open Source Blog](https://aws.amazon.com/cn/blogs/opensource/ready-for-flight-announcing-finch-1-0-ga/)

[[Finch]] 1.0 GA ，支持使用 Seekable OCI [[SOCI]] 来通过延迟加载容器 image 加速启动。
同时提供了很多 AWS CDK 相关的功能便于开发。

---

[基于荷尔蒙开发的开源项目 - EAimTY's Blog](https://www.eaimty.com/2023/opensource-project-based-on-hormone/)

[[TUIC]] 作者的开源总结文，感觉做相关的开源项目，要尽量的避免自己受到一些评论的影响才可以好受些，太难了。

---

[软件开发小段子四则 | Piglei](https://www.piglei.com/articles/programming-jokes-1/)  

大师与学徒的段子。盲打这个技能感觉是所有人必备的，现在手写文字可能已经不顺畅了，对生活影响不大，但如果不能快速的打出你想要表达的文字，影响就太大了（很有可能在与 xx 对线的过程中因为速度过慢而懊恼）。         

---

[Confusing git terminology](https://jvns.ca/blog/2023/11/01/confusing-git-terminology/)

解释了很多 [[git]] 术语，感觉常用的操作很少，偶尔需要一些特殊操作现查就可以了。 reflog 很重要。

---

[一篇精彩的推文，一年后的推特工程实践。 - Xiaowen.Z Deployed](https://xiaowenz.com/blog/2023/10/twitter-engineering-after-a-year/)

[[Twitter]] 最近一年的变化比之前几年都大，还得等等看后续，现在还太早了。

---



### 生活

[The product manager role is a mistake - Software Product Development Pills](https://sollecitom.github.io/software-product-development-blog/posts/2023/2023-10-21-product-manager-role-is-a-mistake/)

读的半知半解，没有完全理解作者的意图，一个好的 [[PM]] 对于产品功能上的帮助是非常大的，无论是方向性还是细节处理，思考维度是很好的补充。

---

[The Written Word · Collab Fund](https://collabfund.com/blog/the-written-word/)

写作是一门艺术，而艺术是主观的。人们记住的不是你写的内容，而是他们读它时的感受。人们不记得书籍、文章，记住的是句子。大多数好的写作是良好阅读的副产品。

---

## 书影

《恶中之恶》，算是中规中矩吧，没有特别出彩的地方，感觉如果拍成一个大电影，会好很多？

