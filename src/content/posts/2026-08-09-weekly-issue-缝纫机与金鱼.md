---
title: Weekly Issue-《缝纫机与金鱼》
date: "2026-08-09:00:00.000Z"
slug: "Weekly-Issue-sewing-machine-and-goldfish"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Scaling the GitLab database](https://about.gitlab.com/blog/scaling-the-gitlab-database/)   
[Scaling Postgres with Read Replicas & Using WAL to Counter Stale Reads — brandur.org](https://brandur.org/postgres-reads)   
[Don't add a read replica until you've read this | Blog | incident.io](https://incident.io/blog/dont-add-a-read-replica-until-youve-read-this)   

关于 [[PostgreSQL]] 引入读副本之后的处理方式的几篇文章，基于 WAL LSN 来解决脏读的问题，核心方式都是类似的，只是有些存在了 Redis 里，有些存在 [[PostgreSQL]] 自身，有些是直接返回 Nack 后续在处理。

---

[Storing times for human events](https://simonwillison.net/2024/Nov/27/storing-times-for-human-events/)   
[Storing times for human events | Lobsters](https://lobste.rs/s/shckuc/storing_times_for_human_events)   
[reddit.com/r/webdev/comments/1k2uuoh/i\_hate\_timezones/](https://www.reddit.com/r/webdev/comments/1k2uuoh/i_hate_timezones/)   
[Storing UTC is not a silver bullet | Jon Skeet's coding blog](https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/)

最近遇到了一些时区相关的问题，把之前收藏的一些博客找出来又看了一遍。很多应用会把未来会议的时间转换为 UTC 保存，同时保存当地的时区信息，但是时区规则可能会变化，如果创建事件时和事件到来时的时区规则发生了变化，那么用户看到的时间就是错误的。推荐记录当地时间+时区+UTC 偏移，UTC 偏移是为了避免夏令时切换时部分时间出现 2 次时无法确定哪次是预期的。还有些评论说直接存目标活动的 GPS 定位的，因为 GPS 定位所在的时区也可能变化。

黎巴嫩在 2023 年 3 月居然出现过不同的机构使用不同的时区的现象，真是离了大谱。

---

[HDD failure rates by manufacturer revealed](https://www.blocksandfiles.com/disk/2026/08/07/hdd-failure-rates-by-manufacturer-revealed/5284845)

> 在保持硬盘的使用年限、容量、外形规格以及温度不变的情况下，我们发现 HGST 公司的硬盘故障率最低，约为 Seagate 硬盘故障率的 41%。WD 公司的硬盘故障率约为 Seagate 硬盘故障率的 52%，但明显低于 HGST 的故障率。而 Toshiba 公司的硬盘故障率则约为 Seagate 硬盘故障率的 107%，因此故障率最高。

---

### 生活

[亡母二十周年祭 – Alien外星人](https://aliengu.com/archives/35701)

> 回温哥华之后，儿子偶尔会问一些关于死亡的问题。他问我和太太「以后我会不会和你们分开」，我们说不会，他又问「那更久更久以后，我们会不会分开」，我们说也不会。他不再问了，沉默，之后是无声的啜泣。我们问怎么了，他说「我知道我们以后还是会分开的」。   
> 我怀疑我遗传了什么有毒的东西给他。   
> 2006 年 8 月 2 日上午，我在母亲房中无忧无虑的玩着 45 度俯视角射击游戏孤单枪手 2，母亲穿上衣服和鞋子，站在门口对我说要去北京办点事情，我随意应承了一句，瞟了一眼门口，然后继续打击异形保护地球。四天后，我亲手给她拔下管子。    
> 终于二十年了。

---

[Don't be a meat proxy](https://gruhn.me/blog/2026-08-03/)

> Making that effort is value you can add.

---

[社交媒体、香烟、科技与个人](https://limboy.me/posts/social-media-and-cigarettes-technology)

> 当一种更可控、更安全的交流方式随时可用，人就可能逐渐减少对真实交谈中那种不确定性的练习。

> 社交媒体也改变了人衡量自己的方式。在面对面的生活中，一个人通常只能接触有限数量的同事、朋友和邻居。社交媒体却让比较的范围变得近乎无限。用户拿自己与别人精心挑选的片段比较，很容易产生一种模糊的落后感：别人的生活似乎总在发生，自己的生活却显得停滞。

> 一个人只有在不急着逃离沉默时，才可能意识到自己究竟在担心什么、想念什么，或真正想做什么。

过于警惕也没必要，习惯是很难改变的，无论社交媒体能带来多少好处，始终不能替代线下人与人之间的沟通。

---

[Why I Stopped Arguing With People](https://wangcong.org/2026-06-30-why-i-stopped-arguing-with-people.html)

> 有时候，我是以微弱优势获胜的，但最终还是输掉了比赛。更常见的情况是，我什么都没得到：我会看着那个人越来越坚信自己刚刚反驳过的观点，而整个房间则静静地转向了他们的方向。从技术上讲，我确实赢了，但实际上却完全独自一人离开现场了。

> 当你与某人争论时，你以为自己是在讨论某个观点。但实际上往往并非如此。你真正是在挑战他们的自我认知。

> 许多人都是出于自我意识的驱动而行事。他们的观点并非他们所持有的立场；它们本身就是一种立场。如果你能证明某个观点是错误的，那并不意味着你纠正了一个事实，而只是攻击了那个人的人格。因此，他们会像任何自卫的人一样来捍卫自己的观点——不是用理性来对抗，而是用抵抗来对抗。你的论点越有力，他们就越会进行顽强的抵抗。

---

[随笔——AI 到底是在替你劳动，还是替你思考？](https://nova.moe/ai-for-labor-or-mind/)

> 好处是对于常见和覆盖常见路径的解决问题的速度变得越来越快，Human in the loop 的时间越来越少（当然，这个是模型能力变强的目标），大家对于事情解决的效率要求和预期变得越来越高，同样的工作可以交给更少的人来做，剩余的人可以完成更多的工作。   
> 坏处也很明显：人对于跨领域的理解需求变得越来越少，每个人需要并行处理（可能多半是 review 模型的工作）的工作会越来越多，然后可能大家都越来越累了。

持续的让 Agent 去解决问题，可能会让一些人产生"我解决了"的错觉/信心，这是短视频不会有的副作用，短视频刷多了，顶多你会比别人多知道 N 个网梗，通常不会说自己真的知道了 blabla"知识"，不会让你产生一些莫名的错觉自己是某个领域的专家。

---

[价值观](https://limboy.me/posts/values)

> - 环境的力量大于反思。长期和什么人待在一起，对你的塑造超过你想清楚的一切。   
> - 只有付出代价时，价值观才被测量，不要代价的价值观是偏好。你说你诚实，如果诚实让你亏钱的时候还能不能选择诚实。    
> - 一个人声称自己重视什么，并不一定等于他真正重视什么。相比语言，更值得观察的是：时间花在哪里，钱花在哪里，注意力流向哪里，关键时刻如何选择。    
> - 可以通过做事之后的反馈反推自己的价值观：什么事情很累却觉得值得，什么成功得到了却觉得空虚，什么东西失去以后才发现不能接受。    

狼人杀教会我的东西：不看一个人说了什么，看一个人做了什么。

---

### 书影播客

《海鸥耶丁》，介绍是长篇无字图像小说，可以理解为一本漫画书，因为没有文字，所以可以有很多解读的角度。画面色彩太过于浓烈，看一阵子需要缓一缓眼睛。


《缝纫机与金鱼》，周末台风天在家里读完这本书很幸运。讲述的是主人公安田佳景的故事， 老年生活比想象中更难，借着护理院、儿媳妇来讲述自己的一生重大节点。我不记得为什么在豆瓣上标记了这本书，我看完之后还特意搜索了很多地方，都没有搜到，值得多年之后再读一遍。想到了我奶奶。

## 碎碎念

* kernel 升级后，sysstat 可能会出现不兼容的情况，导致解析结果是完全错误的。
* 没有逻辑，全是情绪。
* 半年内第三个同事去意大利溜达。
* 都立秋了。
* 同事买的阿里云 qwen coding plan，一个 patch 都没 review 完就用光了 5h 额度，客服打电话过来，建议从个人版升级到团队版，因为团队版没有 5h/1w 限额，只有月限额，你可以一次性用完一个月的额度，销售鬼才。
* 看到一个人的自我介绍：Canonical 、Rancher、HPE、lawyer。等等，lawyer ？这也太酷了
* 2022 年朋友推荐了倍乐，几次尝试都被排队劝退了，终于趁着朋友来上海吃到了。
* 最近的云挺漂亮的。
* Bistro 这个词最早可以追溯到19世纪的巴黎。一个流传很广的说法是，当时俄罗斯士兵在占领巴黎时，用俄语中意为“快点”（быстро, bistro）的词催促店家上菜，后来这个词就演变成了这类快捷、随意小餐馆的代称。 最初，Bistro 就像是法国的“大排档”或“苍蝇小馆”，为普通人提供平价、家常的饭菜和葡萄酒，主打一个方便快捷。
* 在一个意想不到的项目中看到了 Dreamacro 的身影。
* 还是得多看代码啊，有些你不知道自己不知道的东西，还是很难通过 AI 问出来的