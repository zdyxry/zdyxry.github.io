---
title: Weekly Issue-栖霞山
date: 2024-12-01
tags:
- Weekly
description:  
---


## 文章

### 技术


[1 dataset. 100 visualizations.](https://100.datavizproject.com/)

100 种[[可视化]]图表。合适的图表比文字更适合叙事。

---

[Dear friend, you have built a Kubernetes](https://www.macchaffee.com/blog/2024/you-have-built-a-kubernetes/)

> A standard config format, a deployment method, an overlay network, service discovery, immutable nodes, and an API server. Dear friend, you have built a Kubernetes.

对于大部分人来说，即使自己搞了这么多东西，在出现问题时，排查起来的速度应该会比 K8s 快很多，维护成本也会低很多？资源消耗也会低？

---

[I Didn't Need Kubernetes](https://benhouston3d.com/blog/why-i-left-kubernetes-for-google-cloud-run)

跟着上面这篇一起关联阅读，作者从根本上需要的就不是 k8s, 作者需要的只是运行几个 container 的“东西”, 至于是什么把作者们运行起来的，作者不关心, 现在只是 google 帮作者运行起来了, 作者交钱而已 , 作者说 k8s vendor-lock , google 更是 vendor-lock, 作者说 k8s 需要很多的运维知识，作者现在只是掏钱给 google 运维。

---



[Future Crate Maintenance and Redis Inc. Relationship · Issue #1419 · redis-rs/redis-rs · GitHub](https://github.com/redis-rs/redis-rs/issues/1419)

[[redis]] 公司联系项目 owner，说 Rust Redis crate 侵犯了 redis 的商标。改名或者将其转移到 Redis Inc 。关注下后续进展。

2024 年 12 月 2 日更新：看样子暂时不会发生变更了： https://github.com/redis-rs/redis-rs/issues/1419#issuecomment-2503578646 。


---

[Mozilla: DOJ's Plan for Chrome Risks Hurting Smaller Browsers | PCMag](https://www.pcmag.com/news/mozilla-dojs-plan-for-chrome-risks-hurting-smaller-browsers)

司法部说 Google Search 垄断，让 Google 出售 Chrome，同时禁止 Google 给第三方公司付钱将 Google Search 作为默认搜索引擎，Mozilla（2022 年默认搜索引擎收入占比 86%） 跳出来说，这可能反而会损害其他独立浏览器公司，希望能调整。

---

[How I configure my Git identities | benji](https://www.benji.dog/articles/git-config/)

[[git]] 技巧，使用 `includeIf` 来针对不同的 repo 使用不同的配置， git config 示例：

```
[includeIf "hasconfig:remote.*.url:git@github.com:orgname/**"]
  path = ~/.config/git/config-gh-org

[includeIf "hasconfig:remote.*.url:git@github.com:*/**"]
  path = ~/.config/git/config-gh
```

对于同一个 Host 使用不同的 SSH 配置，在 ssh config 和 git config：

```
# ~/.ssh/config
Host gh-work
Hostname github.com
User git
IdentityFile ~/.ssh/work.id_ed25519
# ~/.gitconfig
[url "gh-work:orgname"]
  insteadOf = git@github.com:orgname
```

---

[Deno v. Oracle: Canceling the JavaScript Trademark](https://deno.com/blog/deno-v-oracle)

[[Deno]] 上次 JavaScript 商标后续，Deno 想 USPTO（美国专利局）申请撤销 Oracle JavaScript 商标。

Deno 的推文中的语句是： `Oracle has until January 4th to respond, or the case will go into default, which will result in the trademark being canceled.`
在博客中的语句是： `Oracle has until January 4, 2025, to respond. If they fail to act, the case will go into default, and the trademark will likely be canceled.`

`likely` 被吃了？是故意的还是不小心？我还是对于 Deno 这些行为保持怀疑的态度。

---

[Getting a pointer to a constant in Go - Xe Iaso](https://xeiaso.net/notes/2024/go-pointer-constant/)

我最近使用 `lo.ToPtr` 来做这件事。`raised := &[]string{"foo"}[0]` 可不太好。。。 

---


[Why pipes sometimes get "stuck": buffering](https://jvns.ca/blog/2024/11/29/why-pipes-get-stuck-buffering/)

这篇文章的起始问题时：为什么 `tail -f /some/log/file | grep thing1 | grep thing2` 有时候会没有预期的输出。作者调查了常用程序的 buffer 情况，比如 grep 会根据自己的 stdout 是否为 terminal 来决定是否启用 buffer。libc 的默认 buffer size 是 8k。提到了一些避免 buffer 的方式：
- 记住常用命令的参数，比如 `grep --line-buffered`
- 使用 `stdbuf` 关闭 libc buffer
- 使用 `unbuffer` 强制将程序的输出置为 TTY

配合阅读，stderr 在很多语言的标准库里是 unbuffered 的： [Why stdout is faster than stderr? - Orhun's Blog](https://blog.orhun.dev/stdout-vs-stderr/)

---

[Testing with Go and PostgreSQL: ephemeral DBs - Michael Stapelberg](https://michael.stapelberg.ch/posts/2024-11-19-testing-with-go-and-postgresql-ephemeral-dbs/)

通过使用 inipg 独立的命令来启动一个共享 PG 实例运行单测，不需要引入 Container，但是需要运行单测的实例上存在 PG binary。

---



### 生活

[个人消费主义的迷思](https://blog.sailfishc.com/buy)

因为我日常几乎没有什么特殊的开销，一年网购的次数可能不超过 10次，90% 的场景只有衣食住行，所以当有特殊开销的时候，就会略微的谨慎一些。

---

[不要在危墙之下寻找商机 · 新钱](https://money.otakusaikou.com/2024/11/24/dont-look-for-opportunities-under-a-dangerous-wall/)

> 那么到底什么样子的市场算是「好市场」呢？
> 1. **好的市场应该是规则透明，公平竞争的**
> 2. **好的市场应该是能够自由交易的，可以丰富的选择**
> 3. **好的市场是会监管严格，保护投资者的**

看到很多人说基金定投，分别投不同的行业，为了不让“鸡蛋放在一个篮子里”，但这些篮子可能在一辆车里，有时候可能车的选择更重要。

---

[年轻的中国数字游民，「迷失」在东南亚 - Foresight News](https://s.foresightnews.pro/article/detail/72663)

> 就像格瓦拉骑着摩托游历南美大陆时在他日记本写下的：「我觉得现在的自己，跟刚出发时的自己相比，变得不一样了。」数字游民们也有所谓「人生时刻」。    
> 久居城市的打工青年们厌倦了三点一线、一切向钱看齐、意义感缺失的生活，他们焦虑未来，丧失着当下；在能轻易实现咖啡和兴趣爱好自由的清迈，也有不少游民们在颠倒的日常作息中混乱度日，徘徊在咖啡厅与酒吧。    
> 清迈有宁曼路上颇具小资情调的精致共享空间，也有萍河附近低矮老旧的小楼漆黑的房间，就像西方白人拿着高汇率货币，上着西方高新福利企业的班，完成他们的「地理套利」。在清迈不同文化阶层的数字游民们也有着自己的旷野和轨道，只不过有的人出生就在他人眼中的「旷野」。
> 正如法国作家埃里蓬所言：「这个我曾极力逃离的地方：一片我曾刻意疏离的社会空间、一片在我成长过程中充当反面教材的精神空间，也是无论我如何反抗，依然构成我精神内核的家乡。」
> 而大部分人，模糊的感到自己因为工作这么开心已是很久前的事情。现在，人们对日常的当下容易感到不耐，认为更好的生活一定在将来。最后，在一个又一个干涸凝固的日夜里丢下工作、落了朋友，茫然四顾。
> 

---

[花束般的恋爱 • Usubeni Fantasy](https://ssshooter.com/we-made-a-beautiful-bouquet/)

> 在走岔之后还是另一个问题就是缺乏沟通，他们的内心独白跟对方不一样之后，也没有把真正想表达的东西传达给对方。

无论什么事情什么时候，可以沟通都是一项很重要的能力，如果一个人无法沟通（可能是不沟通，也可能是沟通的方式不一致），那就无法继续。

---

[一年住 7 晚酒店的你，真的需要酒店高级会员吗？ - 少数派](https://sspai.com/post/94079)

> 省流版本：
> 预算 1-1000 元和入住天数 1-7 晚：携程、飞猪、房卷等，怎么便宜怎么来；   
> 预算 600-1000 元和入住天数 8-15 晚：可参与会员计划，显著提升住宿体验；    
> 预算 1000 以上或 17 晚及以上：随意。   

---



## 书影

《素食者》，韩江。压抑，这种压抑和读金爱烂的压抑是不一样的，金爱烂笔下的故事痛苦来的很直接，来得快去得快，这本书的故事是越想越压抑。身份认同、社会压力、个体反抗，他人在遇到这种情况时的困惑、不解以至于最后的回避。读完之后问自己一个问题：如果英惠是我的朋友，我应该如何与之相处？我可能会尊重ta 的选择，但是最终可能也会远离回避。如果不回避呢？怎么做？



## 碎碎念

* 得知一个朋友在四川乐山旅居生活，第一反应是羡慕，第二反应又在想，我在羡慕什么？
* 很多时候对某件事只有一个模糊的感觉或者想法，是因为自己没有能力去想清楚这件事情。
* 发现 google 搜索最近不索引我的博客了，导致搜索都麻烦了，得查查是怎么回事
* 听到了一个烂梗：米的妈妈是谁，花生米。花的妈妈是谁，妙笔。
* 沪漂的时间超过了北漂了。
* 什么叫“老中人”，为什么一口一个老中人？
* 吃饭的时候和同事关于《好东西》 中胡医生是否是渣男的讨论，我和其他人的看法不同，写一下我的想法：   
    * 首先定义“渣男”：百度百科中，通常指男性中一类对待异性之间感情不认真、玩弄对方感情（尤指恋情）的男人。《渣男鑑定手冊》中，所說的「渣男」是指「為對方的精神帶來不良影響，害對方喪失自信的男人」。《好东西》中，胡医生算渣男么？胡医生不想有感情，不想进一步，胡医生玩弄感情了么？如果同样的反过来，王铁梅的”课间十分钟“，王铁梅对小马也是渣？是我的道德标准下降了？我觉得没有，我觉得恰恰是我的道德标准在这里（臭不要脸），所以对于给一个人下定义这种事情是抵触的，哪怕是电影中的角色。
* 我现在看到“正直勇敢有阅读量”，本能的想远离。在南京先锋书店，有一个分类叫“她”，人非常多，我以为都在买书，书没拆封，也看不了，结果发现都在摆拍，看过几本上野千鹤子不知道，拍过倒是不少。

## 栖霞山

之前的碎碎念有提到，上海的秋天很晚，且没什么刻板印象中的秋天，所以就想要寻找秋天，选择的是南京的栖霞山，之前小红书已经看了很久，找个周末去一下。其实很早想去了，但是一直担心枫叶还没有红，等到了这周。上海到南京最快的高铁只要 1h，还是很方便的。因为是一个人，所以不着急，慢慢悠悠的坐地铁公交，我已经很久没有坐那么挤的公交了。栖霞山现在是旺季，门票 80，人非常多，上山都要排队，我上一次爬山还是上海的佘山（如果也可以称为山的话）。

放一些拍的照片。

![](https://oss.zdyxry.com/20241130-nanjing-1.jpg)

![](https://oss.zdyxry.com/20241130-nanjing-2.jpg)

![](https://oss.zdyxry.com/20241130-nanjing-3.jpg)

![](https://oss.zdyxry.com/20241130-nanjing-4.jpg)

![](https://oss.zdyxry.com/20241130-nanjing-5.jpg)
