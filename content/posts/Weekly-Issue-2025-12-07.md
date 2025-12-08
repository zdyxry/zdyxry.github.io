---
title: Weekly Issue-《你可以跑的更快》
date: 2025-12-07
tags:
- Weekly
description:
---



## 文章

### 技术

[You’ll never see attrition referenced in an RCA – Surfing Complexity](https://surfingcomplexity.blog/2025/11/02/youll-never-see-attrition-referenced-in-an-rca/)

hot potato：原作者或原负责团队离开后，服务被移交给缺乏深度知识的新团队，导致操作经验不足;

bus factor：团队对关键知识或关键人员的依赖程度。

---

[写在离开 Folo 之后 - 静かな森](https://web.archive.org/web/20251201065213/https://innei.in/posts/experience/after-leaving-folo)

[[Folo]] 的商业化就是 RSS 的商业化，而  [[RSS]] 商业化的上限很低。

---


[Bun is joining Anthropic | Bun Blog](https://bun.com/blog/bun-joins-anthropic)

> Today, Bun makes $0 in revenue.

> A few weeks ago, I went on a [four hour walk](https://x.com/thdxr/status/1985586605877252285) with Boris from the Claude Code team. We talked about Bun. We talked about where AI coding is going. We talked about what it would look like for Bun's team to join Anthropic. Then we did that about 3 more times over the next few weeks. Then I did that with many of their competitors. I think Anthropic is going to win.

[[Anthropic]] 收购了 [[Bun]]。想要被收购么？先 City Walk 四个小时吧。

---

[Senior Infra Engineer: Datacenters | Railway](https://railway.com/careers/dc-engineer)

[[Railway]] 打算自建数据中心了，想到了这两天又看到有人在讨论下云，可以看看能否应付要面临的问题：
- 为数据中心设计和采购了价值超过 100 万美元的硬件
- 在全球范围内管理和协调供应链
- 设计机架级布局以实现最佳效率（散热 / 能耗等）

---


[Go proposal: Type-safe error checking](https://antonz.org/accepted/errors-astype/)

```go
// using errors.As
var appErr AppError
if errors.As(err, &appErr) {
    fmt.Println("Got an AppError:", appErr)
}
// using errors.AsType
if appErr, ok := errors.AsType[AppError](err); ok {
    fmt.Println("Got an AppError:", appErr)
}
```

[[Go]] 1.26 版本引入 `errors.AsType`，真不错。

---

[Cloudflare outage on December 5, 2025](https://blog.cloudflare.com/5-december-2025-outage/)

> Customer traffic served by our China network was also not impacted.

> Before the end of next week we will publish a detailed breakdown of all the resiliency projects underway, including the ones listed above. While that work is underway, we are locking down all changes to our network in order to ensure we have better mitigation and rollback systems before we begin again.

[[CloudFlare]] 在周五再一次发生严重故障，Lua 版本的 Proxy 没有处理 nil 异常。这种短时间内的两次严重故障，如果我是企业用户，是否需要更换服务商？这时候评估的标准是什么？

---

[Harbor GC 问题 | 卡瓦邦噶！](https://www.kawabangga.com/posts/7057)

维护 [[Harbor]] 总是很麻烦，很久之前我维护了一个 docker compose 的 Harbor，但是后面尝试几次升级都失败了，后面只能重建一个新的 Harbor 实例，后面负责的同事针对每个 Project 进行了严格的空间限制，经常用着用着就需要去删除无用 Image，Harbor 自己的删除策略不太好用。

> 这是一个很有意思的「用运维手段解决技术问题」的例子，在 SRE 的工作中，迫于没有对软件的实现的控制力，我们经常需要用运维手段来解决代码实现上的问题。

这篇文章中提到的两个方式都很有趣，无论是通过找到瓶颈想办法绕过，还是通过搭建两套 Harbor 实例配合 Nginx 进行管理，前者有趣在于寻找瓶颈，后者有趣在于如何在现有限制情况下实现需求，解决当前面临的运维问题。

---

[If You Missed KubeCon Atlanta Here's the Quick Recap | MetalBear 🐻](https://metalbear.com/blog/kubecon-atlanta-takeaways/)

> It felt that OCI has moved from being “a new way to package things” to simply the default way to distribute anything: Helm charts, WASM modules, you name it. The community seems to be converging on a single distribution model that works consistently across registries and tooling.

“OCI, quietly taking over” 是好事。

---



### 生活

[被嫌弃的松子的一生 - Frost's Blog](https://frostming.com/2025/county-woman/)

> 这集齐了家暴、重男轻女两大毒瘤于一身的故事，就发生在我身边，我听完只觉胸中女拳之火熊熊燃烧，想告诉玲子，醒醒吧，生孩子不会好起来，好起来的办法只有一个，就是离开，立刻、马上。可惜我无能为力帮她改变命运，只能把它写下来，写在这里，告诉大家这个千千万万个一样的县城中的平凡的故事。原谅我没有第一手资料，只能用很多「我听说」这样没有力量的词语，写得乱七八糟。

无力是常态。

---

[大巴 | 卡瓦邦噶！](https://www.kawabangga.com/posts/7106)

 有些人有些事，不记下来就忘了，以前觉得忘了也就忘了，没什么大不了的，现在却越来越怕自己忘了。

---
[2025 Garmin Connect data report | Garmin Blog](https://www.garmin.com/en-US/blog/general/2025-garmin-connect-data-report/)

[[Garmin]] 2025 用户数据报告，力量训练增长 29%，女性比男性多 6%；巴西用户人均力量训练量比排名第二的墨西哥高 44%，这数字好夸张。不同年龄端用户的运动偏好感觉也挺符合刻板印象的：18–29 岁：户外跑步、田径跑； 30–39 岁：力量训练、室内有氧、跑步机；40–49 岁：越野跑。

比如关注的一个博主，上马 2023 年成绩是 518，年龄段 34 岁以下排名是 1511。2025 年成绩是 408，年龄段 35-39 岁排名是 1781。

---

[TIME’s Top 100 Photos of 2025](https://time.com/7336112/top-100-photos-2025/)

《时代》周刊 2025 年度百大摄影作品，特朗普含量很高。

喜欢玫瑰那张照片。

---


### 书影播客

[巴黎奥运会 Vlog](https://www.bilibili.com/video/BV14Z421N7Cc)

吴向东的 vlog，这是我近期看过最好看的 vlog。

---

《你可以跑得更快》，作者是徐国峰，一直从事跑步教练工作。在读这本书之前，我自己跑步的时候尝试了提高步频（180->190/200），也尝试了提高步幅（0.9m->1.1m)，效果是一样的，都很快跑崩。这本书之前听播客被推荐了几次，周末开始认真看。因为自己也跑了很久，所以看的时候一直带着明确的问题：我如何跑的更快？

跑步实力由体能、肌力、技术三部分组成。最大摄氧量衡量身体引擎每分钟能输出的最大能量，即每分钟身体每公斤体重消耗的氧气量，跑步的引擎不在于心脏或者肺部，而是肌肉纤维中的线粒体，线粒体越多，体能越好。肌肉端训练优先于心肺端，不然可能会出现心肺能力训练了很久，但是肌肉跟不上，导致效率不高。

建议使用储备心率来区分不同的强度区间，储备心率计算方法：目标心率区间 = (最大心率 – 静息心率) × 储备心率% + 静息心率。

强度区间|储备心率百分比
---|---
E 心率区间：1.0~1.9 | 59%~74%
M 心率区间：2.0~2.9 | 74%~84%
T 心率区间：3.0~3.9 | 84%~88%
A 心率区间：4.0~4.9 | 88%~95%
I 心率区间：5.0~5.9 | 95%~100%

如何评估训练量？依靠训练强度与训练时间，不依靠训练距离。10 分钟 5 级强度与 50 分钟 1 级强度的训练量可能相同。训练能改善体能，也会带来疲劳，通常疲劳系数大于体能系数，体能进步需要时间来体现，疲劳却是立竿见影的。

（这本书和 RQ 的关系很紧密。



## 碎碎念

* 第一次在 Gemini DeepResearch 看到“研究失败” 。
* 买了人生中第一个打火机，因为裤子有个线头，居然有 5 块钱，好贵。
* 折腾了下佳明账号，把国际和国内数据同步下，他们的账号域名还挺有趣的，connect.garmin.com, connectus.garmin.cn, connect.garmin.cn ，傻傻分不清。
* “污言秽语”，这个词可太灵活了。
* 把歌单从 Spotify 迁移到了Youtube。
* 00:06 睡觉，00:11 给我打电话就没接到，睡得也太死了。
* 浑身酸痛，从 18 点持续到 21 点，一直睡不着，我不会是得流感了吧？

