---
title: Weekly Issue-《给阿嬷的情书》
date: "2026-05-17:00:00.000Z"
slug: "Weekly-Issue-Dear-You"
tags:
  - Weekly
description:
---

## 文章

### 技术

[GitLab Act 2](https://about.gitlab.com/blog/gitlab-act-2/)   
[I'm really frustrated that GitLab is doing layoffs - Xe Iaso](https://xeiaso.net/notes/2026/gitlab-layoffs/)   
[Thoughts on GitLab's workforce reduction" and "structural and strategic decisions"](https://simonwillison.net/2026/May/11/gitlab-act-2/)

[[GitLab]] 组织架构调整，没说具体减少的数字。公司发布这些公告的标题都挺好听的，Act 2，开启新的篇章。

不知道 `gitlab.cn` 现在和 Gitlab 还有没有关系，国产化进程领先了一个版本？

---



[I Left Port 22 Open on the Internet for 54 Days. Here's Who Showed Up.](https://arman-bd.hashnode.dev/i-left-port-22-open-on-the-internet-for-54-days-here-s-who-showed-up)

作者留了 ssh 22 入口的蜜罐，分析结论还挺有意思的，大多数攻击都没有使用过交互式 shell，都是执行 `uname` 来探测目标主机信息后结束，只有极少部分会利用 `/dev/tcp` ， `chattr` 等方式来进行攻击。

---


[KISS vs DRY in Infrastructure as Code: Why Simple Often Beats Clever](https://rosesecurity.dev/2025/11/14/kiss-versus-dry-iac.html)

> The fundamental issue is that DRY tooling optimizes for writing code, not reading it under pressure.   
> The question isn’t “how do we eliminate complexity?” It’s “where do we put the complexity to minimize time to business value?”    

> In infrastructure code, transparency trumps terseness every time.   
> Everything that increases time to business value (technical debt from abstraction, lengthy onboarding, opaque troubleshooting) is expensive regardless of how “clean” the code looks.    
> Choose boring technology. Keep it simple. Focus on business velocity over code elegance. Your 3 AM self will thank you.   

完全同意，最近几年也一直按照相同的理念在执行。

---
[The Two Abstractions of System Design: Hide or Reduce](https://muratbuffalo.blogspot.com/2026/05/the-two-abstractions-of-system-design.html)

> So why do I (and every other formal methods/modeling person) see such a large skill gap in abstraction, and flag it as the core, make-or-break skill for modeling?    
> There are two kinds of "abstraction" conflated under the same umbrella term.    
> - **Modularity abstraction:** This is the traditional abstraction taught in CS curricula as ADTs, APIs, layered design, etc. It is all about encapsulation, drawing boundaries, and hiding internals.    
> - **Modeling abstraction:** This is what I talk about when I talk about abstraction in the context of modeling. This is the same sense of abstraction mathematicians and physicists when building models for thinking and reasoning. The goal is to find the minimal and most elegant description that preserves the property you care about. It is all about cutting away everything orhtogonal to the essence of that property.    

---





### 生活

[如何培养爱好 - Miao Yu](https://yufree.cn/cn/2025/05/11/how-to-enjoy-life/)

> 我观察到很多时候人们聚在一起所聊的主题更多是所有人的经验交集，房子车子票子本子孩子，这些东西聊来聊去也就那么回事，变成了一个又一个的人生主线任务，做什么事都想走个捷径找个最高效率，这样既累也没意思，早晚会被人工智能冲击成找不到存在感的行尸走肉。

> 窃以为爱好这张考卷，不是得分越高越好，而是你想得几分就得几分，不多也不少，这其实比一味得高分更有意思。

期望办公室的茶水间话题能从房子装修转移一下。

---

[为什么要写作](https://limboy.me/posts/why-write)

> 这就是为什么要写作，它是无需天赋的思维健身，具有普遍性、重要性、高门槛、复利效应的特性，而且只要你愿意，可以一直写下去。

---



### 书影播客

《又是完美的一天-健身人的生活哲学》，可以理解为健身网红短视频笑点合集。

《新加坡（口袋版） : LP孤独星球Lonely Planet口袋旅行指南》，因为飞猪上看到了往返 300 的机票，找来看看攻略，先了解一下。

《硬件产品经理进阶》，上图的新书，意外的觉得还不错，没有停留在理论堆砌，实操性还挺强的。其中关于“老乡“的这段很有感触，刚工作的时候有一个同事，“吃得开“，和谁都能聊得来，经常“认老乡“，对于后续工作的开展有不小的帮助：

> 公司A的对接窗口是B，其人三十不到，但是性格很强势，总给人一副咄咄逼人的样子，况且其身份还是甲方，所以对接的过程可以预见会有些摩擦。公司A的组长C，和笔者年纪差不多，一聊老家都离得不远，加上笔者有过硬的地理知识，用赞叹组长考家的物产很有名气打开了话题，一来二去这就扯上了"半个老乡"的关系。

《飞驰人生3》，再一再二再三，还能再四么？

《给阿嬷的情书》，好看，真好看，故事很简单，刚看就猜到了后续，但是就是因为知道了故事的后续，所以越看越难受，电影不到一半就看哭了，最后哭出了声，简单的故事，克制的表达，厚重的情谊。电影中的情感都是普世的，和时代有关，和家庭有关，和承诺有关。其中有几句台词流传比较广：“暹罗没有春天，你就是我的春天“， “行船入夜，恰江上升明月，似与你并肩共赏，江海万里，心中念你，便不觉遥远”。 

我最喜欢的是这句：“淑柔我妻， 付港币五十元，随寄布料十尺。我在暹罗非常好，免担忧“，简单质朴的表达，让对方安心，这第一封侨批就是一个“谎话“，日子过的并不好，自己非常想念家里，到后面谢南枝的选择，也想让“家里“更安心。


## 碎碎念

* 过了一个五一，超级碗的沙拉又涨价了。
* 陕西话：包木乱，不要烦。
把人木乱的，烦死了。
* 京沪高铁涨价 20%，班味最重的路线。
* 同事留长发，我说可以做公益，他说做什么工艺？
* 被用 AI 生成的需求文档气到了。每个字都认识，看似啥都写了，又好像啥都没写。
* "不要再自视优越地吐槽 AI 代码质量差，而是应该探索如何生成高质量的代码", 看到这句话，我知道为啥听到同事的抱怨我没什么反应了。
* DeepSeek 在乌兰察布招运维，也挺合理。
* 在孤独星球看到了滨海湾花园的图片，上海温室花园难道是抄袭的么？我还挺喜欢这个地方的： https://www.dmaa.at/work/expo-cultural-park-greenhouse-garden-shanghai 
* 上海话的“劈情操”，对应的英文是什么？Vibing ？
* “那你所谓充分的精力什么时候才会有?”
