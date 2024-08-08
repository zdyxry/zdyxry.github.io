---
title: Weekly Issue-如何对故障进行分类
date: 2024-07-28
tags:
- Weekly
description:  
---


## 文章

### 技术

[数据中心网络高可用技术：序 | 卡瓦邦噶！](https://www.kawabangga.com/posts/6417)

[数据中心网络高可用技术之从服务器到交换机：active-backup | 卡瓦邦噶！](https://www.kawabangga.com/posts/6430)

>"MII Monitoring 就是通过 MII 来检查物理物理网卡的状态。如果物理网卡挂了，通过 MII 就可以检测到。但是 MII 检查通过不能代表网络是通的。"  
>use_carrier 如果打开的话（默认就是 1, 打开的），就使用 netif_carrier_ok 来获取链路状态，底层依赖的是网卡驱动程序。大部分的网卡驱动程序都支持 netif_carrier_on/off 功能，如果不支持的话，那么链路检测永远是 up 的，即使挂了也不会触发 bonding 的切换。所以网卡如果不支持，就得把 use_carrier 改成 0。  
>MII Monitoring 无法检测的问题是：交换机正常运行但是配置错误，或者通过了 Linux 网卡驱动的检测但是发送数据会有问题等等。

---

[编程语言中的 context 是什么？ - Jiajun的技术笔记](https://jiajunhuang.com/articles/2024_07_21-context.md.html)

>因此，我们可以这样理解：context 就是一堆状态(state)，在不同的场景下，context 的具体内容和作用是不同的，但是都是用来保存和传递状态信息的。

---

[What is a REST API entry point and how is it different from an endpoint? - Stack Overflow](https://stackoverflow.com/questions/53199289/what-is-a-rest-api-entry-point-and-how-is-it-different-from-an-endpoint)

Endpoint vs Entrypoint 。

- Endpoint
	- https://example.com/api/login
	- https://example.com/api/accounts
	- https://example.com/api/cart/items
- Entrypoint
	- https://example.com/api

---

[2024 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2024/)

[[StackOverflow]] 2024 开发者调查：
- 云平台： AWS、Azure、GCP，[[Fly.io]] 上榜了；
- AI 工具：ChatGPT、Copilot、Gemini；
- 对于从头构建还是购买产品，Cloud Infra Engineer 购买的意愿最低；
- 在研究新技术或者工具时，询问其他开发人员是一个靠谱的选择，所以产品的口碑很重要；
- 产品技术认可中，API、质量、定制化，这三项几乎是必须要考虑的；
- 大家都面临知识孤岛的问题；

---

[Handling Failures From First Principles | by Dominik Tornow | Medium](https://dominik-tornow.medium.com/handling-failures-from-first-principles-1ed976b1b869)

故障处理的分类：
- 空间维度
	- Application 带有业务语义的故障
	- Platform 平台故障，对业务是透明的
- 时间维度
	- 瞬间故障
		- 发生、消失
	- 间歇故障
		- 发生、持续、消失
	- 永久故障
		- 发生、持续

如何缓解故障：
- 时间维度
	- 瞬间故障、间歇故障
		- 可以通过重试（立即重试、回退重试）来缓解
	- 永久故障
		- 手动修复
- 缓解方式
	- 向后恢复
		- 动作回滚，补偿机制
		- 不需要修复故障的根本原因
	- 向前恢复
		- 将系统从中间状态转换为最终状态，比如重试
		- 需要修复故障的根本原因

---

[x.com](https://x.com/_Freakyclown_/status/1816890415339176256)

>TIL: that intel i 3, i 5, i 7 and i 9 processors are all the same, all made the same, on the same wafer. But depending on how many defects (therefore how many sections actually work) they just rename them. So your i 3 processor is an i 9 with many defects less for an i 5 and less for i 7

Intel `i3` 是残缺版的 `i9` ？

---

[什么？你是怎么从数据包看出MTU异常的](https://mp.weixin.qq.com/s/11BkPO2FN6EJoQMtiOprtQ)

通过分析正常报和异常包的 Length，检查 MSS，配合 `ping -M do -s 1472 -c 3 -i 0.2 $ip` 来定位问题。

---

[The New Internet](https://tailscale.com/blog/new-internet)

[[TailScale]] 老板的文章，读下来感觉是那种典型的“宏大叙事“文体，宏大到我不知道他想要说什么。老板写的东西就是不一样。

[[hacker news]] 热门评论比较有趣，谁阻止了 [[IPv6]] 的发展呢？我觉得肯定不是 [[TailScale]]：“The eternal problem with companies like Tailscale (and Cloudflare, Google, etc. etc.) is that, by solving a problem with the modern internet which the internet should have been designed to solve by itself, like simple end-to-end secure connectivity, Tailscale becomes _incentivized to keep the problem_. What the internet would need is something like IPv6 with automatic encryption via IPsec, with PKI provided by DNSSEC. But Tailscale has every incentive to _prevent_ such things to be widely and compatibly implemented, because it would destroy their business. Their whole business depends on the problem persisting.”


---


### 生活

[要想毁了孩子，那就从《抓娃娃》做起](https://mp.weixin.qq.com/s/9UmEsTLYO2-tQDTG-DaITg)

> 好像，孩子不是有血有肉的生命，而是娃娃机中的娃娃那样，一个不满意，再换一个抓就是了。
> 
> 他喊了一句“晚上还回不回家吃饭了”，好像过往的一切都可以在这句话中消解似的。

---

[Official data: over a million Cubans migrated in two years | Miami Herald](https://www.miamiherald.com/news/nation-world/world/americas/cuba/article290249799.html)

>“可以合理地将这种流失解释为对该岛经济和政治状况普遍不满的迹象，”他说。 “成千上万的古巴人，尤其是最年轻的人，对国家的未来失去了信心，选择到国外寻求更好的运气。”

[[古巴]]在 2022 到 2023 年之间，有 10% 人口离开了古巴，是古巴历史上最大规模的移民浪潮。

---
[37%法则](https://wiki.mbalib.com/wiki/37%25%E6%B3%95%E5%88%99)

> 意思是经过数学家欧拉的实验，以37%作为分界点，前面的时间用来观察，后面的时间用来作决策的一种方法。
 >举例来说，比如要买房子，整个地区的房子有30处，那么需要先看37%的房子，也就是11个房子。37%前的房子只看不买，但是要记住自己认为最好的是什么样子。看完后，从37%以后只有遇到比之前最好的还要好的房子就应该下手买。

---


[再读《聪明的投资者》—— Review 近 3 年观点](https://wsfdl.com/%E7%BC%96%E7%A8%8B%E9%9A%8F%E6%83%B3/2024/03/31/the-intelligent-investor-again.html)

周期性的回顾、复盘、调整，才是可持续改进的方式啊。

---

## 书影

《绝对坦率 : 一种新的管理哲学》，真诚，坦率。

《走走停停》，断断续续看完了，没想象中那么好看。

《甜蜜家园》，有点吓人，不敢继续看了。

《暗战》，是真的好看，短短 3 场爱情戏，但是很让人着迷。


## 碎碎念

* 给其他人推荐东西要谨慎，谨慎。
* 试试 Supermaven ，看看比 Codeium 怎么样，速度是真的快。
* 发现自己好像没什么不能理解的，都可以理解。
* 妈的，我还是有很多不理解。
* 我好久没有喝到有奶味的牛奶了
* 为什么普通人关心宏大叙事？因为普通人没有什么改变的能力，宏大叙事大概率会影响到自己？中产至少有改变的能力和可能。
* >黄昏是我一天中视力最差的时候，一眼望去满街都是美女，高楼和街道也变幻了通常的形状，像在电影里……

