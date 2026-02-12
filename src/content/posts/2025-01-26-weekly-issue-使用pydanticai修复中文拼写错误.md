---
title: Weekly Issue-使用PydanticAI修复中文拼写错误
date: "2025-01-26T00:00:00.000Z"
slug: "Weekly-Issue-使用PydanticAI修复中文拼写错误"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Block AI scrapers with Anubis - Xe Iaso](https://xeiaso.net/blog/2025/anubis/)

使用 [[hashcash]] 方式来对 AI 爬虫进行过滤。好像第一次看到 hashcash 的实际应用。代码实现在这里： [x/cmd/anubis/README.md at master · Xe/x · GitHub](https://github.com/Xe/x/blob/master/cmd/anubis/README.md) 

---

[Do Hard Things](https://writing.nikunjk.com/p/do-hard-things)

> Getting good at these hard things doesn't make life easier—it makes you responsible for harder problems. But that's the point. Everyone faces difficult decisions. The difference is those who built this muscle early get to choose which hard problems they want to solve. Everyone else takes whatever hard problems life hands them. Start before life gets complex—before each new responsibility makes every risk feel heavier.

---

[我在 iOS Conf SG 25 的演讲](https://starming.com/2025/01/21/ios-conf-sg-25-share/)

> 这次的画的图也是我花费时间最长的一次，学习了些时尚杂志的设计和布局。有些来不及调配色的图，我就参考媳妇买的巧克力包装配色。

每一张画作都很精美，完全不懂技术细节也看得很有滋味。

---

[x.com](https://x.com/glcst/status/1882387330129973514?s=46)

[[Turso]] Cloud 再一次发生数据丢失事故（是的，这是第二次）。这种事情发生过一次，就会失去信任了。

---




### 生活


[27 岁，一个日本留学生的 2024年终总结 - Simon's Blog](https://song.al/2024)


> 至于屋久岛，则是一个令我想再去一次的地方。整个岛屿都像是一个巨大的森林公园，在西部林道到处都可以见到各种动物：躺在马路上晒太阳的鹿、在车子旁边抓耳挠腮的猴子。在这个岛上，比人类更多的是动物，而这些动物都没有受到任何拘束，随意行走，在岛上的生活很像隐居山林，每天都有新的惊喜。

[[日本]] [[屋久岛]]很美。

---

[大厂的所有人都是演员，包括我。](https://archive.is/4Ee3R)

> “所有的工资活动都是一种卖银”by🐴，我读的时候，我想，就算卖，也要写高效有用的代码，高效有用的卖。
> 但事实不是这样。卖的人太多了，该卖的花样和地盘已经全卖完了。但为了领工资，老板假装在卖，我也假装在卖，用花里胡哨的三年规划假装在卖，用层出不穷的汇报加班假装在卖。
> 卖吧，同志们，让我们美美与共，天下大卖。

---

## 书影

无。

## 使用 PydanticAI 修复中文拼写错误

最近看到了很多次 PydanticAI ，自己实际上在代码场景下除了 Copilot，貌似没有使用 AI 解决实际的问题。正好我有一个需求场景是很适合 AI 来做：笔记中的拼写错误。于是花了些时间阅读了 PydanticAI 文档，跟着示例走了一遍，发现这个有些玄学，比如关于 Result 的示例中，预期是可以将 AI 返回的结果转换为特定的数据结构的，我预想是将笔记内容给 Agent 后，Agent 可以返回给我成一个特定的数据类型，然后我解析数据类型来更新笔记，但是实际上我试了多个 Model，都没有得到预期的结果。

```Python
from pydantic import BaseModel

from pydantic_ai import Agent


class CityLocation(BaseModel):
    city: str
    country: str


agent = Agent('gemini-1.5-flash', result_type=CityLocation)
result = agent.run_sync('Where were the olympics held in 2012?')
print(result.data)
#> city='London' country='United Kingdom'
```

我的笔记都是使用 Markdown 语法编写的，所以期望的是 AI 返回修复后的结果，并且能够正确的处理一些特殊格式，经过一些调试验证，最终我使用的 Prompt 如下，实际执行流程是 定义 Agent 和 System Prompt，遍历所有的笔记文件，然后将其内容读取，并添加 `%%%{content}%%%` 来传递给 Agent，将 Agent 的返回结果直接覆盖写入到笔记文件中。

```
general_prompt = """
找出内容中的中文和英文拼写错误，并将其更正。 请注意，不要更改内容的格式，例如空格，换行符等。

对于英文中没有通用中文翻译的技术术语，使用英文原文。

对于被反引号 (`) 包围的代码片段，不要更改内容，保持英文原文。 例如，`list`， `dict`，保持不变。

对于被 ([[]]) 包围的内容，不要更正内容，保持原文。 例如，[[pull request]]，保持不变。

对于以 (---) 开头的内容，不要更正内容，保持原文。 例如，---，保持不变。

对于以 (> ) 开头的内容，不要更正内容，保持原文。 例如，> 请注意，保持不变。

内容以 Markdown 格式书写，更正结果也以 Markdown 格式写。 不要在生成的内容周围添加三反引号 (`)。

当出现代码示例，例如控制台或终端输出时，通常用三反引号和类似 “console” 或 “bash” 这样的关键词环绕（例如 ```console）。 不要更正内容，保持英文原文。

原始内容将被三重百分号 (%) 包裹， 你需要找出其中的中文拼写错误并将其原地更正，更正后内容不要包含三重百分号。

如果内容中没有中文或英文拼写错误，则直接返回原始内容， 返回内容不要包含三重百分号。

"""

```

## 碎碎念

* 给 iPad mini7 买了一个闪魔的钢化膜，没想到现在贴膜工具这么傻瓜了，按照步骤贴，效果很好。
* 原来银行的客户经理是可以看到客户的资金用途的呢？汇丰中国的可以。
* 大部分内部项目的 README，写了和没写差不了多少。
* MS 365 Copilot 基于 Word 生成文档，默认格式就挺好看的。
* 蝴蝶机终于加了 5kg 到 60kg 了，不知道春节过后会降到多少




