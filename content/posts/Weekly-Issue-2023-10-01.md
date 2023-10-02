---
title: Weekly Issue 2023-10-01
date: 2023-10-01
tags:
- Weekly
description: 在家最多待 7 天。
---


## 文章

### 技术
[Fixing For Loops in Go 1.22 - The Go Programming Language](https://go.dev/blog/loopvar-preview)

终于不用再 [[Golang]] for loop 中重新声明变量了。

[μMon: Stupid simple monitoring](https://tomscii.sig7.se/2022/07/uMon-stupid-simple-monitoring)

作者逆潮流的选择了 [[RRDtool]] 来实现自己的监控系统。

吐槽 [[prometheus]] & [[Grafana]]：占据不少磁盘空间的 [[TSDB]]、内存资源消耗、配置复杂、网络通信（闲置系统中的噪音）、复杂的前端页面、DSL。

---
[Don't trust default timeouts | Roberto Vitillo's Blog](https://robertovitillo.com/default-timeouts/)

大部分 client 都没有设置 timeout，尽量显式的设置 timeout 来让程序符合预期。

---
https://morven.life/posts/git-like-os-fs/

关于 [[ostree]] 的背景介绍，使用 chroot 来隔离不同的操作系统根文件系统，使用硬链接来避免不同操作系统根文件系统之间的文件重复（通过链接到只读文件系统来限制跨更改的影响）。

[[ostree]] 已经发展这么久了，好像还没有看到大规模的应用或流行的迹象。作为开发使用的操作系统不会选用这个，因为限制太多了，作为生产上，需要确保所有的应用全部容器化，实际运维管理起来也没有那么美好，毕竟除了 rootfs 的变更，系统配置也是需要配合变更的。

---

[Typo traps: analyzing traffic to exmaple.com (or is it example.com?)](https://blog.cloudflare.com/typo-traps-analyzing-traffic-to-exmaple-com-or-is-it-example-com/)

关于 example.com 和 exmaple.com 的分析，typo 引发的流量比想象中的要大得多。想到了 [gail.com FAQ](https://gail.com/) 。

---

[Open Source does not win by being cheaper · getlago/lago Wiki · GitHub](https://github.com/getlago/lago/wiki/Open-Source-does-not-win-by-being-cheaper)

开源软件不能仅仅依靠成本低廉来吸引用户，因为价格敏感的用户往往只会选择免费或者价格更便宜的解决方案。

开源软件能够通过解决透明度问题来获得优势。当闭源软件引发用户对客户和供应商之间的不信任时，开源软件可以通过提供源代码和开放审计的能力来赢得用户的信任。

---

[Tyblog | SSH Kung Fu](https://blog.tjll.net/ssh-kung-fu/)

[[SSH]] 的一些使用技巧。vim 可以直接编辑 scp 远程文件，学到了。

---

[Go项目开发指南](https://chat.openai.com/share/8ac0aeec-d862-4c55-a466-95c404e0946f)

如何 step-by-step 的使用 [[ChatGPT]] 来开发一个 [[Golang]] 项目：尽可能的描述清楚需求、尽可能的把问题抛出，让 [[ChatGPT]] 来修改、如果发现有些不符合习惯的地方，尽早提出、阶段性的让 [[ChatGPT]] 回忆当前的状态。

---

### 生活
[加入灵修后，他们从裸辞到负债百万](https://mp.weixin.qq.com/s/qUZ-Otm22kD0svjt6dwANQ)

[[身心灵]]是门产业。

---

[角膜、小店和母亲的爱，他留给这世界了](https://mp.weixin.qq.com/s/qDgSz27GdB67vEpEP538sA)

看到 [[赛博朋克 2077]] 的新闻，搜了搜相关的故事，真好啊，看开了。

---

[我的笔记实践的变化。 - Xiaowen.Z Deployed](https://xiaowenz.com/blog/2023/09/my-noting-practice/)

* 笔记应对具有原子性
* 笔记应该基于概念/观点
* 笔记应该自然的连接
* 尽量用关联替代层级关系
* 为自己记笔记，不要考虑受众

---

[从学术角度吃瓜《再见爱人》嘉宾李松蔚水平究竟如何](https://web.archive.org/web/20230929071321/https://www.douban.com/note/854436565/?_i=5971573jowl3CC)

因为现在是播客的重度用户，而中文播客中有一个很大的类目，是身心灵，大家追求自己，不断的探寻内心。但是我对这个一直不感冒，尝试过，但是不理解，前段时间听了[[学霸猫]] 的音频，对于[[学霸猫]]的好友：[[张潇雨]]，[[Steve]] 都抱有怀疑的态度。

今天看到有人举报[[李松蔚]]性侵，看到了这篇文章，我希望大家扒一扒这些”身心导师“，看看到底是不是水货。

关联阅读：
    [心理行业的黑暗面到底有多黑？ - 知乎](https://www.zhihu.com/question/24082424/answer/104443213)
    09 年以前，是可以花钱直接买心理咨询师证书的。

---


[Sine - Xe Iaso](https://xeiaso.net/blog/sine/)

有趣的故事，人类情感和科技之间的关系。我们应该更加看重人与人之间的联系，而不是妄图从 Bot 中获取慰藉。

---

## 书影

《不开玩笑》，看完了，前半段在讲幽默、喜剧。后半段在教你如何上台讲脱口秀，是一套完整的方法论。

《摸心第六感》，朋友推荐的，刚开始看。