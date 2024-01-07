---
title: Weekly Issue 2024-01-07
date: 2024-01-07
tags:
- Weekly
description:  
---


## 文章

### 技术

[为什么在容器外修改了文件后容器内的文件没有同步更新？——一次 Docker 文件挂载和 Bind mount 的探索](https://nova.moe/compose-file-mount/)

Bind Mount 特性：

>If you are using some editor like vim, when you save the file it does not save the file directly, rather it creates a new file and copies it into place. This breaks the bind-mount, which is based on inode. Since saving the file effectively changes the inode, changes will not propagate into the container. When the container is restarted the new inode. If you edit the file in place you should see changes propagate.

This is a known limitation of file-mounts and is not fixable.

---

[What is an eTLD + 1?](https://jfhr.me/what-is-an-etld-+-1/)

>The eTLD consists of **the last n parts of a domain that are shared between multiple sites from different owners**.

eTLD 有很多owner，而 eTLD+1 可以确定唯一的owner。

---

[Fake Trees: Using Indents For Simpler UIs - ratfactor](https://ratfactor.com/cards/fake-trees)

很多时候我们真的需要一个tree 么？可能不是，可能只是需要一个类似tree 的样式来展示，实际上在实现的时候可以采用一写简单的方式，比如 indent，sort ，甚至是 find 命令。

---
[SSD controller, object and block cloud storage predictions – Blocks and Files](https://blocksandfiles.com/2024/01/02/ssd-controller-object-and-block-cloud-storage-predictions/)

预测：云计算成本、数据安全、AI 相关业务、私有部署。

---

[Fastest Way to Read Excel in Python | Haki Benita](https://hakibenita.com/fast-excel-python#results-summary)

[[python]] 处理 Excel 方式对比，Calamine 最快，但是只读不能写，pandas/Tablib 相对慢一些，但是支持多种格式。感觉之后如果简单的数据分析需求，还是应该考虑 [[DuckDB]]。

---

[X 上的 Jake Ward：“We pulled off an SEO heist that stole 3.6M total traffic from a competitor. We got 489,509 traffic in October alone. Here's how we did it: https://t.co/sTJ7xbRjrT” / X](https://twitter.com/jakezward/status/1728032634037567509)

作者窃取了竞争对手的 3.6M 的流量，10 月份就获得了 49w 次的点击。操作方式是：
- 导出竞争对手的 sitemap
	- 如何找到想要窃取的网站？
		- 使用 Ahrefs/Semrush
		- 在 Google 上手动搜索
	- 查看他们的 sitemap
		- website.com/sitemap.xml
		- 找到其中具有描述性的结果（去除 ID 类 URL）
	- 导出 sitemap
		- 将 XML 转换为 CSV
- 将他们的 URL 列表变为文章标题
	- 使用 Byword ，从 URL 抓取，并根据 URL 生成文章标题和大纲
- 使用 AI 根据这些标题大规模的创建 1800 篇文章
	- 将上述信息继续生成完整的文章，并发布到自己的网站上

这套流程在国内的各种内容农场已经应用的很熟练了，相信国外应该也有不少，但是为什么他还是要写这个推，并获得了很大的流量(724.1万浏览）呢？因为他要推广自己的 AI 应用 Byword，嗯，就是如此的真实，但有效。

内容农场稍有不同，内容农场几乎可以一眼看出，那些内容是垃圾，但是 AI 生成的东西，辨别的成本变高了。

---

[关于 Azure OpenAI 费用的一次争议-Laisky's Blog](https://blog.laisky.com/p/azure-billing/?lang=zh)

[[Azure]] 费用计算出现 Bug 导致多扣钱，反复交涉得到退回（如果是我可能交涉几次就放弃了吧。。）

---

[How to Harden Server SSH Access Using Advanced OpenSSH Features | Vultr Docs](https://docs.vultr.com/how-to-harden-server-ssh-access-using-advanced-openssh-features)

[[openssh]] 常用的安全配置，其中限制 SSH key 登录执行命令的方式学到了：

> `command="ls" ecdsa-sha2-nistp521 AAAAE2VjZ.....KEY-BODY...Lf+FNXv00Pd+A== user@user's-PC`
> When the user starts an SSH session with this key, the command `ls` executes, and the session ends if the command runs successfully

---



### 生活

[扫兴的东亚父母，还不完债的孩子-虎嗅网](https://m.huxiu.com/article/1949158.html)

>有人总结了中国诡异的亲子关系：和父母分享快乐，快乐就会消失；向父母倾诉烦恼，烦恼就会加倍。  
>子女是父母持有的资产和物品，所以“削骨还父，割肉还母”放在任何时代都具备振聋发聩的悲壮。  
>对东亚人而言，快乐是腐蚀意志力的毒药，是享乐的邪恶魔鬼，蜜罐是贬义的，而苦水才是正道的光。  
>在这片情感匮乏的土地上，人们从未习得爱意究竟是什么。  

---

[twitter.com/kistovincent/status/1741994881806172508](https://twitter.com/kistovincent/status/1741994881806172508)

>那就是工程师们正在以一个让人悚然的速度，践行着“良禽择木而栖”的古训。对于任何一个社会，拥有特定技能和相对较高的文化水平的工程师，毫无疑问是最核心的税基和生产力（还没算上他们往往能孕育更多高水平的下一代）。如此大规模的税基流失，比房价这样的表象数据，恐怖得多。

这个观点值得思考。

---


[纸飞机 - 2023回忆录 | Miableem](https://miableem.com/blog/2023year-in-review)

看生活化的年终总结，让人感受到生活的乐趣，不至于被数字填满。

---




## 书影

《父权制与资本主义》，是那种我从来没有过的思考问题的层次，需要反复阅读多次。如果之前没看过女性主义相关书籍，不建议讲这本书作为第一本，如果一定要选择这个方式，那么直接读《第二性》也许更好。

《长安的荔枝》，这本书有很多解读，最多的应该就是：只要你让老板满意，其他人的想法不重要。也有一些说法是：入职场官场必备读物，社畜必读。我觉得如果刚进入职场，可能还没有很深的体会，可能要进入一年？然后再读可能不错。

《超效率手册》，看到了 xiaowen 推荐，趁着元旦假期读了一下。无法让你产生直接行动事项的信息流，都是垃圾。

《倦怠社会》，引用豆瓣评论：“精致的、视角倾向中产阶级的、面对时代必须正确的读物。但“包装”上，的确很漂亮。”

《年会不能停！》，因为朋友推荐所以去看的，很多人都说能获得很多共鸣，但我想了一下，也和同事聊过，我所在的公司目前好像还没有这个迹象，里面影射的点应该都没有？朋友说：那是因为你们还没有免费的食堂。
