---
title: Weekly Issue-Garmin教练
date: "2025-07-13T00:00:00.000Z"
slug: "Weekly-Issue-Garmin教练"
tags:
  - Weekly
description:
---

## 文章

### 技术

[The AWS Survival Guide for 2025: A Field Manual for the Brave and the Bankrupt - Last Week in AWS Blog](https://www.lastweekinaws.com/blog/the-aws-survival-guide-for-2025-a-field-manual-for-the-brave-and-the-bankrupt/)

> Congratulations! You’re now ready to embark on your AWS journey. Remember, every expert was once a beginner who wondered why their [“simple” WordPress site](https://bsky.app/profile/quinnypig.com/post/3lqfctagyue2y) costs $3,000 a month to run.

想到了我司的 Slogan 是 `make IT simple`，可是产品复杂度上去之后，最终暴露出去的概念一点也不少，在最终用户看来可能既不 simple 也不 easy。

---
[Victorialogs vs Loki - Benchmarking Results](https://www.truefoundry.com/blog/victorialogs-vs-loki)

>  TL;DR of the Numbers
> - **70–94 % faster** across common search patterns.
> - **≈40 % smaller** on disk with the same retention window.
> - **Half the compute**, freeing a full vCPU and ~1–2 GiB RAM on our smallest nodes.

如果现在让我选择监控组件，我会选择 VM 全家桶。

---

[Why 'if not list' is 2x Faster Than len() in Python](https://blog.codingconfessions.com/p/python-performance-why-if-not-list)

很久之前还记得这种 [[python]] tips，现在已经忘光了。

---

[It doesn't make sense to wrap modern data in a 1979 format, introducing .ptar | Plakar - Effortless backup](https://www.plakar.io/posts/2025-06-27/it-doesnt-make-sense-to-wrap-modern-data-in-a-1979-format-introducing-.ptar/)

[[Plakar]] 推出的 `.ptar` 格式，目标是用来替代 `.tar`。在备份场景下，貌似想要享受完整的好处，需要配合他们的备份引擎 Kloset 一起用才行。

原来 `tar` 的全拼是 `Tape Archive`。

---

[Guest Post: How I Scanned all of GitHub’s “Oops Commits” for Leaked Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/guest-post-how-i-scanned-all-of-github-s-oops-commits-for-leaked-secrets)

这篇文章很好，前阵子刚好和同事聊到了这个方式，即使 `git reset && git push` 清理包含了敏感信息的 commit，还是有办法通过 [[Github]] 获取到历史提交。如果要彻底清理的话，只能联系 [[Github]] 发 DMCA 了。

---



### 生活

[知乎的理想国：当知识乌托邦遇上流量现实](https://yinfeng.blog/Zhihu-Idealism)

> 日报的成功，不只是流量产品，更完成了从社区到内容品牌的跃迁。很多人第一次接触知乎，是通过日报的微信推送、豆瓣广播，甚至网易云阅读。
> 在它的黄金年代（2013–2016），知乎日报几乎是中文互联网 “内容审美” 的标杆。我几乎一篇不落全看了，有几篇回答也被选入知乎日报。

> Slack 的更换不是一件小事。在知乎内部，它象征着早期工程师文化：扁平、开放、自由讨论；而企业微信，则代表着流程、权限、管理。这场替换引发了很多老员工的强烈反抗，你没看错，是反抗。Slack 全员大群里，一度爆发激烈讨论。
> 有老员工发帖说：“Slack 是我们最后的精神角落。”

经历过知乎的 2012-2016，刚好和大学时期重合是一件很幸运的事情，让当时的我看到了讨论和思考的维护多样性，影响很大。

---

### 书影

《二战新史 : 鲜血与废墟中的世界》，读着读着发现我借的是上册，下册被其他人借走了，失策，失册。

《分布式数据库 TiDB：原理、优化与架构设计》，周末在上图的新书书架上发现的，把第一部分看完了，有点像之前的一些博客文章的合集。（话说第一次看到书籍的第一页是一个 Grafana 截图的，意义不明。。。


### Garmin 教练

刚刚结束了一个为期 17 周的 Garmin教练训练计划，训练目标是完成 10km，从结果来看是很早就完成了（训练目标设定的不太合理），5km 的配速从最开始的7m30s 到现在的 6m，提升明显。 

Garmin 将 17 周分成了几个阶段：
* 基础训练：基础期通过提高有氧适应能力和增加训练量为接下来的训练奠定基础。
* 进展期：增长肌肉质量和体积阶段会增加锻炼的强度，以提高您的有氧能力。
* 峰值：巅峰期包括注重速度的训练，并进一步增加训练强度。
* 减量期：减量期会减少训练量，但保持训练强度，以帮助您保持状态。

17 周的时间里，中间有两周出去旅游没有训练，其他大部分时间都在严格的按照规划训练，一共跑步 86 次，平均每周跑步在 5-6 次，周末会进行一次长距离 12-15km。训练类型大部分都是基础训练，穿插着有长距离跑和乳酸阈值训练。训练契合分数一致不太高，基础训练还好，但是偶尔配合间歇训练的时候，要求5 分配跑 6min，就跑不下来，只能尽力而为了。Garmin 的训练记录中，会记录很多信息，比如步频、垂直振幅之类的，最开始的时候我还尝试关注一下，后面发现关注也没啥用，还不如先跑起来再说。事实证明也是有效的，当 17 周结束之后，找到了自己舒服的节奏，这些数据看上去也好看不少。

Garmin 对训练内容的调整，是会严格和前一晚的睡眠状态关联的，如果前一晚的睡眠质量很差（睡眠时长过短、深度睡眠时长过短、静息心率过高），都会触发 Garmin 的自动调整，会降低训练强度，最高的一次好像直接从乳酸阈值训练调整为了恢复训练。

接下来又开始了一个为期 17 周的训练，这次训练目标是半马，期待训练结果。


## 碎碎念

* 我妈说我的房间太埋汰了，可是我自我感觉还不错。
* 某种程度上，开发友好很重要，感觉甚至比 CI 都要优先级更高些。
* 真牛啊，感觉有些公司的业务模式上限不高还能持续招人，一定是我哪里理解不到位。
* 一些人在用 AI 进行各种创造，一些人拿着 command not found 来找 Oncall。
* aespa 的 Dirty Work 不好听。
* 什么是号外？编号之外的产物。
* 六分半配速跑 7 公里，佳明认为是基础训练，得提升强度了
