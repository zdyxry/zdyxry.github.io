---
title: Weekly Issue 2023-06-18
date: 2023-06-18
tags:
- Weekly
description: 请3休8。
---


## 文章

### 技术


[我的 ETH 被盗了 - forecho's Blog](https://blog.forecho.com/my-eth-has-been-stolen.html)

私钥直接提交到了 [[github]]，导致 [[ETH]] 被盗。在开发过程中尽量使用环境变量来获取一些敏感信息，有时候写 demo 代码的时候可能图方便就直接 hardcode 了，但可能带来的影响是很容易忽略的。

也有人推荐使用 [[git-secrets]] 在提交代码之前检查是否存在敏感信息。

---


[云SLA是不是安慰剂？](https://mp.weixin.qq.com/s/LC5jAhuVObRcrTLxI1FUQA)

> **然而，SLA 被有意地与服务的真实可靠性相混淆**：**用户不应该将 SLA 视作来服务可用性的可靠预测指标 —— 甚至是过去可用性水平的真实记录**。**对于厂家来说，****SLA 并不是真正的可靠性承诺或历史战绩，而是一种**营销工具****，**旨在让买家相信云厂商可以托管关键业务应用。**  
**所以，SLA 对用户来说不是兜底损失的保险单。在最坏的情况下，它是吃不了兜着走的哑巴亏。在最好的情况下，它才是提供情绪价值的安慰剂。**  

文章中提到的是单个云服务商的 [[SLA]]，现在很多应用都同时在使用很多的 [[PaaS]] 提供的服务，这个时候很难计算自己应用的[[SLA]] 是多少。

---



[How the data center site selection process works at Dropbox - Dropbox](https://dropbox.tech/infrastructure/how-the-data-center-site-selection-process-works-at-dropbox)

[[Dropbox]] 如何选择 [[IDC]]。
- 确认需求：
	- 电源、机柜空间、可上线时间。根据需求联系市场上活跃的供应商。

- 了解供应商能力：
	- 基础设施设计规范，包含电源、冷却、容错能力。
	- 承重能力，需要考虑各个机柜的重量。
	- 网络设计，流量出入，有哪些可选运营商。

- 挖掘细节：
	- UPS 能力。
	- 是否可以按照预期施工。
	- 监控报警是否完备。
- 实际走访
	- 根据线下参观，确认实际细节是否匹配。
	- 为一些关键能力打分：机柜空间、电力、冷却、网络、安全、地域灾害（是否处于洪水和地震区域）、运维支持、后勤。
- 谈判租约
	- 租金：电力成本、空间成本、优惠减免。

---


[I booted Linux 292,612 times | Richard WM Jones](https://rwmj.wordpress.com/2023/06/14/i-booted-linux-292612-times/)

使用 `git bisect` 进行二分测试，定位启动 hang 的问题。

---

[Canonical extends its commercial OpenStack offering to small-scale cloud environments with project Sunbeam | Ubuntu](https://ubuntu.com/blog/canonical-extends-commercial-openstack-offering-to-small-scale-cloud-environments-with-project-sunbeam)

> We use the kubernetes to run the VMs to run the kubernetes.  


---


[Python GIL vs. nogil: Boost I/O Performance 10x With One Line Change](https://www.backblaze.com/blog/python-gil-vs-nogil-boost-i-o-performance-10x-with-one-line-change/)

[[Python]] PEP-703 提出 [NOGIL](https://peps.python.org/pep-0703/) 的版本，在 IO性能上最多有10倍的提升。

现在 [[Python]] 的性能问题和包管理器混乱的问题，如果不是生态比较好，应该也很难再增长了吧。

---

[重新思考"删除"：探索软删除的真正含义](https://zhuanlan.zhihu.com/p/635921542)

现实世界并不会级联删除，不应该把“删除”当做理所当然，在不同的业务逻辑中，“删除”的定义是不同的，应该根据具体的用户和具体的场景，明确真正的意图是什么，以业务为导向，大部分的“删除”对应的是状态的转换。
实操建议  
> 如果你要表达具体的业务语义，请使用具体的业务字段，不要使用 is_deleted 进行偷懒  
如果你要记录数据的变更记录方便回溯，请使用另一张 activity 表进行完整的记录，不要使用 is_deleted 进行偷懒  
如果你要归档数据，就走数据归档流程，不要使用 is_deleted 进行偷懒  
如果你要备份数据，就走数据备份流程，不要使用 is_deleted 进行偷懒  



### 生活

[当代打工人，被迫患上“文字讨好症” - 知乎](https://zhuanlan.zhihu.com/p/633304032)

最近一位新同事非常的喜欢用：~、哈、啊、呀、嘛等语气词，我个人平时为了表示友好，也会使用 “嗯嗯” 这种回复。个人并不是反感这种说法方式，而是这种场景，通常会加着最友好最平和的语气词/ emoji，说着让人最难受的话。

---

[2023-24: 漩涡事件反思录](https://xuanwo.io/reports/2023-24/)

[[开源]] 社区维护思考，从维护者视角和贡献者视角考虑，感觉每个项目都需要一个类似 Project Manager 的角色。

---

[对苹果Vision Pro和空间计算的思考](https://mp.weixin.qq.com/s?__biz=MzIxODI3MjU5NA==&mid=2247483690&idx=1&sn=3e9645c98b2769417ef0f2283bb3fba0&chksm=97ec4717a09bce01ec4589f8921ab19ee9f1a1efaa97e6672f3f50364e0da1796c9ecd5f3b86&scene=126&sessionid=1686538850#rd)

现有的信息呈现方式大部分都是二维的，而[[Vision Pro]] 引入了三维的概念，虽然之前几年的 [[VR]] 已经进行了很多的探索，但是没办法说实质性的成功，文章说是因为交互体验上的缺失，[[Vision Pro]] 从交互体验扔掉了手柄，使用眼睛、收拾和语音的组合。

作为 **大就是好** 的拥趸，还是看好[[Vision Pro]] 的，毕竟这是[[苹果]] 啊。

---

[你最穷的时候是什么时候，是怎么熬过来的？ - 知乎](https://www.zhihu.com/question/46324613/answer/2931107604)

想到了刚毕业的时候，和同学租在百望山附近的韩家川村一个自建房里，房租一个月600块，两人均分一人300，早出晚归，因为房间实在太小，回去也做不了啥，就很早出门很晚回去，回去只是睡一觉。那时候的日子真是有点惨。

---

[像遊客一樣生活 - Just lepture](https://lepture.com/zh/2017/live-better)

心态上的转换太难了，哪怕出去旅行，也不是完全的放松身心。

---

[王国之泪：超越旷野之息的决心，以及方法 | 旗舰评论——战略航空军元帅的旗舰](https://necromanov.wordpress.com/2023/06/14/%e7%8e%8b%e5%9b%bd%e4%b9%8b%e6%b3%aa%ef%bc%9a%e8%b6%85%e8%b6%8a%e6%97%b7%e9%87%8e%e4%b9%8b%e6%81%af%e7%9a%84%e5%86%b3%e5%bf%83%ef%bc%8c%e4%bb%a5%e5%8f%8a%e6%96%b9%e6%b3%95/)

[[塞尔达传说]] 开放世界的构建基础，虽然没有完整的玩过，但是还是看的津津有味。

---

[为什么我们需要一个「关于」页面？ | 今是昨非](https://zuofei.net/5058.html)

当发现一个博客的时候，通常会先看“关于”页面，可以快速了解作者，然后阅读作者的其他文章，根据自己的需要决定是否加入 RSS 订阅中。发现自己的“关于”页面很久没有更新了，需要更新一下。

---

[家庭 Homelab 升级计划 - Manjusaka](https://www.manjusaka.blog/posts/2023/06/16/how-do-I-build-homelab/)

自己也想过折腾一下，但是总担心小垃圾越来越多，最后反而不会把时间投入到想搞的地方。

---

## 书影

《深入理解 Linux 网络》，本周没有继续读。

《她厌男，她是我女友》，同事bowen 推荐的，看完了之后果然符合他的评价：女性主义爽文。现在女性主义书籍的受众应该是很明确的，各大出版社不断地消费这类群体，有点割韭菜的意思。在我看来这本书太取巧了（也看到有评论说是翻译的“功劳”），看似什么都说了，但是又好像什么都没说，只是把这些刻板印象描述出来，除了让女性主义读者爽一爽之外，没有什么用处。  引用豆瓣评论：
>和《82生的金智英》一个毛病，有一种网络热帖整合感，中译者是懂这个理的，娴熟地把一些原文转换成了中文网络里对应的“直男癌”一类热词，“韩男”对应的就是“国男”嘛，原书标题也没有“厌男”这个词亦是此理。因为这类书属于选题意义大过内容，你也不能说这十万加畅销style的东西写得没价值，毕竟也有社会观察的意义嘛，但这部恋爱轻喜剧的性别刻画和探讨，终究还是太粗浅、虚浮了。纸片一样单一的刻板人设且不说，这种女性视角想象出来的典中典男性主角，其实好多地方还是有点太细腻敏锐了233，未免违和(能思考这么细大概率也当不成典中典男性），而且真·激女恐怕根本不会和男主发生任何性缘关系啦。半个多小时翻完好想去韩国写畅销书啊，so easy！

《宋元泉州与印度洋文明》，很薄的一本小册子，作为去泉州游玩的背景知识补充是不错的选择。

《浪漫医生金师傅》，看完了，处于及格线上的韩剧，第二部换了男二和女二，暂时不想看了。

《我们之间没有的》，本周没有继续看。

《黑镜-第六季》，看了第一集，关于用户协议的部分很不错。

《以神之名：信仰的背叛》，讲韩国邪教的，模板化严重，不理解信仰。