---
title: Kubernetes 实战-踩坑记录（持续更新）
date: 2019-07-13 09:34:45
tags:
- Kubernetes
---



## 背景

在对现有服务进行容器话改造的过程中，随着对 K8S 使用程度越来越深，也渐渐的遇到了一些坑，所以开一篇博客，记录自己所遇到的坑，应该会长期更新。

### 更新记录

* 2019.07.13 02:00 来自加班中的 yiran
* 2019.07.19 06:52 早起不想去公司的 yiran

## coredns 无法解析域名

在 Kubernetes 环境中，使用 kubeadm 工具部署的集群，会自动部署 coredns 作为集群的域名服务，每当我们创建了自己的 service，都可以通过域名直接访问，不用再考虑自己多个 Pod 的 IP 不同如何连接的问题。

最近遇到多个环境出现无法解析域名的问题，具体现象如下：

1. 集群部署完成后，部署 daemonset 资源，每个节点均运行一个 busybox；
2. 在 busybox 中对 `kubernetes` 默认域名进行解析，查看解析结果。

正常情况应该是所有的 busybox 都可以正常解析才对，但是最近几个环境中均出现了 3 个node 中1个node 上的 pod 无法解析的问题，示例代码如下：

daemonset.yaml
```yaml
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
        image: "busybox:1.28.4"
        imagePullPolicy: IfNotPresent
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

```bash
[root@node11 21:28:40 ~]$for i in `kubectl get pod  -o wide  |grep ds | awk '{print $1}'`;do kubectl exec $i nslookup kubernetes;echo ;done
Server:    10.96.0.10
Address 1: 10.96.0.10

nslookup: can't resolve 'kubernetes'
command terminated with exit code 1

Server:    10.96.0.10
Address 1: 10.96.0.10 kube-dns.kube-system.svc.cluster.local

Name:      kubernetes
Address 1: 10.96.0.1 kubernetes.default.svc.cluster.local

Server:    10.96.0.10
Address 1: 10.96.0.10 kube-dns.kube-system.svc.cluster.local

Name:      kubernetes
Address 1: 10.96.0.1 kubernetes.default.svc.cluster.local

```

在第一个节点的 Pod 解析时失效，最后命令执行 1min 超时退出。

经过查看发现节点的 NetFilter 相关系统配置未生效，导致 iptables 相关功能失效，具体可以参考 [issue](https://github.com/kubernetes/kubernetes/issues/21613)。

解决方式：

```bash
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables
```


## Flannel OOM

在配置好集群业务后，发现业务时不时的出现中断情况，最开始排查业务自身问题，未发现 Pod 出现重启或异常的日志，开始排查 k8s 状态，发现在节点 `/var/log/messages` 日志中，Flannel 一直处于 OOM 状态，惨不忍睹。

之前还略微惊奇，Flannel 默认的计算资源中，内存只要 50MiB，且上限也是 50MiB，没有给自己留一丝余地，看到 [issue](https://github.com/coreos/flannel/issues/963) 中的描述，感觉这个不是一个偶发事件，最终我将 Flannel 的内存调整为 250MiB 后，未出现 OOM 情况。

issue 中提到的 `kubectl patch` 命令未自动生效，我通过更新 ds 配置，然后依次手动删除节点上的 Flannel Pod 使其生效。


## Nginx Ingress

Nginx Ingress 有多个版本，在编写 Ingress 规则的时候一定要看清自己集群中的 Nginx Ingress 版本，我最开始就是因为这个看错了文档。。

主要的版本有： `kubernetes/ingress-nginx` , `nginxinc/kubernetes-ingress with NGINX` 和 `nginxinc/kubernetes-ingress with NGINX PLUS` ，具体的对比规则可以在 [Github](https://github.com/nginxinc/kubernetes-ingress/blob/master/docs/nginx-ingress-controllers.md) 中了解。


在 `kubernetes/ingress-nginx` 中，默认 `ssl-redirect` 参数是 `true` ，如果自己的服务不支持 https，那么需要显示的声明该参数为 false 才可以，这里需要注意一下。

在配置 nginx 参数的时候，要注意语法，正确的书写方式如下：

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"networking.k8s.io/v1beta1","kind":"Ingress","metadata":{"annotations":{"kubernetes.io/ingress.class":"nginx","nginx.ingress.kubernetes.io/proxy-read-timeout":"3600","nginx.ingress.kubernetes.io/proxy-send-timeout":"3600","nginx.ingress.kubernetes.io/ssl-redirect":"true","nginx.ingress.kubernetes.io/use-regex":"true","nginx.org/websocket-services":"websockify"},"name":"websockify","namespace":"default"},"spec":{"rules":[{"http":{"paths":[{"backend":{"serviceName":"websockify","servicePort":8000},"path":"/websockify"}]}}]}}
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/proxy-read-timeout: "3600"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "3600"
```

相关 issue 链接： https://github.com/kubernetes/ingress-nginx/issues/2007 


## Docker 稳定性

在修改 Docker 配置后，需要重启 Docker.service 使配置生效，在一次重启操作中，直接导致物理节点宕机，自动重启了。。。

重启后观察物理节点日志，未发现异常日志，目前待复现调查，很坑很诡异。

## Helm values 为空更新错误

今天在给应用编写 Helm Charts 的时候，在 Values 中通过 resources.requests.cpu 方式指定了 cpu 和内存，在测试的时候忘记填写具体数值了，像这面这样：

values:
```yaml
# Default values for test.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.

resources:
  limits:
   cpu:
   memory:
  requests:
   cpu:
   memory:
```

在 helm templates 中定义 daemonset，指定使用 resources 字段。

直接执行 helm 命令安装成功了：

```bash
[root@node11 20:44:09 test]$helm install . --name-template test
NAME: test
LAST DEPLOYED: 2019-07-15 20:44:18.151073881 +0800 CST m=+0.092592446
NAMESPACE: default
STATUS: deployed

NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods -l "app=test,release=test" -o jsonpath="{.items[0].metadata.name}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl port-forward $POD_NAME 8080:80
```

我们查看创建出来的 daemonset 资源状态：

daemonset/test

```yaml

Name:           test
Selector:       app=test
Node-Selector:  <none>
Pods Status:  3 Running / 0 Waiting / 0 Succeeded / 0 Failed
Pod Template:
  Labels:  app=test
  Containers:
   test:
    Image:      harbor.zdyxry.com/test/test:0.1.2
    Port:       10402/TCP
    Host Port:  10402/TCP
    Command:
      /bin/sh
      -c
    Args:
      gunicorn -b :10402 -k gevent test.main:flask_app -w 2 --timeout 40 --pid /var/run/test.pid
    Limits:
      cpu:     0
      memory:  0
    Requests:
      cpu:        0
      memory:     0
    Environment:  <none>
```

这时候我在检查资源的时候发现自己忘记设置资源了，我计划通过更新 values 数值来更新 daemonset：

```yaml
# Default values for test.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.

resources:
  limits:
   cpu: 100m
   memory: 100Mi
  requests:
   cpu: 100m
   memory: 100Mi

```

执行 helm upgrade 时候报错：

```bash
[root@node11 20:49:36 test]$helm upgrade test .
Error: UPGRADE FAILED: error validating "": error validating data: [unknown object type "nil" in DaemonSet.spec.template.spec.containers[0].resources.limits.cpu, unknown object type "nil" in DaemonSet.spec.template.spec.containers[0].resources.limits.memory, unknown object type "nil" in DaemonSet.spec.template.spec.containers[0].resources.requests.cpu, unknown object type "nil" in DaemonSet.spec.template.spec.containers[0].resources.requests.memory]
```

根据报错信息可以看到这个字段之前是 `nil` ，现在我们要更新为有效类型更新失败，只能通过 `helm uninstall` 卸载后再次安装修复该问题。

这个问题只在 daemonset 类型下会出现。


## Flannel 网卡丢失

在通常情况下，我们的 k8s 节点都只有单一的网络环境，也就是有一块网卡，在部署 Flannel 插件的时候，默认会找默认路由所在的网卡，并将其绑定在上面。

由于内部测试环境较为特殊，我将其绑定在一个 ovs port 上，这个具体配置在 flannel yaml 中：

```yaml
      containers:
      - name: kube-flannel
        image: quay.io/coreos/flannel:v0.11.0-amd64
        command:
        - /opt/bin/flanneld
        args:
        - --ip-masq
        - --kube-subnet-mgr
        - --iface=port-storage  # 在这里我强制指定了 iface
```

正常运行时时没有问题的，但是对 ovs port 进行了 `ifdown` 操作后，在 OS 层面就无法找到这个 ovs port 了，flannel 默认的 `flannel.1` 这个 link 也丢失了，当我尝试 `ifup` ovs port，这个 port 正常恢复工作了，但是 `flannel.1` 无法自动恢复，目前找到的办法是手动重建 flannel pod。

猜测这个动作在 flannel 的init 相关步骤执行的，在之后 container 正常运行时没有考虑 `flannel.1` 不存在的情况。



## 总结

使用经验通常是踩了一个又一个坑过来的~ 


