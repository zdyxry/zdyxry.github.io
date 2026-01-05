---
title: Weekly Issue-2026
date: 2026-01-05
tags:
- Weekly
description:
---



## 文章

### 技术

[It Works On My Cluster: A Tale Of Two Troubleshooters | Octopus blog](https://octopus.com/blog/verifying-and-troubleshooting-kubernetes-deployments)

https://medium.com/@amirilovic/how-to-fix-node-dns-issues-5d4ec2e12e95

> Kubernetes has a gift for making simple problems look complicated, and complicated problems look simple.

> 1. Schema cache writes files to a shared volume on one pod
> 2. Schema is attempted to be read/written by another pod
> 3. Under high traffic, these operations deadlock
> 4. The cache operations saturate the threadpool while waiting on locks
> 5. `dns.lookup()` calls queue up waiting for a free thread
> 6. Queued DNS lookups eventually timeout
> 7. Application logs: `EAI_AGAIN`

也不能啥事都往 DNS 身上推。

---

[Go away, Python!](https://lorentz.app/blog-item.html?id=go-shebang)

```Golang
//usr/local/go/bin/go run "$0" "$@"; exit
package main

import "fmt"

func main() {
	fmt.Println("Hello world")
}
```

又一个利用 shebang 做文章的，uv + PEP723 已经足够好用了，仍然认为这样搞是邪教。
倒是文章的最后为了避免 go fmt 的写法挺巧妙的，学到了： `/*usr/local/go/bin/go run "$0" "$@"; exit; */`。

---

[2025](https://samwho.dev/2025/)

> I don't think I'm being dramatic when I say that writing on this blog has changed my life. Without Load Balancing, there's simply no way the last few years would have panned out how they did.

作者因为博客文章写的很好，之前比较出名的一篇应该是：[Load Balancing](https://samwho.dev/load-balancing)。改变了职业方向，转职在市场营销部门做 Developer Educator ，可能是类似于 DevRel ？

---

[MongoBleed explained simply - by Stanislav Kozlovski](https://bigdata.2minutestreaming.com/p/mongobleed-explained-simply)

[[MongoDB]] CVE-2025-14847 解释，根本原因在于服务器在解压缩消息后，完全信任客户端提供的 `uncompressedSize` 值，以此作为分配内存缓冲区的依据，不会验证解压缩后的实际数据大小。这导致分配的内存缓冲区中，除了真实数据外，还包含大量来自先前操作的、未被清零的堆内存数据。

---

https://blog.miguelgrinberg.com/post/a-year-in-review-flask-in-2025

FastAPI 的增长非常明显，2025年的 PyPI 下载量已与 Flask 持平，在开发者调查中也是最受欢迎的框架。趋势一旦形成，就很难逆转了。

---

[GitHub - bketelsen/phukit: see github.com/frostyard/nbc for continued development](https://github.com/bketelsen/phukit)

> A Go application for installing bootc-compatible containers to physical disks with A/B partitioning and atomic updates.

虽然介绍是 `bootc-compatible` ，但是其实和 boot/ostree 关系不大，唯一的关系可能就是分区可读性是一致的，其他的没有用到 ostree 的特性。当前实现的方式中，分区是严格写死的，并且在 3-way merge 的阶段实现粒度很粗，在 pristine 的操作流程上感觉也有 bug。

作者后续更新放到了 [Frostyard · GitHub](https://github.com/frostyard) org 下： [GitHub - frostyard/nbc: NBC is not bootc](https://github.com/frostyard/nbc) 

上面提到的 3-way merge 简易实现的问题，彻底换了实现方式，改为使用 overlayfs 来挂载  `/etc` ，利用了 dracut `pre-pivot` hook，在这个阶段来做 `/etc` 的准备，实现的方式有些 hack：

* overlayfs 挂载点不能和 lowerdir 是同一个目录，所以把 `/etc` 改为 `/.etc.lower`，然后把 `/.etc.lower` 作为 lowerdir，upperdir 设置为 `/var/` 下的 dir，最终挂载点是 `/etc`；
* 为了避免用户误操作 `/.etc.lower` ，还挂在了一个不可访问，大小为零的 tmpfs： `mount -t tmpfs -o size=0,mode=000 tmpfs "$SYSROOT/.etc.lower"`。

这种方式真的有些取巧，另外 dracut hook 的调试很不方便，要是我来搞可能会把 3-way merge 完善好，至少好调试啊。

---


### 生活

[可乐外交](https://scateu.me/2025/12/18/cola-diplomacy.html)

> 可乐外交也有细分级别:
>- 无糖可乐
>- 有糖可乐
>- 冻瓷实的冰块可乐，用来砸对方
>- 或者把可乐直接洒地上祭祀对方

哈哈哈哈哈哈。

---

[Leon Fong](https://leonfong.me/)

> Experiencing a new culture, tasting different foods, and meeting people from all over the world opened my eyes to the incredible possibilities beyond my familiar surroundings. From that moment on, I was hooked on travel.

> After returning home, I quit my cubicle job and in March 2025, I set off on my first long-term backpacking trip — my first solo journey as well.

恭喜这位朋友，估计很多人有过类似的想法，但是无法真正迈出这一步。

---

[100gle's Blog - 三十而立——我所看到的世界](https://devlike.top/posts/before-30)

> 所以时至今日我总会跟她说，我要是她，我绝对不会嫁给我爸这种大男子主义、好吃懒做又不会顾家的人，我妈听罢也总是沉默无言。

这话对于母亲来说，有些残忍。

---

[2025 年终总结 | OneV's Den](https://onevcat.com/2025/12/2025-final/)

> 对我，对我的两个孩子来说，相比具体的解题技巧，更重要的也许是：我们是否还能[保持对世界的好奇](https://onevcat.com/2015/12/2015-final/#%E5%A5%BD%E5%A5%87%E7%9A%84%E7%9B%AE%E5%85%89%E5%A7%8B%E7%BB%88%E6%98%AF%E6%9C%80%E7%BE%8E%E7%9A%84)，是否愿意持续学习 “如何学习”，而不是执着于囤积某一代注定会贬值的知识。毕竟在这个时代，唯一看起来不那么容易被自动化的，可能只剩下提出好问题的能力。

> 当执行的门槛被压到极低，试错的成本随之下降，真正稀缺的反而变成了另一种能力：品味与判断。你不再需要知道每一块砖是如何砌成的，但你必须清楚自己想要建造怎样的一座房子，以及它是否美观、稳固、值得存在。

我觉得正是因为执行的门槛大大降低了，执行力反而显得愈发重要，去“写”更多的代码，去做更多的项目，LLM 加快了反馈周期，可以[更快的](https://jsomers.net/blog/speed-matters)去训练自己，形成一个正向循环。快就是好。

---

[我的姥姥 | 卡瓦邦噶！](https://www.kawabangga.com/posts/7151)

> 姥姥的去世，我没有为她感到伤心，只**为我以后再也见不到她了而伤心**。至少她的晚年可以抽烟吃肉，没有把时间都花在了 ICU 里面。

---

[2025年年度总结 | Kivinsae's Nest](https://www.kivinsae.com/2026/01/02/2026-01-02-Summary/)

> 正如很多人所说，这个时代你最好拥有一些和原子有关（可触摸的物质）的技能树，而不能仅仅拥有和电子有关（信息）的技能树，后者的利维坦已经降临在人间了。

> 如果说这个世界是一个硬核模式的角色扮演游戏的话，时刻关注自己的血条永远是第一要务。   
> 世界已经展示了一个存在 AGI 拐点的未来，和毫无意义的努力和学习相比，活到那个时刻才是最有价值的投入 —— 公园里可没有肥胖的老人，他们早就死了。

> 成人的世界其实很少有确定性的非常高的东西，甚至于绝大多数人滚出第一桶金的唯一方法就是对外出售自己的确定性。

我最近对“无伤”的理解好像又加深了一些，2025 年我跑步的目标就是无伤。很久以前看一些游戏视频，不理解为什么要追求“无伤通关”，发现对于现实世界来说，血条是一切的根本，过早的关注无伤是好事，2025 财务复盘中，医疗分类支出已经连续 3 年在增加了，增加的速度还是夸张的翻倍。

---

[年度扯淡 2025](https://archive.is/YEHxq)

> 而专注生产力工具的公司就比较难说了，大部分生产力工具的能力最终都会被内化在某个平台中，从而消亡。能存活下来的只有少数个别公司，最终也难逃被收购的命运。也许 Cursor 会存活下来，但也有很大的可能是被微软或 Google 收购。

老板的年终总结。

---
[2025年终总结 | 不厌其烦](https://blog.yiyu.me/2025/12/31/2025-year-end/)

> 作为一个技术人身处这样的浪潮之中，很难不为AI技术中的各种可能性而感到激动。有一个流行起来的词，“超级个体”，指的是最大限度运用AI技术增强自身能力使自己成为多面手(generalist)的这么一个个人发展方向。在2026年，我希望自己好好磨好AI这把刀，把柴砍得又快又好，看看自己朝着超级个体的方向能走多远吧。

GKE Observability Leader 的年终总结。

---



### 书影播客

《百变小红帽-一则童话三百年的演变》，从小就听过小红帽的故事，这本书将的是不同时代的小红帽故事的不同版本，以及当时的社会背景，挺有意思的，比如为什么会有猎人这个角色。讲故事的最终还是成年人。

《借口 Go》年度颁奖，看到了很多熟悉的韩国演员和歌手，华莎和尹敬浩还现场复刻了朴正民的演出，很难不笑场。

《利刃出鞘 3》，灭霸演的真好。

《捕风追影》，成龙、梁家辉、跟踪队、小花猪。之前看过几遍《跟踪》和《绝密跟踪》，在看的过程一直跳戏。如果之前没看过这两部电影，应该会觉得挺不错的。


## 碎碎念
* 上一次休假还是 5 月
* 生活好简单，休假想到的放松方式是来图书馆随便找本书看
* 你知道自己家附近哪有裁缝店么？你会买鱼做菜么？
* 图书馆的《疼痛部》虽然封面有些旧，但是内部跟新书似的。
* 在很多浏览器插件在疯狂的占有划词的空间，昨天远程朋友电脑，选词之后居然同时有3个插件在工作，和哪吒的三头六臂差不多了。
* 年终对账，今年很不满意。
* 发现自己可以用5分配跑5km，之前对自己还是太宽容了，可以适当顶一顶。
* 形容一个人的生活状态：“生活过得很像白人”
* ampcode free 模式最近好像改模型了，之前一些简单的功能，突然无法执行了
* 跑步 19km，流失汗液大概在 2kg
* 看了看 Clicks Communicator 的介绍，还挺喜欢的。
* Opus + Gemini Pro 额度用完，也没有解决样式隔离问题，果然CSS 是一座大山。