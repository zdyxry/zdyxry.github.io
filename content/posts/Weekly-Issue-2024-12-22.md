---
title: Weekly Issue-《数据化决策》
date: 2024-12-22
tags:
- Weekly
description:  
---


## 文章

### 技术

[Surely not all code's worth it - by Thorsten Ball](https://registerspill.thorstenball.com/p/surely-not-all-codes-worth-it)

现在一些小脚本会直接让 AI 来写，很久之前看到一句话是“十行以内，有准又快”，现在已经远不止十行了。

---


[Tale of a Kubernetes node-feature-discovery incident](https://ahmet.im/blog/nfd-incident/)

[[kubernetes]] NFD 功能异常导致的大规模集群故障。“This was partially because NFD reports a ton of kernel settings by default that we didn’t use.”，NFD 默认上报包含了很多没有被使用的 kernel 配置，一个节点的 NodeFeature 占用 140KB，大规模场景下（4000 +节点）对 etcd 和 apiserver 造成了很大的压力，导致 NFD 控制器无法从 apiserver 获取 NodeFeatures（请求超时），且由于 NFD 控制器没有处理 apiserver 异常场景，导致删除了集群中所有节点的 labels。作者集群依赖于 node label 来进行 Pod 调度配置。问题调查中发现 NFD 的实现上有不止一个场景可能会导致 node label 被删除。最终决定不依赖于 NFD，而是直接将 node label 以静态配置方式管理。

---

[OpenAI Status - API, ChatGPT & Sora Facing Issues](https://status.openai.com/incidents/ctrsv3lwd797)  
[Notes on OpenAI Kubernetes outage](https://ahmet.im/blog/openai-kubernetes-incident/)   
[Breaking down OpenAI's outage: How to avoid a hidden DNS dependency in Kubernetes](https://render.com/blog/a-hidden-dns-dependency-in-kubernetes)   
[Quick takes on the recent OpenAI public incident write-up – Surfing Complexity](https://surfingcomplexity.blog/2024/12/14/quick-takes-on-the-recent-openai-public-incident-write-up/)    
[资深k8s工程师，深入解读OpenAI宕机事故真相，以及应对策略 - xiaoqing blog](https://midbai.com/post/how-to-avoid-openai-incident/)    

> OpenAI's postmortem says that such a dependency existed in their system, because data plane services needed the Kubernetes API server (a key part of the control plane) for DNS resolution.

> Presumably, a custom DNS server is at play here and I’m not sure why it has not continued to serve stale records for a while. (e.g. CoreDNS would continue to serve stale records even if its watch connection to the API server is broken)

> 因此，我认为合理的解释是DNS缓存只是故障的其中一个因素，真正的根本原因可能是架构设计上存在缺陷，dns只是一个替罪羊。


[[OpenAI]] 官方的 [[事故分析]]，以及关注的一些其他工程师针对事故分析给出自己的想法。对于 [[OpenAI]] 的代码变更部署速度有些担心（2:23PM 代码合并，2:52 PM 代码变更在所有生产集群开始生效，这个“效率”太高了）。给出的改善方式有：引入 APF (API Priority and Fairness)、拆分独立的 etcd 集群、将 DNS 组件运行在非控制平面节点上。

---




### 生活

[2024 年终，个人设备盘点 - 苏洋博客](https://soulteary.com/2024/12/20/at-the-end-of-2024-share-personal-device-to-friends.html)

非典型用户的设备使用，同时持有这么多用户且使用率还这么高，看上去是精力充沛型选手了。
看着不错的产品：CUKTECH 酷态科 10 号超级电能棒、小米 67W 氮化镓桌面快充插座。

再次问自己：需不需要搞一台服务器放家里？

---
[英语学习过程中的一些思考](https://blog.sailfishc.com/english2)

> 知道与做到之间存在着非常遥远的距离，很多时候我们不是不知道，而是知道做不到

---

[专栏：职场不用喝咖啡 - 每个职场的关键隐藏信息](https://world.hey.com/xiaowen/post-17d13392)  
[专栏：职场不用喝咖啡 - 组织架构的意义](https://world.hey.com/xiaowen/post-b7c6276c)  
[专栏：职场不用喝咖啡 - 技能地图](https://world.hey.com/xiaowen/post-54562df2)   
[专栏：职场不用喝咖啡 - 最难跨越的职业障碍，行业](https://world.hey.com/xiaowen/post-d344d7cf)    


> 很多人把组织架构图仅仅当作一张员工关系表，这是最大的误解。组织架构是一张「权责地图」，它不仅展示了谁管理谁，更反映了公司的战略重心，分工，权利和责任的分配框架。

> 产品导向的组织架构：贴近业务，快速响应。往往重业务发展和创新，重效率多一些。
> 职能导向的组织架构：稳定性与规范性的守护者。当技术风险管理的重要性超过了业务创新时，企业就会不约而同地选择这种架构。
> 	大部分的传统企业（金融，制造等其他实体行业）都会选择这样的组织架构，核心原因是，传统企业科技部门的定位往往是「赋能业务」，而非「驱动业务」，一般行业或者监管（如金融监管）会对这类企业的信息化建设有相对更保守的要求，在企业内部，科技部门需要有更「独立」的声音，需要在必要的时候「不妥协业务」。

> 你拥有的技能越单一，职场的容错就越差，越容易被大环境影响。  
> 如果你只会写代码，意味着企业里有人费劲的设计出了一个商业模式，让一个只会写代码的人也能发挥商业价值。这也是大部分基础岗位存在的原因，也是这些岗位最容易收到经济波动，行业变化影响的原因。

> 理论上同样的功能有无数种系统实现，但每个行业的软件，其实都带着自己行业的「基因」，有在这个行业内的「最佳实践」。
> 这些代码以外的知识，决定了你的代码和实际业务之间的距离。 **技术决定你入职的下限，但行业和领域内的业务视角决定了你的发展上限。**

---


## 书影

《滔滔生活》，金爱烂。不知道是不是写作时间差别较大，我更喜欢《外面是夏天》和《你的夏天还好吗》，短时间不会再看金爱烂的作品了，年底了，去看一些无需投入感情的书。

豆瓣上关于其中《口水涟涟》的评论：
> 作为“新精英学院”国语部的辅导老师，我谨小慎微而又委屈拧巴地活着。从学生时代就被评价为不思进取，到工作了也不敢为自己主张更高的工资，我好像从来没觉得自己配拥有荣誉、高薪、舒适和体贴。  
> 忍气吞声是这篇短小的小说的主旋律，又是多少东亚女性漫长的人生的主旋律？压抑的不是文字，是东亚女性本就无法舒展的人生。    
> 我的生活两点一线。将两点放大，就构成了小说来回穿插的两个部分。职场里，男女的性别差异、职位级别、外貌凝视压着我，这是一种客观的性别凝视和阶级压迫；而在家里，与后辈的相处之中，压迫我的则是让我憋闷委屈的“教养”。什么样的孩子最难在社会立足？老实孩子，无家底，却有家教。正可谓“法家锁喉，儒家捏肋”。

《数据化决策》，道格拉斯•W•哈伯德。关于如何量化一切的一本书，最近我不理解一些同事的决策，我期望读完这本书能获得一些启发，现在我读完了，我得到的结论就是，同事并没有认真的思考自己的决策会带来什么收益，只是“下意识”/“拍脑袋”的决定。

以下是部分摘要：

- 如果人们找到观测事物的方式，并找到某种方法，无论这种方法多么“模糊”，它能让你知道得比以前多，那么它就是一种量化方法。
- 量化是减少不确定性、优化问题的有效手段。
- 量化和决策支持密切相关，而且在量化领域本身，也要作一些决策。
- 弄清楚不确定性的来源，可以帮助我们量化相关事物，以便最大限度地减少不确定性。
- 迪尔伯特法则：工作最没效率的员工被自动推向他们能造成破坏的最小单位。
- 量化的概念是“减少不确定性”，而且没有必要完全消除不确定性。
- 一旦管理者弄清楚要量化什么以及被量化的事物为什么重要，就会发现事物显现出更多可量化的方面。
- 澄清链就是把某种想象为无形之物再到有形之物的一系列短的链接过程。如果有些事物看起来完全无形无影，只是因为没有给所谈论的事物下定义。
- 4 个假设：
    1. 你的难题并发你想的那么独特；
    2. 你拥有的数据，比你认为的要多；
    3. 你需要的数据，比你认为的要少；
    4. 要获得适量的新数据，比你想象的更容易。
- 说某物不应该被量化的唯一有说服力的理由，就是量化的花费超过了它所带来的收益。
- 如果一项量化工作至关重要，那是因为它会对决策和行为产生一些可感知的效果；如果一项量化工作不能影响或概念决策，那它就没有价值。
- 不确定性：缺乏完全的确定性，也就是说，存在超过一种可能，例如人们不知道的真实的输出/结果/状态/价值。
- 不确定性的量化：为结果集合中的各种可能结果赋上相应的概率。
- 风险：不确定性的一种状态。
- 风险的量化：可能性的一个集合，每种可能性都有相应的发生概率和损失量。
- 量化倒置，一个被量化的事物的经济价值，和它所受到的关注常常成反比。在相当多的领域，被量化事物的重要性根本比不上被忽视的事物的重要性。比如：一场销售培训，典型的关注是培训的出勤率，而经济意义更大的是培训效果所需有的价值；一个新项目，典型的关注是项目的短期成本，而经济意义更大的是项目的长期收益。
    - 为什么会发生量化倒置？1. 人们一般会量化他们以为容易量化或知道如何量化的事物；2. 管理者更愿意量化那些更有可能提供好消息的事物；3. 不知道量化中所获信息的商业价值。



## 碎碎念

* 项目中还没有正式使用 uv，日常偶尔跑个工具直接用 `uvx` 可真是方便啊。
* dating 博主是一条拥挤的赛道
* > 人一定要结婚吗?结婚是社会的规训吗?恋爱和婚姻的关系是什么?恋爱是利他的不理性的吗?婚姻是私有制下提高抗风险能力的利益契约吗?恋爱是否是一种性价比很低的行为……
* 有时候真的搞不懂同事纠结的角度和粒度。
* LLM 会把低代码平台干掉么？Retool ？Webflow ？还是说已经干掉了？
* 和同事聊 DRI 这个职位的职责，同事觉得需求细节上的变动不需要和 DRI 沟通。我理解只要有需求上的变动，就需要与 DRI 沟通。
* 感觉 GitHub Action 的一等公民是 TypeScript，看了几个 Setup Action，都是 TS 写的
* 苦闷的一天，下班朋友说在外面玩带了礼物给我，有些温暖。
* 如何锻炼自己的表达能力？
* > Meta has been on a years-long undertaking to translate our entire Android codebase from Java to Kotlin.
* 酒糖居然是哈尔滨特产么，之前一直不知道。
* 完整的读了 Github Actions 的文档，大概扫了扫一些 Setup Action 的实现，看了看 Act 的实现，然后发现 Gitea Actions 之所以能兼容 Github Actions，是因为 Gitea 是基于 Act 实现的，Fork 了 Act 将其作为一个 library，然后实现 Action Runner 来包一层。
* VSCode 中 Command +J ，可以快速打开 terminal。
* > 在所有文化中，对地狱的描述都是重复。
* 有时候想着今天要不要加 5kg 试试，感觉 5kg 没多重，现实是练 1 个月也不一定能加 5kg。
