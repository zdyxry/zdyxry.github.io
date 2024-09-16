---
title: Weekly Issue-迎中秋
date: 2024-09-15
tags:
- Weekly
description:  
---


## 文章

### 技术

[Goodbye Tinder, hello Strava: have ‘hobby’ apps become the new social networks? | Apps | The Guardian](https://www.theguardian.com/technology/article/2024/sep/08/goodbye-tinder-hello-strava-have-hobby-apps-become-the-new-social-networks)

> Strava 的用户数量[在一年内增长了 20%](https://www.bnnbloomberg.ca/business/2024/08/31/strava-and-letterboxd-surge-as-users-crave-social-media-refuge/#:~:text=Audiences%20for%20niche%20platforms%20jumped,year%20respectively%2C%20Sensor%20Tower%20reported.) 。这一成功促使它添加了一个消息工具，供用户保持联系，同时记录他们的锻炼情况。通过多个第三方应用程序访问的针织社交网络[Ravelry](https://www.ravelry.com/about)拥有超过 900 万用户。 Goodreads 拥有超过 1.5 亿会员。

这种兴趣社区，不就是豆瓣么？现在的增长很有可能是因为他们还处于一个小众的状态，当大规模的用户引入后，就会带来严苛的言论审核，从而引发现有用户的逃离，去追寻下一个 App。

---

[uv under discussion on Mastodon](https://simonwillison.net/2024/Sep/8/uv-under-discussion-on-mastodon/)

社区成员对于 [[uv]] 有很多担忧，其中最大的问题是 uv 背后的公司 [[Astral]] 是拿了投资的，但是现在 [[Astral]] 还没有明确的商业计划，导致不敢使用。[[Astral]] 只是简单的举例说：可能提供 private package registry 来盈利。例子只是一个例子，还有非常多的不确定性。

---

[服务网格架构：Sidecar vs. Sidecarless，谁才是未来？ - Jimmy Song](https://jimmysong.io/blog/service-mesh-sidecar-vs-sidecarless-debate/)

>Linkerd：强调 sidecar 的安全隔离和性能稳定性，对 eBPF 无 sidecar 模式持批评态度，认为其复杂性和安全风险增加。
>Istio：引入 Ambient Mesh，部分采用无 sidecar 方法，以降低复杂性和提高性能，但仍保留 sidecar 的部分功能，体现出对现有 sidecar 架构的保留与创新。
>Cilium：主张通过 eBPF 无 sidecar 模式来优化网络性能和安全性，简化操作，同时保持对多种协议的支持，推动服务网格功能集成到 Linux 内核中。

目前关于 [[sidecar]] 和 [[sidecarless]] 的观点总结。

不知道为什么，这篇文章给我一种是 AI 写出来的感觉。

---

[Here’s our first look at Apple’s in-the-box iPhone updating machine](https://www.theverge.com/2024/3/27/24113561/apple-retail-presto-iphone-update-machine)

[[Apple]] 的 Presto 机器（或者叫系统？）可以通过无线的方式更新还没有拆封的手机，用到了 MagSafe 和 NFC 或者其他的方式，来完成开机、更新、关机一系列动作。

怎么做到的？

---

[How GitHub monopolized code hosting](https://graphite.dev/blog/github-monopoly-on-code-hosting?ref=blog.gitbutler.com)
[Why GitHub Actually Won](https://blog.gitbutler.com/why-github-actually-won/)

为什么 [[Github]] 成为了代码托管的赢家？当时主流代码托管服务不支持 Git，Ruby 社区的支持，社交属性。在合适的时间点推出了合适的产品，什么是“合适”，如何找到这个时间点，感觉都是巧合，直觉。

---

[[心得] SUSE面試經驗 - 看板 Soft\_Job - 批踢踢實業坊](https://www.ptt.cc/bbs/Soft_Job/M.1725988955.A.012.html)

[[SUSE]] [[Rancher]] 面试分配的任务，是 [[Longhorn]] 一个停留了两年的 issue，没有什么描述，从零开始设计，且是下一个版本必须要包含的内容。离谱。

---

[storage - Will reading data cause SSD's to wear out? - Super User](https://superuser.com/questions/440171/will-reading-data-cause-ssds-to-wear-out/440219#440219)

读取数据会导致 [[SSD]] 寿命吗？不会有影响，读取不会影响电子状态，写入会。

---
[Reasons I still love the fish shell](https://jvns.ca/blog/2024/09/12/reasons-i--still--love-fish/)

[[fish]] 在易用性上确实很好，开箱即用，我在 [[zsh]] 使用 `zsh-autosuggestions` 来达到 fish 自动补全历史命令的能力。我不用 fish 的原因是有些 POSIX 语法不兼容，比如 `cmd1 && cmd2` 这类的，不过看上去现在已经有改变。

原来 fish 的全称是：the friendly interactive shell。

---

[Migrating from AWS to Self-Hosting ⚡ Zig Programming Language](https://ziglang.org/news/migrate-to-self-hosting/)

>If the website is temporarily unavailable because of too much traffic, so be it. If it gets accidentally DDoS'd by too many people not [properly caching their CI runs](https://ziggit.dev/t/github-actions-mlugg-setup-zig/4659), so be it.

[[Ziglang]] 将 `ziglang.org` 从 AWS S3 + CloudFront 迁移到了一台 [[Hetzner]] VPS 上。他们的心态真不错，`so be it.`。

---

[Go Enums Suck](https://www.zarl.dev/articles/enums)
[Go Enums Still Suck](https://www.zarl.dev/articles/enums-take-two)
[Enums in Go | Dizzy zone](https://dizzy.zone/2024/01/26/Enums-in-Go/)

关于如何在 [[Golang]] 中实现 Enum 的几篇文章，可以使用 [GitHub - zarldev/goenums: Type Safe Enum generator for Go](https://github.com/zarldev/goenums) 或者 [GitHub - abice/go-enum: An enum generator for go](https://github.com/abice/go-enum) 来快速生成。

---


### 生活

[Apple Hearing Study shares preliminary insights on tinnitus - Apple](https://www.apple.com/newsroom/2024/05/apple-hearing-study-shares-preliminary-insights-on-tinnitus/)

[[Apple]] 对耳鸣的调查结果。一共有 16w 人接受了调查，77.6%的人经历过耳鸣，大约有 15% 的人每天都会经历耳鸣, 55 岁以上的人有 35.8%的人经常耳鸣。缓解耳鸣的方式有：白噪音，自然声音，冥想。

耳鸣没有明确的病因，也没有什么有效的预防手段，减少平时的音量大小是最常见的方式。

---
[山西大同五日游 - 花開未央](https://sizheng.org/travel/shanxi-datong-5-day-tour/)

[[大同]] [[游记]]，山西最近挺火热的，加上《黑神话悟空》游戏，又出圈了。

感觉需要做很多功课才会体验很好。

---

[不上班的第一年 | Randy's Blog | Randy's Blog](https://lutaonan.com/blog/a-year-off-work/)

自洽。

---

[极空间 Z4 Pro 两个月使用体验分享](https://atbug.com/z4-pro-two-months-experience/)

极空间的易用性真不错，同事也有好几个买了的。一直在想是否有必要搞一个 [[NAS]]，说服自己不需要的方式就是“你现在还在想这个问题，那就是不需要”。

---


## 书影


## 碎碎念

* 目前我的一双鞋的寿命大概是 9 个月，到 9 个月之后，无论是鞋底还是后跟处的棉花，就不行了。
* 在讨论的时候，需要把事实和观点区分开来。
* 看了恒哈图乐队的演出，之前一直以为呼麦是大老粗，没想到还可以这么灵动。

