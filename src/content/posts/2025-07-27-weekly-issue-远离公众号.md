---
title: Weekly Issue-远离公众号
date: "2025-07-27T00:00:00.000Z"
slug: "Weekly-Issue-远离公众号"
tags:
  - Weekly
description:
---

## 文章

### 技术

[HTTP QUERY and Go](https://kmcd.dev/posts/http-query/)

[[HTTP]] `QUERY` 方法，一种介于 `GET` 和 `POST` 之间的查询方法，允许在 request body 中携带复杂的 query 语句。等真正能用上估计要很久以后，大概率永远也用不上。

---

[The strange case of ICMP Type 69 on Linux](https://blog.benjojo.co.uk/post/linux-icmp-type-69)

10 年前的文章，问题也早已经修复了，但是看 debug 过程还是很有趣的。

作者在自己的服务器上运行 `collectd` 采集监控数据，发现有很多 ICMP `OutType69`，但是 `69` 不是一个有效的 ICMP 类型，于是进行了调查。

当统计 ICMP 出站消息时，代码使用了 `((struct icmphdr *)skb_transport_header(skb))->type` 来获取 ICMP 类型。对于一个 IPv4 数据包，`skb_transport_header(skb)` 返回的是 IP 头部的起始地址。ICMP 头部应该在 IP 头部之后。当代码直接将这个 IP 头部的起始地址强制转换为 `icmphdr` 结构体并尝试读取 `type` 字段时，它实际上读取的是 IP 头部的第一个字节。

IP 头部的第一个字节中：前四位是 IP 版本（通常是 `0x4`），后四位是 IP 头部长度（IHL，通常是 `0x5`，表示 5 个 32 位字，即 20 字节）。当这两个半字节组合在一起时，形成了字节 `0x45`，其十进制值是 69，IP 头部的信息被错误地解析成了 ICMP 类型 69。

---

[Lovable went from $1M to $100M ARR faster than any other software company in history.](https://x.com/antonosika/status/1948073116984652052)

[[Lovable]] 的 ARR (年度经常性收入 ）从 $1M 到$100 M 的速度超过了 [[Cursor]]。

榜单上分别是：
- [[Lovable]] 8 个月
- Cursor 1 年
- WIZ 不到 2 年
- OpenAI 2 年
- Slack 3 年
- ...

有一点我没搞懂，在现在 AI 产品及应用变化这么快的情况下，讨论 ARR 合适么？真的是 recurring 的么。

让 Gemini DeepResearch 了一些常见软件的复购率（不完全等价，用做参考）：
* Salesforce 92%
* Nutanix 110%
* HubSpot 115%
* 深信服 （没查到

---


### 生活

[＃5 - 近日找工作趣事二三则](https://polebug.github.io/2025/07/20/plog_5_job_hunting_anecdotes/)

网上还是好人多啊。

---
[云风的 BLOG: 慢跑](https://blog.codingnow.com/2025/07/jogging.html)

> 目前身高 187 ，大学毕业时大约 183 ，后来 20 多年陆续又长了几厘米。

原来有人大学毕业后还能继续长高的，希望我也能长高几厘米。

---

[How GLP-1s Are Breaking Life Insurance](https://www.glp1digest.com/p/how-glp-1s-are-breaking-life-insurance)

> Life insurers can predict when you'll die with about [98% accuracy](https://www.soa.org/4aa060/globalassets/assets/files/resources/research-report/2024/rpec-mort-improvement-update.pdf?utm_source=chatgpt.com).

有趣，[[GLP-1]] 对保险公司的影响很大，因为复用了 [[GLP-1]] 之后，对于保单评估是有很大的误导性，而当前 [[GLP-1]] 停用后大概率会反弹。

---

[史上最热夏天，冰淇淋却卖不动了](https://archive.is/b5LSa)


> 「当气温超过30摄氏度，人们就只想喝饮料，水和软饮料的需求量会超过冰淇淋，25或26摄氏度对冰淇淋的销量更好。」

雪糕卖不动，评论区都在说糖太多不健康，但大家奶茶喝的还是起劲的。

---

[今年暑期，自驾游干翻酒店、旅行社](https://archive.is/9xtvH)

> 不少人是睡车上的，还有直接支帐篷的，就住在露营地边上或者景区停车场，除了我们这些包价团客，大部分自由行和自驾游的人，压根不进酒店。”

> 当旅游消费悄然转向，显然**这届游客已经穷得越来越精明了。**

---

[裸辞的年轻人，把尼泊尔躺成大理「平替」](https://archive.is/VW6TA)

> 跳跳在尼泊尔认识的中国年轻人，几乎都是“工作得不如意”的，不是被裁员的，就是裸辞的。月亮遇到的和自己同龄的中国女孩，也基本都是裸辞的，“对上一份工作很厌倦，想要出来玩一会儿”。

> 但在尼泊尔，没有人会和跳跳谈论工作，大家不是裸辞人士就是失业人士，“我们都是世俗意义上的那种失败的，谁好意思谈？”至于那些财富自由来尼泊尔旅居的，更不在乎工作如何了，“而且大家都觉得出来了，别谈国内的那种事情。”

尼泊尔不重要，（相对）低成本无压力的社交环境比较重要。

---

[东亚第一「性压抑」国，穷人不配结婚](https://archive.is/g7luj)

> 人们以为只要一路努力——上大学、找工作、买房子、结婚——幸福就会自动到来。但事实呢？
> 学历不错、收入却不高的男人，结不了婚；
> 学历高、收入也高的女人，依旧结不了婚。
> 在城市里结婚难，在地方上更难。

为啥结婚 `==` 幸福。

集中看了几篇最近微信公众号推荐的文章，这些文章有些相同的共性，经济下行、生活成本高、生活方式转变。无趣，我觉得这类文章有一个问题就是只描述当前的困境，让文章阅读者找到自己“所属”的群体中，当一个共同体名词潮流过去之后，会有下一个名词产生，这些都不解决问题：经济压力大 -> 消费降级 -> 价值观转变。然后呢？会有人说“大家只想追求情绪价值”。“情绪价值”，情绪价值到底是什么？ 越看这类文章，越容易把自己放到一个又一个的群体中，然后合理化自己的状态。这不是一个好的方式。


---


### 书影播客

《Biong Biong 地球游戏厅 第二季》，断断续续看完了，据说一些人说是目前三季中不太好看的一季，当人员固定下来，游戏环境固定，是否好看感觉全看状态了。

《基本无害-Ep167 悉尼生存手册》，推荐的旅游景点是三件套：悉尼歌剧院、悉尼海港大桥和悉尼塔，果然每个地方都有自己的三件套。这期提到了一些长辈为了能在澳洲种植自己想吃的蔬菜，采用的方式是上飞机前，先把种子吃到肚子里，然后保证在飞机上不要进食，一直回到自己家，在排放出来，并且成功了。这算物种入侵么。。。



## 碎碎念

* OpenSSL 1.0.2 已经需要花钱买服务支持才能够下载到源码了，这些老旧的系统真是头大。
* 感谢博通，感谢 vmware/photon ，还保留着 source rpm。
* 看到这么多吐槽用了 qwen-code 之后花了很多钱的，挺好的，让大家对云服务账单有了直接的认知。
