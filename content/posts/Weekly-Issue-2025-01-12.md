---
title: Weekly Issue-《冬泳》
date: 2025-01-12
tags:
- Weekly
description:  
---


## 文章

### 技术

[GitHub Actions?! 想说爱你不容易之记一次 Release CI 重构经验 - 晒太阳的猫](https://zyy.dev/post/github-actions-wtf/)

[[Github]] [[Actions]] 的一些经验总结：
- 尽可能使用 Dockerfile
- 将 Release 环节中的细节放在 Makefile 中
- Action 模块解耦
- 避免在 Actions 中 Shell 加入过多命令
- 正确的配置 Variables 和 Secrets 

“只要代码是开源的，那么就保证软件制品和构建过程同样是开源的；”，这一条感觉需要结合公司实际策略来看待和执行。

---


[OpenDAL RangeReader 的奥妙 - Grep.ing](https://www.grep.ing/secret_of_opendal_range_reader)

这篇博客的代码效果真不错，应该是使用了 [Code Hike](https://codehike.org/) 。

---

[用 LD_PRELOAD 写魔法程序 | 卡瓦邦噶！](https://www.kawabangga.com/posts/6825)

> 花了一天排查无果，问了朋友，最后发现这个问题：Goroutines cause deadlocks after fork () when run in shared library #15538<sup data-fn="0c890f70-7402-470d-a706-a5ebf724db9b" class="fn"><a href="https://www.kawabangga.com/posts/#0c890f70-7402-470d-a706-a5ebf724db9b" id="0c890f70-7402-470d-a706-a5ebf724db9b-link">3</a></sup>，而且开发人员的回复是：This is to be expected. It’s almost impossible for multithreaded Go runtime to handle arbitrary forks.   
> 而 mtr 正好执行了 fork，所以这算是一个 Golang 的 runtime 问题——**如果以 shared-lib 的方式运行，那么主程序是不能 fork 的，如果 fork，Go runtime 中的 goroutine 管理与多线程模型，fork 后线程状态的不一致可能会导致无法正常恢复，从而触发死锁。**

之前好像在其他地方也看到过这个问题，估计自己去 debug 要抓瞎。

---

[Open source all the way down: Upgrading our developer documentation](https://blog.cloudflare.com/open-source-all-the-way-down-upgrading-our-developer-documentation/)

[[CloudFlare]] 的开发者文档从 [[Hugo]] 迁移到了 [[Astro]]。他们在 2021 年从 Gatsby 迁移到了 Hugo，带来了更快的开发流程、自定义组件、结构化的 changelog 管理以及性能优化。

现在迁移到 Astro 是为了：内容组织改进、扩展性、开发体验、JS/TS 支持、CSS 管理。[Starlight 🌟 Build documentation sites with Astro](https://starlight.astro.build/) 是其中的一个决定性因素。

---

[Living in the future, by the numbers](https://tailscale.com/blog/living-in-the-future#welcome-to-the-future)

2024 年相较于 2004 年，发生了哪些变化，计算速度比 20 年前快了 200,000 倍，RAM 大小增加了 16 倍到 750 倍，硬盘容量增长了 100 倍，SSD 处理能力提升了 10,000 倍， SSD 的可靠性有了显著提高。

---


[Gist of Go: Context](https://antonz.org/go-concurrency/context/)

1.21+ 版本中有了 `context.WithCancelCause`, `context.WithTimeoutCause` , 可以携带一些 cancel 的上下文。

---

[Little Endian vs Big Endian | 卡瓦邦噶！](https://www.kawabangga.com/posts/6816)

想到了一个同事之前很喜欢的一道面试题，判断大端序小端序。

---

[containerd internals: Images](https://samuel.karp.dev/blog/2024/12/containerd-internals-images/)

[[containerd]] internal 系列文章，这篇介绍了 Image 及 snapshotter。之前看过 OCI Image Spec 的话，感觉可以略过。

---

[Cognitive load is what matters](https://minds.md/zakirullin/cognitive)

中文版：[cognitive-load/README.zh-cn.md at main · zakirullin/cognitive-load · GitHub](https://github.com/zakirullin/cognitive-load/blob/main/README.zh-cn.md)

认知负荷指的不是任务本身的复杂度，而是与任务无关的 - 由信息的呈现方式导致。通常由与任务并无直接关联的因素引发，比如那些聪明人的 “骚操作”。并且这种类型的认知负荷是可以避免的。我们将在下文着重关注这一类型的认知负荷。

反复阅读，给自己建了一个半年之后的 Todo，半年之后再读一次。

---






### 生活

[2024年: 逐渐平静](https://capops.xyz/2024)

> 厌倦了坐班的生活，向往 web 3 的自由。读了《**Read Write Own**》，学习了 WTF 的 Solidity 课程，以及其它平台关于 web 3 相关学习资料，最终，并没有找到 web 3 远程工作，但是对区块链技术，有了自己的认知：并非外界传闻的骗局，毕竟 USDT 在拉美、土耳其通涨严重的地区很流行，也能解决切实问题。几年前我曾经拒绝过两个区块链公司的 offer，拒绝的原因是觉得那是骗局，现在想想不免觉得可笑。只能说，一切因缘际会，皆因时机未到。依然看好 web 3 方向。

---

[专栏：职场不用喝咖啡 - 求职之前关心啥？](https://world.hey.com/xiaowen/post-ec191aa4)  
[专栏：职场不用喝咖啡 - 如何利人利己（1）](https://world.hey.com/xiaowen/1-8edc66c8)  
[专栏：职场不用喝咖啡 - 如何利人利己（2）](https://world.hey.com/xiaowen/2-317b857a)  
[专栏：职场不用喝咖啡 - 如何利人利己（3）](https://world.hey.com/xiaowen/3-2d9557cf)   
  

> **大部分时候，如果要主动跳槽，尽量往上选，不要平级甚至降级跳槽，哪怕薪资更高。**
> 因为职场从来就不是一个单纯的生产环境，而是一个复杂的人际关系网络。
> 你需要更客观的，不带评分色彩的去了解你共事的同事们，**注意，这里的任何一个方面，都没有「高低之分」，他们更像是「标签」，而不是「分数」**。
> 你的上级是你最重要的职场「资源」，没有之一，是要利用的。

> 很多人在工作中都会遇到这样的困惑：什么情况下应该帮，什么情况下应该拒绝？什么情况下要争，什么情况下要让？
>  **边界分两种：****该打破的边界，和该坚守的边界****。**
> 该打破的边界：非本职工作类型的协作，如沟通，管理，流程，甚至办公室政治。
> 一定要坚守的边界，不能随便帮的，主要是这些场景：1. 需要明确责任归属的任务; 2. 专业性不足产生的困境。

> 不要让任何事情经过自己以后，居然没有任何进展。

---

[TILs are junk food](https://antonz.org/til/)

> *TILs are great for the author*. Yes, they are. Keeping a personal journal and reflecting on the things you've learned is a nice habit. But reading other people's TILs is not nearly as useful. Quite the opposite, in fact.

完全认同。 `TIL` 主要用途是记录自己学到了某个技巧、知识。而这些 TIL 通常是零散的，作为读者没必要去读某个 TIL 合集。

---


[橙子的2024 年终总结：追寻幸福](https://blog.sailfishc.com/2024)

> 这也是我自己的感情观，如果说亲情的亲密关系是不可选择的，那么对于自己另一半的亲密关系是可以有选择的，经过之前的感情，我是对「不可能改变」这件事情很强烈的认同感，不仅是别人不能为你改变，我在很大程度上也不会为对方改变，改变真的很难。

说多少次都不嫌多：不要妄图改变什么，你连你妈都改变不了。

---

[Everything Must Be Paid for Twice](https://www.raptitude.com/2022/01/everything-must-be-paid-for-twice/)

作者的观点是：我们在购买大多数东西时，都需要付款 2 次，第一次是为这个物品的商业价值付款，第二次是为使用这个物品时付出的精力价值付款。用读书来举例的话，第一次付款时 20 美元，第二次付款是 10 个小时的阅读时间。如果没有第二次付款，那么第一次付款相当于扔钱。
在消费主义社会，人们不断的追求第一次付款，来得到即时满足，潜在留下了大量的第二次付款负债，因为精力是有限的。我们往往会把自己的精力放在一些低价的事情上。

---


## 书影


《冬泳》，班宇。每次读东北作家的小说，都会瞬间回到小时候的状态，书里的每一句话，我都能够想象到邻居的东北口音，书中的“虚构”故事，我都能想象是我身边的故事，从小听长辈聊到的故事，都会有一些想家。这可能也是为什么东三省可以统称东北人，因为大家的记忆是相同的。我想读一些关于哈尔滨的故事。

《生活大爆炸》，继续看第一季，谢尔顿之所以还能有人愿意和他相处，很重要的一点是他的真诚。谢尔顿的家里有电视，朋友们可以一起吃饭看电视，电视对我来说还挺重要的，可以随便放些什么，是一个“稳定”的象征？（在看剧的时候，想到了本周听的一期播客，在大城市是否有漂泊感，是否有“根”了，不同的人对此的定义差别很大：有些人觉得自己有稳定住所，有些人会觉得自己结婚/成家了，有些人会觉得家里有电视，有些人觉得家里安装了有线电视。）


## 碎碎念

* 借钱和被借钱真的太难了，人情世故。要么伤感情，要么伤钱。
* 徐汇的写字楼，就是要比后滩的洋气不少。
* 看到群里有人问，去北京有什么推荐的吃的，我上一次去北京是 2021 年出差，对北京的印象已经有些模糊了。
* 上海的冬天来了。



