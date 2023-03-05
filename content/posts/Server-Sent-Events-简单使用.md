---
title: Server-Sent Events 简单使用
date: 2020-02-03 07:36:46
tags:
- Golang
---

## 背景

最近在刷 Twitter 的时候，发现 Twitter 会实时更新已加载页面的内容，以为是 Websocket，看了下请求发现是 Server-sent events，之前没有了解过这个，今天来学习一下。

## Server-sent events

引用维基百科：

> Server-Sent Events (SSE) is a server push technology enabling a client to receive automatic updates from a server via HTTP connection. The Server-Sent Events EventSource API is standardized as part of HTML5[1] by the W3C. 


SSE 通常与 Websocket 相比较：
* SSE 提供单向通信，Websocket 提供双向通信；
* SSE 是通过 HTTP 协议实现的，Websocket 是单独的协议；
* 实现上来说 SSE 比较容易，Websocket 复杂一些；
* 对浏览器来说，IE/Edge 不支持 SSE，其它的都是支持的。
* SSE 有最大连接数限制
* WS 可以传输二进制数据和文本数据，而 SSE 只有文本数据

SSE 使用场景：
* 股票行情自动收录
* 社交网站自动更新（Twitter）
* ...

Websocket 使用场景：
* VNC
* 协同编辑
* ...



## 使用

Golang 有 [eventsource](https://github.com/antage/eventsource) 可以直接使用，示例如下：

### Server

```go
package main

import (
        "gopkg.in/antage/eventsource.v1"
        "log"
        "net/http"
        "time"
)

func main() {
        es := eventsource.New(nil, nil)
        defer es.Close()
        http.Handle("/", http.FileServer(http.Dir("./public")))
        http.Handle("/events", es)
        go func() {
                for {
                        // 每 2 秒发送一条消息，并打印对应客户端数量
                        es.SendEventMessage("hello", "", "")
                        log.Printf("Hello has been sent (consumers: %d)", es.ConsumersCount())
                        time.Sleep(2 * time.Second)
                }
        }()
        log.Print("Open URL http://localhost:8080/ in your browser.")
        err := http.ListenAndServe(":8080", nil)
        if err != nil {
                log.Fatal(err)
        }
}
```


### Client

```html
<!DOCTYPE html>
<html>
  <head>
    <title>SSE test</title>
    <script type="text/javascript">
      window.addEventListener("DOMContentLoaded", function () {
        var evsrc = new EventSource("/events");
        evsrc.onmessage = function (ev) {
          document.getElementById("log")
            .insertAdjacentHTML("beforeend", "<li>" + ev.data + "</li>");
        }
        evsrc.onerror = function (ev) {
          console.log("readyState = " + ev.currentTarget.readyState);
        }
      })
    </script>
  </head>
  <body>
    <h1>SSE test</h1>
    <div>
      <ul id="log">
      </ul>
    </div>
  </body>
</html>
```

## 总结

SSE 很适合 Twitter 这种场景，还特意观察了下微博，发现微博没有。。


## 参考链接

* https://stackoverflow.com/questions/5195452/websockets-vs-server-sent-events-eventsource