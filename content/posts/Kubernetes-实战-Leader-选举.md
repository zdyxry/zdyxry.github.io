---
title: Kubernetes 实战-Leader 选举
date: 2019-09-12 22:05:22
tags:
- Kubernetes
---

## 背景

最近手头上的 Cluster-API 的项目要告一段落， Cluster-API 发布了 [v0.2.1 版本](https://github.com/kubernetes-sigs/cluster-api/releases/tag/v0.2.1) ，正式放出了 YAML 配置文件，看到了点有意思的事情，觉得需要记录一下。

## K8S Leader

看过之前 K8S 实战系列的朋友应该记得我写过一篇 [K8S 高可用部署](https://zdyxry.github.io/2019/06/15/Kubernetes-%E5%AE%9E%E6%88%98-%E9%AB%98%E5%8F%AF%E7%94%A8%E9%9B%86%E7%BE%A4%E9%83%A8%E7%BD%B2/)的文章，在文章中只是讲了具体的操作步骤，没有提到 k8s 是如何保证自己多个组件之间协作的。

我们这里有一个 3 个master 节点的集群：

```shell
[root@node70 21:01:01 ~]$kubectl get node
NAME     STATUS   ROLES    AGE   VERSION
node70   Ready    master   64d   v1.15.0
node71   Ready    master   64d   v1.15.0
node72   Ready    master   64d   v1.15.0
```

我们都知道 k8s 核心组件，其中 apiserver 只用于接收 api 请求，不会主动进行各种动作，所以他们在每个节点都运行并且都可以接收请求，不会造成异常；kube-proxy 也是一样，只用于做端口转发，不会主动进行动作执行。

但是 scheduler, controller-manager 不同，他们参与了 Pod 的调度及具体的各种资源的管控，如果同时有多个 controller-manager 来对 Pod 资源进行调度，结果太美不敢看，那么 k8s 是如何做到正确运转的呢？

k8s 所有功能都是通过 `services` 对外暴露接口，而 `services` 对应的是具体的 `endpoints` ，那么来看下 scheduler 和 controller-manager 的 `endpoints` 是什么：

```shell
[root@node70 21:04:46 ~]$kubectl -n kube-system describe endpoints kube-scheduler
Name:         kube-scheduler
Namespace:    kube-system
Labels:       <none>
Annotations:  control-plane.alpha.kubernetes.io/leader:
                {"holderIdentity":"node70_ed12bf09-7aa3-47d6-9546-97752bb589b5","leaseDurationSeconds":15,"acquireTime":"2019-09-11T05:31:58Z","renewTime"...
Subsets:
Events:  <none>
[root@node70 21:05:25 ~]$kubectl -n kube-system describe endpoints kube-controller-manager
Name:         kube-controller-manager
Namespace:    kube-system
Labels:       <none>
Annotations:  control-plane.alpha.kubernetes.io/leader:
                {"holderIdentity":"node71_c8deeaea-2d66-4459-90ee-65c28563062f","leaseDurationSeconds":15,"acquireTime":"2019-09-12T12:44:15Z","renewTime"...
Subsets:
Events:
  Type    Reason          Age   From                     Message
  ----    ------          ----  ----                     -------
  Normal  LeaderElection  22m   kube-controller-manager  node71_c8deeaea-2d66-4459-90ee-65c28563062f became leader
  ```

  可以看到关键字 `control-plane.alpha.kubernetes.io/leader` ，这两个组件是通过 leader 选举来从集群中多个节点选择一个执行具体动作，如果我们去看 `/etc/kubernetes/manifests/` 下的配置文件，会看到这行配置：

  ```yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    component: kube-controller-manager
    tier: control-plane
  name: kube-controller-manager
  namespace: kube-system
spec:
  containers:
  - command:
    - kube-controller-manager
    - --allocate-node-cidrs=true
...
    - --leader-elect=true
  ```

通过在 YAML 中添加 `leader-elect=true` 来决定是否进行选主逻辑。而这个参数也是在执行 `kubeadm` 部署集群时就自动配置好了，无需手动配置。

## Deployment Leader

我们先来说说 Deployment，Deployment 是从 ReplicaSet 进化来的，主要增加的功能有滚动更新、回滚、扩容所容等，可以说是我们日常使用 K8S 最常见的资源类型了。

那么当我们通过创建 Deployment 间接创建 ReplicaSet 时，我们有时候并不想所有的 ReplicaSet 中的 Pod 运行统一的逻辑。这时候我们就需要一种方式来选择（通知）某一个 Pod ，来确定这个 Pod 提供特殊功能，其他的 Pod 提供普通功能，也就是跟上述 k8s 实现方式一样，通过Leader 选举完成需求。

Leader 选举有很多方式，或是代码中内嵌选举逻辑，或者通过第三方服务，但是有两个的特点：
1. Leader 在同一时间内是唯一的
2. 当 Leader 所在 Pod 发生异常时，其他 Pod 要可以随时变为 Leader 。


## Leader 选举实现方式

### 代码内嵌选主逻辑

在 Golang 中，k8s client-go 这个package 针对 Leader 相关功能进行了封装，支持3种锁资源，endpoint，configmap，lease，方便使用。

代码仓库：https://github.com/kubernetes/client-go/tree/master/tools/leaderelection

因为这次主要不是说具体实现，再加上我也没看过代码，这里先掠过。

### SideCar

相比于代码中内嵌选主逻辑，使用 sidecar 就不用担心跨语言的问题了，使用起来也简单许多，我们现在用的这个项目实现：https://github.com/kubernetes-retired/contrib/blob/master/election/README.md

使用方式：

```yaml
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
  creationTimestamp: "2019-07-12T07:35:32Z"
  generation: 6
  labels:
    app: yiran-test
  name: yiran-test
  namespace: default
spec:
  selector:
    matchLabels:
      app: yiran-test
  template:
    metadata:
      annotations:
        kubectl.kubernetes.io/restartedAt: "2019-09-09T10:58:51+08:00"
      creationTimestamp: null
      labels:
        app: yiran-test
    spec:
      containers:
      - args:
        - --election=elect-yiran-test
        - --http=0.0.0.0:4444
        image: leader-elector:0.5
        imagePullPolicy: IfNotPresent
        name: leader-elector
      - args:
        ...
```

在 Deployment 或 DaemonSet 中，添加 sidecar 指定端口，最终会在所有的 Pod 中选择一个 Leader 。
在业务代码中，只需要访问端口 4444 ，即可获取当前 Pod 中 Leader 信息，目前是通过 hostname 作为唯一标示的。

如果看了这个项目的代码，会发现它也是使用的 client go 中的实现，只是增加了一层 http server：

```go
func getCurrentLeader(electionId, namespace string, c client.Interface) (string, *api.Endpoints, error) {
	endpoints, err := c.Endpoints(namespace).Get(electionId)
	if err != nil {
		return "", nil, err
	}
	val, found := endpoints.Annotations[leaderelection.LeaderElectionRecordAnnotationKey]
	if !found {
		return "", endpoints, nil
	}
	electionRecord := leaderelection.LeaderElectionRecord{}
	if err := json.Unmarshal([]byte(val), &electionRecord); err != nil {
		return "", nil, err
	}
	return electionRecord.HolderIdentity, endpoints, err
}
```


```go
func main() {
	flags.Parse(os.Args)
	validateFlags()

	kubeClient, err := makeClient()
	if err != nil {
		glog.Fatalf("error connecting to the client: %v", err)
	}

	fn := func(str string) {
		leader.Name = str
		fmt.Printf("%s is the leader\n", leader.Name)
	}

	e, err := election.NewElection(*name, *id, *namespace, *ttl, fn, kubeClient)
	if err != nil {
		glog.Fatalf("failed to create election: %v", err)
	}
	go election.RunElection(e)

	if len(*addr) > 0 {
		http.HandleFunc("/", webHandler)
		http.ListenAndServe(*addr, nil)
	} else {
		select {}
	}
}
```

## 是否开启选举参数

那么我们说了这么多，在实际使用中是否应该开启选举参数呢？
这里要说一下我在文章开头提到的有意思的事情，我们来看下cluster-api 的 YAML 文件：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  ...
spec:
  replicas: 1
  ...
  template:
    metadata:
      ...
    spec:
      containers:
      - args:
        - --enable-leader-election
        command:
        - /manager
        image: us.gcr.io/k8s-artifacts-prod/cluster-api/cluster-api-controller:v0.2.1
        name: manager
        ...
```

创建的资源类型是 Deployment，replicas 设置为1，传递了参数 `--enable-leader-election`，当时我觉得有些奇怪，replicas是1 啊，也就是说一共只有1个 Pod，为啥还要开启 Leader 选举逻辑呢？如果说是为了之后的扩容那可以理解，但是在这份配置文件里，应该完全没必要。把这段配置发给 [liqiang同学](https://liqiang.io/) 看，他也觉得有些怪怪的。

秉着不懂就问的精神，我去 Slack #cluster-api 中提出了我的疑问，得到了以下回复，我格式化一下：

```
@cha： 
it's mostly set for best practice. If you scale up the system will still work. If you don't enable leader election and scale up you will have race conditions


@cha：
but you're right. If you're running a single manager you don't need to enable leader election


@jdetiber:
With a Deployment you do, because on rolling out a change it will spin up the new RS in parallel with the other so there will be 2 pods running at the same time for a short while

```

其中 @cha 的回复跟我预想的差不多，主要处于之后的扩容考虑，需要防止竞争情况出现。但是 @jdetiber 提到了一点很关键，当 Deployment 进行滚动升级的时候，哪怕设置了 Replicas 为1，也会存在短时间同时存在 2 个 Pod 的情况，那么肯定会导致我们的代码逻辑错误，很重要（感叹号）。

## 总结

其实今天这篇文章主要是想记录下上面这段话的，自己在平时使用 k8s 过程中，貌似也仅仅是知道这些功能并使用，真正要开发部分功能时，考虑的边界条件太少了。虽然知道 Deployment 滚动升级会有同时存在 2 个 Pod 的情况，却完全没有想到需要配置 Leader 选举参数来保证代码正确运行，涨知识了。


## 参考链接
* https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ 