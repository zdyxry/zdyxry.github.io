---
title: Weekly Issue-《鲜花与面包》
date: "2026-04-19:00:00.000Z"
slug: "Weekly-Issue-flowers-and-bread"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Your code is worthless - Nathaniel Fishel](https://nathanielfishel.substack.com/p/your-code-is-worthless)

> It’s clear the rot has reached the highest levels of tech leadership. This idea has metastasized across Slacks, forums, and boardrooms: the belief that AI has magically “solved” software by making it effortless to generate mass quantities of it.

> We must return to the fundamental truth **The source code is not the product.** The product is the **Outcome** the user achieves. The code is merely the expensive, high-maintenance machinery required to deliver that outcome. If you can deliver a $1,000,000 outcome with 10 lines of code, you are a hero. If you deliver that same outcome with 37,000 lines, you have just created a $1,000,000 liability.

---
[The peril of laziness lost | The Observation Deck](https://bcantrill.dtrace.org/2026/04/12/the-peril-of-laziness-lost/)

连续两篇关于 Garry Tan 的项目讨论。懒惰是为了追求高效抽象来简化系统，因为人类时间有限，迫使人类会去主动的进行抽象，减少后续的认知负担，所以说是偷懒，其实是为了后续的方便在当下投入更多的努力， LLM 不会，他们没什么明确的限制，最终还是回到使用的人上面。

---

[Open Agents - Vercel](https://vercel.com/templates/template/open-agents)

**The key architectural decision: the agent is not the sandbox.** The agent does not run inside the VM. It runs outside the sandbox and interacts with it through tools like file reads, edits, search, and shell commands.

---

[An early look at tailscale-rs, a tsnet library in Rust](https://tailscale.com/blog/tailscale-rs-rust-tsnet-library-preview)

[[TailScale]] Rust 版本，这是好事。

---

[用户即开发者 | VMark](https://vmark.app/zh-CN/guide/users-as-developers/)   
[我为什么要构建 Markdown 编辑器：VMark | VMark](https://vmark.app/zh-CN/guide/users-as-developers/why-i-built-vmark.html)

> Faros AI 的研究——覆盖 1,255 个团队和 10,000+ 名开发者——发现高度 AI 采用与 **每位开发者 bug 增加 9%** 和 **PR 审查时间增加 91%** 相关。当 AI 以更低的准确率生成更多代码时，审查瓶颈会完全吸收"生产力"提升。

李笑来的这些思考真不错，而且真的在 Vibe 「产品」，而不是「工具」。

---

[The Center Has a Bias | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2026/4/11/the-center-has-a-bias/)

> But there is something important missing from that criticism when it comes from a position of non-use: **it is too abstract.**   
> If you want to criticize a new thing well, you first have to get close enough to dislike it for the right reasons. And for some technologies, you also have to hang around long enough to understand what, exactly, deserves criticism.

纸上得来终觉浅，绝知此事要躬行。我认同这篇文章的观点，但“center”和 “neutral”有一点文字游戏，neutral：你们爱吵吵，和我没关系；center：看你们吵吵我来用用，哦，果然不错/还行/不行。

HN 上面有一个大实话：“But right now I think the bigger risk is that the center is biased towards people with time and money”

---

[用 Claude Code 将三万行 Go 项目移植到 Rust：Agent Team 实践与 Harness 效率优化 - Lv. MAX](https://maxlv.net/blog/porting-mihomo-to-rust-with-claude/)

> 文档是给 Agent 写的，不只是给人写的。这意味着文档的写法需要调整：  
> - **用表格代替散文。** Agent 解析表格比理解段落高效  
> - **引用要精确。** "参见 ADR-0001" 比 "参见之前的架构讨论" 好，因为 agent 可以直接定位文件   
> - **状态要明确。** 每个工作项标注 "completed / in-progress / blocked"，而不是 "我们之前讨论过这个"   

---
[从 PostgreSQL fsync EIO 失败处理说起](https://zhuanlan.zhihu.com/p/2024718290497324365)

> 2018 年 3 月底, Craig Ringer 在 pgsql-hackers 邮件列表中报告了一个用户遭遇的数据损坏案例 [1]. 问题的核心在于: PostgreSQL 使用 Buffered I/O, 在写入数据后调用 fsync() 来确保数据落盘. 当 fsync() 失败时, PostgreSQL 的做法是重试 fsync() -- 然而第二次 fsync() 返回了成功, 但数据实际上并没有写入磁盘.


> **为什么这些数据库没有在 fsync 失败后 crash?** 原因是多方面的:   
> 1. **认知盲区**: 2018 年之前, 几乎所有数据库开发者都不知道内核会在 fsync 失败后丢弃 dirty page.   
> 2. **本地存储极少触发**: EIO 在本地 SSD/HDD 上几乎只在物理损坏时才出现, 一辈子可能遇不到.   
> 3. **crash 后未必能恢复**: LevelDB 的 log 和 SQLite 的 journal 也走 Buffered I/O, crash 后的 recovery source 本身可能就是损坏的.    
> 4. **产品约束**: SQLite 和 LevelDB 是嵌入式数据库, 因一次瞬态 I/O 错误就把宿主应用杀掉, 在移动端和桌面端不可接受.    

---




### 生活

[来了不是深圳人(1)：拜拜了深圳 | 积薪(极简版)](https://darmau.design/article/you-will-never-become-szr-1/)   
[来了不是深圳人(2)：离开深圳要去哪 | 积薪(极简版)](https://darmau.design/article/you-will-never-become-szr-2/)   
[来了不是深圳人(3)：成都的好与坏 | 积薪(极简版)](https://darmau.design/article/you-will-never-become-szr-3/)   

> 根据最近的人口普查结果，深圳已经有 1800 万人，跟广州一样。但广州的面积是深圳的 3.7 倍，北京、上海人口比深圳多不了多少，但面积也是好几倍。所以深圳的人口密度是一线城市里最高的。   
> 随你怎么想，失败就失败吧。失败不可怕，可怕的是不愿意承认失败并及时止损。我想要真正的生活，再在深圳耗下去没有意义，不如赶紧跑。

> 整体看下来，气候最宜居的标准就一个：低纬度的高海拔地区。低纬度保证光照，冬天不会太冷；高海拔确保夏天不会太热；同时高海拔大概率发展不了工业，空气就会不错。这就是云南如此舒适的原因。

> 差不多的地段和户型，成都的租金大概是深圳的 30%~40%。假如你要在深圳南山科技园附近租一套两房，至少得准备 8000 的预算；科技园平移到成都就是高新区，在大源要租一套两房，不考虑个别豪宅大户型的话，大概只需要 3000～6000。

> 成都的阳光是稀缺品，尤其是在冬天。一个月太阳直射的时间加起来可能连一个白天都没有，整天都是阴沉沉的。导致你很难分辨方向和时间，有时候恍惚间不知道究竟是上午还是下午。

身边同事这几年陆陆续续的从北京/上海搬去杭州/成都的有不少了。

---

[Ipoh 游记 | 一派胡言](https://dantezy.xyz/posts/ipoh-2024/)   
[吉隆坡游记 | 一派胡言](https://dantezy.xyz/posts/kl-2026/)

> 从机场出来打车去吃了午饭，然后涂了防晒，准备走路去酒店。    
> 来之前我的朋友小柯跟我说，别走路，打 Grab，体感温度 40 度以上。

防晒很重要。上次在马来呆了几天，左右胳膊的色差回来几个月才恢复。

---


[商业战略报告：2026 名创优品 - 三杯过后 | Xiaowen.Z Deployed](https://xiaowenz.com/blog/report-miniso-2026.html)

> **下方挤压**：零食很忙、好特卖等折扣零售 2024 年门店突破 4.5 万家。一瓶可乐折扣店 1.8 元，名创 3 元——价格敏感消费者正在流失。

印象中[[疯投圈]]有一期播客聊过，名创优品卖的比较好的品类有矿泉水。

---

[商业战略报告：胖东来 - 三杯过后 | Xiaowen.Z Deployed](https://xiaowenz.com/blog/report-pangdonglai.html)

> 这种"利润共享"模式在零售行业几乎独一无二。它的直接结果是：员工流失率仅约 2%，而行业平均为 20-30%

---


### 书影播客


《鲜花与面包》，冯子豪的单口专场， 在上上周单利人原创喜剧大赛中，冯子豪获得了亚军，冠军是贤鱼，季军是丹妮。这 3 个人中，贤鱼属于疯子，用冯子豪的话说，没有人可以在舞台表现力上战胜贤鱼，丹妮属于百变，段子充满了巧思，看似是互动，实则全是设计，相比之下冯子豪就显得有些特殊，是很传统的单口演员，属于刻板印象的单口演员。在这之前我不认识他，直接花 99 块卖了票，还不断的和同事安利，果然，3 天后专场价格涨了 40 变成了 139 ，但同事也没有人买。

这个专场前半场靠着刻板印象，后半段靠生活经历：一个山东济南人在成都生活，可惜单口中出名的山东演员太多：张灏喆、孙书恒、唐香玉、徐志胜、何广智、孟川，太多了，已经把山东的刻板印象讲遍了，很多梗我都猜到要说什么，没那么巧妙。在讲自己高考经历的时候，提到自己是 00 后，2002 年出生，高考那年是疫情发生的那年，2020 年已经是 6 年前的事情了。


《气候变化与人类未来》， 读完之后感觉人类没救了，爱咋咋地吧。

部分摘录：

> 在大多数情况下，民众并不愿意承担比如碳定价之类的措施带来的经济成本，因为他们没有意识到处理气候变化问题的紧迫性。虽然不采取减排行动可能给未来造成严重后果的事实已然十分清晰，但是，人类或许仍然无法应对这次风险，而且，留给人们改变现状的时间已经所剩无几。

> 即使我们接受这样一种观点，即人类现在已经走上了一条通往未来的道路，这条道路可能会破坏他们目前的生活方式的基础，而且可能是彻底破坏，但这对于整个地球本身来说没有任何影响。地球的大气和地质过程将会像以往一样调整并过渡到某种新的平衡状态。    
> 无论发生哪种情况，地球都会继续运转下去，只是许多现存物种可能会出现新的大规模灭绝，这类事件在遥远的过去已经发生过很多次。我们知道，幸存的生命又会重新振作起来，以新的方式继续生存。

> 如果我们在某个时候决定尝试通过减少人为温室气体的排放来阻止地球温度继续上升，那么我们这一决定的积极影响，即温度不再上升，将在几十年后才会在大气中显出来。

> 截至2019年，签署巴黎协定的151个国家约占全球76亿人口的46%，但温室气体排放只占全球的15%左右。在这151个国家中，许多国家仍然处于不发达和贫穷状态，毫无疑问，它们未来需要发展经济和使用能源。更重要的是，六大主要排放实体之一的印度也面临这种情况。




## 碎碎念

* 越来越多的网站只提供 dark theme，我现在反而需要一个插件来强制 light theme 了。
* 20 年前的受众较少的影视资源，找起来还有点费劲呢。
* 什么时候我能去参加单立人喜剧节呢？
* 买了单立人原创喜剧大赛亚军的专场票，现在不买，下次就该涨价了。。
* 日常都有 ublock，刚刚在手机上发现 Disqus 的贴片广告真多啊
* TIL: “广西公文包”是网络流行词，指广西地区特有的、用于装载农家自酿白酒的白色方形塑料桶（通常为2.5L-5L），因其形状方正便于手提而得名。
* > AI 把执行成本压到了接近零，但判断成本一分没降。而大多数人一辈子都在逃避的，恰恰是判断。
* 健身房都已经将浴室隔离了，怎么还有人洗澡不关门啊。
* Kimi 接入了天眼查，有点 Setapp 的打包样子了。(但天眼查这样卖数据，不会把自己卖死么？
* 一个看似非常负责的人，轻描淡写的给出不负责任的回复。
* 突然，上海办公室好像也开始进入到特定的周期了：聊买房装修、见家长、结婚生子。感觉进度一下子就变快了，不是别人快了，是我慢了。上一次有这种感受，是 10 年前的北京办公室。
* 看到了韦小宝一家的故事，有些伤感。
* 喜联做了什么能让大部分演员都远离
* 周日下午在西岸躺着，很好
* 据宁波天一阁包氏宗谱，包玉刚是宋朝龙图阁直学士包拯的二十九世孙。
* 人民币韩元汇率也是历史最佳了，1 元可以换 216 韩元。