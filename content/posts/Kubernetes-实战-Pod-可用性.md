---
title: Kubernetes 实战-Pod 可用性
date: 2019-06-26 21:57:31
tags:
- Kubernetes
---

## 背景

Kubernetes 作为一个容器编排系统，负责 Pod 生命周期管理，那么肯定会保证 Pod 的可用性，今天来说下 k8s Pod 可用性相关知识。


## K8S 可用性相关参数

k8s 核心组件有 kubelet,kube-apiserver,kube-scheduler,kube-controller-manager，通过阅读官方文档中相关参数说明，我摘取了认为跟可用性相关的参数，具体列表如下：


### kubelet

#### --housekeeping-interval duration   

Default: 10s

Interval between container housekeepings.

kubelet 主动检测容器资源是否达到阈值的周期。


#### --node-status-update-frequency duration                                        

Default: 10s

Specifies how often kubelet posts node status to master. Note: be cautious when changing the constant, it must work with nodeMonitorGracePeriod in nodecontroller. 

kubelet 上报到 kube-apiserver 频率。



### kube-controller-manager 


#### --node-eviction-rate float32

Default: 0.1 

Number of nodes per second on which pods are deleted in case of node failure when a zone is healthy (see --unhealthy-zone-threshold for definition of healthy/unhealthy). Zone refers to entire cluster in non-multizone clusters.

当 kube-controller-manager 判定节点故障，开始迁移（重建）pod 的速度，默认是 0.1，也就是 1Pod/10s 。


#### --node-monitor-grace-period duration

Default: 40s 

Amount of time which we allow running Node to be unresponsive before marking it unhealthy. Must be N times more than kubelet's nodeStatusUpdateFrequency, where N means number of retries allowed for kubelet to post node status.

kube-controller-manager 标记 kubelet(node) 为不健康的周期。


#### --node-monitor-period duration

Default: 5s 

The period for syncing NodeStatus in NodeController.

kube-controller-manager 定期检查 kubelet(node) 状态周期。


#### --node-startup-grace-period duration

Default: 1m0s 
 
Amount of time which we allow starting Node to be unresponsive before marking it unhealthy.

kube-controller-manager 在标记节点为不健康之前允许无响应时间。

#### --pod-eviction-timeout duration

Default: 5m0s 

The grace period for deleting pods on failed nodes.

kube-controller-manager 判定节点故障，重建 Pod 的超时时间。


## 具体流程

看完了相关参数，我们来看下 kubelet 和 kube-controller-manager 是如何相互关联工作来保证 Pod 可用性的。

1. kubelet 启动，若启动时间超过 node-startup-grace-period，则 kube-controller-manager 将其置为 unhealthy

2. kubelet 按照 --node-status-update-frequency 周期，定时与 kube-apiserver 通信将其状态记录到 etcd

3. 若 kubelet 无法连接到 kube-apiserver，那么 kubelet 会尝试 nodeStatusUpdateRetry 次更新状态信息

4. kube-controller-manager 按照 --node-monitor-period 周期，定时从 etcd 中获取 kubelet 状态

5. 若 kubelet 在 --node-monitor-grace-period 周期内均为非健康状态（这里如果 kubelet 未更新状态，等同），则该节点更新为 NotReady，将需要迁移（重建）的资源放置到队列中

6. 当 kubelet NotReady 的 --pod-eviction-timeout 时间后， kube-controller-manager 开始进行 Pod 驱逐动作

7. 驱逐速度为 --node-eviction-rate ，即每10s 迁移（重建）1个 Pod


需要注意的是，上述 kubelet 和 kube-controller-manager 的操作是异步的，中间任何一个更新步骤都有可能出现延迟的情况，所以真实情况会比上述流程复杂（诡异）的多。比如 lijieao 的[最新博客](https://www.lijiaocn.com/%E9%97%AE%E9%A2%98/2019/05/27/kubernetes-node-frequently-not-ready.html)中碰到的因为磁盘 IO 压力导致 kubelet NotReady 的情况，都是有可能出现的。


按照上面的流程，可以看到，当我们节点故障后，要花费 5min 的时间才会重建我们的业务，这种情况下大部分对稳定性要求较高的业务都无法忍受的，所以有同学可能会考虑修改默认配置，来减少业务宕机时间。

上述提到的参数的默认值，肯定是 k8s 社区经过多年的架构设计（或者经验？）的。之前看过社区中关于这部分的一篇文章提到，不建议修改默认的配置，担心修改了默认配置可能因为其他一些比较微小的故障导致 Pod 频繁的迁移，这是我们不想看到的。

上面提到的情况都是说：当节点发生故障后，我们希望我们的 Pod 能够第一时间迁移到正常运行的节点，那么有没有反过来的，不想迁移的呢？

其实是有的，比如有状态服务配合 kubelet 服务故障场景。我们的节点正常运行的情况下，容器运行时也都正常工作，唯独 kubelet 故障了，那么我们想想此时发生了什么？ 

kube-controller-manager 在一段时间后标记节点故障，开始迁移（重建） Pod 操作，但是要注意，此时因为是有状态服务，而节点上的容器又在正常运行，kubelet 由于故障了，k8s 无法直接操作节点上的容器，只能在其他节点进行重建。这时候问题就出现了，集群中存在2个 Pod 同时读写一个 PV，这种错误是致命的。

在这种场景下，我们想要追求的是哪怕节点故障了，我们也要尽量的不迁移 Pod，来保证我们数据的读写正常。

那么上述情况我们应该怎么解决呢？ 

## 总结

Operator 是一种方式。在 Operator 出现之前，有状态服务的运维工作都是靠着探针或者其他的基础运维工具来完成的，很多工作即使做到了自动化也不完美，现在有了 Operator 结合 CRD，我们完全可以自己在应用层面监控服务状态，从而主动的触发 Pod 的迁移（重建），保证我们业务的稳定。

另一种解决方式是 `Taint based Evictions`，在 1.13 版本中增加了该配置，我们可以在创建资源的时候，指定规则配置Pod 容忍节点异常的时间，加快触发 Pod 重建，这大大减缓了对集群配置的要求。

## 测试 YAML

在测试 Pod 可用性的时候，我们必须创建 Deployment、RS 类型资源，单纯的 Pod 资源是不被保证可用性的。同时我们也想观察 DaemonSet Pod 在节点故障场景下的表现，所以一同创建了。可以使用以下 YAML 用来创建测试环境。

```yaml
[root@m1 ha]# cat ha.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: busybox
  namespace: default
spec:
  replicas: 6
  selector:
    matchLabels:
      app: busybox
  template:
    metadata:
      labels:
        app: busybox
    spec:
      tolerations:
      - key: node-role.kubernetes.io/master
        effect: NoSchedule
      - key: "node.kubernetes.io/unreachable"
        operator: "Exists"
        effect: "NoExecute"
        tolerationSeconds: 2
      - key: "node.kubernetes.io/not-ready"
        operator: "Exists"
        effect: "NoExecute"
        tolerationSeconds: 2
      containers:
      - image: busybox
        command:
        - sleep
        - "3600"
        imagePullPolicy: IfNotPresent
        name: busybox
      restartPolicy: Always
---

apiVersion: "apps/v1beta1"
kind: Deployment
metadata:
  name: "dp"
  namespace: "default"
spec:
  replicas: 6
  template:
    metadata:
      labels:
        app: dp
    spec:
      tolerations:
      - key: node-role.kubernetes.io/master
        effect: NoSchedule
      containers:
      - name: "dp"
        image: "busybox:latest"
        command:
        - "/bin/sh"
        - "-c"
        - |
          set -o errexit
          set -o xtrace
          while true
          do
            sleep 2s
            date
          done

---
apiVersion: "extensions/v1beta1"
kind: "DaemonSet"
metadata:
  name: "ds"
  namespace: "default"
spec:
  template:
    metadata:
      labels:
        app: ds
    spec:
      tolerations:
      - key: node-role.kubernetes.io/master
        effect: NoSchedule
      containers:
      - name: "apply-sysctl"
        image: "busybox:latest"
        command:
        - "/bin/sh"
        - "-c"
        - |
          set -o errexit
          set -o xtrace
          while true
          do
            sleep 2s
            date
            echo "diu~"
          done
```




## 参考链接

https://github.com/Kevin-fqh/learning-k8s-source-code/blob/master/kubelet/(05)kubelet%E8%B5%84%E6%BA%90%E4%B8%8A%E6%8A%A5%26Evition%E6%9C%BA%E5%88%B6.md

https://github.com/kubernetes-sigs/kubespray/blob/master/docs/kubernetes-reliability.md

https://www.lijiaocn.com/%E9%97%AE%E9%A2%98/2019/05/27/kubernetes-node-frequently-not-ready.html#%E8%A7%82%E5%AF%9F-kubelet-%E8%BF%9B%E7%A8%8B%E7%8A%B6%E6%80%81


