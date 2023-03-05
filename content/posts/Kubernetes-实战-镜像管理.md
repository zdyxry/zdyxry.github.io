---
title: Kubernetes 实战-镜像管理
date: 2019-05-24 07:35:08
tags:
- Kubernetes
---

## 镜像组织形式
镜像默认采用 OverlayFS 方式挂载，最终效果是将多个目录结构合并为一个。

其中 lowerdir 为只读路径，最右层级最深。最终容器运行时会将 lowerdir 和 upperdir 合并挂在为 merged，对应容器中的路径为 `/` 。
举例：
镜像 testadd:0.5 版本的层级挂载如下：

```
[root@node111 16:02:24 overlay2]$docker inspect testadd:0.5 |grep Dir
            "WorkingDir": "",
            "WorkingDir": "",
                "LowerDir": "/var/lib/docker/overlay2/693c140b9c70744a7a6ce93de56d3ac7549dae84195cbfac3486062d1ceaccf1/diff",
                "MergedDir": "/var/lib/docker/overlay2/e2f2ad8332a9567ad28495b28342b5f5712218e235b0129435abfc3c781be957/merged",
                "UpperDir": "/var/lib/docker/overlay2/e2f2ad8332a9567ad28495b28342b5f5712218e235b0129435abfc3c781be957/diff",
                "WorkDir": "/var/lib/docker/overlay2/e2f2ad8332a9567ad28495b28342b5f5712218e235b0129435abfc3c781be957/work"
```


运行该容器后，可以看到多了一个 overlay 方式挂载的路径：

```
[root@node111 16:05:53 overlay2]$mount |grep overlay
/dev/md127 on /var/lib/docker/overlay2 type ext4 (rw,relatime,data=ordered)
overlay on /var/lib/docker/overlay2/e1378dc042b534fe00ca6f4565e399f30d56c81d434a30a6137cfae6b5355d00/merged type overlay (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/3NA23BH5OMSSXWTHGPRS6YENB7:/var/lib/docker/overlay2/l/QQVS7UVPGRBVHRZOBDPMMO4EQM:/var/lib/docker/overlay2/l/E7HTYBVD5SXSZRLVTETODOIANT,upperdir=/var/lib/docker/overlay2/e1378dc042b534fe00ca6f4565e399f30d56c81d434a30a6137cfae6b5355d00/diff,workdir=/var/lib/docker/overlay2/e1378dc042b534fe00ca6f4565e399f30d56c81d434a30a6137cfae6b5355d00/work)
```


查看对应关系：

```
[root@node111 16:05:53 overlay2]$mount |grep overlay
/dev/md127 on /var/lib/docker/overlay2 type ext4 (rw,relatime,data=ordered)
overlay on /var/lib/docker/overlay2/e1378dc042b534fe00ca6f4565e399f30d56c81d434a30a6137cfae6b5355d00/merged type overlay (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/3NA23BH5OMSSXWTHGPRS6YENB7:/var/lib/docker/overlay2/l/QQVS7UVPGRBVHRZOBDPMMO4EQM:/var/lib/docker/overlay2/l/E7HTYBVD5SXSZRLVTETODOIANT,upperdir=/var/lib/docker/overlay2/e1378dc042b534fe00ca6f4565e399f30d56c81d434a30a6137cfae6b5355d00/diff,workdir=/var/lib/docker/overlay2/e1378dc042b534fe00ca6f4565e399f30d56c81d434a30a6137cfae6b5355d00/work)
[root@node111 16:06:07 overlay2]$docker inspect testadd:0.5 |grep Dir                                                             
            "WorkingDir": "",
            "WorkingDir": "",
                "LowerDir": "/var/lib/docker/overlay2/693c140b9c70744a7a6ce93de56d3ac7549dae84195cbfac3486062d1ceaccf1/diff",
                "MergedDir": "/var/lib/docker/overlay2/e2f2ad8332a9567ad28495b28342b5f5712218e235b0129435abfc3c781be957/merged",
                "UpperDir": "/var/lib/docker/overlay2/e2f2ad8332a9567ad28495b28342b5f5712218e235b0129435abfc3c781be957/diff",
                "WorkDir": "/var/lib/docker/overlay2/e2f2ad8332a9567ad28495b28342b5f5712218e235b0129435abfc3c781be957/work"
[root@node111 16:06:54 overlay2]$docker ps 
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS               NAMES
e53180ddcd03        testadd:0.5         "bash"              About a minute ago   Up About a minute                       compassionate_roentgen
[root@node111 16:07:06 overlay2]$docker inspect e53180ddcd03 |grep Dir
                "LowerDir": "/var/lib/docker/overlay2/e1378dc042b534fe00ca6f4565e399f30d56c81d434a30a6137cfae6b5355d00-init/diff:/var/lib/docker/overlay2/e2f2ad8332a9567ad28495b28342b5f5712218e235b0129435abfc3c781be957/diff:/var/lib/docker/overlay2/693c140b9c70744a7a6ce93de56d3ac7549dae84195cbfac3486062d1ceaccf1/diff",
                "MergedDir": "/var/lib/docker/overlay2/e1378dc042b534fe00ca6f4565e399f30d56c81d434a30a6137cfae6b5355d00/merged",
                "UpperDir": "/var/lib/docker/overlay2/e1378dc042b534fe00ca6f4565e399f30d56c81d434a30a6137cfae6b5355d00/diff",
                "WorkDir": "/var/lib/docker/overlay2/e1378dc042b534fe00ca6f4565e399f30d56c81d434a30a6137cfae6b5355d00/work"
            "WorkingDir": "",
```



查看容器内根分区，并在容器内创建文件，查看容器挂载 merged 路径下文件

```
[root@e53180ddcd03 /]# ls 
anaconda-post.log  bin  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  test  tmp  usr  var
[root@e53180ddcd03 /]# touch yiran
[root@e53180ddcd03 /]# ls anaconda-post.log  bin  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  test  tmp  usr  var  yiran
[root@e53180ddcd03 /]# 
```

```
[root@node111 16:07:13 overlay2]$cd e1378dc042b534fe00ca6f4565e399f30d56c81d434a30a6137cfae6b5355d00/merged/
You have mail in /var/spool/mail/root
[root@node111 16:09:31 merged]$ls 
anaconda-post.log  bin  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  test  tmp  usr  var  yiran
[root@node111 16:09:32 merged]$pwd
/var/lib/docker/overlay2/e1378dc042b534fe00ca6f4565e399f30d56c81d434a30a6137cfae6b5355d00/merged
```
在容器中创建的文件 `yiran` 在宿主机相应的挂载路径下是可以看到的。

## 镜像管理

### 下载

默认从 docker.io 获取最新镜像，可以在 /etc/docker/daemon.json 中指定 `registry-mirrors` 或 `insecure-registries` 获取私有镜像。

下载完成后可以看到镜像下载完成后会在 `/var/lib/docker/overlay2/` 下保存一份镜像真实内容。

```
[root@node111 16:17:15 docker]$docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
[root@node111 16:17:19 docker]$du -sh . 
624K    .
[root@node111 16:17:21 docker]$docker pull centos
Using default tag: latest
Trying to pull repository docker.io/library/centos ... 
latest: Pulling from docker.io/library/centos
8ba884070f61: Pull complete 
Digest: sha256:b5e66c4651870a1ad435cd75922fe2cb943c9e973a9673822d1414824a1d0475
Status: Downloaded newer image for docker.io/centos:latest
[root@node111 16:18:06 docker]$docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
docker.io/centos    latest              9f38484d220f        2 months ago        202 MB
[root@node111 16:18:17 docker]$du -sh . 
214M    .
[root@node111 16:18:19 docker]$ll overlay2/*
overlay2/6061bd16e5de86e56298bee1496e02998e6a029c34374b21bc0fa3c30202db55:
total 8
drwxr-xr-x 16 root root 4096 May 22 16:18 diff
-rw-r--r--  1 root root   26 May 22 16:17 link

overlay2/l:
total 4
lrwxrwxrwx 1 root root 72 May 22 16:17 A3LUDFNM6LHHPQ6DVXCEI2KFYQ -> ../6061bd16e5de86e56298bee1496e02998e6a029c34374b21bc0fa3c30202db55/diff
```



### 构建
在不同服务构建镜像时，应保证最小化且合理分层，这样可以在最底层使用相同的 overlay 缓存，比较空间浪费。
参考 OpenStack Kolla 项目层级结构，openstack 所有服务镜像均基于 CentOS，60+服务镜像打包占用总空间为 5.48G：

注意：
尽量使用最精简基础镜像，只安装必要软件包
合理拆分服务
尽量保证 Dockerfile 中上层指令相同，若顺序不同则会构建出不同的层级，无法利用缓存特性
保证层级处于最精简状态
...

### 上传
当我们本地存在一份镜像，想要将其上传至指定仓库，我们需要先对镜像打 tag，举例：

```
[root@node111 16:24:55 image]$docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
testadd             0.2                 4e47f016385b        35 seconds ago      202 MB
docker.io/centos    latest              9f38484d220f        2 months ago        202 MB
[root@node111 16:25:07 image]$cat /etc/docker/daemon.json 
{
  "insecure-registries": [
    "192.168.27.146"
  ]
}
[root@node111 16:25:12 image]$docker tag testadd:0.2 192.168.27.146/testadd:0.2
[root@node111 16:25:28 image]$docker images
REPOSITORY               TAG                 IMAGE ID            CREATED             SIZE
192.168.27.146/testadd   0.2                 4e47f016385b        58 seconds ago      202 MB
testadd                  0.2                 4e47f016385b        58 seconds ago      202 MB
docker.io/centos         latest              9f38484d220f        2 months ago        202 MB
[root@node111 16:25:31 image]$docker push 192.168.27.146/testadd:0.2
The push refers to a repository [192.168.27.146/testadd]
f5011c15a820: Pushed 
d69483a6face: Layer already exists 
0.2: digest: sha256:072611b154402d0760d7860374eb5dc706712319331710b4f046e043ba2cc26a size: 736
```

上传到指定仓库之后，其他节点可以修改 docker 配置文件，重启 docker 后即可直接下载指定镜像。

## Kubernetes 镜像管理

### 下载
在 k8s 中，没有针对镜像仓库的集群级别配置，节点各自维护自己的仓库地址，如果需要增加仓库地址，需要修改集群中所有节点配置文件，重启 docker 生效。

---
**20190531 更新**

针对 k8s 中私有仓库的使用更新：
1. 当 k8s 想要配置 http 私有仓库时，只能通过在节点上修改 docker 配置文件 /etc/docker/daemon.json ，添加  "insecure-registries" 字段，并重启 docker 后，k8s 可以自动拉取所需镜像；
2. 当 k8s 配置 https 私有仓库时，只需将根证书拷贝到 k8s 节点的 /etc/docker/certs.d/<domain.com>/ 下，创建 k8s secret docker-registry ，在 YAML 中指定拉取镜像所需的 secret，就可以自动拉取了。

---

可以在 k8s 中配置指定仓库的 secret 类型为 docker-registry 来配置私有仓库的用户名密码，在之后创建 Pod 时指定该 secret 名称即可自动下载，具体操作如下：

```
[root@node3 ~]# kubectl create secret docker-registry regsecret --docker-server=192.168.30.111 --docker-username=admin --docker-password=Harbor12345 --docker-email=yiran@smartx.com
[root@node3 ~]# kubectl get secret regsecret -o yaml
[root@node3 ~]# cat private-reg-pod.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: private-reg
spec:
  nodeSelector:
    type: "233"
  containers:
  - name: private-reg-container
    image: 192.168.30.111/test/busybox:latest
    args: [/bin/sh, -c,
           'i=0; while true; do echo "$i: $(date)"; i=$((i+1)); sleep 1; done']
  imagePullSecrets:
  - name: regsecret
```

### 删除
k8s 自身不提供主动删除节点中无用镜像操作，默认通过配置 GC 参数删除无用镜像。

不推荐使用其它管理工具或手工进行容器和镜像的清理，因为kubelet需要通过容器来判断pod的运行状态，如果使用其它方式清除容器有可能影响kubelet的正常工作。

* --image-gc-high-threshold int32
当用于存储镜像的磁盘使用率达到百分之--image-gc-high-threshold时将触发镜像回收(default 85)

* --image-gc-low-threshold int32
删除最近最久未使用（LRU，Least Recently Used）的镜像直到磁盘使用率降为百分之--image-gc-low-threshold或无镜像可删为止 (default 80)


## CNCF-Harbor
Harbor项目是一个具有存储、签署和扫描内容功能的开源云原生registry。Harbor 由 VMware 创建，通过添加用户所需功能（如安全性，身份认证和管理）来扩展开源Docker Distribution，并支持在registry之间复制镜像。Harbor还提供高级安全功能，比如漏洞分析，基于角色的访问控制，活动审计等等。
主要功能：

* 角色控制/身份校验
* 镜像复制
* 漏洞扫描
* …


资源消耗情况：

```
[root@node111 11:09:02 harbor]$docker stats --no-stream
CONTAINER ID        NAME                CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
90dcf1505eb0        nginx               0.02%               4.152MiB / 15.51GiB   0.03%               6.53MB / 6.77MB     0B / 0B             7
75945a1aa004        harbor-jobservice   0.12%               9.109MiB / 15.51GiB   0.06%               1.24MB / 15.1MB     0B / 0B             13
000f6f349708        harbor-portal       0.07%               1.676MiB / 15.51GiB   0.01%               200kB / 5.47MB      0B / 0B             2
84635df4fe51        harbor-core         0.53%               12.96MiB / 15.51GiB   0.08%               3.62MB / 2.84MB     0B / 0B             14
c6e53b654127        redis               0.18%               6.816MiB / 15.51GiB   0.04%               15.4MB / 1.41MB     0B / 180kB          5
9048a587cf29        registryctl         0.06%               3.031MiB / 15.51GiB   0.02%               114kB / 87.8kB      0B / 0B             7
d88f7c4b36c5        harbor-db           0.03%               8.09MiB / 15.51GiB    0.05%               929kB / 1.57MB      0B / 4.65MB         11
83c474625566        registry            0.20%               19.45MiB / 15.51GiB   0.12%               1.04MB / 335kB      0B / 1.65MB         16
5a3d2707e96f        harbor-log          0.00%               2.152MiB / 15.51GiB   0.01%               766kB / 147kB       81.9kB / 16.4kB     12
```

默认推荐部署方式：docker-composer
k8s 推荐部署方式：Helm

## 总结
在日常开发过程中，公司内部部署私有仓库（比如 Harbor）可以控制用户角色，方便测试同学快速获取最新版本镜像。
在融合产品生命周期中，只有升级场景涉及到镜像的导入、上传、下载、删除操作，因此没必要在集群中持续运行一个仓库服务，浪费资源。

## 参考链接
openstack kolla 项目，目标是通过容器化方式部署 openstack，便于 openstack 滚动升级。

