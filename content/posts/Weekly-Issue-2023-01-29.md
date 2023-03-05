---
title: Weekly Issue 2023-01-29
date: 2023-01-29 19:00:00
tags:
- Weekly
description: Prisma 真不错啊。
---


## 文章

### 技术

[iptables详解（1）：iptables概念-朱双印博客](https://www.zsythink.net/archives/1199)   

[[朱双印]] 关于 [[iptables]] 的基本介绍。

---

[领英上的David Masover: #opentowork | 747 条评论](https://www.linkedin.com/posts/david-masover-253a597_opentowork-activity-7023167482353881089-zI0U/)    

来自 [[Google]]真实事件，真正的 [[SRE]]，和这种人工作应该很幸福。

---

[为什么镜像可以 pull 下来但是在 manifest inspect 的时候提示 no such manifest？—— Docker Buildx Attestations 检修记](https://nova.moe/docker-attestation/)    

[[Buildkit]] 新特性引发的兼容性问题。     
> Buildx v0.10 enables support for a minimal SLSA Provenance attestation, which requires support for OCI-compliant multi-platform images. This may introduce issues with registry and runtime support (e.g. GCR and Lambda). You can optionally disable the default provenance attestation functionality using provenance: false.

---

[Disable the re-registering of HA disabled VMs on other hosts! | Yellow Bricks](https://www.yellow-bricks.com/2023/01/24/disable-the-re-registering-of-ha-disabled-vms-on-other-hosts/)     

[[ESXi]] 虚拟机[[HA]]das.reregisterrestartdisabledvms	
：当 vSphere HA 在特定 VM 上停用时，此选项可确保 VM 在发生故障后在另一台主机上注册。这使您可以启动该 VM，而无需手动重新注册它。

---

[What Doesn't Fit in Git](https://matt-rickard.com/what-doesnt-fit-in-git)

什么不应该放到 [[git]]中，比如 container image。其中提到了配置文件，理由是如果你部署了一个 Deployment，并且配置了 auto-scale group，现在因为流量变化，导致副本数发生变化，是否要同步更新到配置文件中？现在[[GitOps]] 的用户应该是很多的，搜了一下没有搜到最佳实践是啥。。

---

[谈谈 Mastodon、Fediverse 和 ActivityPub - zu1k](https://zu1k.com/posts/tutorials/p2p/fediverse/)

越来越多的用户抛弃了 [[Twitter]] 去了 [[Mastodon]]。

---

[【Prisma，下一代ORM，不仅仅是ORM（下篇） | Linbudu's Blog](https://linbudu.top/prisma-02)    

介绍 [[Prisma]] 相关内容，其中的 [[github]] 仓库中有不少示例。

---

[寫 Web 也可以用 Makefile：好好管理你的環境流程 | 小克's 部落格](https://blog.goodjack.tw/2023/01/use-makefile-to-manage-workflows-for-web-projects.html)

[[Makefile]] 就属于那种不喜欢但又到处都有的东西。

---

[一次线上内存使用率异常问题排查](https://fanlv.fun/2022/06/02/golang-pprof-mem/)

从[[TCMalloc]] 到 [[mmap]] ，到 [[Golang]] 中的内存分配都有说明，最后判定问题是内存已经 GC，但是没有归还给操作系统(scavenging)。

---

[GraphQL 客户端缓存的正确打开方式 | Riptide](http://www.myriptide.com/smart-cache-cn/)   

[[GraphQL]] 客户端缓存处理。

---

[Hardware is fun again](https://world.hey.com/dhh/hardware-is-fun-again-b819d0b4)

> We're exploring moving both caching and job queuing at Basecamp to NVMe instead of RAM. The latency is now close enough that the advantages of abundant, fast NVMe storage wins. We just bought some 12TB NVMe Gen 4 cards for $2,390. 12TB! Using the new [E1/E3 NVMe form factor](https://www.servethehome.com/e1-and-e3-edsff-to-take-over-from-m-2-and-2-5-in-ssds-kioxia/), we're now looking at the possibility of a petabyte's worth of NVMe storage in a single rack server for around $200K. That's bananas!


### 生活


[人人都想功成名就 但可能碌碌无为才是常态 五年 好遗憾啊_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV16Y4y1o7nj/)    

> “一个电话就可以让我们8个人一整年的努力化为一场空”。

最近几年冲浪冲不动了，经常去小鸡词典上面搜索相关的梗，结果没有了。

---



## 书影


《三体Ⅲ》，终于看完了，真是长啊。

《仙症》，东北文艺复兴，郑执的短篇小说，其中看着很有感触，东三省的状态都是差不多的。

《满江红》，反转太多，最后的几个反转太容易猜出了。

《流浪地球2》，大场面，视听效果满分。

《2001太空漫游》，看不懂。


