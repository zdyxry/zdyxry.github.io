---
title: Weekly Issue 2022-11-13
date: 2022-11-13 23:50:00
tags:
- Weekly
description: I got this wrong, and I take responsibility for that.
---


## 文章

### 技术

[2022 年里做前端是怎样一种体验 - rxliuli blog](https://blog.rxliuli.com/p/ef26175b98af43ccaf918296a739ded5/)   
感觉 2016年和2022年之间发生了什么了不得的事情，各种名词给变了一圈了。

---

[Modern Python Environments - dependency and workspace management
](https://testdriven.io/blog/python-environments/) 
对 pyenv ,pip + venv, poetry, pipenv 进行了比较。

---

[Python Tools for Managing Virtual Environments](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko)       
除了针对 venv，virtualenv介绍之外，还比较了 Pyflow、Poetry、Hatch 等较新的 project management 工具。

---

[Why add another Python manager?](https://github.com/David-OConnor/pyflow#why-add-another-python-manager)        
pyflow 讲述为什么需要一个 Python 管理器。

---

[The state of Python Packaging](https://bernat.tech/posts/pep-517-and-python-packaging/)   
关于 Python 包管理演进的3篇文章。

---

[Python Meetup 第3期 | Python最新语言特征](https://www.bilibili.com/video/BV1KT4y1J7PU/?vd_source=37d54b4af4dc28a762ebf052a67761f3)   
49分38秒开始，[[PDM]] 作者讲解 PEP582 及 PDM 实现。

---

[Debian 系统上捉摸不定的 Python](https://frostming.com/2022/03-27/python-on-debian/)   
关于 Linux 发行版中 python 包路径问题。

---

[sarama producer hang 又一例](https://xargin.com/sarama-producer-hang-another-case/)   
[[sarama]] 故障排查总结。

---

[Python 3.11 类型注解新特性 | Henry Z's blog~](https://changchen.me/blog/20221106/type-hinting-python-3-11/)  

眼花缭乱了。

---

[如果编程就是写作  | Piglei](https://www.zlovezl.cn/articles/if-programming-is-writing/)
> 不过有一点我能确定的是：不论编程还是写作，只有“写”才是提升能力的唯一途径。读完 100 本写作教程、翻完 1000 个开源项目的代码，也无法让我们成为大师。所以还等什么呢？关上文章，现在就开始写吧！

---


[Why I Strive to be a 0.1x Engineer](https://benjiweber.co.uk/blog/2016/01/25/why-i-strive-to-be-a-0-1x-engineer/)
10x vs 0.1x 。只做有价值的事情，什么是有价值的事情？
> Given the cost of maintaining everything we build, it would literally be better for us to do 10% the work and sit around doing nothing for the rest of our time, if we could figure out the right 10% to work on.
> We could even spend 10x as long on minimising the ongoing cost of maintaining that 10%. Figuring out what the most valuable things to work on and what is a waste of time is the hard part.

---

[What are Containers?](https://matt-rickard.com/what-are-containers)   
简单明了：什么是[[容器]]。

---



[Information Barbell](https://matt-rickard.com/information-barbell-2)   
关于获取信息渠道，一种是经典内容，一种是直接参与者的内容。前者是经得起时间考验的信息，后者是事情的参与者，介于两者之间的信息渠道信噪比都低很多，并不会让你多了解什么，反而可能会产生误导。  
最近在了解 [[Python]] 包管理相关的内容，网上的大部分信息都是转载或者重复的，直接阅读官方文档或 Pypi参与者(如 [Bernát Gábor](https://bernat.tech/)， [Frost Ming](https://frostming.com/blog/)) 的博客是更好的选择。

---

[Blazing fast CI with MicroVMs](https://blog.alexellis.io/blazing-fast-ci-with-microvms/)   
使用 [[MicroVM]] 来运行 [[github]] actions。主要解决了直接使用 [[docker]]和 [[kubernetes]] 面临的资源隔离问题。也许 [[virtink]] 可以很好的解决这个场景？



### 生活

[苹果的偏执 | Yanng](https://xia0bs.github.io/2016/12/14/apple/)   
关于苹果公司的一些传闻八卦，大部分强调苹果对于产品质量的把控严格，对细节的极致追求。

---

[Why we auto-delete slack messages - killing tribal knowledge at Last9 | Last9 SRE Platform](https://blog.last9.io/why-we-auto-delete-slack-messages-killing-tribal-knowledge-at-last9/)   
[[Last9]] 为了让大家信息公开透明，尽量在 channel 里讨论并形成文档，限制 DM 只保留2天。
之前我们也说过尽量在 channel 讨论，但是很难做到。作为对比，我们 Slack 的消息有 65% 都是 DM，22% 是公开 Channel，其余是私人 Channel。

---

[Writing Is Magic - Marc's Blog](https://brooker.co.za/blog/2022/11/08/writing.html)

[[写作]]带来的价值，平时浪费的时间很可能是写作产出没有价值的所耗费时间的很多倍。   
清晰，可以重新整理思维，针对一个事情进行具体的梳理；   
时间，通过将想法文档化来让他人关注到具体的内容中，不会有打断；   
规模，写作的产出可以当做自己的积累，也可以让他人受益；   
权威，可能是双向的，要保持警惕；   
记忆，人会选择性的忘记一些事情，写作可以让你很好的对时间进行回顾；   

---


[Mark Zuckerberg’s Message to Meta Employees | Meta](https://about.fb.com/news/2022/11/mark-zuckerberg-layoff-message-to-employees/)   

> I got this wrong, and I take responsibility for that.


扎克伯格给 [[Meta]] 员工的信，财源 13% (11000人），降本增效。   
这能说明人们的[[社交]]文化被[[Tiktok]] 这种洞悉人性的产品给打败了么？   

> 无论是用户规模、用户粘性还是用户时长，几乎可以清晰地看到，短视频还是那个短视频，即使名字换成了Tiktok，用户换成了海外，它依然是那个洞悉人性的流量黑洞级产品。

[TikTok要教“大哥们”做事，Google、Meta要变天-36氪](<https://36kr.com/p/1808849230907017>)


---






## 书影


《100 Go Mistakes and How to Avoid Them》 ，本周读了第 11-19 个。

《三悦有了新工作》：有点悲伤。

《寒战》：确实是近些年很好看的港片。


















