---
title: Weekly Issue 2023-04-30
date: 2023-04-30
tags:
- Weekly
description: 强烈推荐宋万博的单口专场《天生非此》。
---


## 文章

### 技术


[服务端性能优化--最大QPS推算及验证 - huangyingsheng - 博客园](https://www.cnblogs.com/huangyingsheng/p/13744422.html)

关于 [[QPS]] 的计算方式，最大 QPS，最佳线程数。单线程𝑄𝑃𝑆=1000𝑚𝑠/𝑅𝑇。最佳线程数 = (RT/CPU Time) x CPU 核数 x CPU利用率 。

---


[绕过 Cloudflare 指纹护盾 | Sxyazi’s blog](https://sxyz.blog/bypass-cloudflare-shield/)

貌似很多站点都会检测 [[Golang]] 的 Cipher Suites，之前应该是[[v2ray]] 提到过类似问题。通过使用 [GitHub - refraction-networking/utls: Fork of the Go standard TLS library, providing low-level access to the ClientHello for mimicry purposes.](https://github.com/refraction-networking/utls) 可以进行更改。

配合阅读：[为什么用 Go 访问某网站始终会 503 Service Unavailable ？ | 无辄的栈](https://www.zackwu.com/posts/2021-03-14-why-i-always-get-503-with-golang/)

---

[How to Gracefully Close Channels -Go 101](https://go101.org/article/channel-closing.html)

[[Golang]] Channel 关闭的几种场景。

---

[Faster Multi-Platform Builds: Dockerfile Cross-Compilation Guide | Docker](https://www.docker.com/blog/faster-multi-platform-builds-dockerfile-cross-compilation-guide/)

使用 [[Buildkit]] 来交叉编译项目示例。现在不少项目的 Dockerfile 还非常的原始，可以利用这些很成熟的方式来提升效率。

---
[使用 BuildKit on Kubernetes 构建多架构容器镜像 | Reimu's blog](https://blog.k8s.li/buildkit-on-kubernetes.html)

在 [[kubernetes]]上部署都架构[[Buildkit]] 说明。公司内部 CI 已经采用这种方式进行使用了。

---

[Should Rye Exist? · mitsuhiko/rye · Discussion #6 · GitHub](https://github.com/mitsuhiko/rye/discussions/6)

[[flask]] 作者个人项目，来处理 [[Python]] 的项目管理问题。 [[PDM]] 的作者写过一系列的博客用于讲解类似的问题，但是官方社区推进速度非常缓慢。
感觉这个属于那种”又不是不能用“，但是”不好用“的问题。

---

[公有云是不是杀猪盘？ - 知乎](https://zhuanlan.zhihu.com/p/614071210)

> **EC2 / S3 / EBS 是所有云服务的定价之锚**。如果说 EC2/S3 定价还勉强能算合理，那么 EBS 的定价乃是故意杀猪。公有云厂商最好的块存储服务与自建可用的 PCI-E NVMe SSD 在性能规格上基本相同。然而相比直接采购硬件，**AWS EBS 的成本高达 120 倍，而阿里云的 ESSD 则可高达 200 倍**。  
> **EBS的高溢价倍率是故意设置的门槛，以便于云数据库杀猪**。  

---

[一文看懂 | GDB底层实现原理](https://mp.weixin.qq.com/s?__biz=MzA3NzYzODg1OA==&mid=2648465474&idx=2&sn=52dfd43e8f376e1ff16b2f81c3c002a7&scene=21#wechat_redirect)

[[GDB]]及[[ptrace]] 基本流程介绍。

---


[CPU Utilization is Wrong](https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html)

[[CPU]]利用率：CPU 未运行空闲线程的时间。CPU利用率很够，很有可能是因为存储介质导致的。应该关注 IPC 指标，它显示了我们在每个 CPU 时钟周期平均完成了多少指令。越高越好。

如果您的 IPC < 1.0，则可能是内存停滞，软件调优策略包括减少内存 I/O，以及改进 CPU 缓存和内存局部性，尤其是在 NUMA 系统上。硬件调整包括使用具有更大 CPU 高速缓存以及更快内存、总线和互连的处理器。

如果您的 IPC > 1.0，则您可能受指令限制。寻找减少代码执行的方法：消除不必要的工作、缓存操作等。CPU 火焰图是这项调查的一个很好的工具。对于硬件调整，尝试更快的时钟速率和更多的内核/超线程。

可以通过 `perf stat -a -- sleep 10` 来观察。

---


[如何开发一个 Packer 插件](https://xknow.net/how-to-write-packer-plugin/)

[microud](https://github.com/microud) 同学最近给内部的虚拟化产品编写了 [[Packer]] 插件，我前阵子也在这个基础上增加了多磁盘的支持。整体上 [[Packer]] 的架构逻辑很清晰，感觉重点是如何衡量暴露给用户的配置方式，哪些属性应该暴露出去，以什么形式暴露。

---

[Emerging Startups 2023: Top Open Source Startups | Tracxn](https://tracxn.com/d/emerging-startups/top-open-source-startups-2023)

开源软件公司是投资者最活跃的目标之一，2.58K 家公司的总融资额为 40.1B 美元。还值得注意的是，大约三分之一的资金是在过去 3 年（2020-2022 年）筹集的。
在这个页面中， `cloud` 出现的次数是31次。


### 生活

[16岁少年沙漠探险身亡：一次夺命的“留学加分”旅行](https://mp.weixin.qq.com/s/wkYXe8kkZwxCDXNBJjoztQ)

> **“人家跟我说，清华北大够牛的吧，多伦多大学在国际上的排名比它们还要靠前呢！我想我也不懂排名，就觉得加拿大也挺好，我儿子胖，喜欢凉快的地方⋯⋯”**  

一声叹息。

---

[成都失去性价比？-虎嗅网](https://www.huxiu.com/article/1299511.html)

> “伊莱那是一座从远方看到的城市的名字，如果走近她，她就变了。”  

最近几年的论调都是卷不过北上深，就去成都，但是成都又哪有想象中那么美好。

---

## 书影

《深入理解 Linux 网络》，阅读了第二章，带着问题去阅读。

《我是一只IT小小鸟》，如果在大学的时候能看到就好了，当然现在看也有些收获。

《构建高性能Web站点》，对于性能评估方法很明确，10年前确实有些太久远了。

《看呐，这人》，宋万博的单口专场，这是他的第二个专场，我很喜欢。

《天生非此》，一天中看的第二场宋万博的单口专场，非常的精彩，里面提到了很多关于教育的缺失、个人的成长，个人如何与父母，主要是父亲维持关系，以什么样的心态去沟通。

《流人》，看了第一集。在不同的地方看到过推荐，节奏没有那么快。

## 碎碎念

最近很喜欢躺在草地上，在来到上海之前，貌似心里一直被种入一个理论：不要践踏草坪。最近去公园的次数明显频繁了不少，家附近就有一片可以趟的草地，周末的时候很多人都在露营，非常的“生活化”，很喜欢，躺在草地上看书的感觉太棒了。
