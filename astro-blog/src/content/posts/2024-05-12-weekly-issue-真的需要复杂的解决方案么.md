---
title: Weekly Issue-真的需要复杂的解决方案么？
date: "2024-05-12T00:00:00.000Z"
slug: "Weekly-Issue-真的需要复杂的解决方案么"
tags:
  - Weekly
description:
---

## 文章

### 技术

[Tim Paul | Automation and the Jevons paradox](https://www.timpaul.co.uk/posts/automation-and-the-jevons-paradox/)

>Jevons paradox，杰文斯悖论，在经济学中，当技术进步提高了资源使用效率（减少了任何一种使用所需的数量），但使用成本下降导致需求的增加足以导致资源使用增加而不是减少。政府通常认为效率的提高会降低资源消耗，而忽略了出现悖论的可能性。

前段时间和同事讨论路网设计的时候，也提到过这个悖论，在高速公路上增加一条车道会减少拥堵。

这篇文章的后半段讨论的内容我没有想法，对自动化/科技带来的进步对人类的影响，没有认知。

>_"[Good, fast, cheap - pick two](https://en.wikipedia.org/wiki/Project_management_triangle)"_ they say. Let's automate to make things better, not just faster and cheaper.

---

[Web APIs: Enriched DX By Disallowing Unknown Fields](https://brandur.org/disallow-unknown-fields)

```Go
type Request struct {
    Message string `json:"message"`
}

data := `{"message":"Hello.","unknown":"Not a field on the struct."}`

decoder := json.NewDecoder(bytes.NewReader([]byte(data)))
decoder.DisallowUnknownFields()

var req Request
if err := decoder.Decode(&req); err != nil {
    log.Fatal(err) // json: unknown field "unknown"
}
```

[Golang](/mentions/golang) 通过 `DisallowUnknownFields` 方法来显式的禁止 API client 传递无效参数。

- 如果是已有的服务，那么在打开这个选项之前，需要先通过日志记录 API 是否存在传递无效参数的情况，如果存在，则联系下游进行调整。
- 在废弃字段时，需要显式的添加相关注释说明该字段现状，明确不应该继续使用。

---


[linux - How to force nginx to resolve DNS (of a dynamic hostname) everytime when doing proxy\_pass? - Server Fault](https://serverfault.com/questions/240476/how-to-force-nginx-to-resolve-dns-of-a-dynamic-hostname-everytime-when-doing-p/593003#593003)

[Nginx](/mentions/nginx) 如果 `proxy_pass` 指向的是一个域名而不是一个变量，那么域名解析只发生在启动解析期间。 需要在变量中设置域名，以此来保证每次都被正确的解析。

```
server {
    ...
    resolver 127.0.0.1;
    set $backend "http://dynamic.example.com:80";
    proxy_pass $backend;
    ...
}
```

---

[Zed Decoded: Linux when?](https://zed.dev/blog/zed-decoded-linux-when)

[Zed](/mentions/zed) 对 [Linux](/mentions/linux) 的支持，里面提到对原生应用的构建支持非常的苦：
- 比如说到 [Linux](/mentions/linux) 的时候，说的是什么？从来没有 [Linux](/mentions/linux) 这个东西
- 发行版，要支持哪些，也要支持对应的包管理器，用了 [TailScale](/mentions/tailscale) 作为例子，相关的构建代码在这里：[tailscale/release at main · tailscale/tailscale · GitHub](https://github.com/tailscale/tailscale/tree/main/release)
- 支持 [X11](/mentions/x11) 还是 [Wayland](/mentions/wayland)？
- 支持 [KDE](/mentions/kde) 还是 [GNOME](/mentions/gnome)？
- ...

P.S. 每次看到 [Zed](/mentions/zed) 的更新，都会想起隔壁的 [Fleet](/mentions/fleet)，刚刚又去看了一圈，没什么新东西。

---

[Alternative clouds are booming as companies seek cheaper access to GPUs | TechCrunch](https://techcrunch.com/2024/05/05/coreweaves-1-1b-raise-shows-the-market-for-alternative-clouds-is-booming/?guccounter=1)

>典型的例子是：CoreWeave 是一家 GPU 基础设施提供商，最初是一家加密货币挖矿公司，本周从 Coatue、Fidelity 和 Altimeter Capital 等投资者那里筹集了 11 亿美元的新资金。本轮融资后，其估值达到 190 亿美元，债务和股权融资总额达到 50 亿美元——对于一家成立不到 10 年的公司来说，这是一个了不起的数字。

挖矿赢一次，卖 GPU 服务又赢了，真是门好生意啊。

第一次看到 `Alternative cloud(s)` 这个概念，搜了搜，貌似是针对 AWS, GCP, Azure 的替代品的统称，比如 DO, Vurtl, Hetzner ？

---



[友好的 Python：封装和复用 | Frost's Blog](https://frostming.com/2024/friendly-python-reuse/)

忘记从哪里看到的了，看各种开源项目可能不能完全了解相关的技术细节，但是至少能让你知道什么是好的。

---

[SRE 日志：我的包去哪了？ | Manjusaka](https://www.manjusaka.blog/posts/2024/05/11/where-are-my-package/)

>向 192.168.0.239 直接发送的包，没有离开机器，所以 IP 地址不会被 MASQUERADE 为本机的 IP，然后直接被 docker-proxy 接管后 src ip 依旧为 172.18.0.3，导致了 conntrack 的状态不匹配，所以最终在 172.18.0.3 上没有对应的 socket，导致了 skb 被丢弃

多个 [DIND](/mentions/dind) 上的容器之间无法进行 UDP 通信调查。

---

[How LLMs Work, Explained Without Math - miguelgrinberg.com](https://blog.miguelgrinberg.com/post/how-llms-work-explained-without-math)

[LLM](/mentions/llm) 101，写的很不错。

---

[k8gb: 云原生最佳开源 GSLB 方案 | Oilbeater 的自习室](https://oilbeater.com/2024/04/18/k8gb-best-cloudnative-gslb/)

[k8gb](/mentions/k8gb) 是可以和 [kubernetes](/mentions/kubernetes) 无缝对接的一款 [GSLB](/mentions/gslb)，解决多个 kubernetes 集群之间的负载均衡问题。当前已有的 GSLB 实现方案存在无法和 kubernetes 无缝对接、公有云服务绑定、容器网络要求限制等问题。

[k8gb](/mentions/k8gb) 使用自身维护的 CoreDNS 来解决多集群负载均衡的问题，将上游的 DNS 记录 forward 到 k8gb 自身的 CoreDNS 中，具体请求流程： [K8GB | k8gb](https://www.k8gb.io/docs/) 。

k8gb 多集群之间的数据同步实现方式：
>大致的思路是每个集群的 k8gb 会把自己的 CoreDNS 的 Ingress IP 同样注册到上游 CoreDNS，这样每个集群就可以直接访问另一个集群的 CoreDNS 了。然后每个集群内的 CoreDNS 再按照一个特殊的域名格式比如 `localtargets-app.cloud.example.com` 来保存本集群内 `app.cloud.example.com` Ingress 的 Ingress IP 并维护其健康状态。    
>这样每个集群就都可以通过这个特殊的域名来或者其他集群这个域名对应的 Ingress IP 然后加入到自己的返回结果里，实现了域名解析的多集群同步。

---



### 生活


[GitHub - dylanaraps/dylanaraps](https://github.com/dylanaraps/dylanaraps)

>Have taken up farming.

[neofetch](/mentions/neofetch) 、 [pure-bash-bible](/mentions/pure-bash-bible) 的作者，把所有的项目归档了，离开了软件开发行业，从事农业。

---


[熊野古道徒步游记](https://sides-hang-nca.craft.me/pEkbr1l5FFfMCt)

同事的 [日本](/posts/日本) [熊野古道](/posts/熊野古道) [游记](/posts/游记)，非常的有趣，记录的很详细。

我要不要也搞一个录音笔，用来长时间的记录自己出去游玩的感受呢？

---

[Simplicity is An Advantage but Sadly Complexity Sells Better](https://eugeneyan.com/writing/simplicity/)

简单 vs 复杂。复杂意味着付出，背后包含了很多其他的含义，被认为更有挑战性，更有价值。这背后的含义，让大家在做事情的时候，本能的不会去将简单的方法视为最佳解决方案。大家追求自己“造轮子”，事实证明大部分晋升与其有相关性。

应该追求实用简单的方式来解决复杂的问题，而不是追求复杂的解决方式。

---

[Six definitions of love — Steph Ango](https://stephango.com/love)

爱就是恐惧。你越爱一个人，你就越害怕失去他们。但你决不能让这种恐惧阻止你尽可能地爱某人。

---

## 书影


《控糖革命》，少吃糖，保持血糖稳定有益于身体健康。最直接的办法就是严格控制自己的糖分摄入，如果不严格控制摄入，那么控制进食顺序也有效果，控制的方式有：
- 吃饭先吃蔬菜，再吃蛋白质，最后吃碳水。
- 吃任何碳水之前先吃点蔬菜。
- 吃饭前喝点醋也有不错的效果。
- 饭后保持一定的活动。

《歌手2024》，吊打，目前看华语歌手在唱歌领域是被吊打的，如果说 Faouzia 是 00 后声音机能强劲，那Chanté Moore 67 年的都可以当奶奶的年纪了，根本不在一个水平线上的比赛。


## 碎碎念

* 《救援高手》中的 Nathan 是怎么做到不笑的呢？
* 膝盖明显不行了，买了氨糖吃，今天吃第一次
* 狠话说出去之后，我再去找补的样子，真的好狼狈啊
* 很久没有一个事物，像 AI 这样，让所有人都 FOMO，如此的害怕错过。走产品功能的时候，虽然有时候跟着热点不一定是好事，但是投入一定的精力去尝试，应该也是作为一个必要的事项的。
* 我以为我限制了每个 app 的使用，手机的使用时间应该是可控的，结果还是每天都超过 5h，这个数字有些让我恐惧。
* Storm 说了一个角度："老外在中国艳遇多，因为出国之后没人认识他，不要脸了，总有可能成功的"
