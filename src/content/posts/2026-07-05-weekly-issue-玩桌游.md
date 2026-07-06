---
title: Weekly Issue-玩桌游
date: "2026-07-05:00:00.000Z"
slug: "Weekly-Issue-boardgame"
tags:
  - Weekly
description:
---

## 文章

### 技术


[Minimus Community Edition: Free Hardened Container Images - Minimus](https://www.minimus.io/post/introducing-minimus-community-edition-free-hardened-container-images-across-our-entire-gallery)

[[Minimus]] 提供了社区版本的安全加固镜像，可以免费试用，这些镜像是通过了一些合规验证的。但是感觉也很难去和 [[chainguard.dev]]、[[Docker DHI]] 竞争，容器安全市场本身一直在高速增长，除了供应链问题外，还有合规法规的要求，导致客户需要应对场景需要投入，但是很多用户免费额度就足够了，不会去付费使用的。另外 [[Minimus]] 核心工具没有开源，那么它和 [[docker]] 就没有差异了，大家肯定可使用 [[Docker DHI]]。

[Chainguard SWOT Analysis & Strategic Plan 2025-Q4](https://www.swotanalysis.com/chainguard)

顺便看了下为什么 [[chainguard.dev]] 需要那么多人，原来是销售占了大头，它们的主要工具都是开源的，受到技术人员认可，但是很难（感觉几乎不可能）转换成明确收益，所以招聘了大量的销售，来将技术卖点转换为合法合规，改为由上至下来推动技术采用。

---

[AI panic](https://xargin.com/ai-panic/)

> 但短时间内，我是悲观的，从历史上看生产力极度过剩的时代基本都是战争的开端。

---

[抢跑时代，你无法靠“安全”赢 - Stay Out Space](https://www.wuyi.space/2026/05/01/%E6%8A%A2%E8%B7%91%E6%97%B6%E4%BB%A3%EF%BC%8C%E4%BD%A0%E6%97%A0%E6%B3%95%E9%9D%A0%E5%AE%89%E5%85%A8%E8%B5%A2/)

> 但在今天的 AI 与智能体应用市场，情况正在发生微妙的变化：我们甚至还没看清鸿沟有多宽，所有人就已经开始冲刺了。

> 于是我们看到：产品还在内测，发布会已经开完了；技术方案还在验证，白皮书已经发出去了；甚至连 Demo 都还没稳定，就已经在说“赋能千行百业”了。鸿沟还没有看清，所有人都在抢那个身位，产品力似乎可以一边跑一边修。

> 维特根斯坦说，语言的界限就是世界的界限。放在 AI 产品营销的语境里，这句话可以翻译成：你能说清什么，你的产品边界就在哪里。你只能赢得你能够清晰表达的市场。

> 问题是，技术狂热者比任何用户都更敏感。Ta 们听得见话术，也辨得出虚实。那些被过度透支的表达，终将在 Ta 们面前失效。于是悖论出现了：抢跑是必要的，但说假话跑不远；说真话又可能显得不够“性感”。


---
[The State of Immutable Linux](https://justingarrison.com/blog/state-of-immutable-linux/)

> Ostree updates in the past were files based. You only had to download the files you needed to perform the update. This is simaly to Flatcar’s block level updates, but could be more efficient because it would download the contents of the block (a.k.a. a file), not the whole block.  

> Moving to containers loses this benefit because now all files are obscured into layers and layers are based on build steps, not contents. So now I can download container layer diffs, but those are much larger and opaque to what I actually need.

虽然作者觉得 [[ostree]] 像 container image 方式的转移，但是我还是很喜欢的，至少用户从使用方便的角度考虑，上手门槛降低很多。
关于提到 OCI 镜像分层不感知 content 引入的分发效率的问题，这个项目是可以解决 一部分的： [GitHub - coreos/chunkah: An OCI building tool for content-based layers · GitHub](https://github.com/coreos/chunkah) ， 在 OCI Image 的构建阶段，将 layer 按照 content 重新组织，计算 RPM 的 stability ，然后根据 stability 进行分层，用构建阶段的耗时来替代分发阶段的耗时。

---




### 生活


[我女儿的感情生活](https://archive.is/CCHgu#selection-1417.0-1422.0)

> 揣着明白装糊涂，从大象边上挪过去。

> 恋爱烦恼也可以跟我聊啊！我是开明的亲爹！没有用，孩子的感情生活，天生就是背着父母的，带着叛逆的意味，是她自我成长的一部分。

> 实践证明，给小朋友讲人生经验没啥用，你觉得特别重要的事儿，她不觉得，有时候还有反效果，因为你小心翼翼的哄着她把天雷滚滚的坑都让开了，所以她觉得风轻云淡都没啥。

> 小朋友交朋友，说好听点是缘分，说直白点是一种布朗运动。大家碰到一起，就混在一起做些朋友做的事情，过两天布朗运动分开了，就跟别的朋友一起做一些朋友做的事情。朋友如此，恋爱亦然，恋爱是为了混在一起做一些恋人做的事情，至于对象是谁，无非是看脸，或者偶然觉得这人还不错，基本没做过理性选择。成年人才他妈量化择偶呢。

> 娃很不开心，娃跟我说，吉他少女为啥要单飞，不是说好做一辈子的好朋友吗？笑死。我跟她说，将来你男朋友讲类似的话，也是一样的，听听就好。

> 虽然我女儿是个吊儿郎当、懒散成性、催三遍才动一动、经常乐极生悲的波西米亚精神病，但她也是一个正直善良有责任感的孩子，我很满意。

> 纪伯伦说过，你的孩子，她不是你的孩子，她是由生命本身的渴望而诞生的孩子（但她还吃你的喝你的拿出不及格试卷让你签字想方设法的找你要钱），我只能陪她很短的一段路，后面更漫长的路，是她自己的路。

> 豆瓣有人说过，生活就像开盲盒，读书、工作、创业、结婚、生娃，我们并不知道什么东西在未来等着我们，只能一个接一个的开下去，人生不过是在泡泡马特的一个下午，转眼日已西沉，满地纸屑，时间到了，你该回家了，你低下头，看到手里只有一些丑陋的廉价塑料娃娃。卧槽花了这么多钱就只得到这些垃圾吗？你握紧了这些垃圾，它们是你最宝贵的东西，因你而赋予了意义。

> 从那一天起，我的想法很简单，就是努力让她跟我一起度过的每一天，都高高兴兴的。

边看边笑，全程姨父笑，这父亲的内心戏非常足，对女儿的教导也很好，值得学习。

---

[Doing nothing at work](https://www.seangoedecke.com/doing-nothing-at-work/)

> As a general rule, if you can simply avoid panicking, you will be doing better than most engineers at incident response.

这篇文章的理念在不同的阶段的人看感觉会有明显的分歧，如果你所在的环境是一个大而不倒的环境，那可能参照作者的方式会让你的精神状态更好，反之，“让公司感觉到痛”这种倒逼方式，最开始受伤的大概率是自己；那些已经存在的“无人愿意触碰”的问题，一定是也会让你糟心的问题，你去解决它，之后自己工作的也会更舒心。

单纯的从负荷管理和优先级分配上考虑，不留 buffer 人会坏的。

---

### 书影播客


[걸어서 상해 속으로..2탄｜여자 혼자 4박 5일｜우캉맨션 길거리 스냅｜도합 8번의 배달음식](https://www.youtube.com/watch?v=Zz7Np0JG7S0&t=3s)  
[걸어서 상해 속으로..｜여자 혼자 4박 5일｜우전 통안 인｜콘래드 상하이｜의문의 헤드 스파](https://www.youtube.com/watch?v=pvZrDljPPsA&t=94s)

推荐一个韩国人的上海游 vlog，全程没有配音，全靠字幕，但是很有趣，和其他韩国人来上海去的地方有很大的差异，比如她会去徐家汇书院。

---

[Ep201 奥克兰生存手册：老想嫁给毛利人了（ You show 还钱！）](https://www.douban.com/podcast_episode/478213)

《基本无害》的奥克兰篇。一些小记录：
- kiwi 在不同的语境下的含义不同：奇异果、新西兰人、鸟；
- 小偷小摸很多，不要在车里放任何东西；
- 有不止一个人被抢过车，离车的时候要及时锁车门，当地人都会买保险，要及时 review 车辆价值；
- 日常光脚走路（和澳洲一样）；
- 新西兰人略微的鄙视澳洲人；
- 其他地区的人略微的鄙视奥克兰人，有专有名词 JAFA："Just Another Fucking Aucklander"，类似于“京爷”/“沪爷”？


## 碎碎念

* 自从注册了两个驾校软件，每天就会收到各种问候。
* 发现因为 Bluefin 关注的一个开发者，是 《Go In Action》的共同作者。
* pidgin，洋泾浜。
* Amp 说自己现在没有 PR，只是 push main，自己解决冲突，然后 push。
* UPS 用上一次，就觉得赚了。
* 这几天关于微信使用 sqlite 的讨论，突然想到，如果陈皓还在，会说什么。
* 看到了 Loop 的定价（每个人最多 10 个 Agent，500块/人/月），Loop 的营销方式看上去和飞书的“先进公司用飞书”一个路数：我们公司还不错吧，我们用 Loop 已经做了 blabla，你想不想用 Loop 来完成类似的事情？那快来试用吧。
* 好像从 2026 年开始，越来越多用户对服务器资源变得敏感了，以前会说我不差计算/存储资源，只要你性能好就 ok。现在会说，你这个怎么占了这么多资源？
* 看到 Laisky 给妻子修眼睛，想到了上次回家的时候，眼镜片不小心摔出来了，家里没有小螺丝刀，我爸妈说姥爷家可能有，大晚上的去姥爷家修眼镜，到了一问，果然有。想到了小时候在姥爷家倒腾那些“破”工具箱，姥爷家啥都有。
* 以为 Nginx 发布时间很早，没想到梦幻西游更早。
* 偷懒了一两天，账就对不齐了
* 单立人上海拼盘巡演票卖不动了，梁海源专场票打4折也卖不动了，再这么大剧场搞下去，能带票的最终都会带不动的。
* 周末被朋友带着玩桌游：掼蛋、德扑、自然和弦、爆珠发明，后两个没玩明白，需要多玩几局。
