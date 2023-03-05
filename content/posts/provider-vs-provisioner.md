---
title: provider vs provisioner
date: 2019-08-17 21:08:46
tags:
- Linux
---

## 背景

之前 liqiang 同学写了一篇博客：[Status 还是 State](https://liqiang.io/post/status-or-state-fa70399e) 用于总结日常工作中遇到的相似词的区别。这两天看代码，经常能够看到两个词：provider 和 provisioner，作为一个英语渣渣，很难准确的理解两个词的区别。

## 字典解释

provider 字典中的解释为：
1. 供应者（商）
2. 提供者（商）
3. 供养人
4. ...

provisioner 字典中的解释为：
1. 粮食供应者

看上去从字面上也是一个意思，那么我们来找个实际场景看看。

## 实际场景

### Terraform

在 Terraform 概念中，同时存在 provider 和 provisioner 两个概念：

```Terraform is used to create, manage, and update infrastructure resources such as physical machines, VMs, network switches, containers, and more. Almost any infrastructure type can be represented as a resource in Terraform.

A provider is responsible for understanding API interactions and exposing resources. Providers generally are an IaaS (e.g. AWS, GCP, Microsoft Azure, OpenStack), PaaS (e.g. Heroku), or SaaS services (e.g. Terraform Cloud, DNSimple, CloudFlare).
```

```
Provisioners are used to execute scripts on a local or remote machine as part of resource creation or destruction. Provisioners can be used to bootstrap a resource, cleanup before destroy, run configuration management, etc.
```

这里的 provider 对应 `供应商` 的含义是可以正确理解的，不同的供应商提供不同的插件。

provisioner 在这里指的是定义的资源可使用的插件，如 `remote-exec`,`file`,`chef` 等等，跟供应商关系不大。


### Vagrant Docker

在搜索过程中，看到有人在 SO 上问了这么个问题 [Vagrant - Docker provider vs. docker provisioner](https://stackoverflow.com/questions/30394707/vagrant-docker-provider-vs-docker-provisioner)

下面的高票回答：

```
Docker provisioner help to prepare environment: build and pull images, run containers if you need multiple containers running for your vagrant machine. Docker provider is running vagrant machine in docker container (instead of VM/cloud as other providers do).
```

虽然感觉说的不是很清楚，但是也可以看出 provider 是有明确分类的，而 provisioner 更像是具体的动作种类，比如创建、删除、更新等。


### CSI

在 k8s CSI 中，也有 provisioner 的概念，这里主要是指具体的“置备动作执行者”。

当然 provisioner 也有多个，根据具体的存储供应商的不同，提供不同的 provisioner。

### Cluster-API

在 Cluster-API 中，不同厂家为了支持 Cluster-API，会实现不同的 provider，比如 cluster-api-provider-aws, cluster-api-provider-vspher 等。


## 总结

根据实际的情况，provider 主要是用来区分供应者，是谁来提供某个事物，通常以公司区分。

provisioner 使用场景不多，主要是涉及到具体的功能执行，我这里理解为“置备动作执行者”，虽然也可以进行分类，但是主要意思应该是前者比较多一些。