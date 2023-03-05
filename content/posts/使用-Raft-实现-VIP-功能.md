---
title: 使用 Raft 实现 VIP 功能
date: 2020-01-17 22:48:28
tags:
- Linux
---

## 背景

在部署应用时想要应用是高可用，通常会在应用前放置一个 HAProxy，当任何一个 Server 故障，HAProxy 会自动切换，但是 HAProxy 也存在单点故障，因此需要多个 HAProxy 来保证业务不中断，这时候我们需要另一个软件配合：Keepalived。通常我用 Keepalived 仅用来提供 VIP，保证当一个 Keepalived 故障，VIP 自动在其他 Keepalived 节点配置。

Keepalived 有一个问题是 virtual route ID 必须是同一网段内唯一的，当我们想要在一个网段内部署多个集群时，就需要人为的介入去分配 virtual route ID，不方便。这次来使用 Raft 自己实现 VIP 逻辑。

## hashicorp/raft

Raft 有很多开源实现，其中 Hashicorp 实现的 [Raft 库](https://github.com/hashicorp/raft) 已经被 Consul 等软件使用，且接口友善，选择使用它来实现。在 Github 上有很多 Raft 的使用示例，比较简单且完整的是 [otoolep/hraftd](https://github.com/otoolep/hraftd)，我们来看看他是怎么使用的。

### otoolep/hraftd

#### main.go

在 main.go 中主要做了 4 件事情：`store.New`, `store.Open`, `http.New`, `http.Start`，先来看看程序是如何启动的：

```go
func init() {
    // 设置命令行参数
	flag.BoolVar(&inmem, "inmem", false, "Use in-memory storage for Raft")
	...
	flag.Usage = func() {
		fmt.Fprintf(os.Stderr, "Usage: %s [options] <raft-data-path> \n", os.Args[0])
		flag.PrintDefaults()
	}
}

func main() {
    // 解析命令行参数
	flag.Parse()
    ...
    // 创建一个 Store 对象
	s := store.New(inmem)
	s.RaftDir = raftDir
    s.RaftBind = raftAddr
    // 运行 Store 
	if err := s.Open(joinAddr == "", nodeID); err != nil {
		log.Fatalf("failed to open store: %s", err.Error())
	}
    // 新建一个 http 对象并运行
	h := httpd.New(httpAddr, s)
	if err := h.Start(); err != nil {
		log.Fatalf("failed to start HTTP service: %s", err.Error())
	}

	// 如果 joinAddr 参数不为空，则处理 join 请求
	if joinAddr != "" {
		if err := join(joinAddr, raftAddr, nodeID); err != nil {
			log.Fatalf("failed to join node at %s: %s", joinAddr, err.Error())
		}
	}

	log.Println("hraftd started successfully")
    // 监听系统信号，若接收到 os.Interrupt 则程序退出
	terminate := make(chan os.Signal, 1)
	signal.Notify(terminate, os.Interrupt)
	<-terminate
	log.Println("hraftd exiting")
}
```

#### http

看了 main.go 我们知道调用了 `http.Start`， 先不管 Store 是什么，先来看看 http 相关实现：

```go
// Start starts the service.
func (s *Service) Start() error {
    // Service 实现了 ServeHTTP 方法
	http.Handle("/", s)
	go func() {
		err := server.Serve(s.ln)
    ...
}
```

```go
func (s *Service) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if strings.HasPrefix(r.URL.Path, "/key") {
		s.handleKeyRequest(w, r)
    // 先忽略其他分支
}
```

主要处理请求的是 `s.handleKeyRequest` 方法：

```go
func (s *Service) handleKeyRequest(w http.ResponseWriter, r *http.Request) {
	...
	switch r.Method {
	case "GET":
		k := getKey()
		if k == "" {
			w.WriteHeader(http.StatusBadRequest)
		}
		v, err := s.store.Get(k)
		...
		io.WriteString(w, string(b))
	case "POST":
		// Read the value from the POST body.
		m := map[string]string{}
		if err := json.NewDecoder(r.Body).Decode(&m); err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}
		for k, v := range m {
			if err := s.store.Set(k, v); err != nil {
				w.WriteHeader(http.StatusInternalServerError)
				return
			}
        }
    ...
```

在 `s.handleKeyRequest` 中根据请求方法，去调用 store 对应的方法，那么 store 实现了哪些接口呢？这也是在 http 模块中定义的：

```go
type Store interface {
	Get(key string) (string, error)
	Set(key, value string) error
	Delete(key string) error
	Join(nodeID string, addr string) error
}
```

除了 Join 看着比较奇怪，其他的都是一个 K/V 系统该有的接口，接下来就看看 Store 具体方法的实现。

#### store

这个模块的编写涉及到了 Raft 中的具体概念，建议先阅读 siddontang 写的 Raft 相关博客快速了解（链接在参考链接列出）。

以下以设置 Key 为例：

```go
func (s *Store) Set(key, value string) error {
	if s.raft.State() != raft.Leader {
		return fmt.Errorf("not leader")
	}

    // 封装具体执行的动作
	c := &command{
		Op:    "set",
		Key:   key,
		Value: value,
	}
	b, err := json.Marshal(c)
    ...
    // 将 command 应用于 FSM
	f := s.raft.Apply(b, raftTimeout)
	return f.Error()
}
```

查看 FSM Apply 方法实现：
```go
// Apply applies a Raft log entry to the key-value store.
func (f *fsm) Apply(l *raft.Log) interface{} {
	var c command
	// 根据操作动作的不同，执行不同的方法，这里以设置 Key 为例
	switch c.Op {
	case "set":
		return f.applySet(c.Key, c.Value)
	...
	}
}
```

```go
func (f *fsm) applySet(key, value string) interface{} {
    // 互斥锁
    f.mu.Lock()
    defer f.mu.Unlock()
    // 设置 Map 中的 Key/Value
	f.m[key] = value
	return nil
}
```

#### raft

看了上面的具体动作实现，接下来看看 Raft 具体启动：

```go
func (s *Store) Open(enableSingle bool, localID string) error {
	// 设置 Raft 配置
	config := raft.DefaultConfig()
	config.LocalID = raft.ServerID(localID)
    // 设置 Raft 通信
	addr, err := net.ResolveTCPAddr("tcp", s.RaftBind)
    ...
	transport, err := raft.NewTCPTransport(s.RaftBind, addr, 3, 10*time.Second, os.Stderr)
    // 设置 Raft 存储对象
	snapshots, err := raft.NewFileSnapshotStore(s.RaftDir, retainSnapshotCount, os.Stderr)
	var logStore raft.LogStore
	var stableStore raft.StableStore
	if s.inmem {
		logStore = raft.NewInmemStore()
		stableStore = raft.NewInmemStore()
	} else {
		boltDB, err := raftboltdb.NewBoltStore(filepath.Join(s.RaftDir, "raft.db"))
		if err != nil {
			return fmt.Errorf("new bolt store: %s", err)
		}
		logStore = boltDB
		stableStore = boltDB
	}
    // 创建 raft 示例，并使用该 raft 实例启动集群
	ra, err := raft.NewRaft(config, (*fsm)(s), logStore, stableStore, snapshots, transport)
	if err != nil {
		return fmt.Errorf("new raft: %s", err)
	}
	s.raft = ra
	if enableSingle {
		...
		ra.BootstrapCluster(configuration)
	}
}
```

这里可以看到 Raft 所需接口为 FSM 和 Snapshot，具体的实现方式根据需求来实现，一般与 hraftd 相仿，大概了解了 hashicorp/raft 的使用，那么我们来实现具体的 VIP 功能。


## VIP

### network

既然是跟 IP 相关，那么肯定需要给对应网卡配置时间，在 Linux 中我们可以通过 `ip` 命令来设置，Golang 中使用 [vishvananda/netlink](https://github.com/vishvananda/netlink) 来实现。

 `netlink.AddrAdd` 可以在指定的网络设备上添加 IP 地址。

```go
func (nc *NetworkConfig) addIP() error {
	res, err := nc.IsSet()
	if err != nil {
		return errors.Wrap(err, "ip check in AddIP failed")

	}
	if res {
		return nil
	}
	if err := netlink.AddrAdd(nc.link, nc.address); err != nil {
		return errors.Wrap(err, "could not add ip")
	}
	return nil
}
```

`netlink.AddrDel` 可以将 IP 从指定网络设备上删除：

```go
func (nc *NetworkConfig) delIP() error {
	res, err := nc.IsSet()
	if err != nil {
		return errors.Wrap(err, "ip check in DelIP failed")
	}

	if !res {
		return nil
	}

	if err := netlink.AddrDel(nc.link, nc.address); err != nil {
		return errors.Wrap(err, "could not delete ip")
	}

	return nil
}
```

### raft

实现了 IP 设置相关，我们不需要提供 HTTP 接口，直接编写 Raft 相关实现，跟 hraftd 实现不同，在 hraftd 中需要进行信息写入读取，而我们的 VIP 仅依赖于 Raft 选举 Leader，所以只需要编写好对应的方法，不需要做额外操作：

```go
type FSM struct {
}

func (fsm FSM) Apply(log *raft.Log) interface{} {
	return nil
}

func (fsm FSM) Restore(snap io.ReadCloser) error {
	return nil
}

func (fsm FSM) Snapshot() (raft.FSMSnapshot, error) {
	return Snapshot{}, nil
}

type Snapshot struct {
}

func (snapshot Snapshot) Persist(sink raft.SnapshotSink) error {
	return nil
}

func (snapshot Snapshot) Release() {
}
```

### serve

基础方法都已经实现了，那么接下来编写集群启动逻辑：

```go
func (manager *VIPManager) Start() error {
	// 初始化 raft 配置、存储对象、通信
	for id, ip := range manager.peers {
		configuration.Servers = append(configuration.Servers, raft.Server{ID: raft.ServerID(id), Address: raft.ServerAddress(ip)})
	}

	// 启动 Raft 集群，这里与 hraftd 不同，需要注意
	if error := raft.BootstrapCluster(config, logStore, stableStore, snapshots, transport, configuration); error != nil {
		return error
	}

	// 创建 raft 实例
	raftServer, error := raft.NewRaft(config, manager.fsm, logStore, stableStore, snapshots, transport)
    ...
	ticker := time.NewTicker(time.Second)
	isLeader := false
    // 服务启动时先删除 VIP，防止集群中同时存在节点都配置了 VIP
	manager.deleteIP(false)
	go func() {
		for {
			select {
            // 如果 当前节点是 Leader 节点，则设置 VIP
			case leader := <-raftServer.LeaderCh():
				if leader {
					isLeader = true
					log.Info("Leading")
					manager.addIP(true)

                }
            // 定时检测，如果是 Leader，则检测 VIP 是否正确设置，如果没有就再次配置 VIP
			case <-ticker.C:
				if isLeader {
					result, error := manager.networkConfigurator.IsSet()
					if error != nil {
						log.WithFields(log.Fields{"error": error, "ip": manager.networkConfigurator.IP(), "interface": manager.networkConfigurator.Interface()}).Error("Could not check ip")
					}

					if result == false {
						log.Error("Lost IP")

						manager.addIP(true)
					}
				}
            ...
			}
		}
	}()
}
```

这里与 hraftd 的实现不同，hraftd 先实例 raft，然后使用该 raft 实例启动集群，这样做的好处是哪怕集群只有一个节点，就是第一个节点，那么集群也是可以正常工作的，坏处是集群启动顺序是固定的，必须要先启动第一个节点，然后其他节点通过 Join 请求添加到 Raft 集群中（我们忽略了 Join 的走读）。

重新想一下我们的需求：集群、高可用、故障。当这几个词放在一起，我们就知道 hraftd 的方法不适合我们，有以下原因：
1. 集群节点启动顺序要求
2. 各个节点配置文件不同，有的需要 Join 参数

所以我们是直接使用 `raft.BootstrapCluster` 来启动集群，虽然只有一个节点集群无法正常工作，但是这个是可以容忍的。

### ARP

在实现完上述功能后，我以为大功告成了，就开始自测，但是测试过程中发现了很诡异的现象，虽然我们通过 Raft 自身选举实现了 VIP 的故障自动漂移，但是实际测试中发现业务访问随着 VIP 的重建并没有立即恢复，，检查 ARP 记录发现集群中各个节点关于 VIP 的 ARP 记录各不相同，甚至是完全不同。

我们来重温下 ARP 协议内容：

> 地址解析协议（英語：Address Resolution Protocol，缩写：ARP）是一个通过解析网络层地址来找寻数据链路层地址的网络传输协议，它在IPv4中极其重要。ARP最初在1982年的RFC 826（征求意见稿）[1]中提出并纳入互联网标准 STD 37. ARP 也可能指是在多数操作系统中管理其相关地址的一个进程。

> 在以太网协议中规定，同一局域网中的一台主机要和另一台主机进行直接通信，必须要知道目标主机的MAC地址。而在TCP/IP协议中，网络层和传输层只关心目标主机的IP地址。这就导致在以太网中使用IP协议时，数据链路层的以太网协议接到上层IP协议提供的数据中，只包含目的主机的IP地址。于是需要一种方法，根据目的主机的IP地址，获得其MAC地址。这就是ARP协议要做的事情。所谓地址解析（address resolution）就是主机在发送帧前将目标IP地址转换成目标MAC地址的过程。

如果 VIP 与真实节点对应的 MAC 地址不同，就相当于 ARP 攻击了，所以我们的 Leader 节点设置完 VIP 后，还需要发送 ARP 请求广播，告诉广播域中的其他节点 VIP 正确的 MAC 地址。采用的方式是 gratuitous ARP（免费 ARP）。这里我们直接找一个开源的 ARP 实现来完成这个需求：

[google/seesaw](https://github.com/google/seesaw) 是一个负载均衡器，里面实现了这个功能：

```go
// ARPSendGratuitous sends a gratuitous ARP message via the specified interface.
func (ncc *SeesawNCC) ARPSendGratuitous(arp *ncctypes.ARPGratuitous, out *int) error {
	iface, err := net.InterfaceByName(arp.IfaceName)
	if err != nil {
		return fmt.Errorf("failed to get interface %q: %v", arp.IfaceName, err)
	}
	log.V(2).Infof("Sending gratuitous ARP for %s (%s) via %s", arp.IP, iface.HardwareAddr, iface.Name)
	m, err := gratuitousARPReply(arp.IP, iface.HardwareAddr)
	if err != nil {
		return err
	}
	return sendARP(iface, m)
}
```

## 总结

使用 hashicorp/raft 可以很简单方便的实现需要选举 Leader 的分布式应用，虽然我司的 Slogan 是 `Make IT Simple` ，但是愈发感觉 Hashicorp 才是这句话的忠实体现，他们的 Terraform、Vault、Consul、Nomad、Vagrant 等软件，都是让基础设施的适用与管理更简单方便的，还是很爽的。

本文的具体实现在 [sparrow](https://github.com/zdyxry/sparrow) 可以看到。


## 参考链接
* https://www.jianshu.com/p/138b4d267084
* https://www.jianshu.com/p/2b60542640e2
* https://www.jianshu.com/p/1bbd7162727d
* https://www.jianshu.com/p/99562bfec5c2
* https://zh.wikipedia.org/wiki/%E5%9C%B0%E5%9D%80%E8%A7%A3%E6%9E%90%E5%8D%8F%E8%AE%AE
* https://github.com/darxkies/virtual-ip/blob/master/pkg/manager.go