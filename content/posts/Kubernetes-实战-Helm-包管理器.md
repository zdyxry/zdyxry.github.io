---
title: Kubernetes 实战-Helm 包管理器
date: 2019-06-21 20:40:24
tags:
- Kubernetes
---


## 简介
Helm 就是`k8s 的包管理器` 。常见的包管理器有：yum,apt,pip...

包管理器基础功能有：
* 安装
    * 依赖安装
* 升级
* 回滚
* 卸载
* 源管理
* 搜索
* ...



### 基本概念  

* Helm: Kubernetes的包管理工具，命令行同名

* Tiller: Helmv2 的服务端，用于接收并处理 Helm 发送的请求，默认以 Deployment 形式部署在 k8s 集群中

* Chart: Helm 包管理的基础单元，等同于 RPM

* Repoistory: Helm的软件源仓库，是一个 Web 服务器，路径下除了响应的软件 Chart 包之外，维护了一个 index.yaml 用于索引

* Release: Helm 安装在 Kubernetes 集群中的 Chart 实例


### 现状
helm 截至06月20日最新稳定版本为 v2.14.1。

在05月16日发布了 v3.0 alpha 版本，根据相关文档描述，v2 无法平滑升级到 v3 版本。

注：存在部分小版本无法平滑升级情况。


helm v3 版本改进：

1. 在 v2 版本设计中，需要单独创建属于 Tiller 的 ServiceAccount，授权 clusteradmin 权限，以为着只要你有 helm 权限，那么你有操作 k8s全集群所有权限。在 v3 版本中删除 Tiller，直接与 k8s api 进行通信，权限管理更清晰
2. helm 提供 libary
3. 模板引擎切换为 Lua
4. 目前通过 Hook 方式创建的资源，helm 后续不会管理，在 v3 会增加管理 Hook 资源功能
5. 目前所有配置保存在 cm 中，后续考虑保存到 secret
6. v2 需要单独维护仓库，v3 中可以将 Chart 推送到 Docker 镜像仓库中，提供 helm push/login 功能
7. ...




## Helm2 基本使用

### 安装


在 Helm Github [Release](https://github.com/helm/helm/releases) 下载最新版本二进制文件，并在本地解压。

在 k8s master 节点，执行 `helm init --server-account tiller` 将 Tiller 部署在 k8s 集群中，指定 Service Account 为 Tiller。

在 k8s 1.6 版本之后，需要创建对应的 ServiceAccount 资源给 Tiller ，便于 Tiller 后续创建资源，参考官方文档：

rbac-config.yaml
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: tiller
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: tiller
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount
    name: tiller
    namespace: kube-system
```

```bash
$ kubectl create -f rbac-config.yaml
serviceaccount "tiller" created
clusterrolebinding "tiller" created
```

通过 `helm version` 验证是否部署成功，成功会显示 client 和 server 对应版本。

```bash
[root@node1 helm]# helm version
Client: &version.Version{SemVer:"v2.14.1", GitCommit:"5270352a09c7e8b6e8c9593002a73535276507c0", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.14.1", GitCommit:"5270352a09c7e8b6e8c9593002a73535276507c0", GitTreeState:"clean"}
```


### 基本使用

#### Chart构建

本地创建一个测试软件包：

```bash
[root@node1 helm]# helm create yiran-test
Creating yiran-test
[root@node1 helm]# tree yiran-test/
yiran-test/
├── charts                            # yiran-test 所依赖的 Chart，此处为空
├── Chart.yaml                        # yiran-test 的基本信息，包含：名称，apiversion, appversion, version
├── templates
│   ├── deployment.yaml               # 配置模板路径
│   ├── _helpers.tpl                  # 用于修改kubernetes objcet配置的模板
│   ├── ingress.yaml                  # 
│   ├── NOTES.txt                     # 类似于 Chart README
│   ├── service.yaml                  # 
│   └── tests
│       └── test-connection.yaml      # 测试模板
└── values.yaml                       # 用于渲染模板的具体值

3 directories, 8 files
```

有了基础示例，我们可以先通过 `dry-run` 方式跑一下：

```bash
[root@node1 yiran-test]# helm install --dry-run --debug ./
[debug] Created tunnel using local port: '39257'

[debug] SERVER: "127.0.0.1:39257"

[debug] Original chart version: ""
[debug] CHART PATH: /root/helm/yiran-test

NAME:   torrid-rodent
REVISION: 1
RELEASED: Thu Jun 20 19:10:08 2019
CHART: yiran-test-0.1.0
USER-SUPPLIED VALUES:
{}

COMPUTED VALUES:
affinity: {}
fullnameOverride: ""
image:
  pullPolicy: IfNotPresent
  repository: nginx
  tag: stable
imagePullSecrets: []
ingress:
  annotations: {}
  enabled: false
  hosts:
  - host: chart-example.local
    paths: []
  tls: []
nameOverride: ""
nodeSelector: {}
replicaCount: 1
resources: {}
service:
  port: 80
  type: ClusterIP
tolerations: []

HOOKS:
---
# torrid-rodent-yiran-test-test-connection
apiVersion: v1
kind: Pod
metadata:
  name: "torrid-rodent-yiran-test-test-connection"
  labels:
    app.kubernetes.io/name: yiran-test
    helm.sh/chart: yiran-test-0.1.0
    app.kubernetes.io/instance: torrid-rodent
    app.kubernetes.io/version: "1.0"
    app.kubernetes.io/managed-by: Tiller
  annotations:
    "helm.sh/hook": test-success
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args:  ['torrid-rodent-yiran-test:80']
  restartPolicy: Never
MANIFEST:

```

#### 安装

可以看到生成的 YAML 文件就是拿 values.yaml 值渲染模板生成的，那么我们来安装一下：

```bash
[root@node1 yiran-test]# helm install ./
NAME:   precise-bear
LAST DEPLOYED: Thu Jun 20 19:12:01 2019
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/Deployment
NAME                     READY  UP-TO-DATE  AVAILABLE  AGE
precise-bear-yiran-test  0/1    0           0          1s

==> v1/Pod(related)
NAME                                      READY  STATUS             RESTARTS  AGE
precise-bear-yiran-test-785f967587-9rll6  0/1    ContainerCreating  0         1s

==> v1/Service
NAME                     TYPE       CLUSTER-IP     EXTERNAL-IP  PORT(S)  AGE
precise-bear-yiran-test  ClusterIP  10.68.142.106  <none>       80/TCP   1s


NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=yiran-test,app.kubernetes.io/instance=precise-bear" -o jsonpath="{.items[0].metadata.name}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl port-forward $POD_NAME 8080:80

[root@node1 yiran-test]# helm list 
NAME            REVISION    UPDATED                     STATUS      CHART               APP VERSION NAMESPACE
precise-bear    1           Thu Jun 20 19:12:01 2019    DEPLOYED    yiran-test-0.1.0    1.0         default  
[root@node1 yiran-test]# kubectl get pod 
NAME                                       READY   STATUS    RESTARTS   AGE
precise-bear-yiran-test-785f967587-9rll6   0/1     Running   0          7s
```

注意，此时我们已经创建好了对应的资源，可以通过 `kubectl` 来查看状态。

#### 升级

我们来修改一下 `yiran-test/Chart.yaml` ，调整下版本，进行升级：

```bash
[root@node1 yiran-test]# cat Chart.yaml
apiVersion: v2
appVersion: "2.0"
description: A Helm chart for Kubernetes
name: yiran-test
version: 0.2.0
[root@node1 yiran-test]# helm list 
heNAME          REVISION    UPDATED                     STATUS      CHART               APP VERSION NAMESPACE
precise-bear    1           Thu Jun 20 19:12:01 2019    DEPLOYED    yiran-test-0.1.0    1.0         default  
[root@node1 yiran-test]# helm upgrade precise-bear ./
Release "precise-bear" has been upgraded.
LAST DEPLOYED: Thu Jun 20 19:18:30 2019
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/Deployment
NAME                     READY  UP-TO-DATE  AVAILABLE  AGE
precise-bear-yiran-test  1/1    1           1          6m30s

==> v1/Pod(related)
NAME                                      READY  STATUS   RESTARTS  AGE
precise-bear-yiran-test-785f967587-9rll6  1/1    Running  0         6m30s

==> v1/Service
NAME                     TYPE       CLUSTER-IP     EXTERNAL-IP  PORT(S)  AGE
precise-bear-yiran-test  ClusterIP  10.68.142.106  <none>       80/TCP   6m30s


NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=yiran-test,app.kubernetes.io/instance=precise-bear" -o jsonpath="{.items[0].metadata.name}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl port-forward $POD_NAME 8080:80

[root@node1 yiran-test]# helm list 
NAME            REVISION    UPDATED                     STATUS      CHART               APP VERSION NAMESPACE
precise-bear    2           Thu Jun 20 19:18:30 2019    DEPLOYED    yiran-test-0.2.0    2.0         default  
```

#### 回滚

通过上述步骤，我们已经把我们的应用 `yiran-test` 从 `0.1.0` 版本升级到了 `0.2.0` 版本，那么我们现在来尝试下回滚。

helm 回滚操作需要指定 Release 名称和目标版本：


```bash
[root@node1 yiran-test]# helm list 
NAME            REVISION    UPDATED                     STATUS      CHART               APP VERSION NAMESPACE
precise-bear    2           Thu Jun 20 19:18:30 2019    DEPLOYED    yiran-test-0.2.0    2.0         default  
[root@node1 yiran-test]# helm rollback precise-bear 1
Rollback was a success.
[root@node1 yiran-test]# helm list 
NAME            REVISION    UPDATED                     STATUS      CHART               APP VERSION NAMESPACE
precise-bear    3           Thu Jun 20 19:23:04 2019    DEPLOYED    yiran-test-0.1.0    1.0         default  
```

嗯，可以看到，我们指定了回滚的目标 REVISION，回滚成功了，`yiran-test` 回到了 `0.1.0` 版本，但是，最恶心的来了，Release 的当前版本变成了 `3` ，而不是设想中的 `1` 。


#### 卸载

如果我们想要从 k8s 上卸载对应的软件，也就是我们的 `yiran-test` ，我们可以直接执行 `delete` 命令，会直接把相关资源全部删除掉。

```bash
[root@node1 ~]# helm list
NAME            REVISION        UPDATED                         STATUS          CHART                   APP VERSION     NAMESPACE
precise-bear    3               Thu Jun 20 19:23:04 2019        DEPLOYED        yiran-test-0.1.0        1.0             default
[root@node1 ~]# kubectl get pod
kuNAME                                       READY   STATUS    RESTARTS   AGE
precise-bear-yiran-test-785f967587-9rll6   1/1     Running   0          139m
[root@node1 ~]# kubectl get svc
NAME                      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
kubernetes                ClusterIP   10.68.0.1       <none>        443/TCP   36d
precise-bear-yiran-test   ClusterIP   10.68.142.106   <none>        80/TCP    139m
[root@node1 ~]# helm delete precise-bear
release "precise-bear" deleted
[root@node1 ~]# helm list
[root@node1 ~]# kubectl get pod
NAME                                       READY   STATUS        RESTARTS   AGE
precise-bear-yiran-test-785f967587-9rll6   0/1     Terminating   0          139m
[root@node1 ~]# kubectl get svc
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.68.0.1    <none>        443/TCP   36d

```

#### 软件源管理

上面我们所有的操作都是针对本地包（路径），那么我们怎么才能通过网络下载别人已经构建好的软件包呢？ 

helm 使用 `repo` 命令来管理软件源，使用上也很简单，简单列举下相应命令实用说明：

```bash
[root@node1 ~]# helm repo list
NAME    URL
stable          https://kubernetes-charts.storage.googleapis.com
local   http://127.0.0.1:8879/charts
[root@node1 ~]# helm repo add stable-mirror https://burdenbear.github.io/kube-charts-mirror/
"stable-mirror" has been added to your repositories
[root@node1 ~]# helm repo add stable https://kubernetes-charts.storage.googleapis.com
helm repo list
"stable" has been added to your repositories
[root@node1 ~]# helm repo list
NAME            URL
stable          https://kubernetes-charts.storage.googleapis.com
local           http://127.0.0.1:8879/charts
stable-mirror   https://burdenbear.github.io/kube-charts-mirror/
[root@node1 ~]# helm repo remove local
"local" has been removed from your repositories
[root@node1 ~]# helm repo list
NAME            URL
stable          https://kubernetes-charts.storage.googleapis.com
stable-mirror   https://burdenbear.github.io/kube-charts-mirror/
```

#### 软件搜索

```bash
[root@node1 ~]# helm search mongo
NAME                                            CHART VERSION   APP VERSION     DESCRIPTION
stable-mirror/mongodb                           5.20.0          4.0.10          NoSQL document-oriented database that stores JSON-like do...
stable-mirror/mongodb-replicaset                3.9.6           3.6             
...
```


#### 打包与本地软件源构建

Helm v2 命令支持本地创建软件源，命令关键字是 `helm serve` ，下面来演示下相关操作：

启动本地源，并指定 IP 地址和 repo 路径：
```bash
[root@node1 helm]# pwd
/root/helm
[root@node1 helm]# ls 
rbac-config.yaml  yiran-test
[root@node1 helm]# helm serve --address 192.168.27.231:8879 --repo-path /root/helm/ 
Regenerating index. This may take a moment.
Now serving you on 192.168.27.231:8879
```


新开终端，通过修改 `yiran-test` 的 Chart.yaml 文件打包两个版本的 Chart：

```bash
[root@node1 helm]# cat yiran-test/Chart.yaml 
apiVersion: v1
appVersion: "1.0"
description: A Helm chart for Kubernetes
name: yiran-test
version: 0.1.0
[root@node1 helm]# helm package yiran-test
Successfully packaged chart and saved it to: /root/helm/yiran-test-0.1.0.tgz
[root@node1 helm]# vi yiran-test/Chart.yaml 
[root@node1 helm]# cat yiran-test/Chart.yaml
apiVersion: v2
appVersion: "2.0"
description: A Helm chart for Kubernetes
name: yiran-test
version: 0.2.0
[root@node1 helm]# helm package yiran-test
Successfully packaged chart and saved it to: /root/helm/yiran-test-0.2.0.tgz
[root@node1 helm]# ls 
index.yaml  rbac-config.yaml  yiran-test  yiran-test-0.1.0.tgz  yiran-test-0.2.0.tgz
```

此时访问浏览器，应该只能看到空的列表，我们更新一下软件源索引：

```bash
[root@node1 helm]# helm repo index --url=http://192.168.27.231:8879 .
[root@node1 helm]# pwd
/root/helm
[root@node1 helm]# cat index.yaml 
apiVersion: v1
entries:
  yiran-test:
  - apiVersion: v2
    appVersion: "2.0"
    created: "2019-06-21T13:43:41.220764856+08:00"
    description: A Helm chart for Kubernetes
    digest: af54cfdc5f8e6463a91311496bab8fafd7364c3588b85b5e676fb930cd4e2754
    name: yiran-test
    urls:
    - http://192.168.27.231:8879/yiran-test-0.2.0.tgz
    version: 0.2.0
  - apiVersion: v1
    appVersion: "1.0"
    created: "2019-06-21T13:43:41.220059406+08:00"
    description: A Helm chart for Kubernetes
    digest: 64b94c30827aab8e52f57cd3950645bb14ae2deb44e3100d48ecd64f1e706ea5
    name: yiran-test
    urls:
    - http://192.168.27.231:8879/yiran-test-0.1.0.tgz
    version: 0.1.0
generated: "2019-06-21T13:43:41.218753007+08:00"
```

可以看到在 repo 路径下生成了一个 index.yaml 文件，这个文件就是 repo 的索引文件，我们可以直接通过浏览器访问 `http://192.168.27.231:8879` 来浏览或下载所需软件包。

也可以将本地 repo 添加到 helm 中，使用 helm 命令将软件包部署到 k8s 中：

```bash
[root@node1 helm]# helm repo list 
NAME         	URL                                             
stable       	https://kubernetes-charts.storage.googleapis.com
stable-mirror	https://burdenbear.github.io/kube-charts-mirror/
[root@node1 helm]# helm repo add local http://192.168.27.231:8879
"local" has been added to your repositories
[root@node1 helm]# helm repo list 
NAME         	URL                                             
stable       	https://kubernetes-charts.storage.googleapis.com
stable-mirror	https://burdenbear.github.io/kube-charts-mirror/
local        	http://192.168.27.231:8879                      
[root@node1 helm]# helm search yiran
NAME            	CHART VERSION	APP VERSION	DESCRIPTION                
local/yiran-test	0.2.0        	2.0        	A Helm chart for Kubernetes
```

尝试从本地源安装应用：

```bash
[root@node1 helm]# helm list 
[root@node1 helm]# helm search yiran
NAME            	CHART VERSION	APP VERSION	DESCRIPTION                
local/yiran-test	0.2.0        	2.0        	A Helm chart for Kubernetes
[root@node1 helm]# helm install local/yiran-test
NAME:   orange-chicken
LAST DEPLOYED: Fri Jun 21 13:49:45 2019
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/Deployment
NAME                       READY  UP-TO-DATE  AVAILABLE  AGE
orange-chicken-yiran-test  0/1    0           0          1s

==> v1/Pod(related)
NAME                                        READY  STATUS             RESTARTS  AGE
orange-chicken-yiran-test-7f494c67b5-q9kwp  0/1    ContainerCreating  0         1s

==> v1/Service
NAME                       TYPE       CLUSTER-IP    EXTERNAL-IP  PORT(S)  AGE
orange-chicken-yiran-test  ClusterIP  10.68.85.197  <none>       80/TCP   1s


NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=yiran-test,app.kubernetes.io/instance=orange-chicken" -o jsonpath="{.items[0].metadata.name}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl port-forward $POD_NAME 8080:80

[root@node1 helm]# helm list 
NAME          	REVISION	UPDATED                 	STATUS  	CHART           	APP VERSION	NAMESPACE
orange-chicken	1       	Fri Jun 21 13:49:45 2019	DEPLOYED	yiran-test-0.2.0	2.0        	default 
[root@node1 helm]# kubectl get pod 
NAME                                         READY   STATUS    RESTARTS   AGE
orange-chicken-yiran-test-7f494c67b5-q9kwp   1/1     Running   0          62s
```


#### Chart 依赖管理

包管理器一个比较钟要的功能就是依赖管理，当我安装 A，A 依赖于 B，那么 B 应该会自动安装完成。

我们在 `yiran-test` 中添加两个依赖，并构建：

```bash
[root@node1 helm]# cat yiran-test/requirements.yaml   # 添加 apache 和 mysql 依赖
dependencies:
  - name: apache
    version: 4.3.2
    repository: https://charts.bitnami.com
  - name: mysql
    version: 1.2.0
    repository: https://burdenbear.github.io/kube-charts-mirror/
[root@node1 helm]# tree yiran-test/ # 当前目录结构
yiran-test/
├── charts
├── Chart.yaml
├── requirements.yaml
├── templates
│   ├── deployment.yaml
│   ├── _helpers.tpl
│   ├── ingress.yaml
│   ├── NOTES.txt
│   ├── service.yaml
│   └── tests
│       └── test-connection.yaml
└── values.yaml

3 directories, 9 files
[root@node1 helm]# helm dep up yiran-test/ # 下载依赖到本地
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "local" chart repository
...Successfully got an update from the "stable" chart repository
...Successfully got an update from the "bitnami" chart repository
...Successfully got an update from the "stable-mirror" chart repository
Update Complete.
Saving 2 charts
Downloading apache from repo https://charts.bitnami.com
Downloading mysql from repo https://burdenbear.github.io/kube-charts-mirror/
Deleting outdated charts
[root@node1 helm]# tree yiran-test/ # 完整目录结构
yiran-test/
├── charts
│   ├── apache-4.3.2.tgz
│   └── mysql-1.2.0.tgz
├── Chart.yaml
├── requirements.lock
├── requirements.yaml
├── templates
│   ├── deployment.yaml
│   ├── _helpers.tpl
│   ├── ingress.yaml
│   ├── NOTES.txt
│   ├── service.yaml
│   └── tests
│       └── test-connection.yaml
└── values.yaml

3 directories, 12 files
[root@node1 helm]# helm package yiran-test
Successfully packaged chart and saved it to: /root/helm/yiran-test-0.2.0.tgz
```

可以看到 helm 对依赖的管理方式是将自己所依赖的所有 Chart，均下载到 `yiran-test/charts/` 路径下，我们打包的时候其实已经包含了所有依赖了。


再创建一个 Chart，依赖于 `yiran-test` ：

```bash
[root@node1 helm]# tree nested/
nested/
├── charts
│   └── yiran-test-0.2.0.tgz
├── Chart.yaml
├── requirements.lock
├── requirements.yaml
├── templates
│   ├── deployment.yaml
│   ├── _helpers.tpl
│   ├── ingress.yaml
│   ├── NOTES.txt
│   ├── service.yaml
│   └── tests
│       └── test-connection.yaml
└── values.yaml

3 directories, 11 files
[root@node1 helm]# cat nested/requirements.yaml 
dependencies:
  - name: yiran-test
    version: 0.2.0
    repository: http://192.168.27.231:8879
```

实际安装 `nested` ，来看下安装结果：

```bash
[root@node1 helm]# helm install nested/
NAME:   alliterating-gopher
LAST DEPLOYED: Fri Jun 21 18:22:52 2019
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/ConfigMap
NAME                            DATA  AGE
alliterating-gopher-mysql-test  1     1s

==> v1/Deployment
NAME                            READY  UP-TO-DATE  AVAILABLE  AGE
alliterating-gopher-nested      0/1    1           0          1s
alliterating-gopher-yiran-test  0/1    1           0          1s

==> v1/PersistentVolumeClaim
NAME                       STATUS   VOLUME  CAPACITY  ACCESS MODES  STORAGECLASS  AGE
alliterating-gopher-mysql  Pending  1s

==> v1/Pod(related)
NAME                                             READY  STATUS             RESTARTS  AGE
alliterating-gopher-apac-7bf7cc75d5-mhdsg        0/1    ContainerCreating  0         1s
alliterating-gopher-mysql-5db64c59d9-987vm       0/1    Pending            0         1s
alliterating-gopher-nested-6c74d785df-jdqgq      0/1    ContainerCreating  0         1s
alliterating-gopher-yiran-test-67b5cb5599-nfspm  0/1    ContainerCreating  0         1s

==> v1/Secret
NAME                       TYPE    DATA  AGE
alliterating-gopher-mysql  Opaque  2     1s

==> v1/Service
NAME                            TYPE          CLUSTER-IP     EXTERNAL-IP  PORT(S)                     AGE
alliterating-gopher-apac        LoadBalancer  10.68.35.233   <pending>    80:21195/TCP,443:26200/TCP  1s
alliterating-gopher-mysql       ClusterIP     10.68.70.173   <none>       3306/TCP                    1s
alliterating-gopher-nested      ClusterIP     10.68.190.252  <none>       80/TCP                      1s
alliterating-gopher-yiran-test  ClusterIP     10.68.217.171  <none>       80/TCP                      1s

==> v1beta1/Deployment
NAME                       READY  UP-TO-DATE  AVAILABLE  AGE
alliterating-gopher-apac   0/1    1           0          1s
alliterating-gopher-mysql  0/1    1           0          1s


NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=nested,app.kubernetes.io/instance=alliterating-gopher" -o jsonpath="{.items[0].metadata.name}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl port-forward $POD_NAME 8080:80

[root@node1 helm]# helm list 
NAME               	REVISION	UPDATED                 	STATUS  	CHART       	APP VERSION	NAMESPACE
alliterating-gopher	1       	Fri Jun 21 18:22:52 2019	DEPLOYED	nested-0.1.0	1.0        	default  
[root@node1 helm]# kubectl get pod 
NAME                                              READY   STATUS    RESTARTS   AGE
alliterating-gopher-apac-7bf7cc75d5-mhdsg         0/1     Running   0          5s
alliterating-gopher-mysql-5db64c59d9-987vm        0/1     Pending   0          5s
alliterating-gopher-nested-6c74d785df-jdqgq       0/1     Running   0          5s
alliterating-gopher-yiran-test-67b5cb5599-nfspm   1/1     Running   0          5s
```

我们可以看到 nested 已经安装完成了，同时 nested 依赖得 yiran-test 及 yiran-test 依赖得 mysql & apache 也已经安装了。

具体得依赖关系直接引用官方文档示例：

假设名为 “A” 的 chart 创建以下 Kubernetes 对象

> namespace "A-Namespace"  
statefulset "A-StatefulSet"  
service "A-Service"  

此外，A 依赖于创建对象的 chart B.

> namespace "B-Namespace"  
replicaset "B-ReplicaSet"    
service "B-Service"  

安装/升级 chart A 后，会创建/修改单个 Helm 版本。该版本将按以下顺序创建/更新所有上述 Kubernetes 对象：

> A-Namespace  
B-Namespace  
A-StatefulSet  
B-ReplicaSet  
A-Service  
B-Service  

这是因为当 Helm 安装 / 升级 charts 时，charts 中的 Kubernetes 对象及其所有依赖项都是如下

1. 聚合成一个单一的集合; 
2. 按类型排序，然后按名称排序; 
3. 按该顺序创建/更新。


因此，单个 release 是使用 charts 及其依赖关系创建的所有对象，这意味着 Helm 不管理依赖服务的相关启动顺序，要由上层应用自己控制（比如创建响应探针）。

具体的资源创建顺序可以看 Tiller [相关代码](https://github.com/helm/helm/blob/master/pkg/tiller/kind_sorter.go#L29)。

## 总结

总体来说 Helm 基础功能使用还是很方便的，关键在于我们如何划分我们应用的粒度，比如 openstack 是以组件为粒度划分的：nova Chart 包含 api、scheduler、conductor 等服务；比如 TiDB Operator 项目是以具体功能来划分的：tidb-backup、tidb-cluster、tidb-operator 。我们应该根据自己的业务需求，合理划分。

还有一点需要注意的是，Helm 项目还处于快速发展阶段（貌似涉及 k8s 的都变化太快），尤其是最近发布了 Helm3 alpha，如果是生产系统，需要考虑后续是否能够平滑升级的影响。

如果实在不喜欢 Helm Tiller 方式，单纯使用 Helm template 也是可以的。
