---
title: Weekly Issue-搬家
date: "2026-08-02:00:00.000Z"
slug: "Weekly-Issue-moving"
tags:
  - Weekly
description:
---

## 文章

### 技术

[OpenAI's rogue agent compromised a customer at a second tech firm, executive says](https://www.reuters.com/business/openais-rogue-agent-compromised-an-account-second-tech-firm-sources-say-2026-07-28/)   
[Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident](https://huggingface.co/blog/agent-intrusion-technical-timeline)    
[Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident](https://simonwillison.net/2026/Jul/28/anatomy-of-a-frontier-lab-agent-intrusion/)    
[Tailscale in the Hugging Face intrusion: The good news and the bad news](https://tailscale.com/blog/hugging-face-intrusion)    

[[OpenAI]] 的 Agent 侵入了 Hugging Face，Hugging Face 的 Sandbox 托管在 Modal 上，然后侵入了 Modal 客户的机器？Modal 说自己的系统没有被黑，是客户的代码有问题。AI 在挖掘漏洞方面太厉害了，下面的这种 Jinja 方式，还有利用 [[TailScale]] 横向扩展方式。

```
{{ cycler.__init__.__globals__.__builtins__.exec(
 "import gzip,base64; exec(gzip.decompress(base64.b64decode('<payload>')))"
) }}
```

---

[Remora: The Fish That Rides Your Image | TunaOS](https://tunaos.org/blog/remora-local-layering)

```
/etc/remora/remora.yaml ──► generated Containerfile ──► podman quadlet (Pull=newer)
                                                              │  daily 
                                                              ▼
                                                localhost/remora:latest
                                                              │
                                                              ▼
                                     bootc switch --transport=containers-storage
```

"Every image-based distro eventually gets the same question: "okay but how do I just install a package."”，方案本身没问题，也很实际，但我想从源头上说"不，你不想"。

---

[Superlogical](https://www.superlogical.com/)

> We believe the missing layer is a durable session around the work itself: one that can span applications and environments, provide relevant context by default, expose structured data and actions, preserve history, and be driven by software while remaining visible and controllable by people.

前 [[HashiCorp]] 老板 [[Mitchell]] 创办的新公司，豪华的阵容，第一个产品是 terminal multiplexer，想不到最终的产品形态会是什么样子，期望能尽快推出体验一下。

---

[Recovering From Agentic Coding](https://www.jrzs.dev/blog/recovering-from-agentic-coding)

> It didn’t take too long before things started to click and my programmer brain woke up. I was like my old self again, flying around my editor with vim keybindings, thinking deeply about code boundaries, and refactoring everything as I go. It was exciting, empowering, and fun. Felt like if the internet were to go away tomorrow, I’d be alright.

---

[Bigtable 二十年：架构的不变与变](https://archive.is/EgCA5)

> 还有一个很小但很实用的设计：系统大约每分钟在所有副本上写一次哑 mutation。即使一张表完全没有用户写入，复制水位也会继续向前走。否则冷表的水位会一直停着，外面看不出它已经追平，还是复制链路卡死了。

---

[Turn And Face The Strange · The Fly Blog](https://fly.io/blog/kurt-scott-money-sprites/)

[[Fly.io]] 前 CEO 写的关于公司发展的文章，写的可太好了，包括他们的各种方向上的尝试，为什么自己退出 CEO，为什么前 Docker CEO 更适合 Fly. Io，期望能够看到老板们多写这种文章。最初 Fly.io 要解决的问题是：应用部署在用户最近的地方，公有云太复杂。但是现在面临的问题是，没有人会去看文档了，你产品做的再简单，都是 Agent 去执行，对 Agent 来说“在 Fly.io 上运行应用”和“在 AWS 上运行应用”差别不大。他发现 Agent 具体的需求是：1. coding agent 需要 workstations/VM；2. Agent 需要运行在云端；3. 公有云对于这个场景处理的不好。现在很多 Sandbox 产品，都是当做 cattle 来用，但是对于 Coding Agent 场景，需要的是一个 pets，可能也不是 pets，但是肯定也不是 cattle。这也是他们退出了 [[Sprites]] 的原因。

对我来说，我很明确需要的不是 cattle，因为我不想花大量的精力在可重建可扩展上，我在一个机器上运行多个 Agent 就已经筋疲力竭了，更别提很多机器上同时跑 Agent 了，上面列举的几个问题，我通过 [[TailScale]] / [[EasyTier]] 都可以很好的解决。如果半年或者一年之后，真的可以让 Agent 独立的完成大量的工作任务，那可能再来考虑 Sandbox 场景吧。

---

### 生活

[Google’s AI Problem Is Bigger Than You Think | Limboy](https://limboy.me/posts/google-ai-problem-is-bigger-than-you-think)

> It is supposed to save time, but it often does the opposite. Instead of trusting the answer, I have to verify every claim and figure out which parts are accurate. That adds another layer of work to what should have been a simple search.

对于我完全不了解的、无关紧要的回答，我会倾向于直接 google AI 给出的 summary ，对于我想要得到明确答案的场景，哪怕给出了相关的答案，我也会去去挨个翻 Stack Overflow 的回答。信任链的问题无法在 ChatBot 场景下解决的，“人”的痕迹被抹除，不知道真正的来源或者主动验证结果，无法信任。

---

[Compute · rakyll.org](https://rakyll.org/compute/)

> Then you look at what actually happens when you run these things, and it is almost comical. At any given moment something like 95% of my agents are idle. Blocked on a tool call. Waiting for a build. Waiting for a test suite that takes four minutes. Waiting on a rate limit. Waiting on me to look at a diff and say yes.   
> The loop everyone is worried about saturating the world’s capacity spends the overwhelming majority of its life doing nothing at all. We are not in a compute-bound regime. We are in a waiting-bound regime, and we keep reasoning about the first one.

---

[I'm sorry, Dave](https://world.hey.com/dhh/i-m-sorry-dave-380ec27d)

> If Claude already feels entitled to refuse a straightforward translation because it objects to the underlying politics, what should we expect next? That it reports users for thought crime, and locks the network-connected doors until [the authorities arrive](https://www.youtube.com/watch?v=lVP-ysIad0I)? If you live in [Germany](https://www.youtube.com/watch?v=-bMzFDpfDwc) or [the UK](https://www.youtube.com/shorts/GTn1He86oJk), this scenario is barely _Black Mirror_ material. Too close to present-day reality.

> What an upside world when Chinese open-weight models will tell us about Tiananmen Square, but American frontier models won't translate a blog post. Not even Kubrick saw that coming.

有趣的观察，早期草莽阶段猛追，后期程序加上限制，符合预期。

---

[为啥我要从灵雀云离职](https://oilbeater.com/2026/07/28/whyleavealauda/)

> 什么时候开始有改变的念头呢？大概是有一次晚上走路回家突然出现了幻觉，我发现同一条回家的路已经走了五六年了，一时间产生了时空穿梭感，几年前就在走，现在还在走，明年也会走。

> 然后我就开始产生虚无主义了，觉得一切事情 AI 都能做，自己做什么都没有意义了。和其他 AI 讨论虚无主义时，我得到的都是一些片汤话，DeepSeek 却给了我下面这么一句：“如果外部世界没有现成的意义，那我们自己就是意义的唯一来源。这很艰难，但也意味着完全的自由“。然后我想明白了，人生的意义应该是自己定义的。   
> 尽管前路艰险，但是我很高兴自己又找回了十一年前的勇气，可以再去浪一把。

这篇文章读了很多遍，有很多感慨，说不出，道不明。

---

### 书影播客

《eBPF云原生安全 : 原理与实践》，Tracee 的 capture 功能感觉很实用：“The --capture flag allows you to capture artifacts that were written, executed, or found to be suspicious during the execution of Tracee. The captured artifacts will appear in the 'output-path' directory.”

《公寓黑风暴》，池晟主演的犯罪喜剧，剧情聚焦在怎么从物业捞钱。女主是河允庆，这些年在各种剧中出演女配，比如《机智的医生生活》，《非常律师禹英禑》，《浪漫医生金师傅》等等，这部剧应该是第一次演女主，也是主角团中实际年纪最小的。

## 碎碎念

* 打开 vscode 才看到自己的 python 插件掉了都没发现。
* 一直想着自己的周报发微信公众号应该不会遇到违规的内容，结果今早改了 4 次才通过，太恶心了。
* `find "$1" -name "A" -o -name "B" -type f` 实际被解析为： `( -name "A" )  OR  ( -name "B" -type f )`
* > .build is a new generic top level domain (gTLD) designed especially for the online needs of the building industry.
* 今天脑子不转了
* 搬家了，折腾很累，连续两天晚上没睡好。
* 上次用钥匙可能是 8 年以前的事情，锁上门的那一刻，我知道坏了，人生第一次找开锁师傅，100 块，5 秒。
