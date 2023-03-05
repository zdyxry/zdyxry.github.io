---
title: Weekly Issue 2022-09-11
date: 2022-09-11 23:50:00
tags:
- Weekly
description: 记录一下自己每周读过的文章，看过的电影，阅读过的书籍。
---


## 文章

### 技术

[容器技术之发展简史](https://mp.weixin.qq.com/s/ccFkJJz97KcuXdO3r5zdXA)

容器技术以及公有云容器功能支持历史。

---

[如何编写低耦合可维护的 Python 代码](https://changchen.me/blog/20220911/how-to-write-maintainable-python-code/)

通过观察者模式和装饰器模式来编写可维护代码。

---

[CPU 是如何与内存交互的?](https://www.luozhiyun.com/archives/701)

---

[How to send raw network packets in Python with tun/tap](https://jvns.ca/blog/2022/09/06/send-network-packets-python-tun-tap/)

如何使用 [[Python]] 发送读取 [[TUN]] 设备数据。

---

[What's Inside Of a Distroless Container Image: Taking a Deeper Look](https://iximiuz.com/en/posts/containers-distroless-images/)

如何选择基础 [[Container]] [[image]] 一直是一个比较重要的考虑，比如很多人不推荐的 [[alpine]]，小而美，但是 [[musl]] 不那么美。很多人推荐使用标准发行版，但是又觉得大小太大不利于分发。 [[Distroless]] 是一个可以看到的方向，但是我个人在不能完全确定自己的项目中是否依赖了某些隐式的内容时，应该还是会使用标准发行版，比如[[Debian]] 或者 [[Fedora]]。

---

[In Pursuit of Better Container Images: Alpine, Distroless, Apko, Chisel, DockerSlim, oh my!](https://iximiuz.com/en/posts/containers-making-images-better/)

博主在 [[Twitter]]  上发起了一些关于 [[Container]] [[image]] 的投票，一些人表面关注 CVE，实际上还是更关注镜像大小。 [[alpine]] 是目前大多数项目的选择，但是已经出现了一些替代品。

---


[Tips to Make Your On-Call Process Less Stressful](https://thenewstack.io/tips-to-make-your-on-call-process-less-stressful/)

关于 [[On-Call]] 建立正确的心理预期：

- 在 On-Call 之前，我需要知道所有组件是如何工作的：不，你不需要，遇到再看也是一样的；
- 遇到问题可能需要一个长期的解决方案：这不是你能决定的事情，通常是妥协的结果；
- 我应该自己解决这个问题：涉及到的组件越多，你越不可能独立解决问题，通常需要组内的其他人一起协助，不要不好意思，毕竟你节省的时间是你自己的。

---

[HOW DISCORD SUPERCHARGES NETWORK DISKS FOR EXTREME LOW LATENCY](https://discord.com/blog/how-discord-supercharges-network-disks-for-extreme-low-latency)

[[Discord]] 为了解决 [[GCP]] 磁盘稳定性的问题，通过 [[mdadm]] 来创建 md 设备，将多块 SSD 创建为 RAID0，再将 RAID0 设备和 非 SSD 磁盘创建 RAID1，并配置 `write-mostly` 参数，来让大多数写入到非 SSD 磁盘 。

---

### 生活

[2022年7月和8月总结](https://reorx.com/blog/2022-07-and-08-summary/)

初中班主任的口头禅：身体是革命的本钱。

---


[Why Slack’s free plan change is causing an exodus](https://blog.zulip.com/author/tabbott/)

Slack 免费策略修改导致用户流失。Slack 自身是一个缩写，全称是：Searchable Log of All Conversation and Knowledge。 作为一个 Knowledge ，现在的免费策略明显是不符合的。

---

[这些年来，原生家庭的影响是否被过度夸大了？](https://daily.zhihu.com/story/9752630)

> **在中国数千年来的儒家父权文化和封建思想影响下，突然进入到人本主义或精神分析的框架讨论人格的构建，这其实是非常跳跃的一个过程，因为这两个文化框架本质上就有巨大的冲突**。 **原生家庭当然是直接影响到我们的“末梢神经”，但每个个体都只是时代洪流中的一粒沙，我们自己和我们的父母都是沙，我们都对自己的人生都有些无能为力。时代或社会洪流不会对我们低头让步，于是我们只能先和自己和解，再去尝试和父母以及时代和解。即孩子也是在独立地面对这个世界、向这个世界（包括父母）发起挑战、在输输赢赢中适应下来的。父母并不能完全掌握你的人生，即使在小时候，很多决定也是你自己性格使然造成的，然后通过和父母或其他什么相互影响越走越远。**
> 

---


## 书影


《真相捕捉 第二季》：真的好看，剧情紧张，期待接下来的更新，按照第一季的节奏，应该不会烂尾。P.S. 这季涉及到部分敏感话题。

《黑话律师》：难看，真的难看。






