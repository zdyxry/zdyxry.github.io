---
title: runc nsenter 源码阅读
date: 2020-04-12 14:57:29
tags:
- Container
---

## 背景

最近在阅读 runc 的实现，发现在 runc 中比较重要的一个逻辑是在设置 namespace 过程中的 nsenter 模块，其中逻辑有些绕，也发现了一段很长很有意思的注释，分享一下。


## What

什么是 nsenter，nsenter 是 runc 中的一个 package，它包含了一个特殊的构造函数，用来在 Go runtime 启动之前做一些事情，比如 setns()。nsenter 会引入 `C` 并使用 cgo 实现相关逻辑。在cgo中，如果在 `C` 的 import 后紧跟注释，则在编译程序包的 C 语言实现部分时，该注释将用作 header。因此，每次 import nsenter 时，nsexec()都会调用 C 函数。

在 runc 中只有 init.go import 了 nsenter。

## Why

容器技术最关键的就是 namespace 和 cgroup，其中 namespace 是通过 setns() 函数来实现的，但是 setns() 有一个问题： `A multithreaded process may not change user namespace with setns().` 。而 go runtime 是多线程的，所以需要在 go runtime 启动前执行 setns() 设置好 namespace，然后再走 go 相关实现流程。

## How

在实际的 nsenter 实现中，存在 3 个进程，分别为 parent, child, grandchild。在注释中可以看到 nsenter 实现过程中的考虑：

```
	/*
	 * Okay, so this is quite annoying.
	 *
	 * In order for this unsharing code to be more extensible we need to split
	 * up unshare(CLONE_NEWUSER) and clone() in various ways. The ideal case
	 * would be if we did clone(CLONE_NEWUSER) and the other namespaces
	 * separately, but because of SELinux issues we cannot really do that. But
	 * we cannot just dump the namespace flags into clone(...) because several
	 * usecases (such as rootless containers) require more granularity around
	 * the namespace setup. In addition, some older kernels had issues where
	 * CLONE_NEWUSER wasn't handled before other namespaces (but we cannot
	 * handle this while also dealing with SELinux so we choose SELinux support
	 * over broken kernel support).
	 *
	 * However, if we unshare(2) the user namespace *before* we clone(2), then
	 * all hell breaks loose.
	 *
	 * The parent no longer has permissions to do many things (unshare(2) drops
	 * all capabilities in your old namespace), and the container cannot be set
	 * up to have more than one {uid,gid} mapping. This is obviously less than
	 * ideal. In order to fix this, we have to first clone(2) and then unshare.
	 *
	 * Unfortunately, it's not as simple as that. We have to fork to enter the
	 * PID namespace (the PID namespace only applies to children). Since we'll
	 * have to double-fork, this clone_parent() call won't be able to get the
	 * PID of the _actual_ init process (without doing more synchronisation than
	 * I can deal with at the moment). So we'll just get the parent to send it
	 * for us, the only job of this process is to update
	 * /proc/pid/{setgroups,uid_map,gid_map}.
	 *
	 * And as a result of the above, we also need to setns(2) in the first child
	 * because if we join a PID namespace in the topmost parent then our child
	 * will be in that namespace (and it will not be able to give us a PID value
	 * that makes sense without resorting to sending things with cmsg).
	 *
	 * This also deals with an older issue caused by dumping cloneflags into
	 * clone(2): On old kernels, CLONE_PARENT didn't work with CLONE_NEWPID, so
	 * we have to unshare(2) before clone(2) in order to do this. This was fixed
	 * in upstream commit 1f7f4dde5c945f41a7abc2285be43d918029ecc5, and was
	 * introduced by 40a0d32d1eaffe6aac7324ca92604b6b3977eb0e. As far as we're
	 * aware, the last mainline kernel which had this bug was Linux 3.12.
	 * However, we cannot comment on which kernels the broken patch was
	 * backported to.
	 *
	 * -- Aleksa "what has my life come to?" Sarai
	 */
```

来看下 parent，child，grandchild 分别做了哪些事情：

### parent

parent 进程通过环境变量 `_LIBCONTAINER_INITPIPE` 获取相关配置信息，然后 clone 出 child 进程，当 child 进程 ready 之后设置 user map，从 child 进程中接受 grandchild 进程 pid，然后通过管道传递给外层的 runc 进程。parent 进程退出条件为 child 进程和 grandchild 都处于 ready 状态后，parent 进程退出。

之所以要 clone child 进程，是因为如果创建了 user namespace，那么 user map 只能由原有的 user namespace 设置，所以需要 clone child 进程，然后在 parent 进程中设置 user map。

### child

child 进程先执行 setns()，在一些老版本的kernel 中，`CLONE_PARENT` flag 与 `CLONE_NEWPID` 有冲突，所以使用 unshare 创建 user namespace， user namespace 需要先于其他 namespace 创建，创建 user namespace 并设置 user map，才有能力创建其他的 namespace。等待 parent 进程设置 user map 后，设置 child 当前进程的 uid 为 root(0) ，使用 unshare 创建其他 namespace，然后 clone grandchild 进程，并将 grandchild 进程 pid 传递给 parent，然后退出。

之所以要 clone grandchild 进程，是因为在 child 进程中设置 namespace 并不会在 child 进程中生效，所以需要 clone 出一个新的进程，继承 namespace 配置。


### grandchild

grandchild 进程就是容器真正的进程，在确保 parent 和 child 进程都处于 ready 之后，设置 uid,gid，从管道中读取相应配置信息，然后 unshare 创建 cgroup namespace，然后将状态发送给 parent 后 返回。grandchild 进程返回后继续执行 go 代码流程。


## 总结

runc 作为 OCI 的标准实现，自身代码量并不大，但是逻辑比较扰，其中 namespace 更是博大精深，尤其是要考虑到一些老版本kernel 以及 rootless 场景下，复杂程度翻倍，有很多细节值得去思考。

## 参考链接

* https://github.com/opencontainers/runc/blob/master/libcontainer/nsenter/README.md
* https://github.com/opencontainers/runc/blob/master/libcontainer/nsenter/nsexec.c