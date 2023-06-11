---
title: Weekly Issue 2023-06-11
date: 2023-06-11
tags:
- Weekly
description: 
---


## 文章

### 技术


[OAuth Authentication with Flask in 2023 - miguelgrinberg.com](https://blog.miguelgrinberg.com/post/oauth-authentication-with-flask-in-2023)

[[Flask]] 实现[[OAuth]] 示例，介绍了如何配置 Provider，如何设置 callback url ，如何使用 authorization code 获取 access token 流程。代码很清理，不到 200行，很适合了解 [[OAuth]] 。

代码地址： [GitHub - miguelgrinberg/flask-oauth-example: Example code from my "OAuth Authentication with Flask" article.](https://github.com/miguelgrinberg/flask-oauth-example/tree/main)

---


[Trailing Dots in Domain Names](http://www.dns-sd.org/trailingdotsindomainnames.html)

关于域名中最后的 `.` 介绍和说明：如果是 `www.example.com.` ，那么就是绝对域名；如果是 `www.example.com` 那么就是相对域名，在应用了每个DNS搜索列表中总是隐含的". "后，变成了`www.example.com.` ；如果输入 `www` 并且 DNS 搜索域中包含 `example.com` ，那么会得到 `www.example.com.`

---

[DNS Lookups in Kubernetes](https://mrkaran.dev/posts/ndots-kubernetes/)

[[kubernetes]] 中 [[DNS]] 解析的优先级，可以直接硬编码 FQDN 来减少无效解析。

---

[Nginx Buffer 机制引发的下载故障 - poslua | ms2008 Blog](https://ms2008.github.io/2021/04/08/nginx-buffer/)

[[Nginx]] 请求响应太大，超过`proxy_max_temp_file_size` 引发的连接超时现象。官方 Ticket 链接： [#1472 (Downloads stop after 1GB depending of network) – nginx](https://trac.nginx.org/nginx/ticket/1472)  

解决方式：
- 调大 `proxy_max_temp_file_size` ，需要保证其大于所有的请求响应。
- 调小 `proxy_max_temp_file_size`， 不让后端超时。

---

https://ma.ttias.be/theres-more-than-one-way-to-write-an-ip-address/

日常不会使用，但是可以了解的 [[ip]] 地址小技巧。

`ping 0 ` 会转换为 `ping 127.0.0.1`
 
`ping 127.1` 会转换为 `ping 127.0.0.1`

`ping 10.0.513` 会转换为 `ping 10.0.2.1`

可以直接 ping 十进制、十六进制、八进制 IP 地址： `ping 167772673`

---

[Move over, Dockerfiles! The new way to craft containers](https://www.chainguard.dev/unchained/move-over-dockerfiles-the-new-way-to-craft-containers)

[[apko]] 的推广文章，主要介绍了目前非主流的集中构建[[image]]工具，[[apko]] 所有的文件来源均是 [[apk]] ，这样可以保证文件是可追溯的，类似于Linux 发行版中所有的文件均来自于[[RPM]]或 [[dpkg]]。同时[[chainguard.dev]] 提供了[[melange]] 用于帮助用户快速的将自己的项目构建[[apk]]，至少理论上可以极大的降低用户成本。


---

[Kubernetes CronJobs at Scale Part 1 by Kevin Yang | Lyft Engineering](https://eng.lyft.com/improving-kubernetes-cronjobs-at-scale-part-1-cf1479df98d4)

[Kubernetes CronJobs at Scale Part 2 by Kevin Yang | Lyft Engineering](https://eng.lyft.com/how-we-learned-to-improve-kubernetes-cronjobs-at-scale-part-2-of-2-dad0c973ffca)

将定时任务从[[crond]] 切换到 [[kubernetes]] [[cronjob]] ，可以灵活的分配资源，但是带来了很多不确定性，由于[[cronjob]] 自身机制（Reconcile、scheduler、sidecard）的启动延迟，监控指标的缺失导致开发人员无法及时获取自己的定时任务是否失败，为什么失败，后续如何手动触发等等。第二篇博客中提到了解决方式，其中关于定时任务的一些监控指标很有用，可以比较清晰的反应定时任务的状态。

### 生活

[影响力的利弊 -#36 - GeekPlux](https://geekplux.com/newsletters/36)
	想到了[[谐星聊天会]] 的威哥，最开始流量和影响力很小，还可以实名，随着影响力越来越大，隐私一点点的消失，在当下言论环境下明显安全会受到威胁，现在直接消失不见。

---

[我在北邮被偷喜茶后的338个小时 – Hzao's Blog](https://blog.hzao.top/2023/05/27/bupt-heyteaevent/)

佩服这位同学，可以很认真很友善的进行沟通，很多时候大家都想当和事老，第三者通常都会和稀泥，对事情的解决没有任何帮助。

---

[Questionable Advice: “How can I drive change and influence teams…without power?” – charity.wtf](https://charity.wtf/2023/06/05/drive-change-and-influence-teams-without-power/)

了解当前状态，倾听大家的想法，开始干（demo），然后推广，后续迭代。

---

[Some blogging myths](https://jvns.ca/blog/2023/06/05/some-blogging-myths/)

找到自己感兴趣的话题，然后编写成文章，文章尽量假象一个读者，如果想不到，name假象这个读者是过去的自己。即使很多话题已经有了很好的文章，很有可能随着时间的变化存在部分不适用的地方，也需要更新。只要能帮助到一个人也是好的。

---

## 书影

《深入理解 Linux 网络》，本周没有继续读。

《聋哑时代》，读完了，边读边回忆自己的初中生活，很多人都能对号入座，那时候的生活是单纯的。

《浪漫医生金师傅》，很久之前朋友推荐的韩剧，最近剧荒捡起来了，目前感觉剧情有些套路，但是还是在线的。

《我们之间没有的》，最近几年日本有不少剧集在讨论两性话题的，奈绪真好看啊。
