---
title: Weekly Issue-疲惫
date: 2025-03-02
tags:
- Weekly
description:  
---


## 文章

### 技术


[What do I mean by some software devs are "ngmi"?](https://ghuntley.com/ngmi/)

> N period on from now, software engineers **who haven't adopted or started** exploring software assistants, are frankly **not gonna make it**. Engineering organizations right now are split between employees who have had that "oh fuck" moment, are leaning into software assistants and those who have not.

> I suspect there's not going to be mass-layoffs for software developers at Companies due to AI, instead there what we will see is a natural attrition between those who invest in themselves right now and those who do not.

---

[Docker Hub から GitHub Packages へ移行した](https://voluntas.ghost.io/migrating-from-docker-hub-to-github-packages/)

時雨堂的创始人因为 Dockerhub 价格翻倍，停止使用 Dockerhub，转而使用 `ghcr.io` 了。

---
[为 Proxmox VE 定制 Debian Cloud 系统镜像与创建虚拟机模板](https://blog.skk.moe/post/proxmox-ve-customize-debian-cloud-image/)

> 其中，普通云环境的镜像又分为 generic 和 genericcloud 两个变种，generic 相比 genericcloud 额外增加了一些驱动以便部署至裸金属物理机上；而 genericcloud 只包含 VirtIO 等虚拟机需要的驱动，因此 genericcloud 镜像相比 generic 镜像体积更小。genericcloud 镜像的体积普遍小于 350 MiB，不到 Debian ISO 官方安装镜像体积的十分之一。  

给 [[Proxmox]] 制作 [[Debian]] Cloud Image，使用 `libguestfs-tools`。

---


[Deno shows us there's a better way](https://www.macchaffee.com/blog/2025/deno/)

作者将一个服务从 [[Django]] 换到了 [[Deno]]，带来的主要体验改进是 DevEx 相关的。这里如此顺利的另一个原因可能是 Deno 和自身的 Cloud 相关服务配合很好？

---





### 生活

[It is no longer safe to move our governments and societies to US clouds - Bert Hubert's writings](https://berthub.eu/articles/posts/you-can-no-longer-base-your-government-and-society-on-us-clouds/)

 作者希望欧洲政府不要讲数据迁移到美国的公有云服务上。有趣的文章，现在每当和周围人讨论云上贵州之类的新闻，我都会拿欧洲来举例。

---

[Amazon Now Openly Discloses You’re Buying a License to View Kindle eBooks](https://blog.the-ebook-reader.com/2025/02/22/amazon-now-openly-discloses-youre-buying-a-license-to-view-kindle-ebooks/)

[[Amazon]] 也开始了，购买电子书购买的是查看该内容的许可，而不是拥有该内容。

---

[回推特网友问题, 如何做到技术和商业两手抓的， 并没有陷入纯技术的泥潭](https://manateelazycat.github.io/2025/03/02/replay-twitter/)

> 很多技术人懂得原理以后就觉得自己了不起， 然后把 90% 的精力浪费在和别人争高低的内耗中， 而世界上最赚钱的事情恰恰不是技术最尖端的事情

---

[从心所欲](https://mp.weixin.qq.com/s/zqu_onw2bFu5rpTUh04S3w)

> 我的老天爷，做人不需要尊重自己的感受的吗？做人必须努力满足等式得到结果吗？如果尊重自己的感受，那就会尊重自己的需求。尊重自己的需求，你看世界的时候全都是方法，都是平替。如果只是想满足等式的要求，眼睛盯着结果，那么整个世界里全都是困难，都是障碍。
> 如果心不得自在，身怎么可能得自在呢？

---


## 书影

《善意的竞争》，有一种要烂尾的感觉。

悟饭单口主打秀，最初看悟饭是在北京单立人，可能是 2018/2019 年，很喜欢他的表演，但是后面去了笑果之后就不怎么演出了，之前专场《嘛呢》巡演过一次，没有缘分没看上。他之前上传过一段老赖的视频，我时不时的就会翻出来看一次，文本结构、语言节奏、表演，都很好笑： [单立人脱口秀—悟饭：2019年，我成了老赖](https://www.youtube.com/watch?v=iixenNsM-tE)。这个主打秀不知道是为了赚快钱还是怎样，感觉老段子的比例太高了，不太喜欢，可能内容和专场《嘛呢》没什么差别？

这次演出发现，看单口演出，俱乐部本身也很重要，主持人能够控得住场（联想到佳佳在播客里说，这个行业一个还不错的主持人太少了），还是应该选一些知名的俱乐部去看。比如之前去无锡看演出全场都是地域梗；去常州看演出全场都是内部梗。这次演出是在上海高笑喜剧，场子很小，观众很跳脱，主持人尽力了，但是也控不住场，导致后面整场演出都有些尴尬，体验不好。


## 碎碎念

* 偶尔用一下同事的键盘，发现茶轴已经让我觉得很硬了，需要我能够感知的“用力”，还是静电容好。
* crane copy 真好用，mirror image 的利器。
* 得持续提升自己的业务水平啊，聊天都聊不到一块去。
* 今日踩坑，OpenAPI 如果 integer 的format 不是 int64 的话，默认生成的 Golang SDK 是 int32
* 还是给 Racknerd 续费了，前年黑五买的，用这没啥问题，不折腾了。
* 2 月的最后一天发生了以下对话：
    * 老板：xxx 怎么样了？
    * 我：还在搞，还有很多问题
    * 老板：那我之前说的月底提供可用版本，现在应该提供不了了吧？
    * 我：em... 今天是 28 号吧，月底是今天吧？ 提供不了。
* 权志龙的新歌，有一句中文“你总是问我，爱你爱得有多深”，我以为我听错了。
