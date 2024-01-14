---
title: Weekly Issue 2024-01-14
date: 2024-01-14
tags:
- Weekly
description:  
---


## 文章

### 技术

[Keeping the lights on while leaving the cloud](https://world.hey.com/dhh/keeping-the-lights-on-while-leaving-the-cloud-be7c2d67)

>But programmers are attracted to complexity like moths to a flame. The more convoluted the systems diagram, the greater the intellectual masturbation. Our commitment to resisting that is the key ingredient in this uptime success.
>You don’t need the cloud to get good uptimes. You need mature technologies run on redundant hardware with good backups. Same as it ever was.

明确项目的目标是什么，追求的是什么，用合适的技术去实现，不要追求过多的复杂性。

---

[监控改造之路4](https://capops.xyz/observe4)

[[Grafana]] 如果将配置模板放在对应的路径下，无法通过界面去删除。

又想到了这条感想： [twitter.com/zdyxry/status/1424735517879402496](https://twitter.com/zdyxry/status/1424735517879402496) 

---

[twitter.com/river\_leaves/status/1743231668910010575](https://twitter.com/river_leaves/status/1743231668910010575)

>据我观察，主要是因为，一些技术人员不思进取，获取信息的能力也有限。调研能力不足的情况下，就只能重复发明纸糊的轮子。实际上是一种惰性。

>一个人的信息检索能力决定了职业天花板。

---

[When is admin not admin?, when it's super-admin!](https://raesene.github.io/blog/2024/01/06/when-is-admin-not-admin/)

[[kubernetes]] 1.29 版本修改了 kubeadm 生成的 admin.conf 默认权限，从 `system:masters` 变为了 `cluster-admins` 。

---

[I quit my job to work full time on my open source project](https://ellie.wtf/posts/i-quit-my-job-to-work-full-time-on-my-open-source-project)

[[Atuin]] 作者从 [[PostHog]] 辞职，全职从事 [[Atuin]] 相关工作。[[Atuin]] 官方可以托管Shell 历史，作者觉得在 Github 上收赞助，如果不经常说自己需要赞助，那么就不会收到赞助，有一种乞讨的感觉。

---

[重新思考浏览器输入了 URL 并按下回车之后到底发生了什么——本地 DNS 部分](https://nova.moe/rethink-type-url-dns/)

2024 年了，关于 [[DNS]] 的知识该更新了：Chrome 现在默认会缓存 1000 条记录；systemd-resolved 会承接 DNS 请求； `getaddrinfo()` 查询顺序按照 `/etc/nsswitch.conf` 决定。

---

[How to figure out what to do - Janmeppe.com 👋](https://www.janmeppe.com/blog/how-to-figure-out-what-to-do/)

需要做什么，怎么做。 如果不知道该做什么，说明需求不明确；如果不知道如何做，说明需要一些其他同事的帮助；如果知道做什么以及如何做，但是没有做，就是其他问题（往往超出了个人可控范围）。

[[hashicorp]] 的相关说明： [How HashiCorp Works](https://works.hashicorp.com/articles/writing-practices-and-culture) 

---




### 生活

[年度扯淡 2023 - 知乎](https://zhuanlan.zhihu.com/p/675272919)

老板的年度“扯淡”。创业者的持续焦虑。

---

[万言万当，不如一默 - Yihui Xie | 谢益辉](https://yihui.org/cn/2020/07/silence/)

万言万当，不如一默。

---

[制造币安：极致效率和简陋工具 - by Crypto4.wtf and 汉洋 MasterPa](https://crypto4.wtf/p/8fd)

>对于币安来说，只要不妨碍增长，那一切事情都可以往后放放——包括管理。

根本原因是”增长“，全文提到了”增长“18 次，在火箭般的增长速度面前，所有人都保持着极大的热情（甚至是激情？），会接受”简单粗犷“的管理方式，但是如果增长速度不再，这些问题就会瞬间暴露，放大。

---



## 书影

《老派少女购物路线》，作者非常会写家庭、食物，怎么会把食物描述的这么好。

《极地暗杀 第一季》，西班牙悬疑剧，算是近期看过的不错的剧了，结局没有走向伟光正，我很喜欢。

## 碎碎念

* 我不理解。 
	>女生一个人旅行总是会受到一些莫名其妙的「优待」，那些来自异性的、长辈的优待，就像大学里食堂阿姨总是会给男生多舀一勺肉的性转版。  
	比如，坐公交的时候会有人给你热情做导览介绍沿街建筑啦，住民宿的时候看你在沉浸式工作会给你外带好吃的啦，买轮船票排长队时有人会直接帮你刷卡进去啦，找人换钱时人家直接用最高汇率给你换了且不要你找钱啦……  
	这样的「小恩小惠」可能发生在很多年轻女性的身上。不过这真的没什么好沾沾自喜的，比起「陌生人的善意」，有时候它更像「上位者对下位者的施舍」。因为当你知道你作为年轻女孩会受到这些礼物时，别忘了，性骚扰和暴力同样只发生在你们身上。  
	倒也不是说命运馈赠的礼物早就标明了价格，而是「我曾经也因为自己长得不错受到优待而沾沾自喜，直到后来我发现真正要受到优待还得长一根几把。」    
* 最近骂人口癖明显增多，非常不好。
* 如何保证自己的项目没有失控，是个很重要的技能啊
* 这期播客，劲有点大： https://cyberpinkfm.xyz/episodes/mentalhealth
* 我以为我不需要降噪耳机，实际上我需要
* openEuler 居然会在一个 LTS 版本中修改 rpm 的后缀，从 oe1 变为了 oe2003sp4 ，这是正常的么？？
* CloudFlare 的裁员视频看着很难受。 时代的一粒灰，落在个人头上，就是一座山 。
