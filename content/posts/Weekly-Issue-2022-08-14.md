---
title: Weekly Issue 2022-08-14
date: 2022-08-14 13:00:00
tags:
- Weekly
description: 记录一下自己每周读过的文章，看过的电影，阅读过的书籍。
---


## 文章

### 技术


[2022-31: Databend 的工程效率实践](https://xuanwo.io/reports/2022-31/)

[[Databend]] 效率工程介绍，使用 SaaS 来完成大部分工作，Self Host Github Runner 尽量使用 [[AWS]] 内部服务，来减免流量费用。

效率工程体会：

- 摆正定位
- 渐进变更
- 公开透明

---

[Improving the Experience of Making Envoy Route Changes](https://eng.lyft.com/improving-the-experience-of-making-envoy-route-changes-2a25dc8e1d44)

[[Lyft]] 针对 [[envoy]] 配置方式进行的改进，原有存在的问题：

原有路由配置使用[[Jinja]] 模版进行维护，无法进行很好的语法检查和验证，现已替换为 [[Golang]]

原有 [[envoy]] API 在配置平面和控制平面都被引用，当 [[envoy]] 升级时，都需要考虑兼容性问题，现在只在控制平面引用

原有[Route table check tool](https://www.envoyproxy.io/docs/envoy/latest/operations/tools/route_table_check_tool#route-table-check-tool) 无法进行很好的分发（为啥一个 binary 会不好分发呢？），改为内部检查工具，并添加了 CI 检测结果。

---

[容器 CPU 和 Memory 限制行为简述](https://www.manjusaka.blog/posts/2022/08/07/A-simple-introduction-about-cpu-and-memory-limit-in-docker/)

关于 CPU 和 Memory cgroup 基本配置参数介绍。


---

[Avoiding CPU Throttling in a Containerized Environment](https://www.uber.com/en-SG/blog/avoiding-cpu-throttling-in-a-containerized-environment/)

[[cgroup]] 使用 cpuset 来避免 CPU throttling 。

---

[How to remove a stuck namespace](https://blog.ediri.io/how-to-remove-a-stuck-namespace)

[[kubernetes]] 如何删除 namespace，通常是因为 [[Finalizers]] 。

---

[“Who Should Write the Terraform?”](https://zwischenzugs.com/2022/08/08/who-should-write-the-terraform/)

应该谁来写 Terraform ？要根据实际组织情况来看，我理解最终期望是 Developer 来写。配合阅读 [Developers Should Deploy Their Own Code](https://matt-rickard.com/developers-should-deploy-their-own-code)

---

[HashiCorp 2022 State of Cloud Strategy Survey](https://www.hashicorp.com/state-of-the-cloud)

[[hashicorp]] 关于 Cloud 的调查。multi-cloud 已经是事实，大多数是独立的团队来维护 multi-cloud 资源。其中 94% 认为存在资源浪费的情况。

---

[Use One Big Server](https://specbranch.com/posts/one-big-server/)

作者表达的观点是，使用一台顶配的服务器可以承担很多服务，垂直扩展的方便程度也远胜于水平扩展。如果从可用性角度，可以使用公有云，但不要完全的使用公有云，公有云的溢价是明显的。但这都是在业务场景规模很大的基础上，如果业务规模很小，那么按量付费是一个好的选择。

---

[When Microservices Are a Bad Idea](https://semaphoreci.com/blog/bad-microservices)

什么时候应该进行[[微服务]] 设计？除非理由非常明确，否则不要这样做。

当现有程序还在运行良好的情况下，进行很好的模块拆分可能比直接拆分为微服务是一个更好的选择，前者本身也是后者的一部分。进行微服务设计的前提是基础设施足够完善。

---

[How Kubernetes Reinvented Virtual Machines (in a good sense)](https://iximiuz.com/en/posts/kubernetes-vs-virtual-machines/)

从应用部署的角度来讲解为什么我们需要[[容器]] 和 [[kubernetes]]。之前还有从应用发布的角度（binary -> tar -> rpm/deb -> container）来讲解为什么需要[[容器]]。


### 生活

[打工人为什么会集体落入“狗屎工作”陷阱？](https://daily.zhihu.com/story/9751475)

> [《 毫无意义的工作》](https://book.douban.com/subject/35929434/)

> **毕竟，我们已经处在一个“狗屎工作”泛滥的时代。而如果这种“狗屎性”来自于一种体系性的力量，带有一点略微不可抗的时代性色彩，那我们就更加需要对自己的工作有更多的反思。**  
最后，也是格雷伯在本书结尾时递上的一碗“鸡汤”：  
**“大部分人喜欢在抽象层面谈论自由，甚至声称自由是最重要的事情……但很少有人去思考自由的生活具体意味着什么。”**  
**因此这本书的目的不是提出解决方案，而是倡导大家去思考和讨论真正的自由，对“正常”有更多的反思。**  
“狗屁工作是一扇窗”。  
它既外看社会，也内观人生。
    

---

[Shopee 衰落幕后：一家最像中国大厂的东南亚巨头的全球化乱局](https://mp.weixin.qq.com/s/3AJ32QiIFz-5xzWiiyCHIA)

[[Shopee]] 的观察文章

---

[《甜蜜蜜》明明是一部悲剧爱情电影，为什么片名要叫「甜蜜蜜」？](https://daily.zhihu.com/story/9751613)

小人物的爱情总是甜蜜的。


## 书影

《应得的权利》

这本书是在阅读 [[《从零开始的女性主义》]] 和 [[《职场妈妈不下班》]] 之后的第三本关于女性主义的书，相比前两本，这本书讲述的场景更多，让人产生思考也更多，更系统的描述了男性与女性在日常生活中所面临场景的不同，以及男性拥有了哪些不属于自己的权利。当我们在觉得一件事情理所当然的时候，我们就应该反问自己，为什么。比如为什么大家觉得男性会更能忍受痛苦(从而导致在表述相同痛苦时，女性很难得到同等对待)？为什么上司敬酒大部分女性会迫于“社会规则”压力去敬酒？为什么性别相关的恶性犯罪新闻经常使用被动句？作为男性，当面对这类事情发生时，我可以做些什么？