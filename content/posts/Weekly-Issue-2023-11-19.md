---
title: Weekly Issue 2023-11-19
date: 2023-11-19
tags:
- Weekly
description:  红山动物园真不错。
---


## 文章

### 技术
[自定义 ProxyCommand 以代理 SSH 的底层连接 - 陪她去流浪](https://blog.twofei.com/887/)

当指定了 ProxyCommand 的时候，**ssh 客户端不会再自己去尝试连接服务器，而是把待连接的服务器的地址和端口作为变量并以参数的形式传递给 ProxyCommand 指定的命令；由此命令建立与服务器的连接，并通过标准输入与标准输出（分别表示网络连接的_读_与_写_）交换数据。** 

---

[两种风格的错误处理 | Frost's Blog](https://frostming.com/error-handling/)

两种处理方式：如果不主动处理错误，当发生错误时，是会上报异常，还是会忽略错误。以前我可能觉得 try...catch... 很好，但是被坑怕了之后，现在几乎所有非标准库的调用都会加 try...catch.. 了，把 python 写成了 golang 的样子。

关联阅读：[关于异常处理的总结和思考](https://blog.beautyyu.one/ideas-about-exception-catch)

---

[curl on 100 operating systems | daniel.haxx.se](https://daniel.haxx.se/blog/2023/11/14/curl-on-100-operating-systems/)

>In the curl project we work relentlessly to maintain ABI and API stability and compatibility. You can upgrade your libcurl using application from the mid 2000s to the latest libcurl – without recompiling the application – and it still works the same.

这个兼容性保证可以称得上伟大的成就。（不知道 [[curl]] 是如何进行测试的。

---

[GPT 帮我搞定了时区转换问题 - Jiajun的技术笔记](https://jiajunhuang.com/articles/2023_11_15-python_datetime_with_timezone.md.html)
`datetime.datetime.replace` 函数没有处理夏令时冬令时的问题，而是直接拿着给的 tzinfo 构建一个新的 datetime 对象， `pytz.localize` 函数处理了夏令时冬令时的问题。

---

[Vanilla software - Wikipedia](https://en.wikipedia.org/wiki/Vanilla_software)

为什么 vanilla 意味着ordinary/original/传统/原生？因为香草冰淇淋是最传统的口味。

---

[🪢 [网络协议] 浅谈 HTTP 优先级算法的演进 | 微信公众号@卤代烃实验室](https://supercodepower.com/http-prioritization)


[[HTTP]] 优先级变化，HTTP/1 没有优先级，HTTP/2 优先级非常复杂：依赖树 x 256 个优先级 x 独占位 x 动态调整，互相乘起来复杂度飙升。HTTP/3 优先级在 HTTP/2 上简化了许多。

HTTP/3 优先级 RFC：[RFC 9218: Extensible Prioritization Scheme for HTTP](https://www.rfc-editor.org/rfc/rfc9218.html)

---

[Golang Structs Memory Allocation](https://prog-bytes.hashnode.dev/golang-structs-memory-allocation)

使用 `unsafe` `Offsetof` 来查看结构体的偏移量。通过调整结构体字段顺序，来减少 padding 。

---



### 生活

[唐僧西天取经时，为什么不直接走中南半岛，而要向西绕远路？ | 国家人文历史官网](https://www.gjrwls.com/geography/20201027/505775667372097536.html)

>这条道路看似又远又艰险，但在当时，这条通道已经比较成熟，作为丝绸之路，虽然处于半干旱地区，也是沿着水源遍布城镇，而且丝绸之路不乏各地商旅，安全比较有保障。
>蜀身毒道虽然理论上距离印度最近，实则暗潮汹涌、风险重重。这么看来，玄奘选择舍近求远，也在情理之中。

---

[Vehicles with higher, more vertical front ends pose greater risk to pedestrians](https://www.iihs.org/news/detail/vehicles-with-higher-more-vertical-front-ends-pose-greater-risk-to-pedestrians)

发动机罩前缘距离地面超过 40 英寸且格栅倾斜角度为 65 度或更小的车辆，与具有相似坡度且发动机罩高度为 30 英寸或更小的车辆相比，造成行人死亡的可能性高出 45%。引擎盖高度超过 40 英寸且钝前端角度超过 65 度的车辆造成死亡的可能性高出 44%。

---

[定期回顾笔记的好处 | 安全代码](https://www.usmacd.com/cn/note_review/index.html)

最近时常也有类似的想法，前阵子看一个人的采访也看到，通过 flashcards 来定期的回顾自己学习的知识，避免遗忘。（但是 Anki 好像不怎么好用，可能要找一找

---

[Use Timestamps · Jan Kremer](https://jankremer.eu/micro/timestamps/)

非常认同，现在信息过时太快，如果发布了一篇文章，那么在显式的地方告诉我这篇信息的发布时间，会辅助我来判断这个信息的有效性，但是有些平台有意的隐藏了时间，比如知乎。

---

## 书影

本周没有任何的书影记录。

## 游戏

推荐桌游《探案实录》，合作推理类，和同事玩了 3 个多小时，做了思维导图，记了笔记，以为自己掌握了关键线索，结果还是大失败。

