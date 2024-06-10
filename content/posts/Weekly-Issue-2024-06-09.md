---
title: Weekly Issue-儿童节的由来
date: 2024-06-09
tags:
- Weekly
description:  
---


## 文章

### 技术

[Signal: Will leave the EU market rather than undermine our privacy guarantees | Hacker News](https://news.ycombinator.com/item?id=40551260)

[Majority for chat control possible – Users who refuse scanning to be prevented from sharing photos and links – Patrick Breyer](https://www.patrick-breyer.de/en/majority-for-chat-control-possible-users-who-refuse-scanning-to-be-prevented-from-sharing-photos-and-links/)

欧盟想要通过聊天控制方式，避免儿童性虐待事件的发生，需要让所有的 IM App 进行信息扫描。[[Signal]] 为了反对这个提议可能会退出欧盟市场。

印象中的欧盟一直以保护用户隐私而出名，现在的这个提议感觉有点过激了，不知道之前一直以欧盟来抨击国内审查制度的人，会如何看待这件事情呢？

---

[计算机网络实用技术：序章 | 卡瓦邦噶！](https://www.kawabangga.com/posts/6097)

[「不可以用路由器？」 | 卡瓦邦噶！](https://www.kawabangga.com/posts/6178)

xintao 编写的网络系列博客，第一篇。打开 [[WireShark]] 可以直接看到根本原因，返回的 TTL=1，导致经过路由器就被丢弃了，可以通过 iptables 在路由器上在传入或者传出时重新设置 TTL。

---


[Ten Years of Kubernetes - Justin Garrison](https://justingarrison.com/blog/2024-06-06-ten-years-of-kubernetes/)

[Kubernetes 2.0 - Justin Garrison](https://justingarrison.com/blog/2024-06-06-kubernetes-2.0/)

[[kubernetes]] 已经发布 10 年了，作者讲述了自己与 [[kubernetes]] 的故事，已经对下一阶段的展望：
- 可选择的 etcd：Almost every customer I worked with at AWS gained no benefits of etcd being the data store behind Kubernetes.
- Versionless：我理解这里不是要 Versionless，而是稳定的 API ？
- 更多的单体服务？其中提到 Cluster API 默认使用微服务，“It’s too complex unless you’re going to be selling it. It’s not for end users.”
- K8sfile，希望能像 Dockerfile 那样， FROM 一个 K8s version，然后 INSTALL 应用。

---

[Comparison to asdf | mise-en-place](https://mise.jdx.dev/dev-tools/comparison-to-asdf.html)

[[DHH]] 推荐了 [[mise]]，一个环境设置工具，可以取代 [[pyenv]]/[[nvm]]/[[asdf]] 等等，使用 [[Rust]] 编写。这篇官方文档比较了 [[mise]] 和 [[asdf]] ，一句话就是更快更易用。

提到了 [[asdf]] 是使用 [[Bash]] 编写的，在调用 node 时的顺序是： `~/.asdf/shims/node` 然后调用 `asdf exec` ，这里每次运行时调用会增加 120ms，性能很差。mise 直接更新 PATH 来实现。

---

[web3-101 slides](https://s3.laisky.com/public/slides/web3-101.slides.html#/)

《面向 Web2 工程师的 Web3 入门》

---

[Preventing Server Side Request Forgery in Golang](https://www.agwa.name/blog/post/preventing_server_side_request_forgery_in_golang)

[[Golang]] 中防止 [[SSRF]] 攻击的方式，在 `net.Dialer` 的 `Control` 中进行一些基本的防御检查操作：

```Go
func safeSocketControl(network string, address string, conn syscall.RawConn) error {
	if !(network == "tcp4" || network == "tcp6") {
		return fmt.Errorf("%s is not a safe network type", network)
	}

	host, port, err := net.SplitHostPort(address)
	if err != nil {
		return fmt.Errorf("%s is not a valid host/port pair: %s", address, err)
	}

	ipaddress := net.ParseIP(host)
	if ipaddress == nil {
		return fmt.Errorf("%s is not a valid IP address", host)
	}

	if !isPublicIPAddress(ipaddress) {
		return fmt.Errorf("%s is not a public IP address", ipaddress)
	}

	if !(port == "80" || port == "443") {
		return fmt.Errorf("%s is not a safe port number", port)
	}

	return nil
}

safeDialer := &net.Dialer{
	Timeout:   30 * time.Second,
	KeepAlive: 30 * time.Second,
	DualStack: true,
	Control:   safeSocketControl,
}

safeTransport := &http.Transport{
	Proxy:                 http.ProxyFromEnvironment,
	DialContext:           safeDialer.DialContext,
	ForceAttemptHTTP2:     true,
	MaxIdleConns:          100,
	IdleConnTimeout:       90 * time.Second,
	TLSHandshakeTimeout:   10 * time.Second,
	ExpectContinueTimeout: 1 * time.Second,
}

safeClient := &http.Client{
	Transport: safeTransport,
}

resp, err := safeClient.Get(untrustedURL)

```


---



### 生活

[[儿童节]]的由来：1949年11月，苏联莫斯科举行的国际民主妇女联合会执行委员会议[2]。执委会委员海伦·加波罗佐（Helen Gabrozo）在会上代表国际妇联书记处建议，订立6月1日为“国际儿童节”[4][1][2]，以悼念在1942年6月10日被纳粹德国屠杀的捷克利迪策村的88名儿童、以及全世界所有在法西斯侵略战争中死难的儿童[4][2]。加波罗佐指出，订立该节是为了保障世界各地儿童的生存权、保健权及受教育权，进而改善儿童的生活面貌[1]。1954年，6月1日被定为“保护儿童国际日”，以保护儿童权益及儿童的学习权、终结童工[5]，使得该日作为儿童节的国际认可有所提升[6]。


---

[Eye exercises for myopia prevention and control: a comprehensive systematic review and meta-analysis of controlled trials | Eye](https://www.nature.com/articles/s41433-023-02739-x)

眼保健操有用么？结论：没用。

或者换一种说法：眼保健操有用么？有用，至少它可以让你真正的闭眼一段时间。

---

[2023H2-2024H1 财误报告](https://www.douban.com/note/862886041/?_dtcc=1&_i=7409120BlBAZ-O)

[2019 财误报告](https://www.douban.com/note/748726366/?_i=7460456BlBAZ-O)

很明显，博主的婚后生活幸福感提升非常大。

我也应该学习一下，如何总结自己的财务状态，如何评估和改善，资产负债率、结余比率、投资比率、负债收入比率、消费比率。

---


[六子吃了几碗粉？ - Jinji](https://jinjipang.com/cn/2022-03-24-/)

我非常羡慕有些朋友的“不在意”，他们能对很多事情不在意，虽然我日常也会嘴上说着“不重要”，但是还是或多或少会影响自己的行为，而有些朋友是真的能做到完全的不在意，仿佛事情没有发生过一样。这是一个很重要的能力。

---

[填报志愿 | 卡瓦邦噶！](https://www.kawabangga.com/posts/6086)

算了算，我弟弟也是今年中考，在我们老家省份应该可以上一个高中吧。
对于身边的亲人这种咨询，我一直很抗拒，一是自己对于各个专业情况的不了解，二是自己当前也处于一个迷茫的阶段，再加上对方和自己有一层亲情关系，生怕自己的不经意回答产生预期外的影响。

---

[理解人性，提升决策](https://anqi.rocks/2023/05/08/)

理解人性，虽然很多平时也会知道一些，但是真正整体去阅读的时候，有一种自己被剖析的错觉。理智告诉我们，应该是从这些角度去考虑事情，来避免自己陷入某些误区从而做出错误的决策。

---

[YNAB究竟有什么不同？](https://xiaowenz.com/2018/12/10/54)

记账的目的是什么？如果只是想知道自己的财务状况，那么不需要详细粒度的记录，只需要定期对账就可以了，如果是想记录消费细节，那么最后设置一个预算，知道自己每个月在某项开支是否符合自己的预期，以此来调节后续消费。

---


## 书影

《被讨厌的勇气》，趁着端午假期看完了。“一切烦恼皆源于人际关系”，“人可以随时改变并能够获得幸福”，“问题不在于能力而在于勇气”。从目的论来解读行为，可能有会一些残忍，但是有效。

读完之后我想起来，很早之前，我看 NBA 的一些时事评论，非常喜欢宏大叙事，比如苏群、张佳伟，但是后来发现，从这个角度看，很多事情都是一样的，或者说严格类似的，后面发现有时候杨毅写的一些内容，事情没有那么复杂，从目的论解读，球员做这个事情的目的是什么，就可以很快的理解一些行为。


《迷失东京》，食贫道旗下的充电视频。里面提到的内容可以看到最近日本的真实状态，对于日本常见社会问题的探讨没有很深入。

《迦南孤儿》，食贫道旗下的充电视频。讲述巴以现在生活的真实状态视频，能够感受到饼叔是有选择性的说了一些内容，没说一些内容。我在去年年底写巴以冲突的观点是：“作为一个普通人，在面对战争新闻的时候，了解的通常是片面的，我也尝试着去了解一些背景，但是这些背景夹杂着各种政治因素在里面，最终就是观点不断地**被**刷新。现在我选择在了解大概之后，不去看这些，逃避虽可耻但有用。”。 看了这个视频，仍保持这个观点。

## 碎碎念

* 「产业后备军」：「马克思则一直强调资本主义经济要求长期的、固定的保留一部分的失业人口，并将其称之为产业后备军。保留一部分的失业人口有利于资本家加强对在岗工人的规训和控制，并且可以压低在岗工人的工资，这是长期存在的。」
* 闲鱼重点不是二手商品，而是信息差
* 我想象中的我是想“打”游戏，而不是想打”游戏“。重点是”打“这个行为，游戏不重要。
* 我平时 3 点或 4 点起床，习惯性的打开 Slack 之后，看到同事加班到 24 点或者 1 点，明明大家都在同一个时区，却有了时差
* 同事科普了一下当前手游氪金的玩法：648、大月卡、小月卡、首充、首充重置。我还停留在魔兽世界的点卡时代，落伍了。


