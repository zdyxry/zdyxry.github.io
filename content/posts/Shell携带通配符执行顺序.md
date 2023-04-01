---
title: Shell 携带通配符执行顺序
date: 2023-04-01
tags:
- Shell
---


## 背景

这周有同事在 Slack 问了一个问题： `发现在v505和v503的集群主机上 sudo的配置有一点点小问题：普通用户使用sudo时 shell中的 wildcard不生效` 。

环境状态大概是这样的：
系统存在普通用户 `yiran` ，并配置了 sudo 权限，同时系统存在 `/var/log/libvirt/qemu/` 路径，其中 `libvirt` 和 `qemu` 的目录 owner 是 root，权限是700， `qemu` 下存在很多以 `.log` 为结尾的文件，owner 是 root，权限是 600，具体示例如下：

```go
[yiran@node11 11:09:35 ~]$id yiran
uid=1002(yiran) gid=1002(yiran) groups=1002(yiran)
[yiran@node11 11:09:40 ~]$sudo ls -l /var/log/ |grep libvirt
drwx------.  3 root      root           4096 Sep 16  2022 libvirt
[yiran@node11 11:09:45 ~]$sudo ls -l /var/log/libvirt |grep qemu
drwx------. 2 root root 319488 Mar 26 03:07 qemu
[yiran@node11 11:09:48 ~]$sudo ls -l /var/log/libvirt/qemu/ |egrep *.log$ | head -n 3
-rw------- 1 root root   0 Mar 26 03:07 00381379-c866-4aee-b22d-af0c63367d0b.log
-rw------- 1 root root   0 Mar 26 03:07 003a4849-a0c4-4ea1-947b-1bbd9b162c7c.log
-rw------- 1 root root   0 Mar 26 03:07 00625e93-ec6e-45e1-b2b9-7ec15c94d803.log
```

同事执行的命令是： `sudo ls /var/log/libvirt/qemu/*.log` ，系统提示 `No such file or directory` ， 问原因。

```go
[yiran@node11 11:11:42 ~]$sudo ls /var/log/libvirt/qemu/*.log
ls: cannot access /var/log/libvirt/qemu/*.log: No such file or directory
```

## 原因

这个现象以及环境决定了这个很明显是一个权限相关的问题，直接 `strace` 看看，截取 5 行看看：

```go
[yiran@node11 11:17:08 ~]$strace sudo ls /var/log/libvirt/qemu/*.log 2>&1 | head -n 5
execve("/bin/sudo", ["sudo", "ls", "/var/log/libvirt/qemu/*.log"], [/* 21 vars */]) = 0
brk(NULL)                               = 0x558432932000
fcntl(0, F_GETFD)                       = 0
fcntl(1, F_GETFD)                       = 0
fcntl(2, F_GETFD)                       = 0
```

换一个可以正常输出的例子对比一下：

```go
[yiran@node11 11:18:58 ~]$strace sudo ls /var/log/*.log 2>&1 | head -n 5
execve("/bin/sudo", ["sudo", "ls", "/var/log/bash.log", "/var/log/boot.log", "/var/log/configcenter-agent.log", "/var/log/detect_conn.log", "/var/log/hugepage-manager.log", "/var/log/ntp.log", "/var/log/ovm-agent-init.log", "/var/log/vector-agent.log", "/var/log/websockify.log", "/var/log/yum.log"], [/* 21 vars */]) = 0
brk(NULL)                               = 0x556b5d5ac000
fcntl(0, F_GETFD)                       = 0
fcntl(1, F_GETFD)                       = 0
fcntl(2, F_GETFD)                       = 0
```

可以看到传给 `execve` 的时候，前者是直接带有通配符，后者已经进行了模式匹配并展开为具体匹配的文件名。找 Bash 的[官方文档](https://www.gnu.org/software/bash/manual/bash.html#Filename-Expansion)看看关于通配符的处理：

```go
After word splitting, unless the -f option has been set (see The Set Builtin), 
Bash scans each word for the characters ‘*’, ‘?’, and ‘[’. 
If one of these characters appears, and is not quoted, 
then the word is regarded as a pattern, and replaced with an alphabetically sorted 
list of filenames matching the pattern (see Pattern Matching). 
If no matching filenames are found, and the shell option nullglob is disabled, 
the word is left unchanged. If the nullglob option is set, and no matches are found, 
the word is removed. If the failglob shell option is set, and no matches are found, 
an error message is printed and the command is not executed. If the shell option 
nocaseglob is enabled, the match is performed without regard to the case of 
alphabetic characters.
```

Bash 在进行参数进行分词后，会扫描每个单词中出现 `*` ，`?` 或者 `[` 的字符，如果出现，则认为这是一个 pattern，然后会进行模式匹配，将其替换为匹配到的结果，匹配过程也与 Bash `glob` 相关参数有关。

在内部环境中，执行命令的过程是，先分词进行解析，检测到 `*` 后，进行模式匹配，普通用户 `yiran` 是没有对 `/var/log/libvirt/qemu/` 目录的读取权限的，所以在进行模式匹配的时候，匹配不到对应的文件，导致真正传递的参数是 `*.log` 本身，而不是具体的文件名，像日常使用的 `ls` `cp` `mv` 经常会携带通配符来进行批量操作，这里使用的能力并不是执行的 `ls` `cp` `mv` 自身，而是 Shell 提供的模式匹配能力。

解决方式也很简单，只需要在 sudo 中执行一个新的 shell 就可以了： 

```go
[yiran@node11 12:04:39 ~]$sudo bash -c 'ls /var/log/libvirt/qemu/*.log' | head -n 3
/var/log/libvirt/qemu/00381379-c866-4aee-b22d-af0c63367d0b.log
/var/log/libvirt/qemu/003a4849-a0c4-4ea1-947b-1bbd9b162c7c.log
/var/log/libvirt/qemu/00625e93-ec6e-45e1-b2b9-7ec15c94d803.log
```

## 参考链接

- [https://unix.stackexchange.com/questions/309244/why-isnt-this-sudo-mv-operation-with-wildcard-working](https://unix.stackexchange.com/questions/309244/why-isnt-this-sudo-mv-operation-with-wildcard-working)