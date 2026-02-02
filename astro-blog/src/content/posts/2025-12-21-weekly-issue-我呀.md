---
title: Weekly Issue-《我呀》
date: "2025-12-21T00:00:00.000Z"
slug: "Weekly-Issue-我呀"
tags:
  - Weekly
description:
---

## 文章

### 技术

[周报 1 —— 远程办公 | Oilbeater 的自习室](https://oilbeater.com/2025/12/15/weekly-1/)

> 这个过程中发现了很多我之前的知识盲区。一个是这里面有的项目是通过截图去记录屏幕信息，但是会通过视频的形式进行存储，原因是视频的压缩率会更高一些。我尝试了一下 5s 的频率截取了 120 张图片，用 zip 普通压缩一下还是有将近 400M，而用 FFmpeg 转成 1FPS 的视频后只需要 3.4M。

细想很有道理，[[ffmpeg]] 真是好东西。

---

[致命「飞线」：Cloudflare 极致效率背后的架构赌局](https://archive.is/xEF51)

> 每个做平台、网关、中台的团队，都应该自问：
> 1. **你的架构是否为了省钱而牺牲了隔离性？** 你的「同构架构」在带来资源复用红利的同时，是否也导致了故障域的无限扩大？
> 2. **你的工具链是否有「记忆断层」？** 你是否有那些没人敢修、只能绕着走的技术债？如果它挡住了紧急发布的去路，你会选择修复它，还是像 Cloudflare 一样剪断它？
> 3. **你的「飞线」被建模了吗？** Killswitch、Bypass 等救火工具，是作为「代码的一等公民」被严格测试过状态转换，还是仅仅被当作运维脚本随意堆砌？
> 4. **你是否把「逻辑」误判为「配置」？** 你是否允许那些能改变代码执行路径的开关，绕过代码发布的灰度流程，直接走商业驱动的配置通道全网生效？是不是绝大部分配置应该是静态化，走标准发布流程？


---


[Pricing changes for GitHub Actions - GitHub Resources](https://resources.github.com/actions/2026-pricing-changes-for-github-actions/)

[[github]] [[Actions]] self-hosted runner 将要收费，$0.002 每分钟，public repo 不受影响。如果在自己的 private repo 中跑一些定时任务的构建，需要考虑一下是否需要迁移。

Github 搞了一个 pricing calc 来帮助用户计算自己的成本，这个界面交互是我用过所有 cloud pricing calc 中最糟糕的了： [Pricing Calculator · GitHub](https://github.com/pricing/calculator) 

---

[Updates to GitHub Actions pricing · community · Discussion #182186 · GitHub](https://github.com/orgs/community/discussions/182186)

[[github]] 针对 self-hosted runner 的价格调整影响范围超过了他们的预期，现在推迟了计划，重新评估相关的计费方案。真的很好奇这里的背后的定价决策是怎么形成的，不是好奇收费的原因，是好奇这个数字是怎么确定的： **$0.002 per-minute**。

开发者永远是价格非常敏感的用户。

---


[Chris's Wiki :: It's now a bad idea to look like a browser in your HTTP User-Agent](https://utcc.utoronto.ca/~cks/space/blog/web/BrowserLikeUserAgentBadIdeaNow)

[WebAIM: History of the browser user-agent string](https://webaim.org/blog/user-agent-string-history/)

看到 User-Agent 的讨论，想到了之前看过的这篇文章，关于为什么很多 User-Agent 都是 Mozilla 呢？是因为最早会根据 UA 来判断是否提供 frames，于是后面的其他浏览器都为了能够获得相应的支持，都加了 `Mozilla/5.0`，一直持续到现在。现在的 User-Agent 都是不可信的，没什么用。

---

[Specs Are Back, But We're Missing the Tools | Pierre Zemb's Blog](https://pierrezemb.fr/posts/specs-are-back/)
> I think that's the trick. **Context is everything**. Build the right context, and the LLM produces the right code.

> Natural language gets ambiguous really fast.
> You need precision. English just doesn't cut it.
> I needed something more engineering-driven. Not formal verification for academic purposes, but practical precision that the whole team could read and reason about.

嗯？真的存在自然语言和代码之间的中间状态么？

---

[On the success of 'natural language programming' - Marc's Blog](https://brooker.co.za/blog/2025/12/16/natural-language.html)

好像刚好回复了上面的问题。软件开发从来都是从模糊的自然语言开始的，无论是需求的提出，还是后续的功能细节的讨论，都是基于自然语言。“Specifications are Loops”，反复修改 spec 并不是失败，而是很自然的开发过程，这个是开发的必要阶段，只是现在 LLM 大幅缩短了这个反馈周期。

---


### 生活

[救命！ | 释怀万物](https://newptcai.gitlab.io/zh/blog/how-not-to-die/)

关于[[植物性饮食]]的分享。美国主要的死亡原因是心脏病，中国第二大死亡原因是心脏病（第一是脑血管疾病），动脉粥样硬化主要由于高水平的低密度胆固醇导致，包括：反式脂肪、饱和脂肪、膳食胆固醇。

PPT 的最后一页是一只兔子做瓦肯举手礼：愿你通过多吃蔬菜拥有生生不息与繁荣昌盛。

---

[ChatGPT's rivals, Kwai's quiet rise: the top Internet services of 2025](https://blog.cloudflare.com/radar-2025-year-in-review-internet-services/)

> - **Kwai’s quiet rise in emerging markets:** The Chinese short-video app climbed in our global social ranking and is now #3 in Brazil and high in several emerging markets.

巴西这个地方还挺有意思的，用快手，听 Kpop。

---

[”剩菜不能吃“是立场之争还是科学之争？ | Xigou Blog](https://xigou.github.io/blog/2025/12/16/Leftovers-a-Matter-of-Stance-or-Science)

> 所以你（60KG）每日摄入超过 50g 加工肉类或者 250g 酱菜就会超过亚硝酸盐 ADI。
> 所以最后给出的公众建议是：
> - 剩菜可以吃，但是要尽快放进冰箱
> - 冷藏的剩菜最多可以存 72 小时，亚硝酸盐没有任何明显升高
> - 不能反复热菜，因为会多次等待冷却，进入细菌活跃温度区间

---

[定在原地，回头和远望 – 代码家](https://daimajia.com/2025/12/18/three-years-off-work-living-with-pain-and-finding-life/)

> 这或许就是上天对我的一次警告，我更应该庆幸自己抓住了，而不是陷入到无尽的懊悔之中。上天会给你在大限之前无数次警告，可能是一次次的体检报告的指标，可能是那难以消退的疼痛，可能是周围朋友的遭遇。他是希望你能抓住的，抓住了就要做些改变。

> 我忽然觉得这才是生活。我以前从来没有生活，只有一碗碗混着鸡汤的鸡血。

孕妇效应明显，自从我父亲腰间盘突出之后，感觉突然间所有人都腰疼了。

---

### 书影播客

《我呀》，王梓晗单口喜剧专场，在 B 站上可以[免费观看](https://www.bilibili.com/video/BV1PL4az2EU1/)。
这不是一个单纯搞笑的专场，而是一个注重文本和表达的专场，这个专场的文字稿如果单独拿出来看，应该也会是一个非常精彩的叙事作品。

专场内容就是标题，讲述的是“我“。这样一个从小是别人家孩子，无论是家庭还是学习都是佼佼者，但是唯独缺少了“我“，一直在迎合着别人的期待。母亲是非常典型的“东亚母亲“，因为职业是教师，还是个加强版本，父亲是警察，存在感很低。她在大四的时候确诊了重度抑郁，于是开始了自己的心理治疗，甚至因为心理医生太过于紧张，她都会去找一些经典案例来编造故事，让心理医生感觉“这道题我学过“。

越缺少什么，就越想要什么。

《狗仔夜行》，魔宙系列小说，作者是郑读。魔宙公众号我应该是 2016 年知道的，一直时不时的追连载，还挺喜欢的，这本小说中的一些故事感觉之前读过，但是连续的故事读起来还是很爽快。不能去带着半真半假的角度去看待这本小说。



## 碎碎念

* 感冒后的第一个间歇跑，突然最后一组突然心率跳到了185，瞬间崩。
* manus 超过了 Lovable，现在是最快的 $100M ARR 公司/产品。可是我没见过身边有人使用它。
* Docker 提供的 DHI 并没有用 Dockerfile 维护，而是用了 syntax=dhi/build，但是 dhi/build 没有开源。
* 17km，12km 的时候有些困了，最后 1km 很艰难。
* 宁波马拉松中签率 10%，不出意外，我是那 90%。


