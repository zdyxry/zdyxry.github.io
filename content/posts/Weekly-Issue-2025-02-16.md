---
title: Weekly Issue-《花样年华》
date: 2025-02-16
tags:
- Weekly
description:  
---


## 文章

### 技术

[用 AI 写了一个属于自己的 AI Deep Search。](https://xiaowenz.com/blog/2025/02/deep-research-dev-by-python/)

代码仓库地址： [GitHub - iamshaynez/deep-research-cli](https://github.com/iamshaynez/deep-research-cli.git)，所有的 Prompt 第一句是定义对方的角色，定义好返回的格式。第一次在 Prompt 见到“温柔”这个词，有趣。

原来有 [[Tavily]] 这种专门提供 LLM Search 功能 API 的平台，不过确实不便宜。

---

[The Exit Interview: JP Phillips · The Fly Blog](https://fly.io/blog/the-exit-interview-jp/)

> GraphQL slows everyone down, and everything.

> It’s too easy to lose sight of whether your current focus [in what you’re building] is valuable to the company.

> We struggle a lot with consistent communication. We change direction a little too often. It got to a point where I didn’t see a point in devoting time and effort into projects, because I’d not be able to show enough value quick enough.

貌似比较少看到这样公开的离职访谈。

---

[From PDFs to Insights: Structured Outputs from PDFs with Gemini 2.0](https://www.philschmid.de/gemini-pdf-to-data)

使用 Gemini 从 [[PDF]] 中提取结构化数据的文章，使用 [[Pydantic]] BaseModel 定义结构。看上去效果很不错。

---

[We Were Wrong About GPUs](https://fly.io/blog/wrong-about-gpu/)

> The biggest problem: developers don’t want GPUs. They don’t even want AI/ML models. They want LLMs.

Flyio 关于 GPU 产品策略的反思，他们最初认为用户“可能”需要 GPU 来运行 AI/ML 模型，并进行了硬件和软件方面的投入，最终觉得用户可能需要的是更上层的能力。如果我是 Flyio 的用户，我可能会倾向于使用现有的 API，而不是想要 GPU。同理，我司的产品如果面向最终用户，提供 GPU 当然好，但是直接提供 LLMs API 可能是更多用户想要的？友商的策略就很不错。

我时常在想，现在做 Infra 的公司，如果不去蹭 DeepSeek 的热度，是不是就落后了，当我看到友商在春节期间还在发 PR，看到春节后各种爷商股价飞涨，这个热度应该蹭的。

---

[Debugging Our New Linux Kernel](https://dasl.cc/2025/01/01/debugging-our-new-linux-kernel/)

作者将 Apache 服务器从 CentOS 切换到 Ubuntu 后，发现了较多的 Listen Overflows，最初怀疑是网络问题（是的，网络永远是第一个被怀疑的），后面发现了对应异常时间点 CPU 使用率很高，使用 perf 抓取到是 `inode_switch_wbs_work_fn` ，通过 bpftrace 来抓取具体的 switch 变更细节，与 cgroup 有关。在定位过程中，二分到与 Apache 的配置服务有关，是一个 Systemd 的 OneShot Service，如果在该 OneShot service 中增加 sleep 3600，那么对应的 CPU 异常时间也会推迟 3600s，最终定位与 cgroup `v2`  的 `io` 和 `memory` 控制器有关。通过临时禁用 Controller 解决。

---


[On Bloat - Rob Pike](https://docs.google.com/presentation/d/e/2PACX-1vSmIbSwh1_DXKEMU5YKgYpt5_b4yfOfpfEOKS5_cvtLdiHsX6zt-gNeisamRuCtDtCb2SbTafTI8V47/pub?slide=id.p)

硬件速度越来越快，软件速度越来越慢。关于引入依赖的部分，“Do not add dependency on a component without being aware of all the indirect dependencies you are also adding to your project and what they do”，这也太难了，感觉完全不可实施啊。

[Open Source Insights](https://deps.dev/) 可以来检查软件包的依赖情况，包含了安全分析、依赖、被依赖，还有具体的打分（好像不是所有的项目都有分数）。

---



### 生活

[Europeans don't have or understand free speech](https://world.hey.com/dhh/europeans-don-t-have-or-understand-free-speech-c7c406e8)

> It's quite like how every dictator around the world pretends to believe in democracy

---

https://x.com/DashHuang/status/1889154012085358990

> 理论上从现在开始，公司里不应该有任何人的工作和AI无关。无论工作内容是否由AI产出，至少工作结果要由AI来检查一轮，指出错误，给出建议。  
> 高情商说法，每个人都是老板，有无数AI听你指挥为你干活。  
> 残酷点说法，每个人也是AI的下属，员工被老板用AI监督工作，老板被股东和政府用AI来监督赚钱和交税  

---

## 书影

《猪猡之王》，韩剧，男主小时候被校园霸凌，长大后复仇的故事，有些吓人，有些压抑。为什么被称男版黑暗荣耀，但是观看的感受完全不同呢，可能是因为结局，也可能是因为男主的选择。

《花样年华》，王家卫作品，主演是张曼玉、梁朝伟。这个电影在大学的时候看过一次，对剧情提不起兴趣，看一半睡着了。这次重映再看，很喜欢。

为什么喜欢，电影本身的故事很简单，如果是用短视频来解说，可能 1 分钟都不用就能结束了：男主的老婆和女主的老公发生了婚外情，男主与女主的故事。这能叫”救赎“么？感觉不合适。两个人如果在一起，是因为互相拯救么？是因为爱情么？还是对自己另一半的报复？

电影中的男女主关系隐晦，女主来借报纸，男主说我还有小说，下一个镜头是还小说。一借一还，就有了下一次见面。两个人模拟自己的另一半进行约会，互相点对方喜欢的食物，是想搞清楚自己的另一半为什么会出轨，还是搞清楚桌子对面当前的这个人喜欢什么？

王家卫呈现出来的非常克制，克制到需要全靠想象来填充空白，可能喜欢的是王家卫本身吧。





## 碎碎念

* 最近做俯卧撑姿势有问题，右手手腕很难受
* 发现偶尔调整一下房间布局，也不错
* 听 Twitter Space 中一个推友讲述自己和朋友在日本旅行的故事，感觉大家对于“朋友”的定义和接受程度差别很大。
* TencentOS 怎么能垃圾成这个样子呢，草台班子，比 openEuler 差远了。而且能够感受到一点 openEuler 20.03 为了方便用户从 CentOS7 迁移过去的努力。
* case 系统的 AI 推荐好不容易准确一次，结果还被一线直接忽略了。AI 信任感真是一个大问题。如果是了解的东西，那看一眼没什么成本，很快就能辨别啊，如果是不了解的东西，更容易产生信任才对，那看看推荐也没啥，为啥直接忽略了结果呢。
* 好像很久没有 Oncall 到 2 点了，可能最近2 年都没有过了。身体明显吃不消。而且睡醒之后，连常规的日常流程都忘记了，自己却完全没有意识到。
* > 上海海拔最高的地方并不是大家广为熟知的佘山，而是位于坐落在上海最南端的杭州湾口以北、偏居一隅、海拔103.7 米的大金山岛，它是上海市最高和最大的基岩岛。
* “中华民族伟大复兴”，突然发现，即使日常中到处都能看到，也从来没有理解这句话。可能口号从来不需要被理解。
* 吐槽几个服务日志少，吐槽了几年，老板也不安排人加一下日志，每次 debug 都傻眼，全靠复现。


