---
title: Weekly Issue-告诉别人你可能过得不好，是善良吗
date: "2024-06-02T00:00:00.000Z"
slug: "Weekly-Issue-告诉别人你可能过得不好是善良吗"
tags:
  - Weekly
description:
---

## 文章

### 技术


[Cloudflare took down our website after trying to force us to pay 120k$ within 24h](https://robindev.substack.com/p/cloudflare-took-down-our-website)

[[CloudFlare]] 要求客户在一周内（24h 内）将付费计划从 250 `$/M` 提升至 10 k `$/M` ，在得知该客户有 [[Fastly]] 进行谈判时，清楚了该客户的所有域名，导致业务宕机。

无论 [[CloudFlare]] 后续的反馈如何，这里的沟通方式和处理方式，都有些粗暴。截止到目前，Cloudflare 还没有对这件事发表回应。

---

[I Sold TinyPilot, My First Successful Business · mtlynch.io](https://mtlynch.io/i-sold-tinypilot/)

[[TinyPilot]] 的创始人把它卖掉了，卖掉的价格是 2.4 倍的年收益，TinyPilot 项目整体带来的利润是 4 年 920 k$ 。
主要的原因是运营一家公司涉及到了大量的杂事，虽然 TinyPilot 只占用了 20% 的时间，但是却带来了 90% 的压力，加上创始人马上就要当爸爸了，所以他打算换一个方向。

---


[Three Laws of Software Complexity (or: why software engineers are always grumpy) | mahesh’s blog](https://maheshba.bitbucket.io/blog/2024/05/08/2024-ThreeLaws.html)

软件复杂性三定律：
- 随着时间的推移，设计良好的系统将退化为设计糟糕的系统；
- 复杂性是一条护城河；
- 软件复杂性没有基本上限

在这样的场景下，我们能做什么呢？作者采取从零开始构建新的系统的方式，但是现实往往不可能。

---
[DuckDB Doesn’t Need Data To Be a Database](https://www.nikolasgoebel.com/2024/05/28/duckdb-doesnt-need-data.html)

假设你经营机器人出租车服务。在 Blob 存储中维护一个不断增长的骑行模式数据集，希望更好地了解这些数据。每天的数据被分割成一个单独的 Parquet 文件。如何与分析师共享该数据集？

可以使用 DuckDB 来共享，所有的真实数据都在 `S3` 中，DuckDB 支持部分读取，所以真实的流量应该也不会很大？

```
# Send
import duckdb
db = duckdb.connect("weird_rides.db")
db.sql("""
    CREATE VIEW weird_rides
    AS SELECT pickup_at, dropoff_at, trip_distance, total_amount
    FROM 's3://robotaxi-inc/daily-ride-data/*.parquet'
    WHERE fare_amount > 100 AND trip_distance < 10.0
""")
db.close()
```

```
# Receive
import duckdb
conn = duckdb.connect()
conn.sql("""
ATTACH 's3://robotaxi-inc/virtual-datasets/weird_rides.db'
AS rides_db (READ_ONLY)
""")
```

---

[Install Proxmox in VMware Workstation Pro - Virtualization Howto](https://www.virtualizationhowto.com/2024/05/install-proxmox-in-vmware-workstation-pro/)

Yes, but why ???

---

[docs: proposal to raise awareness about an unexpected behavior of COPY --link · Issue #4964 · moby/buildkit · GitHub](https://github.com/moby/buildkit/issues/4964)

[[Dockerfile]] `COPY --link`  会导致文件权限不符合预期，使用的时候需要注意下。

---

[Big Data is Dead](https://motherduck.com/blog/big-data-is-dead/)

大多数人没有那么多数据，BigQuery 的数据存储中位数远低于 100GB；存储和计算的偏差，可能有很多数据，但是不需要那么多的计算资源；真实查询的数据远小于总体数据大小，拥有大量数据的客户几乎从来没有查询过大量数据。

---

[Instead of "auth", we should say "permissions" and "login" | nicole@web](https://ntietz.com/blog/lets-say-instead-of-auth/)

非常认同， auth 这个词加上 auth 的扩展 authz 和 authn，每次和同事讨论的时候都非常头痛（甚至不了解背景的同学会以为 authn 是 typo）。有时候使用一些看似不那么“专业”的词反而会更清晰。

---







### 生活

[The Demanding Modern Society - laike9m's blog](https://laike9m.com/blog/the-demanding-modern-society,157/)

>我最近时常感到，虽然我们的生活越来越便捷，但需要考虑的事情却越来越多。

我觉得更多的是因为我们现在获取信息的方式太容易了，相较于父辈，我们无论是获取渠道还是获取质量，都比之前好很多，虽然还是存在很多信息差，但是已经相对的透明了。所以我们可以知道前人不知道的一些信息，这些信息导致我们不得不进行相应的思考。

人际关系是烦恼的根源，我不觉得 AI 会是解决方案，可能倾向于社会学相关的讨论能够帮助思考更多的人解惑。

---

[MXY-7樱花特别攻击机 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/MXY-7%E6%AB%BB%E8%8A%B1%E7%89%B9%E5%88%A5%E6%94%BB%E6%93%8A%E6%A9%9F)

>樱花导弹之所以是针对自杀式任务而设计的飞机，是由于樱花导弹内的战斗部是与弹体连为一体，不能分离出来，所以要炸毁目标，樱花导弹本身必须与目标同归于尽。

是什么样的信念，能够让人驾驶这样的飞机去战斗？可怕。

---

[告诉别人你可能过得不好，是善良吗](http://web.archive.org/web/20240528002719/https://www.douban.com/note/846000232/?_dtcc=1&_i=6855838BlBAZ-O)

>这几天我思考的问题是，那些提醒别人你们可能过得不好的人，是善良的人吗？这个问题真的不好回答。
>我有一个已经被很多人批评的观点，但我还是打算写在这里：一旦金钱超过了生活必需，很多人就会消耗大量不必要的资源，这会产生一种只要我富有，我就能拥有一切的错觉。

---

[Trying to buy a house is 'playing a game you can't win' - BBC News](https://www.bbc.co.uk/news/articles/cmj66r4lvzzo)

>这位来自犹他州的 32 岁保险理算员表示，他和他的妹妹赚的钱比以往任何时候都多。但每月支付 2,500 美元（1,960 英镑）的租金所剩无几。
>自 2019 年底以来，美国房屋销售中位数价格上涨了近 30%，今年春季达到 42 万美元。
>这还不包括利率上升带来的额外成本，目前美国典型的 30 年期固定利率抵押贷款利率约为 7%，而 2020 年约为 3%。
>Zillow 和 Bankrate 等研究公司表示，如今的购房者需要年收入超过 10 万美元（远高于美国家庭中位数约 75,000 美元）才能在美国大部分地区舒适地买房，而每月还款额大约增加了一倍短短四年内。

我理解一下，中国政府的财政收入主要来源于土地，所以地价越高，收入越多，所以房价上涨，带来的问题是房地产泡沫，因为房子不值那么多钱。
美国呢？美国的房价上涨，没有房地产泡沫么？不会再次出现《大空头》么？

---


[黑噪音｜“年轻网络暴民”，正在毁掉中国年轻人](https://chinadigitaltimes.net/chinese/708325.html?utm_source=dlvr.it&utm_medium=twitter)

>**因为年轻网络暴民，他们不仅不相信民间的批评，也不相信权威——这恰好就是暴民的特质，他们只相信自己愿意相信的。说到底，他们只相信一种集体的狂热情绪。**

---

[我「接见」了诺奖得主 - Frost's Blog](https://frostming.com/2024/meet-with-paul/)

> 当佬巨到一定程度，他是向下兼容的。
> 见面之前，他发了很长的一封信介绍他的相关背景，以及计划要谈的话题。即使地位悬殊，年龄悬殊，他依然恪守了基本礼仪，让未来的见面能顺畅进行。我不想因为他是大佬就拼命溜须，但这种谦恭的态度真的让我学到了很多。

---

[运气与努力 || 0x01 byte](https://1byte.io/articles/luck/)

>商业模式往往是以某种信息不对称为基础。互联网消除了很多信息上的不对称后，就有人人为制造出一种信息不对称的错觉和神秘感。卖成功学的人往往要用各种理论包装一番，因为如果看起来很简单就无法赚钱。成功的要点单伟建和 Charlie Munger 的几句话已经总结得很好，简单但不容易，如果能长期坚持就会比大多数人成功。

日常的努力可以让你在运气来的时候有不错过的可能。

---



## 书影

《被讨厌的勇气》，听没理想编辑部播客的时候听他们聊了这本书，读读看，其中提到过的一些想法是已经从其他信息中了解过一些的，期待读完之后会有一些新的感悟。

## 碎碎念

* 焦虑的反义词是具体
* >我已记不清是些什么事。反正，有段日子生活对我们不好，我们也没更多的心力去关照家畜们。似乎我们成了一个周转站生活对我们好一点，我们给身边事物的关爱就会多一点。我们没能像积蓄粮食一样在心中积攒足够的爱与善意，以便生活中没这些东西时，我们仍能节俭地给予。那些年月我们一直都没积蓄下足够的粮食。贫穷太漫长了。
* 发现 Nutanix 股价历史新高了，业绩真强劲啊，也许慢慢大家会发现退出中国其实也没什么影响？
* 一个组老板的说话风格，决定了组员的说话风格，比如我司一个组，现在遇到问题之后，会说：“XX 来感受一下吧” 
* 工作狂人会给其他人带来明显的压力啊
* 触发了微信读书的书籍导入限制，那我也不开会员。
* 为什么我不想给食贫道充电呢？因为它对我不重要。哪怕如果支持的人少，食贫道这样的长视频频道消失嘞，这件事本身对我不重要，所以我不给他充电，与他的视频做的好不好没关系，对我来说，视频这个领域做的好与坏，都不重要。

