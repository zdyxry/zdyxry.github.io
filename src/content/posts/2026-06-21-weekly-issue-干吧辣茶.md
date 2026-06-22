---
title: Weekly Issue-《干吧！辣茶！》
date: "2026-06-21:00:00.000Z"
slug: "Weekly-Issue-"
tags:
  - Weekly
description:
---

## 文章

### 技术



[使用nc命令发送网络请求的一个问题 - 陪她去流浪](https://blog.twofei.com/2308/)

不同来源和不同版本的 `nc` 超时时间参数有些差异，不推荐使用，如果一定要用，建议在外面套一层其他的 timeout。

---

[程序员和软件还有前途吗？从 NocoBase 收入再翻倍谈起](https://x.com/estheryoyoyo/status/2066445140022235186)

> 这种状态马上在我们团队内部开始蔓延。有不止一位同事认为我们做的产品已经没有意义了，因为这种无意义感，导致严重影响正常工作。花几年时间做一个引以为豪的东西，今天 AI 看起来好像几个小时就能做出来，更不用说 AI 还在以极快的速度进化，我们还有存在的意义吗？

> 在 AI 的冲击下，世界的节奏好像加快了很多，尤其在自媒体和平台算法的加持下，每天被新概念狂轰滥炸。但是从我们的实际接触来看，AI 厂商和自媒体与真实世界中的企业是两个差异巨大的群体。   
> 无论概念如何轰炸，真实世界中的企业还在正常生产他们的药品、汽车、矿泉水，还有很多企业连数字化都做不到，在大量使用纸张和 Excel，更别谈 AI 革命了。立足于我们能找到的长期不变的东西，并作为我们产品的服务对象，这将是我们健康活下去的根本。

---

[闲鱼，千问，支付宝：平台信任“赋能”诈骗](https://vonng.com/cloud/ali-scam/)

> **闲鱼信任淘宝，淘宝信任支付宝，支付宝信任千问，然后在千问 CDN 放个钓鱼页面，破功了。**
 

> 1. [https://m.tb.cn/a.VOXUQ](https://m.tb.cn/a.VOXUQ) ← 淘宝短链
> 2. [https://market.m.taobao.com/app/.../wakeup-transit](https://market.m.taobao.com/app/.../wakeup-transit) ← 淘宝唤端中转
> 3. [https://m.taobao.com/?weurl=](https://m.taobao.com/?weurl=)... ← 淘宝 weurl 跳转
> 4. [https://render.alipay.com/p/s/i?actionType=route&qrcode=](https://render.alipay.com/p/s/i?actionType=route&qrcode=) ← 支付宝唤端路由
> 5. [https://workspace-zb-cdn.qianwen.com/.../...html?c=](https://workspace-zb-cdn.qianwen.com/.../...html?c=)← 通义千问 OSS/CDN 中转页
> 6. [https://glicdn.sunaiqwg.top/shisixianyu/App.php](https://glicdn.sunaiqwg.top/shisixianyu/App.php) ← iframe 仿闲鱼钓鱼落地页

好巧妙的骗局啊，我倒是没用闲鱼扫描过二维码，如果有这个使用习惯的话，我可能也容易中招。

---

[April 2026 Outage Post-Mortem - Jim's Pckt - pckt.blog](https://pckt.blog/b/jcalabro/april-2026-outage-post-mortem-219ebg2)    
[Thoughts on the Bluesky public incident write-up – Surfing Complexity](https://surfingcomplexity.blog/2026/04/12/thoughts-on-the-bluesky-public-incident-write-up/)

[[Bluesky]] 事故报告及分析，新上线了一个 API，API 本身的 QPS 很低，但是在一些场景下 request body 会包含大量的 URI，在数据面服务上针对每个 URL 都会创建一个 goroutine，通常都会设置 goroutine 数量限制，但是刚好这个接口没有，导致创建了大量的连接请求，进而导致大量 TCP TIME_WAIT，导致可用端口耗尽，数据面服务在连接 memcache 错误后会记录日志，每秒百万条错误日志，导致大量的 `write(2)` 阻塞调用，生成了大量的操作系统线程，最终影响 GC，服务 OOM。服务重启后又因为无可用端口，循环触发问题。

文章中提到的临时修复方案很不错：

```go
// Use a custom dialer that picks a random loopback IP for each connection.
// This avoids ephemeral port exhaustion on a single IP when a container
// restarts (TIME_WAIT sockets from the old process block the fixed IP).
memcachedClient.DialContext = func(ctx context.Context, network, address string) (net.Conn, error) {
	ip := net.IPv4(127, byte(1+rand.IntN(254)), byte(rand.IntN(256)), byte(1+rand.IntN(254)))
	d := net.Dialer{LocalAddr: &net.TCPAddr{IP: ip}}
	return d.DialContext(ctx, network, address)
}
```

---





### 生活

[GitLab cuts 14% of staff as it scales its platform to serve AI workloads](https://techcrunch.com/2026/06/03/gitlab-cuts-14-of-staff-as-it-scales-its-platform-to-serve-ai-workloads/)

[[GitLab]] 重组的具体数字公布了，14%，350 名员工。

---

[Derbyshire police officer investigated for using AI to 'create evidence' in multiple cases](https://news.sky.com/story/derbyshire-police-officer-investigated-for-using-ai-to-create-evidence-in-multiple-cases-13553661)

> A Derbyshire police officer is being investigated over accusations they used AI to "create evidence".

《真相捕捉》照进现实，防不胜防。

---

[2026 欧洲之旅：资产安全](https://www.ixiqin.com/2026/06/15/2026-european-tour-asset-security/)

> 第一个好物是自行车锁（带伸缩的那种）。     
> 朋友和我说这个的时候，我还一脸懵，没明白这个是干嘛的。朋友解释说：欧洲这边坐火车投行李的人非常多，有了这个，你就可以把你的行李锁在高铁的行李架上，更安全，小偷没办法把你的行李给偷走。

第一个好物就超出了我的想象，前阵子同事去欧洲的时候，也买了很多八字扣。

---

[UniGetUI —— 可能是 Windows 下最好用的应用商店 - 白宦成](https://www.ixiqin.com/2026/06/17/unigetui-may-be-the-best-app-store-for-windows/)

> 作为一个包管理器的 GUI 实现，他提供了 Windows 近年来正火的 WinGET、老牌包管理器 Scoop 和 Chocolaty，同时也针对 Windows 下的 Powershell 5 和 Powershell 7 提供了相关的包管理器；针对编程用户常用的 NPM、PIP、Cargo 和 VCPKG 也有涉猎；虽然能力不完全对其，但最基本的安装管理和卸载等能力都是有的。

用起来还不错，挺方便的。

---





### 书影播客

《干吧！辣茶！》，辣茶单口专场，从演出前的准备时间就感觉到了这场的特殊，他在舞台上放了一台跑步机跑步，然后随机抽观众上台跑 3min。辣茶是一名英国留学生，专场主要讲述的是他毕业之前的旅行经历，没有价值，没有观点，没有想教点什么，这在最近几年的专场中都是少见的，我好像看过的第一场这样的专场。我从来没见过辣茶这样的表演风格，非常的狂躁（褒义），外向到极致，让我都有些不适应，我生活中好像没有这样性格的朋友。专场的内容上，反复的强调”这是真事“，讲完一段之后会讲为什么要写这段，我觉得完全没必要，自己讲解自己的段子不奇怪么，很奇怪啊。其中很多段子，感觉拍成短视频会好很多，配合上他丰富的肢体呈现，我觉得会火，类似于这个视频中的呈现： [《不要进入金字塔！可以刻在我遗书上的7个字》](https://www.bilibili.com/video/BV1VcSZBkEGm)

《经典电子游戏漫游指南》，制作优良，排版精美。

《LlamaIndex大模型RAG开发实践》，上图看到的“新书“，大人，时代变了。

[合集·《最好的足球节目》](https://space.bilibili.com/201164593/lists/958793?type=season)  
世界杯又开始了，假期重新回顾了一下这个系列视频：，标题是《梅西c罗球迷观看 XXX 比赛反应》，哪怕对足球了解不多，看两个人玩梗也看的很开心，4 年过去了，UP 主又更新了这个系列，可以持续的追一下，希望阿根廷/葡萄牙可以走远一点。最新的视频是：    
[《梅西C罗球迷观看阿根廷3比0阿尔及利亚比赛反应》](https://www.bilibili.com/video/BV19DLR6DELE/)   
[《梅西C罗球迷观看葡萄牙1比1刚果比赛反应》](https://www.bilibili.com/video/BV1kSjq6HEXm/)




## 碎碎念

* Paca，体型较大的啮齿动物，看着像是水豚和野猪的结合体。
* Gevent, subprocess, shell=True, Pipe, timeout ，这几个关键词在一起，就有故事和事故。
* 昨晚看开放麦的一个小观察，单口里面长得好看的演员变多了。
* 发现 macbook 的麦克风是在扬声器里面，所以如果日常关闭屏幕使用的话，需要额外的一个麦克风才行。
* 最近面临的一个问题：上次提到不提交 review 建议，而是直接提交 PR，但是我一口气提了 20 个 PR，PR 间的冲突变多了，经常调整完一个 PR 合并之后，其他的 PR 都需要先 rebase 一下，甚至都想一口气合并成一个了。。
如果在 gerrit 上我可以直接用 relation chain ，Github 就很麻烦。
* 突然发现前阵子提到的 bink 项目已经 transfer 到了 bootc-dev org 下了。
* 省会城市的身份证上是没有省的标识的
* 只有少部分省会城市是副省级城市
* 端午假期家里蹲。