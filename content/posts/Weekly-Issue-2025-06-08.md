---
title: Weekly Issue-《强风吹拂》
date: 2025-06-08
tags:
- Weekly
description:
---


## 文章

### 技术

[Red Hat Ansible and HashiCorp Terraform Will Be Coming Together - The New Stack](https://thenewstack.io/red-hat-ansible-and-hashicorp-terraform-will-be-coming-together/)

[[Ansible]] 和 [[Terraform]] 要有更多生态上的集成， Terrible 要来了么？

---
[Start Sidecar First: How To Avoid Snags | Kubernetes](https://kubernetes.io/blog/2025/06/03/start-sidecar-first/)

在使用 `.spec.initContainers` 时，如何保证主程序在 sidecard 正常运行之后运行，可以考虑使用 `startupProbe` 或 `postStart`。

---
[操作系统技术是护城河吗？](https://manateelazycat.github.io/2025/06/05/ask-os/)

> 同事：那我们的护城河是什么？
> 我： 我们的护城河是真诚待人，服务用户。服务意识是唯一一个靠金钱没法去快速积累的竞争优势。因为服务需要靠人，每个人是否真心愿意服务别人，是装不出来的。

我现在不是很喜欢这种论调。

---
[AI Changes Everything | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2025/6/4/changes/)

> Right now it's messy and raw, but the path is clear: we are no longer just using machines, we are now working with them.

> I encourage you not meet that moment with cynicism or fear: meet it with curiosity, responsibility and the conviction that this future will be bright and worth embracing.

`working with them`。

---
[glibc vs. musl — Chainguard Academy](https://edu.chainguard.dev/chainguard/chainguard-images/about/images-compiled-programs/glibc-vs-musl/)

[[musl]] 和 [[glibc]] 的对比，主要为了解释为什么 [[Wolfi]] 使用 [[glibc]] 。[[Wolfi]] 在有些时候很有用，比如你想快速构建一个 container image，打包一些命令工具，但是其中一个命令是 glibc 的，此时直接将 [[alpine]] 替换为 [[Wolfi]] 即可，零成本。

---
[GitHub - hackclub/terminal-wakatime: Wakatime plugin for bash / zsh / fish shells!](https://github.com/hackclub/terminal-wakatime)

[[Wakatime]] 官方不推荐使用各种 terminal 的插件了，文档中已经将其删除了，推荐使用他们的 Desktop 版本，但是 Desktop 版本只追踪窗口级别的粒度，所以 terminal 中的操作都不会被追踪。这个项目通过 Shell Hook 来实现，依赖于 wakatime-cli。

---

[[硬件] 自部署服务推荐（持续更新）](https://changchen.me/blog/20250607/selfhost_app_recommendation/)

> Navidrome 作为一个 go 编写的服务端通过 web 访问，但它兼容所有的 [Subsonic/Airsonic 客户端](https://www.navidrome.org/docs/overview/#apps)！个人目前选择 substreamer 作为苹果客户端。

之前看到有人推荐过 [GitHub - swingmx/swingmusic: Swing Music is a beautiful, self-hosted music player for your local audio files. Like a cooler Spotify ... but bring your own music.](https://github.com/swingmx/swingmusic) 。

---
[Max Mitchell | I Read All Of Cloudflare's Claude-Generated Commits](https://www.maxemitchell.com/writings/i-read-all-of-cloudflares-claude-generated-commits/)

> Around the 40-commit mark, manual commits became frequent—styling, removing unused methods, the kind of housekeeping that coding models still struggle with. It's clear that AI generated >95% of the code, but human oversight was essential throughout.

[[CloudFlare]] 的 [GitHub - cloudflare/workers-oauth-provider: OAuth provider library for Cloudflare Workers](https://github.com/cloudflare/workers-oauth-provider) 是开源的 [[OAuth]] 2.1 实现，在 Git log 中记录了完整的 Prompt。虽然项目是 95% 自动生成的，但是还有一些不得不手动接入的情况。

---
[Why We’re Moving on From Nix](https://blog.railway.com/p/introducing-railpack#image-sizes-and-caching)

[GitHub - railwayapp/railpack: Zero-config application builder that automatically analyzes and turns your code into an image](https://github.com/railwayapp/railpack)

[[Railway]] 将自己的应用包管理器从 Nix-based 切换到了 Buildkit-based。切换的原因主要有：Nix 的版本管理机制导致在进行基础软件版本更新时，所有上层应用都要更新，有可能引入构建错误；Nix 引入会将 `/nix/store` 作为单一 Layer 引入，无法拆分，导致最终的构建 Image 体积较大；同时还有缓存问题，这里没有看懂，将 Deployment ID 注入到构建过程中，后续的 Layer 缓存失效不是预期的么？

他们改进的方式是自己实现了一套 Buildkit LLB + Frontend。之前有看过一些其他的实现方式，Buildkit 引入自定义的语法使用上是很方便的。同时他们使用 [[mise]] 来作为一些运行时的版本管理，不觉得这是一个好的方式，感觉这里会埋坑。

---


### 生活
[内网相亲帖观感 - 且听书吟](https://yufan.me/posts/blind-date-review)

> 思考当下女生对男生需要什么，思考这样的女生为何还是单身，思考如何让自己更加有竞争力（大雾）。

反过来也是一样，为什么还单身？

## 书影

《强风吹拂》，完整的看完了，相对于剧情的推动，更喜欢任务的旁白，在最终的比赛中，大家真的踏上了“顶点”，都在想些什么。每个人都想成为藏原走，都想有灰二的照顾和支持，都想想王子那样短短几个月就能完成蜕变，动漫终究是动漫，现实生活中可能永远也达不到 3 分配，喜欢 KING 的这段独白：
- 光明又快乐的大学生活
- 我只是因为有些期待，电视剧里描绘的那种生活
- 于是选择了那里
- 但是，现实很骨感
- 我的大学生活，没有半点出彩
- 马上就要这样碌碌无为地毕业了
- 要说哪里令人失望
- 那应该就是我自己了
- 我让自己失望了
- 肚量小，气性高
- 但又希望得到他人关怀
- 我讨厌这样的自己
- 表里不一，矛盾重重
- 不管去哪里，和谁在一起
- 好像就只有我是多余的
- 虽然我总是满脸堆笑，但却不曾对他人敞开心扉
- 努力不让他人看到自己的弱点
- 我就是 KING，别靠近我
- 总是这样，也不会有人想靠近了吧
- 但是，要是承认自己的寂寞，那就是输了
- 事到如今，也不可能改变自己了
- 没错，我谁也不是
- 谁不也是，但这才是真正的我

因为这个动漫了解到了箱根驿传，在 B 站上看到很多箱根驿传的视频，争取 2026 年去现场看看？ 好想知道 3 分配是什么感觉啊，一定飞快。箱根山岳险天下！



## 碎碎念

* 上半年的假期太集中了，距离下一个假期还有 4 个月。
* 感觉很多人把”搬家成本“想的太高了。
* EasyTier 真好用啊
* 知道自己想要什么可太难了
* 最近有一个明显的感觉，在 AI 之前产出能力超强的人，现在的产出能力更强了。
* 如果 ChatWise 的导出数据功能有限制的话，拿我估计要被迫付费了。
* 同事问我 List[str] 和 list[str] 有什么区别，这种充满了历史故事的问题真的很难回答。
* 突然发现，自己现在的“闭嘴”技能练的不错啊
* 进行了人生的第一次理赔，在材料齐全的情况下，还是很快的。
* 最近发现了一个还不错测试 Vibe Coding 的方法：收藏夹里一定躺着很多想要了解的项目，随机找一个，然后去 Issue 中找一个看着不难的问题，让 Copilot 修复，观察 Copilot 的修复过程，验证 Prompt 边界。
* Fedora copr 的官方指引确实不咋样，好在日志很详细。
* 麦当劳的 BGM 挺舒服的，不那么抖音
* 用 Fedora copr 构建了 EasyTier 的 x86 和 arm 的包，不知道为什么构建 x86 总是会下载 aarch64 的 source，只能使用一种比较丑陋的方式先绕过去了。
* Dagger 最近的一些信息都是集中在 AI Agent 方向了。
* 最近跑步的状态很不错。