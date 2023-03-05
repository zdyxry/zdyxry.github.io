---
title: Kubernetes 实战-高可用集群部署（无LB）
date: 2019-12-19 21:38:16
tags:
- Kubernetes
---

## 背景

之前写过一篇[《Kubernetes 实战-高可用集群部署》](https://zdyxry.github.io/2019/06/15/Kubernetes-%E5%AE%9E%E6%88%98-%E9%AB%98%E5%8F%AF%E7%94%A8%E9%9B%86%E7%BE%A4%E9%83%A8%E7%BD%B2/) 博客讲 K8S 高可用配置，当时采用的方式是使用 keepalived 配合 HAProxy 自建 LB 的方式，但是最近发现无论是 Kubespray 还是 Rancher RKE 都没有采用这种方式，而是在 worker node 上配置 nginx/haproxy 代理 APIServer 达到目的。今天来手动配置下这种方式，了解下注意事项。

本文配置方式参考 Kubespray，主要是想加深自己对这方面的理解，如果只是单纯的想要搭建环境，那么直接使用 Kubespray 就好。

## 环境
IP | role | 
--- | --- | 
192.168.17.11 | ControlPlane1
192.168.17.12 | ControlPlane2
192.168.17.13 | ControlPlane3
192.168.17.14 | WorkerNode1

## 准备工作

### 软件安装

这部分准备工作与之前一样，没什么不同，因此不详细说明，需要安装 kubectl,kubeadm,kubelet 。

## 部署

### ControlPlane1

kubeadm 配置文件如下：

```shell
[root@install1 17:55:09 tmp]$cat kubeadm.yaml
---
apiServer: {}
apiVersion: kubeadm.k8s.io/v1beta1
certificatesDir: ""
clusterName: test
controlPlaneEndpoint: "192.168.17.11:6443"
controllerManager: {}
dns:
  type: ""
etcd: {}
imageRepository: registry.cn-hangzhou.aliyuncs.com/google_containers
kind: ClusterConfiguration
kubernetesVersion: ""
networking:
  dnsDomain: ""
  podSubnet: 10.244.0.0/16
  serviceSubnet: ""
scheduler: {}

---
apiVersion: kubeadm.k8s.io/v1beta1
kind: InitConfiguration
localAPIEndpoint:
  advertiseAddress: "192.168.17.11"
  bindPort: 6443
nodeRegistration:
  name: 'install1'

```


执行部署动作：
```shell
[root@install1 17:55:10 tmp]$kubeadm init --config kubeadm.yaml --upload-certs
...
You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of the control-plane node running the following command on each as root:

  kubeadm join 192.168.17.11:6443 --token 0xsbed.rcfk0ew0nlgrpjv0 \
    --discovery-token-ca-cert-hash sha256:1be9652019ef048fdd1d16385907c519e5559a1b786aa3ff1c46eeb489e1a6ef \
    --control-plane --certificate-key 2368ee7ebe6697164c46812e358539638de1d7665b3111afde949bce73275029

Please note that the certificate-key gives access to cluster sensitive data, keep it secret!
As a safeguard, uploaded-certs will be deleted in two hours; If necessary, you can use 
"kubeadm init phase upload-certs --upload-certs" to reload certs afterward.

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.17.11:6443 --token 0xsbed.rcfk0ew0nlgrpjv0 \
    --discovery-token-ca-cert-hash sha256:1be9652019ef048fdd1d16385907c519e5559a1b786aa3ff1c46eeb489e1a6ef 
```

### ControlPlane2

kubeadm 配置文件如下：

```shell
[root@install2 17:40:52 tmp]$cat kubeadm.yaml
apiVersion: kubeadm.k8s.io/v1beta2
kind: JoinConfiguration
discovery:
  bootstrapToken:
    apiServerEndpoint: 192.168.17.11:6443
    token: 0xsbed.rcfk0ew0nlgrpjv0
    unsafeSkipCAVerification: true
  timeout: 5m0s
  tlsBootstrapToken: 0xsbed.rcfk0ew0nlgrpjv0
controlPlane:
  localAPIEndpoint:
    advertiseAddress: 192.168.17.12
    bindPort: 6443
  certificateKey: 2368ee7ebe6697164c46812e358539638de1d7665b3111afde949bce73275029
nodeRegistration:
  name: installer2

```

执行部署动作：

```shell
[root@install2 17:40:58 tmp]$kubeadm join --config kubeadm.yaml
...
This node has joined the cluster and a new control plane instance was created:

* Certificate signing request was sent to apiserver and approval was received.
* The Kubelet was informed of the new secure connection details.
* Control plane (master) label and taint were applied to the new node.
* The Kubernetes control plane instances scaled up.
* A new etcd member was added to the local/stacked etcd cluster.

To start administering your cluster from this node, you need to run the following as a regular user:

        mkdir -p $HOME/.kube
        sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
        sudo chown $(id -u):$(id -g) $HOME/.kube/config

Run 'kubectl get nodes' to see this node join the cluster.
```

### ControlPlane3

kubeadm 配置文件如下：

```shell
[root@install3 17:47:24 tmp]$cat kubeadm.yaml
apiVersion: kubeadm.k8s.io/v1beta2
kind: JoinConfiguration
discovery:
  bootstrapToken:
    apiServerEndpoint: 192.168.17.11:6443
    token: 0xsbed.rcfk0ew0nlgrpjv0
    unsafeSkipCAVerification: true
  timeout: 5m0s
  tlsBootstrapToken: 0xsbed.rcfk0ew0nlgrpjv0
controlPlane:
  localAPIEndpoint:
    advertiseAddress: 192.168.17.13
    bindPort: 6443
  certificateKey: 2368ee7ebe6697164c46812e358539638de1d7665b3111afde949bce73275029
nodeRegistration:
  name: installer2
```

执行部署动作：

```shell
[root@install3 17:47:25 tmp]$kubeadm join --config kubeadm.yaml
...
This node has joined the cluster and a new control plane instance was created:

* Certificate signing request was sent to apiserver and approval was received.
* The Kubelet was informed of the new secure connection details.
* Control plane (master) label and taint were applied to the new node.
* The Kubernetes control plane instances scaled up.
* A new etcd member was added to the local/stacked etcd cluster.

To start administering your cluster from this node, you need to run the following as a regular user:

        mkdir -p $HOME/.kube
        sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
        sudo chown $(id -u):$(id -g) $HOME/.kube/config

Run 'kubectl get nodes' to see this node join the cluster.

```


### node1

3 个 ControlPlane 节点已经部署完成，我们可以通过 kubectl 命令获取对应的状态信息，因为没有部署 CNI，所以这里还是 NotReady 的：

```shell
[root@install1 18:00:50 tmp]$kubectl get node -o wide
NAME         STATUS     ROLES    AGE     VERSION   INTERNAL-IP     EXTERNAL-IP   OS-IMAGE                KERNEL-VERSION                        CONTAINER-RUNTIME
install1     NotReady   master   5m2s    v1.16.3   172.18.19.11    <none>        CentOS Linux 7 (Core)   3.10.0-1062.1.2.el7.smartx.1.x86_64   docker://19.3.5
installer2   NotReady   master   4m22s   v1.16.3   192.168.17.12   <none>        CentOS Linux 7 (Core)   3.10.0-1062.1.2.el7.smartx.1.x86_64   docker://19.3.5
installer3   NotReady   master   3m1s    v1.16.3   192.168.17.13   <none>        CentOS Linux 7 (Core)   3.10.0-1062.1.2.el7.smartx.1.x86_64   docker://19.3.5
[root@install1 18:00:53 tmp]$

```

现在要来部署 worker node，当我们有可用的 LB，时，我们无需关心 APIServer 的可用性，由 LB 来决定。那么现在没有可用的 LB，我们的 worker node 想要与 k8s 进行通信，就需要每个 worker node 自身启动一个 proxy，将自己的 kubelet 连接到自己本地，然后通过 proxy 到集群中已有的 APIServer 。

#### 配置 Proxy

这里以 nginx 举例：

```shell
[root@install4 18:05:03 ~]$mkdir /etc/nginx
[root@install4 18:06:02 ~]$chmod 700 /etc/nginx
[root@install4 18:14:23 ~]$cat /etc/nginx/nginx.conf
error_log stderr notice;

worker_processes 2;
worker_rlimit_nofile 130048;
worker_shutdown_timeout 10s;

events {
  multi_accept on;
  use epoll;
  worker_connections 16384;
}

stream {
  upstream kube_apiserver {
    least_conn;
    server 192.168.17.11:6443;
    server 192.168.17.12:6443;
    server 192.168.17.13:6443;
    }

  server {
    listen        127.0.0.1:6443;
    proxy_pass    kube_apiserver;
    proxy_timeout 10m;
    proxy_connect_timeout 1s;
  }
}

http {
  aio threads;
  aio_write on;
  tcp_nopush on;
  tcp_nodelay on;

  keepalive_timeout 5m;
  keepalive_requests 100;
  reset_timedout_connection on;
  server_tokens off;
  autoindex off;

  server {
    listen 8081;
    location /healthz {
      access_log off;
      return 200;
    }
    location /stub_status {
      stub_status on;
      access_log off;
    }
  }
  }
[root@install4 18:18:29 manifests]$vim /etc/sysctl.conf 
[root@install4 18:18:54 manifests]$sysctl -p 
net.ipv4.ip_forward = 1
net.ipv4.ip_local_reserved_ports = 30000-32767
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-arptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
```

#### 加入 K8s 集群

执行部署动作：

```shell
[root@install4 18:31:10 tmp]$kubeadm join 192.168.17.11:6443 --token 0xsbed.rcfk0ew0nlgrpjv0 \
    --discovery-token-ca-cert-hash sha256:1be9652019ef048fdd1d16385907c519e5559a1b786aa3ff1c46eeb489e1a6ef 
[preflight] Running pre-flight checks
        [WARNING IsDockerSystemdCheck]: detected "cgroupfs" as the Docker cgroup driver. The recommended driver is "systemd". Please follow the guide at https://kubernetes.io/docs/setup
/cri/
        [WARNING SystemVerification]: this Docker version is not on the list of validated versions: 19.03.5. Latest validated version: 18.09
        [WARNING Hostname]: hostname "install4" could not be reached
        [WARNING Hostname]: hostname "install4": lookup install4 on 192.168.31.215:53: no such host
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -oyaml'
[kubelet-start] Downloading configuration for the kubelet from the "kubelet-config-1.16" ConfigMap in the kube-system namespace
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Activating the kubelet service
[kubelet-start] Waiting for the kubelet to perform the TLS Bootstrap...

This node has joined the cluster:
* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the control-plane to see this node join the cluster.
```

此时在 K8s 集群中存在 4个节点，其中 3 个是 ControlPlane 节点，1 个是 worker 节点，但是此时 worker 节点是连接的 192.168.17.11:6443 APIServer，如果 这个 APIServer 故障了，那么的 worker 节点就无法正常与集群通讯了，需要进行以下操作：

```shell
[root@install4 18:37:51 kubernetes]$systemctl stop kubelet docker
[root@install4 18:38:09 manifests]$pwd
/etc/kubernetes/manifests
[root@install4 18:38:12 manifests]$cat nginx-proxy.yml 
apiVersion: v1
kind: Pod
metadata:
  name: nginx-proxy
  namespace: kube-system
  labels:
    addonmanager.kubernetes.io/mode: Reconcile
    k8s-app: kube-nginx
  annotations:
spec:
  hostNetwork: true
  dnsPolicy: ClusterFirstWithHostNet
  nodeSelector:
    beta.kubernetes.io/os: linux
  priorityClassName: system-node-critical
  containers:
  - name: nginx-proxy
    image: docker.io/library/nginx:1.17
    imagePullPolicy: IfNotPresent
    resources:
      requests:
        cpu: 25m
        memory: 32M
    securityContext:
      privileged: true
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8081
    readinessProbe:
      httpGet:
        path: /healthz
        port: 8081
    volumeMounts:
    - mountPath: /etc/nginx
      name: etc-nginx
      readOnly: true
  volumes:
  - name: etc-nginx
    hostPath:
      path: /etc/nginx
```

修改 kubelet 配置文件，将 Server 字段替换为 `127.0.0.1:6443` ，启动 kubelet 和 docker 即可。

## 配置修改

最开始我以为到这里就结束了，结果在自己测试的过程中，发现了一点问题，使用 kubeadm 部署集群，在添加 ControlPlane 的时候，会将 kubelet 所连接的 APIServer 配置为 controlPlaneEndpoint 地址，这在没有 LB 的场景下是致命的，单点故障。

所以我们需要依次的修改所有节点的 kubelet 配置，修改内容如下：

### ControlPlane

因为所有的 ControlPlane 节点都会自己运行 APIServer，那么 kubelet 连接自身即可。

### Worker

Worker 节点因为没有 APIServer，所以我们刚刚通过配置本地的 Proxy 来达到相同的目的，这里无需再次修改。


## 总结

到这里我们的集群已经配置完成了，无论是 ControlPlane 节点故障，还是 Worker 节点故障，都不是单点的，可以起到高可用的作用。这种方式其实是没有 LB 的一种妥协，这里引用 Kubespray 关于 HA 模式的文档：

> K8s components require a loadbalancer to access the apiservers via a reverse proxy. Kubespray includes support for an nginx-based proxy that resides on each non-master Kubernetes node. This is referred to as localhost loadbalancing. It is less efficient than a dedicated load balancer because it creates extra health checks on the Kubernetes apiserver, but is more practical for scenarios where an external LB or virtual IP management is inconvenient. 

如果有 LB 肯定还是优先 LB 的，但是在没有 LB 的情况下我们如何选择，就看我们自己的场景了，如果真的是自建 Keepalived & HAProxy ，那么之后的集群管理是一个很麻烦的事情，而且 Keepalived 在使用上没有那么的友好，尤其是网络环境复杂之后（我之前碰到过一次 ovs & keepalived 不工作的情况）。

目前社区中关于 K8S 生命周期管理的工具越来越多，但是如果仔细看看，其实大家的做法都是大同小异。还是要自己了解一下具体的问题点在哪里，如何解决才是硬道理。



## 参考链接
* https://github.com/kubernetes-sigs/kubespray