---
title: Weekly Issue-《天生就会跑》
date: 2025-11-16
tags:
- Weekly
description:
---


![上海秋天](https://oss.zdyxry.com/20251116.jpg)

## 文章

### 技术

[Chris's Wiki :: blog/linux/Fedora42OrphanUsrSbinBinaries](https://utcc.utoronto.ca/~cks/space/blog/linux/Fedora42OrphanUsrSbinBinaries)

作者在升级 Fedora 42 之后，发现自己的 `/usr/sbin/` 下有很多不属于任何 RPM 的 binary。之前我也有过类似的经历，不过我的可能大部分是手动 cp 过去的，自从开发机使用 OSTree 之后，不存在这类困扰了。

---

[“捉迷藏”式收割：撕开鲁大师为首系列企业流量劫持黑幕！-技术文章-火绒安全](https://www.huorong.cn/document/tech/vir_report/1858)

火绒发布的针对[[鲁大师]]的恶迹调查，他们的推广条件还挺有意思的：
- 检查浏览器历史记录，如果访问过 12345 等投诉网站、zhihu、微博、看雪、吾爱破解网站的，不推广；
- 安装了火绒、卡巴斯基的，不推广；
- 安装了 IDA、Visual Studio 、WireShark、VSCode 的，不推广；
- 安装了淘客助手的，不推广；
- 还有一些时间相关的策略；


最搞笑的是“值得注意的是，在劫持浏览器的过程中，会对用户是否访问过周鸿祎的微博进行检测，若检测结果为已访问，则不会进行推广。”

---

[sudo-rs Affected By Multiple Security Vulnerabilities - Impacting Ubuntu 25.10](https://www.phoronix.com/news/sudo-rs-security-ubuntu-25.10)

谁如果用了 [[Ubuntu]] 25.10，我会敬佩一声勇士。

---

[AI 辅助编程时代，哪些编程语言会更流行？](https://disksing.com/ai-era-languages/)

> 但现在情况变了。AI 帮我们写代码，“写起来爽 "这个优势基本没了。反而，那些让人" 写起来爽 " 的特性，可能成了 AI 的负担。   
> 我觉得这个趋势已经开始了。越来越多的语言引入类型系统，越来越多的项目强制使用代码格式化工具，这些都在让代码变得更 "结构化"、更 "明确"。

> 注：文中提到关于我在 AI 编程时遇到的各种状况，全都是 AI 生成的，如有不切实际本人概不负责，我只提供了本文的基本观点。

这是现在大家的一个共识了，[[Jetbrains]] 的[年度调查](https://blog.jetbrains.com/go/2025/11/10/go-language-trends-ecosystem-2025/)中也提到了： “Survey data indicates that, on average, Go developers began adopting AI earlier than their peers using other languages, and they continue to use it more extensively for day-to-day tasks.”

现在我写 Python 的时候也会尽量在 AGENTSmd 文件中强调要制定类型，方便之后迭代，我自己 review 代码也方便。

---

[使用 Local Coding Agents 疯狂地并发开发 · xxchan's blog](https://xxchan.me/zh/blog/2025-11-14-concurrent-local-coding-agents/)

这篇关于 Agents 使用的思考很推荐，我日常停留在“我成了瓶颈”的状态，事情很多很杂，Agents 很快就把活做完了，在多个“结果”之间进行切换、验证、发布，单独看某个任务肯定是效率有提高，整体上就很难说了。

找时间试用一下 [GitHub - xxchan/AgentDev: A CLI tool for managing Agent instances with git worktree](https://github.com/xxchan/AgentDev) 

---

[A prison of my own making-Jana's cozy corner](https://jsteuernagel.de/posts/a-prison-of-my-own-making/)

> I was overwhelmed by all of the things that I convinced myself to be necessary. I was overwhelmed by all of the things that I convinced myself to be necessary.
> - **Everything needs to be declarative**
> - **Machines as cattle, not pets**
> - **Immutable systems and containers**
> - **GitOps all the things**
> - **Automated deployment**
> - **CI/CD pipeline**
> - **Security considerations**

> Spelling it out now, it feels like I should have realized way earlier what was killing my joy. But now I did, so I'll be undoing a lot of this mess.

这周刚好和同事闲聊到了这个，大多数场景下，工作里面的最佳实践，对于个人场景来说都是不需要的，如果它还带给你痛苦，那直接远离就好。

---

[Calculating String length and width – Fun with Unicode | Tom de Bruijn](https://tomdebruijn.com/posts/rust-string-length-width-calculations/)

以 [[Rust]] 为例讨论 `.len()` 、`.chars().count()` 、`graphemes(true).count()` 的差异。

在说“字符串长度”的时候，到底在说啥，是字节长度、还是字符数量、还是 grapheme cluster，即使是 grapheme cluster 也可能不是最终用户看到的显示宽度。

我讨厌 emoji 的滥用。

---

[Bending Spoons Cofounders Become Billionaires After Italian Startup Raises At $11 Billion Valuation](https://www.forbes.com/sites/iainmartin/2025/10/30/bending-spoons-cofounders-become-billionaire-after-italian-startup-raises-at-11-billion-valuation/)

[[Bending Spoons]] 最新融资后估值达到了 110 亿美元，4 位联合创始人都已经是亿万身价了。这个公司真有意思，收购成熟的产品，改造，然后盈利，感觉像是有一批能力超强的雇佣兵，收购之后可以进行快速的迭代改造，短期完成后继续下一个目标。代表是 [[Evernote]]。

---


[真实、残酷的 AI 就业冲击 —— 从一篇极其精彩的哈佛论文聊起](https://archive.is/14OIL#selection-199.11-199.15)

[工作, 后工作：就业市场崩溃观察笔记 – Telegraph](https://telegra.ph/Work-After-Work-Notes-From-an-Unemployed-New-Grad-Watching-the-Job-Market-Break-11-10)

两篇连着看，AI 采纳者公司在 2023 年后初级岗位招聘量显著下降，批发与零售业是重灾区。招聘的逻辑也发生了变化，先考虑“AI 能不能做”，再考虑是否真的需要一个员工。

---



### 生活

[Make it Possible, Then Make it Normal · Daniel Mangum](https://danielmangum.com/posts/possible-then-normal/)

作者 2023 年给自己定了跑完 2023 英里的目标，最终跑完了 3000 英里，今年没有给自己定目标，但是一个平常的周末发现，自己居然比 2023 年还要早两个月完成了当时的目标。

第一次完成目标很艰难很兴奋，之后将其变为日常，每一次完成它，那就是明知道它需要多少努力，但是还是完成了它，对自己来说那就是非凡。

---
[Eliud Kipchoge Custom Nike New York City Marathon Top — NIKE, Inc.](https://about.nike.com/en/magazine/eliud-kipchoge-radical-airflow-new-york-city-marathon)

[[Nike]] 为基普乔格定制的运动服，可以让汗水快速蒸发。国内好像轻功、必迈也有类似的“科技”衣服，不知道实际效果怎么样。

---

[Valve is about to win the console generation - Xe Iaso](https://xeiaso.net/blog/2025/valve-is-about-to-win-the-console-generation/)

> The biggest difference between SteamOS and other console operating systems is that SteamOS is just an immutable image-based fork of Arch Linux with a skin on top. If you can do it with a normal PC, you can do it on SteamOS.

> Yes, Steam Machine is optimized for gaming, but it's still your PC. Install your own apps, or even another operating system. Who are we to tell you how to use your computer?

---

[日本浮生录：追逐棕熊、户外越野，在北海道遇见最美秋日 - Simon's Blog](https://song.al/Hokkaido01)

理论上我今天经历了两个秋天，分别是在哈尔滨和上海，可惜哈尔滨的秋天全称没有出门，上海的秋天又很难说感受到秋。

---

[用AI假图骗“仅退款”，这是今年双十一最脏的一幕。](https://archive.is/PwbYt)

> 就是在双十一期间，大家都知道，退货率肯定会变高，然后，就有很多人，用 AI 来 P 图，骗商家 “仅退款”。

人可以坏成什么样。

---

[纽约上州游记之三——尼亚加拉大瀑布 - David Feng个人网站](https://davidfeng.us/zh-cn/2025-10-31-niagara-falls/)

> 注意地图上方是西边。河对岸是加拿大。没错，此处加拿大在美国的西边。（冷知识，底特律附近有一段美加边境加拿大在美国南边。

> 最大的马蹄瀑布。宽 790 米，尼亚加拉河 90% 的水量从此处倾泻而下，每秒钟水量可以填满一万五千个浴缸！

我好像还没见过大瀑布？仔细想了想，世博公园那个小落差的肯定是不算的，那好像真的没有啊，

不知道为什么，突然想起之前看这个[纽芬兰自驾 vlog](https://space.bilibili.com/3305831/lists/3622177?type=series) 的时候，总觉得“纽芬兰”应该在南半球或者在欧洲很北的地方。

---

[古希腊思想通识课-希罗多德 | imesong.com](https://imesong.com/posts/%E5%8F%A4%E5%B8%8C%E8%85%8A%E6%80%9D%E6%83%B3%E9%80%9A%E8%AF%86%E8%AF%BE-%E5%B8%8C%E7%BD%97%E5%A4%9A%E5%BE%B7/)

> 关于经典的意义，书中引用了著名文学评论家哈罗德·布鲁姆在《西方正典》中的一段话：   
> 阅读经典并非为了服务于意识形态……深入研读经典既不会使人变好或变坏，也不会使公民变得更有用或更有害。心灵的自我对话本质上是一种社会现实。西方经典的全部意义在于帮助人善用自己的孤独，而这种孤独的最终形式是一个人与自己死亡的相遇。

---

### 书影播客

《天生就会跑》，《天生就会跑 2.0》，作者是克里斯托弗・麦克杜格尔，美联社记者。这两本书如果单独说跑步的部分，其实很少，更多的是在讲关于跑步的故事，可能是因为第二本的故事更纯粹，我更喜欢第二本。在阅读的时候问自己一些问题：如何跑步？在买鞋子的时候现在通常看到：稳定/支撑/缓冲/训练/竞赛等分类，在有这些”专业“跑鞋之前，是怎么跑步的？书中的观点是回到原始状态，不只是跑步的原始状态，生活方式也要回到原始状态，比如作者说自己按照塔拉乌马拉人的方式生活和训练，结果是跑得更快了，受伤更少了，我觉得和他短时间体重下降了 12 公斤有很大关系。怎么舒服怎么跑吧。

《天生就会跑》的中文译者是严冬冬，如果之前看过《比山更高》的话，应该对他不陌生，是一名自由登山者，在 2008 年奥运火炬传递中登顶了珠峰，崇尚阿式攀登，《比山更高》中提到他当时靠着翻译收入来支撑自己登山，这本《天生就会跑》应该就是其中之一了。严冬冬在 2012 年登山时遇难。


一些标注：


> 不正常的反而是极少数从来不受伤的跑步者。百分之八十的跑步者每年都会受伤。进行这项运动时，不管你体重是大是小，速度是快是慢，距离是长是短，都有可能伤到膝盖、胫骨、跟腱、髋部和足跟。

> 美国的长距离耐力跑运动经历过三次大起大落，每一次兴起都是在国家遭遇危机的时期。这三次起落或许并非偶然，也许是因为人类心理存在着某种开关机制，意识到危险来临时，就会激活最原始的求生本能。在缓解压力和营造快感方面，跑步甚至比性更有作为。人类天生就具有奔跑的欲望，需要做的只是将它释放出来。

> 我说，“那正确的跑步姿势是什么样子的？”，“是个不朽的问题。”戴维斯医生说。


> 我们把‘拉拉基帕瑞’叫做生命游戏。”安杰尔说，“你无法预料比赛究竟有多艰苦，也不知道它什么时候才会结束。你不能控制它的进程，只能尽力去适应。”


> 一个周日，安起大早跑了二十英里，回家吃过早饭后又出门跑了二十英里。因为有些家务活要做，跑完她便回到家里忙碌起来。到傍晚，她对这一天很满意：不仅做完了家务活，还跑了四十英里。于是作为奖励，她又出门跑了十五英里。


> 按照传统运动医学的说法，一周内跑步里程达到一百英里，基本就会导致膝盖损伤，而超长距离耐力跑选手却可以在一天之内跑完这么长的距离，有些选手每周的训练量甚至超过两百英里，却仍然不会受伤。

> 就连业余的耐力跑选手都清楚，比赛时最聪明的策略是紧跟在领先选手身后，尽量保持稳定的速度，临近终点时全力冲刺。


> 但问题并不在为什么别人跑得越来越快了，而是为什么我们跑得越来越慢了。事实正是：美国长跑运动的衰落过程，刚好跟金钱介入其中的过程相吻合。一九八四年之后，奥运会开始对专业运动员开放，这便意味着跑鞋厂商可以付钱给长跑运动员，把他们包装成“专业选手”​。

> 泰德有些纳闷，在足弓支撑技术、内外翻控制技术和凝胶减震技术发明之前的几百万年里，人类究竟是怎么奔跑的。

> 九个月的塔拉乌马拉式训练，让我发生了彻底的转变：体重减了十二公斤，可以很轻松地跑完过去会要了我命的路程。尽管我每周的训练量超过八十英里，但我仍然精力旺盛，总期待着下一次训练。最重要的是，十年来第一次，我没有因为高强度的跑步受伤。​“他绝对是个奇迹创造者。​”

> 许你可以通过拉伸韧带来避免受伤？徒劳。一九九三年，​《美国运动医学期刊》发表了一份针对此问题的研究报告，研究者选择了两组荷兰运动员作为受试者，其中一组在每次跑步之前先拉伸韧带作为热身，另一组则直接开跑。实验结果是，两组运动员的受伤概率完全一致。次年在夏威夷大学进行的进一步研究则表明，拉伸韧带甚至会起到反效果，让受伤概率提高百分之三十三。

> 换句话说，结论是：鞋底的缓冲性越好，实际为双脚提供的保护反而越差。

> 有时患者不听从我们的建议，反倒能让我们学到新东西。​”戴维斯博士说，​“我想，足底筋膜炎之所以在美国如此普遍，或许正是因为我们平时束缚足部肌肉发挥它应有的作用。​”那位患者的康复让她无比振奋，她索性也开始尝试光脚行走。

> 小步快频的运动方式，比力强幅大的方式更有效率。​”

> 每七名死于癌症的患者中，就有一名是因为体脂含量过高而发病的。换句话说，减少体脂可以降低患癌的风险。



## 碎碎念

* 我想要一个基于 ostree 的 fedora server 版本，现在 ucore 是基于 coreos 的，安装起来真是麻烦。
* Mirantis 现在的标语是：Mirantis: Build AI Infrastructure Your Way, Anywhere.
* 发现我的稍后阅读是真的会阅读， Youtube 稍后再看，是真的不会再看的。。。
* 你的生活新鲜吗？你的生活肯定不新鲜！
* 感觉这个 App 的广告都在一步步的试探着用户的底线，现在 TG 会在信息流中插入广告了，下一步呢？每条信息带一个广告？
* 正经叭叭大刘唱了一句“北京晚报”，结果没人接住，感觉自己也确实年纪大了。 ”北京晚报，有人征婚有人打广告，其实就是吹牛逼和想糙“
* Wails 整体还是挺好的，对平时用 Golang 的用户，上手很愉快。
* Veritas 和 Commvault 都退出了，最近是有什么风声么？
* 玩弄流量，迟早被流量玩死。
* 主理人的英文是 curator 么？
* 好天气，心情好