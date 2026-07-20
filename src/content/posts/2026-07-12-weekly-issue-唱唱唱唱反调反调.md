---
title: Weekly Issue-《唱唱唱唱反调反调》
date: "2026-07-12:00:00.000Z"
slug: "Weekly-Issue-opposite"
tags:
  - Weekly
description:
---

## 文章

### 技术

[当编程变得不再有趣](https://onevcat.com/2026/07/coding-not-funny-anymore/)

> 如果说过去一年，这种乐趣只是被稀释，我好歹还能在编程的副驾位置上混一混，那么 Fable 5 的出现，更像是有人干脆把我的整个驾驶室都端走了。

> 写了二十年代码，“能亲手解决困难的问题”曾经是我确认自己的方式之一。现在这个位置上坐着别人了，而且它不用睡觉，不会烦躁，也不需要成就感，只需要一点电力和两百美金。

---

[GitHub - MaximeRivest/riddle: The diary of Tom Riddle for the reMarkable Paper Pro — write with your pen, the page drinks your ink and answers in a flowing hand · GitHub](https://github.com/MaximeRivest/Riddle)

用 [[AI]] 来做有趣项目的典型示范：将 [[reMarkable]] 设备变成《哈利波特》中汤姆里德尔的日记，用笔在纸上写下自己的话，然后字迹小时，然后对方给出回复，最终所有痕迹消失。这就是魔法啊。

上一个印象很深的博客是这篇： [cannoneyed.com/projects/isometric-nyc](https://cannoneyed.com/projects/isometric-nyc)，将纽约地图转换成像素地图。

---

[I stopped self-hosting these 4 services after realizing maintenance wasn't worth it](https://www.xda-developers.com/stopped-self-hosting-these-services-due-to-maintenance/)

作者停止维护了 4 类 self-hosted 服务：音乐播放、站点管理、邮件、密码管理。我尝试过维护音乐播放，但是每次找资源都有些麻烦，哪怕现在有龙虾自动的找，但 Youtube 的封锁机制一直在持续的更新，总归要投入时间想着这件事。放下执念，放过自己。

---

[Kepler, re-architected: Improved power accuracy and a community call to action!](https://www.cncf.io/blog/2026/06/30/kepler-re-architected-improved-power-accuracy-and-a-community-call-to-action/)

> To prioritize ease of adoption and accuracy improvement, we are shifting away from eBPF and going back to basics. Our re-architected solution leverages read-only access to standard `/proc ` and `/sys`. Because these are universally available on Linux systems, they require significantly lower privileges and minimal setup.

[[Kepler]] 去掉了 [[eBPF]] 的强依赖，改为使用 `/proc` 和 `/sys` 来获取信息，找机会在内部部署一个试试，能量化的东西都是好东西。

---

[Excessive logging causes process to block · Issue #990 · coreos/bugs](https://github.com/coreos/bugs/issues/990#issuecomment-395168773)
[High journald CPU usage · Issue #1162 · coreos/bugs · GitHub](https://github.com/coreos/bugs/issues/1162#issuecomment-194223382)

最近在想是否有可能把一些服务日志从自己管理统一到 journald 管理，毕竟现在 systemd 大一统，系统日志流转已经统一变成了 kmsg, syslog, service unit stdout/stderr, audit 统一接入 journald, journald -> rsyslog -> /var/log 的状态了。  
转到 journald 的优势很明显，可以结构化查询，日志空间自动管理，输入输出统一管理。带来的问题也有一些，有默认的速率限制，比如 30s 最多 10000 条日志，使用 journald 之后所有的日志都统一管理（高版本有 LogNamespace 可以配置独立的 journal），哪怕配置了持久存储，不同服务日志的轮转策略通常是有差异的，还是需要 rsyslog 转发一次，这个时候之前的一次写动作就变成了多次，且写入路径非常的长，需要配合 logrotate，该需要的这些传统配置都少不了。

如果 journald 有 bug，影响范围太大了，我期望的是即使系统日志无了，我的关键服务仍可以运行，当日志文件系统使用率 100% 之后，write 会返回 ENOSPC，看上去 journald 之前有过阻塞 write 动作的 issue，结论：不迁。

---

### 生活

[黑暗投资暴论](https://taresky.com/my-ego)

> 之前说过的金融行业一定需要做合规，因为利润的来源是不合规。这就是真实世界的样子，政治是人类奴役人类的终极手段，建立合规门槛是为了阻碍门槛之外的对手。虽然它们往往被包装成“保护普通人”，也做了一些表面功夫，但这是营销，而不是初衷。

> 市场的全部利润，都来自于有人在不计磨损地交易。这个人可能是股神、天才；可能是庄家、黑客；也可能是散户、韭菜。但无一例外，他们愿意支付交易成本，换取更好的流动性，是一切利润的根源。

> 任何交易都需要有对手方。有人告诉你可以共赢，是因为他先上车了，希望你来抬轿子。

虽然我没啥投资能力，但是这套理论是认同的。

---

[写作指令](https://nofluff.0x01.me/)

> 写下任何比喻或概括性说法之前，你必须能回答两件事，一是能用具体事实或逻辑把它展开，二是它确实比直白说法更帮助理解。任何一条答不上，就换成直白的说法。

一直觉得比喻这个修辞方式很难，尤其是在专业场景下，有一些看似有道理的比喻方式，细想就有问题了，这个时候感觉比喻反而是坏事。关于修辞，之前看到过有人推荐过陈望道先生（《共产党宣言的中文译者》）的 [修辞学发凡 (豆瓣)](https://book.douban.com/subject/1046205/)。

---

[工作不是一种祝福，而是诅咒](https://edward40.com/zh-cn/p/work-is-not-a-blessing-but-a-curse/)

> 也许真正值得相信的不是工作会拯救我们，而是即使工作暂时没有着落，人也未必真的会坠落到底。没必要提前为那些还没出现的事情受苦，因为焦虑未发生的事并不会让未来变得更可控，只会让今天更加恶化。该准备的时候准备，该投简历的时候投简历，该面对的时候面对，但不要把未来每一种可能的不幸都提前搬到今天来承受。

我倾向于认为这里的“并不会”是因为还没有发生，如果发生了，再来回过头看这段话就是另一番场面了。知道现实世界的游戏规则是什么，在规则之内，确保自己可以站得稳，之后再谈其他。

---
[很多少数民族不是还没进化到有文字，而是主动丢弃了文字](https://www.douban.com/topic/493230026/?_spm_id=MTYxMzA4NzA2)

> Scott 提出了一个极其大胆且迷人的假说：山民没有文字，可能不是因为他们笨或者进化落后，而是一种为了保持政治灵活性而进行的战略性拒绝。   
> 他挑战了一个根深蒂固的偏见：即识字/文字代表进步，文盲/口传代表落后。他提出，对于那些想要逃避国家的人来说，文字不仅不是进步，反而是一种致命的行政陷阱。

> 对于逃亡者来说，没有记录就是最好的保护。   
> 文本是僵死的、证据确凿的；而口述是活的、可以随时改写的。在口传社会里，历史、家谱和法律都是根据现在的需要来发明的。文字是国家的栅栏，而口语是自由的荒野。

> 识字固然带来了知识，但文字也带来了锁链。   
> 少数民族通过保持口头文化，获得了一种历史的豁免权——他们可以随时重新定义自己，永远走在国家行政机器的前面。

---
[Maybe you should learn something](https://archive.is/PdGfq#selection-101.0-120.0)

> In the long term, learning new things is fun and makes life richer in ways you can’t even imagine, and it’s a time investment that will pay dividends for life as these skills never really go away. There are even social aspects, as you’ll quite literally become a more interesting person to talk to.

---
[Blog about things you don't understand yet](https://www.seangoedecke.com/blog-about-things-you-dont-understand-yet/)

这篇博客还是有些启发的，我日常会记录我读到的博客的想法，如果读完一篇博客我没有什么想法，那么我不会记录它，如果读完一篇博客之后，我有一些模糊的想法，但是无法形成阶段性的结论，我会搁置它，后面很有可能就一直搁置下去了。

如果按照这篇博客推荐做法，那我应该先预设一个结论（不需要正确，哪怕只是一个角度），比记录下自己所有模糊想法的原因，这样即使搁置了后面回过来也能继续思考，直到最终有一个想法。

---


### 书影播客

《唱唱唱唱反调反调》，二维马单口专场，一个月前买票的时候是 99，知道不带票肯定卖不完，没想到大麦周三打折最低 69，亏了，下次不提前买了。个人风格保持的非常完美，第一个专场《小薯》是讲孩子的，观众的接受度高一些，上一个专场《晚到旅客安检通道》和这个专场，都是围绕着逻辑谬误这个方式来写，先设想一个谬误，然后围绕这个谬误去解释，最后合理化。发现辽宁演员对观众的冒犯成都挺高的，大风天几个演员的冒犯程度排名：好梦>二维马>史研>宁佳宇。这么看，一些观众说宁佳宇拧巴，还是有点说法的。

另外，觉得 Storm 的喜剧联盒国要倒闭了，希望它能多坚持一阵子的，我不想每次看单口都跑到南京东路/北外滩去。


《良渚密码》，南派三叔。我一直分不清南派三叔和天下霸唱，只记得某一年暑假的时候捧着两本全集看完了《鬼吹灯》和《盗墓笔记》，这本书有点让我想到了那个时候。


## 碎碎念

* 一个月前买了这周专场的门票，结果这周我 Oncall。
* 总感觉 wakatime 在 AI 时代可以做更多事情，没跟上热点。感觉当前的各种 token 统计都是侧重于 token 用量，但是时间维度好像不太行。
* WorkBuddy 到底投了多少广告。
* Github Action 定时任务堆积已经从延迟 1h 变成了延迟 4 h 了。
* 苏州河的正式名称还是吴淞江。
* 听播客听到了两种不同的消费方式：a. 如果我今天不买这个东西，我明天会死么？b. 如果我明天死了，我今天还要买这个东西么？其实两者不冲突，可以一起来决定的。
* 同事和女朋友的办公地点，中间只隔着黄浦江，我说在这当牛郎织女呢。
* ping 没啥问题，只靠 ping 就有很大的问题了。
* 大米先生有自选称重的店铺了，感觉比之前划算很多。
