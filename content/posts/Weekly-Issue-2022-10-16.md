---
title: Weekly Issue 2022-10-16
date: 2022-10-16 23:50:00
tags:
- Weekly
description: 记录一下自己每周读过的文章，看过的电影，阅读过的书籍。
---


## 文章

### 技术


[Startup Ideas I've Considered](https://matt-rickard.com/startup-ideas-ive-considered)

无代理可观测性平台、机器学习基础设施、表格系统、安全、VPN、BaaS、版本控制。

---

[为你的 Python 应用选择一个最好的 Docker 映像](https://aws.amazon.com/cn/blogs/china/choose-the-best-docker-image-for-your-python-application/)

如何选择 容器 镜像是一个需要仔细调研权衡的问题，从各方面考虑 alpine 不是一个好选择。

---

[Infrastructure Defined Software](https://matt-rickard.com/infrastructure-defined-software)

- Puppet 2009, Salt 2011, Ansible 2012
- CloudFormation 2011, Terraform 2014
- Pulumi 2017, AWS CDK 2019
- 下一步是什么？

---

[白话Kubernetes入门实践](https://getk8e.zhubai.love/)

k8e 作者关于 kubernetes 的一系列文章，持续更新中。

---

[Why Linkerd doesn't use Envoy](https://linkerd.io/2020/12/03/why-linkerd-doesnt-use-envoy/)

[将 Cloudflare 连接到互联网的代理——Pingora 的构建方式](https://blog.cloudflare.com/zh-cn/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet-zh-cn/)

为什么 Linkerd 不使用 envoy.
    - 复杂度、资源消耗、安全。
    - But what if we have a requirement to use Envoy? 
    I would argue that’s not a real requirement. Your job is not to adopt a particular piece of technology. Your job is to solve a problem. 
    And if your problem is “we need to build a reliable, secure, and observable Kubernetes platform without paying an insane complexity cost” then I highly suggest you consider taking a look at Linkerd.

---

[Docker: How To Extract Image Filesystem Without Running Any Containers](https://iximiuz.com/en/posts/docker-image-to-filesystem/)

如何不运行容器 而导出容器镜像文件系统
> `$ docker pull nginx $ CONT_ID=$(docker create nginx) $ docker export ${CONT_ID} -o nginx.tar.gz`

---

[为什么 TCP 协议有性能问题 ·（一）](https://www.infoq.cn/article/psxdnqxu0ojdbxk5a9jg)

> 弱网环境是丢包率较高的特殊场景，TCP 在类似场景中的表现很差，当 RTT 为 30ms 时，一旦丢包率达到了 2%，TCP 的吞吐量就会下降 89.9%[3](https://draveness.me/whys-the-design-tcp-performance#fn:3)，从下面的表中我们可以看出丢包对 TCP 的吞吐量极其显著的影响：

---


[Why We Use CUE (and Not Helm)](https://cloudplane.org/blog/why-cue)

为什么使用 [[CUE]]，比较了 [[jsonnet]]、[[Dhall]] 和 [[CUE]]。

[[Dagger]] 和 [[Acorn]] 也采用了 [[CUE]]

---

[老司机们坐稳了 – 将Amazon EC2到Amazon S3的数据传输推向100Gbps线速](https://aws.amazon.com/cn/blogs/china/pushing-the-data-transfer-from-amazon-ec2-to-amazon-s3-to-100gbps-line-speed/)

> 答案是非常肯定的:  在全球任何一个亚马逊云科技的区域里, Amazon EC2 到 Amazon S3的默认数据传输[带宽都可以最高达到100Gbps](https://aws.amazon.com/cn/premiumsupport/knowledge-center/s3-maximum-transfer-speed-ec2/)。

---

[十多年了，这个最容易犯错的Go语法终于要改了](https://colobu.com/2022/10/04/redefining-for-loop-variable-semantics/)

"for 循环中变量的使用问题".[https://github.com/golang/go/discussions/56010](https://github.com/golang/go/discussions/56010)

---


[Move a running process into a tmux session](https://xai.sh/2020/10/16/Move-running-process-into-tmux-session.html)

通过 reptyr 将一个进程移动到 tmux 中

---

[Ansible你快点：Ansible执行过程分析、异步、效率优化](https://www.junmajinlong.com/ansible/11_faster_ansible/)

通过修改 ansible 配置、SSH 配置，使用第三方 Mitogen 插件来提速。

---
[货物和货车的匹配](https://blog.codingnow.com/2022/09/cargo_matching.html)

---


[Docker: How To Debug Distroless And Slim Containers](https://iximiuz.com/en/posts/docker-debug-slim-containers/)

使用 namespace 和 kubectl debug 启动临时容器进行 debug。关于 kubectl debug 的更多细节：[Kubernetes Ephemeral Containers and kubectl debug Command](https://iximiuz.com/en/posts/kubernetes-ephemeral-containers/)

---

[Why Is NixOS Popular Again?](https://matt-rickard.com/why-is-nixos-popular-again)

- Nix 现在讨论热度上升了:"a more formal team structure around development ([link](https://discourse.nixos.org/t/nix-team-creation/22228)), new startups built around Nix, 30% YoY user growth ([link](https://discourse.nixos.org/t/2022-nix-survey-results/18983)), and exponential growth in GitHub stars." ，但是 Nix 真正流行起来还是很困难，Nix 的语法，包的持续维护，使用场景。
- 用户真的需要 NixOS么？我之前想通过 NixOS来准备自己的开发环境，但是开发环境很少需要重新配置，基本上配置一次可以用很多年，如果真的需要重新配置开发环境，通常也到了更新自己的开发工具链的时候，体验下新鲜工具貌似也不错？

---

[Skyfall: eBPF agent for infrastructure observability](https://engineering.linkedin.com/blog/2022/skyfall--ebpf-agent-for-infrastructure-observability)

linkedin 使用 eBPF 采集网络相关 metric。
> Smoothed RTT (Round trip time): The predicted RTT value obtained by applying a smoothing factor to it, which is also used to adjust the RTO (Retransmission timeout) value. We are collecting this metric to measure the contribution of the network to overall performance. 
> RTT variance: An indication of path jitter. TCP uses this value, combined with SRTT, to compute the RTO. We are collecting this metric to detect transient network issues. 
> Packetloss and Retransmits: These metrics are being collected to monitor network performance. 
> Sending congestion window size: Congestion window controls the number of packets a TCP flow may have in the network at any time.

---

[How Product Teams Can Build Empathy Through Experimentation](https://netflixtechblog.com/how-product-teams-can-build-empathy-through-experimentation-6253603880a6)

- 同理心，将自己作为真正的用户去思考产品。
- When you’re building things, whether you’re a visual designer, or a designer of an API, or a PM, or anybody who’s building something, lean into trying to put yourself in the shoes of the user. And if you can do that, not just at the beginning when you write down the specs, but all the way through the process, you make a better product in the end.

---

[Go 的几种函数传参模式](https://www.zlovezl.cn/articles/go-func-argument-patterns/)

Golang 参数传递方法，函数式选项模式。

---

[eBPF File Watching](https://matt-rickard.com/ebpf-file-watching)

inotify 存在的问题：
> Doesn't support recursive directory watches 
Can drop changes when a large number of filesystem events occur (fixed-sized buffer) 
> No native debouncing support when a large number of events occur 
> Race conditions (rename events and between different instances of inotify) 
> API issues (no event information about the process that changed the file, path names as the event data)

---

[OAuth 2 详解（一）：简介及 Authorization Code 模式](https://jiajunhuang.com/articles/2022_10_08-oauth2_explained.md.html)

Jiajun 同学的 OAuth 2.0 系列博客。

---

[A Complete Guide to Working With Cookies in Go](https://www.alexedwards.net/blog/working-with-cookies-in-go)

Golang 关于 cookie 处理方式。

---


[Short Taxonomy of Open-Source Strategies](https://matt-rickard.com/short-taxonomy-of-open-source-strategies)

开源策略分类：招聘、市场营销、进入全新市场、减少竞争对手的护城河、建立标准。

---

[Go Worker Pool: The Concurrency Powerhouse](https://medium.com/higher-order-functions/go-worker-pool-the-concurrency-powerhouse-2dc7971f4f15)

一步一步将一个串行业务改为并行。



### 生活

[空城计与职场生存秘籍](https://tumutanzi.com/archives/16923)

谈论制造“被需要”，但是这种制造方式感觉不“正确”。

---

[婚礼回顾和一些经验分享](https://www.kawabangga.com/posts/4840)

摆正心态，这场婚礼最重要的是谁，是给谁办的，想明白这个问题，然后其他的问题都以这些人会不会高兴为准。

国庆刚好也参加了朋友的婚礼，婚礼需要一个项目经理来掌握全局，细节部分很容易分散精力且让人暴躁。

---

[The documentation system](https://whatiknown.strrl.dev/notes/vivthodp9f5lzmz6wjw7dh3/)

教你如何写文档的文档。

---

[真正的好作品只能靠自己去发现](https://reorx.com/essays/2022/10/how-novels-become-boring/)

> 好的作品不会过于套路化，因为有追求的创作者总是在尝试突破和创新，因此不仅生产效率不会太高，还需要读者有一定的耐心和智力才能渐入佳境。  大众认为好的不一定对自己而言是好的。

---

[How the largest open source companies got their first 1k community members](https://pchase.substack.com/p/how-the-largest-open-source-companies)

如何获得 1k 个用户？hackernews、meeting、注重早期用户。

---

[倍速播放：青年闲暇时间的消费与异化](https://mp.weixin.qq.com/s/94LRW6NSy28tTaBVr-cQ7g)

> 在倍速播放背后，折射出从工业社会、消费社会到互联网社会资本增殖逻辑的转变，资本从原来压榨劳动时间的逻辑转变为促进闲暇时间的商品消费，最后转变为想方设法占用人们的闲暇时间本身。 
> 倍速播放在一定程度上可以看作是青年对快时代节奏的主动适应和对资本逻辑的反抗，彰显了青年的主体性。然而，即使青年自主选择了倍速播放，背后依然难以挣脱资本支配的逻辑。 
> 在青年和资本的博弈中，资本获得了播放时长增加和播放效率提升的双重胜利，青年却未能获得加倍的自由和幸福，导致了闲暇时间的异化。倍速播放是闲暇时间效率化的体现，是倍速生活的缩影，却并不一定是通往自由和幸福的捷径。


## 书影


《子弹列车》：打打打杀杀杀。

《万里归途》：感觉不如《战狼》啊。

《圈套》：系列剧，推理加搞笑，轻松娱乐。

《独行月球》：不好笑。

《Take One：终极一曲 》：理想主义者的演出。

《Terraform：多云、混合云环境下实现基础设施即代码》： 最近打算搞一个 Provider，重新看书了解一下使用姿势。