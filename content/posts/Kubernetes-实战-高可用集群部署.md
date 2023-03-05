---
title: Kubernetes 实战-高可用集群部署
date: 2019-06-15 01:44:28
tags:
- Kubernetes
---


## 准备工作

本文所有节点 OS 均为 CentOS 7.4 。

### 1.关闭 selinux

所有节点执行：

```bash
[root@node211 ~]# cat /etc/selinux/config 

# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=disabled
# SELINUXTYPE= can take one of three two values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected. 
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted 


[root@node211 ~]# getenforce 
Disabled
```

### 2. 关于 firewalld

所有节点执行：

```bash
[root@node211 ~]# systemctl disable firewalld
[root@node211 ~]# systemctl stop firewalld
[root@node211 ~]# systemctl status firewalld
[root@node211 ~]# systemctl status firewalld
● firewalld.service - firewalld - dynamic firewall daemon
   Loaded: loaded (/usr/lib/systemd/system/firewalld.service; disabled; vendor preset: enabled)
   Active: inactive (dead)
     Docs: man:firewalld(1)
```


### 3. 安装必要 yum 源：epel-release

所有节点执行：

```bash
[root@node211 ~]# yum install epel-release
[root@node211 ~]# ls /etc/yum.repos.d/epel.repo 
/etc/yum.repos.d/epel.repo
```

### 4. 关闭节点 swap 空间

所有节点执行：

```bash
[root@node211 ~]# cat /etc/fstab 

#
# /etc/fstab
# Created by anaconda on Thu Jun 13 09:45:52 2019
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
/dev/mapper/centos-root /                       xfs     defaults        0 0
UUID=c0f0a31a-0c36-42cf-b52a-8f3b027ef948 /boot                   xfs     defaults        0 0
#/dev/mapper/centos-swap swap                    swap    defaults        0 0
[root@node211 ~]# free -h
              total        used        free      shared  buff/cache   available
Mem:           3.7G        102M        3.3G        8.3M        230M        3.3G
Swap:            0B          0B          0B
```


### 5. 安装 docker-ce 

所有节点执行：

```bash
[root@node211 ~]# 
[root@node211 ~]# head -n 6 /etc/yum.repos.d/docker-ce.repo
[docker-ce-stable]
name=Docker CE Stable - $basearch
baseurl=https://download.docker.com/linux/centos/7/$basearch/stable
enabled=1
gpgcheck=1
gpgkey=https://download.docker.com/linux/centos/gpg
[root@node211 ~]# rpm -q docker
docker-1.13.1-96.gitb2f74b2.el7.centos.x86_64
[root@node211 ~]# systemctl enable docker
[root@node211 ~]# systemctl start docker
[root@node211 ~]# systemctl status docker
● docker.service - Docker Application Container Engine
   Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; vendor preset: disabled)
   Active: active (running) since Fri 2019-06-14 19:48:40 CST; 3s ago
     Docs: http://docs.docker.com
 Main PID: 11488 (dockerd-current)
   CGroup: /system.slice/docker.service
           ├─11488 /usr/bin/dockerd-current --add-runtime docker-runc=/usr/libexec/docker/docker-runc-current --default-runtime=docker-runc --exec-opt native.cgroupdriver=systemd --userland-proxy-path=/usr/libexec/docker/docker-proxy-current --init-path=/usr...
           └─11495 /usr/bin/docker-containerd-current -l unix:///var/run/docker/libcontainerd/docker-containerd.sock --metrics-interval=0 --start-timeout 2m --state-dir /var/run/docker/libcontainerd/containerd --shim docker-containerd-shim --runtime docker-r...

Jun 14 19:48:40 node211 dockerd-current[11488]: time="2019-06-14T19:48:40.282909889+08:00" level=info msg="Docker daemon" commit="b2f74b2/1.13.1" graphdriver=overlay2 version=1.13.1
Jun 14 19:48:40 node211 dockerd-current[11488]: time="2019-06-14T19:48:40.293315055+08:00" level=info msg="API listen on /var/run/docker.sock"
Jun 14 19:48:40 node211 systemd[1]: Started Docker Application Container Engine.
```

### 6. 开启必要系统参数 sysctl

所有节点执行：

```bash
[root@node211 ~]# sysctl -p
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
```


## kubeadm

因为 kubeadm 官方文档中没有详细步骤，因此相关描述尽量具体到命令行。

### 环境信息

ip | role |
--- | --- | 
192.168.77.211 | master
192.168.77.212 | master
192.168.77.213 | master 
192.168.77.214 | node


### 1. 安装 kubeadm

所有节点执行：

```bash
[root@node211 ~]# cat /etc/yum.repos.d/kubernetes.repo 
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
proxy=socks5://127.0.0.1:1080
[root@node211 ~]# yum install kubeadm kubelet
[root@node211 ~]# which kubeadm 
/usr/bin/kubeadm
```


### 2. 安装 keepalived

所有 master 节点执行：

```bash
[root@node211 ~]# yum install keepalived
[root@node212 ~]# yum install keepalived 
[root@node213 ~]# yum install keepalived
```

编辑 node211 配置文件：

```bash
[root@node211 ~]# cat /etc/keepalived/keepalived.conf 
! Configuration File for keepalived

global_defs {
   notification_email {
        feng110498@163.com
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 127.0.0.1
   smtp_connect_timeout 30
   router_id LVS_1
}

vrrp_instance VI_1 {
    state MASTER          
    interface eth0
    lvs_sync_daemon_inteface eth0
    virtual_router_id 79
    advert_int 1
    priority 100         
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
      192.168.77.219/20
    }
}
```

编辑 node212 配置文件：

```bash
[root@node212 ~]# cat /etc/keepalived/keepalived.conf 
! Configuration File for keepalived

global_defs {
   notification_email {
        feng110498@163.com
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 127.0.0.1
   smtp_connect_timeout 30
   router_id LVS_1
}

vrrp_instance VI_1 {
    state MASTER          
    interface eth0
    lvs_sync_daemon_inteface eth0
    virtual_router_id 79
    advert_int 1
    priority 90         
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
      192.168.77.219/20
    }
}
```


编辑 node213 配置文件：
```bash
[root@node213 ~]# cat /etc/keepalived/keepalived.conf 
! Configuration File for keepalived

global_defs {
   notification_email {
        feng110498@163.com
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 127.0.0.1
   smtp_connect_timeout 30
   router_id LVS_1
}

vrrp_instance VI_1 {
    state MASTER          
    interface eth0
    lvs_sync_daemon_inteface eth0
    virtual_router_id 79
    advert_int 1
    priority 70         
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
      192.168.77.219/20
    }
}
```

node211, node212, node213 重启 keepalived：

```bash
[root@node211 ~]# systemctl restart keepalived
[root@node212 ~]# systemctl restart keepalived
[root@node213 ~]# systemctl restart keepalived
```

因为 node211 优先级最高，此时 VIP 192.168.77.219 应该在 node211 节点，查看 node211 节点 IP：

```bash
[root@node211 ~]# ip ad 
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether 52:54:00:42:fd:a6 brd ff:ff:ff:ff:ff:ff
    inet 192.168.77.211/20 brd 192.168.79.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet 192.168.77.219/20 scope global secondary eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::5554:b212:7895:c8ad/64 scope link tentative dadfailed 
       valid_lft forever preferred_lft forever
    inet6 fe80::3e97:25b9:cc1a:809c/64 scope link tentative dadfailed 
       valid_lft forever preferred_lft forever
    inet6 fe80::7a4f:3726:af17:18bf/64 scope link tentative dadfailed 
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN 
    link/ether 02:42:6f:0e:81:59 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 scope global docker0
       valid_lft forever preferred_lft forever
```

配置无异常，node211,node212,node213 设置开机自启动：

```bash
[root@node211 ~]# systemctl enable keepalived
Created symlink from /etc/systemd/system/multi-user.target.wants/keepalived.service to /usr/lib/systemd/system/keepalived.service.
[root@node212 ~]# systemctl enable keepalived
Created symlink from /etc/systemd/system/multi-user.target.wants/keepalived.service to /usr/lib/systemd/system/keepalived.service.
[root@node213 ~]# systemctl enable keepalived
Created symlink from /etc/systemd/system/multi-user.target.wants/keepalived.service to /usr/lib/systemd/system/keepalived.service.
```

### 3. 安装 haproxy

所有 master 节点执行：

```bash
[root@node211 ~]# yum install haproxy
[root@node212 ~]# yum install haproxy
[root@node213 ~]# yum install haproxy
```

编辑所有 master 节点配置文件：

```bash
[root@node211 ~]# cat /etc/haproxy/haproxy.cfg 
global
        chroot  /var/lib/haproxy
        daemon
        group haproxy
        user haproxy
        log 127.0.0.1:514 local0 warning
        pidfile /var/lib/haproxy.pid
        maxconn 20000
        spread-checks 3
        nbproc 8

defaults
        log     global
        mode    tcp
        retries 3
        option redispatch

listen https-apiserver
        bind *:8443
        mode tcp
        balance roundrobin
        timeout server 900s
        timeout connect 15s

        server m1 192.168.77.211:6443 check port 6443 inter 5000 fall 5
        server m2 192.168.77.212:6443 check port 6443 inter 5000 fall 5
        server m3 192.168.77.213:6443 check port 6443 inter 5000 fall 5
```

所有 master 节点启动 haproxy，并设置 开机自启动：

```bash
[root@node211 ~]# systemctl start haproxy 
[root@node211 ~]# systemctl enable haproxy
Created symlink from /etc/systemd/system/multi-user.target.wants/haproxy.service to /usr/lib/systemd/system/haproxy.service.
[root@node212 ~]# systemctl start haproxy 
[root@node212 ~]# systemctl enable haproxy
Created symlink from /etc/systemd/system/multi-user.target.wants/haproxy.service to /usr/lib/systemd/system/haproxy.service.
[root@node213 ~]# systemctl start haproxy 
[root@node213 ~]# systemctl enable haproxy
Created symlink from /etc/systemd/system/multi-user.target.wants/haproxy.service to /usr/lib/systemd/system/haproxy.service.
```


### 4. 编写 kubeadm 配置文件

在 node211 节点编写 kubeadm 配置文件：

```bash
[root@node211 ~]# cat kubeadm-init.yaml
apiVersion: kubeadm.k8s.io/v1beta1
kind: ClusterConfiguration
apiServer:
  timeoutForControlPlane: 4m0s
certificatesDir: /etc/kubernetes/pki
clusterName: kubernetes
controlPlaneEndpoint: "192.168.77.219:8443"
dns:
  type: CoreDNS
etcd:
  local:
    dataDir: /var/lib/etcd
imageRepository: registry.cn-hangzhou.aliyuncs.com/google_containers
kubernetesVersion: v1.14.3
networking:
  dnsDomain: cluster.local
  podSubnet: "10.123.0.0/16"
scheduler: {}
controllerManager: {}
---
apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration
mode: "ipvs"
```


### 5. 初始化

在 node211 节点执行初始化操作：

```bash
[root@node211 ~]# kubeadm init --config=kubeadm-init.yaml --experimental-upload-certs
[init] Using Kubernetes version: v1.14.3
[preflight] Running pre-flight checks
	[WARNING Hostname]: hostname "node211" could not be reached
	[WARNING Hostname]: hostname "node211": lookup node211 on 192.168.64.215:53: no such host
	[WARNING Service-Kubelet]: kubelet service is not enabled, please run 'systemctl enable kubelet.service'
	[WARNING RequiredIPVSKernelModulesAvailable]: 

The IPVS proxier may not be used because the following required kernel modules are not loaded: [ip_vs_rr ip_vs_wrr ip_vs_sh]
or no builtin kernel IPVS support was found: map[ip_vs:{} ip_vs_rr:{} ip_vs_sh:{} ip_vs_wrr:{} nf_conntrack_ipv4:{}].
However, these modules may be loaded automatically by kube-proxy if they are available on your system.
To verify IPVS support:

   Run "lsmod | grep 'ip_vs|nf_conntrack'" and verify each of the above modules are listed.

If they are not listed, you can use the following methods to load them:

1. For each missing module run 'modprobe $modulename' (e.g., 'modprobe ip_vs', 'modprobe ip_vs_rr', ...)
2. If 'modprobe $modulename' returns an error, you will need to install the missing module support for your kernel.

[preflight] Pulling images required for setting up a Kubernetes cluster
[preflight] This might take a minute or two, depending on the speed of your internet connection
[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Activating the kubelet service
[certs] Using certificateDir folder "/etc/kubernetes/pki"
[certs] Generating "ca" certificate and key
[certs] Generating "apiserver" certificate and key
[certs] apiserver serving cert is signed for DNS names [node211 kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local] and IPs [10.96.0.1 192.168.77.211 192.168.77.219]
[certs] Generating "apiserver-kubelet-client" certificate and key
[certs] Generating "front-proxy-ca" certificate and key
[certs] Generating "front-proxy-client" certificate and key
[certs] Generating "etcd/ca" certificate and key
[certs] Generating "etcd/server" certificate and key
[certs] etcd/server serving cert is signed for DNS names [node211 localhost] and IPs [192.168.77.211 127.0.0.1 ::1]
[certs] Generating "etcd/peer" certificate and key
[certs] etcd/peer serving cert is signed for DNS names [node211 localhost] and IPs [192.168.77.211 127.0.0.1 ::1]
[certs] Generating "etcd/healthcheck-client" certificate and key
[certs] Generating "apiserver-etcd-client" certificate and key
[certs] Generating "sa" key and public key
[kubeconfig] Using kubeconfig folder "/etc/kubernetes"
[endpoint] WARNING: port specified in controlPlaneEndpoint overrides bindPort in the controlplane address
[kubeconfig] Writing "admin.conf" kubeconfig file
[endpoint] WARNING: port specified in controlPlaneEndpoint overrides bindPort in the controlplane address
[kubeconfig] Writing "kubelet.conf" kubeconfig file
[endpoint] WARNING: port specified in controlPlaneEndpoint overrides bindPort in the controlplane address
[kubeconfig] Writing "controller-manager.conf" kubeconfig file
[endpoint] WARNING: port specified in controlPlaneEndpoint overrides bindPort in the controlplane address
[kubeconfig] Writing "scheduler.conf" kubeconfig file
[control-plane] Using manifest folder "/etc/kubernetes/manifests"
[control-plane] Creating static Pod manifest for "kube-apiserver"
[control-plane] Creating static Pod manifest for "kube-controller-manager"
[control-plane] Creating static Pod manifest for "kube-scheduler"
[etcd] Creating static Pod manifest for local etcd in "/etc/kubernetes/manifests"
[wait-control-plane] Waiting for the kubelet to boot up the control plane as static Pods from directory "/etc/kubernetes/manifests". This can take up to 4m0s
[kubelet-check] Initial timeout of 40s passed.
[apiclient] All control plane components are healthy after 107.014141 seconds
[upload-config] storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[kubelet] Creating a ConfigMap "kubelet-config-1.14" in namespace kube-system with the configuration for the kubelets in the cluster
[upload-certs] Storing the certificates in ConfigMap "kubeadm-certs" in the "kube-system" Namespace
[upload-certs] Using certificate key:
1436c652cc6bb7e91386b4f744e3376df7b3b6ffd5e9a1a2930f9b6241daac4a
[mark-control-plane] Marking the node node211 as control-plane by adding the label "node-role.kubernetes.io/master=''"
[mark-control-plane] Marking the node node211 as control-plane by adding the taints [node-role.kubernetes.io/master:NoSchedule]
[bootstrap-token] Using token: ptuvy5.hl4rzxugpxpgkgkh
[bootstrap-token] Configuring bootstrap tokens, cluster-info ConfigMap, RBAC Roles
[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to post CSRs in order for nodes to get long term certificate credentials
[bootstrap-token] configured RBAC rules to allow the csrapprover controller automatically approve CSRs from a Node Bootstrap Token
[bootstrap-token] configured RBAC rules to allow certificate rotation for all node client certificates in the cluster
[bootstrap-token] creating the "cluster-info" ConfigMap in the "kube-public" namespace
[addons] Applied essential addon: CoreDNS
[endpoint] WARNING: port specified in controlPlaneEndpoint overrides bindPort in the controlplane address
[addons] Applied essential addon: kube-proxy

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of the control-plane node running the following command on each as root:

  kubeadm join 192.168.77.219:8443 --token ptuvy5.hl4rzxugpxpgkgkh \
    --discovery-token-ca-cert-hash sha256:2a190612b1e3a68a549d02b42335bfba4dd4af3bb1361124ad46862e1ab418d4 \
    --experimental-control-plane --certificate-key 1436c652cc6bb7e91386b4f744e3376df7b3b6ffd5e9a1a2930f9b6241daac4a

Please note that the certificate-key gives access to cluster sensitive data, keep it secret!
As a safeguard, uploaded-certs will be deleted in two hours; If necessary, you can use 
"kubeadm init phase upload-certs --experimental-upload-certs" to reload certs afterward.

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.77.219:8443 --token ptuvy5.hl4rzxugpxpgkgkh \
    --discovery-token-ca-cert-hash sha256:2a190612b1e3a68a549d02b42335bfba4dd4af3bb1361124ad46862e1ab418d4

```

按照说明，拷贝 kubectl 配置文件并验证：

```bash
[root@node211 ~]# mkdir -p $HOME/.kube
[root@node211 ~]# sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
[root@node211 ~]# sudo chown $(id -u):$(id -g) $HOME/.kube/config
[root@node211 ~]# kubectl get node
NAME      STATUS     ROLES    AGE   VERSION
node211   NotReady   master   82s   v1.14.3
```

### 6. 部署 flannel 网络插件

在 node211 节点部署 flannel 插件：

```bash
[root@node211 ~]# kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/a70459be0084506e4ec919aa1c114638878db11b/Documentation/kube-flannel.yml
clusterrole.rbac.authorization.k8s.io/flannel created
clusterrolebinding.rbac.authorization.k8s.io/flannel created
serviceaccount/flannel created
configmap/kube-flannel-cfg created
daemonset.extensions/kube-flannel-ds-amd64 created
daemonset.extensions/kube-flannel-ds-arm64 created
daemonset.extensions/kube-flannel-ds-arm created
daemonset.extensions/kube-flannel-ds-ppc64le created
daemonset.extensions/kube-flannel-ds-s390x created
```

查看部署状态：

```bash
[root@node211 ~]# kubectl get pod -n kube-system
NAME                              READY   STATUS    RESTARTS   AGE
coredns-d5947d4b-rn2wl            0/1     Pending   0          3m17s
coredns-d5947d4b-zdptx            0/1     Pending   0          3m17s
etcd-node211                      1/1     Running   0          2m48s
kube-apiserver-node211            1/1     Running   0          2m28s
kube-controller-manager-node211   1/1     Running   0          2m59s
kube-flannel-ds-amd64-vzk7c       1/1     Running   0          36s
kube-proxy-w5gsg                  1/1     Running   0          3m16s
kube-scheduler-node211            1/1     Running   0          2m41s
```



### 7. 添加其他 master 节点

按照 node211 初始化提示，在 node212 节点及 node213 节点添加到集群，角色为 master：

```bash
[root@node212 ~]# kubeadm join 192.168.77.219:8443 --token ptuvy5.hl4rzxugpxpgkgkh \
>     --discovery-token-ca-cert-hash sha256:2a190612b1e3a68a549d02b42335bfba4dd4af3bb1361124ad46862e1ab418d4 \
>     --experimental-control-plane --certificate-key 1436c652cc6bb7e91386b4f744e3376df7b3b6ffd5e9a1a2930f9b6241daac4a
[preflight] Running pre-flight checks
	[WARNING Hostname]: hostname "node212" could not be reached
	[WARNING Hostname]: hostname "node212": lookup node212 on 192.168.64.215:53: no such host
	[WARNING Service-Kubelet]: kubelet service is not enabled, please run 'systemctl enable kubelet.service'
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -oyaml'
	[WARNING RequiredIPVSKernelModulesAvailable]: 

The IPVS proxier may not be used because the following required kernel modules are not loaded: [ip_vs_sh ip_vs_rr ip_vs_wrr]
or no builtin kernel IPVS support was found: map[ip_vs:{} ip_vs_rr:{} ip_vs_sh:{} ip_vs_wrr:{} nf_conntrack_ipv4:{}].
However, these modules may be loaded automatically by kube-proxy if they are available on your system.
To verify IPVS support:

   Run "lsmod | grep 'ip_vs|nf_conntrack'" and verify each of the above modules are listed.

If they are not listed, you can use the following methods to load them:

1. For each missing module run 'modprobe $modulename' (e.g., 'modprobe ip_vs', 'modprobe ip_vs_rr', ...)
2. If 'modprobe $modulename' returns an error, you will need to install the missing module support for your kernel.

[preflight] Running pre-flight checks before initializing the new control plane instance
[preflight] Pulling images required for setting up a Kubernetes cluster
[preflight] This might take a minute or two, depending on the speed of your internet connection
[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'
[download-certs] Downloading the certificates in Secret "kubeadm-certs" in the "kube-system" Namespace
[certs] Using certificateDir folder "/etc/kubernetes/pki"
[certs] Generating "etcd/server" certificate and key
[certs] etcd/server serving cert is signed for DNS names [node212 localhost] and IPs [192.168.77.212 127.0.0.1 ::1]
[certs] Generating "apiserver-etcd-client" certificate and key
[certs] Generating "etcd/peer" certificate and key
[certs] etcd/peer serving cert is signed for DNS names [node212 localhost] and IPs [192.168.77.212 127.0.0.1 ::1]
[certs] Generating "etcd/healthcheck-client" certificate and key
[certs] Generating "apiserver" certificate and key
[certs] apiserver serving cert is signed for DNS names [node212 kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local] and IPs [10.96.0.1 192.168.77.212 192.168.77.219]
[certs] Generating "apiserver-kubelet-client" certificate and key
[certs] Generating "front-proxy-client" certificate and key
[certs] Valid certificates and keys now exist in "/etc/kubernetes/pki"
[certs] Using the existing "sa" key
[kubeconfig] Generating kubeconfig files
[kubeconfig] Using kubeconfig folder "/etc/kubernetes"
[endpoint] WARNING: port specified in controlPlaneEndpoint overrides bindPort in the controlplane address
[kubeconfig] Writing "admin.conf" kubeconfig file
[kubeconfig] Writing "controller-manager.conf" kubeconfig file
[kubeconfig] Writing "scheduler.conf" kubeconfig file
[control-plane] Using manifest folder "/etc/kubernetes/manifests"
[control-plane] Creating static Pod manifest for "kube-apiserver"
[control-plane] Creating static Pod manifest for "kube-controller-manager"
[control-plane] Creating static Pod manifest for "kube-scheduler"
[check-etcd] Checking that the etcd cluster is healthy
[kubelet-start] Downloading configuration for the kubelet from the "kubelet-config-1.14" ConfigMap in the kube-system namespace
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Activating the kubelet service
[kubelet-start] Waiting for the kubelet to perform the TLS Bootstrap...
[etcd] Announced new etcd member joining to the existing etcd cluster
[etcd] Wrote Static Pod manifest for a local etcd member to "/etc/kubernetes/manifests/etcd.yaml"
[etcd] Waiting for the new etcd member to join the cluster. This can take up to 40s
[upload-config] storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[mark-control-plane] Marking the node node212 as control-plane by adding the label "node-role.kubernetes.io/master=''"
[mark-control-plane] Marking the node node212 as control-plane by adding the taints [node-role.kubernetes.io/master:NoSchedule]

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

按照说明，拷贝 kubectl 配置文件并验证：

```bash
[root@node212 ~]# mkdir -p $HOME/.kube
[root@node212 ~]# sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
[root@node212 ~]# sudo chown $(id -u):$(id -g) $HOME/.kube/config
[root@node212 ~]# kubectl get node
NAME      STATUS   ROLES    AGE     VERSION
node211   Ready    master   7m48s   v1.14.3
node212   Ready    master   66s     v1.14.3
```



```bash
[root@node213 ~]# kubeadm join 192.168.77.219:8443 --token ptuvy5.hl4rzxugpxpgkgkh \
>     --discovery-token-ca-cert-hash sha256:2a190612b1e3a68a549d02b42335bfba4dd4af3bb1361124ad46862e1ab418d4 \
>     --experimental-control-plane --certificate-key 1436c652cc6bb7e91386b4f744e3376df7b3b6ffd5e9a1a2930f9b6241daac4a
[preflight] Running pre-flight checks
	[WARNING Hostname]: hostname "node213" could not be reached
	[WARNING Hostname]: hostname "node213": lookup node213 on 192.168.64.215:53: no such host
	[WARNING Service-Kubelet]: kubelet service is not enabled, please run 'systemctl enable kubelet.service'
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -oyaml'
	[WARNING RequiredIPVSKernelModulesAvailable]: 

The IPVS proxier may not be used because the following required kernel modules are not loaded: [ip_vs_wrr ip_vs_sh ip_vs_rr]
or no builtin kernel IPVS support was found: map[ip_vs:{} ip_vs_rr:{} ip_vs_sh:{} ip_vs_wrr:{} nf_conntrack_ipv4:{}].
However, these modules may be loaded automatically by kube-proxy if they are available on your system.
To verify IPVS support:

   Run "lsmod | grep 'ip_vs|nf_conntrack'" and verify each of the above modules are listed.

If they are not listed, you can use the following methods to load them:

1. For each missing module run 'modprobe $modulename' (e.g., 'modprobe ip_vs', 'modprobe ip_vs_rr', ...)
2. If 'modprobe $modulename' returns an error, you will need to install the missing module support for your kernel.

[preflight] Running pre-flight checks before initializing the new control plane instance
[preflight] Pulling images required for setting up a Kubernetes cluster
[preflight] This might take a minute or two, depending on the speed of your internet connection
[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'
[download-certs] Downloading the certificates in Secret "kubeadm-certs" in the "kube-system" Namespace
[certs] Using certificateDir folder "/etc/kubernetes/pki"
[certs] Generating "front-proxy-client" certificate and key
[certs] Generating "etcd/server" certificate and key
[certs] etcd/server serving cert is signed for DNS names [node213 localhost] and IPs [192.168.77.213 127.0.0.1 ::1]
[certs] Generating "etcd/peer" certificate and key
[certs] etcd/peer serving cert is signed for DNS names [node213 localhost] and IPs [192.168.77.213 127.0.0.1 ::1]
[certs] Generating "etcd/healthcheck-client" certificate and key
[certs] Generating "apiserver-etcd-client" certificate and key
[certs] Generating "apiserver" certificate and key
[certs] apiserver serving cert is signed for DNS names [node213 kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local] and IPs [10.96.0.1 192.168.77.213 192.168.77.219]
[certs] Generating "apiserver-kubelet-client" certificate and key
[certs] Valid certificates and keys now exist in "/etc/kubernetes/pki"
[certs] Using the existing "sa" key
[kubeconfig] Generating kubeconfig files
[kubeconfig] Using kubeconfig folder "/etc/kubernetes"
[endpoint] WARNING: port specified in controlPlaneEndpoint overrides bindPort in the controlplane address
[kubeconfig] Writing "admin.conf" kubeconfig file
[kubeconfig] Writing "controller-manager.conf" kubeconfig file
[kubeconfig] Writing "scheduler.conf" kubeconfig file
[control-plane] Using manifest folder "/etc/kubernetes/manifests"
[control-plane] Creating static Pod manifest for "kube-apiserver"
[control-plane] Creating static Pod manifest for "kube-controller-manager"
[control-plane] Creating static Pod manifest for "kube-scheduler"
[check-etcd] Checking that the etcd cluster is healthy
[kubelet-start] Downloading configuration for the kubelet from the "kubelet-config-1.14" ConfigMap in the kube-system namespace
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Activating the kubelet service
[kubelet-start] Waiting for the kubelet to perform the TLS Bootstrap...
[etcd] Announced new etcd member joining to the existing etcd cluster
[etcd] Wrote Static Pod manifest for a local etcd member to "/etc/kubernetes/manifests/etcd.yaml"
[etcd] Waiting for the new etcd member to join the cluster. This can take up to 40s
[upload-config] storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[mark-control-plane] Marking the node node213 as control-plane by adding the label "node-role.kubernetes.io/master=''"
[mark-control-plane] Marking the node node213 as control-plane by adding the taints [node-role.kubernetes.io/master:NoSchedule]

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


按照说明，拷贝 kubectl 配置文件并验证：

```bash
[root@node213 ~]# mkdir -p $HOME/.kube
[root@node213 ~]# sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
[root@node213 ~]# sudo chown $(id -u):$(id -g) $HOME/.kube/config
[root@node213 ~]# kubectl get node
NAME      STATUS   ROLES    AGE     VERSION
node211   Ready    master   11m     v1.14.3
node212   Ready    master   4m39s   v1.14.3
node213   Ready    master   72s     v1.14.3
```


### 8. 添加其他 node 节点

按照 node211 初始化提示，添加 node214 节点到集群，角色为 node：

```bash
[root@node214 ~]# kubeadm join 192.168.77.219:8443 --token ptuvy5.hl4rzxugpxpgkgkh \
>     --discovery-token-ca-cert-hash sha256:2a190612b1e3a68a549d02b42335bfba4dd4af3bb1361124ad46862e1ab418d4 
[preflight] Running pre-flight checks
	[WARNING Hostname]: hostname "node214" could not be reached
	[WARNING Hostname]: hostname "node214": lookup node214 on 192.168.64.215:53: no such host
	[WARNING Service-Kubelet]: kubelet service is not enabled, please run 'systemctl enable kubelet.service'
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -oyaml'
	[WARNING RequiredIPVSKernelModulesAvailable]: 

The IPVS proxier may not be used because the following required kernel modules are not loaded: [ip_vs_wrr ip_vs_sh ip_vs_rr]
or no builtin kernel IPVS support was found: map[ip_vs:{} ip_vs_rr:{} ip_vs_sh:{} ip_vs_wrr:{} nf_conntrack_ipv4:{}].
However, these modules may be loaded automatically by kube-proxy if they are available on your system.
To verify IPVS support:

   Run "lsmod | grep 'ip_vs|nf_conntrack'" and verify each of the above modules are listed.

If they are not listed, you can use the following methods to load them:

1. For each missing module run 'modprobe $modulename' (e.g., 'modprobe ip_vs', 'modprobe ip_vs_rr', ...)
2. If 'modprobe $modulename' returns an error, you will need to install the missing module support for your kernel.

[kubelet-start] Downloading configuration for the kubelet from the "kubelet-config-1.14" ConfigMap in the kube-system namespace
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Activating the kubelet service
[kubelet-start] Waiting for the kubelet to perform the TLS Bootstrap...

This node has joined the cluster:
* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the control-plane to see this node join the cluster.
```

至此 kubeadm 配合 keepalived & haproxy 搭建高可用集群就完成了。

```bash
[root@node211 ~]# kubectl get node
NAME      STATUS   ROLES    AGE     VERSION
node211   Ready    master   4h10m   v1.14.3
node212   Ready    master   4h3m    v1.14.3
node213   Ready    master   4h      v1.14.3
node214   Ready    <none>   3h57m   v1.14.3
[root@node211 ~]# kubectl get pod -n kube-system
NAME                              READY   STATUS    RESTARTS   AGE
coredns-d5947d4b-rn2wl            1/1     Running   0          4h10m
coredns-d5947d4b-zdptx            1/1     Running   0          4h10m
etcd-node211                      1/1     Running   0          4h9m
etcd-node212                      1/1     Running   0          4h3m
etcd-node213                      1/1     Running   0          4h
kube-apiserver-node211            1/1     Running   0          4h9m
kube-apiserver-node212            1/1     Running   1          4h3m
kube-apiserver-node213            1/1     Running   0          3h59m
kube-controller-manager-node211   1/1     Running   1          4h9m
kube-controller-manager-node212   1/1     Running   0          4h2m
kube-controller-manager-node213   1/1     Running   0          3h59m
kube-flannel-ds-amd64-gchpj       1/1     Running   0          4h
kube-flannel-ds-amd64-mx44p       1/1     Running   0          3h57m
kube-flannel-ds-amd64-vzk7c       1/1     Running   0          4h7m
kube-flannel-ds-amd64-x9rm7       1/1     Running   0          4h3m
kube-proxy-fj448                  1/1     Running   0          4h
kube-proxy-jmhm7                  1/1     Running   0          4h3m
kube-proxy-s7jdf                  1/1     Running   0          3h57m
kube-proxy-w5gsg                  1/1     Running   0          4h10m
kube-scheduler-node211            1/1     Running   1          4h9m
kube-scheduler-node212            1/1     Running   0          4h2m
kube-scheduler-node213            1/1     Running   0          3h59m
```

### HA 机制

由集群节点上运行的 keepalived & haproxy 提供 VIP & LB，集群中所有节点的 kubelet 连接至 VIP:<haproxy port> EndPoints。

当 VIP 所在节点发生故障，VIP 切换到集群中其他 master 节点，即可正常提供服务。

### 坑

1. kubeadm 需要正常网络支持，需要确保自己处于正常网络环境下；
2. kubeadm 在添加节点时，有可能会 hang 住，未查明原因；
3. kubeadm 默认生成证书有效期为 1年，若想要修改，则需要手动生成证书替换；
4. ...

## kubespray

因为 kubespray 项目主要使用 ansible 配合 kubeadm 部署，具体内容可以直接查看 github 文档，因此不详细记录具体步骤。

### 环境信息

ip | role |
--- | --- | 
192.168.77.201 | master
192.168.77.202 | master
192.168.77.203 | master 
192.168.77.204 | node



### 1. 安装 kubespray

在 GitHub [项目链接](https://github.com/kubernetes-sigs/kubespray/releases)上下载最新 Release 版本代码。

```bash
[root@node201 ~]# wget https://github.com/kubernetes-sigs/kubespray/archive/v2.10.3.tar.gz
```

### 2. 安装必要依赖

项目依赖于 Python3，所以这里采用 Python3.6 版本进行安装。

```bash
[root@node201 kubespray-2.10.3]# yum install python36
[root@node201 kubespray-2.10.3]# yum install python36-pip
[root@node201 kubespray-2.10.3]# pip3 install -r requirements.txt 
```

3. 生成 ansible inventory

项目默认提供了一个 Python 脚本用于自动生成 inventory，该脚本生成 inventory 通常需要根据实际情况自己调整。

```bash
[root@node201 kubespray-2.10.3]# cp -rfp inventory/sample inventory/mycluster
[root@node201 kubespray-2.10.3]# declare -a IPS=(192.168.77.201 192.168.77.202 192.168.77.203 192.168.77.203)
[root@node201 kubespray-2.10.3]# CONFIG_FILE=inventory/mycluster/hosts.yml python3 contrib/inventory_builder/inventory.py ${IPS[@]}
DEBUG: Adding group all
DEBUG: Adding group kube-master
DEBUG: Adding group kube-node
DEBUG: Adding group etcd
DEBUG: Adding group k8s-cluster
DEBUG: Adding group calico-rr
DEBUG: Skipping existing host 192.168.77.203.
DEBUG: adding host node1 to group all
DEBUG: adding host node2 to group all
DEBUG: adding host node3 to group all
DEBUG: adding host node1 to group etcd
DEBUG: adding host node2 to group etcd
DEBUG: adding host node3 to group etcd
DEBUG: adding host node1 to group kube-master
DEBUG: adding host node2 to group kube-master
DEBUG: adding host node1 to group kube-node
DEBUG: adding host node2 to group kube-node
DEBUG: adding host node3 to group kube-node
```

查看生成 inventory 结果：

```bash
[root@node201 kubespray-2.10.3]# cat inventory/mycluster/hosts.yml 
all:
  hosts:
    node1:
      ansible_host: 192.168.77.201
      ip: 192.168.77.201
      access_ip: 192.168.77.201
    node2:
      ansible_host: 192.168.77.202
      ip: 192.168.77.202
      access_ip: 192.168.77.202
    node3:
      ansible_host: 192.168.77.203
      ip: 192.168.77.203
      access_ip: 192.168.77.203
  children:
    kube-master:
      hosts:
        node1:
        node2:
    kube-node:
      hosts:
        node1:
        node2:
        node3:
    etcd:
      hosts:
        node1:
        node2:
        node3:
    k8s-cluster:
      children:
        kube-master:
        kube-node:
    calico-rr:
      hosts: {}
```

可以看到跟我们计划中的有所差别，根据实际情况调整 kube-master 数量即可。

### 4. 编写部署配置参数

在 `[root@node201 kubespray-2.10.3]# ls inventory/mycluster/group_vars/all/all.yml` 路径下包含了一些全局配置，比如 proxy 之类的，可以手动调整。

### 5. 编写 k8s 配置参数

在 `[root@node201 kubespray-2.10.3]# ls inventory/mycluster/group_vars/k8s-cluster/k8s-cluster.yml ` 路径下包含了 k8s 所有配置项，根据实际情况编辑修改。


### 6. 部署

在所有准备工作完成后，执行部署操作。

注意， Kubespray 部署的前提条件是你的网络是一个正常的网络，可以正常访问所有网站，若无法访问，则根据自身实际情况，调整配置，配置路径为： `roles/download/defaults/main.yml` 。

```bash
ansible-playbook -i inventory/mycluster/hosts.yml --become --become-user=root cluster.yml
```

等待部署完成即可。

### HA 机制

集群中所有的 Node 节点自己启动一个 Nginx Static Pod，用于代理转发，将所有指定 `127.0.0.1:6443` 的请求转发至所有 master 节点真实 apiserver ，这样所有的 kubelet 只需要自己节点即可，无需其他节点参与。



### 坑 

1. CentOS 默认 Python2.7，需要单独安装 Python3.6
2. 通过 pip 安装依赖，部分软件包需要 gcc,python36-devel,openssl-devel 等依赖包，需要根据错误提示自行安装，文档中没有提到
3. 默认会安装 docker & containerd 服务，但是 containerd 服务未设置开机自启动，会导致 docker 无法自动运行
4. 在安装过程中，会安装 selinux 相应 Python 库，但是该依赖未在 `requirements.txt ` 声明
5. ...



## 总结

无论是直接只用 kubeadm + vip 方式部署 HA 集群，还是通过 Kubespray 部署，在网络正常情况下，是很快可以完成的。

在使用 kubeadm 过程中，因为无需引入第三方依赖库，导致整体流程顺畅，体验极佳。

在 Kubespray 过程中，因为采用 Python3 方式，但相关依赖又未显示声明，导致部署过程繁琐。但是也比较好理解，Kubespray 作为一个致力于部署企业级 k8s 集群的项目，需要处理大量的边界条件了，这个项目中 YAML 就写了 15k 行，可见一斑。

