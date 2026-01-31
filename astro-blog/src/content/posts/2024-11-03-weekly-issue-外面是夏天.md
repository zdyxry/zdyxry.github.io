---
title: Weekly Issue-《外面是夏天》
date: "2024-11-03T00:00:00.000Z"
slug: "Weekly-Issue-外面是夏天"
tags:
  - Weekly
description:
---

## 文章

### 技术


[Using less memory to look up IP addresses in Mess With DNS](https://jvns.ca/blog/2024/10/27/asn-ip-address-memory/)

一个 [Golang](/mentions/golang) 程序的内存使用优化过程记录，先是尝试了一些其他的方案，比如 SQLite，trie，都放弃了。最后一点点通过 runtime 来分析内存使用，通过修改部分数据结构来优化内存，在优化的过程中，搜索到了 Tailscale 发表的关于 `net.IP` 问题的博客，最终节省了 70MB 的内存。

---

[Omnivore is joining ElevenLabs - Omnivore Blog](https://blog.omnivore.app/p/omnivore-is-joining-elevenlabs)

[omnivore](/mentions/omnivore) 被 [ElevenLabs](/mentions/elevenlabs) 收购了，[ElevenLabs](/mentions/elevenlabs) 是一个 AI 音频平台。[omnivore](/mentions/omnivore)  所谓的 self-hosted 之前是一句笑话，之后应该也是。

---

[An update from Drew | Dropbox Blog](https://blog.dropbox.com/topics/company/an-update-from-drew)

[Dropbox](/mentions/dropbox) 决定裁员约 20%（528 人）。Dropbox  本身是盈利的，4.5 亿美元利润/2.5B 美元收入的净利润。

想到之前在 Twitter 上看到的 Dropbox 办公室政治已经非常严重，裁员也不意外。

---

[c++ - Cycles in family tree software - Stack Overflow](https://stackoverflow.com/questions/6163683/cycles-in-family-tree-software)

问题作者在开发家族图谱软件，收到了一个用户问题，软件报错是：“X 不能即是 Y 的父亲又是 Y 的祖父”。信息量好大，但是评论也很有道理，在宠物行业，为了追求纯种，这样的现象貌似很常见。

回答者指出了 GEDCOM 存在的问题，GEDCOM 的很多限制在现实生活中很有可能出现，建议只保留逻辑上的限制（一个人不能是自己的父母，关系链需要两个人，等等）。

---

[SSH Remoting is Here!](https://zed.dev/blog/remote-development)

[Zed](/mentions/zed) 的 SSH Remoting 功能进入到了 Beta 版本，快速试用了一下， Golang 项目的代码跳转速度明显比之前的 Alpha 快很多，感觉到了可以真正尝试的阶段了。

---

[GitHub - henrygd/beszel: Lightweight server monitoring hub with historical data, docker stats, and alerts.](https://github.com/henrygd/beszel)

轻量级的监控方案，基于 [PocketBase](/mentions/pocketbase) 构建，想着作为 PocketBase 学习素材看看，结果发现是通过 SSH 协议通信的，在 agent 启动一个 ssh server，然后 hub 作为 client 通过 ssh 链接 agent 来获取实时的监控数据。为啥是 SSH 呢？每个 agent 都需要占用一个端口，对于没有公网 IP 的场景怎么办？后续的扩展性如何处理，感觉是个玩具项目。

---

[Go单元测试 Mock 方案总结](https://taoshu.in/go/mock.html)

[Golang](/mentions/golang) 单元测试相关的 Mock 方案，其中提到了 [GitHub - bouk/monkey: Monkey patching in Go](https://github.com/bouk/monkey) 以及 [xgo/README\_zh\_cn.md at master · xhd2015/xgo · GitHub](https://github.com/xhd2015/xgo/blob/master/README_zh_cn.md) 。

之前看到有人推荐过字节的这个 mockey： https://github.com/bytedance/mockey ，与上面的 houk/monkey 是一样的，都需要禁用内联和编译优化。

---

[豆瓣标记导出到 Notion 并同步 | Blah Blah Booooom](https://zhuzi.dev/posts/2021-06-05-douban-backup-sync-notion/)

自动将豆瓣标记同步到其他平台，如 Notion Database 或者 Neodb。

---

[Okta AD/LDAP Delegated Authentication - Username Above 52 Characters Security Advisory](https://trust.okta.com/security-advisories/okta-ad-ldap-delegated-authentication-username/)

[Okta](/mentions/okta) AD/LDAP 存在安全问题，如果用户名长度大于等于 52 时，用户 **有可能** 只需要提供用户名就能登录。

[Okta](/mentions/okta) 有一些[黑历史](https://x.com/GergelyOrosz/status/1852503333149241780)，[CloudFlare](/mentions/cloudflare) 也不使用 [Okta](/mentions/okta) 作为 identity vendor 了，选择自己搞。

---

[Authentication for beginners, part 1: You don’t store the passwords](https://unknwon.substack.com/p/authentication-for-beginners-part-one)
> As of this writing, popular and safe choices of signature algorithms are **Argon2, Bcrypt, Scrypt and PBKDF2 with cryptographically randomly-generated salts and right parameters**.

 [Joe Chen](/mentions/joe-chen) 的 newsletter，作者是 [Sourcegraph](/mentions/sourcegraph) 负责身份验证/鉴权验证/IAM 等系统的开发。这篇文章是早于上面的 [Okta](/mentions/okta) 事故公开时间的，但是一起阅读很应景。

---

[How I write code using Cursor: A review](https://www.arguingwithalgorithms.com/posts/cursor-review.html)

这篇文章的作者提到 Cursor 对于工作流的影响：
- I am _much_ less likely to reach for a new library or a framework.
- I also worry less about adhering to DRY (Don't Repeat Yourself) in my own code.
- My willingness to use a language or framework I am less familiar with is much higher.
- I find myself iterating quickly on small components before integrating them into the larger codebase.

虽然大家都说 [Cursor](/mentions/cursor) 交互很好，但感觉想要用好还是需要花些时间学习下的。

---

[GitHub - MikeWang000000/n4: 双 NAT4 网络打洞 PoC](https://github.com/MikeWang000000/n4)

N4 是针对双方均为 “端口递增型 NAT” 的一种打洞测试工具。作为学习了解简易实现。

>解释说明：
> 1. 客户端向服务端发送 Hello 包；
>2. 服务端收到两个客户端的 Hello 包后，同时向两方发送 Ready 包；
>3. 客户端收到 Ready 包，使用 UDP 向服务器发送 Exchange 包，表示交换两客户端 UDP 公网信息；
>4. 服务端收到一客户端的 Exchange 包，向另一客户端发送 Peerinfo 包，携带前者 UDP 公网信息；
>5. 客户端收到 Peerinfo 包，根据对方地址 `IP:PORT`， 预测对方将来的地址会有 `IP:PORT + peer_port_offset`。 客户端从自身端口 `src_port_start` ~ `src_port_start + src_port_count` 范围， 使用 UDP 逐一向 `IP:PORT + peer_port_offset` 固定地址发送 Punch 包。
> 
> 如果客户端收到 Punch 包，代表打通。否则，增加源端口值，再次尝试。

---

[Understanding Round Robin DNS - by Zsolt Ero](https://blog.hyperknot.com/p/understanding-round-robin-dns)

对 Round Robin DNS 的行为进行验证，分别验证 Cloudflare DNS-only 和 Proxied。发现对于 Cloudflare DNS-only 模式（通用 DNS 配置），无论是所有服务器都在线还是离线，各个 Client 虽然行为不同，但是总能按照预期工作；在 Cloudflare proxied 模式下，服务器存在离线场景，Client 无法获取其他在线服务器的响应，即 Cloudflare 没有检测到服务器离线。

在 HackerNews 上引发了讨论，Cloudflare CEO & CTO 进行了回复，确认行为是异常的，目前已经进行了修复。

---





### 生活

[50 Years Ago, Sugar Industry Quietly Paid Scientists To Point Blame At Fat : The Two-Way : NPR](https://www.npr.org/sections/thetwo-way/2016/09/13/493739074/50-years-ago-sugar-industry-quietly-paid-scientists-to-point-blame-at-fat)

《50 年前，制糖业悄悄付钱给科学家，让他们将责任归咎于脂肪》，工业界/资本对于普通人生活的影响，方方面面。如何正确的识别信息的真实性，太困难了。

---

[Writes and Write-Nots](https://paulgraham.com/writes.html)

> If you're thinking without writing, you only think you're thinking.

Paul Graham 认为几十年后会有很多人不会写作。要想写好，必须清晰的思考，但是清晰的思考是很难的。

---

[Character Amnesia in China](https://globalchinapulse.net/character-amnesia-in-china/)

我现在也经常提笔忘字，甚至有时候长时间的看一个字，会去怀疑这个字的写法是否正确。
周围有几个同事日常靠书写来找寻内心的平静，也许他们不面临这个问题。

日语韩语不面临这个问题么？

---


## 书影

《外面是夏天》，金爱烂。我太喜欢金爱烂了，之前看过的《你的夏天还好吗》就很喜欢，韩国的文化背景和我们相同，写的是现在的故事，每个故事都看的我心痛，但是又在感慨为什么能写的这么好。她对生活观察的非常细致，擅于解读人物的内心，能够用简洁的语言描写出来，我在读的时候，仿佛书中的故事和人是存在在我的生活中。这本书的译者序完全说出了我读书时候的感受：

> 我认为，每个金爱烂的读者都可以非常轻松地接受到一个讯号：她的故事与“个体”密切相关，每篇故事中一个或两个人物，他们作为个体的处境，他们内心深处的惶恐，他们身处茫茫人世间必须表面做出来的镇定——每一个个体都没有经过符号化的处理，并未刻意被赋予某种“典型环境”之下的含义。

> 我认为，每个金爱烂的读者都可以非常轻松地接受到一个讯号：她的故事与“个体”密切相关，每篇故事中一个或两个人物，他们作为个体的处境，他们内心深处的惶恐，他们身处茫茫人世间必须表面做出来的镇定——每一个个体都没有经过符号化的处理，并未刻意被赋予某种“典型环境”之下的含义。

> 但金爱烂的可贵之处在于，所谓的“社会话题性”在她的作品里并不是目的，而是场景中的一个因素；换句话说，高压的生活环境与氛围对人的碾压虽然残酷，但这只是“人生”这趟残酷之旅的一部分。除却环境高压带给人的负面影响，一个卑微的人必须经历的，还有突如其来的生离，没有预料的死别，以及种种让人猝不及防之下看清自己的欲望或脆弱的瞬间。


《外面是夏天》这本书主要讲的是失去，译者说“每篇小说都弥漫着淡淡的丧失感”​，我现在已经到了身边可能会发生“失去”的年纪了，可是我不知道该如何面对失去。有些失去是淡淡的，渐进式的到来，你有所感知，有些失去是突然的，就像一辆卡车向你撞击。作为一个现代社会的成年人，被撞了之后，好像只能装作无事发生，继续扮演自己的角色，继续过着之前的生活，其实我们知道，有些事情不会去触碰了，我们潜意识里会避开它。当你以为你已经可以从容的面对的时候，也许很久之后的某一天，它会突然再次倒车撵过你。“和熟悉的事物告别，这是大人也不擅长的事。”。


> 琐碎而无聊的日子一天天积累下来成为四季，四季积累下来就是人生。

> 尽管只是名义上属于我，其实并不是我的房子。漂泊二十多年，终于有了在某个地方扎下细根的感觉。一棵刚刚钻出种子的根穿透黑暗破土而出，弥漫四周的微热和叹息如数传入我的体内。下班后洗完澡躺在床上，奇异的自豪和不安同时向我袭来，感觉好像历经千难万险到了某个地方。尽管不是中心，却也没有被赶到外面，安心感犹如叹息般油然而生，又有些疲惫感，疲惫感中夹杂着今后可能遇到的疲惫和懂得什么是疲惫的疲惫。即便这样，我还是极力不往坏处想。我努力让自己相信，我选择的不安是全世界所有家长都要承受的不安中相对较好的不安。这在某种程度上是事实。至少我还拥有选择的自由。

> 我和你分手不是因为你没有钱，没有成为公务员，也不是因为你拿回了保证金。只是我心里的某种东西消失了，好像没什么办法挽回。

> 大人是不会轻易分手的。发现彼此之间有无法重合的间隔，也不一定就意味着分别......不过有的人最终还是要分手，并不一定是谁做错了，每个人都尽了全力，还是会发生这样的事情。因为彼此的存在方式和重力的缘故，不是不见，而是无法相见。

> “理解”是需要姿态的，就像躺着就要摘掉帽子，感到疲劳的时候最先扔掉的就是它。





## 碎碎念

* 安卓上的 GKD 很久之前试用过，当时还存在误触发的情况，现在的版本使用体验已经好很多了。
* 饿了么的优惠越来越少了，最近改用美团
* Linus 教我学俚语，Troll 是指在网上故意发布攻击性或挑衅性消息的人
* Follow 无法自己控制抓取频率，比如我日常早上会看一些咨询类，我知道对方会在早上更新，但是 Follow 现在貌似无法自动根据 RSS 更新频率来调整抓取频率。而且看上去后续会根据用户助力 Power 来提高频率。
* 聊胜于无，比完全没有稍微好一些。 这个成语是褒义词还是贬义词？ 
* 每次遇到问题 debug 的时候，看到那些恨不得什么日志都不打的服务就头疼。
* vscode 的新功能大部分都是 AI 相关的，有些无趣，有有些无奈。现在对于 Copilot 的使用太初级了，vscode 关于 Copilot 的帮助文档那么多，一定有很多有用的东西，应该花时间好好看一下。
* 今天是万圣节，但是感觉已经过去了很久一样，没有万圣节。
* Google doc 支持把文档下载为 Markdown，我在想文档中的图片怎么搞，原来是直接 Base64 存在Markdown 文本本身了。
* 汉堡王现在好难吃，不能再吃了
* 在问 AI 问题的时候，不要将自己理解（猜测）的答案告诉 AI，应该让 AI 去回答问题，然后与自己的答案做比较。
* 统计学里面的门道太多了，全是手法没有感情。因为统计学上的数字吵起来，没必要。
* 在谈论文化传播影响力的时候，与金钱收益相关么？一些人听到有人说 kpop 的文化影响力，就拿原神比较，直接算金钱收益的话，比不上原神，但是原神有文化影响力么，什么文化？Rose 的 apt 这首歌让世界上大部分人知道韩国的一个酒桌游戏，国内会有这样一首歌么？不会有。
* B站呆若木一说，之前歌手收歌，都是一整首的收歌，然后去制作发型。现在是分段收歌，主歌和副歌的作者完全不认识？？？

