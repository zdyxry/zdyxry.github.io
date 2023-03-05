---
title: Linux audit buffer 配置
date: 2021-08-15 08:49:59
tags:
---

## 背景

最近遇到了一个 case，一台主机处于挂起状态，当时主机的 IPMI console 显示日志 ： `audit: backlog limit exceeded` ，由于一些原因，导致没有及时的发送 NMI 信号触发 kernel core dump，所以只能根据已有信息进行排查，记录下 audit buffer 相关配置的学习。

## Audit

Linux kernel 在 2.6 引入 audit，为了能够更好的记录系统中的各种安全事件，比如文件修改事件和系统调用事件。

### 配置方法

`/etc/audit` 目录下
- 控制规则：设置 audit 系统的一些行为以及修改其默认设置
- 文件系统规则：审计文件，记录特殊文件或目录的访问情况
- 系统调用规则：记录一些特殊应用程序的系统调用行为

### buffer 配置

- 当事件无法被正确记录时，会打印一些异常日志：

        ```
        audit: audit_backlog=321 > audit_backlog_limit=320
        audit: audit_lost=44395 audit_rate_limit=0 audit_backlog_limit=320
        audit: backlog limit exceeded
        ```
- 根据 audit 的flag 配置决定，当 flag ==1 时，打印提示日志；当 flag ==2 时，kernel panic。 默认flag = 1 。

- 在审计系统中，使用 socket buffer queue 来保存事件，每当接收到一条新的事件时，都会记录并准备添加到这个 queue 中，有以下几个参数来控制该行为：
	- backlog_limit
		- queue 最大长度，当记录了一个事件导致queue 长度超过限制，那么就会发生failure
	- raid_limit
		- 速率，一秒钟内事件数量超过限定值时，则不会添加到 queue 中并会发生 failure


### 故障处理
- 如果无法记录事件，那么会发生故障，根据 flag 设置来决定处理行为
	- 0，silent，静默处理
	- 1， printk(默认行为)，打印到系统日志中，具体打印限制根据 kernel 参数决定：

		  ```
		  # sysctl -a | grep kernel.printk_rate
		  kernel.printk_ratelimit = 5
		  kernel.printk_ratelimit_burst = 10
		  ```
	- 2， panic，kernel panic
  
### buffer 资源计算
- queue 在内存中，需要设置一个合理的 backlog_limit 数值来防止占用过多内存资源，每条事件在 9000 bytes 左右，如果设置为 320，那么占用内存资源为 320 * 9000 = 2.7 MiB 左右。

### 可能遇到的问题
- `audit: backlog limit exceeded`
	- IPMI console 打印以上日志，表示事件未被正确的记录，事件当前数量超过 backlog_limit 限制，可能会导致系统 hang 或者无响应

        > An audit buffer queue at or exceeding capacity might also cause the instance to hang or remain in an unresponsive state.

	- 推荐根据实际情况调整 backlog_limit 大小，比如 8192.
	- 可能产生的原因：
		- 审计系统设置参数设置不合理
		- 冻结文件系统（通常由于系统快照）  
	- audit 版本为 2.4.1-5 ，其中的配置为：

		  ```
		  [root@dogfood-idc-elf-65 audit]# rpm -qa |grep audit
		  audit-2.4.1-5.el7.x86_64
		  audit-libs-2.4.1-5.el7.x86_64
		  [root@dogfood-idc-elf-65 audit]# auditctl -s
		  enabled 1
		  flag 1
		  pid 1093
		  rate_limit 0
		  backlog_limit 320
		  lost 0
		  backlog 0
		  loginuid_immutable 0 unlocked
		  ```
	- audit 版本为2.7.6-3，其中的配置为：

		  ```
		  [root@node90 14:16:09 ~]$rpm -q audit
		  audit-2.7.6-3.el7.x86_64
		  [root@node90 14:16:13 ~]$auditctl -s
		  enabled 1
		  failure 1
		  pid 1133
		  rate_limit 0
		  backlog_limit 8192
		  lost 0
		  backlog 0
		  loginuid_immutable 0 unlocked
		  ```
### 坑
- auditd 禁止 restart 操作（RefuseManualStop = yes），所以无法使用 [[systemctl]] 控制服务启停，可以使用 `service` 代替
	- `service auditd restart`


### 总结

Redhat 推荐在线上服务器上合理配置 audit 相关参数，避免因为参数不合理产生一些意外情况，CentOS7 系列的 audit 最新版本 backlog_limit 已经是 8192 。但是对于 audit 出现异常所产生的影响，不是很明确，在 AWS 的 KB 中是这么说的：
 > An audit buffer queue at or exceeding capacity might also cause the instance to hang or remain in an unresponsive state.

但是在 Redhat 的相关 KB 中关于具体可能产生怎样的影响并没有详细说明，还需要后续调查。

## 参考链接
- buffer 的单位是什么？ https://serverfault.com/questions/701335/auditctl-buffer-setting-how-large-is-this
- 关于 buffer 参数的解释： https://blog.siphos.be/2015/05/audit-buffering-and-rate-limiting
- AWS 关于 `audit: backlog limit exceeded` 的KB： https://aws.amazon.com/cn/premiumsupport/knowledge-center/troubleshoot-audit-backlog-errors-ec2/?nc1=h_ls
- RedHat 关于 `audit: backlog limit exceeded` 的 KB，其中提到了部分可能的原因和根本原因： https://access.redhat.com/solutions/19327