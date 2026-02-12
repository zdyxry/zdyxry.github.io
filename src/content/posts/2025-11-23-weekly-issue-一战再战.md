---
title: Weekly Issue-《一战再战》
date: "2025-11-23T00:00:00.000Z"
slug: "Weekly-Issue-一战再战"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Incident Report: September 22nd, 2025](https://blog.railway.com/p/incident-report-sept-22-2025)

> During a code cleanup, we made a database schema change to remove an unused column. However, a subsequent code change reverted part of this unintentionally, leading to failures for a core API our frontend relies on.

> Further investigation revealed the issue stemmed from a PgBouncer version upgrade. Our Control Plane database relies on PgBouncer as a connection pooler, common in most applications for managing Postgres connections at scale.

> We had been using an older Bitnami image, and following [Bitnami's deprecation of their public images](https://github.com/bitnami/charts/issues/35164), we migrated to our internal mirrored repository. This migration advanced us several PgBouncer versions ahead.

[[Railway]] [[事故分析]]。DB schema 变更因为“不小心”被 revert 了，控制面崩了，控制面崩了发现是 PgBouncer 资源消耗异常，原来是因为 [[bitnami]] 不维护公开 image 了，所有他们迁移到了内部的 repository，但是这次迁移并不只是“迁移”，而是将 PgBouncer 升级了几个版本。。。这两个变更咋能通过 review 上线的呢？

当然，如果要调侃的话，可以说一句：“博通罪大恶极”。

---



[Cloudflare outage on November 18, 2025](https://blog.cloudflare.com/18-november-2025-outage/)

[Rust 背锅了：Cloudflare 故障分析 | CatCoding](https://catcoding.me/p/rust-in-cloudflare-incident/)

[从 Cloudflare 故障到代码安全 | Cyandev](https://cyandev.app/post/from-cloudflare-outage-to-code-safety)


[[CloudFlare]] [[事故分析]]，这是它们自 2019 年以来最严重的故障，故障原因已经写的很清楚了，各种分析也很多，很多人开始玩梗来说 [[Rust]] blabla，看到这类言论感觉和那种营销号标题党没有差别，太无聊了。

这里有一个有意思的地方，[[CloudFlare]] Status 站点与 Cloudflare 自身所有资源都是隔离的，但是当主站故障的时候，Status 站点也刚好故障了。。。这应该是误导他们认为是 DDOS 的一个原因？不知道这里的故障原因是什么，文章中没有提到。

---

[Monitor These 5 Metrics to Prevent Downtime](https://dzone.com/articles/stop-reactive-network-troubleshooting)

1. **RTT 变化**：RTT 的细微增加通常预示着更严重的网络拥塞。
2. **缓冲区使用率**：监控关键网络设备的缓冲区使用情况可以揭示即将出现的瓶颈。
3. **接口错误率**：CRC 错误或接口丢弃的少量增加可能预示着硬件故障。
4. **TCP 重传率**：此指标表明了用户可能遇到的应用程序性能问题。
5. **网络流量对称性**：异常的非对称流量通常表明安全问题或应用程序配置错误。

---

[原地报废：不要在生产环境用 Docker 跑PostgreSQL！ · 老冯云数](https://vonng.com/db/no-docker-pg/)

> **为什么会这样？原因其实很简单、也很离谱：**
> 1. Docker 官方 PG 镜像只支持 **两个 Debian 版本**
> 2. 当 Debian 发布新版本时，只要你没明确指定 debian 版本标签，它会 **自动变成新的默认基础镜像**
> 3. 新的 Debian 版本用了 **新版本的 glibc**
> 4. Glibc 更新后，**locale（排序规则）文件发生变化**
> **于是你现在的状态变成：**
> - 运行的 PostgreSQL **链接的是一套 locale 文件**
> - 而数据库里的数据与索引 **是基于另一套旧的 locale 文件生成的**

再次坚定：指定 tag 甚至指定 hash 总是没错的。

原来 PG 的 dockerhub 里面的 Official Image 主语是 [[Docker]]，不是 PG 社区自己维护的......

---

[Top 200 Most Common Passwords | NordPass](https://nordpass.com/most-common-passwords-list/)

"123456" 还是当前最常用的软密码，排名 129 的是 “theworldinyourhand”，这是什么软件的默认密码么？排名 143 的是 "cisco"。

---



### 生活

[我的欧洲生活 – 挪威篇 | 土豆不好吃](https://dmesg.app/europe-no.html)

>也许是被统治惯了，不想再被别人管，挪威没有加入欧盟，却是北约的创始成员国。为了与欧盟国家保持良好关系，它又加入了欧洲经济区（EEA），并签署了申根协定。   
> 顺便说一句：欧盟、申根区、欧洲经济区、欧元区、北约 —— 这五个其实完全是不同的概念。

> 欧洲急需新的能源供应，而挪威成了最大的赢家：石油、天然气出口暴涨，财政收入创下历史新高，更别提那个神话一般的 “主权基金” 了。    
> 挪威是世界上最大的三文鱼出口国之一，海水寒冷而纯净，养出的鱼肉鲜嫩肥美。

---

[剪影-姥爷-Himself65](https://www.himself65.com/blog/mother-father)

> 我姥爷可能绝大部分人生都在研究彩票上。
> 
> 我出国留学后再也没见到过他，对我来说只是一个普通的夜晚，我妈给我发来消息：“你姥爷去世了”，随后是一片沉默；几年后，我妈来国外旅游和我聊天，心血来潮，说他最后说在病床前楠楠道，想来出国找我。   
> 我想，这可能比彩票中奖还要难。

写的真好，读的难受。

毛冬的一个说法我非常认同，大家可以在自己长辈还健在的时候，多拍照，多录音录像，可能现在觉得没什么，也许有一天你突然就想起来了，会想看看的。

---

### 书影播客

《一战再战》，笑了么？笑了。看懂了么？没看懂。只能说是大概知道在讲些啥，但是细节上就完全不清楚了。感觉西恩潘可以再得一次奥斯卡。

不怕剧透可以看这篇影评： [把左派、右派，都骂的狗血淋头](https://archive.is/j4Vo0)

《我们的箱根驿传》，2025 年 8 月出版的书，在上海书城看了开头，作为相关信息的了解是不错的选择，想要当场买，结果书城 65，淘宝 24，果断选择淘宝。

《没理想编辑部-Vol.202 对话土豆：喜剧不能总是取最大公约数啊》，这期对土豆的采访有趣，土豆是个有趣的人，随口抛出的梗都很难接住。这一季喜人他最后悔的，应该就是没有坚持自己的想法，选择了“保底“。

[《【Reaction】华莎 x 朴正民 'Good Goodbye' 祝贺舞台演员反应｜第 46 届青龙电影节｜251119》](https://www.bilibili.com/video/BV19VU5BDE6S)

周末的快乐是这个视频给的，第 46 届青龙电影节，华莎演唱自己的歌曲《Good Goodbye》，这首歌的 MV 男主是朴正民，在青龙的现场有一个小小的互动，台下都是韩国最会演戏的演员，大家的反应很真实很有趣，都是姨母笑，都磕到了。


## 碎碎念

* 公众号可以用账号密码登录，但是每次都要二次校验微信扫码，那还有什么用。
* 周末在图书馆找书，按照检索结果死活没找到，上上下下爬了 3 次。
* Ampere Computing 在 2025 年 3 月被软银以 65 亿美元收购。
* 最近很喜欢用实际功能的用户数量来作为参考纬度，进行一些取舍判断。
* 最近看到了两个项目名称挺有趣的：Yansu、Tansu。
* 我一直不知道自己用的什么字体。
* Windows 有 icon cache，如果更新之后，需要手动清理才行。
* Slack 也退出了：We are writing to let you know that due to changes in how Salesforce services are provided in mainland China, Slack will no longer be renewing your workspace.
* 善用 block，让生活更美好
* 越看各个网络安全公司的现状，越觉得深信服很厉害，用 Gemini DeepResearch 进行的调研总结：
    * 通过 HCI 平台，深信服成功地将自身产品从传统网络边缘的 “附加安全设备” 升级为数据中心内部的 “原生安全能力” 1。这种技术融合不仅增强了客户粘性，更重要的是，使其营收来源从周期性、偏向 OPEX（运营支出）的安全预算，扩展到了基础性、强制性的 CAPEX（资本支出）基础设施预算，从而在整体市场上占据了更大的份额。
    * 这种战略上的定位转移，使得深信服能够从传统安全产品的 “高利润率、低天花板” 困境中跳脱出来，转向基础设施平台 “低利润率、高成长性” 的赛道。尽管基础平台业务的短期毛利率较低，但它能带来极高的客户粘性，并保障了未来在高价值安全服务上的持续收入。
* 今早的跑 13 km，速度不快，心率也不高，但是体感很差，可能是湿度的问题么，还是上海的空气质量太差了？
* 金爱烂的书在上海书城卖断货了，好事。
* 疯投圈：国内的茑屋书店都是加盟的。
* 最近李逗逗的黑脸导师系列突然火了起来，想起来有一次在上海话剧中心看演出，还和她互动过。
* 听播客知道 Hoka 例跑活动可以试鞋。
