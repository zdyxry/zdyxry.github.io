---
title: Weekly Issue 2023-12-10
date: 2023-12-10
tags:
- Weekly
description:  
---


## 文章

### 技术


[A Spooky Performance Regression in AWS EBS Volumes | DoltHub Blog](https://www.dolthub.com/blog/2023-11-22-spooky-performance-regression-aws-ebs/)

我不理解，为什么不直接运行 fio 之类的来直接验证下 EBS 的性能呢？

---

[How to (and how not to) design REST APIs · stickfigure/blog Wiki · GitHub](https://github.com/stickfigure/blog/wiki/How-to-(and-how-not-to)-design-REST-APIs)

关于 REST API 设计的一些想法：
- 使用复数名词
- 不要添加不必要的 path segments
- 不要讲数组作为 response 结构
- 不要反馈映射结构（dict 动态 key）
- 使用字符串作为标识符
- 给标识符增加前缀，可以快速分辨不同类型的标识符
- 不适用 404 来表示 not found
- 保持一致，各个资源/字段的命名
- 返回结构化错误
- 提供幂等机制
- 使用 ISO8601 代替时间戳

---

[四层负载均衡漫谈 | 卡瓦邦噶！](https://www.kawabangga.com/posts/5301)

[[负载均衡]] 介绍，包括四层负载均衡的要求是什么，常用技术选型和实现原理。值得多读几次。

---

[从一个 PR 聊聊我为什么喜欢开源👋 😄 🎉 🎄 🦋](https://liruifengv.com/posts/a-starlight-pr/)

>从这次 PR 的经历，一个很简单的功能，学到了很多知识点，所以这也是我为什么喜欢参与到开源中来。一些开源项目的维护者，不管你是小的 PR 还是大的 PR，都会认真的 review 你的代码，并且给你一些建议，我遇到的一些开源项目的维护者，都是非常友好的。所以，如果你想学习一些新的知识，或者想提升自己的编程能力，那么我强烈建议你参与到开源项目中来，这是一个非常好的学习方式。

---

[Mounting git commits as folders with NFS](https://jvns.ca/blog/2023/12/04/mounting-git-commits-as-folders-with-nfs/)

把[[git]] 通过 [[FUSE]] 映射为 [[NFS]] ，这样可以把所有的 commit 都当做folder，可以在对应的folder 下直接看到对应 commit 的所有改动。使用场景是：

- 搜索已经被删除的函数，可以直接用grep 来查找所有 commit
- 快速查看另一个分支上的文件并复制
- 在所有分支上搜索一个函数

项目代码：[Fetching Title#1ism](https://github.com/jvns/git-commit-folders)

---

[一个来自保留IP地址的连接 - zu1k](https://zu1k.com/posts/events/why-reveice-connection-from-class-e-ip/)

这个问题我和同事也想了很久，震惊于评论的实现方式，果然大家都是能人啊。

---


[生成式 AI 是如何工作的](https://step-saga-examples.pages.dev/simple-ai-01-cn/)

同事学习整理的，图文并茂。

- 理解词语：对词语在不同维度进行分类打分，维度可能有上千个，相似的词语在更多维度上会有更相近的分数。
- 理解句子：理解包含了一组词语的句子时，除了理解词语本身，还应该将每个词语和句子中的其他词语相结合进行第二轮理解。单个词语和句子中其他词语之间的关联性，称之为“注意力”，由于是和同一个句子自身的词语结合理解，所以称之为“自注意力”。
- 生成内容：将所有词语的量化结果和自注意力结合，得到一组新的量化结果（虚线下方）作为它对整个句子的总体理解。当进行生成时，AI 模型会从自己的词汇表中对比各个词语和当前句子的关联性。
	- 幻觉：
		- AI 模型在继续生成的过程中，实际是在挑选**可能性最高**的词语，那么这一挑选过程仍然可能存在误判。
		- 实际上，许多 AI 模型都会努力克服幻觉，让 AI 模型对虚构的内容、不安全的内容加以针对性的学习，让这些内容对应的词语产生极高的注意力，从而在生成内容时可以挑选到一些专门用于防范的词语作为结果。
		- 一种让 AI 模型重获创造力的方式是通过输入一些特定的词语，吸引 AI 模型的注意力，引导其产生新的内容。这种引导 AI 模型注意力的方法也被称为提示词工程（prompt engineering）。

---

[AI 版“神笔马良”是如何工作的](https://step-saga-examples.pages.dev/simple-ai-02-cn/)

- 如何理解图片：根据图片标注信息，将图片切分并提取特征，将特征与标注信息进行关联。
	- CLIP，将一张图片和一段文本对应，分别提取各自的量化结果，进行关联。通过 CLIP 可以快速的判断图片与文本的关系，但是无法基于现有信息进行信息生成
		- CLIP 使用社交媒体的图文作为素材
	- Flamingo，将词语和图片分别交给两个模型处理，得到词语/图片自身的量化结果和自注意力产物。如何使用这些产物？
		- 知道输入（量化结果），知道输出（预期生成内容），找规律，通常是线性关系。
>可以看出，尽管 AI 模型不断演进，但现阶段创意和工程仍然是重要的组成部分。AI 模型与工程结合，更高效地解决特定场景的问题还有很多探索空间。

---

[Goodbye, Clean Code — overreacted](https://overreacted.io/goodbye-clean-code/)

过于追求 Clean Code 可能会带来一些问题，比如可能带来更多理解抽象的成本，在后续迭代中并没有很好的降低复杂度。里面提到了一点之前没有在意的观点：在重构团队中他人的代码之前，最后和他们进行沟通，而不是直接提交代码，可能会对团队合作产生影响。

---

[比特币分叉往事补遗](https://blog.yishi.io/p/btc-fork-retrospective)
故事很精彩，从文章讲述的上下文，对[[币信]] 的动机有些怀疑，真的有人为了信仰而承受着那么大的亏损么？

---



### 生活

[Elon Musk Twitter](https://twitter.com/elonmusk/status/1731369367340732734)

>Life is kind of like a party.You invite a lot of people, some leaveearly, some stay all night, some laughwith you, some laugh at you, and someshow up really late. But in the end, afterthe fun, there are a few who stay to helpyou clean up the mess. And most of thetime, they aren't even the ones who madethe mess. These people are your true friendsin life. They are the only ones who matter

---

[一些鬼故事](https://xargin.com/ghost-story/)

>这个世界，有些事情明明大多数人做不到，但是你做到了，他就会觉得很简单。所以那些坚持者往往还不如那些投机者赚得多。反过头来还要被弱鸡评头论足。  
>现在很多纯技术人员也被乱七八糟的价值观污染，连基本的就事论事都做不到，拿着给一线销售洗脑的价值观大做文章，多么可笑，一起开复盘会的时候大片的时间在强调价值观，心诚了系统就稳了？  
>我们可以做很多事情来预防事故的发生，但即使做了，也没有用，因为一个商业机构，**不可能对没有在自己身上发生过的事情提起重视。**  
>盛极必衰在互联网公司同样适用，公司做大了，大多数既得利益群体都丧失了学习动力。在某公司曾经见过 x9 的业务规划给 x8 做，x8 再给 x7 做，最后变成了高级工程师在给整个公司做战略规划的奇观。  
>再说明白一点，可能监控系统自己的监控需求，还不如业务的监控做的好。也是找个实习生糊弄一下了事。  
>作为一个过来人，我的建议也只有两条：  
	- 无论什么时候，都选择给你钱最多的地方；  
	- 先有钱，再去谈理想和长期主义；  
	- 软件架构里有个概念叫 Leave Options Open，你的职业和人生选择也应如此；  

---

[为什么东北人一听就是东北人？ - 知乎](https://www.zhihu.com/question/622987208/answer/3307897003)
>从语言学上讲，汉语的发音除了我们正常说的阴平（读高平调，符号是“ˉ”）、阳平（读高升调，符号是“ˊ”）、上声（读先降后升的曲折调，符号是“˘”）、去声（读降调，符号是“ˋ”）四声外，还有控制发音高低的五度调值，这玩意你可以当作是五线谱的do re mi fa so，标作12345，数字越大调越高。
>普通话的调值是55度，或45度，主打一个高，说句子时是为了突出结尾的高调，往往采用214、215的调值，先抑后扬，音调差距明显。
>而东北话则是44度或33度，相较普通话音调更低，说句子时采用213的调值，虽然也是先低再高，但相比普通话，存在明显的压声。
>更有特点的是东北话古入声多派上声，就是东北话里喜欢把很多阳平（ˊ）读成上声（˘），典型的就是“国家”东北话好读成“果家”、“皮革”读成“皮葛”。

我记得之前看过一个人的视频，讲国内的各个地区方言的发音方式不同，那个 UP 可以说很多方言，总结的很好，但是找不到了。（之后看到有意思的还是要记下来

---

[Linears - Websites inspired by Linear](https://www.linears.art/)
>Linear 以其深色风格配上外发光、渐变模糊的风格独树一帜，这个网站收集了一些类似 Linear 风格的网站。

审美疲劳，现在如果有某个官方不是这种风格的，我都会都看几眼。

---

[建造你的小森林 | 小信号](https://xiaoxinhao.top/article/xiaosenlin)
[关注和囤积的小思考 | 小信号](https://xiaoxinhao.top/article/tunjizheng)
在日常信息获取之后，需要定期的进行回顾整理，来尽量的精简自己所需要的东西。一味的收集是没有用的，当你收集了很多，下次遇到的时候，还是需要从一堆内容中找到自己想要的，这个搜索过程也会比较痛苦。

---

[冷知识：虹桥高铁站正确的打开方式。 - Xiaowen.Z Deployed](https://xiaowenz.com/blog/2023/12/hongqiao-railway-station/)

>如果你的检票口是小号（小于等于 15），则选择提前一站下地铁，从机场走过去，整体体感最优 如果你的检票口是大号（大于等于 15），则可以选择终点站下车，在耗时大概相同的情况下，步行距离最小。

这个方法一直知道，小红书上看到过，身边同事也分享过，但一直没尝试过。

---



## 书影

《万能钥匙》，细思恐极的电影，但是如果看过《逃出夺命镇》，那可能就会被提前剧透了。

