---
title: Weekly Issue-《功夫女足》
date: "2026-10-25:00:00.000Z"
slug: "Weekly-Issue-Kung-Fu-Soccer"
tags:
  - Weekly
description:
---

## 文章

### 技术

[PingCAP TiDB Cloud Leaks](https://fulcrumsec.vg/pingcap/)

[Security Update – October 2026 Security Incident Report: Unauthorized Access to PingCAP Cloud Resources](https://www.pingcap.com/trust-hub/security/security-update-october-2026/)

[不正アクセスによる情報漏洩に関するお詫びとご報告 | TiDB](https://pingcap.co.jp/trust-hub/security/security-update-october-2026/)

> We even stood up a replication feed of their own control-plane database using credentials committed in their own repositories — GCP service-account keys and an Azure service principal — and let their infrastructure deliver it to us.

[[PingCAP]] 出现安全事件，记录下文章中一些数字：

- 57 个月的 AWS 名义成本是 1.07195 亿美元，折算每月 188 万美元；
- 企业协议折扣是 1035 万美元；
- 特定服务的费率折扣是 883 万美元；
- 跨 Zone 传输成本 1651 万美元；
- HubSpot（合同金额还是什么？）金额 5.52 亿美元；
- Stripe 用户数：8428；
- FY25 云配额：2943 万美元；（按照 30% 增长来预估的？）

PingCAP 的官方公告中，全球公告和日文公告有些差异，侧重点感觉也不太一样，可能和地方法规有关，发现了这些差异：

- 全球公告标题是安全事件报告，日本公告是信息泄露的道歉和报告；
- 全球公告提到了源代码泄露，日本公告没有；
- 全球公告提到特定用户记录，日本公告写五万名日本用户个人信息泄露；
- 全球公告提到了修复了 4 个漏洞，日本公告没有；

10 月 21 日 [[NebuSec]] 发布相关公告：[Investigating the PingCAP Security Incident: Credential Exposure and Cloud Data Collection | NebuSec](https://nebusec.ai/research/pingcap-security-incident/)

> The threat actor gained initial entry to the PingCAP environment via a compromised GitHub account, exposing private repositories. Utilizing compromised keys and tokens harvested from those repositories and Terraform state, the attacker pivoted into Google Cloud, Jira, and the enterprise internal IM used for TiDB alerts.

**a compromised GitHub Account**，不知道这位朋友还好么。

---

[FulcrumSec: The Cloud Extortion Group Behind 21 Victims and Counting](https://www.moxfive.com/blog/who-is-fulcrumsec-inside-the-cloud-extortion-group-behind-21-victims-and-counting)

> FulcrumSec is aggressive with extortion and wastes little time when organizations push back or go quiet. The group monitors victim communications and counters public statements directly, has named individual executives publicly, and is quick to post data when organizations don't cooperate. The tactics below are drawn from observed behavior, reported incidents, and the group's own published claims.

关于攻击 [[PingCAP]] 的组织 [[FulcrumSec]] 的描述，强硬派，只偷不加密。

---

[Security Disclosure: Wednesday October 21st | Railway Blog](https://blog.railway.com/p/security-disclosure-wednesday-october-21st)

[[Railway]] 安全披露，建议用户清除所有的环境变量，轮转所有的 API key。Railway 让用户轮转所有的 API key，但同时他们暂停了用户的应用部署，如果用户轮转 API key，用户的业务就会停止，死循环了。

[Preliminary Report: Oct 21st Security Incident](https://blog.railway.com/p/preliminary-report-october-security-incident)

> Railway's system is built so that if one set of keys is compromised, they should not compromise the entire system. As a result, we can validate that at most 1.85% of all workspaces had some environment variables potentially compromised. This represents, numerically, about 100,000 workspaces.

后续补充，1.85% 用户受到影响，10w workspace，实际上运行的全量 workspace 在 540w 左右。

---

### 生活

[抑郁了 – 代码家](https://daimajia.com/2026/10/18/depression/)

> 老大夫给我简单讲了一下我难受的根源，他说我可能有一些基础疼痛一直没有消除，疼久了以后对情绪产生了很大的影响，又反过来作用神经系统，放大了我的基础疼痛，导致疼痛变成了两部分，一部分基础疼痛，一部分情绪放大的疼痛。现在要吃药去消解神经系统带来的情绪部分的疼痛。   
> 因为自打 2023 年腰痛以来，感觉自己好多事情都没有办法做，坐上三四十分钟，就感觉难受的厉害，很多事情都没有办法去推进，有时候觉得挺遗憾的，在当打之年只能赋闲在家。

唉，不能以健康的人角度来考虑病患。

---

[介绍一家最近去的头马 Toastmasters 演讲俱乐部](https://www.owenyoung.com/toastmasters)

> 社会学家长期以来认为，人际关系的维系更多依赖于规律性，而不是亲密程度。我们最好的朋友经常是我们的同学，就是因为同学被强制放在同一个教室里好多年，天天见一个人，自动就熟悉了，这种环境是我们成年之后很难复制的东西。   
> 而头马的活动就刚好凑齐了这几个条件：**固定时间，基本固定的一群人，每个人都要当着所有人的面说话。** 来的人是各行各业的，我目前遇到过的有：地理老师、皮肤科医生、律师、开发者、服装设计、银行牛马、金融牛马、做播客的。

第一次听说这个组织，头马俱乐部，看上去还挺有趣的。

---

[「听不懂话」的销售](https://blog.solazy.me/20261020/)

> 如果今天他在电话里直接告诉我：「先生，重疾险因为涉及到健康告知和法定受益人，没领证确实没法代买，而且就算领了证，也需要她本人知情同意。您如果想悄悄给她一份保障，重疾险这条路走不通。」   
> 一句话就能把边界划清楚。既节省了我的时间，也证明了他不是个为了提成满嘴跑火车的混子。   
> 可惜大部分人算不明白这笔账。他们总觉得承认「不行」就是丢了单子，却不知道用虚假的承诺把客户骗进微信里，再用牛头不对马嘴的推销和越界的玩笑把人得罪光，才是真正断送了自己所有的潜在机会。

日常生活中，如果是闲扯淡侃大山，咋聊都行，如果真的聊事情，对方又一直东扯西扯，就会很烦了。很多人的沟通方式就是那样，也改不了。有一次和外人尝试用自己的方式来沟通，我只是让对方把事情交代清楚，就挨说了，被我妈说一句"你好好说话"，"态度不好"。

---

[蒙古东方省努木尔格草原火：日本主流媒体的 12 天](https://blog.ringsaturn.me/posts/2026-10-21-mongolia-fire-thoughts/)

> 我知道日本存在記者クラブ制度。媒体对一次信源的依赖可以解释一部分：KDDI 新闻室到 20 日没有发过任何东西，警察的调查结论也没有公布，记者手里没有可以引用的日方官方说法。但这只解释了为什么没有调查报道，解释不了为什么连转述都没有。一家日本上市公司 98.8% 持股的子公司，其日籍 CEO 在外国电视上公开道歉，这件事本身就是一条新闻，不需要等 KDDI 发公告。

> 我开始怀疑，在日本，新闻专业主义与调查记者这个行当是否还事实上存在着。我有些失望。

摆事实，列数据，给观点。记得学生时代听过一句话"我可以不说真话，但我不能说假话"，现在想来选择性的沉默也是很可恶的。20261025 更新，这个事情上了热搜。

---

[赛博火鸡的朝圣与献祭：当我们在大模型的铜墙铁壁外伪造人生](https://catcat.blog/2026/10/cyber-turkey-pilgrimage-and-sacrifice)

> 他们给那台远在大洋彼岸的电脑安排了一套无懈可击的"美国中产阶级人生"——它拥有纯净的住宅宽带、合规的北美账单地址、永不跳动的物理定位，以及全天候的英文系统环境。那个虚拟出来的美国人，活得比屏幕前蓬头垢面的宿主还要体面、还要地道。

> 在这个语境下，封号不再是一种冰冷的商业拒止或算法清退，而变成了一场因为"心不诚、礼不周"而招致的神罚。于是，"火鸡科学家"们应运而生。他们像中世纪研究赎罪券的神甫一样，通过九十九天的幸存者偏差，总结出一套又一套动辄上万字的《防封终极指南》。

> 只有那些散落在中文互联网各个角落里的远程桌面、指纹配置与防封秘籍，像一具具赛博时代的精致标本，无声地记录着这群"中国火鸡"曾如何倾尽全力，试图在别人的屋檐下，伪造出一场永不醒来的美利坚幻梦。

大家一边在尽可能的保护自己的身份不被偷，一边又在尽可能的去伪造另一个身份。

---

### 书影播客

[王师傅の日记的个人空间-王师傅の日记个人主页-哔哩哔哩视频](https://space.bilibili.com/3546619609876957/lists/9088094?type=season)

王师傅的 318 骑行日记结束了，这一路的风景要比骑行本身更美好。

[23梁田田：穿牛仔裤跑 800 米的女孩，成长为全国冠军。赛场外和场上有何不同？](https://podcasts.apple.com/us/podcast/23%E6%A2%81%E7%94%B0%E7%94%B0-%E7%A9%BF%E7%89%9B%E4%BB%94%E8%A3%A4%E8%B7%91-800-%E7%B1%B3%E7%9A%84%E5%A5%B3%E5%AD%A9-%E6%88%90%E9%95%BF%E4%B8%BA%E5%85%A8%E5%9B%BD%E5%86%A0%E5%86%9B-%E8%B5%9B%E5%9C%BA%E5%A4%96%E5%92%8C%E5%9C%BA%E4%B8%8A%E6%9C%89%E4%BD%95%E4%B8%8D%E5%90%8C/id1864918458?i=1000797433773)

梁田田是河南田径运动员，最近两届全运会女子 5000 米冠军，还有各种 10000 米冠军、半马冠军。围绕她的讨论挺多的，作为一个在所属项目中有绝对统治力的运动员，很多比赛采用的是跟随跑的策略，被说没有竞技精神，不敢突破自己，跑出成绩。这期播客发现她对于这些舆论并不在意，完全坚定的执行自己的战术策略，睡得好练得好，成绩自然好。


《功夫女足》，有阵子没有完整的看完一部电影了，翻了翻豆瓣的想看列表，我之前看过《少林足球》，也看过张卫健的《功夫足球》，那个时候的特效略微浮夸，但是在那个时候看还是很好看的。找来这部电影不带脑子看看，带着这样的预期，发现电影还是比我想象中更“小品”，剧情的起承非常的生硬，张小斐的演技没有演技可言（我没看过她的其他作品），迪丽热巴挺好的，没让我出戏，小师叔这个角色感觉换成魏翔会好一些。特效也很微妙，按理说技术进步了，但是这个电影的特效我仿佛在看仙侠片，不喜欢。 全片我记住的一个梗是：““队长，牛肉不用煮太熟”。




## 碎碎念

* TiDB 安全事件相关的帖子，日语含量极高。
* 202610，租一周四子星，15000 CNY，一个月 60000 CNY，这服务器厂商真是躺着赚钱，不到一年就回本了？
* 这次 PHP 的漏洞也是 Wiz （同时）发现的，印象中 Wiz 发现了很多高分漏洞了。
* CVE 和水浒卡似的，恨不得所有组件都要集齐。
* 突然得知有个同事明年就可以退休了，震撼
* "good opsec will save you from bad crypto. but the converse is not true, good crypto will not save you from bad opsec"
* 想到了 N 年前看到的代码中经常有 sync;sync;sync;reboot; ，现在我也写了类似的代码了： sysctl --system;sysctl --system ，真是朴实的方式。
* 感觉当前大部分 terminal 产品都没有考虑到 Devcontainer 场景。
* 20261022，今年的跑步距离超过了去年。
* 又是一年 1024，参加这么多年德扑比赛，今年终于拿到了个第三
* 想吃我奶做的韭菜馅饺子了
* 一两生煎，指的是生煎用的面皮的干面粉的重量是一两
* 快要 11 月了 上海的普通超市已经把冰柜撤下去了，不卖冰淇淋了
* “队长，牛肉不用煮太熟”
* 高山红薯好吃，烟薯不好吃。
* 周末去参加了狂喜播客节，是通过单立人的活动报名的，免了门票，见到了一些日常听播客的主播：吕东、Storm、钱粮胡同的野人、电影最 TOP 的老张。