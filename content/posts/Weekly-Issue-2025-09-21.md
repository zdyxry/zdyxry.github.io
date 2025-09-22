---
title: Weekly Issue-一根新鲜的玉米
date: 2025-09-21
tags:
- Weekly
description:
---

![](https://zdyxry.github.io/images/corn.jpg)

## 文章

### 技术

[Hosting a WebSite on a Disposable Vape :: BogdanTheGeek's Blog](https://bogdanthegeek.github.io/blog/projects/vapeserver/)

如果世界末日，我想和他呆在一起。突然想到如果世界末日，深圳是不是一个很好的城市，有巨量的电子垃圾，估计什么都能组装起来，而且靠海。

---

[人人都能写程序：Vibe Coding 与问题规模](https://blog.lyric.im/p/everyone-can-code-vibe-coding-and-problem-scale?utm_source=twitter&utm_medium=social&utm_campaign=newsletter)

> ## 程序 / 服务是商品  
> 不会写程序的人，通过**购买软件或订阅服务**来租用别人的解决方案。   
> 供应方卖的不是代码，卖的是**可持续的可靠性**与**持续维护**。   

> 对授课/知识付费/方法论反而是利好。因为「把问题讲清楚」和「把需求说准」变得更重要。   
> 好老师会教你**如何描述问题、如何验证结果、如何迭代**。这直接提升 Vibe Coding 的产出质量。


---

[What’s wrong with AAA games? The development of the next Battlefield has answers. - Ars Technica](https://arstechnica.com/gaming/2025/07/behind-the-next-battlefield-game-culture-clash-crunch-and-colossal-stakes/)

读着读着，感觉不只是在说 3A 游戏... 大型项目、张口就要 All in、涉及到多个团队、Deadline 明确，这几个关键词一上来就感觉到压力了。

---
[NVMe 子系统故障预测 - 健康度指标](https://archive.is/BH1W0)

> 当前，当服务器上出现 NVMe   SSD 故障时，排查过程复杂且耗时，例如需要登录操作系统和 BMC 查找故障盘，并通过点灯功能定位，操作繁琐，极大地增加了人力成本和误操作风险，甚至可能因 Surprise   Hotplug 支持不佳而引发机器重启。   
> 此外，目前行业缺乏统一的故障预测标准，各 OEM/ODM 厂商和 SSD 厂商的支持程度不一，导致信息抓取不一致，不利于全局监控和管理。

各个硬件厂商都是自己玩自己的，有时候明明已经有问题了，但是联系厂商也不给更换，老大难。这里的健康度 1-5，分别是：   
- 5，健康，Telemetry log 没有任何异常值   
- 4，亚健康，Telemetry log 中有些轻微的异常值   
- 3，有过小疾，Telemetry log 曾经有过一些异常值但恢复了   
- 2，重疾，Telemetry log 有一些关键的异常值   
- 1，膏肓，严重故障。   
感觉只有 1 和 2 能被更换。   

---
[Container Bandwidth Limiting | Hechao's Blog](https://hechao.li/posts/container-bandwidth-limit/)

针对主机上的容器进行带宽控制，使用 TC、HTB、IFB、eBPF。   
流量整形 (Shaping)：在出口 (egress) 控制带宽。流量管制 (Policing)：在入口 (ingress) 控制带宽。IFB 的作用：将入口流量重定向到虚拟接口，再在出口进行整形，从而实现 ingress 限速。关于 IFB 在其中的具体生效位置，参考这个链接： [iptables - How is the IFB device positioned in the packet flow of the Linux kernel - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/288959/how-is-the-ifb-device-positioned-in-the-packet-flow-of-the-linux-kernel) 

---
[If you are good at code review, you will be good at using AI agents](https://www.seangoedecke.com/ai-agents-and-code-review/)

>  If you don’t have the technical ability to spot when the LLM is going down the wrong track, you’ll rapidly end up stuck.

---
[%CPU Utilization Is A Lie - Brendan Long](https://www.brendanlong.com/cpu-utilization-is-a-lie.html)

作者尝试在自己的 5900X CPU 上验证 CPU 使用率和实际工作负载之间的关系，使用 Stress 和 Nginx 来进行测试。测试结果是当 CPU 使用率到 50% 时，实际的工作负载可能已经达到了最大负载的 60～100%，部分场景下 CPU 使用率到 80% 是，实际的工作负载可能到了最大负载的 100%，和多线程/Turbo 有关。

某种意义上讲，在监控报警中将 CPU 使用率阈值设置为 60% /  80% 也挺合理。想到了这篇： [CPU Utilization is Wrong](https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html) ，相较于 CPU 使用率，更建议关注 IPC (insns per cycle)。

---

[探秘源码：从 ChaosBlade 到 kubectl exec | My Site](https://spencercjh.me/blog/from-chaosblade-to-kubectl-exec#%E4%B8%BA%E4%BB%80%E4%B9%88%E4%B8%9A%E5%8A%A1%E4%B8%8D%E8%83%BD%E4%BE%9D%E8%B5%96-podsexec)

> 在 B 站的实际使用环境里，特别是用户广泛开展混沌测试的 UAT 环境，机器负载水位常年偏高。高峰期间很容易出现 `kubelet` 因故重启，但上面业务服务正常工作的情况。特别是考虑到 B 站 Kubernetes 容器服务 “去 Kubernetes” 程度较高，不使用 CoreDNS，不使用 Service，不使用 ConfigMap / Secret，故障情况下 pod probe 不影响服务流量进入。   
> `kubelet` 挂掉重启是非常正常的事情。`kubelet` 乃至 `containerd` 挂掉都是对业务服务来说可以接受的。

---

[Letter to Arc members 2025](https://browsercompany.substack.com/p/letter-to-arc-members-2025)

> A lot of people loved Arc — if you’re here you might just be one of them — and we’d benefitted from consistent, organic growth since basically Day One. But for most people, Arc was simply too different, with too many new things to learn, for too little reward.   
> To get specific: D 1 retention was strong — those who stuck around after a few days were _fanatics —_ but our metrics were more like a highly specialized professional tool (like a video editor) than a mass-market consumer product, which we aspired to be closer to.

确实，身边同事还在用 Arc 浏览器的，都是没有更换的打算。现在 Edge 和 Chrome 都已经添加了 Copilot 功能了，每个月都能看到各种 Chromium fork ，浏览器作为入口的激烈程度明显比 IDE 要高好多。

---

[Church Of Turing - The Enterprise Experience](https://churchofturing.github.io/the-enterprise-experience.html)

关于 $ENTERPRISE 的一些吐槽：
- 在小企业中不是问题的事情，在大组织中突然就成了棘手的问题    
- 因小失大
	- 一个为期两年的项目在即将启动时被取消，因为它略微超出预算，高层领导决定通过招标来节省更多资金。你购买新鼠标的请求已被拒绝。
- “紧迫性” 只是一个词
	- 这就是薛定谔紧迫感的一个有趣例子。它存在于巨大压力和绝对零压力的叠加之中。我再怎么强调也不为过，唯一的区别在于你是否打开了盒子。在这种情况下，一位优秀的经理才是关键；有些人会屈服于压力，希望成为一名 “团队成员” 能让他们获得领导层的赞赏（但这不会发生）；而有些人会出于体面而维护团队，希望这能让他们获得同事的赞赏（但这会的）。
- 工程团队本身就是帝国
	- 占主导地位的帝国很少愿意失去自己的地位，而且一般来说，帝国也很少愿意削弱自己的自主权。
---
[systemd system extensions for Fedora image based systems | extensions.fcos.fr](https://travier.github.io/fedora-sysexts/)

发现我对 sysexts 的理解有些问题，之前以为是类似于 distrobox/toolbox ，用于 debug 或者执行某些特定动作的 container，现在看好像是为了避免构建 base image 而引入的一些应用层的 container image。我好像可以把自己维护的 COPR 换成 sysexts。

---


### 生活

[As I remember London](https://world.hey.com/dhh/as-i-remember-london-e7d38e64)

[What’s a Foreigner? | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2025/9/14/whats-an-foreigner/)

值得阅读和思考，但我没有想法。

---

[[读后感]《婴幼儿及其照护者：基于尊重、回应和关系的心理抚养》](https://changchen.me/blog/20250918/infants_toddlers_and_caregivers/)

感觉把这里的「婴儿」换成「老人」也同样适用。

---
[又去了趟关西 - 就差亿点点](https://blog.zerob13.com/life%20manual/kansai-trip-2024/)

iPhone 可以直接用西瓜卡确实方便，不知道啥时候安卓可以用上。

---

[在菊厂八年的那些人、那些事 - 史海的博客](https://shihai1991.github.io/software%20engineering/2023/10/30/%E5%9C%A8%E8%8F%8A%E5%8E%82%E5%85%AB%E5%B9%B4%E7%9A%84%E9%82%A3%E4%BA%9B%E4%BA%BA%E9%82%A3%E4%BA%9B%E4%BA%8B/)

> 华为云计算在 2019 年左右经历了软件交付的交付流程变革，从公司的 IPD 交付模式转换到 DevOps 模式。   
> 但引入了 DevOps 作业流是否真的带来了质量和效率上的提升？目前还没看到最终的答案，希望在 5 年内能看到结果。

> **我们的工作、生活由无数次类似小朋友掷骰子事件叠加而成，所以我们的未来就有无限的可能。因此决定我们未来生活质量的不是那些我们已知的内容，而是那些不确定性事件以及我们如何在未知的情况下能处理好不确定事件。** 

> 17 年刚入职的那会，精力旺盛，开会交流和任务推进都可以做到各种怼天怼地怼空气，也挺佩服自己当初年轻精力旺盛，哈哈。但回头来看其实也挺惭愧的，许多讨论实际上没有有效产出。其中一个原因是过高的估计自己理解，而过低评估了事件的复杂度以及他人对事件的理解。后来也就慢慢懂了： **交流点到为止，我们不一定都是对的**。

> 我们遇到的更多的是如何在面对不确定性、不完美的时候，发挥主观能动性，扩宽可能性空间，在黑暗中寻找光。

---

### 书影播客

《独树不成林-252 - 查理・柯克的谋杀为何对当今美国右翼意义非凡？》    
《铜镜-23 Kirk 枪击案：政治暴力、共和传统和历史教训》

讲查理柯克枪击案的两期播客，我更喜欢铜镜的这期，感觉独树不成林感觉带有的感情色彩更浓一些，配合上结尾的 BGM，有一种时评节目的感觉，铜镜的这期更友善些。

《基本无害-Ep173 珀斯生存手册：在最孤独的城市做最莫名其妙的工作》，这期很有趣，在整个城市生存手册系列中都算是有趣的，观众从事的行业种类也很多：有 IT、金融、移民、装修、建筑、矿工等等。另外这期讨论了澳洲移民的一些事情。


## 碎碎念

* 家里突然停电，匆匆忙忙出去找咖啡店。
* 其实不匆忙，7 天前就发短信给我爸通知了，但是他没在意。
* 几周过去了，我觉得 《How It's Done》比 《Golden》 好听，可能因为后者太“规整”了。
* 重新走过自己小学中学生活过的地方，发现20 年过去：
    - 小学最初的地方已经拆掉了；
    - 小学搬到了我中学的校园；
    - 中学搬到了另一个地方；
    - 当时附近有两个中学，其中一个已经关掉好多年了；
    - 中学时候吃的包子铺还在营业，买了两个，味道确实是那个味道；
    - 一些小区的维护状态已经非常差了；
    - 看到了自己很多第一次经历的地方：网络小说、游戏厅、看电影、被抢钱；

    整体感受还不错。
* 感觉 arkade oci install 的安装方式挺讨巧的，看了眼代码内部直接调用的 crane 。
* 我好像跑的比之前快了
* 不记得自己上一次在地里干活是什么时候了，拍一根新鲜的玉米
* Dler 送的 udh emby 还不错。
