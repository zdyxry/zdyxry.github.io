---
title: Weekly Issue 2023-11-12
date: 2023-11-12
tags:
- Weekly
description: 
---


## 文章

### 技术
[Linux Installation Date: How to Discover Your System's Age](https://linuxiac.com/how-to-find-linux-os-installation-date/)

如何查看 [[Linux]] 安装时间，通过获取 `/` 文件系统的 Birth time 来确定：

```
$ stat /
  File: /
  Size: 188             Blocks: 0          IO Block: 4096   directory
Device: 0,33    Inode: 256         Links: 1
Access: (0755/drwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2023-03-16 13:11:52.876212014 +0800
Modify: 2023-09-25 09:15:24.162426570 +0800
Change: 2023-09-25 09:15:24.162426570 +0800
 Birth: 2023-03-16 13:11:52.876212014 +0800
$ stat / | awk '/Birth: /{print $2 " " substr($3,1,5)}'
2023-03-16 13:11
```
---

[Gregory Szorc's Digital Home | My User Experience Porting Off setup.py](https://gregoryszorc.com/blog/2023/10/30/my-user-experience-porting-off-setup.py/)

从`setup.py` 迁移到 `pyproject.toml` 的过程，作者找不到官方有效信息来辅助迁移，整个过程非常的痛苦。[[python]] 的包管理器混乱是众所周知的，社区也一直在努力做好，如果你想要做类似的事情，我觉得不要 **迁移**，而直接**重新配置** 。无论是 [[poetry]] 还是 [[PDM]]，从零开始从比较好。

---

[100% test coverage is not enough](https://blog.robertroskam.com/p/100-test-coverage-is-not-enough)

100% 的单测覆盖率不能说明所有，作者提到可以使用 [GitHub - HypothesisWorks/hypothesis: Hypothesis is a powerful, flexible, and easy to use library for property-based testing.](https://github.com/HypothesisWorks/hypothesis) 来帮助我们自动的生成测试参数，防止遗漏某些场景。

---

[让 ChatGPT 帮我们总结 Hacker News - 喵叔没话说](https://blog.betacat.io/post/2023/06/summarize-hacker-news-by-chatgpt/)

发现我也有类似的需求，平时通过 RSS 订阅了一些博客/新闻，需要让 [[ChatGPT]] 先总结一下所有的订阅信息，可以快速的帮忙做一个初步的筛选。

---

[用排队论解释延时与利用率的关系 - 喵叔没话说](https://blog.betacat.io/post/2023/05/explain-latency-and-utilization-using-queueing-theory/)

>可以看到，在`0.8`之前，利用率每提升 10 个百分点，延时就会增加 60% 左右，但利用率一旦超过`0.8`，延时急剧上升，且增速越来越快。在 0.9~0.99 这个区间内，延时甚至增加了 11 倍。这就是为什么，我们会有个不成文的惯例 —— **系统的各项指标使用率都不要超过 80%**。

>系统处理能力（`μ`）与延迟（`W`）成反比，提升处理能力后，也能线性的减少访问延迟。

>吞吐与延迟成正比，所以有人认为，[同一个集群不可能同时满足低延迟和高吞吐的需求](https://blog.danslimmon.com/2019/02/26/the-latency-throughput-tradeoff-why-fast-services-are-slow-and-vice-versa/)，只能做取舍，具体解释如下：  
    - 低延迟意味着低利用率，即希望系统没有排队现象，请求来了立即就得到处理，无需等待。  
    - 高吞吐意味着高使用率，即希望系统队列中始终有可用请求，这样各种资源才不会有空闲的时间，系统始终处于忙碌状态。  

扩展阅读：[The Latency/Throughput Tradeoff: Why Fast Services Are Slow And Vice Versa – Dan Slimmon](https://blog.danslimmon.com/2019/02/26/the-latency-throughput-tradeoff-why-fast-services-are-slow-and-vice-versa/)

---

[Go's 1.22+ ServeMux vs Chi Router - Calhoun.io](https://www.calhoun.io/go-servemux-vs-chi/)

作者比较了[[Golang]] 1.22 引入的 ServeMux 和 chi 的对比，从使用方便的角度来说 chi 更方便些。

---

[git rebase: what can go wrong?](https://jvns.ca/blog/2023/11/06/rebasing-what-can-go-wrong-/)

`force pushing makes code reviews harder`  这个问题貌似 [[Github]] 没有什么比较好的解决方式，只能尽可能的在一个 PR 里面多叠加新的 commit 来显示此次修改内容。

---



### 生活

[HHKB Studio 上手体验](https://tjtsblog.notion.site/HHKB-Studio-73c4c83dc7cc4770b9427bba7390c676)

看上去不错，可以解决有时候必须用鼠标操作的场景，双手在鼠标和键盘之间移动的困扰，现在虽然大部分在 Chrome 下都是用 `Vimium`，但是有些界面不是很友好，还是需要用到鼠标。

---
[城市轨道交通规划设计行业2年 萌新 Aaa](https://aaany.app/aaa/loiq85kia)

关于轨道交通的一些问答。
>一条线从规划到运营大致经历：线网规划—建设规划—预可（规划方案）—工可（工程可行性研究）—总体设计—初步设计—施工图设计—施工—运营这样的流程 在中国前期的规划设计大致经历3-4年 土建开工到开通运营又得经历5-6年 整套流程下来大概8-10年 这个速度在全球算是偏快的
>
>如果是从财务、一体化开发还有客流效益之类角度来讲的话肯定是香港 但香港的土地制度还有法规体系和内地没法比 而且香港地铁的公益属性不如国内明显 内地的话北上广深这些超一线城市还有常年蝉联新一线城市头把交椅的成都 他们的地铁系统从规模量级还有客流效益都算很可以的 具体到交通接驳还有与城市的融合程度来看可能南方做得比北方更好一些
>
>高峰小时运能人次每小时，一般来说有轨电车运能在每小时1.2w一下 而轻轨能到1-3w 地铁的话基本在3w以上。
>从造价角度考虑的话，地下肯定是要比高架要贵上几倍的（高架3-5亿造价vs地下8-10亿+的造价）。

---

[Solving the Productivity Paradox](https://www.newyorker.com/culture/office-space/solving-the-productivity-paradox)

>We gained access to an armada of supercharged workplace tools, and yet we’re not getting much more done.   

作者认为工具所带来的生产力提升是有限的，应该从流程上去改变。但是我觉得这里应该有一个前提，就是工具已经足够好用的情况下。而且文章中提到的“生产力” 也过于抽象，没有一个明确的定义和标准，如果对于个体员工而言，一个好的工具确实可以提高工作效率，这个是明确的；可能对于公司而言，相对于工具上的改进，从工作流程上改进更能提高效率。

---

## 书影

《魔鬼的计谋》，韩国综艺，一群陌生人共同生活7天6夜，通过人性、智力游戏，来赢得奖金。国内类似的节目有《决胜 21 天》（节目很糊，可以去看火树的 reaction）。整体还是好看的，不过能感觉到节目组为了提升节目效果，剪辑上有些差异。

《上瘾五百年》，所有容易让人上瘾的东西，都是被控制的。如果看上去没有被控制，那一定是无法大规模传播。瘾品和早期的殖民是有强关联的。

