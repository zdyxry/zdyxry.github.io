---
title: Weekly Issue 2023-09-24
date: 2023-09-24
tags:
- Weekly
description: 国庆假期开始了。
---


## 文章

### 技术

[相关技术 - NebulaGraph Database 手册](https://docs.nebula-graph.com.cn/3.6.0/1.introduction/0-2.relates/)

[[GraphDatabase]] 的简单介绍，其中提到了一些开源的 [[Graph]] 分析工具：NetworkX, Cytoscape, Gephi等。

---

[简单聊一下开源 - (ゝω·)~ kira](https://blog.dreamfever.me/2023/09/12/jian-dan-liao-yi-xia-kai-yuan/)

这篇文章记录了作者参与 [[Bun]] 的一些感受，背后是有一个公司去运营的，在 Issue 和 PR的管理上都是混乱的。

---

[Windows Subsystem for Linux September 2023 update - Windows Command Line](https://devblogs.microsoft.com/commandline/windows-subsystem-for-linux-september-2023-update/)

[[WSL]] 终于可以回收内存了。当设置 `AutoMemoryReclaim` 为 `gradual` 时，当 WSL 闲置 5min 后，自动释放内存。通过设置 `cgroup.memory.reclaim` 来实现，需要禁用 [[cgroup/v1]] ，当前会导致 [[Docker/Desktop]] 无法工作。

---


[Github commit 签名+合并 Commit | crossoverJie's Blog](https://crossoverjie.top/2023/09/18/ob/git-tips-rebase/)

对 git commit 进行签名。

---

[Zig Makes Go Cross Compilation Just Work - DEV Community](https://dev.to/kristoff/zig-makes-go-cross-compilation-just-work-29ho)

使用 [[Ziglang]] 可以非常容易的实现 Go 程序在不同平台间的编译,不需要处理 cgo 的各种问题。

---

[Automate (But Automate Last)](https://matt-rickard.com/automate-but-automate-last)

> Automate. That comes last. The big mistake in Nevada and at Fremont was that I began by trying to automate every step. We should have waited until all the requirements had been questioned, parts and processes deleted, and the bugs were shaken out.

只有在充分的了解了当前流程中每一个细节之后，再考虑自动化才能符合预期。

---

[从 Manjaro 切换到 EndeavourOS](https://manateelazycat.github.io/2023/09/10/endeavour-os/)

作者将[[开发机]]从 [[Manjaro]]切换到了[[EndeavourOS]]。我现在在使用 [[Garuda]] ，与 [[EndeavourOS]] 的主要区别是：[[Garuda]] 针对图形界面更友好；默认使用 [[btrfs]]创建快照；也意味着更臃肿。


### 生活

[焦虑的普通家庭小孩，都挤在张雪峰直播间里](https://mp.weixin.qq.com/s/dsGvj0earMzk0APMBr3_UQ)

> **这个时代让人不安的，不是张雪峰们的言论。**  
**这个时代让人不安的，是很多人真的需要一个张雪峰。**  

---

[CyberClip #42 极简主义的幻象](https://shyrz.me/cyberclip-42-the-illusion-of-minimalism/)

> **极简主义已不再只是关于简化生活，它越来越被广泛地称为审美极简主义——就是你的家有多么时尚、整洁、明亮和通风。**  
**这种极简主义的含义显而易见，但它似乎从未被提及：唯一能够以任何有意义方式「实践」极简主义的人，是那些无需被经济条件所迫的人。**  

---

[钱包瘪掉的中产，正在1688里购物_投资界](https://news.pedaily.cn/202309/522476.shtml)

之前一直购买的淘宝店铺自从升级为天猫店铺之后，衣服越来越贵了，[[1688]] 可以很方便的找到一些平替产品。

---




## 书影


《不开玩笑》，写的真好，引经据典，正在看，有点喜欢。

《大宋少年志》，看完了，中规中矩，故事没有那么的宏大，感觉还是有点小家子。

《超异能族》，在今年韩剧整体拉胯的时候，这部剧算是不错的了，无论是孩子还是父母的剧情，都排的很好。按照目前的剧情会有第二季，在有意的交代了北朝鲜异能人士都是被逼无奈之后，感觉要成立复仇者联盟了？

