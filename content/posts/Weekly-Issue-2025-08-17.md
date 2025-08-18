---
title: Weekly Issue-《K-Pop 猎魔女团》
date: 2025-08-17
tags:
- Weekly
description:
---


## 文章

### 技术


[现代化你的 Go 代码 | Oilbeater 的自习室](https://oilbeater.com/2025/08/08/go-modernize/)

学到了几个之前不知道的方法：
- `strings.SplitSeq`
- `maps.Clone`, `maps.Copy`, `maps.Insert`
- `slices.Delete`

---

[NixOS Now Celebrates Pride Month… Year Round](https://lunduke.substack.com/p/nixos-now-celebrates-pride-month)

[[NixOS]] 表示出明确的政治倾向，并且直接 block 提出异议的人。挺好，双向选择。

---

[Vercel Goes All In on Vibe Coding Web Apps - The New Stack](https://thenewstack.io/vercel-goes-all-in-on-vibe-coding-web-apps/?taid=689b17b25029200001b33cbf)

> **v0.app Is Changing the Next.js Framework**    
> There’s another interesting dynamic within Vercel: The Next. Js team is updating the framework so that it plays better with LLMs and agentic AI, Khandelwal said.   
> “We work super closely with the Next. Js team,” he said. “In fact, we are very good customers of Next. Js — we give them a lot of feedback on good examples or things like, ‘LLMs don’t seem to understand this syntax’ or ‘don’t seem to understand this pattern in the framework.’”    
> The team will ask for either better documentation or whether the situation can be simplified or changed.

---

[The Future Isn't Model Agnostic · The Fly Blog](https://fly.io/blog/the-future-isn-t-model-agnostic/)

> Your users don’t care that your AI project is model agnostic.

> Every startup pitch deck with ‘model-agnostic’ as a feature should become a red flag for investors who understand product-market fit. Stop putting ‘works with any LLM’ in your one-liner. It screams ‘we don’t know what we’re building.’

这里的一些观点和 [[ampcode]] 是一样的。

---

[pyx: a Python-native package registry, now in Beta](https://simonwillison.net/2025/Aug/13/pyx/)

[[Astral]] 的商业化项目，一个 private package registry。和去年在 [[Mastodon]] 上的回复一致。是在 PYPI 之上的一层么？没看懂。

---

[LoxiLB -- More than MetalLB | Oilbeater 的自习室](https://oilbeater.com/2025/08/15/loxilb-metallb/)

> MetalLB 的缺陷 - 缺乏有效的监控   
> 这同样是依赖 kube-proxy 实现导致的一个问题，kube-proxy 的多种实现方式都没有流量层面的监控，导致的后果就是如果你看 MetalLB 提供的监控指标就会发现里面没有任何流量的指标。这种几乎没有任何数据平面监控的 LB 要上生产，就有点过于松弛了。


---




### 生活

[丟失的表達欲 - Just lepture](https://lepture.com/zh/2025/loss-of-self-expression)

> 我也试过写点周记，谈谈一周见闻或所做之事，却往往不见下一周。大抵因为下一周乏善可陈，于是不了了之。不然尝试写一下月记？

> 除了介绍自己的项目，还能写点什么呢？近来有什么所思所想，又有什么洞见或者观察？似乎没有。这大约就是所谓的咸鱼人生吧。意识到了，似乎就应该翻一下身，来晒晒另一面。

如果某一周没有看一个完整的作品（电影、书籍、剧集），我的周报中的关键词就很难想，通常就会想到那句话：“没关系，又活了一周，已经很棒了”。

### 书影播客

《K-POP：猎魔女团》：网飞出品的电影，有一种迪士尼电影的感觉，制作精良，剧情简单。因为有很多的 K-pop 元素，时不时的就原地唱跳一波，又感觉在看一个张专辑的完整 MV。这部电影本身影响范围应该只是还好，但是靠着其中的几首歌曲一直在各大榜单中刷榜，各大“老牌”女团 Vocal 都在翻唱《Golden》这首歌，B 站上有人制作了翻唱合集：[【K - POP: 猎魔女团】Golden 翻唱](https://space.bilibili.com/419085137/lists/5932512?type=season)，喜欢郑恩地、李海丽的翻唱版本。    
（ 另外，电影中好像真的没有双眼皮。


《两个写作者对抗AI-EP10 Storm 徐风暴 “脱口秀演员在舞台上绝不说 sorry，但口水喷到观众脸上除外”》，这是谢梦遥的播客，主要内容是对各个领域的人进行采访，他本人是《人物》杂志主笔（一个有争议的人）。在采访过程中，会问一些比较尖锐的问题，有些问题很直接，这期对谈就很好，因为 Storm 也是一个直接的人。听完更觉得， Storm 应该早点脱离俱乐部老板的身份，把更多的精力集中在单口上。国内的单口俱乐部，都很难和演员找到一个可持续经营的方式。


《两个写作者对抗AI-EP19 刘旸教主 关于新书，去年喜单名次，负面评价，真诚，虚荣，努力，以及是什么拦住了我去加吴镇宇的微信》，很多人看完教主的表演，都会觉得他很用力、很努力，他只是做自己，就让别人感觉到他很努力，也是一种抵抗外界的方式。


《基本无害-Ep169 柏林生存手册：闲着也是闲着，先罢个工吧！》，城市生存手册柏林篇，在听之前就对德国的租房听说过一些地狱难度，但是这里聊到的也太难了，确实太卑微了，很难就说这是一种良好的状态。里面有个女生提到，因为自己作为二房东，在找房客时没有认真“审核”，导致自己反而被迫搬出去，在搬出去前，还有给房客找一个适合的二房东，这太憋屈了。



## 碎碎念

* 小红书支持长文了，B 站开始推广视频播客了。长文和播客，都属于“长”内容，世道变了。
* 虽然有时候觉得过分信任要不得，但是一个人是怎么能把自己的可信度降到这么低的呢。
* Github Action 的 scheduler 需要是默认分支才会生效。
* BeastMode 确实比 VSCode 默认的 Agent 要好。
* 现在最快实现可以 fuse 挂载的方式，是实现 webdav ？
* 继续踩坑，OpenAPI generator 参数 disallowAdditionalPropertiesIfNotPresent 默认为 true。
* 原来 docker 也干过打错 tag 又删掉的情况。
* 靠着周末写点其他代码回血。