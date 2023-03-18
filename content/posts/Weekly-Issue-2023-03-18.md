---
title: Weekly Issue 2023-03-18
date: 2023-03-18
tags:
- Weekly
description: 有脱口秀陪伴的一周。
---


## 文章

### 技术

[After four years of SMR storage, here's what we love—and what comes next - Dropbox](https://dropbox.tech/infrastructure/four-years-of-smr-storage-what-we-love-and-whats-next)

与 [[Backblaze]] 不同， [[Dropbox]] 目前大量使用[[SMR]] 磁盘。密度高，省电，服务器数量减少，维修成本降低。

---

[简单聊聊 IaC：Infrastructure as Code - Manjusaka](https://www.manjusaka.blog/posts/2023/03/12/a-simple-introduction-about-iac/)

最近在使用 [[Packer]]配合 [[terraform]] 来帮助我自动的创建一些环境（虚拟机），我的创建是 [[vSphere]] 已经存在，如果只是创建新的虚拟机，那不会遇到太多问题，但是如果我想要针对某一个[[vSphere]] 集群中的所有主机增加一个 vswitch，然后新创建的虚拟机关联的是对应的 vswitch，这个需求就很难做到，首先想要从集群获取到所有主机，就需要先 import resource，而 import resource 和 code 中定义的 resource 中的状态是有很大差别的，所以import resouce 之后，需要去更新 code 中定义的对应 resource，然后继续后续步骤，整体流程一点也不 [[IaC]] ，社区中有一些自动 import resource 并生成 code 的项目，但是对于各个 provider 的支持力度有限，感觉这个场景应该在 [[terraform]] 中做，而不是去适配。

---

[[Ipmitool-devel] GitHub account suspended | IPMItool](https://sourceforge.net/p/ipmitool/mailman/message/37787037/)

[[ipmitool]] 项目被 [[github]] 归档，目前可能得原因是维护者是俄罗斯人，所在公司被制裁。

---


[How Kubernetes Validates Custom Resources · Daniel Mangum](https://danielmangum.com/posts/how-kubernetes-validates-custom-resources/)

讲解 [[CRD]] 如何进行校验，附带一个最小实现示例。

---

[AWS is Asleep at the Lambda Wheel - Last Week in AWS Blog](https://www.lastweekinaws.com/blog/aws-is-asleep-at-the-lambda-wheel/)

[[AWS]] 对于各个语言的运行时支持不是很积极。

---

[Scaling AutoBuild: Our Journey Towards Delivering An Enhanced Customer Experience | LinkedIn Engineering](https://engineering.linkedin.com/blog/2023/scaling-autobuild--our-journey-towards-delivering-an-enhanced-cu)

[[linkedin]] 的 [[AutoBuild]] 架构演进。[[AutoBuild]] 是用来管理 [[BareMetal]] 的内部工具，随着新增节点和原有节点重置之前的动作混合，带来了很多问题，比如任务优先级，消息队列不稳定导致的消息丢失，存在单点故障。所以开发了 V2 版本来解决上述问题。

---

[DNS Outage on 2023-01-25 | Inside Rust Blog](https://blog.rust-lang.org/inside-rust/2023/02/08/dns-outage-portmortem.html)

使用[[Terraform]] 进行环境管理中出现的问题，根本原因是执行一次变更中包含了多个内容，导致在进行状态比对的时候将多个资源进行了状态变更，从而引发了问题。
经验教训：测试环境中的变更需要依次在生产环境中执行变更，尽量避免一次进行多个资源状态变更；尽量减少测试环境与生产环境的偏差。

---

[The yaml document from hell](https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell)

又是一片吐槽[[YAML]] 的文章，结论中推荐使用[[TOML]] 。

---

[Benchmarking Kubernetes node initialization - Symbiosis](https://symbiosis.host/blog/comparing-node-launch-times)

在[[公有云]]上创建 [[kubernetes]] 节点的 [[benchmark]]，不知道当考虑 scale 的时候是否能够满足用户需求。

---

[详解 TCP 半连接队列与全连接队列 - 个人笔记](https://wgzhao.github.io/notes/troubleshooting/deep-in-tcp-connect/)

[[TCP]] 半连接队列与全连接队列相关参数理论及验证。在[从一次线上问题说起，详解 TCP 半连接队列、全连接队列-51CTO.COM](https://www.51cto.com/article/687595.html) 的基础上补充了全连接队列验证的抓包结果。


### 生活


[Please Mind Your Metaphors · Daniel Mangum](https://danielmangum.com/posts/please-mind-your-metaphors/)

在使用隐喻的时候，需要注意，是否为了使用隐喻，而又补充说明了很多与隐喻不相同的点。

---


## 书影

《毫无意义》，伍迪艾伦的自传，刚开始看。

《姨妈的后现代生活》，值得思考。

《重启人生》，如果会重新来过，会选择走一样的路，还是完全不同的路。

