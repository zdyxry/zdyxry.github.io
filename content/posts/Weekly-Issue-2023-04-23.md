---
title: Weekly Issue 2023-04-23
date: 2023-04-23
tags:
- Weekly
description: 《伊卡洛斯》很好看。
---


## 文章

### 技术


[2023 年 KCD 大连站活动后记 （2023-04-15） - 马全一/马道长](https://www.maquanyi.com/articles/kcd-dalian-2023-04-15)

> 真正的后记来了，从离开腾讯后确实没有怎么关注云原生领域的发展。从当前的感觉来看，这个领域已经没有特别地创新。不知道是真的进入落地阶段，还是已经进入自嗨、回魂还是僵死。正好第二天转机到阿姆斯特丹参加 KubeCon ，是一个近距观察的机会。  

---

[Load Balancing](https://samwho.dev/load-balancing/)

常见负载均衡策略讲解，图文并茂，包含轮询，加权轮询，最小连接数，以及Peak EWMA 。

配合阅读： [Beyond Round Robin: Load Balancing for Latency | Linkerd](https://linkerd.io/2016/03/16/beyond-round-robin-load-balancing-for-latency/)
不同策略之间的差异与其说是算法上的差异，不如说是用于做出平衡决策的信息上的差异。

---

[Pricing v3, plans, packages, and debugging · Tailscale](https://tailscale.com/blog/pricing-v3/)

[[TailScale]] 更改了自己的定价策略，在现有用户数据的支持下，解释做出这样变更的原因。免费团队支持3个用户，100个设备。

---

[nohup,setsid与disown的不同之处 - 暗无天日](http://blog.lujun9972.win/blog/2018/04/20/nohup,setsid%E4%B8%8Edisown%E7%9A%84%E4%B8%8D%E5%90%8C%E4%B9%8B%E5%A4%84/index.html)

nohup 会关闭进程的stdin，当进程尝试读取输入时，只会得到EOF。disown命令会将命令从bash的job list中删除。 这样，当bash收到SIGHUP信号后，并不会将SIGHUP信号发送给该命令。

> 若调用setsid函数的进程就是一个进程组的组长，则该函数会返回出错。 为了解决这种情况，通常函数需要先fork，然后父进程退出，由子进程执行setsid。 由于子进程继承的是父进程的进程组ID，而其PID是新分配的ID，因此这两者不可能相等，即子进程不可能是进程组的组长。 这种情况下，由于父进程先于子进程退出，因此子进程的父进程会有init进程接管。 而这就是sid命令的实现原理。  

---

[Kubernetes 1.27: Query Node Logs Using The Kubelet API | Kubernetes](https://kubernetes.io/blog/2023/04/21/node-log-query-alpha/)

[[kubernetes]] 可以通过 kubelet API 获取 Host 节点上的日志。这个功能是 [[openshift]] 贡献的。

---

[It’s fine to use names in post-mortems – Dan Slimmon](https://blog.danslimmon.com/2023/04/20/its-fine-to-use-names-in-post-mortems/)

在进行事故复盘时，有时会因为避免直接提及具体人而使用代称（dev/ops），但是如果公司的氛围能明确是对事不对人，那么陈述一个事实是没有问题的。

---

[Go 框架 Gin 解析：HTTP 的处理](https://liqiang.io/post/gin-how-router-and-middleware-works-9644c966)

[[Gin]] 介绍，包含了 Engine 和RouterGroup 。

---


[Searching 1.5TB/sec: Systems Engineering Before Algorithms - Dataset](https://www.dataset.com/blog/systems-engineering-before-algorithms/)

[[Dataset]] 使用暴力来实现日志检索功能。这里的暴力是相对于关键词索引的方式来说。暴力实现是可行的，在适当的场景使用暴力实现是一种权衡，相对来说暴力实现可以提供一致的性能，减少了可能的意外引入，用户感知的性能是整个系统的性能，不仅仅是内部的细节实现。

---



### 生活

[随便写点 - laike9m's blog](https://laike9m.com/blog/sui-bian-xie-dian,146/)

保持自己的生活节奏很重要，比如每周定期的看书、看电影。我的周末基本上是固定的，每天什么时间做什么事情，基本上不会发生变化。

> 人们的生活太过复杂，以至于他们宁愿选择死亡。他们通过自杀寻求死亡是为了结束复杂。因为这种复杂一旦失控，就导致痛苦。  

---

[去南半球的海岛 | 卡瓦邦噶！](https://www.kawabangga.com/posts/5025)

[[巴厘岛]]游记，很真实很有趣。去外地如果吃不惯东西，麦当劳和肯德基是最不会出错的选择。

---

[5 Years of Indie Hacking](https://allisonseboldt.com/5-years-of-indie-hacking/)

热情不能够持久的支撑；很多时候期望实现自己感兴趣的工作，但实际上完全远离与人的沟通。

---

## 书影


《我在北京送快递》，书里描述的场景，是一个日常生活中很多人没有在意的场景，如果仔细观察都可以感受的，如果人与人之间没有利益关系，还是会有善意的。另外，微信读书中的一些划线评论，让人不适。

《深入理解 Linux 网络》，这周没投入时间。

《模仿犯》，没有想象中好看，这个标题也对不上，模仿，要模仿才会更有趣。

《伊卡洛斯》，刘旸教主的专场，开票的时候没有抢到，晚上的时候突然发现咸鱼上有人原价转二手，赶紧买了。剖析自己的内心，团结湖北，哪怕我知道团结湖，都没有想到这个梗。

