---
title: 基于 Yamux 的内网穿透简易实现
date: 2022-02-09 11:57:51
tags:
- Golang
---


## 基于 Yamux 的内网穿透简易实现


### Server

模拟真实服务器，假设运行在内网环境，端口 8881。

```
package main

import (
    "fmt"
    "log"
    "net/http"
)

func main() {

    http.HandleFunc("/hello", HelloHandler)
    fmt.Println("Server started at port 8881")
    log.Fatal(http.ListenAndServe(":8881", nil))
}

func HelloHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, there\n")
}
```

### Hub

运行在公网环境的 Hub，用于 Agent 连接，并保持会话。端口 8882。

提供 session 管理机制，主要用来保存 Yamux session 和 Agent 对应关系。
每个内网可以运行多个 Agent，每次新建连接会从已有的 Agent session 列表中随机选择一个 session，并通过创建一个新的 Yamux Stream 机制复用连接。

```go
type SessionManager interface {
	AddSession(key string, sess *yamux.Session)
	DialTarget(key string) (net.Conn, error)
}

func NewSessionManager() SessionManager {
	return &sessionManager{
		sessions: map[string][]*yamux.Session{},
	}
}

type sessionManager struct {
	sessions map[string][]*yamux.Session
	mutex    sync.Mutex
}

func (m *sessionManager) AddSession(key string, sess *yamux.Session) {
	m.mutex.Lock()
	defer m.mutex.Unlock()

	curr := m.sessions[key]
	if curr == nil {
		curr = []*yamux.Session{}
	}
	curr = append(curr, sess)
	m.sessions[key] = curr
}

func (m *sessionManager) DialTarget(key string) (net.Conn, error) {
	m.mutex.Lock()
	defer m.mutex.Unlock()

	ss := m.sessions[key]
	for {
		if len(ss) == 0 {
			return nil, fmt.Errorf("no session found in '%s'", key)
		}

		idx := rand.Intn(len(ss))
		conn, err := ss[idx].Open()
		if err != nil {
			log.Printf("removing session #%d of '%s' due to dial error: %s", idx, key, err)
			ss[idx].Close()
			ss = append(ss[:idx], ss[idx+1:]...)
			m.sessions[key] = ss
			continue
		}
		log.Printf("find session with key '%s'", key)
		return conn, nil
	}
}
```

Hub 自身暴露两个 API 接口，其中 `/api/v1/hubs/:id` 用于 Agent 建立 WebSocket 连接，`api/v1/proxy/:id/*proxyPath` 用于后续 Client 通过 Hub 访问 Server 。当用户访问 `/api/v1/proxy/` 并指定 Agent ID 时，通过`NewSingleHostReverseProxy` 创建反向代理，并指定 Transport 中的 conn 为 Yamux Stream。

```go
func SetupHandlers(r *gin.RouterGroup) {
	m := NewSessionManager()

	r.GET("/hubs/:id", func(c *gin.Context) {
		upgrader := websocket.Upgrader{
			ReadBufferSize:  1024,
			WriteBufferSize: 1024,
		}
		conn, err := upgrader.Upgrade(c.Writer, c.Request, nil)
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"msg": fmt.Sprintf("failed to upgrade to WebSocket: %s", err)})
			return
		}

		session, err := yamux.Server(conn.UnderlyingConn(), nil)
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"msg": fmt.Sprintf("failed to multiplex channel: %s", err)})
			return
		}

		m.AddSession(c.Param("id"), session)
	})

	r.Any("/proxy/:id/*proxyPath", func(c *gin.Context) {
		u, err := url.Parse("http://127.0.0.1")
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"msg": err.Error()})
			return
		}

		rp := httputil.NewSingleHostReverseProxy(u)
		key := c.Param("id")
		rp.Transport = &http.Transport{
			DialContext: func(ctx context.Context, network string, addr string) (net.Conn, error) {
				conn, err := m.DialTarget(key)
				return conn, err
			},
		}
		rp.ErrorHandler = func(w http.ResponseWriter, r *http.Request, err error) {
			c.JSON(http.StatusBadRequest, gin.H{"msg": err.Error()})
		}

		hostInQuery, exist := c.GetQuery("x-proxy-host")
		if exist == true {
			c.Request.Header.Add("X-Proxy-Host", hostInQuery)
		}
		c.Request.Header.Add("X-Proxy-Path", c.Param("proxyPath"))
		rp.ServeHTTP(c.Writer, c.Request)
	})
}


func setupRouter() (*gin.Engine, error) {
	r := gin.Default()

	v1 := r.Group("/api/v1")
	SetupHandlers(v1)

	return r, nil
}

```


### Agent

内网可以运行多个 Agent 用于连接 Hub，Agent 会通过 WebSocket 连接 Hub，后续所有通信均通过该连接进行传输。在连接建立后，创建 ReverseProxy，配置 Direcotr 修改 Request 参数，指定 host,path。


```go
func Setup(connectURL string) error {
	dialer := websocket.DefaultDialer
	dialer.TLSClientConfig = &tls.Config{
		InsecureSkipVerify: true,
	}
	wsConn, _, err := dialer.Dial(connectURL, nil)
	if err != nil {
		return errors.New(fmt.Sprintf("failed to dial hub %q: %s", connectURL, err))
	}

	sess, err := yamux.Client(wsConn.UnderlyingConn(), nil)
	if err != nil {
		return errors.New(fmt.Sprintf("failed to create multiplex channel: %s", err))
	}
	log.Println("connected to hub")

	director := func(req *http.Request) {
		log.Println(req)
		host := req.Header.Get("X-Proxy-Host")
		path := req.Header.Get("X-Proxy-Path")
		req.Header.Add("X-Forwarded-Host", req.Host)
		req.Header.Add("X-Origin-Host", host)
		req.URL.Scheme = "http"
		req.URL.Host = host
		req.URL.Path = path
		req.Host = ""
		log.Println(req)
	}

	proxy := &httputil.ReverseProxy{Director: director}
	server := &http.Server{
		Handler: proxy,
	}

	idleConnsClosed := make(chan struct{})
	go func() {
		sigint := make(chan os.Signal, 1)
		signal.Notify(sigint, os.Interrupt)
		signal.Notify(sigint, syscall.SIGTERM)
		<-sigint

		if err := server.Shutdown(context.Background()); err != nil {
			log.Printf("failed to shutdown server: %s", err)
		}
		close(idleConnsClosed)
	}()

	log.Println("starting proxy")
	if err := server.Serve(sess); err != nil {
		return errors.New(fmt.Sprintf("error running proxy: %s", err))
	}

	<-idleConnsClosed

	return nil
}
```


### Client

Client 可以通过访问 Hub 的 proxy API，将真实请求转发至 Agent ，再由 Agent 请求 Server。

### 完整流程

1. 运行 Hub 对外提供服务
2. 运行 Agent 通过 WebSocket 连接至 Hub，并创建 ReverseProxy
3. Client 请求 Hub proxy API
4. Hub 在已有 Session（WebSocket）上 Yamux Stream 将请求转发至 Agent
5. Agent 解析 Request，并将请求转发至 Server，返回

### 参考链接

* https://github.com/hashicorp/yamux
* https://github.com/smartxworks/kopilot
* https://gist.github.com/fengye87/76791723511f6867b02723ba0c437315
* https://stackoverflow.com/questions/60657906/websocket-over-yamux-over-websocket-not-working
