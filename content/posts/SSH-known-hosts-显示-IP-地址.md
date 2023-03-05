---
title: SSH known_hosts 显示 IP 地址
date: 2019-12-06 21:54:25
tags:
- Linux
---


## 背景

工作上使用的电脑因为各种各样的原因，被我安装为 Ubuntu 19.04，平时使用上没什么问题，但是最近发现它默认的 SSH 配置随着版本升级发生了变化，known_hosts 文件中记录的不再是 IP 地址，而是一串字符，这导致了当我想要删除某个主机的 key 时，无法准确的找到，因此想办法解决这个事情。

## SSH

我们使用 Linux 系统的一个最基本的服务应该就是 SSH 了，除了偶尔我们通过 VNC 或者 KVM(Keyboard Virtual Manager)连接控制主机外，都是通过 SSH 到 Linux 主机上进行某些操作。那么 SSH 就是 Secure Shell，安全外壳协议。可在不安全的网络中为网络服务提供安全的传输环境。SSH 通过在网络中建立安全隧道来实现SSH客户端与服务器之间的连接。

SSH 最重要的就是安全，采用的是非对称加密，关于加密相关的部分，可以看我之前写的一篇[《图解密码技术》读书笔记
](https://zdyxry.github.io/2019/09/14/%E3%80%8A%E5%9B%BE%E8%A7%A3%E5%AF%86%E7%A0%81%E6%8A%80%E6%9C%AF%E3%80%8B%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0/) 里面有比较完整的相关知识。

这里主要说一下使用密码登陆和密钥登陆的流程。

### 密码登陆

1. 客户端向服务端发起连接请求

```shell
root@test-hostname-ubuntu-s-1804:~# ssh 192.168.67.90
The authenticity of host '192.168.67.90 (192.168.67.90)' can't be established.
ECDSA key fingerprint is SHA256:ca9Zk/7pR4f6rrNP3wi1WK+CQMtG4Ka+kkouwQYU0nY.
Are you sure you want to continue connecting (yes/no)?
```
2. 客户端会提示，知道服务端的唯一标示，确认连接么
3. 确认连接，输入 yes

```shell
root@test-hostname-ubuntu-s-1804:~# ssh 192.168.67.90
The authenticity of host '192.168.67.90 (192.168.67.90)' can't be established.
ECDSA key fingerprint is SHA256:ca9Zk/7pR4f6rrNP3wi1WK+CQMtG4Ka+kkouwQYU0nY.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.67.90' (ECDSA) to the list of known hosts.
root@192.168.67.90's password:
```

4. 服务端传输公钥给客户端，客户端输入密码，使用服务端公钥加密并发送给服务端
5. 服务端使用私钥解密，验证密码正确，登陆成功

```shell
root@test-hostname-ubuntu-s-1804:~# ssh 192.168.67.90
The authenticity of host '192.168.67.90 (192.168.67.90)' can't be established.
ECDSA key fingerprint is SHA256:ca9Zk/7pR4f6rrNP3wi1WK+CQMtG4Ka+kkouwQYU0nY.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.67.90' (ECDSA) to the list of known hosts.
root@192.168.67.90's password:
Last login: Fri Dec  6 21:51:00 2019 from 192.168.73.54
[root@node90 22:30:29 ~]$
```

### 密钥登陆

1. 客户端向服务端发起连接请求
2. 服务端收到客户端的请求，找到对应客户端的公钥，生成随机数
3. 服务端使用客户端的公钥对随机数进行加密，发送给客户端
4. 客户端使用私钥进行解密，得到随机数，并将随机数与 session key 拼接，并将结果通过 MD5 算出散列值
5. 服务端同样使用随机数与 session key 拼接，并将结果通过 MD5 算出散列值
6. 服务端对两个散列值进行校验，如果想通，则登陆成功

## 相关文件

### ~/.ssh/id_rsa

当前节点生成的私钥，使用 RSA 算法。

### ~/.ssh/id_rsa.pub

当前节点生成的公钥，使用 RSA 算法，与 id_rsa 成对出现。

### ~/.ssh/authorized_keys

用于保存已经授权（信任）的客户端公钥。

### ~/.ssh/known_hosts

known_hosts 中存放 SSH 自动维护并检查的一个数据库，该数据库包含曾经连接过的所有主机的标识。

这个文件也是今天的主角。

## known_hosts

当我们客户端尝试连接服务端，会有一条提示，服务端主机的唯一标示是xxx，确认连接么，如果输入yes，那么这个主机的标示就会记录到 known_hosts，一般我们的 known_hosts 会长这样：

```shell
root@test-hostname-ubuntu-s-1804:~# cat .ssh/known_hosts
|1|+YgY28AEikbKxdosHK1Cxb6zJqs=|yEi41f2MIl6hU9uQOvXyzK0hByM= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHJscGQ4nUV7b7+nUtHVFPgm38JrUJwMapVqkq+oF1RR7mniCGhrkIGpb2cqKINrcZFyKFRqWhuAgYtMyFALOrM=
```

或者长这样：

```shell
root@yiran-30-250:~
   head -n 1 .ssh/known_hosts
192.168.70.250 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHNWt8CDe7sPvATsqx5zH5v9wJzYrFhu9fmYnshIYLEnuoXmCmVu2cGU8s/IjK2jU8hnFad4T1gMhst7cXLmqAo=
```

了解 https 相关知识的同学应该知道，证书的重要性。在 SSH 场景下，我们没有证书，那么就需要我们自己人为的确保我们要连接的服务端是可信的。如果我们第一次登陆 192.168.1.1 后，系统保存了主机唯一标示到了 ~/.ssh/known_hosts，如果我们下一次登陆 192.168.1.1 客户端发现主机唯一标示产生了变化，那么就会禁止我们登陆了。

在工作中经常遇到这种场景，可能的原因有很多：系统重装、快照回滚、IP 冲突等等。通常我们的做法就是闭着眼睛删除 known_hosts 里面的对应主机信息，然后重新登陆就可以了。

但是最近发现 Ubuntu 19.04 中记录的 known_hosts 是这样的：

```shell
root@test-hostname-ubuntu-s-1804:~# cat .ssh/known_hosts
|1|+YgY28AEikbKxdosHK1Cxb6zJqs=|yEi41f2MIl6hU9uQOvXyzK0hByM= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHJscGQ4nUV7b7+nUtHVFPgm38JrUJwMapVqkq+oF1RR7mniCGhrkIGpb2cqKINrcZFyKFRqWhuAgYtMyFALOrM=
```

是的，我们无法在一堆看似乱码中找到我们想要的主机并删掉它，这其实是 OpenSSH 新版本中的一项安全改进。

在 [记一次系统被入侵分析过程](https://zdyxry.github.io/2019/10/25/%E8%AE%B0%E4%B8%80%E6%AC%A1%E7%B3%BB%E7%BB%9F%E8%A2%AB%E5%85%A5%E4%BE%B5%E5%88%86%E6%9E%90%E8%BF%87%E7%A8%8B/) 博客中有提到，现在好多病毒在入侵之后都是通过 SSH 相关信息进行横向扩散的，所以我们应该尽可能的少在系统中保存明文的 IP 地址相关信息。

但是对我测试环境来说，是没什么关系的，因此我需要禁止这个安全配置，来达到我的目的。

正确的姿势是修改 SSH 客户端的配置，将 `HashKnownHosts` 置为 no ，清空 known_hosts 文件，再连接服务端，就可以看到 known_hosts 已经显示 IP 地址了。

```shell
root@test-hostname-ubuntu-s-1804:~# cat /etc/ssh/ssh_config |grep -i hash
    HashKnownHosts no
root@test-hostname-ubuntu-s-1804:~# cat .ssh/known_hosts
192.168.67.90 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHJscGQ4nUV7b7+nUtHVFPgm38JrUJwMapVqkq+oF1RR7mniCGhrkIGpb2cqKINrcZFyKFRqWhuAgYtMyFALOrM=
```

当然如果你想搞破坏，可以尝试下这篇[博客](https://blog.rootshell.be/2010/11/03/bruteforcing-ssh-known_hosts-files/)中提供的脚本：https://blog.rootshell.be/wp-content/uploads/2010/11/known_hosts_bruteforcer.pl.txt （谨慎使用）


## 参考链接

* https://zh.wikipedia.org/wiki/Secure_Shell
* https://blog.rootshell.be/2010/11/03/bruteforcing-ssh-known_hosts-files/
* https://unix.stackexchange.com/questions/31549/is-it-possible-to-find-out-the-hosts-in-the-known-hosts-file
