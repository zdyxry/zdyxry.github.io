---
title: Weekly Issue 2023-09-10
date: 2023-09-10
tags:
- Weekly
description: 
---


## 文章

### 技术

[KubeVirt 探秘：一些核心问题解答 | MoeLove](https://moelove.info/2023/09/03/KubeVirt-%E6%8E%A2%E7%A7%98%E4%B8%80%E4%BA%9B%E6%A0%B8%E5%BF%83%E9%97%AE%E9%A2%98%E8%A7%A3%E7%AD%94/)

[[KubeVirt]] 优势：声明式配置；资源请求和限制；复用 Kubernetes：调度能力、网络、存储、可观测。

---

[VM's and Containers I am Running - 2023](https://blog.networkprofile.org/vms-and-containers-i-am-running-2023/)

[[self-hosted]]，作者自托管了很多机器和应用，大部分采用 VM + [[Container]] 的形式，没有引入 [[kubernetes]]，比较好奇他如何管理这些机器和设备。

---


[有关 TLS/SSL 证书的一切 | 卡瓦邦噶！](https://www.kawabangga.com/posts/5330)

关于 [[TLS/SSL]] 的背景、实现说明，有一种读了一遍迷你版的《图解密码技术》 的感觉，写的太好了。

> **CA 只是拿自己的 private key 给原证书 append 了一个加密的 hash 值而已**  

---

[If P99 Latency Is BS, What's the Alternative? - The New Stack](https://thenewstack.io/if-p99-latency-is-bs-whats-the-alternative/)

P99延迟指标只关注延迟分布的99百分位点,而忽略了剩余1%的情况。作者提出,P99延迟指标容易遮蔽系统中的问题,不应过分依赖。建议可以使用"痛苦指标"(misery metrics)来补充P99。监控系统中的失败情况,如超时、重试、失败查询等,可以更直观地反映用户体验。当这些指标恶化时,就表明存在问题需要排查,不用等待P99恶化。

---


### 生活

[核电废水排放 // Shell's Home](https://blog.shell909090.org/blog/archives/2894/)

>1.  日本负责处理污水的机构是东电，而东电的记录不怎么良好。2011年震灾的时候连续出包，硬生生把问题搞大。2013年承认放射性地下水泄漏到了太平洋里。（参考引用[7]）这里漏的可不是只含有氚的废水，而是真正的核污水。  
真正最大的问题尚不是处理过之后的污水排放，而是关东震灾再来一次怎么办？

---

[电动车横向对比](https://manateelazycat.github.io/2023/09/06/electric-car/)

对比了外观、内饰、空间、静音、自动驾驶、舒适度、语音助手、屏幕操作、产品细节。结论是不差钱上[[蔚来]] ES8。

---


[现在房价进行到哪一步了？](https://darmau.design/article/now-what-stage-are-house-prices-at)

> 权力高度集中**擅长的不是解决问题，而是拖延问题**。  
**历史不是螺旋型上升的，也可能是秦制两千年的循环。**  

---

[《The Missing README》——工程师的职业图谱。 - Xiaowen.Z Deployed](https://xiaowenz.com/blog/2023/09/the-missing-readme/)

学习能力、沟通能力、协作能力都很重要。加到想读列表中。



## 书影


《计算机网络》，继续在看。

《不开玩笑》，谈论幽默的定义可能本身也是一种幽默。

《第八个嫌疑人》，是一部叙事电影，电影的故事很简单，作为真实事件改编的电影，应该算是不错的。

《大宋少年志》，终于把第一段故事看完了，其中的特效真的是五毛特效，特意查了一下《哈利波特与魔法石》是 2001 年的电影，里面的特效过了快 20 年还是领先的。

