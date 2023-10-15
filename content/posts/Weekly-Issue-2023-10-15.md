---
title: Weekly Issue 2023-10-15
date: 2023-10-15
tags:
- Weekly
description: 
---


## 文章

### 技术

[Bootstrap an Air Gapped Cluster With Kubeadm | Kubernetes](https://kubernetes.io/blog/2023/10/12/bootstrap-an-air-gapped-cluster-with-kubeadm/)

官方下场，手把手教你如何部署一个离线[[kubernetes]] 集群。

---

[2023 年 10 月 4 日 1.1.1.1 查询失败](https://blog.cloudflare.com/zh-cn/1-1-1-1-lookup-failures-on-october-4th-2023-zh-cn/)

[[CloudFlare]] `1.1.1.1` 因为新的资源记录类型 `ZONEMD` 无法解析，导致使用旧版本的记录，最后由于 [[DNSSEC]] 签名过期导致故障。 这里在设计时没有考虑增加对应的报警项，导致这个场景出现的时候完全静默。。

---
[mmproxy - Creative Linux routing to preserve client IP addresses in L7 proxies](https://blog.cloudflare.com/mmproxy-creative-way-of-preserving-client-ips-in-spectrum/)

解决经过代理之后客户端源 IP 丢失的问题。使用了 Linux 的 IP_TRANSPARENT 套接字选项来执行源 IP 欺骗，自定义路由表来强制返回流量路由到回环接口。

---

[Deconstructing Type Parameters - The Go Programming Language](https://go.dev/blog/deconstructing-type-parameters)

[[Golang]] 使用泛型实现 Slice 的 `Clone` 方法的介绍。（但是现在还没有真正使用过泛型。

```Go
	func Clone[S ~[]E, E any](s S) S {
	    return append(s[:0:0], s...)
	}
```

---

[什么是拥塞控制算法，ECN 又是什么？ – Yachen's Blog](https://yach.me/2023/10/14/ccn-and-ecn/)

[[Hysteria]] 通过采用自己实现拥塞控制算法 **Brutal** 来保证网络通信最大速度。

---

[Why HTTP/3 is eating the world | APNIC Blog](https://blog.apnic.net/2023/09/25/why-http-3-is-eating-the-world/)

[[HTTP/3]] 的占比已经到了19% 。文中提到了 [[QUIC]] 与[[TCP]] 关于 [[TLS]] 的差异。对于 TCP，TLS 仅加密实际的 HTTP 数据。通过 QUIC，TLS 还对 QUIC 协议本身的大部分进行加密。这意味着 TCP 中所有中间件都可见（且可更改）的元数据（例如数据包编号和连接关闭信号）现在仅可供 QUIC 中的客户端和服务器使用。

我们需要的不是 [[HTTP/3]] 而是 [[QUIC]]。 

---


[Editing stuff in prod](https://rachelbythebay.com/w/2022/03/05/prod/)

虽然日常工作中禁止 dev 通过 ssh 登录生产环境去执行一些动作，但是有时候还是避免不了（一时想不到，但总是存在的）。

> Editing files in prod to develop them? That's bad news. Deliberately rigging tunnels to spoof a connection from prod? That's also bad news. Having to do them to get your job done? You might be in the bad place.

---

### 生活

[来日本的第一周 - rxliuli blog](https://blog.rxliuli.com/p/f1210fce6cb4447da12699dfc6f176a4/)

除了提到饮食和消费上的差异之外，电子信息化也是体验上的不同，看上去只带手机出门是不太可行的。很多看上去很美好的事物，还是要实际体验之后才能有更确切的感受。

---

[Buy wisely — Steph Ango](https://stephango.com/buy-wisely)

把物品的价格除以使用预期的次数,算出每次使用的成本。对比一次性物品和可长期使用的物品,后者虽价格较高但在长期使用中每次使用的实际成本会更低。有些东西可能无法很好评估成本，可以先计算使用频率，尽可能的降低到每次使用的成本接近于 0 。

---

[CyberClip #43 自我人类学](https://shyrz.me/cyberclip-43-self-anthropology/)

通过记录田野日志，来不断地观察自己。这应该就是 [[Flomo]] 的理念吧。

---

[旧文，移动端最好的游戏，《Dream Quest》以及其它 · Issue #274 · yihong0618/gitblog · GitHub](https://github.com/yihong0618/gitblog/issues/274)

[[rogue like]] 游戏是有一定的成瘾性的，个人觉得数值设定是其中比较关键的点。国庆期间在玩[[吸血鬼幸存者]] ，确实是我最近几年以来，短时间内玩的时间最长的游戏了，预期是比较低的，没想到玩了很久，现在也会时不时的玩上一把。

---

[互联网生存法则：不与他人争辩 | 印记](https://yinji.org/5163.html)

与我现在的状态是类似的，网络上的信息只是用来了解世界，了解一些其他的观点，防止自己每天只看到自己预期看到的事情，导致对一些事情的走向的观点过于单一。


---

[100 Ways To Live Better – PUTANUMONIT](https://putanumonit.com/2019/12/30/100-ways-to-live-better/)

- 收集朋友们的反馈；
- 学习一些即兴表演（一直想参与 Yes And）；
- 适当的跳过不喜欢的内容（不限于播客、书籍、电影）不要因为朋友在看而为了找话题去看糟糕的内容；
- 适当的发表自己的想法；
- 限制听到政治新闻的频率；
- 买一块 20 每月的肥皂，看看一件同类型价格上限的物品是否有什么特别（有趣）；

## 书影

《目标》， 非常典型的韩国电影，过程中会有紧张的感觉， 但话题太极端了，及格分。
