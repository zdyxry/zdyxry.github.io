---
title: Weekly Issue 2023-02-26
date: 2023-02-26 19:00:00
tags:
- Weekly
description: FPS游戏太难了，用手柄玩就更难了。
---


## 文章

### 技术


[Nix Is Fighting The Last War](https://matt-rickard.com/nix-and-the-last-war)

[[Nix]] 注定是一个小众的解决方式。

---

[Tcpdump 从 TCP_option_address 中根据真实 IP 过滤 | 卡瓦邦噶！](https://www.kawabangga.com/posts/4925)

[[tcpdump]] 抓取 [[LVS]] 转发前的真实 IP 地址。

---

[How Levels.fyi scaled to millions of users with Google Sheets as a backend](https://www.levels.fyi/blog/scaling-to-millions-with-google-sheets.html)

早起通过[[Google]][[Sheets]] 配合 [[Lambda]] 和 API Gateway 快速验证产品可行性，后续根据需要来切换到后端服务加数据库形式。

---

[FOSDEM 2023 - I was wrong about Flatpak, AppImage, and Snap (Containerised Apps Presentation) - YouTube](https://www.youtube.com/watch?v=4WuYGcs0t6I)

讨论了AppImage、Snap和 Flatpak ，2017年以及现状，结论是使用 Flatpak 让生活更美好。

---

[K8S 生态周报| Cilium 和 Istio 的新版本带来众多新特性 | MoeLove](https://moelove.info/2023/02/19/K8S-%E7%94%9F%E6%80%81%E5%91%A8%E6%8A%A5-Cilium-%E5%92%8C-Istio-%E7%9A%84%E6%96%B0%E7%89%88%E6%9C%AC%E5%B8%A6%E6%9D%A5%E4%BC%97%E5%A4%9A%E6%96%B0%E7%89%B9%E6%80%A7/)

> containerd v1.6.18 发布
修复了 CVE-2023-25153，在导入OCI镜像时，某些文件没有对读取的字节数进行限制。如果一个恶意制作的镜像包含了一个非常大的文件，且没有对其进行限制，可能会导致拒绝服务攻击；

最近内部遇到的一个问题，使用[containers/image](<https://github.com/containers/image/blob/10858b2058d8c0c709bb2489e1cb7773d1d09216/storage/storage_dest.go#L191-L195>) 这个库，在进行 layer 写入的时候没有 sync，可能会导致 dirty page 太多进而导致程序触发 [[OOM]]。这个场景在配合 xfs 的时候出现问题，ext4 正常。

---

[You Can Stop Updating Copyright Attribution Years](https://hynek.me/til/copyright-years/)

每次更新代码的时候都要考虑是不是更新[[Copyright]]，越来越多项目部写具体年份了。
[[LinuxFoundation]] 针对[[Copyright]] 有具体的博客讲解：[Copyright Notices in Open Source Software Projects - Linux Foundation](https://www.linuxfoundation.org/blog/blog/copyright-notices-in-open-source-software-projects)

---

[Design | Parca](https://www.parca.dev/docs/parca-agent-design#cpu-sampling-frequency)

[[Parca]] Agent 关于[[CPU]] 采样频率设置  
> We sample at 19Hz (19 times per second) because it is a prime number, and primes are good to avoid collisions with other things that may be happening periodically on a machine. In particular, 100 samples per second means every 10ms which is a frequency that may very well be used by user code, so a CPU profile could show a periodic workload on-CPU 100% of the time which is misleading as it would produce a skewed profile.  
19 is close to 20 which would have been a natural choice just for lowering profiling overhead, and it's easier to reason about, e.g., we could take roughly 80 samples per second on 4-CPU machine.

---

[针对进程设置路由规则 | 卡瓦邦噶！](https://www.kawabangga.com/posts/4935)

[[iptables]] , [[LD_PRELOAD]], 代码中直接修改。评论中提到其他实现方式：把进程放到独立的 network namespace ，然后配合 iptables + route；或者 iptables --uid-owner 匹配 Mark，将不同的进程用不同的 UID 运行，[[Istio]] 采用了这种方式。

### 生活


[对于上野千鹤子的对话视频，我非常非常愤怒 - hayami's blog](https://hayami.typlog.io/ueno)

> 而这会让人觉得，这么多前人后人前仆后继浴血奋战薪火相传，结果讨论的东西简直梦回清朝裹脚布，我裹上去之后还一个劲在问吾与裹脚布谁美？

视频中的双方不在一个层面上，上野千鹤子只要用真诚就已经秒杀对方了。

---


[抢教授话筒的中学生——“大词过敏症”正在这代年轻人中退潮](https://mp.weixin.qq.com/s/MLHMIphuF5HS02ZhfNzcuA)

> 但有没有可能，这些都是错误的呢？有没有可能，你个人好好学习这件事情，既无法显著的改善你的个人命运、也对国家崛起这样的大事能起到的推动作用微乎其微，而只关乎你个人的性格、修养、见识与灵魂呢？  
而这，也许才是教育的本意 ，我们是普通人，一个现实是：普通人读书并不太可能为自己或为国家的命运起到什么“翻天覆地”的大推动、大变化。**能培养一个独立、善良、理性而能享受自己平凡的生活和思维乐趣的普通公民，就已经是教育的成功了。**

---



## 书影

《当我们不再理解世界》，刚开始看，还没有什么感受。

《千寻小姐》，有村架纯的新电影，视角和故事都很平淡，但是这种平淡的故事也很少有人拍，有点像《西瓜》的感觉。

《模范出租车》，典型的韩国类型片，目前按照剧情看可能没有什么可反转的地方，当做下饭剧还不错。