---
title: Weekly Issue-《爱欲之死》
date: 2024-10-13
tags:
- Weekly
description:  
---


## 文章

### 技术

[Announcing the Stainless SDK generator](https://www.stainlessapi.com/blog/announcing-the-stainless-sdk-generator)

Stainless 公司提供通过 [[openapi]] 生成 SDK 的产品及服务，收费很贵，与之前的 [[fern]] 类似。目前的客户有 OpenAI、Cloudflare、Lithic。

作者 2017 年在 Stripe 负责 API 及 SDK 生成，当时评估市面上没有符合需求的工具，所以 Stripe 决定自己开发。在离开 Stripe 后的 2022 年，创立了 Stainless，同时 Lithic 成为了第一个客户，所以 Stainless 成立的第一天就是盈利的状态。

[Lessons from building an automated SDK pipeline](https://blog.cloudflare.com/lessons-from-building-an-automated-sdk-pipeline/)
[Automatically generating Cloudflare’s Terraform provider](https://blog.cloudflare.com/automatically-generating-cloudflares-terraform-provider/)

Cloudflare 将自己的 API 及 SDK 从手动维护转变为 Stainless 之后，带来的大量的改进，从之前的手动更新 schema、手动更新 SDK、手动更新 Terraform Provider，变成了手动更新 schema、自动更新 SDK、Terraform Provider。

在博客中写了很多经验，比如通过 [Redocly CLI](https://redocly.com/docs/cli) 来校验 OpenAPI，使用 [Comby · Structural code search and replace for \~every language.](https://comby.dev/) 或者 [Grit](https://about.grit.io/) 来做批量的代码改写。

---

[Scaling vCenter Server Connections for Improved Resiliency - VMware Cloud Foundation (VCF) Blog](https://blogs.vmware.com/cloud-foundation/2024/09/26/scaling-vcenter-server-connections-for-improved-resiliency/)

[[vcenter]] 在 `8.0u3` 版本针对请求连接进行了优化。vCenter 使用 Envoy 作为代理服务器，监听 443 和 80 请求，在 Envoy 做了连接数限制，但是存在一些问题：
- 按照连接类型分别限制了连接数，2048 个外部 HTTP 连接，2048 个外部 HTTPS 连接等等；
	- 如果所有 HTTPS 连接都在使用，但是有可用的 HTTP 连接，此时新的 HTTPS 请求会失败；
- 超过连接数限制时没有错误信息，只能通过 SSH 到 vCenter 中查看 envoy 日志
- 没有预警，当连接数接近上限时，没有告警
- idle timeout 非常长，8h

在 `8.0u3` 改进后：
- 将 HTTP 和 HTTPS 共享一个连接池，总数控制在 8000
- 逐步降低 idle timeout：当连接数达到限制的 50%时，开始减少 idle timeout，最开始为 8h，随着连接数的增多，idle timeout 开始降低，最低为 2s
- 当达到连接限制的 80%时，主动 draining，对于 `HTTP/2` 时发送一个 `GOAWAY` 信号，对于 `HTTP/1` 来说，设置一个 drain timer 来关闭最近较少使用的空闲连接
- 当达到连接限制的 99%时，envoy 停止接受新的请求并返回 503 ，并在 header 中携带 `x-envoy-local-overloaded` 便于让用户识别是连接数过多问题

---


[date - Why does man print "gimme gimme gimme" at 00:30? - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/405783/why-does-man-print-gimme-gimme-gimme-at-0030)

`man` 中的一个彩蛋，在 `00:30` 执行时会打印 `gimme gimme gimme`。可以使用 `man -w` 来避免。

印象中类似的彩蛋还有一些，应该有人汇总过？

---

[Advancing Our Chef Infrastructure - Slack Engineering](https://slack.engineering/advancing-our-chef-infrastructure/)

Slack 的 Chef 治理，2024 年看到公司没有使用 [[kubernetes]] 来进行基础设施管理，很难得了。

因为从来没用过 Chef，所以对于其中的一些痛点理解不深。

---


[Remove global-rate-limit feature by rikatz · Pull Request #11851 · kubernetes/ingress-nginx · GitHub](https://github.com/kubernetes/ingress-nginx/pull/11851)

Kubernetes Ingress-NGINX 移除了 global-rate-limit 功能。maintainer 提前在 Slack、周会、邮件列表等处发表了相关的说明，没有收到实质性的反馈，最终决定移除，但还是有些用户引发了不满，觉得项目移除了一个重要的功能。

maintainer 为了更好的维护项目，更好的迭代，Kubernetes Leader 要求社区及时的修复 CVE，并尽可能的减少 CVE 的可能，于是移除了，社区是欢迎贡献的。

---

[x.com](https://x.com/solomonstre/status/1842316197020443018)

为什么 [[docker]] 使用 [[Golang]] 编写？
- 编译后的 binary 不需要安装运行时
- 创始人是 Python/C 背景，Golang 均衡了两者
- 主流语法，没有小众或激进的概念，有助于建立大型的贡献者社区
- 直觉，觉得 Golang 很酷很新，想要使用它

---

[Leveraging Kubernetes virtual machines at Cloudflare with KubeVirt](https://blog.cloudflare.com/leveraging-kubernetes-virtual-machines-with-kubevirt/)

[[CloudFlare]] 内部是如何使用 [[KubeVirt]] 的，主要用于：Kubernetes 扩展性测试、开发环境、内核和 iPXE 测试、软件构建（Cloudflare 大部分软件构建都是在 KubeVirt 的虚拟机中完成的）。

目前 KubeVirt 的主要用户已经非常多了，ARM、Bytedance、Apple、EQUINIX、RedHat、SUSE 以及 Cloudflare。

---

[Use data that looks like data - by Thorsten Ball](https://registerspill.thorstenball.com/p/use-data-that-looks-like-data)

>When debugging or testing your program, do not use data that looks like a variable or type name.
>Do not use data that looks like a label or a column name or something your operating system has tons of.
>Do not use data that looks like it’s part of the program.

---

[AWS's Valkey Play: When a Fork Becomes a Price Cut - Last Week in AWS Blog](https://www.lastweekinaws.com/blog/aws-valkey-play-when-a-fork-becomes-a-price-cut/)

[[AWS]] 将基于 [[Valkey]] 的价格比基于 [[redis]] 的价格便宜，在 AWS 庞大的用户基数下，是否会导致用户更多的倾向于 Valkey，从而带动 Valkey 生态的发展？

---

[Open Source Pledge](https://opensourcepledge.com/)

开源承诺，参与的公司保证：每年给开源软件维护者支付费用，每年发布一个报告来简述费用支出细节。

目前一些公司有：
- Sentry
- HeroDevs
- Perfect
- Pydantic Logfire
- Astral
- ...

---

[System Initiative](https://www.systeminit.com/)

>System Initiative is an Intuitive, Powerful, and Collaborative replacement for Infrastructure as Code.

SystemInit 声称自己是 IaC 的替代品，在 Twitter 上引发了不少关注，花了些时间看相关的资料，发现自己到现在还不知道它到底是什么。

但是他们的收费非常的夸张，每个资源每个月 5 美元，这仅仅是 SystemInit 的价格，还不包括 AWS 资源自己的价格。

### 生活

[聊聊RSS这个“古董” - 乱槽之癫](https://blog.andie.im/talking-about-rss/)

[资本化信息分发 - Joshua](https://joshua.xlog.app/zi-ben-hua-xin-xi-fen-fa)

RSS 不受大公司欢迎完全可以理解。

---

[Tag: 马尔代夫 • Usubeni Fantasy](https://ssshooter.com/tag/%E9%A9%AC%E5%B0%94%E4%BB%A3%E5%A4%AB/)

[[马尔代夫]] [[游记]]，在 Maafushivaru 岛上度假加求婚，看着很浪漫很幸福。

---

[The best $4 ever spent](https://papanotes.com/the-best-4-ever-spent)

这几年最大的感受就是，把钱花在体验和经历上，比花在实际的物品上带来的感受要好的多。

---

[从北京的秋天到澳洲的春天-邂逅30岁的生日月](https://blog.sailfishc.com/Australia)

[[澳洲]] [[自驾游]]游记。

>有时候我也会将旅行和其他的东西比较，这次花了1W元就会想1W块钱能买一个Mac了，我想这个对比想法应该是很多人也会考虑的，今年我其实也去了很多地方

这里其实是很久之前我的心态，就是我会不自觉的换算，一次旅行的花费是否可以用来购买 XXX 了，但是很少这样想了，旅行中的体验是物品无法给予的。

> 凡是遥远的地方，对我们都有一种诱惑。不是诱惑于美丽，就是诱惑于传说。即使远方的风景并不尽如人意，我们也无需在乎。——汪国真《旅行》
> 旅行对我的意义是让我看到了当地人的生活方式，有了更加多元的视角来看待生活，有了一种原来还可以这样的感叹，看到一些美景和面对人的笑容的时候，就会有一种人间值得的心态。

---

[x.com](https://x.com/notengoprisa/status/1842550658102079556)

[[Google]] 搜索显示的所有“孔雀宝宝”都是 AI 生成的，但是这是 [[Google]] 的问题么？这不是，这是滥用 AI 的必然结果，有人推荐使用 [[Kagi]] 来代替 Google，但是我就觉得这是搜索引擎的工作模式导致的，AI 生成的内容是爆炸式的，人们越使用 AI 越相信 AI，就会有越来越多 AI 生成的内容，悲观的认为是无解的。

---


## 书影

《爱欲之死》，韩炳哲。

> 如今，爱被当成一种享受的形式被积极化了。首先，它必须制造出愉悦感受，不应有情节、有故事或者带有戏剧性，而应该是一种连续不断的感情和刺激。它必须免于受到伤害、攻击、打击等负面行为的影响。爱的消退本身已经是相当消极的事情了。但这些消极面其实是爱的本质的一部分:“爱不是一种可能性，它并不基于我们的努力和积极态度而存在，它可以没来由地打击我们，伤害我们。”然而，在这个被绩效和能力统治的社会，一切必须具备可能性、积极性和项目化的特点，无法接受爱所带来的伤害和磨难。

> 绩效原则已经统御了当今社会的所有生活领域，包括爱和性。正因如此，畅销小说《五十度灰(Shades ofGrey)里的女主人公才会惊讶于她的伴侣对于关系的要求如同“招聘广告，划定了固定的工作时间、清晰完整的任务设置和严苛明确的管理办法以确保工作绩效和质量”。绩效原则不能姑息无度、无节制，以及越界犯规所带来的负面性。因此.在他们签订的“协议”里，顺从的一方即“奴”,有义务满足相应的条件，比如规律的运动、健康的饮食和充足的睡眠。除了必要的水果之外，“奴”甚至被禁止在正餐之间进食。“奴”不得过量饮酒，不得抽烟，不得吸食毒品，也不能将自身置于任何不必要的危险中。甚至性生活也必须以身体的健康状况为前提,一切指向负面的行为都被禁止。那张长长的协议条款清单甚至包括了排泄物的使用，所有象征性或者实际上的污秽一并被排除在外。

> 女主人公肩负着“在任何时刻必须保持清洁，使用剃刀或蜜蜡清除体毛”的义务。小说中描述的 SM 操作方法是这种性关系的另一种反映。一切有懵越、违背意图的行为都被禁止被打上巴塔耶“性禁忌”的记号。参与 SM 的女性不得违背事先在协议中商定的“硬限制”，所谓的“安全词令”( Safewords)只是为了确保她不会遭受过度的、无节制的强求。对形容词“可口”一词的频繁使用也体现了一种强制的迎合意味，将所有行为转化为一种享受和消费模式。因此，《五十度灰》甚至使用了“可口的刑罚”一词。在“积极世界”中，只有可消费的事物被允许存在，疼痛也必须以被享受的方式存在。黑格尔所说的“痛苦”中包含的否定性或消极面是不存在的。

> 在列维纳斯看来，情欲是由欲成未成、欲来未来之物所滋养的。他者在全部感官的集合体中的缺席对于肉欲的张力和激烈程度至关重要。当今社会的“爱情”无非代表着需求、满足和享用，跟他者的存在与否并无关联。作为搜索和消费机器的当今社会，已经将所有与他者相适应的需求抹去，世界上不存在不能被发现、攫取和消费的事物。情欲被“脸孔”唤醒，这既提醒了他者的存在，同时又是对他者的否定。他使用的“脸孔”(Antlitz)一词与普通意义的“脸”( face)完全相反它是一种以色情意味被赤裸裸地展出的，完全可见可消费的商品。

> 伊娃·易洛思在《消费浪漫》(Konsum der Roman-tik ) 一书中指出，当今的爱情越来越“女性化”。小说常常使用“友好的”“亲密的”“安静的”“舒服的”“讨人喜欢的”“温柔的”等形容词来描述浪漫的爱情情节，而这些词汇都体现出浓浓的女性色彩。人们习惯将浪漫场景中的男性角色代人女性的感觉范畴中。20通过这个判断，她进一步得出结论:当今的爱情不仅是被“女性化”那么简单。随着所有生活领域出现的种积极化趋势，爱情也被驯化成一种消费模式，不存在风险，不考量胆识，杜绝疯癫和狂迷，避免产生任何消极和被否定的感觉。舒适的感觉和无须承担任何不良后果的刺激取代了痛苦和激情。

> 伊娃·易洛思在《 爱，为什么痛?》中将前现代时期的想象力称为“信息匮乏”。信息匮乏导致会“高估”他人，将他人的“价值看得过高”，甚至将其“理想化”。而今，由于数字通信技术发达，想象力被过量的信息所填充:“借由互联网传播而形成的先人为主的想象力，与信息匮乏而成的想象力不同。互联网想象以堆砌的碎片化符号为支撑，缺乏整体性在这种处境下，人们看似掌握了大量信息，却不易将事物理想化。”易洛思进一步假设，日益增长的选择自由带来了愿望的“理性化”。愿望不再是无意识的，而是受有意识的选择的支配。

## 碎碎念

* 爱情中的很多困扰，都和爱情本身无关
* 人生的目标是幸福和快乐，其它的只是实现这个目标的途径
* 罗斯退役了，麦格教授去世了，穆托姆博去世了。到了每年都会有熟知的人离开的年纪
* 在非洲大草原上，羚羊似乎从一出生就被贴上了“猎物”的标签。它们的一生仿佛注定是在死亡的边缘徘徊:吃草时要时刻提防猛兽，喝水时心里默默数着“被捕倒计时”，就连睡觉都得保持警觉。它们的命运就像一场永不停歇的逃亡。听上去荒谬可笑，难道羚羊活着的意义就是为了给狮子和猎豹填饱肚子吗?但大自然显然并不在意意义，生存规则简简单单:强者猎杀，弱者逃命，圈圈相生，毫无浪漫。

    反过来看我们人类，尽管摆脱了那些最直接的生存威胁，却似乎也无法真正超越"吃饱、繁衍、睡觉”这套最基础的生存逻辑。我们可以去旅行、打游戏、学哲学，仿佛生活变得充实了，但这只不过是“生存任务”上的一些额外装饰。面对现实的本质、我们只是找到更多“消遣工具”来打发这段生命进程。我们自豪于人类文明的伟大成就，却时不时怀疑:“这一切的意义究竟是什么?”

    也许深层次上，我们和羚羊并没有多大不同。羚羊的每一天是和死神赛跑，而我们呢?也许是和无聊、空虚、甚至虚无赛跑。羚羊被追捕的时候，它不会去思考“活着的意义”，而我们有了思考的能力，反倒让这个问题成了终生困扰。讽刺的是，或许我们在复杂化生命的时候，忘记了简单的道理:活着，不一定要有一个崇高的意义，只要活得自在，有时候就已经足够了。

    而人类的内心OS从“吃什么外卖”偶尔也转变为“生命的意义是什么?”

    于是我们明白，羚羊在大草原上飞奔，其实没有什么所谓的意义，只是在遵循自然规律。而我们或许也是一样，所有的努力、挣扎和追求，不过是为了在这片人生草原上奔跑得更远些，不至于太早跌倒在虚无的怀抱中。
* logseq 从 4 月到 10 月，都没有发布 Beta release，这也太夸张了，对于一个 2C 创业团队来说，这感觉像是事故了。。
* 为什么会有人想要攻击 Internet Archive 呢，这能有什么好处，Internet Archive 目前看完全是大善人。希望有些大厂能做这个大善人，AI 厂家大概率抓取了 Internet Archive 的信息的，如果他们能公开维护就好了。

