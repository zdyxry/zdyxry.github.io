---
title: Weekly Issue 2023-02-04
date: 2023-02-04 19:00:00
tags:
- Weekly
description: 平平无奇的一周。
---


## 文章

### 技术

[The only thing worse than cloud pricing is the enterprisey alternatives](https://world.hey.com/dhh/the-only-thing-worse-than-cloud-pricing-is-the-enterprisey-alternatives-854e98f3)    

涉及到金钱的东西总是让人头大。企业服务的定价确实很玄幻，透明度很低。

---

[OpenLens 6.3.0 - No Logs or Shell buttons · Issue #6823 · lensapp/lens · GitHub](https://github.com/lensapp/lens/issues/6823)

[[Lens]] 删除了部分功能引发了大家对其所有权的担忧，官方在推 Desktop 版本。

---

[Linux Load Averages: Solving the Mystery](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html)

[[Linux]][[负载]] 解释说明，其中关于`TASK_UNINTERRUPTIBLE` 的历史进行了调查，文章末尾提供了 [性能检查列表](https://www.brendangregg.com/USEmethod/use-linux.html)

---

[协议栈源端口选择性能衰减问题 - 撸代码 - LuCode.net](https://blog.lucode.net/network-stack/problem-of-performance-degrading-in-linux-src-port-selecting.html)

> 自kernel 4.2开始，端口资源的分配策略改了，目前奇数端口留给`bind`，偶数端口留给`connect`为了均衡资源的占用，但是显然，这种策略不适合本文所述的特殊场景，并且对于`bind`而言，也存在性能衰减的问题。

> 依次尝试去获取，当然每次获取的起点是随机的。很明显，当我们完全占用偶数组的端口后，所有后续的`connect`调用，所需的源端口应该位于奇数组中，然而该函数依旧会尝试完整遍历偶数组资源，这也就是`__inet_check_established`耗时占比这么高的原因。

---

[Introducing Hermes, An Open Source Document Management System](https://www.hashicorp.com/blog/introducing-hermes-an-open-source-document-management-system)

[[hashicorp]] 开源的基于 [[Google Workspace]] 的文档管理系统。

---

[iPotato | Fly.io 初体验之博客搬家](https://ipotato.me/article/74)

把[[Python]] 博客放到[[[Fly.io](http://fly.io/)]] 上运行。提到了 [[[Fly.io](http://fly.io/)]]的招聘流程很有趣。    

> 通过他们官网的[招聘流程介绍](https://fly.io/docs/hiring/hiring/)，可以看到他们的“面试”过程很有趣，这里的面试打了引号是因为他们其实并没有面试这一步，而是通过做 2 到 3 个挑战题的方式第一阶段通关后直接加入他们的公司 Slack 和他们的工程师工作一天，一切顺利的话就会给你发 Offer。从这样一个细节来看，除去好用的产品外，这也真的是一家有趣的公司。

---

[Future is Not Evenly Distributed](https://matt-rickard.com/future-is-not-evenly-distributed)

其中许多技术趋势仍然有很大的增长，还需要进行很多其他的工作来扩大用户。

---

[Image Stacks and iPhone Racks - Building an Internet Scale Meme Search Engine | FindThatMeme.com Blog](https://findthatmeme.com/blog/2023/01/08/image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine-Qzrz7V6T.html)

作者使用二手 & 闲置的 iPhone SE 创建了一个 OCR 的服务集群。现在手机性能已经过剩了，作为一个独立的可接入终端（4G，WIFI），有很多需求都可以通过手机运行 App 来完成，是时候学学 Flutter 了。

---

[为什么要把复杂的联表操作拆成多个单表查询？ - Jiajun的编程随想](https://jiajunhuang.com/articles/2023_02_03-mysql.md.html)   
> 让缓存的效率更高。应用程序中，简单查询对应的代码也会更简单，也就更好设计缓存，应用程序可以拆开来，缓存其中的结果，以便 下次使用复用;  
> 将查询分解后，执行单个查询可以减少锁的竞争;  
在应用层做联接，可以更容易对数据库进行拆分，更容易做到高性能和可扩展;  
查询本身的效率可能也会有所提升;  
可以减少对冗余记录的访问，MySQL联表操作可能会访问很多数据，并且可能是重复的访问  

---

[I am Mitchell Hashimoto, Founder and CTO of HashiCorp. Ask me anything! - Hashnode](https://hashnode.com/post/i-am-mitchell-hashimoto-founder-and-cto-of-hashicorp-ask-me-anything-cjr6ptyne003qdjs29mz7m3hv)


[[hashicorp]] CTO 针对社区部分提问进行回复，包含了开源社区，个人管理和公司管理。



### 生活

[土耳其 iCloud 上车指南](https://www.imbytecat.com/a7dda0b3249b448d8d5f322cc0f4467b)

[[iCloud]] 家庭共享可以跨区。

> 因此我将我的主号即美区账号作为家庭创建者，再 **通过 iMessage 邀请土区账号**（似乎其他方式会失败），由土区账号来共享 iCloud 订阅给家庭。

---



[Mental Accounting - The Decision Lab](https://thedecisionlab.com/biases/mental-accounting)

[[心理账户]]：塞勒认为，每个人都有心理账户，通过该心理账户来进行各种各样的经济[决策](https://zh.m.wikipedia.org/wiki/%E5%86%B3%E7%AD%96)。通过心理账户，可以解释人的不理性经济决策。

> 比如，我们会把工资划归到靠辛苦劳动日积月累下来的“勤劳致富”账户中；把年终奖视为一种额外的恩赐，放到“奖励”账户中；而把买彩票赢来的钱，放到“天上掉下的馅饼”账户中。

---

[Write Simply](http://www.paulgraham.com/simply.html)    

使用简单的单词和句子来写作，避免花里胡哨。

---

[My Story as a Logseq Contributor | pengx17](https://pengx17.vercel.app/posts/my-logseq-contributions)

[[logseq]]从一个用户到贡献者的故事。

---

[银行卡组织和中国卡市场的前世今生。 - Xiaowen.Z Deployed](https://xiaowenz.com/blog/2023/02/card-network-in-china/)

[[银行卡组织]] 的介绍和历史梳理。

---





## 书影

《TypeScript入门与实战》，利用春节假期看完了。

《狂飙》，大热剧，确实跟大家说的一样，看到 26集就可以了。

《伊藤润二狂热：日本恐怖故事》，恐怖，部分故事有套路，但还是很吓人。


