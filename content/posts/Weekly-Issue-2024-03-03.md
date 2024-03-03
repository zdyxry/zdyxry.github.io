---
title: Weekly Issue 2024-03-03
date: 2024-03-03
tags:
- Weekly
description:  
---


## 文章

### 技术


[GitHub - TNK-Studio/gortal: 🚪A super lightweight jumpserver service developed using the Go language. 一个使用 Go 语言开发的，超级轻量的跳板机服务。](https://github.com/TNK-Studio/gortal)

一个简单[[跳板机]] 实现：启动一个 sshd server，来监听连接请求（使用的 [GitHub - gliderlabs/ssh: Easy SSH servers in Golang](https://github.com/gliderlabs/ssh) ），默认会进入到一个 TUI 的交互界面（使用 [GitHub - manifoldco/promptui: Interactive prompt for command-line applications](https://github.com/manifoldco/promptui) ），让用户进行用户选择、服务器选择、连接等等。

额外解析了 `scp` 命令，如果检测到 ssh cmd 是 scp 时，会采用自身实现的 scp 来上传/下载文件。

配合阅读： [How the SCP protocol works (Jan Pechanec's weblog)](https://web.archive.org/web/20170215184048/https://blogs.oracle.com/janp/entry/how_the_scp_protocol_works)， 讲解了 [[SCP]] 协议的工作模式，以及具体的示例。

---


[Netlify just sent me a $104k bill for a simple static site | Hacker News](https://news.ycombinator.com/item?id=39520776)

用户使用 [[Netlify]] 免费套餐，但是受到了 [[DDOS]] 导致要被收取大量费用，[[Netlify]] 没有账单限制。

吓得我赶紧去看了看自己的 [[Vercel]] ，看上去还在合理的使用范围内，也没有绑定信用卡，应该还好。

[ServerlessHorrors | Home](https://serverlesshorrors.com/) 收集了很多 [[Serverless]] 恐怖故事。。。

---

[Images as Code: The pursuit of declarative image builds](https://www.chainguard.dev/unchained/images-as-code-the-pursuit-of-declarative-image-builds)

[[OCI]] Image 构建，大部分还是依赖于 `RUN` 命令来实现， 的，但是 `RUN` 命令会是的多架构场景变得困难，且不是 Reproducibility 的。

我们期望的是 Image 中只有应用程序自身，不包含其他的东西，对于应用来说，大部分通过 `pip install -r requirements.txt` 或等价操作来完成应用程序自身的构建，但是对于 Base Image 的构建问题没有解决，已有的发行版 Image 大部分都是采用 `RUN` 和包管理器(apk/apt/yum) 来构建的，在构建过程中无法保证所有的内容都有对应的包管理，所以难免会使用 `curl` `tar` 。

[[chainguard.dev]] 开发了 [[apko]]， 一个基于 apk 包管理来构建 Image 的工具，用户编辑 apko file 来定义 Image 内容，因为基于包管理器，Image 的所有文件都来自于 apk，可追踪和验证，提供的 Image 也是 Reproducibility 的。（这带来了引申问题，就是如果构建 apk 包？同步开发了 [GitHub - chainguard-dev/melange: build APKs from source code](https://github.com/chainguard-dev/melange) 用来快速构建 apk。）

此时用户通过上述工具得到的能力：构建一个 Reproducibility 的 Image。

但在构建 apko 的时候，存在大量命令式的编排脚本，这个是不可重现的，于是作者开发了 Terraform Provider 来解决 apko 构建问题。

疑问：
- 这里重点好像是 [[SBOM]] 和 [[cosign]] 配合？ [[cosign]] 和[[SBOM]] 解决的是什么问题？
- 为什么 [[chainguard.dev]] 没有采用 [[RPM]] 或者 [[DEB]] 呢？

---



### 生活

[Austria: A Fearful Country In Need Of A Vision | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2024/2/26/austria-needs-a-vision/)

[[Flask]] 作者对 [[奥地利]] 的简单介绍。读完就是一个词：保守。做什么事情都需要许可，并且有些许可不容易获得。

>It got dealt an amazing hand but it's just to afraid of playing it.

---

[Imperfect your memories - Austin Kleon](https://austinkleon.com/2023/02/26/imperfect-your-memories/)

你今天不知道将来你到底想记录今天的什么，在可能的情况下可以记录尽可能多的信息。

我目前在笔记中尽可能的记录多的信息，比如碎碎念，或者一些零星的想法。最近打算零星的拍点视频，上传到各个社交媒体上保存，自己还没有 NAS ，本地就先不保存了。

---

[Why time seems to pass faster as we age - Inverted Passion](https://invertedpassion.com/why-time-seems-to-pass-faster-as-we-age/)

为什么随着年龄的增长，时间好像过得很快？

作者认为是大脑进化为一个高效的存储设备的结果，人们期望接下来发生的事情是可预测的，所以会记录很多已有的信息，任何新发生的事情都是已有记忆中的一个 diff 结果。 当生活中开始重复时，新发生的事情就变得越来越少。

如果想要感觉时间变得很慢，那么可以拥抱变化，让未来不可预测。但是随着年龄的增长，大家会倾向于留在舒适区中。

**变化越小，那段时光就越不值得纪念。**

---


[县城中产的人情经济学-虎嗅网](https://www.huxiu.com/article/2730666.html?f=wangzhan)

人情世故，难也不难，就是看有没有利益关系。


## 书影

《周处除三害》，好看，有些血腥。 其中关于邪教的部分，应该有很多类似的片段，比如《模范出租车》第二季中就有，所以在看的时候有很熟悉的感觉。



## 碎碎念

* 需要掌握一个新的技能：装死。

