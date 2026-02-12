---
title: Weekly Issue-《史密斯夫妇》
date: "2025-11-02T00:00:00.000Z"
slug: "Weekly-Issue-史密斯夫妇"
tags:
  - Weekly
description:
---

## 文章

### 技术

[AI driving data center - and storage - transformation – Blocks and Files](https://blocksandfiles.com/2025/10/27/ai-driving-data-centre-and-storage-transformation/)

> Most enterprise-type organizations won’t build their own AI factories. Instead “they will consume application programming interfaces and software built on top by firms such as OpenAI, Anthropic PBC, other AI labs and cloud players.” Silicon Angle suggests “enterprise AI will be adopted through access to mega AI factories via APIs and connectors with a software layer that hides underlying primitives and tools complexity that live under the hood.”

大多数公司最终不会自建 AI 基础设施，但是他们可能会积极的采用 AI 功能，这些 API 需要一个统一的组件来管理，[[Kong]] 这类 API Gateway 的产品需求量和重要性是大大增加的么。

---

[CVE-2025-62725: From “docker compose ps” to System Compromise | Imperva](https://www.imperva.com/blog/cve-2025-62725-from-docker-compose-ps-to-system-compromise/)

[[docker]] compose 在处理 OCI artifacts 时，没有针对 `compose.file` 进行校验，导致攻击者会获得任意路径的些权限。`v2.40.2` 引入了 `validatePathInBase` 修复这个问题：

```go
// validatePathInBase ensures a file path is contained within the base directory,
// as OCI artifacts resources must all live within the same folder.
func validatePathInBase(base, unsafePath string) error {
	// Reject paths with path separators regardless of OS
	if strings.ContainsAny(unsafePath, "\\/") {
		return fmt.Errorf("invalid OCI artifact")
	}

	// Join the base with the untrusted path
	targetPath := filepath.Join(base, unsafePath)

	// Get the directory of the target path
	targetDir := filepath.Dir(targetPath)

	// Clean both paths to resolve any .. or . components
	cleanBase := filepath.Clean(base)
	cleanTargetDir := filepath.Clean(targetDir)

	// Check if the target directory is the same as base directory
	if cleanTargetDir != cleanBase {
		return fmt.Errorf("invalid OCI artifact")
	}

	return nil
}
```

我日常用到的 compose 还都是自己拷贝修改的，还没用过 `docker compose -f oci://docker.io/username/my-compose-app:latest up` ，看着就不放心。

---


[AWS to Bare Metal Two Years Later: Answering Your Toughest Questions About Leaving AWS](https://oneuptime.com/blog/post/2025-10-29-aws-to-bare-metal-two-years-later/view)

> Ran the MicroK 8 s + Ceph stack in production for 730+ days with 99.993% measured availability.

介绍了过去的两年内 [[OneUptime]] 从 [[AWS]] 迁移走之后的成果，回答了一些社区问题，从当前的现状来看，这个选择没有任何问题，无论从成本、还是长期维护的角度。

> **Automation:** We're now moving to Talos. We PXE boot with Tinkerbell, image with Talos, manage configs through Flux and Terraform, and run conformance suites before each Kubernetes upgrade. All of those tools also hardened our AWS estate, so they were not net-new effort.

文章中多次提到他们会从当前的 [[MicroK8s]] 切换到 [[Talos]]，以至于我以为是一篇软文。[[hacker news]] 上面的一个评论，能够感受到他的痛苦：
> Talos is great until it's not. We ran into Ceph IO speed bottlenecks and found it was impossible to debug ("talosctl cgroups —preset=io" is a mess) because the devs didn't want to add an SSH escape hatch into their black box OS. Our Talos nodes would also randomly become unhealthy and you have no way of knowing why. 
> Switched to PXE booted Alpine linux with vanille k8s, and we had a much more stable experience with no surprises, and the ability to SSH whenever we want has been hugely helpful.


---

[Fluid Storage: Forkable, Ephemeral, and Durable Infrastructure for the Age of Agents | Tiger Data](https://www.tigerdata.com/blog/fluid-storage-forkable-ephemeral-durable-infrastructure-age-of-agents)

[[TigerData]] 为自己的业务设计的分布式块存储，他们当前的业务是在 AWS EBS 上， EBS 存在一些问题，且这些问题在 Agents 场景下更加突出，Agents 经常需要创建一个临时环境进行工作，工作完成后又自动清理：
- 并不弹性，很多操作有 6-24 h 冷却期，冷却期内无法执行其他操作，无法缩容（文章中提到了 xfs 和 ext 4, 但 xfs 不能缩容，ext 4 也不能在线缩容吧？）
- 按照分配空间收费，用户通常需要超额分配来防止空间不足；
- 操作缓慢，数据从 [[S3]] 中加载耗时较长

于是他们实现了 Fluid Storage，目标是解决上述问题：A forkable storage layer offers a more general foundation: volumes that can be cloned, branched, or scaled independently of the systems that use them (and not limited to Postgres databases)。主要组件有 DBS (Distributed Key-Value Block Store), Storage Proxy 和 User-space Storage Device Driver。

有人在 [[hacker news]] 上问为啥不用 [[Ceph]]，得到的回复是：There's some secret sauce there I don't know if I'm allowed to talk about yet。 

---



### 生活


[2025年末如何借助AI查询疾病相关知识 | 创造力溢出](https://quaily.com/goldengrape/p/how-to-use-ai-to-learn-about-diseases-by-end-of-2025)

> 首先，不要用 DeepSeek

作者推荐的模型是：千问>=智谱 >> 豆包。提示词：
> `请为我综述【疾病名称】。请仅仅采信权威证据，例如教科书、pubmed文献。关于治疗建议应当依据循证医学证据强度进行分级。`
> `根据这个报告和报告中的参考文献，请用通俗易懂的语言，为我讲解什么是【多焦点/扩展景深IOL】，有哪些优点哪些缺点？`

这里是一个反向的过程，通常大家需要和疾病打交道，都是已经有了明显症状，此时根据症状去推测疾病不建议用 AI 来做，很可能自己把自己吓死，如果知道了疾病再来查询如何治疗，就好很多了。

---

[Sabbaticals keep our attrition at bay](https://world.hey.com/dhh/sabbaticals-keep-our-attrition-at-bay-9ccba5c0)

> Bottom line is that we all need a long break every now and then. Not just two weeks on Mallorca, but time enough to get bored. To get hungry for the intellectual stimulation of work and the social connection of colleagues. The sabbatical is a great way to deliver that and keep founders from wanting to sell and employees from wanting to quit.

[[37Signals]] 所有员工每 3 年有 6 周的带薪休假，他们觉得这样的长假是可以让头脑 reset（重置？），因为当一个员工觉得 Burnout 想要发生改变的时候，通常只能选择辞职，他们觉得单纯的从人才留存的角度就很有说服力：看着自己培养的人离开代价太高。

---

[重生之我在新加坡开餐馆 - 外卖](https://www.douban.com/note/876892151/?_i=1691843teD_jlF,1832195teD_jlF)

> 因为本质上，不管再早一些 OTA 平台也好，还是外卖，亦或是打车，其实都是一类互联网业务，我个人总结就是「重资产，重运营，赢者通吃」。

>重资产，重运营，这两点就导致了，一旦在这类业务市场上取得优势，基本等同于垄断。

>东南亚小美团 + 滴滴 **Grab** ，先说结论，没有 Joker fee 的平台，同样 GMV 的前提下，比如 500，到手大概是 250 不到，实际抽成率在 55% 左右，但明显感觉得到还算有得赚。

---

[Kaze.run-Yan's Blog](https://blog.mockee.com/kaze-is-up/)

听播客知道的一个跑步工具，搜着关键词找到了作者的博客。Kaze 可以连接 [[Strava]] 数据，并可以通过创建自定义机器人来完善活动信息（标题、描述），便于记录和分享。作者的博客整体配色也很舒服。

---

[Tips for stroke-surviving software engineers - by James Padolsey](https://blog.j11y.io/2025-10-29_stroke_tips_for_engineers/)

作者给[[中风]]工程师的一些生活和工作建议，希望我永远也用不上。中风之后可能会导致注意力障碍，里面提到了一些工作方式的调整，原因是顶叶皮层在信息转换与重组时负荷很高，如果频繁的切换任务会加重认知负担，严重可能会诱发癫痫。
- 及时休息
- 减少不必要的干扰
- 健康优先
- 善用法律支持

---


[My impressions of the MacBook Pro M4 - Michael Stapelberg](https://michael.stapelberg.ch/posts/2025-10-31-macbook-pro-m4-impressions/)

>  so, in retrospect, I could have stayed with the M 1 for a few more years. Oh well.

原来只有 MacBook Pro 才有  nano-textured display ，Air 是没有的，可以显著的减少反光。对我来说 M1 当前还没有什么问题，已经很够用了，只是随着使用年限难免面临电池老化的问题。

---

[[读后感]《孩子：挑战｜Children: The Challenge》](https://changchen.me/blog/20250926/children_the_challenge/)

> 传统文化中，孩子应该安静地待在一旁，而不发表过多意见或打扰成年人的活动。然而时代在发展，==“民主”==的概念融入生活的每一角，上面的传统观念也早已过时。孩子对环境的变化更为敏感，逐渐意识到人人平等并开始挑战大人的 “权威”。传统养育方式失效后（you-do-as-I-say），家长找不到新的教育方法，最终导致了当前的困境。

> 对于宠坏的孩子，大人似乎竭尽全力给予关注哄她开心（encourage），实则无意间过度保护（overprotection），discourage 她独立自给自足照顾好自己的能力，例如孩子想哭就让她哭，可以给她提供玩具，然后让她自己去处理问题。因为真正的幸福不是依赖于别人的关注，而是源于自我满足的结果。

> 家长对孩子的爱，实际上是自爱（self-love）：表面上是为了孩子好，实则是在满足自己的情感需求，反而摧毁了孩子面对和解决问题的能力。


> **少管闲事**：母亲应该管好自己的事，不要试图控制一切。她有权利坚持自己的信念，不打孩子，但她没有权利告诉丈夫如何对待他（这是他们父子的事情）。越是控制越是说明对孩子的能力不自信。


---



### 书影播客

《天生就会跑》，细想发现自己在跑步这件事上投入的精力不算少，很多事情也会给它让步，打算找几本跑步的书看看，这本刚开始看。

《史密斯夫妇》，印象中第一次看应该是初中的时候，在一个同学（和这个同学也没有联系了，上一次知道他的近况是在北京的一家建筑公司里做设计）家里看的 DVD，这周又看了一次，还是觉得很精彩，至少可以让人看下去。2005 年的电影，那时候的皮特和朱莉可太年轻了，朱莉的眼神可太美了，导演给了好多次特写，剧情是很扯淡的，但是连贯性很好，为啥 2025 年我看不到这样的电影了呢，我打开《偷天盗日》看了 20min 就关掉了，不明所以。

《基本无害-Ep178 35 岁成为了国家二级运动员 —— 地球 online 和人生复利》，四舍五入也是毛冬回顾自己的前半生了。关于如何做决定，做决定所需要的努力，在组织中获得的安全感与离开之后的收获，找到自己热爱的事并让它可以为自己带来一定的收入，支撑自己继续投入。

《没理想编辑部-Vol.198 你不需要所有人的喜欢》。去成为一根尖刺，但也去成为一场拥抱。



## 碎碎念

* Amp 的广告质量还是可以的，也不是什么都推，广告位置选择的也真不错，我几乎看了每一条广告。。。
* 2025 年了，怎么还会有“移动没有入驻小区”这种事情。
* 今年看病花了 1800 了，第一次达到起付线。
* 如果有一个牛奶，上次喝过它之后坏肚子了，经过对照比较，确认喝其他牛奶没有问题。下次见到它，还会尝试么？我不会。
* 差点以为马上要交付的一个功能有问题，今天心跳最高的时候就是刚刚。
* 11 月 31 日是一个完美周五，还是万圣节，可惜上海没有什么活动。
* 在内部文档中，看到了“根据 AI 的结论”字样，感觉药丸。
* 目前来看，体重是跑步能力提升的很大的阻碍。
* Folo 更新了 1.0 版本，免费用户订阅数量上限是 150，印象中和 Inoreader 好像差不多，没有作为主力工具使用是正确的，还是 Miniflux 适合我。
* Heynote 如果能够支持 Image 就好了，纯文字在工作的时候还是不太方便。看了下社区的 Issue 讨论，对于当前的架构设计影响比较大，应该没有短期内实现的可能。
