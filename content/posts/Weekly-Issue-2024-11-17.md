---
title: Weekly Issue-《茁壮》
date: 2024-11-17
tags:
- Weekly
description:  
---


## 文章

### 技术

[Supermaven joins Cursor](https://supermaven.com/blog/cursor-announcement)

> That meant we needed to build our own editor, because the extension APIs in VS Code and JetBrains IDEs were too restrictive to build the interface we wanted.

[[Supermaven]] 加入了 [[Cursor]]，前者的补全速度是我用过所有代码补全里面最快的。

---

[Pyroscope Go Playground](https://playground.flamegraph.com/playground)

自带 flame graph 的 golang playground，感觉可以平替掉官方的了。速度上有点慢？

---

[House rules in Fortnite](https://world.hey.com/dhh/house-rules-in-fortnite-16e0e5e8)

> All screen time is not created equal.

DHH 和孩子们一起玩堡垒之夜，制定了两个规则：呆在一起，不要抱怨。里面提到和常见的合家欢游戏比如《马里奥赛车》，《任天堂明显大乱斗》明显区别是，前者是合作类游戏，所有人在统一阵营，而后者是互相对抗。

---

[When is read-only not read-only?](https://raesene.github.io/blog/2024/11/11/When-Is-Read-Only-Not-Read-Only/)

> However due to the details of how Websockets works with Kubernetes, this access *can* allow for users to run `kubectl exec` commands in pods and get command execution rights in that namespace! There’s information on the origins of this in [this Github issue](https://github.com/kubernetes/kubernetes/issues/78741) but it’s essentially down to how websockets works.

> What’s possibly more interesting is that, while this behaviour has been in place for a while you might not have noticed it, as the default in Kubernetes was to use [SPDY](https://en.wikipedia.org/wiki/SPDY) for `exec` commands instead of websockets, until Kubernetes version 1.31. So if a user with `GET` rights on `pods/exec` tried to use `kubectl exec` in 1.29 you’d get an error like this

[[kubernetes]] 在 1.31 版本从 SPDY 切换到 Websockets 之后，会导致有 get API 权限的用户可以执行 `exec` 。

---

[x.com](https://x.com/kiru_io/status/1856296527049711945)

`Qt` 的发音是 `cute`，`JWT` 的发音是 `jot`。

---


[MomBoard: E-ink display for a parent with amnesia](https://jan.miksovsky.com/posts/2024/11-12-momboard)

用技术来解决生活中的需求，提升生活质量，让人感觉生活美好的文章，虽然文章中没有过多的提到作者母亲的情况，但是可以想象其中的艰辛。

---

[🦋 Cloud Native is on Bluesky! · Bret Fisher](https://www.bretfisher.com/cloud-native-is-hot-on-bluesky-cndo-68-2/)

最近 Twitter 上面的很多开发者已经转到了 Bluesky，但是我还不清楚 Bluesky 和 Mastodon 在实现协议上有什么区别，如果只是去中心化，为什么他们之前不转到 Mastodon 呢？这是否只是一种跟风？以及，Bluesky 的盈利模式是什么？没有广告的状态可以持续多久？

Bluesky 的 starter-pack 确实很好用，可以用来快速关注某个列表中的所有人。[bluesky-migrate.com](https://www.bluesky-migrate.com/) 这个迁移指南也很有针对性，可以直接使用 Sky Follower Bridge 自动搜索当前关注的 Twitter 用户有多少 Bluesky 用户，可以一键关注，体验还不错。

---

[Maybe Bluesky has “won” | anderegg.ca](https://anderegg.ca/2024/11/15/maybe-bluesky-has-won)

很理性的分析了 Bluesky 的现状，简单理解它可能是一个社交媒体版本的 RSS 抓取器，你可以提供 RSS，但是如果你想互动，一定要统一通过 Bluesky 作为入口。

同时提到了 Bluesky 的收费模式，目前是卖域名。

---





### 生活

[[霸王茶姬]]中的咖啡因含量真的高么？

2024 年 11 月 12 日官方小程序显式，一杯伯牙绝弦中咖啡因行量是 103.9 毫克，与之对比的：  
- 奥地利红牛（蓝罐）每罐含量是 40 毫克 
- 天丝红牛（黄罐）每罐 15 毫克 
- 罐装星冰乐摩卡每罐是 60 毫克 

---

[2024.10 长穿毕光雾山极致秋色之旅](https://sides-hang-nca.craft.me/zEWy8lq5XINXhG?anonymousName=yiran&c=7C6634AE-A6D8-4F7D-84D7-9C37E4A2ECA1&replyToEmail=zdyxry%40gmail.com&type=external_comment)

博文同学的长穿毕游记，这是一趟徒步旅行，相比于之前的游记，这篇的故事线很清晰传统，在豆瓣上估计要不及格的水平。

---

[在东京七年，对日本“袪魅”](https://mp.weixin.qq.com/s/AlP7Hd5eTizVy-xLcOI_sA)

> 在外国人的眼中，日本是一个无比严谨和规整、大家都很守规矩的国家，而这种规整一般都被当作优点。但正如上面两个例子，日本社会里也有很多混乱、失序、不合常理的地方，这是它作为一个民主国家的特点。

> 比如“儿童”的读音是“Kodomo”，“Kodomo”就有三四种写法（子ども、こども、子供……）。我曾见到报纸分析这些写法，在什么场景下应该用哪种，什么场景下第一个字应该写成“子”，后面两个字用平假名，什么情况下应该三个都用平假名。在日文里人们经常会琢磨这种事。

---



## 书影

《茁壮》，嘻哈的单口喜剧专场。嘻哈是四川人，非常符合我刻板印象中的四川女生，直爽，豪气。专场讲述的是嘻哈成长过程中经历的一些故事，这些故事都有一个主体，当你受到不公平待遇的时候，你会怎么做。嘻哈的善良以及行动力，是大部分人没有的，同时嘻哈的爸爸也是一位妙人（不知道多少单口演员靠自己爸爸妈妈”养着“），很多的教育观点现在看是很正常的，但如果 20年前能听到，那会很幸福。在演出结束之后，我脑子里想到的一个演员是夏夏，北京单立人的单口演员，是陕西人，因为她俩在演出过程中表现的那种愤怒，是一致的，只是夏夏的愤怒带来的更多是不解，去内化，而嘻哈的愤怒带来的是行动，这点真是少见。

现在豆瓣上有很多单口喜剧专场的评分，都有一些虚高，看看就好，与其看评分，不如看自己喜欢演员的评价来的靠谱。


## 碎碎念

* 试用了下 Dae ，挺好用的，快速配置比较方便。
* 傻逼的共识也是共识
* 现在对于观察性研究的报告信息信任度极低，只信任随机对照实验的报告。
* 一个国外服务商提供的服务，如果其他人都说好用，但是你体验糟糕的话，有大概率是你的网络出现了问题。
* 如果 Bluesky API 好用的话，可以把它当做 Infra 么，好像有一些基于 AT 的应用了？
* 律师有立场么？律师有立场，只是立场比较灵活。