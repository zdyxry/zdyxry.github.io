---
title: systemd 常用操作及配置
date: 2020-03-06 21:02:49
tags:
- Linux
---


## 背景

现在大多数 Linux 发行版是由 systemd 来进行系统管理了， systemd 也是越来越复杂，但是常用的操作就那么多，今天来说说自己常用的操作及配置。

## 操作

### daemon-reload

在给系统新增服务的时候，通常要不断的改 test.service 配置文件，在改配置文件后，通常需要执行 `systemctl daemon-reload` 来重新加在 systemd 配置。

### no-page

通常使用 journalctl 查看服务日志，但是当日志超过当前行可显示最大字符数时，默认会将日志截断，此时可以使用 `journalctl -u <service> --no-page` 来让日志自动折行。

### disk-usage

systemd 日志配置文件在 `/etc/systemd/journald.conf` ，那么如果我想查看一个服务的日志占用空间，可以用 `journalctl -u <servie> --disk-usage` 命令查看。

### poweroff

Linux 下关机命令有很多， `init`,`shutdown`,`poweroff` ，但是如果你注意过会发现以下事实：

```shell
root@localhost:~ 
 $ ll `which init`
lrwxrwxrwx. 1 root root 22 8月  22 2019 /usr/sbin/init -> ../lib/systemd/systemd
root@localhost:~ 
 $ ll `which poweroff`
lrwxrwxrwx. 1 root root 16 8月  22 2019 /usr/sbin/poweroff -> ../bin/systemctl
root@localhost:~ 
 $ ll `which shutdown`
lrwxrwxrwx. 1 root root 16 8月  22 2019 /usr/sbin/shutdown -> ../bin/systemctl
```

是的，systemd 大法好，systemd 通过判断 `$0` 名称来执行对应命令，那我们就可以执行 `systemctl poweroff` 来进行关机。


### list-dependencies

systemd 可以指定服务的依赖，在关键字 `After`,`Before`,`Requires` 来指定，通过 `systemctl list-dependencies <service>` 来显示服务的具体依赖路径。


## 配置


### Restart

大部分服务都是一个常驻进程，我们通常希望它能在 crash、kill、异常中断等情况下仍保持运行，所以我们可以在 `[Servie]` 中指定 `Restart=on-failure` 来完成目的。

### TimeoutStopSec

在通过 `systemctl stop` 进行服务停止时，如果在 `ExecStop` 中指定的操作耗时较长，我们可以通过添加 `TimeoutStopSec=10s` 来设置超时时间。

### RefuseManualStop

如果有些服务我们只想让它处于启动状态，或者通过依赖自动启动，而不想受人为因素干扰，那么我们可以通过设置 `RefuseManualStop=true` 来保证服务无法被人工停止，比如 rdma.service：


```shell
[root@yiran 21:10:36 ~]$systemctl stop rdma
Failed to stop rdma.service: Operation refused, unit rdma.service may be requested by dependency only (it is configured to refuse manual start/stop).
See system logs and 'systemctl status rdma.service' for details.
```

### `PartOf`

与 Requires= 类似， 不同之处在于：仅作用于单元的停止或重启。 其含义是，当停止或重启这里列出的某个单元时， 也会同时停止或重启该单元自身。 注意，这个依赖是单向的， 该单元自身的停止或重启并不影响这里列出的单元。

如果 a.service 中包含了 PartOf=b.service ，那么这个依赖关系将在 b.service 的属性列表中显示为 ConsistsOf=a.service 。 也就是说，不能直接设置 ConsistsOf= 依赖。


### `@`

在 Linux 上配置过 openvpn 的同学应该都看到过一些 `openvpn@client.service` 这样的例子：
> 若需在系统启动时自动启动 OpenVPN，对服务器端与客户端，都可以采用在对应机器上 启用 openvpn@<configuration>.service 的方式配置。例如，如果客户端配置文件是 /etc/openvpn/client.conf，则服务名称应为 openvpn@client.service。或者，如果服务器端配置文件是 /etc/openvpn/server.conf，则服务名称应为 openvpn@server.service。 


我们来看下对应的 systemd 配置文件：


```
yiran@t480:~/Downloads 
 $ cat /lib/systemd/system/openvpn@.service

[Unit]
Description=OpenVPN connection to %i
PartOf=openvpn.service
ReloadPropagatedFrom=openvpn.service
Before=systemd-user-sessions.service
After=network-online.target
Wants=network-online.target
Documentation=man:openvpn(8)
Documentation=https://community.openvpn.net/openvpn/wiki/Openvpn24ManPage
Documentation=https://community.openvpn.net/openvpn/wiki/HOWTO

[Service]
Type=notify
PrivateTmp=true
WorkingDirectory=/etc/openvpn
ExecStart=/usr/sbin/openvpn --daemon ovpn-%i --status /run/openvpn/%i.status 10 --cd /etc/openvpn --script-security 2 --config /etc/openvpn/%i.conf --writepid /run/openvpn/%i.pid
PIDFile=/run/openvpn/%i.pid
KillMode=process
ExecReload=/bin/kill -HUP $MAINPID
CapabilityBoundingSet=CAP_IPC_LOCK CAP_NET_ADMIN CAP_NET_BIND_SERVICE CAP_NET_RAW CAP_SETGID CAP_SETUID CAP_SYS_CHROOT CAP_DAC_OVERRIDE CAP_AUDIT_WRITE
LimitNPROC=100
DeviceAllow=/dev/null rw
DeviceAllow=/dev/net/tun rw
ProtectSystem=true
ProtectHome=true
RestartSec=5s
Restart=on-failure

[Install]
WantedBy=multi-user.target

```

可以看到其实我们 `@` 后面的字段，对应的就是配置文件中的 `%i` ，这样可以让我们很方便的针对同一个应用的不同实例来创建对应的服务。


## 总结

systemd 大法好，博大精深。

## 参考链接

* https://wiki.archlinux.org/index.php/OpenVPN_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#systemd_%E6%9C%8D%E5%8A%A1%E9%85%8D%E7%BD%AE
* http://www.huzs.net/?p=2180


