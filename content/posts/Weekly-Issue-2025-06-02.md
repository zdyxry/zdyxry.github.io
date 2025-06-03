---
title: Weekly Issue-如何看病
date: 2025-06-02
tags:
- Weekly
description:
---


## 文章

### 技术

[Implemented AGPL MinIO Object Browser simplified Console by bexsoft · Pull Request #3509 · minio/object-browser · GitHub](https://github.com/minio/object-browser/pull/3509)

有趣，[[Minio]] 删除了社区版本中的管理界面。官方说法是这些代码没在维护，且容易有安全问题，所以删除了。印象中之前 [[Lens]] 也有过类似的操作。

---

[2025.05 云原生相关信息简报 | 云原生信息简报](https://quaily.com/cloud-native-ralated/p/cloud-native-information-newsletter)

[vGPU 是伪命题？NVIDIA 官方为什么不自己出细粒度共享呢？](https://archive.is/IFd78)

5 月份的 [[k8s]] 简报。[[HAMi]] 的这篇文章很真诚，截取部分记录。关于产品的核心竞争力，选准赛道很关键，当前国内用户对国产化设备的支持几乎是必选项，我觉得这就是核心竞争力，这也能解释为什么国内用户采用的很多而海外很少，文中提到的“信任”更多的是核心竞争力的附属品。

> **NVIDIA 为何“不为”？是技术不能，还是商业不愿？**   
>  对 NVIDIA 而言，“不为”并非力有不逮，而是为了守护高端硬件溢价、vGPU 许可收入，以及既有关键生态伙伴关系的综合商业选择 —— 这正给了 HAMi 在容器原生、细粒度共享上的机会空间。   
>  **HAMi 的核心竞争力与长期护城河到底在哪里？**   
>  对异构硬件的广泛兼容。   
>  我认为，真正的壁垒更多在于那些难以快速复制的要素。不断增长的社区用户和贡献者，正在逐步形成一个生态圈，赢得这个圈子的信任需要时间。通过大规模实战检验所积累的**客户信任与产品稳定性**。   

另外一个小细节，产品的 FAQ 中，“Why don’t some domestic vendors require a runtime for installation?”，为什么要加 "domestic" 呢？

---

[Wicked features | sean goedecke](https://www.seangoedecke.com/wicked-features/)

> Wicked features are features that must be considered _every time you build any other feature_.

> This is a common reason for engineers underestimating tasks. It’s easy to forget one or more wicked features that complicate the implementation, and then to get blindsided when someone asks “what about X?”    
> This is particularly true of engineers who haven’t spent much time at the company and might just straight-up not know about some of the wicked features.   
> Company “veterans” are valuable largely because they’re familiar with all the wicked features.

---

[Secure Self-Hosted Password Manager: Deploying Vaultwarden with Tailscale and Docker | by kevincxy | May, 2025 | Dev Genius](https://blog.devgenius.io/secure-self-hosted-password-manager-deploying-vaultwarden-with-tailscale-and-docker-b650fe104ff3)

使用 [[TailScale]] 自托管 [[VaultWarden]]，使用 TSNET 配置之后，1 个 domain 对应的应该是 1 个 device，[[TailScale]] 个人免费最多 100 个 device。

---


### 生活

[moving managers](https://x.com/mitchellh/status/1928539528823976057)

“搬家经理”（可以这么翻译么？），Mitchell 需要搬家，但是涉及到大量的物品整理以及恢复，如果自己来做需要花费不少经历，所以朋友推荐了 moving manager，提供自己的生活方式信息（包含作息、物品位置、做饭视频等），对方会在 24h 完成搬家流程，整体开销小于 50k 刀。

有趣的是，moving manager 没有网站，没有 yelp，没有社交媒体，完全靠朋友介绍，口口相传。

感觉有点像老家附近的临时工，如果做的靠谱，自然会有人推荐给身边朋友，只是这个岗位是全国性质的。

---

[只办婚礼不领证，年轻人开始一种很新的「婚姻」](https://archive.is/c1tkD)

这是一篇很好的 10w+ 文章，这不是一篇好文章。样本选择和叙事方式的结果，就是评论区火热，阅读量飙升。

---

[20240111: 35 岁](https://carlosgong.github.io/posts/2024011101.html)

> 我觉得在进入 35 岁时，我在心理上主要变化是：接受自己是一个不太聪明的人，并且不再为自己过去的「幼稚」行为和想法感到羞耻 / 不好意思。   
> 到了接近 35 岁的时候，我觉得经历了过去十几年的反复循环，这些「无法面对过去的自己」的想法都逐渐烟消云散了 —— 我就是我，我有各种问题、我有很多不会的东西、我曾经想法很奇怪，但是这些都是生命中必经的阶段。所以我不再纠结这些了

我自认为现在接受了自己，不知道几年之后是否还会这样想。

---

[如何看病 | GoldenGrape's Blog](https://goldengrape.github.io/posts/ophthalmology/How-to-see-a-doctor/)

如何看病。

---


## 书影


《机智住院医生生活》，从第 3 集开始进入到了熟悉的节奏，可能也是因为熟悉的面孔回来客串了，还不错。感觉这部剧的血腥场面要比《机智的医生生活》多不少，不太适应。

《Biong Biong 地球游戏厅》，韩国综艺，4 位明星跟着罗英锡做游戏旅游的故事，适合下饭看。艺人的能量太高，感觉有用不完的力气，能感觉到有一些演绎的成分，但还是很佩服。

《强风吹拂》，“你喜欢跑步吗？” 。我很难说是否喜欢，跑步是一件当前让我感觉还不错的事情，如果可以的话想要继续跑下去。


## 如何看病

发现自己很少与医院打交道，近期身体不适去医院看病，才发现自己对如何看病一无所知。此处记录一下自己在上海华山医院的看病经历，供参考。

### 背景

我的社保所在地是北京，工作地是上海，所以需要在微信小程序“异地备案”中进行备案。

### 预约挂号

华山医院的挂号是分为预约挂号和现场挂号，现场挂号需要地理位置在医院附近 3km 内，除非特殊情况，选择预约挂号即可。 因为我是异地医保，所以预约挂号使用的是自费账号，第一次就诊前，需要在对应科室的收费处和工作人员进行说明，会更换为医保账号。

第一个问题是，自己应该挂什么科室，之前可能需要去医院的导诊台咨询，现在可以直接借助各种 AI 进行初步分析，比如华山医院小程序中自带的 AI 咨询。关于是否挂专家号，我个人认为，大多数人是不需要的，而且知名医院大概率挂不到专家号。

### 就诊

以我在普外科的就诊为例，到达医院后，需要看对应的科室要求，是否需要“签到”。虽然预约挂号的通知上已经有了对应的时间，但如果需要签到，还是需要在到达医院后进行签到，才会开始排队叫号（比如华山医院的眼科需要签到）。

等待排队即可，叫号后进入诊室，进行简单的问诊，描述清楚自己的症状（我个人有一个文档专门记录自己的身体情况，记录自己所有感觉到身体不适的时间点和症状）。

医生开了 B 超检查，先缴费，再去 B 超检查室进行预约，大概率预约不到当天的检查，我预约到了第二天的，于是返回普外科和医生沟通，确认医生第二天是否出诊，得到肯定答复后，第二天进行B 超检查，拿结果直接找医生确诊，开药方，就废，拿药结束。

到这里和我之前去医院的经历差不多，不同的是预约检查和就诊不是同一天，这里和医生确认了第二天是否出诊，所以我检查当天没有挂号。

### 复查

之前医生说一个月之后需要复查，一个月后进行预约挂号，复查时戴上了上一次的就诊记录和检查结果，医生没说什么，开了B 超检查，缴费后去检查室预约检查时间，这次检查项多了一个，最早可预约的检查是 5 天之后，只能 5 天后再来。

5 天之后来检查当天，需要先签到（和第一次检查又不一样，上一次无需签到），然后排队叫号。预约单上写明我是 10:30 - 11:00 的时间段，我签到时间是 09:47，虽然不在预约时间段内，也是允许签到的，最终我检查的时间是 10:50。如果我在 10:30 之后签到，那我检查的时间可能会更晚。

这里发现一个问题，我当天没有挂号，我不知道一个月前就诊的医生当天是否出诊，我不能拿着检查单直接去普外科找医生，赶紧在排队的时候紧急挂号，这里就是前面提到的当天挂号，我此时就在医院里，所以符合 3km 要求，挂到了当天的普外门诊，拿到检查单后去找医生挂号。

由于没有报销经验，第一次就诊没有让医生开病历，所以这次特意让医生开了病历，写明日期，便于后续报销。

### 总结

完整的流程是：
* T0 预约挂号
* T1 就诊
* T2 B 超检查，确诊
* T3 预约挂号（复查）
* T4 复查
* T5 B超检查，复查

一点经验：
* 平和的心态，去医院看病的病人大多数都是身体不适，身体情况会影响情绪，医生也会有情绪，告诉自己“平常心”；
* 就诊前确认是否需要签到，别傻等；
* 检查结果无法当天拿到，不确定医生是否出诊，重新挂号稳妥；
* 出了门诊室，大概率需要先缴费；
* 确认后及时让医生更新病历，便于后续报销；



## 碎碎念

* 感觉 LLM 的 Deep Research 应该根据文章的时间、作者进行相应的权重调整。
* 5 月 25 号，同事跟我说，618 结束了。
* 有时候想要顺手（顺口）问 AI 一个问题，但是交代起来需要打字出完整的上下文，会感觉有点麻烦，想着语音输入也许在 AI 时代真的很有必要。
* 我非常想念一位前同事，如果他还在的话，一定会跟我一起反驳老板的。突然有些难过，很难过。
* 周五了，一篇文章都没看，真是荒废的一周。
* 箱根驿传好热血啊
* 综艺、电影、电视剧中透出的元气，都可能有演绎的成分，体育不会
* 每当想要深度使用 Folo 的时候，都告诉自己，这不是一个可自建的项目。
* 去东京的时候，从同事那里拿了一些日元现金，回来之后转账给她人民币，这笔钱怎么记账难住我了。
* 自行车后胎又扎了，一年内的第 3 次了？