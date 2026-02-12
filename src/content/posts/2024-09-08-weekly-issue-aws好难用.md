---
title: Weekly Issue-AWS好难用
date: "2024-09-08T00:00:00.000Z"
slug: "Weekly-Issue-AWS好难用"
tags:
  - Weekly
description:
---

## 文章

### 技术

[谈谈最近玩 AI 的体悟](https://www.bmms.me/blog/recent-insights-on-ai-exploration)

>AI 时代会越来越放大个人的软性技能，尤其是定义和描述问题的能力。那种老黄牛式的勤奋会越来越容易被淘汰。

---

[Why don't more people use Linux?](https://world.hey.com/dhh/why-don-t-more-people-use-linux-33b75f53)

>Besides, if you're able to figure out how to setup a modern build pipeline for JavaScript or even correctly configure IAM for AWS, you already have all the stamina you need for the Linux journey. Think about giving it another try. Not because it is easy, but because it is worth it.

不经意间黑了下前端构建和 AWS 的 IAM（也不是黑，就是陈述事实）

---

[Exploring Cloud Native projects in CNCF Sandbox. Part 1: 13 arrivals of 2023 H1 – Palark | Blog](https://blog.palark.com/cncf-sandbox-2023-h1/)

[[CNCF]] 2023 年上半年新加入 Sandbox 的项目，没看到想要立即试用的。

更想知道哪些 Sandbox 项目已经死了（不活跃了），然后被踢出去的。

---

[Greppability is an underrated code metric](https://morizbuesing.com/blog/greppability-code-metric/)

```
const getTableName = (addressType: 'shipping' | 'billing') => {
    return `${addressType}_addresses`
}

const getTableName = (addressType: 'shipping' | 'billing') => {
    if (addressType === 'shipping') {
        return 'shipping_addresses'
    }
    if (addressType === 'billing') {
        return 'billing_addresses'
    }
    throw new TypeError('addressType must be billing or shipping')
}

```

代码是否可快速搜索到想要的内容，是一个很关键的指标，后者比前者在可搜索上更好。

---

[PoC Is Not Production Ready: Ensuring Your Service Is Truly Ready for Production](https://reliabilityengineering.substack.com/p/poc-is-not-production-ready-ensuring)

PoC 到生产可用，至少要做到如下几点：
- 文档记录，每个任务、变更和实施都要被记录
- 尽可能的使用 [[IaC]] 或 Config as Code ，来保证可扩展、可重复的执行
- 知识转移，在完成该工作的基本背景和操作知识必须与至少一名团队成员共享，可以采用 demo 或视频录制的方式

---

[vmware-explore-2024-session-urls/vmware-explore-us.md at master · lamw/vmware-explore-2024-session-urls · GitHub](https://github.com/lamw/vmware-explore-2024-session-urls/blob/master/vmware-explore-us.md)

[[vmware]] Explore 2024 相关资料。看了 `Tech Deep Dive: Automating VMware ESXi Installation at Scale`，通过 PXE 配合 Kickstart 大规模安装，在安装部署模式上没看到太多改变，随着 ESXi 的更新，Kickstart 的一些配置方式发生了变化。

---

[Why vSAN Max aka disaggregated storage? | Yellow Bricks](https://www.yellow-bricks.com/2024/09/06/why-vsan-max-aka-disaggregated-storage/)

2023 年这个时候，[[vmware]] 推出了 vSAN MAX，是一个分离式的存储产品，最初的定位是“用于 PB 级别的存储平台“，现在这个解释发生了一些变化，是作者之前没想到过的，与技术无关，与运营和政治有关。

在传统环境中，根据规模的不同，通常会看到职责分离。有虚拟化管理员、网络管理员和存储管理员。在过去的十年中，VMware 一直期望的是能够培养 ful-stack 工程师，但是没什么效果，很多公司还存在这样的职责，而且 20 年之后可能还会存在。

在 HCI 场景下，通常虚拟化管理员也会承担存储职责，但是使用 vSAN MAX，就可以仍然保持不同团队管理不同资源。这现在是 vSAN 的一个很好的用户场景。

之前我司对外推出独立的存储产品，我了解到的说法是：灵活，存算分离，可以适配更多的虚拟化平台，用户接入成本低。没有考虑到“人”这个因素，有趣。

---

[Your Database Skills Are Not 'Good to Have'](https://renegadeotter.com/2023/11/12/your-database-skills-are-not-good-to-have.html)

使用 Database 作为例子来说明应该更多的关注自己代码的完整流程，如果遇到业务感知的慢，那就一点点的排查为什么慢，而不是说直接加一个其他的中间缓存来尝试解决这个慢。另外说了 ORM 可能会造成太过于方便的写业务，会做很多“自动”的事，导致让编写代码的人觉得查询是没有成本的。

不只是 Database，大部分说“慢”的场景下，问“为什么慢”都很难得到明确的答复。

---

[Writing Helpful Error Messages  |  Technical Writing  |  Google for Developers](https://developers.google.com/tech-writing/error-messages)

如何让错误提示更友好：
- 给出具体原因
- 如果是输入信息无效，给出具体的判断依据
- 在解释原因后，给出如何解决问题
- 简洁用语
- 避免双重否定
- 保持术语一致性

---


### 生活

（居然一篇值得记录的都没有。。


## 书影

《躁动的无意识》，读完了，有些缥缈，有些虚无，这种虚无与读韩炳哲的书还不太一样，是真正的虚幻，如果无法接受身心灵的理论，可能根本读不下去。最后的落点是冥想、正念。豆瓣上现在的书评感觉有些假。

《花儿与少年·丝路季》，好看，非常好看，我很久没看到这么好看的综艺了，是那种很舒服，可以当电子榨菜的类型，周末甘愿当一个沙发土豆，在床上反复的看。其中的处事方式，很多值得学习，在看的时候换位思考，如果自己是 ta，自己能做到现在的样子么，大概率不能，需要极高的情商才可以。北方人含量过高，甚至东北人含量过高。


## 碎碎念

* 发现 dnsmasq 居然没有其他替代品，同时支持 DNS/DHCP/TFTP/PXE ，居然没有人用 Rust 重写它。
* 如何避免会议又臭又长呢？
* 为什么大部分公有云厂商不支持从 ISO 创建实例呢？AWS/Azure/GCP/DO 不支持，Vultr 支持。这是出于什么考虑呢？
