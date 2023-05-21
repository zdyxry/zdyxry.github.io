---
title: Weekly Issue 2023-05-21
date: 2023-05-21
tags:
- Weekly
description: 
---


## 文章

### 技术

[Slack Said It Had 100% Uptime. Did It Really? - Metrist](https://metrist.io/blog/slack-said-it-had-100-uptime-did-it-really/)

[[Slack]] 报告自己的在线时间是100%，但是实际上不是这样， [[Slack]] 自己对于停机时间的定义有些狭隘，也许是为了 100% 看着好看，说出去比较好听，但是实际上作为 [[Slack]] 的用户体验并不是这样的，部分用户确实是经历了停机时间的。作为 [[SaaS]] 服务商应该以用户体验为准。

像[[metrist]] 这类产品，如果各家服务商自己的 status 页面提供了 RSS 接口，是不是就可以被替代了。


---

[几种使用Go发送IP包的方法](https://colobu.com/2023/05/13/send-IP-packets-in-Go/)

操作 IP packet 的方式。

---


[Sandboxing and Workload Isolation · Fly](https://fly.io/blog/sandboxing-and-workload-isolation/)

有 [[Container]] 的情况下还是用 [[Container]]，没有的话推荐使用 `systemd-nspawn` ，毕竟 [[systemd]] 是现在的事实标准，不需要额外的依赖。

---

[Investigating the impact of HTTP3 on network latency for search - Dropbox](https://dropbox.tech/frontend/investigating-the-impact-of-http3-on-network-latency-for-search)

[[Dropbox]] 关于 [[HTTP/3]] 的测试数据，在可能发生数据包丢失的网络环境中， [[HTTP/3]]针对 head-of-line blocking 的处理显著降低了延迟。


### 生活

[R.I.P. 陈皓 - laike9m's blog](https://laike9m.com/blog/rip-chen-hao,147/)

最近身边突然很多人离世，有的人很突然，有的人是早就知道，但是真正离开也很难受。认知中像陈皓g这个级别，还在持续的输出观点的人已经很少了，不只是技术观点，有很多人生观点也是很受用。大家还是要坚持锻炼，保持健康。

查了一下 [[coolshell]] 的域名到 2028 年过期，不知道后续是否有人管理，先爬取一波吧。我之前有类似的担心，所以blog 一直使用的是 github page 默认的 github.io 。

---


[关于 TweetID:1658453862561501184 中典型诡辩论部分的拆解 | Kivinsae's Nest](https://www.kivinsae.com/2023/05/17/2023-05-17-no_sophism/)

很多事情，看上去第一感觉是毫无逻辑，如果硬要说出个一二三，可能要仔细想想才可以，这篇文章对于分析一段话是一个很好的例子。同理最近的脱口秀的事情也是一样，事情的走向太快以至于无法真正的想清楚。

---

[纪念陈皓（左耳朵耗子） | 陈硕的博客](https://giantchen.wordpress.com/2023/05/18/haoel/)

[[左耳朵耗子]]因为心梗去世了，很多人写了纪念文章。期望 [[AI]] 技术的发展可以真正的存在数字生命吧。

---

[冒犯不是艺术。 - Xiaowen.Z Deployed](https://xiaowenz.com/blog/2023/05/stand-up/)

最近有几个关于[[冒犯]]的讨论，微博上东东枪也做了回答。我对于这部分一直没有一个明确的认知体系，感觉需要汇总整理一下。

---

[冒犯由谁定义 - ADoyle 观思言](https://talks.adoyle.me/-ae798ee321e343168dcb1a2c96cc04d8)

[[冒犯]] 可以达成共识么？可能在第三者可能，但是在当事人双方感觉有些困难。在表达观点时，要尽可能的清楚自己的观点可能会产生的影响，同时也要有心理准备，不论说什么，都存在不认同你观点的人。


## 书影

《深入理解 Linux 网络》，本周没有继续读。

《大医·日出篇》，本周没有继续读。

《最佳出价》，爱情的陷阱，这样的好导演请多来一点。

《疾速追杀4》，打打打，杀杀杀。杀手世界的世界观还不太明确。