---
title: Weekly Issue 2023-12-03
date: 2023-12-03
tags:
- Weekly
description:  
---


## 文章

### 技术

[S3 Express is All You Need - WarpStream](https://www.warpstream.com/blog/s3-express-is-all-you-need)

[[AWS]] [[S3 Express]] 发布，每 GB 的存储成本比 S3 标准高 8 倍。超过 512KB 的每个 API 操作（写入/读取）按 GB 收费。对于大容量场景，S3 Express 不会带来显著的成本或性能改进，但是从软件设计上，可以完全围绕对象存储来构建，比在应用程序层手动复制数据更便宜、更耐用并且更不容易出错。

[[baotiao]] 前两天发布的[推特](https://twitter.com/baotiao/status/1727058804905509126)也是类似的观点：

>我觉得学术界和工业界还是有点脱钩, 还在研究一些在 数据库在 modern hardware 上的优化, 我理解以后的数据库大部分应该是针对云上的硬件进行优化了, 包括 VM, essd 等等

---

[Rust std fs 比 Python 慢！真的吗！？](https://mp.weixin.qq.com/s/m-IBomxu88DlNcEyOgyOew)

从最初的用户上报，到一点点的复现问题，进行各种尝试，包括不限于：更换内存分配器、调整 mitigations、调整透明大页、调整 NUMA等等。最终确定是与 FSRM 相关。社区力量大啊。

如何发现 offset 的[差异](https://github.com/Xuanwo/blog/discussions/416#discussioncomment-7704455)：

>两个相同的系统调用不可能有不同的时间，在排除了 `length` 参数差异之后，找到了 `-e raw=read` 参数，发现了 offset 差异。

>`FSRM`，即 `Fast Short REP MOV`，是英特尔最初的创新，近期也被AMD采纳，用以提升 `rep movsb` 和 `rep movsd` 的速度。它旨在提高大量内存复制的效率。声明支持它的CPU将在 `glibc` 中默认使用 `FSRM`。

---


[X 上的 halfbloodrock：“趁着滴滴宕机10小时，都说是Kubernetes升级引起的，刚好kubernetes是老本行，在eBay那几年，都是在做大规模kubernetes集群管理，kubernetes集群升级这块，正好蹭个热点，讲讲这几年在kubernetes上踩过的坑。” / X](https://twitter.com/halfbloodrock/status/1729876674786070751)

[[kubernetes]] 升级遇到的坑汇总：

- ip pool block要是配小了，很可能出现pod拿不到IP起不来而计算资源空闲的情况。调度器可不看IPAM里还有多少剩余IP
- 为啥要改k8s代码？For KPI？ k8s一直到1.12才趋于稳定，比如admission webhook是1.9才引入，到1.13稳定 之前admission上的一些需求只能改上游代码，改动提给社区，人家不一定要，而后面版本cherrypick这些自己改的代码，维护起来还是比较痛苦的。 不过到今天绝大部分需求都不用再改上游代码
- 改了上游代码，最好的结果是，提给社区合并进主干。但是大部分情况是提上去的社区不接受，原因众多。 那在下个大版本升级时候，需要把改过的代码cherry-pick进去，解决冲突，过UT，过e2e，过benchmark
- k8s可以应用无感知升级吗？ 至少1.18之前不行 Kubelet升级之后要重新算下pod hash，会重建底层容器，不少应用其实不太能容忍这个动作，每次升级都要收到很多pod重启的抱怨
- 有状态应用到底能不能上k8s? k8s的statefulset解决的是pod启动顺序问题，其实真正的核心点是有状态应用如何存数据。 像es这种天生分布式的，可采用本地lvm卷做存储[https://github.com/openebs/lvm-localpv…](https://t.co/5uQoqbr3Za) 像MySQL，官方推荐的是mysql cluster+proxy （但是我没在生产上跑过） [https://github.com/mysql/mysql-operator](https://t.co/V2JUw3lJOt)
- 为啥一升级就挂？k8s里有两个地方变动相对频繁，一个是feature gate，一个是api-version 问题七中的坑，1.10之前可以disable这个feature gate，但是1.10之后强制打开，没有disable的机会。 升级过程中发现了，用户改代码没那么快咋办？只能把上游的这个commit 去掉
- 能跨版本升级吗？能跨多少版本？ 不要跨超过三个版本：[https://kubernetes.io/zh-cn/releases/version-skew-policy/…](https://t.co/COop5Y9DxV) 熟读ChangeLog 曾经的坑，用户在pod里对secret做修改，1.10之后社区去除了这个功能，这直挺挺升级上去用户应用就挂了。这些变动在每个版本ChangeLog里都有

---

[Cloudflare Gen 12 Server: Bigger, Better, Cooler in a 2U1N form factor](https://blog.cloudflare.com/cloudflare-gen-12-server-bigger-better-cooler-in-a-2u1n-form-factor/)

[[CloudFlare]] 12 代服务器硬件设计。CPU TDP 现在的趋势是逐代快速增加，Intel/AMD 下一代 x86 CPU TDP 将达到 500W。

1U1N 服务器，使用风扇进行散热，每个风扇的功耗是 40W，每台服务器 7-8 个风扇，每台服务器的总系统功耗可能会超过 750W。1U 服务器最多容纳 8 个 40mm 风扇，假设视为是 40 度，8 个风扇最多可以支持 TDP 为 400W 的 CPU，无法支持下一代 CPU。此外，机架有自己的功率限制，考虑到单台服务器的功耗 750W，加上网络设备空间，最终机架空间利用率可能是 50%。

在计算 TCO 时，虽然单台服务器会随着 CPU TDP 提升而提升，但是因为机架本身又功率和高度限制，最终选择将 1U1N 替换为 2U1N。

---

[The Weirdest Bug I’ve Seen Yet](https://engineering.gusto.com/the-weirdest-bug-ive-seen-yet/)

页面崩溃了，可能是什么原因呢？只影响了Chome？ Chome 版本错误？Chrome 扩展？结果定位到是一个 Gif 导致的。

这篇博客的调查过程，非常符合我的各个猜测，看到每个猜测被印证是错误的，然后就想继续往下看，写的真好。

---

[Code is run more than read](https://olano.dev/2023-11-30-code-is-run-more-than-read/)

从几个维度思考软件开发，user, maintainer, author 和 business 。
- 无法维护的代码： author > maintainer 
- 无法使用的软件：dev > user 
- 无法部署的软件：dev > ops
- 软件的目的是代码本身：dev > business
- 简历驱动开发：dev > *
- 想象中的软件：business > user > ~~ops~~ > dev 或者 business > ~~user~~ >ops > dev
- 晚期资本主义：~~business~~ >user > ops > dev

结论：用户可能不总是优先于业务，但是业务不应该无条件的放在第一位。

---


[Gateway API 将是 Kubernetes 中流量管理的未来吗？ | MoeLove](https://moelove.info/2023/11/26/Gateway-API-%E5%B0%86%E6%98%AF-Kubernetes-%E4%B8%AD%E6%B5%81%E9%87%8F%E7%AE%A1%E7%90%86%E7%9A%84%E6%9C%AA%E6%9D%A5%E5%90%97/)

[[kubernetes]] [[Gateway API]] 介绍。南北向流量使用 [[Ingress]] 管理，但是 [[Ingress]] 提供的能力较少，依赖 Controller 提供的 CRD 或者  annotation 才可以实现更多的能力，想要在不同的 Ingress Controller 迁移很困难。东西向流量使用 Service 管理，需要配合各种 Service Mesh 项目。

Gateway API 面向角色，不同的角色进行不同阶段的配置，表现能力更强，扩展性更好（提供了 spec.parametersRef 关联其他自定义资源）。

---

[记一次由 Systemd 超时导致 OSTree 挂载失败的故障调查 | CosPotato's Blog](https://blog.0x233.cn/blog/2023/12/02/system-ostree-failed/)

[[ostree]] 未能按照预期挂载 `/ostree/deploy/$stateroot/var` ，调查思路从 ostree 到 systemd，主要是集中在 systemd generator 部分，根本原因是虚拟机的 IO 太慢 。之前在非 ostree 场景下也遇到过，比较典型的是 systemd-fsck 的时候失败，导致 os 进入 emergency mode，缓解的办法是调整 systemd timeout，systemd 很复杂，涉及到的 timeout 参数很多，需要找到最小影响范围的 timeout，进行更改，更改的时候尽量采用 drop-in config 的方式。

---

[Chrome’s next weapon in the War on Ad Blockers: Slower extension updates | Ars Technica](https://arstechnica.com/google/2023/12/chromes-next-weapon-in-the-war-on-ad-blockers-slower-extension-updates/)

最近[[Chrome]] 对广告拦截器的针对性动作实在是有点多，有点丧心病狂的意思。

---

[Not Everything Is Google’s Fault (Just Most Things)](https://blog.railway.app/p/gcp-incidents)

[[Railway]] 最开始使用 [[GCP]]，但是体验很糟糕，这篇文章列举了遇到的问题：网络问题、Registry 配额问题、售后支持。现在在逐渐迁移至自己的物理服务器。

---



### 生活

[Naev - Home](https://naev.org/)

Naev 是一款关于太空探索、贸易和战斗的游戏。玩家在银河系中旅行，通过交易、战斗和执行任务来赚钱。

---

[The Complete Guide to Time Blocking](https://todoist.com/productivity-methods/time-blocking)

同事貌似一直深受痛苦，我推荐了[[time-blocking]] 给他，他反馈说还不错（也不知道能坚持多久）。工作方法论，合理的安排时间。

---

[趁着 2023 Steam 秋季特惠，推荐几款今年比较喜欢的游戏 - Another Dayu](https://anotherdayu.com/2023/5490/)

游戏推荐：潜水员戴夫，吸血鬼幸存者，The Battle of Polytopia，Impostor Factory《影子工厂》，Impostor Factory《影子工厂》。
我只玩过吸血鬼幸存者。

---


[入门到精通：从今天开始成为感冒专家 - 少数派](https://sspai.com/post/84574)

最近北京的“感冒”人数貌似多了不少，也持续了一段时间了。
- 解热镇痛：对乙酰氨基酚、布洛芬；
- 缓解鼻塞、流涕、打喷嚏：氯苯那敏、苯海拉明；
- 缓解鼻塞：伪麻黄碱；
- 镇咳：右美沙芬、布桂嗪o。

---

[Working with problems | Seth's Blog](https://seths.blog/2023/11/working-with-problems/)

遇到问题的时候，如何处理问题？

首先需要明确这是一个problem 还是一个situation，problem 有解决方案，无论是解决方案有多么不喜欢，但是总是有解决方案的，但是situation 只是我们需要忍受的事情。关注 situation 通常是压力的来源。
如果一个 problem 已经存在一段时间了，那么说明这个问题无法立即解决，我们需要调整对这个 problem 的期望，可以将其视为一种 situation。

---

[揭秘拼多多：市值超越阿里，它是怎么做到的？](https://web.archive.org/web/20231201220126/https://mp.weixin.qq.com/s/q6VnNrWvV2Jh9UuTl96dWQ)

>所谓“刚性执行”，**就是绝对服从、没得商量的意思。**  
>要做到拼多多这样的强执行，员工应该很痛苦，为什么还有这么多员工愿意来拼多多呢？朋友告诉我，原因很简单，因为给钱多。  
>大家工作是来挣钱的，想让员工服从和努力，就要拿钱说话。  
>**因为拼多多一直在筛选，只有为了挣钱、能接受高压和绝对服从的人才能留下来。**  
>**在管理者的要求和意志面前，服从成为了唯一的选择。**  

---


## 书影

《征服世界完全手册》，脑洞大开，如果你是一个超级大反派，如何选择自己的基地：地上？地下？水底？需要考虑哪些方面？

《东京八平米》，对于作者来说，房间大小对生活的影响没有那么大，更多的是自己与周围的连接。作为漂在外面的人，自己和周围的朋友时常感受到无意义/飘泊感，也许我们应该更多的打开自己，多观察周围的生活，多与人沟通交流。  
记得之前听到过一句话：“考古是考证人类的历史”，对于我们应该也是一样，我们在一座城市生活过，能真正留下记忆的，应该我们在这座城市与人，与城市连接的痕迹，大概率不是我们在出租屋里的一天（如果有，应该也不是什么美好的回忆）。



