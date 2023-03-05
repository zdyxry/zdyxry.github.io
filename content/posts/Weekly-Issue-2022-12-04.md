---
title: Weekly Issue 2022-12-04
date: 2022-12-04 19:00:00
tags:
- Weekly
description: 克拉拉的一切品质与情感都是无法用人类的纬度去衡量的，因为，正是由于自私的欲望与升华的渴望并存，人类的心中才会充满了矛盾、彷徨与痛苦；没有了自私那下坠的重力，一切崇高、向上的人性也就虚无缥缈得失去了分量。自私是人类沉重的负担，但也许在并不遥远的未来，也会是人之所以为人的一个最重要的锚点吧。 
---


## 文章

### 技术

[聊聊 Docker 的存储驱动 Overlay2 | MoeLove](https://moelove.info/2022/11/28/%E8%81%8A%E8%81%8A-Docker-%E7%9A%84%E5%AD%98%E5%82%A8%E9%A9%B1%E5%8A%A8-Overlay2/)        
[[overlayfs]] 介绍。

---

[Ask HN: Azure has run out of compute – anyone else affected? | Hacker News](https://news.ycombinator.com/item?id=33743567)    
[[azure]] 德国无法扩容更多容量，看评论(各家)都已经遇到很多次了。

---

[Linux RT 进程引发内核频繁卡死的优化方案](https://mp.weixin.qq.com/s/EqKU052H5LxRjE68jeiaDg)    
> 经过查看内核 RT 实现，发现 RT 进程是有相关的占用时间设置的 /proc/sys/kernel/sched_rt_runtime_us ,sched_rt_runtime_us 的默认值为 950000，代表 RT 进程可以占用 95% 的 CPU 时间片，剩余 5% 用于响应其他请求，而这里比较诡异的是为什么 sched_rt_runtime_us 明明设置了 950000 这个值，surfaceflinger 这个程序为什么还能将 CPU 使用到 100% 呢？

> 经过代码分析和社区 issues 查找，**发现引发该问题的罪魁祸首是 RT_RUNTIME_SHARE 这个特性，该特性可以使 RT 任务长期占用 100% CPU, 从而使诸如 kworkers 等相关的内核任务无法获取到 CPU 资源，造成内核卡死。**而客户使用的内核版本恰好是 5.4.53 版本，该版本 RT_RUNTIME_SHARE 默认被设置为 true，5.4 的最新内核版本已经默认关闭该特性。

---

[docker buildx run yum install very slow, while docker build is fine · Issue #379 · docker/buildx · GitHub](https://github.com/docker/buildx/issues/379)   
[[docker]] build 因为 `ulimit` 配置，执行 [[yum]] 很慢。

---

[使用 neovim 作为 PDE(个性化开发环境) - 咸糖 - 自律者自由](https://vim0.com/post/neovim/)   

[[neovim]] 配置。

---



[2022-47: Databend 文档的 i18n 实践](https://xuanwo.io/reports/2022-47/)   

使用 [[github]] [[Vercel]][[Crowdin]] 工具链来进行文档翻译。

---

[Twitter 实习生 George Hotz |程序员的喵](https://catcoding.me/p/geohot/)   

[[George Hotz]] 的直播很有趣。

---

[Introducing Finch: An Open Source Client for Container Development | AWS Open Source Blog](https://aws.amazon.com/cn/blogs/opensource/introducing-finch-an-open-source-client-for-container-development/)    

[[Finch]] 通过组装 [[lima]][[containerd]] 和 [[nerdctl]] 来简化用户使用成本。

---

[Boosting Kubernetes container runtime observability with OpenTelemetry | Kubernetes](https://kubernetes.io/blog/2022/12/01/runtime-observability-opentelemetry/)   

使用 [[OpenTelemetry]] 来观测 [[kubernetes]]内部状态。   
部分 [[OCI]] 没有计划支持 [[OpenTelemetry]]，用 [[Rust]] 编写的[[youki]] 有这个计划。

---

[What is runwasi - Nigel Poulton](https://nigelpoulton.com/what-is-runwasi/)   

通过 [[runwasi]] 实现 [[containerd]] shim，来让 [[kubernetes]] 支持运行 [[wasm]]

---

[到底一台服务器上最多能创建多少个TCP连接 | plantegg](https://plantegg.github.io/2020/11/30/%E4%B8%80%E5%8F%B0%E6%9C%BA%E5%99%A8%E4%B8%8A%E6%9C%80%E5%A4%9A%E8%83%BD%E5%88%9B%E5%BB%BA%E5%A4%9A%E5%B0%91%E4%B8%AATCP%E8%BF%9E%E6%8E%A5/)     

服务器最多可以创建多少个 [[TCP]]连接： 在内存、文件句柄足够的话一台服务器上可以创建的TCP连接数量是没有限制的。

---

[Drag and drop from terminal](https://blog.meain.io/2022/terminal-drag-and-drop/)   

从 [[terminal]]直接拖拽文件

---

[Tailscale/Headscale ACL 使用教程 – 云原生实验室 - Kubernetes|Docker|Istio|Envoy|Hugo|Golang|云原生](https://icloudnative.io/posts/tailscale-acls/)   

[[TailScale]] [[ACL]] 配置方式。之前看了官方文档，但是自己的需求比较少，暂时还不需要。

---

[Building A Virtual Machine inside ChatGPT](https://www.engraved.blog/building-a-virtual-machine-inside/)    

[[ChatGPT]] 模拟一台虚拟机，实际上真的是处于模拟状态。

---

[Finding suspicious syscalls with the seccomp notifier | Kubernetes](https://kubernetes.io/blog/2022/12/02/seccomp-notifier/)   

通过 [[Seccomp]] Notifier 来追踪 [[Container]] 异常系统调用。

---

[PromCon 2022 演讲：Alerting with Confidence | 卡瓦邦噶！](https://www.kawabangga.com/posts/4860)   

> 今年在 PromCon 上做了一个演讲，介绍了从 Alert 的配置，到触发，最后 Review 的一些经验。

---

[How To Publish a Port of a Running Container](https://iximiuz.com/en/posts/docker-publish-port-of-running-container/)    

通过启动新的 [[Container]]与目标容器共享[[namespace]] 的方式来实现端口转发。

---

[一些关于时间和定时任务的库](https://colobu.com/2022/11/26/some-time-and-cron-libs/)   

[[Golang]] 第三方库，时间、[[cronjob]] 相关。





### 生活


[https://xiaowenz.com/read/read-detective/](https://xiaowenz.com/read/read-detective/)   
[[推理]] 小说推荐。

---

[The Need to Read](http://paulgraham.com/read.html)
> You can't think well without writing well, and you can't write well without reading well. And I mean that last "well" in both senses. You have to be good at reading, and read good things.

---


[Tech predictions for 2023 and beyond | All Things Distributed](https://www.allthingsdistributed.com/2022/12/tech-predictions-for-2023-and-beyond.html)   
2023 技术预测：云技术、模拟、新能源、供应链、定制芯片。

---


## 书影


《100 Go Mistakes and How to Avoid Them》 ，本周读了关于错误处理部分的第 48 - 54 个。

《人类的群星闪耀时》，不能当做历史来看。别名：西方列强闪耀时。

《克拉拉与太阳》，引用译者的话：

> 克拉拉的一切品质与情感都是无法用人类的纬度去衡量的，因为，正是由于自私的欲望与升华的渴望并存，人类的心中才会充满了矛盾、彷徨与痛苦；没有了自私那下坠的重力，一切崇高、向上的人性也就虚无缥缈得失去了分量。自私是人类沉重的负担，但也许在并不遥远的未来，也会是人之所以为人的一个最重要的锚点吧。 

《边缘世界》，弃了。











