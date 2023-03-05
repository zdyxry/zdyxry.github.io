---
title: Weekly Issue 2023-02-12
date: 2023-02-12 19:00:00
tags:
- Weekly
description: 周末还是应该多走走，上海去苏州真的是方便。
---


## 文章

### 技术

[Some random thoughts on Generative AI | Reorx’s Forge](https://reorx.com/makers-daily/002-thoughts-on-generative-ai/)

[[ChatGPT]] 大大降低了大家的使用门槛，只要你有想法，就可以快速POC。

---

[Cloud Backup Best Practices for SMBs](https://www.digitalocean.com/blog/cloud-backup-best-practices-startups-smbs)

云应用的[[备份]]实践，借机推广[[Snapshooter]]。

---


[设计师如何入门前端](https://dott.love/writing/design-engineering)

> 最后我想说，无论是设计工具还是[[前端]]代码，都只是实现创意的工具。最终能够限制创意的，只有不够开放和好奇的大脑。

---

[Kubernetes 证书管理系列（一） | MoeLove](https://moelove.info/2022/12/07/Kubernetes-%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E7%B3%BB%E5%88%97%E4%B8%80/)

[[证书]]管理是个非常麻烦的事情，[[openssl]] 的命令行也是用过的命令工具里面比较难用的几个之一了。

---

[Cloud Backup Best Practices for SMBs](https://www.digitalocean.com/blog/cloud-backup-best-practices-startups-smbs)

云应用的[[备份]]实践，借机推广[[Snapshooter]]。

---

[Supabase Clippy: ChatGPT for Supabase Docs](https://supabase.com/blog/chatgpt-supabase-docs)

[[Supabase]] 在文档网站提供[[ChatGPT]] 功能，来辅助用户搜索。如何构建：将完整文档拆分为多份，使用 [[OpenAI]] API 将其作为输入，使用[[pgvector]] 存储到[[Postgres]] 中，获取用户问题，在[[Postgres]] 中获取问题相关的文档，讲这些文档作为[[GPT-3]] 上下文，返回给用户。

---

[Bad Observability - SquaredUp](https://squaredup.com/blog/slight-reliability/bad-observability/)

关于可观测需要避开的点：

> Forgetting the customer;
Environment inconsistency;
Not understanding your ecosystem;
No consistent trace ID;
The big dumb metric;
Bad sampling intervals;
Misunderstanding metrics;
Lazy synthetic transactions;
A plague of dashboards;
Unnecessary alerts;
Hoarding data;
Disconnected data;
Throwing tools at a problem;
Mandating tools;
The chosen few;

---

[Dockerized Redis performance on CentOS 7.5 | ThreatMark | Anti Fraud](https://www.threatmark.com/dockerized-redis-performance-on-centos-7-5-2/)

[[Seccomp]] 对 [[redis]] benchmark 的影响。

---

[Profiling 101 - XX’s Blog](https://xxchan.github.io/cs/2023/02/08/profiling-101.html)

[[Profiling]]  101。 对于如何在[[Python]] 环境中进行有效的性能排查一直没有掌握。

---

[Everybody is More Complex Than They Seem | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2023/2/9/everybody-is-complex/)

> The most important lesson for me was loving myself and the path I'm on, and how utterly destructive it can be to myself to not be in balance about my true goals and desires.

---

[天工开物 #5 我的 Linux 开发机](https://mp.weixin.qq.com/s/ERggKUosAYIkAKN0DEmKhw)

[[Linux]][[开发机]] 配置，选择的发行版是 [[Garuda]]。 感觉目前因为[[企业微信]][[微信]][[腾讯会议]] 等等类似的软件，一台 PC 的情况下还是没办法只使用 [[Linux]]。打算等我的 PC 到了之后尝试一下 [[WSL2]]，看看现状如何。文中提到的云服务器比较贵的事情，最近发现如果只是实验性质的工作，可以考虑[[竞价实例]]，价格很友好。

---

[下一次工业革命近在眼前了](https://xargin.com/winter-is-coming/)

最近关于 [[AI]] 的讨论热度太高了，感觉跟之前的[[元宇宙]] 不同，后者是虚无缥缈的，前者现在是实实在在有可以让你感到震撼的能力了。

---

[The Law of Stretched [Cognitive] Systems](https://ferd.ca/the-law-of-stretched-cognitive-systems.html)

有些悲观，但也是现实？

> Every system is stretched to operate at its capacity ; as soon as there is some improvement, for example in the form of new technology, it will be exploited to achieve a new intensity and tempo of activity.

---

[Enterprise Restaurant Compute. by the CFA Enterprise Restaurant… | by Brian Chambers | chick-fil-atech | Jan, 2023 | Medium](https://medium.com/chick-fil-atech/enterprise-restaurant-compute-f5e2fd63d20f)

[[Edge Computing]] 具体场景处理。

### 生活

[为什么在当下要谨慎做出买房决策？ – 基地文稿站](https://b.brave2049.com/wei-shen-me-zai-dang-xia-yao-jin-shen-zuo-chu-mai-fang-jue/)

[[房子]] 是[[资产]]还是[[负债]] ？

---

[年度扯淡 2022 - 知乎](https://zhuanlan.zhihu.com/p/595625553)

老板的年终总结。

---

[What Won't Change](https://matt-rickard.com/what-wont-changed)

未来 10 年什么会发生改变？什么不会？

---

[思考生活与生命在英语中的区别 | Reorx’s Forge](https://reorx.com/essays/2023/02/life-vs-life-in-english/)

由一句话的翻译引发的思考。
> 关于“掌控时间”的说法，可能你想强调的是时间管理或自律这个概念吧，单说字面翻译 DeepL 更好一些，master 更接近 manipulate 的含义。二是“生活”如果是指物质层面，英语一般习惯用 ^^standard of living^^ 描述，精神层面 ^^quality (质量) of life^^ 用得多。
再就是“生命价值”这个概念，中文里可以说价值多还是少，而英文里 life value 更偏重价值观，对应的是忠诚、正义这样的词，所以这个翻译不是很恰当。然而 value of life 也不行，这个词是形容一条命值多少钱的。我觉得 ^^self actualization^^ 更符合这个语境。
最后就是两个细节，回到汉语的思维模式，“使我的生活变得更好”显然没有“改善我的生活”更地道，英语也是一样的，像 improve/enhance 这些词自带改变的含义。还有中文的“不仅/还”是隐含的递进关系，强调后面的部分，字面对应的 not only 在关系强调上要若一些。

---



## 书影

《足利女童连续失踪事件》，刚开始看，作者面对社会上的“既定事实”还可以去进行质疑，佩服。

《魔翡翠》，经典老片。