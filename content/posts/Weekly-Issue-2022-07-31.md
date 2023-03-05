---
title: Weekly Issue 2022-07-31
date: 2022-07-31 23:59:00
tags:
- Weekly
description: 记录一下自己每周读过的文章，看过的电影，阅读过的书籍。
---


## 文章

### 技术


[一些 System Design 面试的建议](https://sichengingermay.com/how-to-do-system-design-interview/)

明确需求；定义系统接口和业务 Entity；画一个架构图；讨论具体细节。

---

[A Checklist Manifetsy](https://www.etsy.com/codeascraft/a-checklist-manifetsy)

维护自己的检查清单可以对所做内容更有掌控感。

---

[Alerts, what are they good for?](https://medium.com/@tophatengblog/alerts-what-are-they-good-for-fe085e9ab4db)

如何设置报警规则？在我司通常是依靠经验拍脑袋。作者提出了一个可以量化的规则来 评估规则：

影响：越严重则数值越大

频率：发生频率越高，则数值越大

可恢复性：如果涉及到的问题所需要手动工作量越大，则数值越大

最终计算方式为`(i+f)*r` ，作者给出了数值建议：

> **1–19** ignore  
**20–49** alert  
**50–79** evaluate the event. is it rated properly and if yes, what improvements can be made if any. The below example of US East 1 going down is a worse case scenario that relies on DR however, with good monitoring, can be detected and actioned  
**80–100** IMHO, any event with this scoring should NOT exist and if it does, we are in dire trouble

---

[为什么浮点运算不精确](https://blog.shell909090.org/blog/archives/2885/)

---

[Open Source is Not About You](https://gist.github.com/richhickey/1563cddea1002958f96e7ba9519972d9)

关于[[开源]] 的讨论

---

[User settings, Lamport clocks and lightweight formal methods](https://jakub-m.github.io/2022/07/17/laport-clocks-formal.html)

辅助阅读：[周刊（第21期）：Lamport时钟介绍](https://www.codedump.info/post/20220703-weekly-21/)

---

[The RED Method: key metrics for microservices architecture](https://www.weave.works/blog/the-red-method-key-metrics-for-microservices-architecture/)

[[weaveworks]] 关于设置监控指标的分类方法 `RED`：

Rate，服务每秒请求数

Errors，每秒失败的请求数

Duration，每个请求耗时分布

---

[The USE Method](https://www.brendangregg.com/usemethod.html)

Utilization：以一定时间间隔内的百分比表示。例如，“一个磁盘以 90% 的利用率运行”。

Saturation：作为队列长度。例如，“CPU 的平均运行队列长度为 4”。

Errors：错误事件的计数。

---

[Vertical CPU Scaling: Reduce Cost of Capacity and Increase Reliability](https://eng.uber.com/vertical-cpu-scaling/)

通过合理计算 Pod 的 CPU 使用率和预期可以容忍的可能故障，来计算最终分配给 Pod 的CPU core。

The reason for this is that responsibilities within a storage cluster can change over time, and all pods must therefore be allocated sufficient resources so that they can become the busiest pod in the cluster.

采集过去14天 Pod 的 CPU 利用率，在这些数据中，提取每8小时 P99 数值，选择利用率最高的 Pod 作为集群基准，利用率最高的 Pod 数据中的第三高作为最终用于计算额度的数值。Quota = Peak usage / Utilization target。

---

[三种git流程以及发版模型](https://jiajunhuang.com/articles/2022_07_28-git_flows.md.html)

多种 Git 开发流程对比。

---

[A toy remote login server](https://jvns.ca/blog/2022/07/28/toy-remote-login-server/)

实现一个简单的远程登录 Server，需要注意 tty 的使用，相关阅读可以看之前关于 tty 的介绍。



### 生活


[How do I get better at giving feedback?](https://www.theengineeringmanager.com/qa/how-do-i-get-better-at-giving-feedback/)

如何更好的进行反馈？（觉得还是看人。

---

[有哪些外行觉得丑但其实很厉害的画？](https://daily.zhihu.com/story/9751019) 

厉不厉害不知道，丑是真的丑。。。