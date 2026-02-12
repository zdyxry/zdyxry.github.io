---
title: Weekly Issue-《只有我一个人觉得特好笑吗？》
date: "2025-08-31T00:00:00.000Z"
slug: "Weekly-Issue-只有我一个人觉得特好笑吗"
tags:
  - Weekly
description:
---

## 文章

### 技术

[一个很 sb 的硬件 bug，及其 patch](https://fuis.me/post/34)

> 机箱上有一个不可拆卸的螺丝柱顶到了内存插槽的第八槽，导致硬件错误

> Patch：用透明胶粘上了


Hahahahahahaha。

---

[Using Podman, Compose and BuildKit · emersion](https://emersion.fr/blog/2025/using-podman-compose-and-buildkit/)

Docker CLI 对接 podman sock ，为了对接 buildkit 自己实现了 bakah 来构建 Image，一种“为了这点醋包了一顿饺子”即视感。Podman 自己一直在推自己的 Quadlet，感觉不如赶快把 podman-compose 的功能对齐上来，可以更快的吸引用户使用。

---
[From Python to Go: Why We Rewrote Our Ingest Pipeline at Telemetry Harbor](https://telemetryharbor.com/blog/from-python-to-go-why-we-rewrote-our-ingest-pipeline-at-telemetry-harbor/)

> During our canary deployment of the Go endpoint, we noticed something concerning: the 400 error rates were significantly higher than expected.

> - **Boolean coercion**: If someone submitted `True` or `False` (standard Python boolean values), Pydantic would silently interpret these as `0` and `1` respectively. There was no validation error, no warning—just automatic conversion.
> - **String-to-number coercion**: When users submitted numbers as strings (like `"123.45"`), Pydantic would automatically convert them to floats or integers without any validation warnings or errors.

印象中不止一次看到有人在从 Python 迁移走的时候，遇到这种类型转换问题了。

---
[Cracks are forming in Meta’s partnership with Scale AI | TechCrunch](https://techcrunch.com/2025/08/29/cracks-are-forming-in-metas-partnership-with-scale-ai/)

一团乱麻，顶级诈骗？



### 生活

[派派成长日记 #4 - 幸福但不快乐的二月龄](https://changchen.me/blog/20250824/paipai_three_months/)

> 书中还有一段印象深刻的话，大致观点：需要谨慎区分 “安抚” 与 “道具”，以安抚奶嘴为例，如果婴儿放在嘴中安静吸吮则是 “安抚”，如果需要待在他身边不断塞到嘴中，则你成为了那个 “道具” : ( 需要尽可能避免成为 “道具” 消耗自己。

> 经过三个月的带娃旅程，对孩子这种 “无理取闹” 的行为有了新的理解：当一个 `三岁` 的大朋友对家长大发脾气，与 `三个月` 的宝宝歇斯底里大声哭泣，有没有可能并不是无理取闹，而是由于家长没有满足某个需求？

读这类文章会让人心情愉悦，一个生命在成长。

---

[沒有表達慾 - Pin 起來！](https://pinchlime.com/letters/no-desire-to-express/)

> 前阵子看到一件很看不顺眼的事（不是犯法或者是任何与我身边的人事物有关的事），本来有很强烈的表达欲望想要分享这件事，但由于某些原因（可能是工作、身分或者是其他类似的东西），我限制自己不能分享。那么为何不用影射、暗指的方式就好？我当时在某篇 journal 里面跟自己激烈地自我对话，最后还是决定不影射或暗指。不过后来我发现，这样子把完整的事与自己的心情记录下来后，好像就有某种「已分享」的感觉了，或者说，我知道这件事总会有某个地方有留下纪录，不会被遗忘，那也就足够了！

我的笔记中有很多类似的自己和自己对话。

---

[You Have to Feel It – Mitchell Hashimoto](https://mitchellh.com/writing/feel-it)

> We, as people, feel something with every interaction. Frustration, joy, relief, confidence. A feeling. A person interacts with our work. Our work evokes a feeling. The feeling matters. The feeling is part of the work. The _desired feeling_ is part of the requirements.

> When you feel it, you know. The feature makes you smile when you use it. It fits right in, like it was always meant to be there. You want to use it again. You want to tell people about it.

想到了很久之前看到的 Burn-out 的缓解方式中，看到自己的工作成果发挥总用、被认可是一种很好的方式。

---



### 书影播客

《只有我一个人觉得特好笑吗？》，刘旸教主的书，通过一些具体的事件场景分享单口喜剧演员们的视角和思考，同时也代入了自己的一些想法，有点像他个人的碎碎念。以下是一些摘录：

> 一个什么事情都能理解的人，当不了喜剧演员，尤其当不了单口喜剧演员。   
> 从业这么些年，我也渐渐感受到，不带着偏见，或者不敢表露出偏见的人，很难制造笑点。也许单口演员，尤其是优秀的单口演员，就是多了那么一丁点勇气，敢于在生活中保留自己的偏见，表达自己的偏见，哪怕因此被一些人所讨厌。   
> 隐藏自己的所有情绪，曲意逢迎地去强制要求自己理解一切自己不理解的事情，抱着“存在即合理”的想法委曲求全，是这个时代最大的愚蠢。

> 我们以骂甲方开始，就以骂甲方结束吧。送大家一个反向类比：   
> “跟甲方相处的日子，就像在度假海滩上一样，放眼望去，全是沙子。”

> 优秀的单口演员郝雨曾经讲过这样一个讽刺那些微信文章的段子:    
> 我丈母娘那天发我一个文章，说现在葡萄不能吃了，尤其是无籽葡萄。那无籽葡萄都是喷避孕药喷成无籽的。我心说，这葡萄多少钱一斤啊，避孕药多少钱一斤啊，我喷这么多药光卖这点儿葡萄我挣得回来吗?有这工夫，我卖避孕药送葡萄行不行啊，我还省点儿力气。而且喷避孕药就能把葡萄喷成无籽的?那我种什么葡萄啊，我种石榴呀!这大石榴一点儿籽儿都没有，咔咔吃，多高兴!

（这个段子是郝雨专场里的段子，我更喜欢他这段的下一段，我大概转述一下：    
（我丈母娘跟我说：注意啊，茄子，茄子不能多吃，吃了容易生病；    
（第二天：注意啊，大辣椒，不能多吃，吃了容易生病；    
（第三天：注意啊，土豆，不能多吃，吃了容易生病；   
（我直接说：妈啊，你是不是就是不喜欢吃地三鲜啊。   

> 网上盛传一个段子:当你去看心理医生时，他工作起来非常简单，就是机械性地说，这是原生家庭问题，这是原生家庭问题，这是原生家庭问题……    
> 虽然是笑谈，但也能看出来原生家庭对一个人的影响之深。我曾经接受了一年的心理咨询，得出的结论当然也是原生家庭问题。我生在内蒙，初一到北京生活。小学的时候我家里很穷，所以我妈经常鞭策我的话就是，要努力读书改变命运，否则会被人瞧不起。这个“瞧不起”一直深深地印在我的脑海里，以至于我直到现在还会觉得别人会因为什么理由瞧不起我。这种情绪在不同时期有不同的投射。    

> 当然，在国内训练“what if”最简单的方法，就是去认识几个东北人，东北人经常说的“咋地”，就是“what if” 这个词最完美的翻译。

（ 我觉得可以更精确，认识几个锦州人，每句话都是 what if

> 喜剧的内核，在我看来，只有乐观。超脱于生命的宋观，敢于嘲笑一切黑暗的乐观，面对死亡放声大笑的乐观。   
> 如果非要说单口演员有些什么不一样的地方，我觉得不是心理疾病的发病率，而是对待疾病的态度。很少有人会像泰勒·汤姆林森一样遇到生命中不能承受之重时，觉得:“天哪，这我可得好好写个段子啊!”    
也许正是这种面对绝境也能保持乐观的心态，才能让人勇敢面对生活中的一切不顺。所以，当你深夜emo，觉得自己此生为何如此不顺时，不妨体验体验喜剧的真正内核，面对这一切笑出声来，可能整个人生会因此走向完全不同的方向哦!    
> 喜剧的内核，是乐观。愿你拥有这份内核。    

> 可见面对自己不想做却不得不做的事情，想让自己渡过难关的方式，就是意识到，这一切本来可以更糟糕的。这也就是单口喜剧演员对抗负面情绪的小小智慧吧

> 不过，这种心态实际上很难一下子扫清，毕竟从世俗最普遍的角度来看，单身还是一种“不正常”，是一个需要解决的“问题”。    
> 但其实我们这一生最应该解决的问题是“如何学会爱自己”。如果单身是个准备期，它唯一的目的就是让我们学会如何爱自己。而当你学会了如何爱自己时是否需要去爱别人就纯粹是一个选择，而不是一种需求了詹·柯克曼的这个专场，直面了自己单身的小纠结但我们看到的却是她选择的方向，一个学会爱自己的人所选择的人生。

《各说各的呗-小块：花有重开日，人总在少年；咱名声在外，但是声名狼藉呀》：这应该是脱口秀和他的朋友们综艺录制之后的闲聊，其中提到了小块的鼻毛段子，小块因为年年上节目，但是年年很早被淘汰，导致喜剧信用很低，逐渐的从他自己吐槽自己不行，到大家都本能觉得他不行，这种状态要想改变需要花很大力气，不过今年的鼻毛段子还是很好的。




## 碎碎念

* 哈尔滨已经有上海秋天的感觉了。
* 日常锻炼和体力劳动完全是两个东西。
* 虚空讨论，倒是没病走两步啊
* 最近体会到了同时进行两份工作，一份体力劳动，一份脑力劳动，脑子是会打架的。
* 再次看到一些人为了展示自己而去没事找事，我能理解那是一种工作方式，但是不能接受。
* 想糊弄总是能糊弄过去的，但何必呢。平时不注意最佳实践，等真需要的时候也就不记得了。
* 突然发现今天一个初中同学结婚，Ta 是先有了孩子再结婚的，在现在好像还挺少见的。