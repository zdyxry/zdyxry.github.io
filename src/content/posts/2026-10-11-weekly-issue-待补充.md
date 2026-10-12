---
title: Weekly Issue-国庆假期
date: "2026-10-11:00:00.000Z"
slug: "Weekly-Issue-National-Day-Holiday"
tags:
  - Weekly
description:
---

## 文章

### 技术

[How I manage my agents](https://arslan.io/2026/09/11/how-i-manage-my-agents/)

半年前如何让 Agent 完成一项工作已经不需要做什么了，现在面临的问题是当多个 Agent 同时工作时，怎么协调，我现在日常用 RaftBuild，每个对话都设置为一个任务，体感是不错，但由于我日常工作主要在 Slack/企业微信，我还需要人肉来回粘贴消息，终究是没有形成一个完整的 Loop。在 DeepSeek v4.1 Flash 发布后，假设有足够的 token 可以使用，那么如何更好让多个 Agent 工作是一个问题，作者基于 git 来采用文件层级的方式描述任务状态，协调器负责任务状态的更新，任务具体的执行交由其他 agent 处理，看描述应该不是 SubAgent 模型，而是一个全新的 Agent Session。

---

[小议 agent Harness 设计上的 tradeoff](https://gaocegege.com/Blog/genai/server-side-agent)

> 我在我的 PC 上做了非常多的配置，丝滑地 migrate 到一个 cloud based 环境上，并且保持双向同步，是困难且收益不大的。Coding 更主要的需求是远程控制。

> 如果是 server side agent，本身带了多租户的设计，如何保证 evaluation 的对象，agent 的 harness 是跟线上一致的，如何做合理的抽象和设计来支持离线自动化的 evaluation，并且过程中的工具调用是在一个可复现的环境里，能够多次重复执行，也是一个考验设计的地方。

---

[检查工具的自包含分发](https://chaneyzorn.github.io/codes/self-contained-dist-tools/)

> 再次做类似的工具，我不再认为使用 ansible 就是脚本小子。我认为关键在于数据接口的标准化：这一次我没有使用 http 接口来定义标准结构，而是用 json schema 来约定每一个检查模块的输出内容。脚本小子的问题不在于写冗长的脚本，而是不会因地制宜。使用 ansible 后节省大量精力用于思考更关键的问题，这就值得。

用合适的工具做合适的事情。

---

[Inside ZCode: Silently Uploading Your Entire Git History to the Cloud](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)

> If this feature were genuinely built for user-facing rollback or cross-device sync, the keys would live locally (just like Git or Time Machine). **A key that only the server can use serves exactly one purpose: making sure the server can read your code whenever it wants.**

[[ZCode]] 这种默默地行为，很讨厌。

---

[智算卡生态进校园之我见](https://jia.je/misc/2026/09/22/xpu-in-campus/)

> 你应当把东西做得非常可用、门槛足够低、足够开放，让用户在 90% 的日常使用中不需要和你的任何人沟通，自己买卡、自己从网上获取资料，就能很好地用起来。这是长期要做的功课。短期内，国产智算卡要迈出的第一步，是先让用户觉得"这东西能用、靠谱"，愿意把它当作英伟达的一个下位替代，至少先做到"可替代"，再谈进一步的事情。下一步，才是去谈超越英伟达：和你一样好用，甚至更好用、更容易用，在某些方面比你做得更好，这才是未来的方向。

对于任何特定行业想要替代竞品的软件来说，标准都是一样的，易用性的潜在影响力是很大的。

---

[Buildkite service disruption](https://www.buildkitestatus.com/incidents/tm6746k61p73)
[Thoughts on the Buildkite Aug 25 incident – Surfing Complexity](https://surfingcomplexity.blog/2026/09/01/thoughts-on-the-buildkite-aug-25-incident/)

Buildkite 最近一直在将生产集群负载从 ECS 迁移到 EKS，这是一项长周期的事情，目前已经迁移了 4 个月，在迁移时，对于一些时间敏感的通知类型任务，为了保证有足够的容量，所以将最大副本数设置的很大。   
在新的应用迁移时，应用 Pod 数量激增（surge），触发了 EKS 的横向扩展，同时，一些原有的应用也触发了横向扩展，因为现有集群资源不足，所以原有应用的横向扩展一直没有办法完成，所以触发的服务扩容指标没发生变化，导致发出了更多的 pod 创建请求，本来自动扩缩容会因为服务配置的最大数量限制，而终止后续请求，但是因为前面把最大副本数设置的很大，所以会一直发送。

CoreDNS 的原有监控存在缺陷，导致未能及时上报查询时间 metric 和查询量（如果 RED 监控错了，那可能 USE 也有问题），导致他们没发现自己的 CoreDNS 处于崩溃边缘，加上"the client-side latency increase was offset by recent performance gains in our applications"，也是很无奈了。最终 CoreDNS 的查询事件从 1ms 增加到 780ms，然后大量的请求导致 OOM，进而导致上层其他应用出现故障。这个时候没有 node 级别的 localdns 么？感觉可以避免这个问题？

最终通过调整 CoreDNS 副本数和内存限制来恢复服务，直接将 CoreDNS 副本数从 3 增加到了 12，启用了 CoreDNS 的自动扩展，增加了相关监控。

最后，这篇故障报告写的不错，事情交代的非常清楚，值得学习。

---

[一次内存引起的网络丢包问题排查 | 卡瓦邦噶！](https://www.kawabangga.com/posts/7422)

想了想我们的系统如果遇到这个问题会发生什么，感觉应该可以避免：

- 系统产生报警 SEL Uncorrectable ECC，用户收到报警联系一线；
- 一线联系硬件厂商进行硬件故障确认；
- 硬件厂商确认后进行硬件更换；

另外想到了另一个之前被坑过的问题，有的 NUMA node 没有内存。

---

[Introducing Forge: the open source pipeline for generating SDKs, CLIs, docs, and more](https://blog.cloudflare.com/forge-open-source-generation-pipeline/)

> We've tried several hosted products that attempt to solve this, and relied on some in production. None of them solved this problem for us, and some have shut down entirely. One team would merge a change that inadvertently would break the generation pipeline, another team would discover this at release time, and we spent too much time swimming upstream through hosted tools we couldn't control, coordinating changes between teams and vendors.
>
> We'll have more on our SDKs very soon, including TypeScript, Rust, Python, Go, PHP, and Terraform. Especially Terraform.

2024 年 [[CloudFlare]] 使用 [[Stainless]] 来生成自己的 SDK，在 2026 年 5 月，[[Anthropic]] 收购了 [[Stainless]]，当时就在想 [[CloudFlare]] 要怎么办，现在看还是得自己搞。现在的状态看起来还很早期。

我自己前阵子使用 [lathe](https://github.com/lathe-cli/lathe) 来给内部的一个产品生成 CLI，配合 Agent 还挺好用的，比让 Agent 直接调用 OpenAPI 好用很多。如果 [[Forge]] 支持了 [[terraform]] 自动生成，可以考虑切换过去，在实现 HTTP Server 的时候需要考虑便于自动生成其他 SDK/IaC 的 API schema。感觉 Forge 自己需要提供一套规范才行。

---

[connect-go v2 is here](https://buf.build/blog/connect-go-v2)

> Our use of generics turned out to be more pain than it was worth.
> We were wrong. After four years of production use, we've found that most calls don't need those wrappers.

> In v1, returning an ordinary Go error from a handler sent its message to the client, potentially exposing sensitive details from a database error. In v2, only locally created `*connect.Error` values have their messages sent to clients.

看上去都是很务实的优化。

---

[Deno is joining Cloudflare | Cloudflare Blog](https://blog.cloudflare.com/deno-joins-cloudflare/)   
[Deno is joining Cloudflare | Deno](https://deno.com/blog/cloudflare)

> After that year we will end our development of the Deno runtime. Deno will remain open source, and we welcome others who want to continue its development.

[[Deno]] 团队加入 [[CloudFlare]]，Deno 项目一年后停止正式开发，保持开源。想到 3 月份有人问 [[Deno]] CEO 去哪里了，怎么一直不发声，同时可以看去年的这篇文章：[Reports of Deno's Demise Have Been Greatly Exaggerated | Deno](https://deno.com/blog/greatly-exaggerated)，里面提到了 [[Deno]] 的一些商业化路线，现在看应该都失败了，当时说想看看 [[Astral]] 也发表类似的声明，现在 [[Astral]] 加入了 [[OpenAI]]，[[Deno]] 加入了 [[CloudFlare]]，都结束了。

---

[DigitalOcean MicroVMs: Fast, isolated compute for your AI agent infrastructure | DigitalOcean](https://www.digitalocean.com/blog/microvms-public-preview)

[[Digital Ocean]] 的 MicroVM 产品，价格和常规的虚拟机一样，在计费粒度上是分钟粒度按需计费，在一些场景下会便宜些。功能上和 [[Fly.io]] 的 [[Sprites]] 看着一样？

---

### 生活

[第一个教师节随想](https://jia.je/misc/2026/09/10/first-teachers-day/)

> 我越来越觉得，以后计算机一定会像数学一样，成为所有人都该学会使用的专业或技能。其中比较重要的一点，就是 AI 的使用。这一定是所有人都可以、也一定要学会的，然后把它应用到自己的领域里去，不一定是计算机，什么领域都可以。这既是趋势，也是我们教育者要努力促成的事。

真好啊，有理想的教育工作者。

---

[放下助人情结，我又辞职了](https://blog.solazy.me/20260909/)

> 前几天开一个例会，对面又在用极其抽象的黑话包装一个完全没有经过验证的伪需求，会议开了两个小时，核心问题一个没碰，全是在论证「态度」和「站位」。散会之后，我看着团队里几个年轻人眼神呆滞地坐在工位上，那一瞬间我突然意识到一件极其残酷的事：我根本救不了任何人，我甚至连自己都在往里面搭。

> 团队里的每个人都是成年人。他们选择留在这个公司、选择忍受什么样的环境、选择在什么样的项目上投入时间，背后都有他们自己的考量和代价。有人需要这份薪水还房贷，有人还没想好下一步去哪，有人可能根本不在乎这件事情做得体不体面，只要按时打卡就行。

> 牺牲感是职场里最廉价也最危险的情绪，一旦你觉得自己是在「为了别人而忍耐」，你离怨妇就只有一步之遥。

用现在（流行？）的话说，已经到了都能理解的状态了，大家当下的选择，都有各自的原因，平时的抱怨左耳朵进右耳朵出就好，保护好自己的精神状态是最高优先级。

---

[提完离职之后](https://blog.solazy.me/20260911/)

> 很多人习惯用「能不能待下去」来衡量一份工作的去留，潜意识里觉得只有被边缘化或者干不下去的人才该走。这本质上还是在用一份工来向外界证明自己的能力。但我早就不需要一份工作来证明自己的价值了。   
> 相反，逻辑应该倒过来：一个能给组织带来绝对硬收益的人，需要时刻反向审视这个平台对自己到底还有没有价值。这个价值不是虚头巴脑的职场头衔，而是它能不能继续给我带来认知成长，或者匹配足够的绝对收益。当这两样东西我都感知不到的时候，待得再稳、再舒服，也没有继续耗着的必要。

---

[有花堪折直须折，莫待无花空折枝！——MOOC之死有感 - David Feng个人网站](https://davidfeng.us/zh-cn/2026-09-10-mooc/)

> Coursera/Udacity/edX 等几大公司宣传，把顶尖大学课程民主化，向全世界免费开放，真是乌托邦啊！但天下没有不散的筵席，这几家公司最终商业模式殊途同归，重点转到职业技能培训。遗憾！

这些公司的风口时间正好是念书的时候，当年多多少少看过一些公开课，可惜注定无法持续，感觉最终可能剩下的就是各个大学自己的网站了，考虑到大学的资金来源主要靠财政拨款，特朗普上台之后也砍了一批预算，不知道后面会不会有其他事件发生。

---

[CNX Markets · Chiang Mai market guide](https://markets.spdso.app/)

[[清迈]]集市地图，有营业时间，种类偏好，感觉用的上。

---

[致 Iris](https://letter2iris.me/)

> 你说过，你一直在尽力迁就我的情绪和需要，努力照顾我，维持我们之间的关系。你说你很痛苦、很疲惫。现在我终于明白，那是一种什么样的疲惫。最后的短短几周，我已经不堪重负，而你却坚持了几个月！

沟通的重要性，想什么要说出来，如果对方没有反馈，那结束也挺好的。

---

[我从 S 公司提桶跑路了](https://blog.19960312.xyz/blog/2026/09/24/I-have-resigned-from-S)

> 同事之间相处和谐友善，有问题互相讨论请教，大家也都乐于帮助，就算是互相观念不同发生争论，也没人会记仇针对你。特别是在出现比较紧急的售后的时候，半夜把同事打电话叫醒，大家也都是尽量创造条件去解决客户问题。同事们是真的把彼此当成最信任的伙伴，把自己融入团队内去共同承担责任，没有任何互相推诿指责的现象，也不存在谁资格老就倚老卖老，可以说这些员工（**并非每一个**）是 S 公司最珍贵的资源和良好工作体验的保障。

> 我没法和那些文艺青年一样，将 Gap Year 描绘成寻找人生答案的关键之路，也没有什么特别伟大的计划。其实我早就认识到了自己是一个很普通的接近于废物的人，我经历的一切大多来自于小聪明和命运的馈赠。我很清晰地知道，我的裸辞的鲁莽行为，付出的成本是不菲的：至少一年没有收入，职业生涯中断可能导致未来选择受限，甚至有可能再也无法回到软件开发行业。

> 但是，在思考了一切之后，我还是选择了执行这个计划，我想要一段属于自己的时间，我想要一段无所事事的时间，因为这些时间才是属于我自己的生命，而非作为一个大型机器的零件而存在。

---

### 书影播客

[《涨点脑子》](https://www.xiaoyuzhoufm.com/podcast/69b0e15796d585b34fa0ac2b)

主播是 DWZ，目的是让你在看到时政新闻时，能够知道这里背后的故事，前几期应该是真人录制的，后面大概率是 AI 生成的，内容质量上不错，最近跑步的时候常听。推荐以下几期：
- 1. 美国以色列为什么打伊朗
- 4. 中东为什么这么乱（上）
- 5. 中东为什么这么乱（下）
- 6. 犹太人怎么就把全世界都“得罪”了
- 8. 再聊犹太人，屠龙少年终变恶龙

如果对其中的宗教历史感兴趣，也推荐 B 站 UP 主青蛙刀圣的系列视频 [合集·[科普]西方宗教文化](https://space.bilibili.com/17588331/lists/524844?type=season)

[《基本无害-Ep211 宁波生存手册：宁波打的用户正坐滑翔伞去看集装箱》](https://www.douban.com/podcast_episode/536959)

种草了宁波的集装箱和炼化厂，确实震撼。

《孤独星球-越南、柬埔寨、老挝和泰国北部》，国庆假期去了越南，行程很早就定好了，国内飞机落地越南胡志明，主要在胡志明、岘港、河内溜达了一圈，最后从河内通过友谊关陆路回国。因为整体行程是朋友安排的，所以我全程没带脑子，也就不打算写游记了。上述几个城市，推荐的是岘港，很舒服的城市，沙滩很漂亮，适合放松的时候发呆。在越南期间，断断续续的在听《时雨集》的这期播客： 《美国吹哨人、第四权力和越战真相：五角大楼文件泄密始末》(https://www.xiaoyuzhoufm.com/episode/6a6afbe9b581962ce2bddf68)，帮我了解了越南（越南）的历史背景。


## 碎碎念

* International System of Units ，国际单位制的缩写是 SI，是来源于法语的：Système international d'unités 。
* AI 写了一段贼炫的 AWK，写的真好。
* 2026 年 9 月 9 日，两个同事在认真的讨论，智能马桶一点都不智能，延伸到痔疮生长在什么部位，asshole，什么是hole？进而学到了，0维洞是指空间不联通的隔离部分，比如篮球中的空洞，1维洞，指的是甜甜圈那种。
* tyty是 thankyou thankyou 的缩写；IIUC 是 if I understand correctly 的缩写。
* 全球穆斯林人口超过 20 亿
* 这周遇到了两个奇怪的硬件问题：鲲鹏的 2socket 48core 的 CPU 现成是 95 个，可能和 SMMU 有关；多台同样配置的 Intel 6306 ，其中一台 JVM 稳定 crash，RIP 指向了一条指令的中间位置，关 JIT 没问题，换主板后解决。
* 《七里香》MV 拍摄地点： Umino-juku and Takasaki City
* 把 2022 年部署的 rsshub 更新到了最新的上游。
* 最近高强度的使用 git worktree 之后，发现自己的用法好像还是有点麻烦，需要看看大家怎么用的。
* 宁波的简称：甬
* 在尝试优化 Agent 测试流程，发现哪怕 Agent 已经写的很清楚了自己做了什么，验证了什么，我还是很难信任。
* 越渴越吃盐
* 有阵子没关注 Talos 了，发现他们也开始做 VMware 替代了。。而且被 Yardi 收购了。
