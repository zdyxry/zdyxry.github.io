---
title: Weekly Issue-让我们给 WebArchive 捐款吧
date: 2024-05-26
tags:
- Weekly
description:  
---


## 文章

### 技术

[OpenAI compatible API endpoints · Cloudflare Workers AI docs](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/?utm_medium=organic-social)

[[CloudFlare]] Workers AI 的 API 现在提供了与 [[OpenAI]] 兼容的 Endpoints。

---

[奇客Solidot | 2013 年的网页有 38% 今天已无法访问](https://www.solidot.org/story?sid=78207)

当前如果想要最大程度的保留信息，还是需要完整的把网页保存下来才可以，或者及时的把对自己有用的信息提取出来记录下来。

是时候去给 [Wayback Machine](https://web.archive.org/) 捐款了。

---

[Reclaiming CPU for free with Go's Profile Guided Optimization](https://blog.cloudflare.com/reclaiming-cpu-for-free-with-pgo/)

[[CloudFlare]] 使用 `PGO` 优化 CPU 使用情况，在他们内部环境中，节省了 3.5% 的 CPU cores。

通过获取典型节点的 pprof 信息，然后使用 `go tool pprof -proto "${working_dir/}"*.pprof > profile.pprof` ，最终在构建产品时传递 `go build -pgo ./pgo/profile.pprof` 参数。

Google Cloud 的一个相关视频介绍： [Boost performance of Go applications with profile guided optimization - YouTube](https://www.youtube.com/watch?v=FwzE5Sdhhdw)

---

[Introducing Copilot+ PCs - The Official Microsoft Blog](https://blogs.microsoft.com/blog/2024/05/20/introducing-copilot-pcs/)

[[Microsoft]] 退出的新版本 Surface，取名 Copilot+ PC，是 ARM 架构的，起售价 999$。描述中可以提供长达 22h 的本地视频播放或 15h 的网页浏览（有点怀疑真实性）。

特色功能：
- Recall，类似于 [Rewind](https://www.rewind.ai/) ，自动获取屏幕中的所有信息，并保存索引，便于后续的搜索。
- Cocreate，AI 绘图。
- Copilot，采用 `GPT-4o` 模型

---

[Amber](https://amber-lang.com/)

一门新的编程语言, 可以编译为 [[Bash]]。优势是：现代语法，类型安全。

直接编写 Bash，使用 ShellCheck 配合 [https://github.com/dylanaraps/pure-bash-bible…](https://t.co/gLUITP96Un) ，基本上可以应付大部分场景了吧

---

[一个不知名的开源项目可以带来多少收入 —— NocoBase 3 年总结分享](https://blog-cn.nocobase.com/posts/nocobase-opensource-income-3years/#%E6%9B%B4%E9%87%8D%E8%A6%81%E7%9A%84%E6%94%B6%E8%8E%B7)

[[NocoBase]] ，一个开源项目的背后故事。当前团队规模 10 人，已经盈利。

---


[Making EC2 boot time 8x faster](https://depot.dev/blog/faster-ec2-boot-time)

将 [[EC2]] 的启动时间从 40s 减少至 5s，有点标题党。

通过提前准备好 [[EC2]] 虚拟机，并使用 fio 来预热，然后将虚拟机关机，在下次需要的时候进行开机即可，减少时间主要来自于：从 AMI 创建 EBS 时间，虚拟机基础信息配置，IP 地址分配时间等。

---

[UI Density || Matthew Ström, designer-leader](https://matthewstrom.com/writing/ui-density/)

>UI 密度是用户从界面获得的价值除以界面占用的时间和空间。

我很喜欢“信息密度”高的界面，比如之前的 Windows Phone 界面。

---

[Rebuilding my homelab: Suffering as a service - Xe Iaso](https://xeiaso.net/blog/2024/homelab-v2/)

>CoreOS was radical and way ahead of its time. # 非常同意。

Xe 因为 [[Nix]] 事件而抛弃 [[Nix]]，在重新折腾自己的 homelab。
- 先尝试了 RockyLinux 配合 Ansible，管理比较麻烦
- 评估 CoreOS，Fleet 可以自动发现 CoreOS 并组件集群，但已经不维护了。Fork 的 Flatcar 如果想要修改 Ignition 配置，一定要重新的 Image machine ，所以没有尝试
- 评估 Fedora CoreOS，按照 Bazzite Linux 的方式，准备一个 Base Image 作为不可变基础层，然后在上面安装一些日常使用中需要的 RPM。
	- 参考链接： [running k3s on fedora coreos bare metal](https://devnonsense.com/posts/k3s-on-fedora-coreos-bare-metal/)
	- 使用 `coreos-installer` 来构建 ISO，并使用 `butane` 生成 Ignition 配置
	- 一切比较顺利，但是因为 Fedora CoreOS 的理想是所有的应用全部都是 Container，所以如果想要重新修改配置，那么就需要重新的 Image machine，对于个人用户有些重
- K3OS，发现 K3OS 被抛弃嘞，转向了 Elemental
- Talos，简单易用，快速上周，并且可以拜托上面的一些利操作同时得到 Linux 和 K8s
	- 在安装 CSI 的时候发现很多 Operator 都硬编码了 `cluster.local`
	- Talos 默认的安全策略比较严格，需要注意
	- 接下来就是一堆 K8s 相关的配置了，Ingress，DNS 等等。

优雅的维护 [[homelab]] 是一门艺术。

---




### 生活


[新加坡OCBC华侨银行线上开户完全指南 – 土木坛子](https://tumutanzi.com/archives/17315)

[[新加坡]] [[OCBC]] 开户说明，可以支持大陆用户远程开户。管理费需要满足日均一定数量的存款可免。

---

[How 3M Execs Convinced a Scientist the Forever Chemicals She Found in Human Blood Were Safe — ProPublica](https://www.propublica.org/article/3m-forever-chemicals-pfas-pfos-inside-story)

《3M 高管如何让科学家相信她在人体血液中发现的永久化学物质是安全的》。

每当这个时候，我都想到《潜伏》中的谢若林的台词：“现在有两根金条摆在这，你告诉我哪一根是高尚的，哪一根是龌龊的?”

---

[【404文库】何加盐｜中文互联网正在加速崩塌](https://chinadigitaltimes.net/chinese/708143.html)

>**中文互联网正在迅速崩塌，移动互联网出现之前的中文互联网内容，已经几乎消失殆尽。**
>**我们曾经以为互联网可以保留一切，但结果是一切都没能保留。**
>**本质上，互联网内容和生命一样，也受进化论的支配。其存在的标准只有一条：以尽可能低的成本争取尽可能多的注意力。**

我很早就没有**以为**互联网可以保留一切，因为一切都是要成本的，从最原始的角度去理解就可以了。之前我使用稍后阅读的统计是，链接 404 的比例在 5% 左右，不只是中文互联网，全世界都是类似的，只是中文可能崩塌的更快。

能够完整保留内容的方式，就是保存在自己手里。

让我们继续给 [[WebArchive]] 捐款吧。

---

[大模型的扑克牌：独家内幕故事](https://wallstreetcn.com/articles/3715681#from=ios)

>**这是一起特殊时候的中国特殊的资本故事——它沉默又喧嚣、萎靡又阔绰、团结又精明，充满了矛盾感。**
>但若是，一家创业公司最终以50亿美元甚至100亿美元卖给巨头？
>“我也能理解。”一名投资者说，**“对我来说，这是一个很成功的失败，并不是一个失败的成功。”**

---


## 书影

（也不知道自己在做什么

## 碎碎念

* 暴躁是因为无能么？
* >再次拜读了我厂底层研发生存指南：“少反思自己，多指责别人。如果你是对的，一定要得理不饶人。如果你是错的，要想办法发脾气”，听起来很操蛋，但实际就是这么个情况。  

  看到了这条推，下面很多人表示认同。我读了好几遍，都不能认同。。

买了个录音笔，打算记录一下自己的日常生活，周六的时候录了一个小时自己的碎碎念，因为不知道自己能说多久，也不知道自己会说些什么，录完之后自己再听，感觉有些奇妙。打算继续尝试。