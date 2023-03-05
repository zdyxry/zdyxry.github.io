---
title: Kubernetes 实战-Cluster API
date: 2019-08-09 19:41:49
tags:
- Kubernetes
---

## 背景

在当前 Kubernetes 生态中，生命周期管理相关工具官方的有 kubeadm、kubespray（部署集群部分通过 kubeadm） ，开源社区还有很多其他的实现，我们可以通过这类工具来实现 k8s 集群的部署，升级，增删节点，但是使用一个工具的前提是：基础设施已经准备完成。只有当基础设施准备完成后，kubeadm 之类工具才可以正常工作。


当我们在部署 Kubernetes 集群时，节点可能在任何环境上，比如 AWS、OpenStack、Vsphere、Azure 等，那么想要自动化配置基础设施，通常我们根据自己的环境不同，编写不通的代码来支持我们的虚拟化（or 服务器）场景。


基础设施包括不限于：
* OS 安装
* Load Balance 配置
* 网络配置
* IP 分配
* …

## Cluster-API

Kubernetes 社区针对基础设施问题，发起了一个项目：cluster-api，目前处于 alpha1 版本，项目目标：
1. 使用声明式API管理 Kubernetes 集群的生命周期
2. 支持多种环境，私有云或公有云
3. 使用社区中现有的工具完成相应功能
4. …

### 功能简述
1. 无需创建额外基础设施前提下创建 bootstrap cluster
2. 通过 bootstrap cluster 创建目标 k8s 集群


### 工作流程
1. cluster-api 使用声明式 API 管理 k8s 集群，需要环境中先存在一个 k8s 集群，通常成为 bootstrap cluster，若不存在，也可通过提供的命令行工具 clusterctl 创建 bootstrap cluster
2. 在 bootstrap cluster 中，部署 CRD 及相应的 cluster api 控制器及 provider 控制器
3. 在 bootstrap cluster 中，开始创建我们真正想要创建的资源：k8s 集群
创建资源类型为 Cluster、Machine 或 MachineDeployment ，对应的控制器会自动为我们创建好虚拟机
4. 在虚拟机创建完成后，通过 kubeadm 创建 k8s 集群

### 具体实现

#### 虚拟机创建
目前看到的几个 Cluster-API Provider 项目实现，虚拟机均通过克隆的方式创建出来的。

#### 虚拟机创建失败处理
百度：每次等待 30s 查询一次，重试10次，若仍未成功，则创建失败

腾讯：每 2s 查询一次，若不成功，则一直循环

vsphere：提交虚拟机创建任务后未检查是否正确创建，未发现重试逻辑

OpenStack：每 10s 检测一次，若超过设定 timeout ，则创建失败

#### 虚拟机控制方式
如果虚拟化平台支持 Cloud-init（或类似功能），后续 k8s 部署通过 Cloud-init 实现；

若虚拟化平台不支持，则 bootstrap cluster 中的 Pod 通过 ssh 方式进入倒虚拟机内部执行命令。

通过 Clout-init 实现的好处是Controller 只需要控制虚拟机开机即可，后续无需再主动与虚拟机进行通信，由 Cloud-init 自行触发部署 k8s集群任务；若没有 Cloud-init，则 Controller 在提交虚拟机创建任务后，需要循环等待虚拟机是否正常，等待正常后还需通过 ssh 主动与虚拟机进行连接控制，过于繁琐。




## 总结

Cluster API 目前还处于 Alpha1 版本，但是已经有很多厂家对其进行适配了，目前看到完成度比较高的公有云是 AWS，私有云是 Vsphere，之后好好读一下 Vsphere 的代码，了解下具体实现。
