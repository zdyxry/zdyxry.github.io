---
title: Kubernetes 实战-集群部署
date: 2019-05-31 21:22:51
tags:
- Kubernetes
---

## 背景

本来计划这周写一下如何定制 UEFI Linux 发行版的，但是计划赶不上变化，加上 UEFI 的改动比想象中的多，这周还是继续 k8s 系列好了。

说起来 k8s 写了 3 篇博客一直没有写集群部署相关的，一是当时对 k8s 了解不多，集群搭建大多是 GitHub 上的开源项目或 Rancher 快速搭建起来的；二是 k8s 官方工具 kubeadm 现在还有很多的不确定性，随着 v1.14 版本的发布，可用性大大提高，虽然还不支持 HA，但是要写一下了。

本文并不会介绍具体的部署步骤，望周知。

## Kubernetes 主要组件

因为主要说集群部署相关的，因此只列出 Master 和 Node 的主要组件，k8s 内部资源不再罗列：

### Master
* apiserver： 集群中所有其他组件通过 apiserver 进行交互

* scheduler： 按照 Pod 配置来对 Pod 进行节点调度

* controller-manager：负责节点管理，资源的具体创建动作， `desired state management` 具体实行者

* etcd：用于存储集群中数据的键值存储

### Node

* kubelet：处理 master 及其上运行的 node 之间的所有通信。它与容器运行时配合，负责部署和监控容器

* kube-proxy：负责维护 node 的网络规则，还负责处理 Pod,Node和外部之间的通信

* 容器运行时：在节点上运行容器的具体实现，常见的有 Docker/rkt/CRI-O


## Kubernetes 集群准备

### 所需资源

大部分的安装文档中，都会先写明 os 要求，计算 & 存储资源需求，k8s 自身对资源消耗很低，通常的 2c4g + 30GiB 足够运行起来。

上面说完了硬件资源，那么我们来说下软件资源， k8s 作为一个容器编排系统，它需要的软件资源也是很重要的一部分，这里我们来说一下网络部分。

假设我们集群中存在 5 个节点，使用 `kubeadm init` 方式部署集群，那么最基本的，需要 5 个节点的 IP。那如果是高可用的集群呢？我们需要加一个 VIP，也就是 6 个 IP 地址。

在考虑了 IP 地址之后，我们来说下网段划分，以 flannel 为例，在创建网络时，每个 k8s 节点都会分配一段子网用于 Pod 分配 IP，这里的网段是不可以跟宿主机的网络重叠的，所以这里的网络划分也是一个很重要的资源。

具体其他网络类型，我会在之后的网络部分详细的写一下。

### 部署方式

好了，现在我们已经有了资源了（无论是硬件资源还是软件资源），那么我们可以部署了，那此时采用什么方式部署，或者说怎么部署成了问题。

--- 

首先说下最特殊的服务，kubelet，它作为节点的实际管控者，它如果运行在容器中，那么谁来控制kubelet 容器的启停呢？当节点故障恢复后，又如何自启动呢？最开始我使用 Rancher 部署的时候发现他们是将 kubelet 直接部署在容器中的，那是因为他们在节点上还有其他 Agent 用于管理节点，Rancher 相当于 k8s 集群之外的上帝，管控着一切。

当我们没有 Rancher 这类管理工具时，还是老老实实将 kubelet 以服务的形式部署在宿主机上吧。

---

官方推荐使用 `kubeadm` 进行集群部署，简单快捷，只是还在快速迭代中，存在较多不确定性，那么现在那些大厂是如何部署的呢？

我花了点时间阅读了下 Github 上面一些关于 k8s 部署项目，简单的罗列一下：

项目名称| 项目地址| 星 | 服务运行方式 | ha 
--- | --- | --- | --- | ---
ansible-kubeadm | https://github.com/4admin2root/ansible-kubeadm | 3 | Static Pod |  - 
ansible-kubeadm-ha-cluster | https://github.com/sv01a/ansible-kubeadm-ha-cluster | 5 | Docker | keepvalied 
kubeadm-playbook | https://github.com/ReSearchITEng/kubeadm-playbook | 117 | Static Pod | keepalived 
Kubernetes-ansible | https://github.com/zhangguanzhang/Kubernetes-ansible | 208 | Service | keepalived & Haproxy
kubeadm-ansible | https://github.com/kairen/kubeadm-ansible | 281 | Static Pod | - 
kubeadm-ha | https://github.com/cookeem/kubeadm-ha | 502 | Service | keepalived & nginx 
kubeasz | https://github.com/easzlab/kubeasz | 2987 | Service | keepalived & Haproxy 

可以看到虽然有些细微的差别，但是大家做的都围绕着一个目的，就是把上一节提到的 k8s 所有必要组件部署到集群中，我们根据服务运行方式和 HA 方式来说一下。

## 服务运行方式

根据我上面总结的各个项目，大体分为 3 类，分别是：Host Service、Docker、Static Pod。我们一个一个的过一下。

### Host Service

在没有容器的时代，我们要部署一个服务，都是采用 Host Service 方式，我们在宿主机的 OS 上配置一个服务，管理方式可能是 init.d ，也可能是 systemd 。k8s 所有的服务都可以通过 Host Service 方式运行。

优点：

在 systemd 大法加持下，所有服务均可通过 systemd 统一管理，可以配置随着系统进行启停。

缺点：

如果通过 systemd 方式部署，那么服务配置修改、服务升级是一个大麻烦。

###  Docker

既然我们觉得 Host Service 的方式服务配置修改、升级都比较麻烦，那我们直接通过 Docker 启动就好了，升级直接更新 image 重新启动，一切问题放佛都解决了。

但是考虑一个问题，当集群全部掉电，系统开机后，k8s 如何自启动？以 Docker 作为容器运行时的基础上，Docker 比较让人诟病的一点就是它是一个 Daemon，在这里反而是优点，我们可以设置 Docker 随开机自启动，并将 k8s 所有服务对应镜像设置为 `--restart=always`，就可以解决这个问题。

优点：

服务配置、升级方便。

缺点：

依赖于 Docker，若更换其他 CRI，无法处理极端情况。

### Static Pod

最后我们来说说 Static Pod，这种方式是 kubeadm 目前所采用的方式，也是 k8s 所推荐的方式。

什么是 Static Pod？其实就是字面意义， `静态 Pod`，k8s 不去调度的 Pod，而是由 kubelet 直接管理。前面我们在讨论 kubelet 提到，kubelet 是以服务的形式运行在宿主机上的，那么也就是 kubelet 的启停是通过 systemd 控制的，不受 k8s 控制。

Static Pod 由 kubelet 控制，当 kubelet 启动后，会自动拉起 Static Pod，且 Static Pod 不受 k8s 控制，无论是通过 kubectl 进行删除，还是通过 docker 对该 Pod 进行 stop 动作，kubelet 都会保证 Static Pod 正常运行。

这个方式很适合我们来处理 k8s 自身的服务，比如 apiserver/scheduler ，每个 master 节点上通过 Static Pod 配置，当 kubelet 启动后，自动拉起 apiserver/scheduler 等服务，那么 k8s 集群也就自启动了，也就解决了我们上面提到的集群全部掉电的情况。

优点：

跟随 kubelet 启停，完美适配 k8s 升级场景。

缺点：

因为随着 kubelet 启停，所以导致更新 kubelet 配置时需要指定 manifest 文件路径。

## HA 配置

k8s 作为一个基础架构服务，它的可用性关乎着我们整个业务的稳定，所以一定要保证不会出现单点故障。

在公有云场景下，由公有云提供 LB 的支持，只要我们部署了多个 master 节点，就不用担心了。

那在裸机场景下怎么办呢？

目前通用解决方案是 VIP 配合 LB（也就是 keepalived & haproxy/nginx）。

 keepalived 提供了 VIP。在 k8s 集群部署过程中，所有节点都指定 `controlPlaneEndpoint` 为 VIP，而 VIP 在集群中的一个 master 节点上。当 VIP 所在节点故障时， VIP 自动漂浮到集群中其他 master 节点上，保证高可用。

 haproxy/nginx 作为 LB，当我们 k8s 集群中所有节点都连接一个 apiserver 时，通过 LB 按照既定策略将请求分发到集群中多个 master 节点上，保证性能。



## 总结

关于 k8s 集群的部署大概就是上述这些内容，具体的操作步骤都可以通过官网或者 github 找到相关资料。目前如果个人学习的话，直接通过 kubeadm 部署就好；如果想要在生产环境中部署，那么需要根据自身业务类型，仔细考虑自己是否需要 HA，如何配置 HA。

