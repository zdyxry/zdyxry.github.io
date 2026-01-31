---
title: Weekly Issue-《好东西》
date: "2024-11-10T00:00:00.000Z"
slug: "Weekly-Issue-好东西"
tags:
  - Weekly
description:
---

## 文章

### 技术

[把 Cloudflare WARP 转换为 http 代理 | 土豆不好吃](https://dmesg.app/warp-http-proxy.html)

> 偶然取消 DNS 请求的勾选，就成功了…… 突然恍然大悟，WARP 可能不支持远程解析 DNS    
> 那么要么用回 socks4    
> 	$pproxy -v -l http://127.0.0.1:8118 -r socks4://127.0.0. 1:60606    
> 	$gost -L http://127.0.0.1:8118 -F socks4://127.0.0. 1:60606    
> 要么给加上 DNS 的支持    
> 	$gost -L "http://127.0.0.1:8118?dns=1.1.1.1" -F socks5://127.0.0. 1:60606

---

[Mutable vs. Immutable: Infrastructure Models in the Cloud Era](https://dzone.com/articles/infrastructure-models-in-the-cloud-era)

讨论可变基础设施和不可变基础设施的优缺点，以及适用场景。比较维护比较全，也许后面写文档可以用得上。

---

[if it hurts, do it more often - 频率就是解药](https://mp.weixin.qq.com/s?__biz=MzkzNzY0NDg4MA==&mid=2247483868&idx=1&sn=3fd6838e1afe12ca60365baba3c94e70&poc_token=HFNlKWejO5nyCZk0flZQgtCmMfkHkUAtlrwTLebz)

> 你是否遇到过这些问题？
> - 每次合并代码都面临大量冲突，解决起来异常痛苦？
> - 每次上线发布都如临大敌，心惊胆战？
> - 每次进行底层重构时，风险高得让人犹豫不决？

答案是提高频率。之前其他人也说过，应该让每次修改都尽可能的快，更快的验证、测试、上线。只有这样才有动力去做更多。

---

[curl -v https://google.com - YouTube](https://www.youtube.com/watch?v=atcqMWqB3hw)

如标题所示，这是一个 `curl -v https://google.com` 的视频，观看的时候需要带上耳机。太酷了。

---


[Writing secure Go code | Jakub Jarosz](https://jarosz.dev/article/writing-secure-go-code/)

编写安全的 [Go](/mentions/go) 代码，这里的“安全”是多种含义，包含了 CVE 相关的安全，也包含了业务语义上的安全。
- 即是更新 golang 版本
- 使用工具检查
	- `go vet`
	- `staticcheck`
	- `govulncheck`
	- `gosec`
	- `go test -race`
	- `golangci-lint`，可以使用 `golangci-lint` 来包含上述所有检查， 一直觉得 golangci-lint 默认的 linter 太多了，每次都需要手动调整
---


[Bank scammers using genuine push notifications to trick their victims – Terence Eden’s Blog](https://shkspr.mobi/blog/2024/05/bank-scammers-using-genuine-push-notifications-to-trick-their-victims/)

简单的中间人攻击，还是会有人上当。最简单直接的解决方式，不接听所有陌生来电，

大部分场景都可以通过 IM 解决，如果对方没有我的 IM，那大概率不是重要的事情。如果是平台联系我，会通过邮箱，及时查看邮箱就好。

---


[特殊的 ARP 用法：Gratuitous ARP, ARP Probe 和 ARP Announce | 卡瓦邦噶！](https://www.kawabangga.com/posts/6698)

之前自己实现过一个 VIP 项目，实现上关于免费 ARP 是抄的 [seesaw/ncc/arp.go at master · google/seesaw · GitHub](https://github.com/google/seesaw/blob/master/ncc/arp.go#L84) 部分，发现 kube-vip 项目中关于免费 ARP 的部分是交替发送的，Issue 中描述是有些网络设备只支持一种。

[Gratuitous ARP – Definition and Use Cases – Practical Networking .net](https://www.practicalnetworking.net/series/arp/gratuitous-arp/) 中关于免费 ARP 的描述中，“The **Target MAC** address is **`ffff.ffff.ffff`** – a reflection of the Destination MAC address. But in reality, the contents of this field are irrelevant – they are ignored in a Gratuitous ARP. Some implementations of ARP will use **`0000.0000.0000`** in this field.”，

而在 [RFC](https://datatracker.ietf.org/doc/html/rfc5944#section-4.6) 中的描述是：“When using an ARP Reply packet, the Target Hardware Address is also set to the link-layer address to which this cache entry should be updated (this field is not used in an ARP Request packet).” ，总感觉这里的描述是有些差异的。

---


[For the first time ever, AMD outsells Intel in the datacenter space | Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/for-the-first-time-ever-amd-outsells-intel-in-the-datacenter-space)

> Meanwhile, (Nvidia)compute GPU sales reached $22.604 billion in Q2 FY2025, which far surpasses the combined sales of Intel and AMD datacenter hardware.

数据中心领域，AMD 超过了 Intel，AMD 第三季度收入是 3.549 Billion, Intel 是 3.3 Billion。看似在说 AMD 和 Intel 的事情，但是 Nvidia 的数据中心收入超过了前两者之和。

---



### 生活

[I've had a change of heart regarding employee metrics](https://rachelbythebay.com/w/2024/11/03/metrics/)

> Why? It's surprisingly simple. It's the job of a manager to know what their reports are up to, and whether they're doing a good job of it, and are generally effective. If they can't do that, then they themselves are ineffective, and *that* is the sort of thing that is the responsibility of THEIR manager, and so on up the line. They shouldn't need me (or anyone else) to tell them about what's going on with their damn direct reports!

大实话： **In theory, at least, that's how it's supposed to work. That's their job: actually managing people!**

---

[关于“脱口秀是冒犯的艺术”是谁特么第一个说的](https://mp.weixin.qq.com/s/cpTtEOkaj6xvN_ihfUDoVQ)

> 由于脱口秀在上的一些貌似“冒犯”的观点，很容易引起争议，引发热搜，于是很容易形成社会话题，比如殷储和杨笠关于“普信男”的大战一直到今年的京东代言事件。在大众视野里最出圈，被最多人讨论的却是“冒犯”。即，**由于争议性的话题出圈，因此“冒犯”引发连环误解，做实了这个错误定义**。

作为一个单口喜剧爱好者，之前也写过一篇博客来讲自己的看法： [单口喜剧与冒犯 · Yiran's Blog](https://zdyxry.github.io/2023/05/20/%E5%8D%95%E5%8F%A3%E5%96%9C%E5%89%A7%E4%B8%8E%E5%86%92%E7%8A%AF/)

---

[杨太太 ｜ 美国大选里被人忽视的关键因素](https://mp.weixin.qq.com/s/CRE6Awe0NIoMfS76N8pBuA)

> 因为民主党对于同性恋婚姻和女性堕胎权的支持，导致有很多美国的基督徒完全没有了选择，再不喜欢也只能捏着鼻子投川普的票

> 很多中国人觉得美国深红区的人是因为非法移民抢了他们的饭碗，所以他们才支持共和党。**但是事实情况恰恰相反，深蓝地区才是非法移民的重灾区，像我们这种深红地区，穷乡僻壤，啥啥也没有，非法移民根本不会过来啊。**
> 

> 所以他们投共和党，并不是出于对他们自己的私利的支持，更多是一种对于他们持有的价值观的表达。

> 如果你打开美国大选地图，你会发现很多州虽然是蓝州，比如明尼苏达，弗吉尼亚，伊利诺伊……但是他们大部分的县是红色的，只是因为州里的大城市是蓝的，而大城市的选票实在是太多了，所以这个州最终是蓝州。

---

[Musk, the Foxy Kingmaker – On my Om](https://om.co/2024/07/23/musk-the-foxy-kingmaker/)

**Kingmaker**.

> CloudFlare 创始人转发对 Elon 买了 twitter 的评价：
> 「令人着迷的是，这将如何从根本上改变任何评估推特收购的尝试。从商业角度来看，这是一次巨大的失败，而且可能永远都是：马斯克为当时的推特支付了过高的价格，而在接下来的几年里，广告商纷纷逃离该平台，使其价值更低。
> 然而，从马斯克公司的角度来看，X 在确保即将上任的政府在 SpaceX 获得实际前往火星的能力的那一刻，满足马斯克的需求方面发挥了关键作用，只要美国联邦航空管理局（尤其是美国联邦航空管理局）给予他这样做的自由。仅此一项就几乎肯定值 440 亿美元！
> 更广泛地说，这解释了为什么马斯克如此难以讨论：关注他的成就，尤其是特斯拉和 SpaceX，是如此重要，以至于似乎有理由原谅他的手段；与此同时，我对那些因他的手段而反对他的人表示同情。然而，不可否认的是，他举足轻重。」

20241108，SpaceX 提出了 Marslink 概念，用于火星到地球的高速互联网。

---

[功不唐捐 - Frost's Blog](https://frostming.com/2024/efforts/)

> 所以，你看过的每一本书，玩过的游戏，走过的路，都不会浪费。只是你还没找到用处罢了，又或者它们已经内化在你的个人气质中了。

““唐捐”是佛经里的话，意思就是泡汤了、白费了。功不唐捐是就**努力绝不泡汤、绝不白费**。一个人的努力，在看不见想不到的时候，在看不见想不到的地方，会生根发叶、开花结果。”

看到过不少类似的调调，说“读过的书都忘记了，还看它有什么用”。我最近发现自己看过的很多书，内容可能已经不记得了，对我明显的改变可能也看不出，这能说明它没用么？它是一个信息输入，既然当时我选择读完它，说明它对于当时的我来说是有价值的，无论是实用价值还是情绪价值，这么多年的信息输入形成了现在我对很多事情的观念，从这个角度去看是“有用”的。

---

[Australia proposes 'world-leading' ban on social media for children under 16](https://www.reuters.com/technology/cybersecurity/australia-proposes-ban-social-media-those-under-16-2024-11-06/)

> 澳大利亚政府将立法禁止16岁以下儿童使用社交媒体。

搜了下新加坡的相关条例：
> 新加坡卫生部去年3月发布针对零岁至12岁孩童的屏幕使用指导原则。指导原则不鼓励18个月及以下的婴孩使用屏幕，年龄介于一岁半至三岁的幼童，每日屏幕时间不应超过一小时。（档案照片）

回想了下，我好像是 15 岁或者 16 岁正式使用社交媒体的。

---

## 书影

《好东西》，邵艺辉导演作品。之前导演过《爱情神话》，当时是 2021 年底上映，是我 2021 年最喜欢的电影。《好东西》应该会是我 2024 年最喜欢的电影。如果你喜欢《爱情神话》，那大概率会喜欢这部电影，发生在同一个城市中的故事，电影结尾的路演中，导演也说，自己恨不得现在就回家去写（下一部的）剧本。

电影讲述的是一个单亲妈妈带着孩子独自生活，和邻居小叶在生活中发生的故事。片中的笑点很多（有一句台词是“尚音”的，我没理解这里的笑点。。），经常全场爆笑到听不到下一句的台词，也许下一部电影可以控制一下节奏？。邵艺辉很会写简单的故事，传统意义上的戏剧冲突很少，会写故事尤其体现在对话上，当几个各怀鬼胎的人坐在一个饭桌上，吃饭之间精妙的对话，很难不笑。与故事相对的是人物，这些人物的刻板印象是很强的，比如男性之间的雄竞、女主的独立话术、恋爱脑的不清醒，在观影中就听到“太典了”之类的声音。

相较于上一部电影，这一部导演想要表达的观点明显更多，主要集中在性别的刻板印象上，从电影的英文名也能看出，《Her Story》，豆瓣上看到说有些人破防了，这部电影可能会冒犯到一些人？作为恰好看过几本上野千鹤子老师的书的人，观影非常愉快，有一种看了一场单口喜剧专场的感觉，强烈推荐大家去看。



## 碎碎念

* 之前的想法是，现在人没有选择死亡的权力，看到一篇文章讲述，如果允许安乐死的话，可能会有很多“被动”安乐死，比如一些行动不便的老人，或者精神疾病患者。需要读一些相关书籍了解一下，才有更全面的了解。
* 三辉图书倒闭了，现在没有人去讨论电子书和实体书了，相比于之前讨论时候的状态，这种慢性死亡更可怕。
* 史炎发微博：”脱口秀不是冒犯的艺术，正如川菜不是辣的艺术。川菜是他妈的好吃的艺术。 ​​​“
* 公开透明，什么叫公开，什么叫透明
* 相较于跑路，骑车，跳伞，潜水是唯一一个可以上下左右移动的？
* 原来不只是我一个人有这种感觉，作为哈尔滨人，在外面没什么想念的，唯独雪，一看到雪或者听到雪，就想家了。
* 现在的风评开始反思 DEI，那我能看到白的的《白雪公主》了么？我能看到《美人鱼》了么？
* 为什么对泰国印象很好，禁烟是一个原因
* 我从来不主动升级 MacOS，它很好，我日常所有的需求它都能工作的很好，我完全没有升级的动力。
* OCBC 不能办理了，果然有些事情拖着拖着就不行了，警醒


