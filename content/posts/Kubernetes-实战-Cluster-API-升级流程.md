---
title: Kubernetes 实战-Cluster API 升级流程
date: 2019-12-22 16:53:55
tags:
- Kubernetes
---

## 背景

之前已经介绍过 ClusterAPI 及相应实现方式，但是针对使用 ClusterAPI 部署的 K8s 集群社区中一直没有升级方案，其中 vmware 实现了一个简单的[升级工具](https://github.com/vmware/cluster-api-upgrade-tool)，可以在社区没实现之前提供使用，今天来看下这个工具是如何实现的。


## cluster-api-upgrade-tool

项目地址：https://github.com/vmware/cluster-api-upgrade-tool

因为这只是一个单独的工具，因此代码结构比较简单：

```shell
yiran@t480:~/go/src/github.com/vmware/cluster-api-upgrade-tool 
master ✔ $ tree .
.
├── CODE-OF-CONDUCT.md
├── CONTRIBUTING.md
├── Dockerfile
├── go.mod
├── go.sum
├── hack
│   └── tools
│       ├── go.mod
│       ├── go.sum
│       └── main.go
├── LICENSE.txt
├── main.go # 命令行入口
├── Makefile
├── NOTICE.txt
├── pkg
│   ├── internal
│   │   └── kubernetes
│   │       ├── client.go # 获取 client
│   │       └── pod_exec.go
│   ├── logging
│   │   └── logrus_logr.go
│   └── upgrade
│       ├── config.go 
│       ├── control_plane.go # 主要升级逻辑
│       └── control_plane_test.go
├── README.md
└── test
    └── integration
        ├── go.mod
        ├── go.sum
        └── main_test.go
```

## 升级流程

首先在 main.go 封装了相应的命令行用于升级，获取到相应配置后，开始升级：

```go
			upgrader, err := upgrade.NewControlPlaneUpgrader(newLogger(), finalConfig)
			if err != nil {
				return err
			}

            return upgrader.Upgrade()
```

在 control_plane.go 文件中是升级的主要逻辑，所有的步骤都是顺序执行的，摘要下主要的步骤：

```go
// Upgrade does the upgrading of the control plane.
func (u *ControlPlaneUpgrader) Upgrade() error {
	machines, err := u.listMachines()
	...
	if err := u.reconcileKubeadmConfigMapAPIEndpoints(); err != nil {
	err = u.updateKubeletConfigMapIfNeeded(u.desiredVersion)
	err = u.updateKubeletRbacIfNeeded(u.desiredVersion)
    if err := u.etcdClusterHealthCheck(15 * time.Second); err != nil {
    if err := u.UpdateProviderIDsToNodes(); err != nil {
	return updateKubeadmKubernetesVersion(in, "v"+u.desiredVersion.String())
	if err := u.updateMachines(machines); err != nil {
	if err := u.reconcileKubeadmConfigMapAPIEndpoints(); err != nil {
}
```

1. `u.listMachines`获取 TargetCluster 所有的 ControlPlane 节点   
    a. 通过 label 来进行 machine 过滤  
    b. 如果 Machine 的 DeletionTimestamp 字段为 0，则追加到列表中
2. `u.reconcileKubeadmConfigMapAPIEndpoints` 这里主要是确保对应的 APIEndpoints 节点都在 k8s 集群中，通过对比 nodeList 与 APIEndpoints 来进行过滤
3. `u.updateKubeletConfigMapIfNeeded` 在 k8s 中，在 ConfigMap 中是有保存 kubelet 配置信息的，在升级过程中，需要重新创建对应版本的 kubelet 配置信息，这个函数中直接将原版本的 kubelet 复制了一份，创建一份目标版本的 kublet 配置 ConfigMap
4. `u.updateKubeletRbacIfNeeded` 创建目标版本的 Role 和 RoleBinding 资源
5. `u.etcdClusterHealthCheck` 检查 etcd 集群是否健康，这里主要通过 `endpoint health --endpoints` 来检查 etcd 是否健康
6. `u.UpdateProviderIDsToNodes` 通过 Cluster-API 创建出来的节点，需要设置 node.ProviderID 才可以被 Cluster-API 识别为 running 状态，ProviderId 格式为：`vmware://xxxxx` ，这里根据 ProviderID 来检测出具体的 ID，并将其作为一个 map 返回
7. `u.updateKubeadmKubernetesVersion` 将 kubeadm ConfigMap 中的  `kubernetesVersion` 字段更新为目标版本，便于后续添加节点时指定的是目标版本
8. `u.updateMachines` 在所有配置文件已经准备、更新完成后，开始做整个升级中最重要的部分，节点（Machine）升级，首先遍历所有 Machine 资源，针对每个 Machine，进行如下动作：   
    a. `u.etcdClusterHealthCheck` 检查 etcd 集群是否健康，如果不健康，则退出升级  
    b. `generateReplacementMachineName` 生成替代 Machine 相应配置信息，如 MachineName  
    c. `u.updateInfrastructureReference` 创建替代 Machine 的 Infrastructure Object   
    d. `u.updateBootstrapConfig` 创建替代 Machine 的 Bootstrap Config，因为默认 Cluster-API 使用的 kubeadm Bootstrap，所以这里其实是生成替代 Machine 执行的 kubeadm 配置  
    e. `u.updateMachine` 真正创建替代 Machine 的步骤，创建对应的目标虚拟机，等待目标虚拟机添加到 K8s 集群中且处于 Ready 后，将原虚拟机对应 etcd 节点从 etcd 集群中移除，随后将原虚拟机对应节点从 K8s 集群中移除  
9. `u.reconcileKubeadmConfigMapAPIEndpoints` 等待所有 Machine 替换完成后，重新配置 kubeadm ConfigMap 保证 kubeadm ConfigMap 中保存所有的 APIEndpoints 信息。

## 总结

Cluster-API 作为 K8s cluster-lifecycle SIG 的一个还处于 Alpha 阶段的项目，还处于一个快速更新迭代的状态，因此最终升级流程是怎样还不确定，但是从 vmware 的这个工具来看，后续很有可能采用这种方案，毕竟 Cluster-API 不想通过 SSH 这种比较麻（恶）烦（心）的方式对节点进行管理，从 kubeadm Bootstrap 使用 Cloud-init 就可以看出，尤其是当支持多种 Linux 发行版后，可以预想这是一个灾难。因此使用这种节点逐一替换的方式是很方便的，具体实现看 v1alpha3 发布之后社区的讨论结果吧。

吐槽：
Cluster-API 项目在代码中很少使用缩写，带来的好处很明显，易读易懂，上手容易，我自己的项目也一直秉承着这种观点，但是当我看到 `reconcileKubeadmConfigMapAPIEndpoints` 这种长度的变量名，还是很崩溃的。

## 参考链接
* https://github.com/vmware/cluster-api-upgrade-tool