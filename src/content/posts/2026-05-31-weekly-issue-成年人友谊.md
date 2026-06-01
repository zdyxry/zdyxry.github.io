---
title: Weekly Issue-The quiet grief of adult friendship
date: "2026-05-31:00:00.000Z"
slug: "Weekly-Issue-The-quiet-grief-of-adult-friendship"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Incident Report: May 19, 2026- GCP Account Suspension](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage)

> Railway owns our vendor choices, and we ultimately own this one. Your customers don't care whether the failure was Google or Railway; they see your product. Your uptime is our responsibility, and we'll keep delivering on it. 

---

[We should be more tired than the model | ✰Vicki Boykis✰](https://vickiboykis.com/2026/05/28/we-should-be-more-tired-than-the-model/)

> Lately, I’ve been feeling like I’m losing control over the code I write when I work with agentic code generation.

We need friction, more and more.

---
[I’m tired of talking to AI](https://orchidfiles.com/im-tired-of-ai-generated-answers/)

> He didn’t even read the AI’s answer. He just took a screenshot and forwarded it to me.

我不反感同事使用 AI 来回复我，我期望的是对方在使用 AI 回复的信息之前，能够仔细的辨别正确性，带点自己的想法，直接转发没有任何正面效果，反而会让双方都对彼此失去信任，信任丢了可找不回来了。

---
[GitHub - alicefr/bink: Bootc in Kubernetes, tool for creating bootc kuberntes clusters · GitHub](https://github.com/alicefr/bink)   
[GitHub - jlebon/bootc-operator: A Kubernetes operator for managing bootc nodes · GitHub](https://github.com/jlebon/bootc-operator)

[[bink]]，在 [[Podman]] 中运行 Fedora Bootc VM 来启动真正的 K8s 集群，实现上还挺巧妙的，外层的 Container 运行的是带有 systemd/libvirt/qemu 的 Fedora Image，libvirt 启动是的 Fedora Bootc，利用了 virtiofsd 来避免 VM 内部重复处理 k8s image，VM 配置采用 cloud-init（看 Issue 后面可能换成 Ignition），利用 passt / mcast 来处理网络。

bootc-operator 的想法就更好了，看样子要基于 Machine Config Operator 来实现一套适用于所有基于 Bootc 的发行版的物理机管理，持续关注一下。

---



### 生活

[The quiet grief of adult friendship](https://archive.is/Ju0Rs)

> 曾几何时，友谊无需精心策划。   
> 与爱情不同，友谊的结束并非戏剧性的。没有最后的对话，没有彻底的决裂，也没有电影般的结局。大多数友谊都是在不知不觉中逐渐消逝的——电话被推迟、工作压力巨大、地理距离遥远、情绪疲惫、作息时间不同、生活重心不同，以及彼此的人生节奏也截然不同。有一天，你会突然意识到，那个曾经了解你所有想法的人，如今只知道你在 Instagram Stories 上不经意透露的那些信息。   
> 如今的年轻职场人士生活在这样的体系中：它表面上颂扬人与人之间的联结，实则暗流涌动，友谊却在悄然消逝。工作耗尽了他们的情感能量。城市残酷地拉长了人与人之间的距离。周末不再是社交空间，而是变成了休养生息的时间。雄心壮志让每个人都成了自己人生的项目经理。就连休息，如今也似乎被设定为必须保持高效。   

> 悲剧在于，这种孤独感往往与持续不断的数字化互动并存。我们或许是第一代能够随时随地与彼此联系，却同时在情感上变得疏离的一代。我们时刻感知着彼此的存在，却无法真正参与到彼此的生活中。我知道朋友们吃什么，去哪家咖啡馆，抱怨什么。我知道他们升职了，因为领英会在他们自己知道之前通知我。然而，有时我却会犹豫要不要打电话，因为我不再了解他们生活的情绪起伏。   
> 成年生活奖励的是自我约束。每个人都很累。每个人都在努力提升自己。每个人都“经历了很多”。   
> 不知从何时起，友谊也开始吸收管理语言。我们现在讨论情感带宽，就像讨论流量套餐一样。就连情感有时也像是经过了无形的成本效益分析：谁先发短信？谁付出更多？谁更容易投入情感？谁消耗了你的精力？    
> 不知从何时起，友谊也开始吸收管理语言。我们现在讨论情感带宽，就像讨论流量套餐一样。就连情感有时也像是经过了无形的成本效益分析：谁先发短信？谁付出更多？谁更容易投入情感？谁消耗了你的精力？    
> 然而，友谊始终依赖于某种非理性的慷慨。一种愿意一起虚度光阴的意愿。一种愿意第五次倾听同样的焦虑。一种愿意静静地陪伴彼此的意愿。一种愿意不带任何目的、随时待命的意愿。   

写的太好了，好久没看到写的这么好的文章了，值得反复阅读。

---

[Clanker: A Word For The Machine | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2026/5/26/clankers/)

我发现一个人如何对待 AI 有一个简单的区分方式：是否会使用“你”来下发任务。

---

[Gap 半年](https://www.jocs.me/blog/gap-year/)

> 每天都很忙，但很难说清自己到底创造了什么。

> 不再被时间持续推着向前的状态。

---



[简单易懂的有毒职场炼成术](https://roriri.one/notes/toxical-workplace)

> 此外，「拥抱变化」常常被用来粉饰产品经理阴晴不变的个人品味、以及想不明白事情胡乱开车。

> 「拥抱变化」这个概念被提出的初衷是允许需求在开发过程中随着「来自用户」的真实反馈调整。请注意，「真实反馈」来自用户，产品经理阴晴不变瞎改主意不是市场反馈，和敏捷开发的设立初衷毫无瓜葛。

> OKR 和敏捷尝试向开发引入人本因素，但是一个原本就威权的体系里扭曲了这些人本追求的意含，将其转化为持续压榨的工具。开发者在成为人力「资源」之前，他们首先得是人。但很明显的，一些有毒的工作场所把人当成了 AI，又期待 AI 变成人。



---

[大都会博物馆拉斐尔特展](https://davidfeng.us/zh-cn/2026-05-06-raphael/)

> 注意圣母宝座的透视构图以及人物手势眼神互动的节奏。色彩上，左前景圣彼得身上的黄色与右上角天使的黄色呼应。红色和绿色也有类似的对应关系。布展特意选择了画面中出现最少的蓝色作为背景，也是用心了。

> 许多描述拉斐尔的文字都会提到一个叫做 Sprezzatura 的词语。这个词就是像主在《廷臣论》中发明的，描述贵族的理想举止风格——刻意掩盖努力痕迹的优雅，一切看起来毫不费力，浑然天成。

> 但柳暗花明又一村，他在圣母子（温柔圣母 Madonna of Tenderness, 圣母与圣子亲密地脸颊接触）这个赛道上找到了突破口，并建立口碑。这种画一般比较小，放在富裕委托人的家里。画面中健康的婴儿和喜乐的母亲，用来保佑保佑分娩的母亲和孩子。

想到了小时候每年春节，姥姥家总是喜欢贴墙画，通常是两个大胖孩子抱着锦鲤/金元宝/桃子，寓意着连年有余。

---


### 书影播客

《家弑服务》，什么玩意儿，看似有什么东西想表达，却只是一个爽片，还不怎么爽，不喜欢。



## 碎碎念

* 公司楼下停车费，一个月 1k。
* 麻蛋，Kimi-code 的变更导致 Slock 不工作了。
* 最近发生了几次，看一个项目看着看着，发现 maintainer 在用 Rust 重写。
* review 代码，发现有一个文件怎么看都没理解是什么意思，问 owner，发现他也不知道。
* 周五，发工资，18 点，23 度，江边，跑步，完美。
* 语音输入法使用频率继续增加。
* 居住地附近还是得有公园，那种感觉差别很大。