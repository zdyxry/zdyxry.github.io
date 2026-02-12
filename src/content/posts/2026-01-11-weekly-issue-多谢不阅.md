---
title: Weekly Issue-《多谢不阅》
date: "2026-01-11T00:00:00.000Z"
slug: "Weekly-Issue-多谢不阅"
tags:
  - Weekly
description:
---

## 文章

### 技术
[Go 1.26 interactive tour](https://antonz.org/go-1-26/)

[[Golang]] 1.26 是一个很大的版本迭代，性能、开发体验都有改进，感觉值得升级。

---
[Why I don’t like “Correction of Error” – Surfing Complexity](https://surfingcomplexity.blog/2025/12/20/why-i-dont-like-correction-of-error/)

> Remember, errors happen every single day, but incidents don’t. _Correction of error_ evokes the idea that incidents are caused by errors. But until you internalize that errors aren’t enough to explain incidents, you won’t understand [how incidents actually happen in complex systems](https://www.adaptivecapacitylabs.com/HowComplexSystemsFail.pdf). And that lack of understanding will limit how much you can genuinely improve the reliability of your system.

系统正常运行只是系统诸多故障时刻的特例。

---
[It’s hard to justify Tahoe icons @ tonsky.me](https://tonsky.me/blog/tahoe-icons/)

好文章，苹果 macOS Tahoe 系统中新增的菜单图标设计进行了解读。从用户角度来说，我其实不是很关注图标的细节：美观、差异化、整体性好，是这是加分项，但不是决定项，我关注的是图标可以帮我养成操作习惯，无论一个软件有多难用，只要它的功能操作是确定性的，一旦养成了操作习惯，那用户也就不会觉得有多么难用了，比如著名的 JIRA。   
当图标无法达成这个目的，我要图标干什么呢？

---


[My HomeLab Setup in 2026 · Danb Blog](https://danb.me/blog/2026-homelab/?ref=selfh.st)

作者的这个小机柜太漂亮了，国产小主机在海外市场的表现也越来越好了。

---

[Code And Let Live · The Fly Blog](https://fly.io/blog/code-and-let-live/)

[[Fly.io]] 推出了新的产品：[Sprites - Stateful sandboxes](https://sprites.dev/)。
这是一篇关于 Agents 和 sandbox 的讨论，看似说了很多，但是我没有理解，这和 EC2/MicroVM 区别是啥呢？可能是基于 Firecracker  的，计费粒度细一点？操作速度快一点？

确实不理解为啥要新造词，这种叙事风格观感不好。

---

[《征服C指针》 | 卡瓦邦噶！](https://www.kawabangga.com/posts/7160)

> 我认为，​“谨慎地” 编码并没有什么了不起的，那些能够尽可能地回避 “麻烦事” 的人才是优秀的程序员。在我心中，理想的程序员是下面这样的：在能够安全地偷懒的地方尽可能地偷懒，并且尽可能地依靠工具而不是肉眼来进行检查，但在无论如何都需要人工处理麻烦的事情时，会在心中坚定地起誓 “总有一天要将它自动化”​。

有印象看到过其他人发过类似的话，出处是这里么。

---



### 生活

[天高地厚之间的行走 -- EBC三垭口+Gokyo+岛峰全记录 - 原创分享(新) - Chiphell - 分享与交流用户体验](https://www.chiphell.com/thread-2769739-1-1.html)

风景是真好，看着也是真累。

---

[2025 投资组合年报](https://blog.joway.io/posts/2025-portfolio-annual-report/)

> 即便我十分擅长反思自己，但我至今也无法分辨自己当时的心态属于哪一种。我也深刻认识到「知行合一」的困难，它远远不是你知道了某件事然后就去做某件事这么简单，而是反过来，你做了某件事，你却不知道自己是因为哪一种「知」而做了这件事。   
> 而人性往往会倾向于帮你选择那一个你最希望的「知」来合理化你的行为，最终真正的「知」就消失在了一堆道不清的妄念之中了。你脑子里所臆想的你自己也会远远和你实际行动塑造的真实自己所背离。

---


### 书影播客

《多谢不阅》，作者: [荷] 杜布拉夫卡・乌格雷西奇。书上的这个“荷“，就挺讽刺的，作者出生于南斯拉夫，后续定居荷兰，但是她一直说自己是一个跨国界的写作者，国内出版要求必须有国籍标识，用了法律上的国籍。这本书是随笔集，很多的随笔写于 199x 年，也就是 30 年前，在 2026 年的现在看，毫不过时（想到了[There Is No New Aesthetics](https://borretti.me/article/there-is-no-new-aesthetics) 文章）。书中有很多讽刺：作家身份比写作本身重要；读者不是为了阅读，而是为了一种社会身份；一本书的重点在于是否有卖点，而不是内容本身；北美人觉得东欧人的作品不受欢迎，西欧人觉得东欧人的作品不受欢迎，东欧人自己觉得自己的作品也不受欢迎。即使说了这么多，作者自己也还是要去参加文学节，也要去接受采访。2025 年出版的《还可以的金女士》作者也在播客中提到，不理解为什么要有签售会，为什么要跑那么多个城市，现实如此。

《疯狂动物城 2》，无论有多少隐喻，都是很好的合家欢电影。



## 碎碎念
* 年度复盘，完全复盘不出个啥东西。
* Github Action Job 访问 Github Release 下载binary，都能 504 的么
* 通常需要“靠手”在编辑的时候理清自己的表达。
* 我有时候会用“正确的废话”来形容一个观点，这好像有碍于针对这个观点的进一步思考。
* 果然，你去看一些自动化项目，最终都会追到operator。。。
* 看到一个operator，reconcile 里面实际动作是创建新的deployment 执行命令来完成 CR状态更新，虽然是邪教，但是debug 起来感觉挺方便。
* 单口演员买了巴黎世家，第一感受是，骑共享单车不方便
* Trae: 北京引力弹弓科技有限公司.
* 走到地铁站，发现自己忘记带跑步衣服，当脑子里一直想着工作的事情时，就一定会对生活产生影响。
* 代码和文档，总要有一个是能运行的，不能两个都不行。。
* Lovable 使用体验确实很好，在提取需求时，会给出几个选项，其中一个问题是“你的目标用户群体是谁“，这个问题让我惊喜。
* 感觉 CEL 很适合在 API 测试领域发光发热啊。 