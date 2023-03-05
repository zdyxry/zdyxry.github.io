---
title: Weekly Issue 2022-07-24
date: 2022-07-24 18:55:00
tags:
- Weekly
description: 记录一下自己每周读过的文章，看过的电影，阅读过的书籍。
---


## 文章

### 技术


[如何劫持 docker.io 的镜像流量到私有仓库](https://www.chenshaowen.com/blog/hijack-docker-io-req-to-private-repository.html#22-%E9%83%A8%E7%BD%B2-dockerio-%E7%9A%84%E4%BB%A3%E7%90%86-registry)

通过修改Client 受信证书将 docker.io 流量转发到内部其他 registry。  
问题：所有 Client 都需要进行证书配置。如果证书这环节出了问题，会引发较大安全问题。


[周刊（第22期）：图解一致性模型](https://www.codedump.info/post/20220710-weekly-22/)

通过发布朋友圈作为示例来描述：顺序一致性、线性一致性、因果一致性。

顺序一致性条件：

条件1：每个进程的执行顺序要和该进程的程序执行顺序保持一致。

条件2：对变量的读写要表现得像FIFO一样先入先出，即每次读到的都是最近写入的数据。

线性一致性条件，在顺序一致性的基础上，增加：

条件3：不同进程的事件，如果在时间上不重叠，即不是并发事件，那么要求这个先后顺序在重排之后保持一致。

因果一致性是更弱的一致性，只要满足`happen-before`关系即可。由于`happen-before`关系实际上是由Lamport时钟定义的，这是一种逻辑时钟，所以不同的读者看到的先后顺序可能会有点`反直觉`，但是只要满足`happen-before`关系就是正确的。

[工程效能CI/CD之流水线引擎的建设实践](https://tech.meituan.com/2022/07/14/cicd-pipeline.html)

美团内部 CI/CD 发展过程。在 jenkins 阶段遇到了调度瓶颈、资源管理瓶颈，Jenkins 多集群方式管理困难，转为自研。

[spf13 Google -->](https://spf13.com/p/spf13-google/)

spf13 从 [[Google]] 离职加入了Two Sigma

> When I first joined there was so much to learn about both Go and working within Google. My learning had slowed down dramatically. I was torn. I loved the team and the work we were doing, but was feeling personally stagnant.
    
    

[从一次经历谈 TIME_WAIT 的那些事](https://coolshell.cn/articles/22263.html)

通过设置 `SO_LINGER` 为 0 来避免 TIME_WAIT 过多情况。[https://github.com/tevino/tcp-shaker](https://github.com/tevino/tcp-shaker)

[DNS Incidents Like Cloudflare’s Could Turn your Status Page Useless; Here is How to Prevent It](https://statuspal.io/blog/2022-06-22-dns-incidents-like-cloudflares-could-turn-your-status-page-useless-here-is-how-to-prevent-it/)

很多公司使用`status.yourcompany.com` 来展示自己的服务状态，但是这可能会因为 DNS 问题而导致可用性变差，建议使用独立的 DNS 服务器并且使用 `yourcompany-status.com` 。

举例：

- [https://metastatus.com/](https://metastatus.com/)

- [https://api.twitterstat.us/](https://api.twitterstat.us/)

- [https://www.cloudflarestatus.com/](https://www.cloudflarestatus.com/)


[DNS Esoterica - Why you can't dig Switzerland](https://shkspr.mobi/blog/2022/07/dns-esoterica-why-you-cant-dig-switzerland/)

DNS 冷知识： `The default query class (IN for internet) is overridden by the -c option.  class is any valid class, such as HS for Hesiod records or CH for Chaosnet records.`

[DNS Response Size](https://www.netmeister.org/blog/dns-size.html)

关于 DNS 请求响应大小的验证，通过不断地调整 DNS 解析大小来理解完整的请求流程。

DNS Packet Size限制在 512Byte 么？可以通过 `UDP payload size` 允许更大 size，当 size 更大时，会遇到 MTU 限制。更大的时候会自动切换到 TCP 进行重试，这个时候限制是 IP Packet Size 2^16=65535： `65536 bytes for DNS overhead + payload.` 。理论上我们可以设置的 A 记录大概在 4k 左右(4092)。

[Nutanix Objects Violates MinIO’s Open Source License](https://blog.min.io/nutanix-objects-violates-minios-open-source-license/)

MinIO 发表声明 Nutanix 违反了 AGPL v3协议。Hackernews 关于事件的讨论： [https://news.ycombinator.com/item?id=32148007](https://news.ycombinator.com/item?id=32148007)

[Why does Kubernetes even exist?](https://twitter.com/sidpalas/status/1549026569535963136?s=12&t=klOsSoeDfEW9Ra6ESp68HA)

为什么 Kubernetes 被需要，软件部署管理发展过程图示



[New tool: an nginx playground](https://jvns.ca/blog/2021/09/24/new-tool--an-nginx-playground/)

如何实现一个 Nginx playground：

- 写入 nginx 配置
- 创建 net namespace
- 在 namespace 中分别运行 nginx 和 go-httpbin
- 执行 curl/http 命令并将结果返回给用户

[What happens when you press a key in your terminal?](https://jvns.ca/blog/2022/07/20/pseudoterminals/)

项目地址： [https://github.com/jvns/goterm/blob/master/main.go](https://github.com/jvns/goterm/blob/master/main.go)

通过 xterm.js 和 goterm 来学习在输入按键时，发生了什么。

在使用终端模拟器(比如 SecureCRT) 时，我们通常可以选择 V100、Xterm或者 ANSI 不同的终端序列/终端类型。

ANSI转义序列：**ANSI转义序列（ANSI escape sequences）**是一种[带内信号](https://zh.wikipedia.org/w/index.php?title=%E5%B8%A6%E5%86%85%E4%BF%A1%E5%8F%B7&action=edit&redlink=1)的[转义序列](https://zh.wikipedia.org/wiki/%E8%BD%AC%E4%B9%89%E5%BA%8F%E5%88%97)标准，用于控制视频文本[终端](https://zh.wikipedia.org/wiki/%E7%B5%82%E7%AB%AF)上的光标位置、颜色和其他选项。在文本中嵌入确定的字节序列，大部分以[ESC](https://zh.wikipedia.org/wiki/%E9%80%80%E5%87%BA%E9%94%AE)[转义字符](https://zh.wikipedia.org/wiki/%E8%BD%AC%E4%B9%89%E5%AD%97%E7%AC%A6)和"["字符开始，终端会把这些字节序列解释为相应的指令，而不是普通的[字符编码](https://zh.wikipedia.org/wiki/%E5%AD%97%E7%AC%A6%E7%BC%96%E7%A0%81)。

[Coredns 源码解析：启动流程](https://www.kawabangga.com/posts/4728)

Coredns 启动流程介绍，Coredns 自身使用 caddy 作为框架来实现，在实现流程上混杂着 caddy 和 coredns 自身逻辑。

[Commit Messages Don’t Matter](https://matt-rickard.com/commit-messages-dont-matter/)

我理解作者表达的是如果把 commit msg 作为主要的文档不合适，而不是 commit msg 不重要，一个良好的 commit msg 可以帮助 reviewer 和后续改动相关代码的人快速了解之前改动背景原因(可能不是很详细)，而不需要去查看相关的设计文档或 Ticket 了解细节。


[HOW TO READ COMPUTER SCIENCE (SYSTEMS) PAPERS USING SHAMPOO ALGORITHM](http://charap.co/how-to-read-computer-science-systems-papers-using-shampoo-algorithm/)

Q：如何阅读 CS Paper？A： 按阶段重复阅读。阅读论文是一个非线性的过程，在阅读的过程中，如果在某一章节没有理解，那么重复阅读是比较好的选择，在重复阅读的同时，需要提出问题以确保我们理解了这一章节的内容。

在阅读的过程中，我们要尽可能的慢下来，在阅读过程中同步进行笔记记录可能是一个好的方式。

[Roman Khavronenko | Open-source strategy at VictoriaMetrics](https://www.youtube.com/watch?v=-DbbIZzFHIY)

[[VictoriaMetrics]] 创始人讲述 VictoriaMetrics 如何起步，为什么开源，如何找到自己的用户，在开源过程中做了哪些事情来帮助社区快速成长。

### 生活

[$9.99/MONTH](https://basicappleguy.com/basicappleblog/999month)

- 每个月花费在订阅软件上的钱有多少？可能平时吃喝开销会及时感知，但是软件上的开销很容易就被忽略掉。我自己用了一款付费软件来记录自己每个月为软件付费(是的，我为了记录又买了一个软件)，目前每个月的开销是 91元。

[糖，不那么伟大的作品丨青山资本2022年中消费报告](https://www.foodaily.com/articles/27497)

美国对国民的糖摄入推荐量为每日男性36克，女性25克，实际上他们的摄入平均数为70克。中国居民膳食指南表示，糖的摄入量每天最好不超过25克，但一听可乐就能轻松超过30多克糖。

GI（glycemic index）值指摄取某种食物后对人体血糖上升影响的速度。低GI食物在肠胃中停留更久，吸收率更低，更能增加饱腹感，降低进食欲望。高GI食物则会让血糖升高更快，胰岛素分泌增加，饿得更快。长此以往，不仅会让胰岛素过于兴奋，还抑制脂肪分解，促进脂肪合成。虽然胃里的食物其实足够了，但饥饿感带来的难以控制的加餐，使得摄入能量远超身体实际需要的。

[坚持跑步对身体到底好不好？](https://www.notion.so/2022-07-24-150c9e8f32744d7297a2124a1677e4bc)

**仅跑步 10 分钟，就能增加大脑中流向双侧前额叶皮层各个位点的局部血流量，从而有益于心理健康、增强执行能力**。

“我们的研究表明，**仅需 6 个月的锻炼，就有可能逆转衰老对血管的影响。在 21 岁 -69 岁不同年龄段的健康人群中，普遍能观察到这些益处。**这强调了**改变生活方式以减缓衰老相关风险**的重要性，特别是在年龄较大、基础较弱的人群中，开始跑步也似乎永远不会太晚。”


[用了很久的全拼改为双拼值得吗？](https://www.zhihu.com/question/383416202/answer/2584564433)

优势：确定性(每次输入两个按键来完成一个文字的输入)；快(只需要输入2个按键)；

劣势：多平台适配；学习成本；


## 书籍

《职场妈妈不下班》： 婚姻中男性与女性对于家务劳动的付出的探讨，介绍了多个不同家庭的婚姻生活示例，来讲解不同类型/态度的人对于家庭生活付出的想法，想法的成因(往往是人原生家庭影响)。婚姻生活就是不断妥协的结果，几乎是一种潜规则，你不说，我不说，日子就继续这样过下去。原生家庭对于一个人的影响是看得见的，影响时间也远远超出一代人的范围。