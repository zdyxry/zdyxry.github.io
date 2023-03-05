---
title: Weekly Issue 2023-01-15
date: 2023-01-15 19:00:00
tags:
- Weekly
description: 三个字，等过年。
---


## 文章

### 技术

[Deploy Kubernetes on Equinix Metal - Kubeadm via Userdata and Cloud-config](https://deploy.equinix.com/developers/guides/kubernetes-with-kubeadm/)   

[[Equinix]] 通过 [[cloud-init]] 配合 [[kubeadm]] 部署 [[kubernetes]] 集群。

---



[Buf | Introducing buf curl - Call your gRPC endpoints with the simplicity of buf](https://buf.build/blog/buf-curl)   

[[bufbuild]] 的 [[grpc]] 命令行。

---

[Scaling Kubernetes to Thousands of CRDs](https://blog.upbound.io/scaling-kubernetes-to-thousands-of-crds/)   

[[Crossplane]] 管理上千个 [[CRD]] 遇到的问题和改进方式。（现在好像一个 [[kubernetes]] 集群里面的 CRD 上百也不稀奇。

---

[简洁的 Bash Programming 技巧 - 团子的小窝](https://kodango.com/simple-bash-programming-skills)   

[[Bash]] 中 `--` 后面的参数不会被当做选项解析。

---

[How Docker 2.0 went from $11M to $135M in 2 years](https://sacra.com/p/docker-plg-pivot/)    

[[docker]] 公司靠着[[Dockerhub]] 和 [[Desktop]] 收费实现收益。（但现在替代品已经很多了

---

---

[GitHub - sourcegraph/conc: Better structured concurrency for go](https://github.com/sourcegraph/conc)   

列举了一些常见的 [[Golang]]并发场景。

---

[Why not DNS?](https://whyk8s.substack.com/p/why-not-dns)   

为什么 [[k8s]]不直接通过 [[DNS]] 来配置 service 至 pod，而是通过 cluster-ip？避免缓存。

---

[Go runtime vs CFS quota - Vladimir Varankin](https://vladimir.varank.in/notes/2023/01/go-runtime-vs-cfs-quota/)  

[[Golang]] runtime 无法感知 资源限制，如果用默认的 `runtime.GOMAXPROCS` 可能会导致应用更早的触发节流，可以考虑使用 [GitHub - uber-go/automaxprocs: Automatically set GOMAXPROCS to match Linux container CPU quota.](https://github.com/uber-go/automaxprocs) 来自动配置。

---


### 生活

[2022年终总结之我的买房经历 · Issue #53 · superleeyom/blog · GitHub](https://github.com/superleeyom/blog/issues/53)   

[[长沙]]买房经历。

---


[gail.com FAQ](https://gail.com/)     

> A: In 2020 this page received a total of 5,950,012 hits, which is an average of 16,257 per day. Looking at just unique hits, we received a total of 1,295,284, for an average of 3,539 unique hits per day. Occasionally, we get Twitter-bombed and may get several tens of thousands of visitors a day. As an example, on July 21st 2020 we received 109,316 hits.

---

[笔记软件与写作软件的不同 - oldj's blog](https://oldj.net/article/2023/01/09/note-app-and-writing-app/)    

笔记和写作从需求上看是不同的场景，用 [[logseq]] 来写一篇文章感觉痛苦，有时候甚至不如一个独立的 markdown 编辑器来的爽快。

---


## 书影

《开夜车》，新加坡的鬼片，无趣。  

《下辈子我再好好过 第三季》，更新到第三季了，比较期待女主的结局。

《斑马》，傅真的长篇小说，开头比较苦，后面关于个人情感的变化比较有趣。同事推荐了傅真的其他小说，说是都不错。


