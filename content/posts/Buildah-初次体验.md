---
title: Buildah 初次体验
date: 2019-10-19 10:15:39
tags:
- Linux
---

## 背景

上周体验了 [Podman](https://zdyxry.github.io/2019/10/12/Podman-%E5%88%9D%E6%AC%A1%E4%BD%93%E9%AA%8C/) 来管理容器的构建、生命周期管理等。Podman 自身是可以通过 Dockerfile 来进行容器镜像的构建，并且也支持容器镜像的 pull/push/login 等操作，Buildah 能够带来什么好处，我们为什么要使用它？

容器工具体验系列：
* [Podman 初次体验](https://zdyxry.github.io/2019/10/12/Podman-%E5%88%9D%E6%AC%A1%E4%BD%93%E9%AA%8C/)
* [Buildah 初次体验](https://zdyxry.github.io/2019/10/19/Buildah-%E5%88%9D%E6%AC%A1%E4%BD%93%E9%AA%8C/)
* [Skopeo 初次体验](https://zdyxry.github.io/2019/10/26/Skopeo-初次体验/)

注意：本文章所采用环境为 CentOS7，需要除了 Buildah 工具外，还需要安装 `containers-common` 用于配置容器。

## What

我们现在使用的容器管理工具无论是 Podman 还是 Docker，都是符合 OCI 规范的，他们操作的镜像也需要符合 OCI 规范，Buildah 介绍很简单： `A tool that facilitates building OCI images`。

Buildah 功能列表：
1. 创建容器
2. 通过 Dockerfile 或者一个处于运行状态的容器（指 Buildah 自身创建的容器，Podman 不可见
3. 挂载/卸载镜像文件系统
4. 使用更新后挂载的镜像文件系统作为文件系统层创建新的镜像
5. ...

### Buildah 与 Podman 的关系

在官方说法中，Buildah 与 Podman 是相辅相成的关系，有很多共同点：它们都不需要 root 权限；都可以通过 Dockerfile 来构建容器镜像；都采用 fork-exec 模型；都不需要守护进程等等。 Buildah 主要的优势在于可以在没有 Doclerfiles 的情况下创建容器镜像，这也造成了从 Docker 切换到 Buildah 的用户使用成本会稍微高一些，因为部分概念发生了改变，主要有以下这些对比：

Command	|Podman Behavior|	Buildah Behavior
--- | --- | ---
build|	Calls buildah bud|	Provides the build-using-dockerfile (bud) command that emulates Docker’s build command.
commit	|Commits a Podman container into a container image. Does not work on a Buildah container. Once committed the resulting image can be used by either Podman or Buildah.|	Commits a Buildah container into a container image. Does not work on a Podman container. Once committed, the resulting image can be used by either Buildah or Podman.
mount|	Mounts a Podman container. Does not work on a Buildah container.|	Mounts a Buildah container. Does not work on a Podman container.
pull and push|	Pull or push an image from a container image registry. Functionally the same as Buildah.	|Pull or push an image from a container image registry. Functionally the same as Podman.
run	|Run a process in a new container in the same manner as docker run.	|Runs the container in the same way as the RUN command in a Dockerfile.
rm	|Removes a Podman container. Does not work on a Buildah container.|	Removes a Buildah container. Does not work on a Podman container.|
rmi, images, tag|	Equivalent on both projects.|	Equivalent on both projects.
containers and ps|	ps is used to list Podman containers. The containers command does not exist.	|containers is used to list Buildah containers. The ps command does not exist.

## How

### 从 Dockerfile 构建镜像

buildah 提供了 `build-using-dockerfile` 命令支持从 Dockerfile 构建镜像，命令等同于 `docker build` 与 `podman build`。

```bash
root@yiran-30-250:/tmp/buildah
 $ cat Dockerfile  # 编写 Dockerfile
FROM centos

MAINTAINER <zdyxry@gmail.com>

CMD echo "hello yiran"
root@yiran-30-250:/tmp/buildah
 $ buildah bud -t yiran . # 使用 `bud` 命令构建镜像，等同于 `docker build`
STEP 1: FROM centos
STEP 2: MAINTAINER <zdyxry@gmail.com>
STEP 3: CMD echo "hello yiran"
STEP 4: COMMIT yiran
Getting image source signatures
Copying blob 9e607bb861a7 skipped: already exists
Copying blob 5f70bf18a086 skipped: already exists
Copying config ebaeed04e2 done
Writing manifest to image destination
Storing signatures
ebaeed04e23610d304c74d1e3bc0c428162e6e7eac529dce1376d8b284604b85
root@yiran-30-250:/tmp/buildah
 $ buildah images
REPOSITORY                 TAG      IMAGE ID       CREATED              SIZE
localhost/yiran            latest   ebaeed04e236   3 seconds ago        227 MB
docker.io/library/centos   latest   0f3e07c0138f   2 weeks ago          227 MB
root@yiran-30-250:/tmp/buildah
 $ podman images # 构建出来的镜像保存在 `/var/lib/containers/storage` ，因此 Podman 可以直接使用
REPOSITORY                 TAG      IMAGE ID       CREATED              SIZE
localhost/yiran            latest   ebaeed04e236   7 seconds ago        227 MB
docker.io/library/centos   latest   0f3e07c0138f   2 weeks ago          227 MB
root@yiran-30-250:/tmp/buildah
 $ podman run localhost/yiran:latest
hello yiran
```

### 从容器中构建镜像

这是 Buildah 最常使用方式，`buildah` 配合 Host 的命令操作来达到简化镜像构建的目的。

```bash
root@yiran-30-250:/tmp/buildah
 $ buildah from centos
centos-working-container
root@yiran-30-250:/tmp/buildah
 $ buildah run centos-working-container yum install httpd -y
Complete!
root@yiran-30-250:/tmp/buildah
 $ echo "Hi yiran" > index.html
You have new mail.
root@yiran-30-250:/tmp/buildah
 $ buildah copy centos-working-container index.html /var/www/html/index
062e7183713e39f9788fe12ef40c298aa69e394df5ee9699aa6c136fb32f3144
root@yiran-30-250:/tmp/buildah
 $ buildah config --entrypoint "/usr/sbin/httpd -DFOREGROUND" centos-working-container      
root@yiran-30-250:/tmp/buildah
 $ buildah commit centos-working-container  yiran-httpd
Getting image source signatures
Copying blob 9e607bb861a7 skipped: already exists
Copying blob a6d6842abbd9 done
Copying config daa1399f36 done
Writing manifest to image destination
Storing signatures
bdaa1399f36944ff74e6fe20c5b346aece51f5edb9c47907027ac4d877ccf179c
root@yiran-30-250:/tmp/buildah
 $ buildah images
REPOSITORY                 TAG      IMAGE ID       CREATED          SIZE
localhost/yiran-httpd      latest   daa1399f3694   7 seconds ago    277 MB
localhost/yiran            latest   ebaeed04e236   13 minutes ago   227 MB
<none>                     <none>   975b7fcdfccc   13 minutes ago   227 MB
<none>                     <none>   8cafad8a1ab0   15 minutes ago   227 MB
docker.io/library/centos   latest   0f3e07c0138f   2 weeks ago      227 MB
root@yiran-30-250:/tmp/buildah
 $ podman images
REPOSITORY                 TAG      IMAGE ID       CREATED          SIZE
localhost/yiran-httpd      latest   daa1399f3694   15 seconds ago   277 MB
localhost/yiran            latest   ebaeed04e236   13 minutes ago   227 MB
<none>                     <none>   975b7fcdfccc   13 minutes ago   227 MB
<none>                     <none>   8cafad8a1ab0   15 minutes ago   227 MB
docker.io/library/centos   latest   0f3e07c0138f   2 weeks ago      227 MB
root@yiran-30-250:/tmp/buildah
 $ podman run -p 8080:80 localhost/yiran-httpd:latest
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 10.88.0.5. Set the 'ServerName' directive globally to suppress this message
```

上述操作解释如下：
1. `buildah from` 命令创建一个新的处于运行中的容器
2. `buildah run <container id>` 在容器中执行命令
3. `echo yiran > index.html` 在主机上执行的命令，生成文件，该文件保存在主机上
4. `buildah copy` 将主机上的文件拷贝到容器中，等同于 Dockerfile 中的 `COPY`
5. `buildah config --entrypoint` 给容器配置 entrypoint，等同于 Dockerfile 中的 `ENTRYPOINT`
6. `buildah commit` 将该容器制作为镜像，保存在 `/var/lib/containers/` 下

### 挂载镜像

buildah 提供了 `buildah mount` 命令，可以将运行中容器挂载到 Host 的文件系统上，我们可以直接在 Host 上对容器内文件进行操作：

```bash
root@yiran-30-250:/tmp/buildah
 $ buildah images
REPOSITORY                  TAG      IMAGE ID       CREATED          SIZE
localhost/yiran-httpd       latest   daa1399f3694   25 minutes ago   277 MB
localhost/yiran             latest   ebaeed04e236   39 minutes ago   227 MB
docker.io/library/centos    latest   0f3e07c0138f   2 weeks ago      227 MB
root@yiran-30-250:/tmp/buildah
 $ buildah from localhost/yiran-httpd
yiran-httpd-working-container
root@yiran-30-250:/tmp/buildah
 $ buildah mount yiran-httpd-working-container
/var/lib/containers/storage/overlay/75d42aaf05bfb855d59c7ae32ac138acd17c6a40f56cd541b16bffad6c720e9b/merged
root@yiran-30-250:/tmp/buildah
 $ cat /var/lib/containers/storage/overlay/75d42aaf05bfb855d59c7ae32ac138acd17c6a40f56cd541b16bffad6c720e9b/merged/var/www/html/index
Hi yiran
```

我们除了可以直接操作容器内文件，也可以在 Host 上给容器安装一些软件，如 dnf、make 等工具：

```bash
dnf install --installroot=<container mountpoint>
make install DESTDIR=<container mountpoint>
```

这里面临一个问题：如果在构建镜像的时候依赖于我们 Host 的环境，那么就无法达到我们想要的构建环境隔离了。这个问题可以通过使用多个容器共同构建来解决。

假设如果我们需要 gcc 环境，那么我们可以准备两个容器：其中一个包含 gcc ，并用它来编译，编译完成后在另一个纯净的容器中安装，最终只需要 commit 纯净的容器就可以。

这里的好处是 buildah 方式构建镜像，不会像 Dockerfile 一样包含很多层，只有执行 `buildah commit` 的时候产生一层镜像文件，我们也不需要考虑清理编译环境等问题。

## Why

了解了基本的使用，那么我们需要知道为什么要使用 Buildah。

首先如果不使用 Buildah，对于整个容器工具链来说是完全 Ok 的，哪怕是不使用 Docker，仅凭 `podman build` 命令配合 Dockerfile 也是足够的，我们可以构建我们所需要的任意镜像。

使用 Buildah 能带来什么好处呢？我理解是我们可以通过更多的手段去构建镜像，不局限于 Dockerfile 中有限的关键字，我们有了更多的可能性，这就足够了。无论是 Buildah 原生命令还是通过 `buildah mount` 挂载到本地文件系统，都让我们可以更舒服的构建镜像，我们从维护一个 Dockerfile 转变为维护一个 Shell 脚本。

当然无论使用哪种方式，我们都需要知道 OCI 镜像标准是什么，这是最基本的。


Shell 脚本示例：
```shell
#!/usr/bin/env bash

set -o errexit

# Create a container
container=$(buildah from fedora:28)
mountpoint=$(buildah mount $container)

buildah config --label maintainer="yiran <zdyxry@gmail.com>" $container

curl -sSL http://ftpmirror.gnu.org/hello/hello-2.10.tar.gz \
     -o /tmp/hello-2.10.tar.gz
tar xvzf src/hello-2.10.tar.gz -C ${mountpoint}/opt

pushd ${mountpoint}/opt/hello-2.10
./configure
make
make install DESTDIR=${mountpoint}
popd

chroot $mountpoint bash -c "/usr/local/bin/hello -v"

buildah config --entrypoint "/usr/local/bin/hello" $container
buildah commit --format docker $container hello
buildah unmount $container
```


## 参考链接
* https://github.com/containers/buildah
* http://chris.collins.is/2017/08/17/buildah-a-new-way-to-build-container-images/ 
* https://developers.redhat.com/blog/2019/02/21/podman-and-buildah-for-docker-users/

