---
title: Weekly Issue 2023-08-27
date: 2023-08-27
tags:
- Weekly
description: 你的夏天还好吗？
---


## 文章

### 技术

[Code-first vs. Product-first](https://thezbook.com/code-first-vs-product-first)

> If the product doesn’t work well, the code is not good.  

---

[Scripting with Go — Bitfield Consulting](https://bitfieldconsulting.com/golang/scripting)

用 [[Unix]] 命令风格来写 [[Golang]]，比如 `script.Args().Concat().Match("Error").First(10).Stdout()`

甚至内置了 `jq` : `data, err := script.Do(req).JQ(".[0] | {message: .commit.message, name: .commit.committer.name}").String()`


---

[OpenTF Foundation](https://opentf.org/announcement)

[[OpenTF]] 已经确认，即将 fork [[terraform]] 来保证开源协议的可用性。期待故事后续的发展。有没有可能像 [[RHEL]] 和 [[centos]] 一样，因为开源版本，社区更加繁荣？


---

[重定向xboxlive系列CDN到国内节点以加速下载 - TERRYCHAN.ME](https://blog.terrychan.me/2021/redirct-xboxlive-cdn-to-china)

劫持 DNS 配合 HTTP 重定向，来加速下载。

---

[由 HTTP Header 引起的请求超时问题排查](https://selfboot.cn/2023/08/08/http_100_continue/)

HTTP `Expect: 100-continue`  导致的请求超时问题，很多服务没有很好的支持这个 header，慎重使用，但是对于 libcurl 自动添加的这种，除了踩坑知道也没什么好的办法。


### 生活



[個人域名郵箱免費方案 - Just lepture](https://lepture.com/zh/2023/free-email-provider)

配置个人邮箱域名，使用 [[CloudFlare]]的 Email Routing 来接受邮件，使用 [[AWS]] SES 设置发送邮件，包含了 DKIM 验证（可以防止邮件进入垃圾箱）。


---

[Ego death. | Kris Nóva](https://krisnova.net/posts/ego-death/)
	
Kris Nova 担心社交媒体正在恶化人们的自我中心和虚荣心，认为社交媒体鼓励人们展示自己的道德品质和获取外在关注，而不是真正关注他人或采取行动，大家追求这些多于对自身的关注。   
退出了社交媒体，进行登山攀岩，帮助她重新找到自我。     
不幸的的是，Kris Nova 离开了我们，恰好也是因为登山攀岩的意外。某种意义上，在追寻自我的过程中离去，可能也是一种幸福。     

---



[让我们粗鄙一点 | Kivinsae's Nest](https://www.kivinsae.com/2023/08/23/2023-08-24-talking_with_people/)

多观察，保持宽容。我自己日常为了防止自己只看到自己安全区的内容，看到一些不舒服的观点，也不会主动的去屏蔽或者取消关注，而是保留着，让自己知道还有这些思考的角度。


---

[用ChatGPT写日记 | CreativityOverflow](https://quail.ink/goldengrape/p/write-diary-with-chatgpt)

作者用 [[ChatGPT]] 记录日记一周，感受很好，这里是详细的 prompt。

我觉得直接发给 [[ChatGPT]] 在国内的环境下还是不太方便，可能需要用其他的形式来中转一下，定期投喂，可能比较好。

---



## 书影


《你的夏天还好吗？》，推荐这本韩国作家写的小说，其中一篇在上班路上看哭了，写的很真实，发现优秀的作家对于生活的细节观察总是独特的。

《超异能族》，在现在韩剧都很烂的时候，有这样一部制作精良的剧，真幸福。其中高允贞演高中生不违和，听说后续主要是父辈的戏码，期待一下。


《黑白魔女库伊拉》，《狼狈》，很早之前看过的两部电影，周末的时候突然想起来，在豆瓣上补标一下。




