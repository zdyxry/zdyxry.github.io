---
title: Weekly Issue 2023-12-24
date: 2023-12-24
tags:
- Weekly
description:  
---


## 文章

### 技术

[Debounce and Throttle | Reorx’s Forge](https://reorx.com/blog/debounce-and-throttle/)

>**Debounce**: 将间隔不超过设定时间的多次连续调用变成一次。
>**Throttle**: 确保一个函数被连续多次调用时，在设定时间内最多只实际执行一次。
>
>相似之处：Debounce 和 Throttle 都限制了函数执行的最大频率不超过每设定时间一次
>不同之处：在快速（间隔小于设定时间）连续调用时，Throttle 确保了函数会规律执行，但 Debounce 只有当连续调用放缓（间隔大于设定时间）时才会执行。

---

[关于 k8s 的 zero downtime deployment 一些建议](https://wklken.me/posts/2023/12/17/some-tips-for-zero-downtime-deployment.html)

滚动更新配置防止 502 的一些方式：
- 配置 liveness/readiness
- 配置 terminationGracePeriodSeconds
- 程序需要支持 graceful shutdown
- 主进程 pid 为 1，可以收到信号
- 通过配置 `preStop` 来保证 service endpoint 变更和 pod 删除的变更顺序

不过如果在滚动更新过程中遇到问题，需要终止，好像还是采用两套 deployment 在接入层切换多一些。

---

[2024 State of Internal Developer Portals | Port](https://www.getport.io/state-of-internal-developer-portals)

>Developers spend significant time on non-core work and face prolonged software deployment timelines

---

[Introducing Fly Kubernetes · The Fly Blog](https://fly.io/blog/fks/)

[[Fly.io]] 使用 [[k3s]] 配合 [[Virtual kubelet]] 构建自己的 [[kubernetes]] 平台，最小组件：CoreDNS，SQLite，Virtual kubelet，将 virtual kubelet 相关接口实现为自己的 Fly machine API 。

---

[Flask 已死，FastAPI 永生 | 李辉](https://greyli.com/flask-fastapi-2023/)

非常佩服[[Grey Li]]，面对这种明显是标题党的文档，还会有理有据的去回应，去证明。框架的选型是多方面的，对于文章中提到的 [[FastAPI]] 的问题，我会本能的避开。

文章中剃刀的几个Flask 类似 FastAPI 的框架，之后可以选择用用：
- [APIFairy](https://github.com/miguelgrinberg/APIFairy)
- [APIFlask](https://github.com/apiflask/apiflask)
- [Connexion](https://github.com/zalando/connexion)
- [Eve](https://github.com/pyeve/eve)
- [Flask-RESTX](https://github.com/python-restx/flask-restx)
- [Flask-Smorest](https://github.com/marshmallow-code/flask-smorest)
- [Flask-Rebar](https://github.com/plangrid/flask-rebar)
- [SpecTree](https://github.com/0b01001001/spectree)

---

[Agile has failed. Officially.. Either I’m a gifted oracle, and all of… | by Tamás Polgár | Developer rants | Dec, 2023 | Medium](https://medium.com/developer-rants/agile-has-failed-officially-8136b0522c49)

有趣，Agile 死了？我没有什么概念，我司内部好像一直 Aglie 不起来，都是瀑布式的开发流程，貌似有个小组采用了，不知道效果怎么样（听说每天的同步会议倒是没少开）。

---


### 生活

[北漂十年，搬家三十次](https://mp.weixin.qq.com/s/XaR_bpTYqF_LexzQltVgxg)
>作为一个被书籍和电影哺育大的「文青」，除了北京，伯姐不知道还能在哪里找到这类影视传媒相关的工作。
>北京这座城市欲拒还迎地向她开着一扇半掩的门，它允许你的窥探，接受你的燃烧，但始终拒绝你的进入与停留。

---

[Weaponized incompetence - Wikipedia](https://en.wikipedia.org/wiki/Weaponized_incompetence)

武器化无能，战略无能，与个人利用假装或故意的无能来逃避不必要的责任有关。

日常生活中，有表现出这个现象么？周围的人有表现出这个现象么？绝对是有的，生活中还不少。

---




## 书影

《父权制与资本主义》，从同事那里借了好久，一直没看，打算趁着年底，看完还回去。
