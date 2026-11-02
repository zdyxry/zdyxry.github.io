---
title: Weekly Issue-《何以为战》
date: "2026-11-01:00:00.000Z"
slug: "Weekly-Issue-Why-War"
tags:
  - Weekly
description:
---

## 文章

### 技术

[GitHub - tinkerbell/captain: In-memory Operating System Installation Environment for Executing Tinkerbell Workflows based on systemd](https://github.com/tinkerbell/captain)

[[Tinkerbell]] 的又一个**下一代**安装执行环境，之所以说又，是因为上一个 Hook 也是下一代，从执行环境的角度，他们已经迭代了 3 次了，每次选择的路线可以说是完全不同，我理解这里的一个重要原因是 Tinkerbell 的架构设计上决定了每一个安装动作都是一个 container run 的动作，所以早期一定需要 docker daemon。

最初是：[osie](https://github.com/tinkerbell/osie)，采用的是 [[Alpine]]，通过自定义 init，在启动的时候读取 kernel 参数决定自己要执行的动作，启动 OpenRC，OpenRC 去启动 Docker daemon、SSHD、安装服务等。这个阶段面临的问题在 Hook 中有提到：他们会去修改 kernel、无法让用户更好的去定制 OSIE、CI/CD 平均要 1h、构建流程复杂且分散。

他们开启了：[hook](https://github.com/tinkerbell/hook)，与 OSIE 不同，这是一个基于 [[LinuxKit]] 的安装执行环境（好像是我第一个在生产环境中使用 LinuxKit 的项目），最直接的一个好处就是构建标准化，且构建速度极快，并且默认已经带了 containerd，系统启动通过自定义 init，启动 containerd，运行服务，服务是通过 container 来运行，除了基础服务外还会启动 tinkerbell 自己需要的服务，比如 DinD，因为前面提到他们一定需要 docker daemon，所以这里会比较绕，启动 DinD 之后，还要把 docker socket 挂载到 HostOS 上，然后另一个 containerd 下的容器再挂载 docker socket 来启动真正的 tink worker，执行后续的动作。

接下来就是现在的 captain 了，这次他们的技术选择终于是现在比较大众的了：[mkosi](https://github.com/systemd/mkosi)，基于 systemd 的 Debian 系统，带来的好处有：initramfs 很小、干掉了 DinD（我觉得 Hook 也完全可以做）、熟悉的 systemd 生态、架构简单。这里另一个考虑我猜可能是 LinuxKit 现在已经没什么维护和迭代了，上一次 release 已经是一年前了，从生态上和 systemd 差距太大。

---

[Inside Prometheus: Meta's Journey to a Gigawatt-Scale Supercluster](https://engineering.fb.com/2026/10/19/data-center-engineering/inside-prometheus-meta-gigawatt-scale-supercluster/)

> The larger scale-up domain is what gives NVL72 its bandwidth advantage, but it also makes the 72-GPU rack the [unit of allocation we plan capacity around](https://openreview.net/pdf?id=18jPgte2tM). Training parallelism maps most efficiently onto power-of-two group sizes, so each NVL72 domain runs a 64-GPU slice and keeps its remaining eight GPUs as in-rack spares. When a GPU fails, a spare takes its place immediately, so the job restarts from its last checkpoint instead of waiting on hardware repair, and the rack stays in the job.

> During the initial phase of Prometheus in mid-2025, our interruption rates reached a peak of nearly 1,000 events per 8K GPUs daily. Through a year of rigorous cross-functional engineering, we have achieved a 99% reduction in interruptions, enabling the cluster to sustain multiple training jobs of tens of thousands of GPUs in parallel.

---

[Pour One Out for the Leap Second](https://www.wired.com/story/leap-second-is-abolished-bipm-says/)

> In other words, not our problem, and good luck to future generations!

相信后人的智慧，闰小时这么麻烦的事情，就交给后人来考虑吧。

---

### 生活

[Hunger beats tenure: Advice for junior engineers](https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/)

> In a world where execution is expensive, you normally have to grind your way to some social status before the entire organization would "take a bet" on your idea.

---

[云风的 BLOG: QWERTY 键盘布局的发展历史](https://blog.codingnow.com/2026/10/qwerty.html)

> 为什么不需要数字 1 和 0？因为可以用 I 和 O 代替：这两个字母和数字看起来差不多，放在句子里也不会被误解。

> 由于在 1870 年，经常需要输入 1870 或 1871 组合，而 I 又被当作 1 用，所以就安排在了 8 的下方，和 O（当 0 使用）排在一起。

这个故事真有趣。

---

### 书影播客

《特立独行》，爆米花喜剧，因为张国强的片段去看的电影，结果发现最出彩的也就是那几个片段了。

《一个部门的诞生》，香港电影，讲述的是一个男青年因为电视台套餐退订问题，去营业厅办理期间发生了一些误打误撞的故事，他成为了劫匪，劫持人质的主要目的是退订套餐。剧情中规中矩，结局没想到。香港客服的沟通方式确实很古老，每次和他们打客服电话，都感觉得作为一件正式的事情去准备，沐浴更衣，全身贯注听提示，还要在电话里输入很多信息，非常的麻烦。

《何以为战-现代西方战争的文化逻辑》，尝试从利益之外的角度来解读战争，三个字总结就是“讲故事”，讲让人相信的故事，无论故事的背景是通过控制媒体还是通过军事力量，有人相信自己的故事就好， 哪怕故事是虚假的。如果自己讲不来故事，那么你就有可能被故事所裹挟而不得不做一些事情。故事可能是平凡叙事、悲剧、传奇（英雄主义）、末日。书中选了苏伊士运河、海湾战争、伊拉克战争作为例子，讲述在不同的战争中，大国的选择以及战争的结局。


部分摘要：

> 为何我们会因为同一手牌在战争辩论的文化政治中被反复打出而产生似曾相识的感觉；为何某些战争看起来疑窦重重，其他战争又似乎大致正当；英雄如何被制造，惩罚又如何被施予。文化不只是战争的一部分，更是战争的关键。

> 历史学者的时间定位总是在诉诸清晰可辨的利益与整齐一致的因果的时候解释的“光滑线条”中经过“折射”。但在有生命的历史的知识论与存在论空间中决定国家政策立场的，并不是利益，而是关于何为利益，该怎么处理利益的感知。这些感知不被客观现实以任何简单的、无条件的方式决定，而由依赖时间所给出线索的公民话语和体裁结构塑造。

> 在这里，战争必须有目共睹地针对那些名为“邪恶”的目标，它的烈度必须与它所应对的威胁相称，推动它的必须是有高尚理念的冷静头脑。军事技术和职业技能似乎有助于满足这样的要求，同时把它对主流体裁政体的附带伤害控制在最低限度。受损的二元对立也通过“失误”概念而得到修补。

> 无论布什和他的支持者是否相信他先前关于萨达姆的言论，这都不是重点，我们只需要理解：言论是述行性的，行动者也要对自己的修辞负责。布什的民意调查支持率出现了骤降。由于担心唤起“败坏” 的评价，他（布什）不得不令人震惊的闭口不谈他任职四年以来的至高荣耀：集结一支多国联军，执行一套出色的作战计划，以及解放科威特。



## 碎碎念

* 爸妈从家里给我寄了一堆的吃的，感觉能吃个半年。
* 三周没喝咖啡了
* 发现看视频听歌还是不行，会丢很多细节，比如 NEON 的 2m10s 之后。另外习惯的力量太强了，现在一首3m29s 的歌都觉得长了。
* 威哥果然升处长了，还去中农大讲课了。
* 韩国孝道：抢任英雄演唱会门票。
* 家里跳闸，PVE 起不来了。
* 有时候也摸不清规律，有些事情国产模型没什么底线，有些事情反而国外模型没什么底线。感觉和国内的电影审查机制似得，血腥场景国内来者不拒，黄色场景国内是一点不能沾，国外正相反。
* 走到地铁站发现忘带饭了，回家取
* 看到 Foursquare 要关闭了，想到有一阵子 LBS 这种基于位置社交的软件很火热，后面不知道怎么就消失了。
* Mute 了一个 channel，因为同事一直用 AI 发消息。
* 终于在 2026 年，把项目中的 poetry 替换为了 uv。
* 耐克，Nike，源自古希腊神话中的胜利女神“尼刻”(Nike)，另一个胜利女神，罗马神话中的维多利亚。
* 大学同学邀请去北京参加他的答谢宴，确实让我纠结了好几天要不要去。