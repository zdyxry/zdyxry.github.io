---
title: Podman 初次体验
date: 2019-10-12 21:40:30
tags:
- Linux
---

## 背景

CentOS8 在9月24号正式 Release 了，比 RHEL8 要推迟了4个月。这次的更新感觉比 CentOS7 的更新要来的重要，内核更新到了4.x，网络管理彻底替换了 network.service，防火墙管理等等，还包括去除了 Docker 作为默认的容器化管理工具，使用 Podman、Buildah、Skopeo 进行了替换，这里来体验下 Podman。

容器工具体验系列：
* [Podman 初次体验](https://zdyxry.github.io/2019/10/12/Podman-%E5%88%9D%E6%AC%A1%E4%BD%93%E9%AA%8C/)
* [Buildah 初次体验](https://zdyxry.github.io/2019/10/19/Buildah-%E5%88%9D%E6%AC%A1%E4%BD%93%E9%AA%8C/)
* [Skopeo 初次体验](https://zdyxry.github.io/2019/10/26/Skopeo-初次体验/)


本篇文章所有环境基于 CentOS8。

## Podman

为啥不用 Docker 了？我个人觉得 Docker 目前使用上最大的问题就是需要运行一个守护进程，虽然需要 root 用户也是一个问题，但是对于我个人来说还好。随着 K8S 定义 CRI 标准，且 Docker 的稳定性一直是个问题（虽然最近有在往好的趋势发展），但越来越多人使用 CRI-O 来替代 Docker，Docker 在被大家所抛弃（- - 

Podman 创建的容器不需要守护进程，且可以用普通用户创建容器。Podman 中的大部分命令的使用方式与 Docker 相同，可以看左 `alias docker=podman` 。

Podman 的缺点：
1. 仅在 Linux 下支持，无法像 Docker 一样支持 Windows 和 MacOS
2. 缺少 docker-compose 工具替代品，哪怕有 k8s Pod 概念（虽然有 [podman-compose](https://github.com/containers/podman-compose)，但是他还没有release 1.0版本，使用需谨慎
3. 更新频繁（使用这类工具是有些心累的。。


### 安装

Podman 可以直接使用 `dnf` 继续安装，需要注意的是，在 CentOS 中 Podman 依赖于 containers-common，这里会附带很多配置信息到 `/etc/containers`，后续会用到：

```bash
yiran@yiran-centos8:~ 
 $ sudo dnf install podman                      
Last metadata expiration check: 0:03:31 ago on Wed 02 Oct 2019 11:57:25 AM CST.
Package podman-1.0.0-2.git921f98f.module_el8.0.0+58+91b614e7.x86_64 is already installed.
Dependencies resolved.
Nothing to do.
Complete!
yiran@yiran-centos8:~ 
 $ dnf info podman        
Installed Packages
Name         : podman
Version      : 1.0.0
Release      : 2.git921f98f.module_el8.0.0+58+91b614e7
Arch         : x86_64
Size         : 37 M
Source       : podman-1.0.0-2.git921f98f.module_el8.0.0+58+91b614e7.src.rpm
Repo         : @System
From repo    : AppStream
Summary      : Manage Pods, Containers and Container Images
URL          : https://github.com/containers/libpod
License      : ASL 2.0
Description  : Manage Pods, Containers and Container Images
             : libpod provides a library for applications looking to use
             : the Container Pod concept popularized by Kubernetes.

```


### 配置

安装完成后，来看下 Podman RPM 中附带了些什么文件：

```bash
yiran@yiran-centos8:~ 
 $ rpm -ql podman  |grep -v '/usr/share/man/'  # 去除 man 手册中内容
/etc/cni/net.d/87-podman-bridge.conflist
/usr/bin/podman
/usr/lib/.build-id
/usr/lib/.build-id/37
/usr/lib/.build-id/37/e7f04d352e5dbde603e9701baedb0b1be6bc37
/usr/lib/.build-id/9a
/usr/lib/.build-id/9a/2b43332ca5756f9e2a086bae9b953009ef5a37
/usr/lib/systemd/system/io.podman.service
/usr/lib/systemd/system/io.podman.socket
/usr/lib/tmpfiles.d/podman.conf
/usr/libexec/podman/conmon
/usr/share/bash-completion/completions/podman
/usr/share/containers/libpod.conf
/usr/share/licenses/podman
/usr/share/licenses/podman/LICENSE
```

可以看到只有一个配置文件是在 `/etc/cni` 路径下的，与 Bridge 的配置有关：

```bash
yiran@yiran-centos8:~ 
 $ cat /etc/cni/net.d/87-podman-bridge.conflist
{
    "cniVersion": "0.3.0",
    "name": "podman",
    "plugins": [
      {
        "type": "bridge",
        "bridge": "cni0",
        "isGateway": true,
        "ipMasq": true,
        "ipam": {
            "type": "host-local",
            "subnet": "10.88.0.0/16",
            "routes": [
                { "dst": "0.0.0.0/0" }
            ]
        }
      },
      {
        "type": "portmap",
        "capabilities": {
          "portMappings": true
        }
      }
    ]
}

```

在上面我们有提到，Podman 依赖的 containers-common RPM 中包含了很多配置文件，我们一个一个的来看一下：

#### registries.conf

/etc/containers/registries.conf 用于保存 registries 相关配置：

```bash
yiran@yiran-centos8:~ 
 $ cat /etc/containers/registries.conf         
# This is a system-wide configuration file used to
# keep track of registries for various container backends.
# It adheres to TOML format and does not support recursive
# lists of registries.

# The default location for this configuration file is /etc/containers/registries.conf.

# The only valid categories are: 'registries.search', 'registries.insecure', 
# and 'registries.block'.

[registries.search]
registries = ['registry.redhat.io', 'quay.io', 'docker.io']

# If you need to access insecure registries, add the registry's fully-qualified name.
# An insecure registry is one that does not have a valid SSL certificate or only does HTTP.
[registries.insecure]
registries = []


# If you need to block pull access from a registry, uncomment the section below
# and add the registries fully-qualified name.
#
# Docker only
[registries.block]
registries = []

```

#### mounts.conf

`/usr/share/containers/mounts.conf ` 在执行 `podman run` 或者 `podman build` 命令时自动挂载的路径，该路径只会在容器运行时挂载，不会提交到容器镜像中。

```bash
yiran@yiran-centos8:~ 
 $ cat /usr/share/containers/mounts.conf                               
/usr/share/rhel/secrets:/run/secrets

```

#### seccomp.json

`/usr/share/containers/seccomp.json` 是容器内允许的 seccomp 规则白名单。 seccomp（secure computing）是一种安全保护机制，一般情况下，程序可以使用所有的 syscall，但是为了避免安全问题发生，通常会指定相应的规则来保证。

```bash
yiran@yiran-centos8:~ 
 $ cat /usr/share/containers/seccomp.json

{
	"defaultAction": "SCMP_ACT_ERRNO",
	"archMap": [...],
	"syscalls": [...]
}
```

#### policy.json

`/etc/containers/policy.json`  证书安全相关配置：

```bash
yiran@yiran-centos8:~ 
 $ cat /etc/containers/policy.json      
{
    "default": [
        {
            "type": "insecureAcceptAnything"
        }
    ],
    "transports":
        {
            "docker-daemon":
                {
                    "": [{"type":"insecureAcceptAnything"}]
                }
        }
}

```

### 使用

#### 镜像


##### 构建

```bash
yiran@yiran-centos8:~/podman/hello 
 $ pwd                                                                                                                                  1 ↵
/home/yiran/podman/hello
yiran@yiran-centos8:~/podman/hello 
 $ cat Dockerfile 
FROM docker.io/library/centos:latest

RUN echo 'hello'
yiran@yiran-centos8:~/podman/hello 
 $ podman build -t hello:1.0 .    
STEP 1: FROM docker.io/library/centos:latest
STEP 2: RUN echo 'hello'
hello
--> 895ce449f0b3f1f2d8a0d2dca280cb46f4c69bb2824c93bb0e72eb49987c9050
STEP 3: COMMIT hello:1.0
--> 618f931bc244f2eaff53d9f2bcb1df97c5ddac501088d5919450a57f995173af
yiran@yiran-centos8:~/podman/hello 
 $ podman images               
REPOSITORY                             TAG      IMAGE ID       CREATED          SIZE
localhost/hello                        1.0      618f931bc244   8 seconds ago    210 MB
<none>                                 <none>   895ce449f0b3   13 seconds ago   210 MB
docker.io/library/nginx                latest   f949e7d76d63   2 weeks ago      130 MB
docker.io/library/centos               latest   67fa590cfc1c   7 weeks ago      210 MB
registry.fedoraproject.org/f27/httpd   latest   18f01f6f77ef   15 months ago    426 MB

```

##### 搜索

```bash
yiran@yiran-centos8:~ 
 $ podman search mongo |head -n 5
INDEX       NAME                                                 DESCRIPTION                                       STARS   OFFICIAL   AUTOMATED
quay.io     quay.io/hellofresh/delete-old-ahoy-mongo-dbs                                                           0                  
quay.io     quay.io/ukhomeofficedigital/mongo-34                                                                   0                  
quay.io     quay.io/utilitywarehouse/mongo-burs                                                                    0                  
quay.io     quay.io/ukhomeofficedigital/mongo                                                                      0                
```

##### 拉取


```bash
yiran@yiran-centos8:~ 
 $ podman image pull nginx
Trying to pull registry.redhat.io/nginx:latest...Failed
Trying to pull quay.io/nginx:latest...Failed
Trying to pull docker.io/nginx:latest...Getting image source signatures
Copying blob b8f262c62ec6: 25.84 MiB / 25.84 MiB [=========================] 13s
Copying blob e9218e8f93b1: 22.48 MiB / 22.48 MiB [=========================] 13s
Copying blob 7acba7289aa3: 202 B / 202 B [=================================] 13s
Copying config f949e7d76d63: 6.51 KiB / 6.51 KiB [==========================] 0s
Writing manifest to image destination
Storing signatures
f949e7d76d63befffc8eec2cbf8a6f509780f96fb3bacbdc24068d594a77f043
```

除了像 Docker 一样从网络拉取镜像，Podman 为了方便用户从 Docker 迁移过来，Podman 支持从本地的 docker daemon 中直接拉取镜像，如果没有 domain 的话，目前会自动补全 `docker.io/library/` 前缀。

```bash
yiran@yiran-centos8:~ 
 $ docker images |grep yiran
harbor.yiran.com/yiran_tuna/leader-elector                                   0.5                           129c97fdb20d        3 years ago         169MB
yiran@yiran-centos8:~ 
 $ podman pull docker-daemon:harbor.yiran.com/yiran_tuna/leader-elector:0.5
Getting image source signatures
Copying blob bf87964bccfd done
Copying blob 5f70bf18a086 done
Copying blob 3efb68385a82 done
Copying blob 5f70bf18a086 done
Copying blob 42755cf4ee95 done
Copying blob ce31f2e01592 done
Copying blob 5f70bf18a086 skipped: already exists
Copying config 129c97fdb2 done
Writing manifest to image destination
Storing signatures
129c97fdb20d5fb7a0c569994f710c2b0d5292219f189f4f66c313f7bed9f434
```

看上去一切都很美好，但是要注意下面这种错误：

```
ERRO[0005] Error pulling image ref //testimg:latest: Error committing the finished image: error adding layer with blob "sha256:caed8f108bf6721dc2709407ecad964c83a31c8008a6a21826aa4ab995df5502": Error processing tar file(exit status 1): there might not be enough IDs available in the namespace (requested 4000000:4000000 for /testfile): lchown /testfile: invalid argument
```

因为 Podman 可以用普通用户运行容器，平时操作时也都是普通用户，这时候我们就面临一个UID & GID 映射的问题，默认的 subuid 的上限是 65536，这个可以自己做相应的调整：

```bash
yiran@yiran-centos8:~/podman/hello 
 $ cat /etc/subuid
yiran:100000:65536
yiran@yiran-centos8:~/podman/hello 
 $ cat /etc/subgid
yiran:100000:65536
```

不只是在镜像拉取过程中，在操作文件时，也需要关注 UID & GID 的问题，这个是之前使用 Docker 忽略的点。


##### 列出

```bash
yiran@yiran-centos8:~ 
 $ podman images
REPOSITORY                 TAG      IMAGE ID       CREATED       SIZE
docker.io/library/nginx    latest   f949e7d76d63   7 days ago    130 MB
docker.io/library/centos   latest   67fa590cfc1c   6 weeks ago   210 MB

```

##### 检查

```bash
yiran@yiran-centos8:~ 
 $ podman image inspect docker.io/library/nginx |head -n 10
[
    {
        "Id": "f949e7d76d63befffc8eec2cbf8a6f509780f96fb3bacbdc24068d594a77f043",
        "Digest": "sha256:066edc156bcada86155fd80ae03667cf3811c499df73815a2b76e43755ebbc76",
        "RepoTags": [
            "docker.io/library/nginx:latest"
        ],
        "RepoDigests": [
            "docker.io/library/nginx@sha256:066edc156bcada86155fd80ae03667cf3811c499df73815a2b76e43755ebbc76"
        ],

```


##### 删除

```bash
yiran@yiran-centos8:~ 
 $ podman image rm docker.io/library/nginx                 
f949e7d76d63befffc8eec2cbf8a6f509780f96fb3bacbdc24068d594a77f043
yiran@yiran-centos8:~ 
 $ podman images                          
REPOSITORY                 TAG      IMAGE ID       CREATED       SIZE
docker.io/library/centos   latest   67fa590cfc1c   6 weeks ago   210 MB

```

#### 容器

##### 运行

```bash
yiran@yiran-centos8:~ 
 $ podman images                             
REPOSITORY                 TAG      IMAGE ID       CREATED       SIZE
docker.io/library/centos   latest   67fa590cfc1c   6 weeks ago   210 MB
yiran@yiran-centos8:~ 
 $ podman run -it docker.io/library/centos sh
sh-4.2# cat /etc/centos-release
CentOS Linux release 7.6.1810 (Core) 
sh-4.2# exit

```


##### 停止

```bash
yiran@yiran-centos8:~ 
 $ sudo podman ps                                                                                               
[sudo] password for yiran: 
CONTAINER ID  IMAGE                                        COMMAND               CREATED        STATUS            PORTS                   NAMES
af3d9001ad32  registry.fedoraproject.org/f27/httpd:latest  container-entrypo...  8 minutes ago  Up 8 minutes ago  0.0.0.0:8080->8080/tcp  elastic_goldwasser
yiran@yiran-centos8:~ 
 $ sudo podman stop af3d9001ad32
af3d9001ad3211f5503742ca3cca8ddca542e27d7b9e54099c56ab7e04778503
yiran@yiran-centos8:~ 
 $ sudo podman ps               
CONTAINER ID  IMAGE  COMMAND  CREATED  STATUS  PORTS  NAMES

```

##### 删除

```bash
yiran@yiran-centos8:~ 
 $ sudo podman ps -a
CONTAINER ID  IMAGE                                        COMMAND               CREATED        STATUS                     PORTS                   NAMES
af3d9001ad32  registry.fedoraproject.org/f27/httpd:latest  container-entrypo...  8 minutes ago  Exited (0) 29 seconds ago  0.0.0.0:8080->8080/tcp  elastic_goldwasser
yiran@yiran-centos8:~ 
 $ sudo podman rm af3d9001ad32                                                                                       
af3d9001ad3211f5503742ca3cca8ddca542e27d7b9e54099c56ab7e04778503
yiran@yiran-centos8:~ 
 $ sudo podman ps -a          
CONTAINER ID  IMAGE  COMMAND  CREATED  STATUS  PORTS  NAMES

```

##### checkpoint/restore

Podman 提供了类似于 git 的功能，能够对 container 进行 checkpoint(commit)，并且可以 restore(checkout)，虽然 [demo 视频](https://podman.io/blogs/2018/10/10/checkpoint-restore.html) 很美好，但是我本地想通过快照（虚拟化功能）的方式来验证，却发现因为 CRIU 的版本过低不支持该功能，等后续深度使用后再研究下这个功能的原理。

##### 健康检查

Podman 1.2.0 版本提供了 healthcheck 功能，我们在运行容器时，可以通过参数 `--healthcheck-command` 来指定健康检查的方式，然后通过 `podman healthcheck` 命令来检测：

```bash
$ sudo podman run -dt --name hc1 --healthcheck-command 'CMD-SHELL curl http://localhost || exit 1' --healthcheck-interval=0 quay.io/libpod/alpine_nginx:latest
d25ee6faaf6e5e12c09e734b1ac675385fe4d4e8b52504dd01a60e1b726e3edb
$ sudo podman healthcheck run hc1
Healthy
$ echo $?
0
```

`--healthcheck-command` 命令是在容器内执行的，所以我们需要保证容器镜像中存在相应命令； `--healthcheck-interval` 如果设置为 0 则不自动检查。

##### systemd

由于 Podman 没有 daemon ，所以没办法像 docker 一样通过指定参数 `--restart=always` 在 docker 进程启动时自动拉起镜像。 Podman 通过 systemd 来支持该功能。

首先，我们需要准备一个已经可以正常运行的容器：

```bash
yiran@yiran-centos8:~ 
 $ podman ps 
CONTAINER ID  IMAGE                                  COMMAND               CREATED                 STATUS                     PORTS  NAMES
cf6b656d4ab0  docker.io/library/envoy:latest  /usr/bin/mongod -...  Less than a second ago  Up Less than a second ago         smtx-mongodb
```

编写 systemd 配置文件，通常默认路径为： /usr/lib/systemd/system/

```bash
yiran@yiran-centos8:~ 
 $ cat /usr/lib/systemd/system/envoy.service 
[Unit]
After=network.target

[Service]
Restart=always
ExecStart=/usr/bin/podman start -a envoy
ExecStop=/usr/bin/podman stop -t 10 envoy

[Install]
WantedBy=multi-user.target
```

编写完成后，我们需要执行下 `systemctl daemon-reload` 重新加载一次配置，然后就可以通过 `systemctl` 来控制容器的启停、开机自启动了。

```bash
yiran@yiran-centos8:~ 
 $ systemctl start envoy
yiran@yiran-centos8:~ 
 $ systemctl enable envoy
Created symlink from /etc/systemd/system/multi-user.target.wants/envoy.service to /usr/lib/systemd/system/envoy.service.
[root@node99 16:28:12 ~]$systemctl status envoy
● envoy.service
   Loaded: loaded (/usr/lib/systemd/system/envoy.service; enabled; vendor preset: disabled)
  Drop-In: /etc/systemd/system/envoy.service.d
           └─cgroup.conf
   Active: active (running) since Sat 2019-10-12 20:09:34 CST; 3h 41min left
 Main PID: 47684 (podman)
   CGroup: /system.slice/system-zbs.slice/system-zbs-others.slice/envoy.service
           └─47684 /usr/bin/podman start -a envoy
```



#### Pod 


##### 创建及使用

Podman 除了像 Docker 一样提供基本的容器管理，还提供了 K8S 中的 Pod 功能（得对的起名字啊）。
对于最终要运行在 k8s 环境的同学来说，Podman 非常适合，可以很大的减少环境不通导致的工作量：Podman 的 YAML 和 k8s pod yaml 文件格式是兼容的。

首先，我们来创建一个 Pod：

```bash
yiran@yiran-centos8:~ 
 $ sudo podman pod create --name postgresql -p 5432 -p 9187
error adding Infra Container: unable to pull k8s.gcr.io/pause:3.1: unable to pull image: Error determining manifest MIME type for docker://k8s.gcr.io/pause:3.1: pinging docker registry returned: Get https://k8s.gcr.io/v2/: dial tcp 64.233.189.82:443: i/o timeout

```

了解 K8S Pod 的同学应该知道 `google_containers/pause`容器，它主要的作用是 namespace  控制和启动 init 进程，即 PID 为1。在 Podman 中也是如此，这里需要 pull pause 镜像，但是喜闻乐见的 timeout。。。。

（此处开始折腾网络）

我们重新来走一次 demo ：

```bash
yiran@yiran-centos8:~ 
 $ sudo podman pod create --name postgresql -p 5432 -p 9187  # 创建 Pod，并映射端口
17020cd16ae689f5d4e0f17468c67c3f9d3b8aa424d9e463dc8b187bb80bd328
yiran@yiran-centos8:~ 
 $ sudo podman pod ls                                      
POD ID         NAME         STATUS    CREATED         # OF CONTAINERS   INFRA ID
17020cd16ae6   postgresql   Running   7 seconds ago   1                 5f38e2d70484
yiran@yiran-centos8:~ 
 $ sudo podman pod ps 
POD ID         NAME         STATUS    CREATED          # OF CONTAINERS   INFRA ID
17020cd16ae6   postgresql   Running   23 seconds ago   1                 5f38e2d70484
yiran@yiran-centos8:~ 
 $ sudo podman run -d --pod postgresql -e POSTGRES_PASSWORD=password postgres:latest # 运行 postgresql
bb00b1087b3e86f5f8915deb9a826875f4a1f063b30ef6eb743c3ad6b155a823
yiran@yiran-centos8:~ 
 $ sudo podman run -d --pod postgresql -e DATA_SOURCE_NAME="postgresql://postgres:password@localhost:5432/postgres?sslmode=disable"  wrouesnel/postgres_exporter # 运行 postgres exporter
f1197be2aa8be6169e0a0cf3b235b951dafdc4e98afe6753c661a9871038c17c

```

首先我们创建了一个 Pod，端口映射是在 Pod 这个级别配置的，然后在这个 Pod 中，我们创建了两个 container，分别是：postgres 和 postgres_exporter ，其中 postgres_exporter 主要是暴露 metrics 用于 Prometheus 抓取进行监控。

我们可以通过 curl 相应端口来验证是否正常工作：

```bash
iran@yiran-centos8:~ 
 $ sudo podman ps -a              
CONTAINER ID  IMAGE                                                          COMMAND               CREATED        STATUS            PORTS                                           NAMES
f1197be2aa8b  docker.io/wrouesnel/postgres_exporter:latest                   /postgres_exporte...  4 minutes ago  Up 4 minutes ago                                                  quizzical_mcclintock
bb00b1087b3e  docker.io/library/postgres:latest                              docker-entrypoint...  4 minutes ago  Up 4 minutes ago                                                  kind_spence
5f38e2d70484  registry.cn-hangzhou.aliyuncs.com/google_containers/pause:3.1                        5 minutes ago  Up 5 minutes ago  0.0.0.0:5432->5432/tcp, 0.0.0.0:9187->9187/tcp  17020cd16ae6-infra
yiran@yiran-centos8:~ 
 $ curl localhost:9187/metrics                                                                                                                                 
# HELP go_gc_duration_seconds A summary of the GC invocation durations.
# TYPE go_gc_duration_seconds summary
go_gc_duration_seconds{quantile="0"} 0
go_gc_duration_seconds{quantile="0.25"} 0
go_gc_duration_seconds{quantile="0.5"} 0
go_gc_duration_seconds{quantile="0.75"} 0
go_gc_duration_seconds{quantile="1"} 0
go_gc_duration_seconds_sum 0

```

可以看到已经正确的获取到了相应 metrics 数值，可以通过 `podman pod top` 来获取当前进程状态：

```bash
yiran@yiran-centos8:~ 
 $ sudo podman pod top postgresql             
USER                PID   PPID   %CPU    ELAPSED           TTY   TIME   COMMAND
0                   1     0      0.000   6m15.74147022s    ?     0s     /pause 
postgres            1     0      0.000   5m45.755275073s   ?     0s     postgres 
postgres            51    1      0.000   5m44.755304824s   ?     0s     postgres: checkpointer    
postgres            52    1      0.000   5m44.755329093s   ?     0s     postgres: background writer    
postgres            53    1      0.000   5m44.755350888s   ?     0s     postgres: walwriter    
postgres            54    1      0.000   5m44.75537351s    ?     0s     postgres: logical replication launcher    
postgres_exporter   1     0      0.000   5m34.767207535s   ?     0s     /postgres_exporter 

```

在 Podman 中，可以简单的将 Pod 理解为 docker-compose 中的一组容器，并且可以通过 `podman pod start/stop` 来控制这组容器的启停：

```bash
yiran@yiran-centos8:~ 
 $ sudo podman pod stop postgresql                                                                      
17020cd16ae689f5d4e0f17468c67c3f9d3b8aa424d9e463dc8b187bb80bd328
yiran@yiran-centos8:~ 
 $ sudo podman pod ls              
POD ID         NAME         STATUS   CREATED         # OF CONTAINERS   INFRA ID
17020cd16ae6   postgresql   Exited   8 minutes ago   3                 5f38e2d70484
yiran@yiran-centos8:~ 
 $ sudo podman pod ps 
POD ID         NAME         STATUS   CREATED         # OF CONTAINERS   INFRA ID
17020cd16ae6   postgresql   Exited   8 minutes ago   3                 5f38e2d70484
yiran@yiran-centos8:~ 
 $ curl localhost:9187/metrics
curl: (7) Failed to connect to localhost port 9187: Connection refused
yiran@yiran-centos8:~ 
 $ sudo podman pod start postgresql                                                                                                                                                                            7 ↵
17020cd16ae689f5d4e0f17468c67c3f9d3b8aa424d9e463dc8b187bb80bd328
yiran@yiran-centos8:~ 
 $ curl localhost:9187/metrics      
# HELP go_gc_duration_seconds A summary of the GC invocation durations.
# TYPE go_gc_duration_seconds summary
go_gc_duration_seconds{quantile="0"} 0
go_gc_duration_seconds{quantile="0.25"} 0
go_gc_duration_seconds{quantile="0.5"} 0

```


##### k8s 联动

通过 `podman generate` 命令可以生成 k8s 可用的 YAML 文件：

```bash
020cd16ae689f5d4e0f17468c67c3f9d3b8aa424d9e463dc8b187bb80bd328
yiran@yiran-centos8:~ 
 $ sudo podman generate kube postgresql > postgresql.yaml
no matching entries in passwd file

```

嗯，又遇到了一个错误，在 Github 上有看到相关 issue，先忽略吧。

使用 `podman play` 命令可以直接创建完整的 Pod 及其所拥有的容器：

```bash
podman play kube postgresql.yaml
```


## 总结


如果从 Docker 迁移过来，有以下几点很纠结：
1. 说好的 rootless，但是如果你想要进行端口映射，那么还是要老老实实 sudo 的
2. 虽然 systemd 大法好，但是如果 container 直接被删除了，我要单独的管理 systemd service 配置文件（貌似可以通过 OCI hook 实现
3. 更新真的太快了
4. ...

很多同学都在说 `学不动了`，纠结归纠结，学还是要学的，说不定最后 **真香** 了呢。


上述所有功能示例都可以通过官方 Demo 项目运行：https://github.com/containers/Demos/blob/master/podman_cli/README.md。

## 参考链接
* https://podman.io/blogs/
* https://podman.io/blogs/2018/10/03/podman-remove-content-homedir.html
* https://www.redhat.com/sysadmin/rootless-podman
* https://mkdev.me/en/posts/dockerless-part-3-moving-development-environment-to-containers-with-podman
