---
title: Weekly Issue-《奔跑吧，爸爸》
date: "2026-10-18:00:00.000Z"
slug: "Weekly-Issue-Run-Dad"
tags:
  - Weekly
description:
---

## 文章

### 技术

[2024 年模型训练攻击事件：受害者陈述与证据整理](https://keyu-tian-sabotage.github.io/)

> 在情况最严重的一两个月里，项目组几乎进入了全天候的故障排查状态。分布在北京、上海和西雅图的中美团队轮流值守，24 小时监控训练程序的运行情况。团队每天早晚召开会议，交接排查工作，汇总当天发现的异常现象，区分哪些问题已经得到解释、哪些仍然无法解释，并讨论下一步的诊断方向。整个过程就像一支 24 小时待命的医疗团队，守着一位病情危重、不断出现疑难杂症的患者，随时准备应对新的突发状况。

这种故障排查情况一个人持续一两周就很难受了，一个组一两个月，承受的压力可太大了，估计都怀疑人生了。

---

[How the incident happened: a play in one act – Surfing Complexity](https://surfingcomplexity.blog/2026/09/19/how-the-incident-happened-a-play-in-one-act/)

> A: I see what you're saying, I really do. I'd like to be able to sit down and spend the time really reading through this whole document. But, given all of the current obligations that business has placed on me, I don't have that time to invest. I want to learn from this incident, and I know I would learn more if I spent the time on reading the whole thing, but there's a limit to how much time I can commit to that. So I need to have the important details summarized.   
> B: Just to make sure I understand: you're saying that, even though you admit you'd learn more if you read the entire write-up, because of the various work pressures that you are facing, you're making an explicit trade-off to reduce the amount of time you spend on this task, in order to have the time to spend on other tasks you have to work on?   
> A: Yes, exactly!    
> B: Well, now you know how the incident happened.

笑话一则，同理可换成 AI summarize。

---

[Feature freeze update 4](https://docs.endurain.com/blog/2026/10/09/feature-freeze-update-4/?ref=selfh.st)

> Since moving Endurain to Codeberg, we ran into some real problems:   
> - We've been hit with repeated availability problems, especially with SSH access, Codeberg going down, and commit operations failing as a result. This was starting to actively slow down development, especially since we do this in our free time;

这个项目又从 [[Codeberg]] 迁移回 [[GitHub]] 了，还是那个观点，现在这个阶段迁移只会带来更多的问题，我好像还看到 Cursor Origin 也有类似的评论。

---

[Stateful jobs · rakyll.org](https://rakyll.org/stateful-jobs/)

从多个角度考虑有状态应用面临的问题：放置、升级、应用分层、故障处理、空闲判定。比如放置阶段，要容忍节点暂时不可达，因为短期不可达引发的状态重建动作更重；空闲判定的缩容对应的是一系列动作，如何设置合理的空闲时间；如何判断任务是否空闲，仅靠流量是不准确的。

---

[Better HTTP/1 connection reuse - The Go Programming Language](https://go.dev/blog/http-connection-reuse)

> Even programs that do read the response body can run into this issue if they stop just short of the end of the body. For example, [`encoding/json.Decoder`](https://go.dev/pkg/encoding/json#Decoder) stops reading as soon as it sees the closing `}` of a JSON object.    
If a server sends a JSON response terminated with a newline, decoding the JSON object will leave the newline still unread. The connection cannot be reused for a new request until that newline is consumed. Thus, a healthy connection might end up being abandoned, even though it was only a single byte away from being reusable.

[[Golang]] 1.27 真是好啊，应升尽升。

---

[NTP: Building a more accurate time service at Facebook scale](https://engineering.fb.com/2020/03/18/production-engineering/ntp-service/)

[[Meta]] 采用 4 层 NTP 服务设计：0 层是 GNSS（全球导航卫星系统）；1 层是 Meta 自己的原子时钟，2 层是 NTPServer，闰秒的平滑处理在这一层；3 层是更多的 NTPServer。文章主要对比了 Ntpd 和 Chrony 在时间预估的差异，发现 Chrony 的时间预估要比 Ntpd 好很多，并进行了更多的测试，最终得到的结论精度好 10 倍到 100 倍。Chrony 还支持硬件时间戳，能将精度提升到几百纳秒，可以通过 `ethtool -T` 来查看：

```
$ ethtool -T ens1f1
Time stamping parameters for ens1f1:
Capabilities:
        hardware-transmit
        software-transmit
        hardware-receive
        software-receive
        software-system-clock
        hardware-raw-clock
PTP Hardware Clock: 3
Hardware Transmit Timestamp Modes:
        off
        on
Hardware Receive Filter Modes:
        none
        ptpv1-l4-sync
        ptpv1-l4-delay-req
        ptpv2-event
```

---

[NTS: Authenticated Time at Meta - Engineering at Meta](https://engineering.fb.com/2026/10/06/production-engineering/nts-authenticated-time-at-meta/)

[[Meta]] 在 NTP 服务器上启用了 NTS (Network Time Security)，目的是解决 NTP 缺少的认证机制。常见的 HTTPS 使用 X.509 证书来验证，但是 X.509 本身所依赖的 notBefore/notAfter 会导致当你时钟出现偏移时校验失败，进而导致无法同步时间，存在循环依赖，常见的绕过方式是跳过验证，或者放宽证书有效期窗口。NTS 解决的是同步路径中的中间人伪造时间响应，不能防延迟攻击。

---

[Thoughts on the July 8th Telstra outage report – Surfing Complexity](https://surfingcomplexity.blog/2026/09/12/thoughts-on-the-july-8th-telestra-outage-report/)

[[NTP]] 3 连，是这种阅读时间最长的文章了。澳大利亚 Telstra 因为 NTP 原因引发的重大网络中断，中断影响非常大，有大量的紧急呼叫（类似于110/119/120）无法接通。作者写了一些自己的推测和图示，记录一些关键点：
1. 谨慎设置 NTP peering/symmetric 对等连接，保证 NTP 同步有一个清晰的层级关系；
2. 变更留痕很重要，这次故障原因最早可以追溯到 6 年前；
3. 感觉上维护团队没有人知道 GPS 当时是啥作用？
4. GPS 可能存在 rollover issue（不是所有 GPS 都存在这个问题，后续供应商提到了发送邮件提醒更新固件）内部记录 19800105 以来的周数，是一个 10 位的二进制数，每 1024 周会翻转一次，19.7 年；


### 生活

[Winlane：我的 Mac 工具箱](https://catcoding.me/p/winlane/)

> - [Raycast](https://www.raycast.com/): 这几乎是大部分人的选择，但我只用其中的部分核心功能，而 Raycast 的新版本越来越臃肿。

我日常用 [[Raycast]] 的功能可能只有 2 个：剪切板管理，应用快速启动，其他功能完全用不上。

---
 
[大马攻略（上）：在吉隆坡与马六甲，做一只与南洋味道热恋的蜜蜂。](https://web.archive.org/web/20261017065015/https://www.douban.com/group/topic/495526051/?_spm_id=MTg4OTcxODU4&_i=2219319LSXVbco,2219816fkobzPn)   
[大马攻略（下）：从怡保到槟城，蕉风椰雨流俗地中，南洋北望唐人街外。](https://web.archive.org/web/20261017065238/https://www.douban.com/group/topic/494936067/?_spm_id=MTg4OTcxODU4&_i=5414907d9SxPiF,2219390LSXVbco)

拍的多，写的好。

---

[No Man Is an Island](https://borretti.me/article/no-man-is-an-island)

> Motivation we can break down into two components:   
> - **Intrinsic motivation:** we learn for the sake of learning, we create art from a compulsion we can't understand, etc.    
> - **Extrinsic motivation:** David Chapman [defines](https://meaningness.substack.com/p/nobility-table-of-contents) "nobility" as manifesting glory for the service of others, and using our abilities in service of others. We want our work to be useful to others, we want others to benefit from our work, we want to contribute to a shared human project. Fame and the esteem and good will of your peers are the proxies by which we measure our contribution.    
> We tend to think of intrinsic motivation as the purest kind: endogenous, self-created, unmotivated by material or social gain. But it's an emotion, and, like all emotions, it's transient and short-lived. And this is rational: otherwise, we'd all be stuck in life-long unproductive obsessions. So, we need something to fill the gaps between moments of divine inspiration. Extrinsic motivation serves this function.

---

### 书影播客

[灰度纪年-李光耀：当代最强「造国者」｜26W04](https://www.xiaoyuzhoufm.com/episode/69764639109824f9e17fb911)

朋友送的付费播客，讲述的李光耀的故事，信息来源比较丰富，有书、报纸、视频、演讲等，适合跑步的时候听。

《奔跑吧，爸爸》，上图新书柜上的发现，最近发现上图的韩国作家书籍少了很多，不知道是搬到其他地方还是什么原因，难得看到新书。这是金爱烂的第一部短篇小说集，能够看到数据故事的角度不多，写的很真实。我比较喜欢其中的两篇： 《谁在海边随便放烟花》中的结局和预想中一致，但是作者在可以预想到的结局中还是给了惊喜；《不敲门的家》更多的是大家在大城市中求生活，每个人以为自己是不一样的，自己有自己的想法自己的追求，但又同样的孤独和疏离。

## 碎碎念

* 休息一天确实不行。
* 企业微信支持了 channel 功能，默认创建出来的是不公开的，开放又不开放。
* 惊输，Kiasu，源自闽南话，意思是“怕输”。
* 最近发现一个提升幸福感的事情，用米家在自己快到家之前设置自动开灯。自己回家的时候，家里灯是开着的，感觉还是挺好的
* 日体大的神奇还在继续
* 不要习惯性的用暴力的方式处理问题
* Metal3 的发音是 meta cubed.
* 两周没喝咖啡了
* 上海图书馆的韩国作家的书好像少了很多