---
title: Weekly Issue-五一假期
date: "2026-05-10:00:00.000Z"
slug: "Weekly-Issue-五一假期"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Ghostty Is Leaving GitHub – Mitchell Hashimoto](https://mitchellh.com/writing/ghostty-leaving-github)   
[Before GitHub | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2026/4/28/before-github/)   
[An update on GitHub availability - The GitHub Blog](https://github.blog/news-insights/company-news/an-update-on-github-availability/)   

[[GitHub]] 的重点不是 [[Git]]，而是 `Hub`，当 Issue、PR 这种核心功能故障，影响范围太大了，很多原有提供 API 服务的 SaaS ，不主动做改变的话，在 AI 时代都吃不消。

---

[GitHub - LobsterTrap/tank-os · GitHub](https://github.com/LobsterTrap/tank-os)

基于 [[bootc]] 的 [[OpenClaw]] 定制运行环境，最小化、不可变， 不得不说，[[bootc]] 在定制化方便程度上真的是太方便了。另外这个 Org 是 [[RedHat]] 搞的，Org 下还有 [GitHub - LobsterTrap/lola: Lola is able to package AI Context Modules or skills into a distributed package to be supported across multiple AI assistants. Think of your skill as the RPM package and Lola as the YUM/DNF. Write your skills once, run everywhere. · GitHub](https://github.com/LobsterTrap/lola) 这种 [[SKILL]] 的包管理器，感觉基于这种通用 Agent 的管理方向还是有搞头的。

---


[2026.04 云原生相关信息简报](https://quaily.com/cloud-native-ralated/p/cloud-native-informational-briefing-april)

>2. KubeVirt v1.8：机密计算、多 Hypervisor 与性能优化全面升级    
>- Hypervisor 抽象层（HAL）：引入 Hypervisor Abstraction Layer，使 KubeVirt 能够支持除 KVM 之外的多种 Hypervisor 后端，同时默认仍保持 KVM 优先策略。

[cloud-hypervisor: Assess integration with KubeVirt](https://github.com/cloud-hypervisor/cloud-hypervisor/issues/4201)：

> That hypervisor abstraction layer is the work from my colleague for adding MSHV support. It is not really related to the VMM layer. The VMM is still QEMU.

---
[AI 正在吞噬我们的耐心 | 静かな森](https://innei.in/posts/experience/ai-is-eating-our-patience)

> 我不再像以前一样，可以很自豪地做出一个项目，然后和别人侃侃而谈里面的细节，比如为什么这样设计、它的优点和优势在哪、以及性能表现等等。

---
[To my students](http://ozark.hendrix.edu/~yorgey/forest/00FD/index.xml) 

> Where people are racing to create intelligent machines, but only in order to make them slaves.

> - Cultivate your ability to think deeply. Do whatever it takes to carve out distraction-free bubbles for yourself in both space and time. This might mean saying no to technologies or patterns of working that others say are critical or inevitable.   
> - Care deeply about your craft. Refactor code until it is clear and elegant. Write good documentation for other humans to read. Have the courage to go slowly, especially when everyone else is telling you that you need to go fast and cut corners.    
> - Care more about people, relationships, and justice than you do about profits, code, or productivity.    

**Above all, be motivated by love instead of fear.**

---

[Uber Spends Full 2026 AI Budget in 4 Months](https://www.briefs.co/news/uber-torches-entire-2026-ai-budget-on-claude-code-in-four-months/)

[[Uber]] 4 个月已经用光了全年的 AI 预算。评论区“I just can't figure how _how_ to burn that much money a month responsibly“中的 `responsibly` 用的好，公司搞 token 消耗排名，那员工自然就会在任何场合尽可能的多用 token，这种现象有一个专有词“Tokenmaxxing”，这已经是负和博弈了？

---

[当我们在维护模型 API 服务时我们在维护什么 | Manjusaka](https://www.manjusaka.blog/posts/2026/03/15/what-we-maintain-when-maintaining-model-api)

> 整个项目最值得说的一个设计决策——用注册表 + 动态导入来管理多版本，让 app.py 在加新版本时一行不用改。

这种动态注册的方式，也避免了 Flask/FastAPI 的装饰器都是直接挂在应用对象上的问题。

---

[Pydantic 不是免费的——聊聊数据校验的边界 | Manjusaka](https://www.manjusaka.blog/posts/2026/03/23/the-boundary-of-pydantic/)

> 数据校验这件事，从来不是越多越好。它有明确的边界——边界之内是契约和安全，边界之外是无谓的开销。Pydantic 是非常好的工具，但用它的人也得知道自己什么时候用、为什么用。

虽然讲的是 [[Pydantic]] 的具体使用场景，但是我种草了 [[beartype]]，想办法在项目中引入一下“Beartype is zero-cost. Beartype inflicts no harmful developer tradeoffs”

---
[Building for the future](https://blog.cloudflare.com/building-for-the-future/)

什么是 future ？“We are writing to let you know directly that we’ve made the decision to reduce Cloudflare’s workforce by more than 1,100 employees globally”。    
“Cloudflare’s usage of AI has increased by more than 600% in the last three months alone. ”， AI 成本大增，但是收益没增，又不能不用，只能削减人力成本来维持利润。

当我以为股价大涨的时候，结果大跌 23%。

---

[I don't want your PRs anymore](https://dpc.pw/posts/i-dont-want-your-prs-anymore/)

项目作者越来越难处理 PR，同样的，作为普通用户，我感觉会出现越来越多的 fork，然后自己维护自己的需求了。
 
---




### 生活


[Marathon world record evolution (2025) | The Blog by Javier](https://theblogbyjavier.com/2025/09/30/marathon-world-record-evolution-2025/)

> Most of the times below 2h08′ are achieved **between 23 and 33 years old**, but indeed most of the best ones are achieved **between 28 and 39** years old, with the exception of the 3 marathons ran by Kelvin Kiptum, including his current world record.

> Another interesting chart to relate best times and age is the histogram below. In that one we can see that effectively most of the times below 2h08′ are achieved between 24 and 30 years old, and **between 23 and 33** (both included) **80%** of those times are achieved.

在马拉松领域，肯尼亚和埃塞俄比亚是绝对的领先，大多数出成绩的年纪是在 23 到 33 之间。

---
[我在远东种大豆](https://hanyang.wtf/p/817)

> 但王哥又不只是农民，他也是地主。最标准意义上的地主，在远东承包了一万五千亩地，相当于一个西湖加五个故宫。   
> 但王哥又不像地主、更不像资本家：首先他对挣绝对意义上的钱没有兴趣，虽然他嘴上说的是钱，但一切收入都会被他投入到更多的地里。他挣钱是为了种地，而种地却不是为了存钱。   

> 最主要的是年龄在这里是个准入机制：五十岁以下概不考虑。因为五十岁以下的年轻农民是没有足够的经验解决每一件事儿的。这里需要一个人有能力解决所有事儿。只有在被上个时代东北农场所训练的农民，再配上几十年的工作经验，才配得上这无垠的黑土。

>「咱们中国是一个地贵人便宜的世界，我想看看一个人贵地便宜的世界是什么样。」   
> 处处都不一样。即使合作种地的大哥们都是黑龙江人，但跨过乌苏里江来到远东，他们仿佛都换了一种思维模式：能靠换一片地解决的，那就换一片地；能用机器干的，就用机器干；如果一件事必须要人干，那就干脆不干。

> 说到这里我希望你能真正理解「广种薄收」是什么意思——人贵到没有人，地便宜到只剩地，这样的世界里，运行着另一套逻辑。一切都依赖机械运作，这里像是黑灯工厂更甚于我们了解的那个田园牧歌的乡村。

在 2026 年，种地还是要看天吃饭的。

---


### 书影播客


《真要跑步了吗？那太好了！》，比想象中要好很多，如果我开始跑步的时候看的是这本书，感觉会容易一些。

[《带着女儿跑火车》](https://space.bilibili.com/3546603208050819/lists/6334051?type=season)，推荐下这个 vlog，忘记是怎么看到的了，博主是一名货车司机，觉得女儿的一些观点不对，于是在暑假带着女儿跑了一趟货车，记录了沿途中父女的对话，里面的很多道理现在的我已经知道了，但是如果在中学的时候了解，可能会有些不同。

## 五一假期

趁着五一假期，连着把 2025 年的年假休了，一共 10 天，去了苏州和无锡，然后回哈尔滨呆了几天。结论就是公共假期最好在家里休息，热门景区的人流真的可怕。

我第一次去苏州是在 2017 年，后面又去了几次，只记得苏州博物馆和几个园子，直到自己进了虎丘的园子里面，才想起来自己去过。当时是第一次去南方，拍了张七里山塘的照片发朋友圈，配文是“这是我印象中南方的样子“，有一个丽水的朋友评论说“这是江南的样子，不是南方的样子“。我印象中最后一次去苏州就是前几年的事情，当时苏博门口还没有地铁站，现在去就有了。第一次去七里山塘的时候，还不需要排队，现在已经需要排几个小时才能进去。之前一直有一个刻板印象，一线城市的变化很慢，该建的都已经建好了，现在想想这个想法真是错的离谱，越是一线城市，变化越快，反而是二三线城市没什么生机，可能十几年都没什么变化。

无锡之前看演出去过一次，路过清名桥的时候，发现之前的一个脱口秀俱乐部现在已经变成餐厅了。这次去了鼋头渚，很不错，我很喜欢，也可能是因为大部分人已经回去上班了，人不多，适合闲逛。在太湖仙岛的时候，想到了镰仓的江之岛，整体的感觉很像，我觉得可以称江之岛是小太湖仙岛。只是太湖仙岛的神位貌似有些乱，先后看到了：玉帝、西王母、观音、佛祖、妈祖、老子。感觉是泉州人来搞的建设。


![](https://oss.zdyxry.com/20260501-1.png)
刻板的江南印象

![](https://oss.zdyxry.com/20260501-2.jpg)
登高望远

![](https://oss.zdyxry.com/20260501-3.jpg)
好胖的鸟

![](https://oss.zdyxry.com/20260501-4.jpg)
想出放几艘船的人是个人才

## 碎碎念

* 日常在世博转悠的我，周末连续两天去西岸躺着，朋友住在普陀，周末来世博躺着。
* Obsidian Web Clipper 的阅读器模式，就是我之前一直想要的东西，真的太好用了
* 破二的人穿阿迪的鞋子，一些人就来嘲讽 Nike，这完全没必要，在当时来看，Nike 能做出那个计划，无论是否是为了营销，都是值得称赞的。
* 垂直头部播客一个月的商单 20w ？
* 昨天遇到了一个问题，对方没有先扔到 AI 问，而是先来问 Oncall，有一点诧异。
* 人都是那一波人，哪里热就往哪个方向去。
* 一些修复问题的脑回路很惊奇。
* 突然感觉硬盘状态变差了，争点气，别这时候给我坏了。
* 使用拼多多退货，分别在拼多多、丰巢、顺丰 3 个 App 找付费按钮。
* 同事中有人开始打替尔泊肽了。
* Copy Fail 的披露流程有些奇怪。
* 大钟寺家乐福买的水壶被我摔裂了，又一个 N 年的老物件无了。
* 邓氏编码（D-U-N-S® Number）是由邓白氏集团签发的实时动态的企业身份标识码。 该编码是由邓白氏集团签发的一种企业身份标识，为一个九位数字的全球编码系统，每个号码对应唯一的企业实体且不会重复使用。 邓氏编码被国际标准组织、50多家全球行业及贸易机构、美国政府及欧盟等承认或要求使用。
* initiative 是个好词啊
* 每次在写字楼看到有人抽烟，都想念融科
* 在西岸中环索康尼店铺试了试胜利 23，脚感确实不错，但是线上 1000 出头，线下 1390，买了不是大傻子么。
* 西岸遛猫遛狗的真多，世博输了
* 对食可以是宦官与宫女，或是宫女与宫女之间的恋情，但多为短暂交往；而菜户则专指宦官与宫女的长久稳定恋爱关系，有如夫妻。
* 太久没出上海溜达，充电宝都忘了
* 自从同事开始聊买房，我的微信天天推各种上海新盘
* 手机屏幕右下角有个黑点，不知道什么时候出现的
* 我 2017 年来过虎丘，但是我忘了
* 星空卫视黄了？
* 我奶说上海今天 22 度，她每天会看上海的天气预报。
* 家里老人说的最多的话：钱薄了。
* 假期结束，上班