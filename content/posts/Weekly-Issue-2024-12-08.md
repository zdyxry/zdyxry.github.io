---
title: Weekly Issue-《选择安乐死的日本人》
date: 2024-12-08
tags:
- Weekly
description:  
---


## 文章

### 技术

[The next platform](https://www.macchaffee.com/blog/2024/the-next-platform/)

作者提到的 [[kubernetes]] 的问题：
- Steep learning curve.
- Lots of moving parts.
- Requires a dozen other CNCF projects to do useful work.
- Helm templating was a mistake but it's too popular now.
- Everything has to be containerized, which complicates dev environments and slows down CI/CD.

我日常需要的是一个随时启动的、持久化的 VM/Container。话题太大，以至于没有想法。

---

[Gregory Szorc's Digital Home | Transferring Python Build Standalone Stewardship to Astral](https://gregoryszorc.com/blog/2024/12/03/transferring-python-build-standalone-stewardship-to-astral/)
[A new home for python-build-standalone](https://astral.sh/blog/python-build-standalone)

`python-build-standalone` 项目将转移到 [[Astral]] Org 下。过去几个月的版本发布已经是 Astral 员工维护，为了更好的体现这一点，所以进行了转移。

`python-build-standalone` 的一个 Release 包含的 Assets 有 947 个，这会不会是 Github 上面最多的.....

---

[What is proto? | moonrepo](https://moonrepo.dev/docs/proto)

一个新的版本管理器，重点是 pluggable。不知道和 [[mise]] 的区别是什么。

---

[Pessimistic or Optimistic Concurrency Control? Lessons Learned from Real-World Customer Scenarios | by siddontang | Dec, 2024 | Medium](https://medium.com/@siddontang/pessimistic-or-optimistic-concurrency-control-lessons-learned-from-real-world-customer-scenarios-a4f0b8dd6e49)

> What We Learned from Customers:
> - Don’t Assume the Customer Knows Their Workloads
> - Don’t Assume the Customer Knows How to Write Retry Logic
> - Don’t Assume the Customer Can Easily Change Their Codebase
> - Don’t Assume the Customer Only Has Short, Small Transactions
> - Don’t Assume the Customer Understands Which Keys Are Prone to Conflict

> **If there’s one lesson we’ve learned, it’s this: Always evaluate concurrency control strategies in the context of real-world conditions, not just theoretical ideals.  

---

[专栏：职场不用喝咖啡 - 开篇](https://world.hey.com/xiaowen/post-e21b61eb)
[专栏：职场不用喝咖啡 - 工作的收益究竟是什么？](https://world.hey.com/xiaowen/post-f0f31070)

忘记是什么时候在推特上关注的 Xiaowen 了，是靠谱的职场老大哥，他的一些观点我时不时的会重新看一看。还有一位职场老大哥是在豆瓣上关注的 ，他可能不想太多人关注到，就不贴了。

---

[iptables 拦截 bridge 包的问题排查 | 卡瓦邦噶！](https://www.kawabangga.com/posts/6726)

> 经过一通乱查，发现 Bridge 的包跑到了 iptables 里面去，被 iptables 的 FORWARD chain DROP 了。

> 我有一个排查 iptables 是哪一条 rule 丢包的妙计，就是 `watch -d "iptables -nvL | grep DROP"`，watch 会监控引号中的脚本，脚本会过滤出来所有会丢包的 rule，`-d` 参数很关键，它可以让 `watch` 每次对比和上一次命令的不通，然后高亮出来。一眼定位到问题。

---



### 生活

[韩国旅行回忆：首尔、釜山与仁川的真实体验 - Jimmy Song](https://jimmysong.io/blog/south-korea-trip/)

> 评价：下次可能不会再来了

[[韩国]]游记。刚好最近朋友也去韩国玩了很久，跟我推荐釜山。我还挺想去一次韩国的，因为日常看韩剧比较多，听歌也听 K-pop 多一些，想实际的去看看韩国的生活。

---


## 书影

《选择安乐死的日本人》，前阵子安乐死的相关讨论很多（大家在谈论安乐死的时候默认指的是主动安乐死），但是自己对于这个伦理话题没有什么想法，想着找本书来了解下。书里讲述的主体是一个单身年长女性患病（MSA）“自死”的过程记录。当前日本是不允许安乐死的，所以她选择去瑞士去寻死。当前安乐死的前提条件是：a. 有难以忍受的病痛；b.没有治愈的希望；c.能够明确地表达意愿；d.没有患者期望的治疗手段。这个世界还有很多的病痛没有解法，患者知道自己接下来的生活状态会是什么样子，比如失去沟通能力、无法行走、无法自理。安乐死分为两种，一种是机构把药给患者，由患者自行服用；另一种是医生主动投药使患者死亡。

当一个人因为患病痛疼难忍，作为一个人的基本能力丧失，无法自理，这不仅仅是自己生理上的痛苦，精神上的痛苦更难忍。患者不会主动说出自己的不方便，会因为尊严尽可能的“少麻烦其他人”，当他人照顾患者的时候，既要考虑尽可能的方便患者，提供患者能够“自己”完成必要的自理活动，又要避免做的过多，导致伤及患者的自尊心，这里的尺度非常难以控制。我多多少少听过一些老年人上年纪生了病之后，会脾气大变，对自己的亲人恶语相向。而在没有安乐死的国家，患者的生活水平又是由亲人决定的。国内没有安乐死相关的法案，几年前出国一个“丈夫拔掉妻子氧气管”案，丈夫的说法是不忍心自己的妻子忍受痛苦，所以拔掉氧气管，最后的判罚是有期徒刑3年，缓刑3年。

我觉得选择安乐死的人，是积极的面对死亡的人，他们是亲自面对死亡的人，比亲人考虑的更多。这里的积极不是贬义，而是他们主动的选择，选择体面的结束自己的一生。




## 碎碎念

* 突然有些好奇，Inoreader/Feedly/Follow 这种 RSS 平台，当前活跃的 RSS Feed 数量是多少？如果活跃的定义是一个月有一次更新的话，这个会影响他们内部的抓取频率么？
* 一部作品，没有看过硬要评价，只会让人不适。
* 博通现在的 CEO Hock Tan 是马拉西亚人。
* 文案相关： 在“和”、“与”、“或”等连词前不应使用顿号。
* 少说一点“正确的废话”，世界会变得美好。
* 现在各个 AI 编辑器就是，每当我觉得已经站起来了，他都会告诉我，我还没有。
* 谨防逻辑谬误。
* 给人留下“靠谱”这个印象，是好事还是坏事
* > If your solution to some problem relies on “If everyone would just…” then you do not have a solution. Everyone is not going to just. At not time in the history of the universe has everyone just, and they’re not going to start now.
* 不要在对外公布的文档中使用 "`" 来引用代码，尽量使用 "```" ，否则有可能文档的用户会直接粘贴去执行。不能假设所有人都知道 Markdown。