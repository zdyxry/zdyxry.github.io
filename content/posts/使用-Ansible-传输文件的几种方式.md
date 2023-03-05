---
title: 使用 Ansible 传输文件的几种方式
date: 2019-11-22 20:15:17
tags:
- Linux
- Ansible
---


## 背景

Ansible 作为一款配置管理和应用部署的软件，日常使用的场景很多，我自己也是重度用户。最近在使用 Ansible 进行文件传输的时候踩了个坑，借此机会整理下 Ansible 传输文件的几种方式。

实验环境：

```bash
[root@yiran ~]# ansible --version
ansible 2.7.12
  config file = None
  configured module search path = [u'/root/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/site-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.5 (default, Aug  7 2019, 00:51:29) [GCC 4.8.5 20150623 (Red Hat 4.8.5-39)]
```

## Template

https://docs.ansible.com/ansible/latest/modules/template_module.html

Ansible 一个常用的功能就是配置管理，通过 Ansible 批量分发配置文件，达到统一版本管理的效果，如果我们想要进行少量的文件传输，从控制节点传输到被管理节点，那么可以采用这种方式来完成。

具体的使用[官方文档](https://docs.ansible.com/ansible/latest/modules/template_module.html) 已经讲的很详细了，这里不再啰嗦。

因为版本是通过 Jinja2 模板传输，支持模板渲染
虽然我们可以在模版中不制定任何参数，直接将其拷贝，但是相比 Copy/Fetch 模块还是需要有模版渲染的一步，速度要慢一些

## Copy/Fetch 模块

https://docs.ansible.com/ansible/latest/modules/copy_module.html

https://docs.ansible.com/ansible/latest/modules/fetch_module.html

如果说我们通过模板来传输文件优点歪门邪道，那么通过 Copy/Fetch 就是 Ansible 官方提供的两个正统模块。

Copy 用于把文件（或文件夹）从控制节点（或远程节点）分发到被管理节点，Copy 在拷贝过程中不会修改文件中的内容或编码，仅仅做传输工作。


Fetch 用于从被管理节点传输文件到控制节点。需要注意的是 Fetch 只能拉取文件，而 Copy 是可以传输文件或者文件夹的。

### 不算坑的坑

在使用 Copy/Fetch 时，总体感受是比较好的，但是有一点需要注意，如果你拷贝的文件过多，或者单个文件大小过大，那么最好不要使用 Copy/Fetch。

Ansible 默认配置中，使用 SFTP 作为文件传输协议：
> There’s really no reason to change this unless problems are encountered, and then there’s also no real drawback to managing the switch. Most environments support SFTP by default and this doesn’t usually need to be changed.

SFTP 是基于 SSH 协议的，与 FTP 没啥关系。SFTP 并不以性能渐长，甚至可以说性能很差，至少与 FTP、Rsync 没办法相比。

关于 SFTP 为什么速度这么慢，StackOverFlow 有个回答写的很详细，这里引用一段：
> I'm the author of HPN-SSH and I was asked by a commenter here to weigh in. I'd like to start with a couple of background items. First off, it's important to keep in mind that SSHv2 is a multiplexed protocol - multiple channels over a single TCP connection. As such, the SSH channels are essentially unaware of the underlying flow control algorithm used by TCP. This means that SSHv2 has to implement its own flow control algorithm. The most common implementation basically reimplements sliding windows. The means that you have the SSH sliding window riding on top of the TCP sliding window. The end results is that the effective size of the receive buffer is the minimum of the receive buffers of the two sliding windows.

## Synchronize

上面提到的两个模块性能都不好，总会有个性能好的来解决这个问题，就是 Synchronize。Synchronize 是通过 rsync 来达到文件传输的目的，是 rsync 的封装。

在使用上因为是调用的 rsync，所以控制节点需要安装 rsync ，Synchronize 模块的并不会完全实现 rsync 所有功能，只是通过 rsync 来达到我们想要的快速同步的功能。

### 坑

在使用 Ansible 过程中，通常会使用普通用户配合密钥的形式来进行用户验证，如果需要 root 权限那么通过 become 关键字来提权。

在 sudo 的早期版本中， `/etc/sudoers` 中有这么一条配置，高版本取消了 tty 的限制：

```
#
# Disable "ssh hostname sudo <cmd>", because it will show the password in clear.
#         You have to run "ssh -t hostname sudo <cmd>".
#
Defaults    requiretty
```

这个配置会导致 Ansible 调用 rsync 执行时失败，可以通过修改 `/etc/sudoers` 或者升级 sudo 软件包来解决。

## 总结

那么说了以上这三种方式，就需要来一个总结对比，看看什么场景下使用什么模块更方便：

|  模块   | 传输文件  | 传输文件夹 | 文件修改 | 文件编码 |  速度 | 文件源 | 权限配置 | 文件验证 | 
|  ----  | ----  | --- | --- | --- | --- | --- | --- | --- |
|  Template | Y | N | Y | Y | 慢 | 控制节点 | Y | Y 
| Copy/Fetch  | Y | Y/N | N | N | 慢 | 控制节点/远程节点 | Y  | Y 
| Synchronize | N | Y | N | N | 快 | 控制节点 | Y | N 

各个模块没有具体的好坏，全看个人需求来使用合适的模块就好。


## 参考链接
* https://docs.ansible.com/ansible/latest/modules/template_module.html 
* https://daniel.haxx.se/blog/2010/12/08/making-sftp-transfers-fast/
* https://stackoverflow.com/questions/8849240/why-when-i-transfer-a-file-through-sftp-it-takes-longer-than-ftp