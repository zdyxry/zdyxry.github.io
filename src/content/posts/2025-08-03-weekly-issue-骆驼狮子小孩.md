---
title: Weekly Issue-《骆驼狮子小孩》
date: "2025-08-03T00:00:00.000Z"
slug: "Weekly-Issue-骆驼狮子小孩"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Summary of Heroku June 10 Outage | Heroku](https://www.heroku.com/blog/summary-of-june-10-outage/)

[[Heroku]] [[事故分析]]，这个故障造成一些客户长达 24h 的停机，属于重大事故了。

> A lack of sufficient immutability controls allowed an automated process to make unplanned changes to our production environment.

发生了什么？
- 生产环境运行了本应该禁用的操作系统更新，在更新过程中重启了网络服务
- 网络服务有一个遗留脚本，该脚本只在系统启动时执行一次，如果后续网络服务重启不会执行，导致网络中断
- status 站点与内部工具运行在同一个环境中，当生产环境发生故障，内部报警通知也故障了

看到他们现在的 status 页面的域名还是 `status.heroku.com`，感觉之后还是会可能发生因为 DNS 配置文件导致用户无法访问 status 页面，这里建议的做法是搞一个 `company+status.com` 域名来提供 status 页面，比如 `www.cloudflarestatus.com`。 

---

[Choosing Between Count and For-Each | Ned In The Cloud](https://nedinthecloud.com/2022/01/27/choosing-between-count-and-for-each/)

[[terraform]] 的 `count` 和 `for_each` 差异。`count` 生成的是一个有序列表，通过整数索引来访问，`for_each` 生成一个 map，通过唯一键来访问。当列表顺序发生变化， `count`  会先删除原有资源然后重新创建，`for_each` 不会。推荐默认使用 `for_each`。

---


[How we tracked down a Go 1.24 memory regression across hundreds of pods | Datadog](https://www.datadoghq.com/blog/engineering/go-memory-regression/)

[How Go 1.24's Swiss Tables saved us hundreds of gigabytes | Datadog](https://www.datadoghq.com/blog/engineering/go-swiss-tables/)

[[DataDog]] 在将 [[Golang]] 升级到 1.24 之后的经历。
- RSS 显著增加，但是 Go Runtime 的内存统计数据没有变化
	- 通过检查 `/proc/$pid/smaps` 对比，发现 Go Heap 增加了，最终 Golang 团队定位是 1.24 在进行 mallocgc 重构时移除了一个优化：在分配包含指针的大对象时，Golang 会无条件的重新清零这些内存。
- 1.24 的 Swiss Tables 哈希表实现带来了内存效率的明显提升。

---

[Our $100M Series B / Oxide](https://oxide.computer/blog/our-100m-series-b)

[[Oxide]] B 轮融资了 $100 M，还是那个问题，什么客户会购买他们的产品呢？

---

[GitHub - charmbracelet/crush: The glamourous AI coding agent for your favourite terminal 💘](https://github.com/charmbracelet/crush)

开源版本的 Claude Code，是 Golang Charm 团队维护的，目前在 Golang 生态中编写 TUI 的话可能大概率会选择 Charm 的 bubbletea ，不知道这个使用体验是否会好一些。

另外有趣的是它们的 License 是 [FSL - Functional Source License](https://fsl.software/)，FSL License 会在 2 年后自动转换为 Apache 2.0 或 MIT，相当于提供了一个 2 年的商业保护期。

---
[Making Postgres 42,000x slower because I am unemployed](https://byteofdev.com/posts/making-postgres-slow/)

喜欢这篇文章，各种意义上。当大部分人在告诉你如何变得更好时，找到一些变得更糟糕的办法也可以更好的了解系统运行方式。（我司产品的一些 bug 就是靠着各种嵌套集群发现的。

---

[PDF 电子书重排和裁剪 | 卡瓦邦噶！](https://www.kawabangga.com/posts/7048)

[Willus.com's K2pdfopt](https://www.willus.com/k2pdfopt/) 可以对 [[PDF]] 进行裁剪，比如去掉边框空白部分。

---
[AWS deleted my 10-year account and all data without warning](https://www.seuros.com/blog/aws-deleted-my-10-year-account-without-warning/)

作者在 [[AWS]] 的所有服务都因为 [[AWS]] 内部错误丢失了，[[AWS]] 推脱说是因为作者没有及时的完成身份验证，所有数据都被删除了。作者是在住院期间收到的邮件，在确认要住院前，还特意把所有的数据都备份到 [[AWS]] 上。

难以想象该有多绝望（想了一下我自己的数据，如果 Google 突然删除了我的账号，我的很多关联事项就会瘫痪。。


---


### 生活

[大厂祛魅：破碎的专注力](https://capops.xyz/suckwork)

> 在这里，大厂员工的话题总是围绕着数字：工资、级别、股票、分红、年终奖。置身其中，让人不禁感慨自己仿佛是一位职场新手。

说起来，我从北京来到上海有部分也是因为这个原因。直到现在，当我身边有同事因为发布了某款 3A 游戏请假去玩的时候，我还是会很开心，这个环境是我喜欢的。

---
[My Experience Working at TSMC Arizona For 4 Years : r/Semiconductors](https://www.reddit.com/r/Semiconductors/comments/1m96m4f/my_experience_working_at_tsmc_arizona_for_4_years/)

> They refused to help us because "Americans make too much money for us to help them."

> Also, all of those I still talked to that had quit said they were better off. Every project comes from the "mother fab" in Taiwan and needs to be followed no matter what, excluding logic or reason. So there was zero place for innovation or even basic brain use. The job became show up, see what you're being told to do that day, have the plans change, fix it, be super behind, rinse and repeat.

> It created a very toxic style of no teamwork, no one helping anyone, and overall delaying all projects.

> **I work to live, they live to work.**

一名美国台积电员工的经验贴。这里的描述符合我对一个糟糕工作氛围的想象。

---

[Product Manager vs. Product Owner: Why Teams Get These Roles Wrong - The New Stack](https://thenewstack.io/product-manager-vs-product-owner-why-teams-get-these-roles-wrong/)

> **Product Manager (PM): Driving the What and the Why**
> **Product Owner (PO): Owning the How and When**
> While the PO role is crucial within Agile teams, it should not be confused with product management. Assigning PO responsibilities to someone without strategic training or customer exposure often results in delivery without direction.
> **Business Analyst (BA): Making Clarity From Chaos**
> **Delivery Manager: Keeping the Wheels Turning**
> **Technical Product Manager (TPM): Translating Vision into Systems**
> **Product Marketing Manager (PMM): Crafting the Narrative** 

印象中和朋友聊过很多次这些岗位对应的职责，很多时候都是混乱的，如果直接从职责去聊，然后把职责扔到具体的人身上，不定义岗位，可能就清晰多了。

---

[一次家庭沟通](https://www.douban.com/topic/330794081/)

> 起因是他发了一个关于现在的中国人普遍不感恩父母的视频，明显是针对这类老年人的流量，我则一直秉持着即便冒犯也要实话实说的态度，把我同温层里的普遍认知发给他看。对这种思想进行解剖和批评。  
> 结果当然是老父亲各种感叹号问号排比句，近乎破口大骂。我也继续启动激情互怼模式。   
> 但是突然之间，我对他发来的一些恶狠狠的微信文字产生了间离感。过去那种 ptsd 没有再发作，而是变成了一种轻微的滑稽感。我竟然拿着手机笑了出来。

> 我不会对爽文应激和生气，因为它其实根本无法威胁到我。我反而会想一想，对方说这些，是在向我乞求什么，我可以适当满足，而不要看成是压迫。只要不是心理变态的父母，你真的做出卧冰求鲤的举动，他们反而会吓坏了的。所以，根本无须以为宣扬孝道就真的希望你那么做。这只是一种低层次认知里的夸张。

---



### 书影播客

《骆驼狮子小孩》，宁家宇单口喜剧专场，豆瓣评分目前是 7.1。这个专场没有开场演员，主持人下台之后直接就是他自己讲，讲了 2h，相较于国内的其他专场，实在是太长了。

在我观察中，宁家宇是有一个很得体的社会身份的，东北人，毕业之后进入辽宁广播电视台，有几档受众还不错的节目，结婚生子，在广播行业不景气之后，离职在沈阳创办了单口喜剧俱乐部，同时自己也在北京演出。不管怎么说，这个社会身份是很不错的。但他在喜剧行业里的评价是两极分化的（可能不喜欢的更多一些），播客和单口都不讨喜。

这个专场的名字是来自于尼采的《查拉图斯特拉如是说》，骆驼、狮子、小孩分别对应着不同的精神状态，在这个专场中，宁家宇将其分别对应于他自己、老婆、儿子。讲述的是一个中年男人在亲密关系中，在面对现在的“主流”声音时，自己的一些想法。在看的过程中，感觉其中的有些观点有些别扭，这个别扭不是来自于观点，而是来自于观点和他这个人的矛盾，不知道是不是为了迎合观众，感觉他有点太在意了。他作为一个中年男人，面对来自社会身份的压力，一直在以骆驼的状态去“我应该”；在与老婆平时的沟通中的“谨慎”，发现老婆一直在“我要”；在与儿子想要做朋友，但是发现儿子真的“不拿他当爹”之后产生的身份失衡，发现儿子一直处于“我是“，心态失衡。回应到开头我观察到他的社会身份，他为了在这个社会身份中扮演一个合格的角色，活的很累。

《不开玩笑-202. 低头不见抬头见：聊聊邻里间那些事》，感觉大家都差不多，只有小时候会去邻居家串门，或者因为有了孩子之后，邀请孩子的朋友到家里串门。

《不开玩笑-203. 赛出风格，赛出水平，聊聊比赛，斯密马赛》，知道了淘宝有一个“丑东西”大赛，最近在杭州有线下展览，确实挺丑的： [淘宝首个丑东西线下展，也太没创作瓶颈了](https://www.digitaling.com/articles/1385089.html) 。



## 碎碎念

* 孕妇效应明显：周六晚上和朋友吃云南菜，聊到了：马来西亚、云南。结果当天吃完饭就在朋友圈看到了马来西亚，第二天收到了同事请假去云南玩。
* 一些服务连基本的 schema 都没定义好，就要提供 MCP Server 了。也太胡闹了。
* 工作日下午 3 点的 KFC，好多人捧着全家桶在吃，感觉是工作遇到了委屈所以靠吃来宣泄下。
* 不考虑 DevEX 就算了，一个仓库 700M 是闹哪样啊。
* 一个完全内部的项目 Python 版本还停留在 3.8 ，工具链还是上古的，怎么忍受的。
* 在 Bash 里看到 eval 总是会很小心。
* 我以为交接过来的东西已经快结束了，结果才刚开始，我年轻了。
* 7 月跑步 178km
* Figma 凭啥值一半的 Adobe 呢？
* 感觉最近半年收到的垃圾邮件，比之前几年都多。
* 暑假请假的人真多。
* 每次用 Gemini 2.5 Pro 的时候，都想说：大就是好
* 一直想统计一下公司内部到底有多少个 Dogfood 节点，发现数量比我想象中要少。