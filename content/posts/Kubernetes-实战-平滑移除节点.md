---
title: Kubernetes 实战-平滑移除节点
date: 2019-08-01 23:07:29
tags:
- Kubernetes
---

## 背景 

自己玩 K8S 以来，搭建的环境没有10几套，也有5，6套了，当环境测试完成后，基本上直接删除掉了，也没有想着一直维护，最近在维护一个集群的时候，想要删除一个节点，发现自己一直不知道如何删除节点，特此记录。


## 平滑移除

### 获取节点列表

```bash
kubectl get node
```

### 设置不可调度

由于节点目前处于正常工作状态，集群中新建资源还是有可能创建到该节点的，所以先将节点设置为不可调度：

```bash
kubectl cordon $node_name
```

### 将节点上资源调度到其他节点

目前集群已经不会分配新的资源在该节点上了，但是节点还运行着现有的业务，所以我们需要将节点上的业务分配到其他节点：

```bash
kubectl drain $node_name
```

注意：DaemonSet Pod 和 Static Pod 是不会在集群中其他节点重建的。

### 移除节点

当前集群中已经没有任何资源分配在节点上了，那么我们可以直接移除节点：

```bash
kubectl delete $node_name
```


至此，我们平滑移除了一个 k8s 节点。如果移除的是一个 master 节点，那么记得之后还要添加一个新的 master 节点到集群中，避免集群可靠性降低。


## 参考链接

* https://stackoverflow.com/questions/35757620/how-to-gracefully-remove-a-node-from-kubernetes 