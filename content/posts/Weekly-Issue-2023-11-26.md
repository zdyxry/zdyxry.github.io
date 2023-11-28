---
title: Weekly Issue 2023-11-26
date: 2023-11-26
tags:
- Weekly
description:  “好像什么都不想做”，“那就什么都不做”
---


## 文章

### 技术

[X 上的 NadeshikoManju@摇曳露营 S3 2023年四月放送：“阿里的同学关注到了这条推，那我就详细聊聊我用下来的坑点把 1. 先说定位，为什么没有一个 all in one 的 aliyun cli，为什么需要用户一个产品安装一个 CLI？ 2. 然后我们来看安装，为啥不能提供包管理的安装方式，非要用户手动下载二进制。而且你们下载二进制不做 SHA 系的校验和 GPG 签名发布么？” / X](https://twitter.com/Manjusaka_Lee/status/1725931182070837581)

[[Manjusaka]] 提到的关于 [[Aliyun]] `ossutils` 体验很差的吐槽，其中很多是通用的：
- 为什么没有统一的命令行工具，反而需要一个产品提供一个 CLI？
- 为什么不提供包管理的安装方式，只提供二进制，但是二进制不做 SHA 校验和 GPG 签名；
- 提供的统一配置文件，需要手动填写 endpoint,accessKeySecret, stsToken..... 为什么不提供 SSO？
	- 不支持单文件内的多个不同账户配置
- 不支持环境变量指定配置文件；
- CP 命令参数不清晰，--acl 和 --meta x-oss-object-acl 的区别？暴露了过多细节给 client；
- 不支持 bash_complete ；

其中 [[ayanamist]] 的总结是：都是外包做的，而且文档都很差，主要是没有办法给些文档这件事打绩效，做 DX 都是无法打绩效的，如何评判工作做的是否好呢？

---

[Canonical Microcloud: Simple, free, on-prem Linux clustering • The Register](https://www.theregister.com/2023/11/16/canonical_microcloud/)

[[Canonical]] 推出 [[Microcloud]] ，应对小型私有云场景，看上去也挺好的，可以用用。（demo 翻车是常见操作了，还是录制视频比较靠谱。

---

[Python errors as values: Comparing useful patterns from Go and Rust - Inngest Blog](https://www.inngest.com/blog/python-errors-as-values)

关于[[python]] 的错误处理，其中提到了 [GitHub - rustedpy/result: A simple Rust like Result type for Python 3. Fully type annotated.](https://github.com/rustedpy/result) 这个库，可以让[[python]] 的返回值变为[[Rust]] 模样。

```python
from result import Result, Ok, Err

def divide(a: int, b: int) -> Result[int, str]:
    if b == 0:
        return Err("Cannot divide by zero")
    return Ok(a // b)

values = [(10, 0), (10, 5)]
for a, b in values:
    divide_result = divide(a, b)
    match divide_result:
        case Ok(value):
            print(f"{a} // {b} == {value}")
        case Err(e):
            print(e)
```

---

[Push Ifs Up And Fors Down](https://matklad.github.io/2023/11/15/push-ifs-up-and-fors-down.html)

将 if 尽可能的放在上面，for 尽可能的放在下面。将条件判断放在函数调用处统一处理，保证函数在执行时的参数始终是正确的。将数据处理统一实现为 batch ，将 batch 操作视为基本情况，将单个处理视为 batch 处理的特殊情况。
实际编写业务代码时，可能大部分场景下都是都是依赖于 walrus 自身属性来进行判断比较多？

```rust
// GOOD
if condition {
  for walrus in walruses {
    walrus.frobnicate()
  }
} else {
  for walrus in walruses {
    walrus.transmogrify()
  }
}
// BAD
for walrus in walruses {
  if condition {
    walrus.frobnicate()
  } else {
    walrus.transmogrify()
  }
}
```
---

[It's Time For A Change: datetime.utcnow() Is Now Deprecated - miguelgrinberg.com](https://blog.miguelgrinberg.com/post/it-s-time-for-a-change-datetime-utcnow-is-now-deprecated)


[[python]] `datetime.datetime` 的 `utcnow()` 和 `utcfromtimestamp()` 将被移除，需要使用 `datetime.datetime.now(datetime.UTC)` 来替代。

根本原因是 `utcnow()` 和 `utcfromtimestamp()` 不感知时区，但是有些函数接受时间戳并假设它带边的是带有时区的时间戳。

---

[test, [, and [[ - Julio Merino (jmmv.dev)](https://jmmv.dev/2020/03/test-bracket.html)

很多人第一次编写 [[shell]] 时候，都会遇到 `[` 和 `[[` 的问题，这篇文章总结的很好： `[` 与 `test` 是一个东西，`[[` 是 [[Bash]] 中的能力。如果想要写通用的 [[shell]] ，那么使用 `[` ，如果明确执行的环境是 [[Bash]]，那么保持使用 `[[` 。 

---

[twitter.com/zdyxry/status/1727636324898005405](https://twitter.com/zdyxry/status/1727636324898005405)

我吐槽自己的 `onmyzsh` 太慢了，大家提供了很多很多的工具和方法，感觉需要汇总整理一波。

---

[VMware homelab [Part 1]: Introduction & Considerations | jimangel.io](https://www.jimangel.io/posts/vmware-series-p1-considerations/)

作者使用 3台 [[NUC]] 来构建自己的 [[homelab]] ，手把手教学。

---

[How moving from AWS to Bare-Metal saved us $230,000 /yr.](https://blog.oneuptime.com/moving-from-aws-to-bare-metal/)

作者从[[AWS]] 迁回自建机房，本身业务 CICD 都是基于 K8s 的，在 BareMetal 上使用 MicroK8s 来管理 K8s 集群，配合使用 [[NFS]] 和 [[MetalLB]] 。

---

[Exporting PostgreSQL logs into Prometheus metrics using Vector – Palark | Blog](https://blog.palark.com/vector-to-export-pgsql-logs-into-prometheus/)

通过 [[vector]] 将 [[PostgreSQL]] 的异常日志暴露给 [[prometheus]]，只需要使用 vector 就可以实现日志的读取、解析、结构化、过滤、转换为 exporter。最终暴露的指标是异常日志的数量，通过检查最近 30min 内日志数量是否有变化来产生报警。
最近有一个需求，需要将 IPMI SEL 通过 exporter 暴露 Metric，在基本的接受到日志就产生告警之外，还需要拿到告警的具体信息，可能需要通过 label 来暴露。

---

[Launch Week Day 3 - Fastest self-hostable open-source workflow engine | Windmill](https://www.windmill.dev/blog/launch-week-1/fastest-workflow-engine)

介绍 [[Windmill]] Workflow ，受伤的只有 [[airflow]] ，[[airflow]] 真的是太慢了。

---

[Software engineering is about thinking, not typing | Organizing Chaos](https://jordankaye.dev/posts/thinking-not-typing/)

> Weeks of coding can save you hours of planning.

思考的重要性远胜于敲击键盘的重要性。虽然迭代式工作和快速反应变化的能力非常重要，但在着手解决问题之前，仔细思考潜在解决方案的全貌更加有效。

---

[The Categories of Bugs in Python Apps](https://threeofwands.com/the-types-of-errors-in-python-apps/)

将[[Python]] 程序错误分为4类：Type 错误；import 错误；runtime 错误；业务逻辑错误。如何有效的避免这些错误，应该尽可能的降低错误类别，将业务逻辑错误转换为 runtime 错误，将 runtime 错误转换为 import 错误。 尽可能的提前暴露错误。

---

[The Changing “Guarantees” Given by Python's Global Interpreter Lock · Stefan-Marr.de](https://stefan-marr.de/2023/11/python-global-interpreter-lock/)

[[Python GIL]] 的行为在不同版本中的变化，其中提到了Python 3.9和Python 3.13之间GIL实现的差异，特别是在释放GIL的时机上的变化。Python 3.13引入了更强的原子性保证，使得大多数字节码序列都是原子的，而Python 3.9则只有很少一部分字节码序列是原子的。

在编写代码的时候不应该依赖特定的 GIL 行为。

---



### 生活

[为什么我从 iPhone 切换至 Android 手机 | Henry Z's blog\~](https://changchen.me/blog/20231117/iphone2android/)

喜欢这种在购买一件物品前的思考，发现周围有朋友换设备的原因是：”这个手机我已经用 3 年了“，这种非常感性的原因，不从自己的需求出发。

---

[Faker：再度攀登 | 大破进击](https://jesor.me/2023/14-times-long-journey/)

是[[Faker]] 让[[LOL]] 更精彩。

---

[Working Effectively With Executives During an Incident | Rootly](https://rootly.com/blog/working-effectively-with-executives-during-an-incident)

如何让老板知道当前事故的进展？
- 明确通知条件（case 级别）
- 当前进展
	- 对客户造成的影响
	- 解决问题取得了哪些进展
	- 相关的文档链接
- 保持简洁，汇报不要包含过多的技术细节
- 重新思考自己的局限性
	- 常规处理流程可能会按照既定框架执行，如果没有既定框架，可以做些什么来快速的解决问题？
- Why?What?How?

---

[开源项目礼节 - MDN Web 文档项目 | MDN](https://developer.mozilla.org/zh-CN/docs/MDN/Community/Open_source_etiquette)

[[Mozilla]] 开源礼节，友好，耐心。共勉。

---

[南都观察-旧-在中国，感冒治疗史就是一部药物滥用史-南都公益基金会](https://www.naradafoundation.org/content/5691)

>**实际上，在中国治疗感冒，就是一部药物滥用史。**
>**大部分感冒真的是喝水喝好的，而不是吃药吃好的。**
>**只有病毒引起的，才能称之为感冒。因为致病原因不同，治疗的药物自然是不同的。**
>抗生素只对细菌有效，对病毒引起的感冒并无效果。
>**感冒需要吃“消炎药”，也是中国人根深蒂固的一种想法。此处的“消炎药”又被窄化为了抗菌素中的抗生素。**
>**滥用抗生素只会催生出对抗生素耐药的细菌，甚至是会出现现有抗生素都奈何不了的“超级细菌”。**
>**世界卫生组织的调查结果显示：中国住院患者抗生素的使用率高达80%，其中使用广谱抗生素和联合使用两种以上的抗生素的比率高达58%，远超出30%的国际水平。**

药，还是别乱吃的好。

---

[Things you're allowed to do](https://milan.cvitkovic.net/writing/things_youre_allowed_to_do/)

可以做的事，有很多事是出于各种原因没有尝试过的。
- 可以说“我不知道”；
- 不说善意的谎言；
- 去见朋友，只是为了见朋友；
- 聘请专业的人来帮你完成某些事情；
- 接触陌生人；

---

[Stop Obsessing Over Tools | PlugWorld](https://plug-world.com/posts/stop-obsessing-over-tools/)

> 这样做并不会提高你的效率，你永远找不到最好或最完美的设置。我的建议是，只要一样东西足够好、能完成工作，你就不妨坚持用下去。不要盯着工具，而要盯着你要完成的工作。

很多人都在追求工具，在各个社交平台上分享工具总是流量密码，以前我可能也会这样，但是现在除非遇到了问题，否则我会维持现在的工具链。但是同时，我也会关注一些新的工具，了解它们解决什么问题，如何解决的。如果真的适合也会及时尝试，快速试错，来防止自己“过时”。

---

## 书影

《涉过愤怒的海》，故事没讲好，想要说家庭，那就讲家庭，试图用几分钟的旁白来解释，太无力了。

