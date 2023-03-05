---
title: 使用 systemd timer 替换 crontab
date: 2018-06-28 07:04:39
tags:
- Linux
---


在日常工作中，经常会用到定时任务配合脚本自动处理一些重复性工作，通常我会选择 crontab & flock & script 这样的组合进行配置，
最近了解了 systemd timer ，发现虽然配置上比 crontab 要麻烦一点（需要编写两个配置文件），
但是其他的优势是 crontab 不具备的。

## systemd timer 优势
1. systemd 会自动将定时任务事件记录在 systemd 日志中，可以通过 journalctl 轻松查找
2. 可以配置定时器之间的依赖关系
3. 定时器启动/关闭不需要再注释掉 crontab 中的某一行或移除 `/etc/cron.d/` 下的某个文件，而是直接 start/stop/enable/disable 控制
4. 自带锁机制，无需通过 flock 或脚本中添加锁文件的方式控制任务执行与否

## 使用方式

例如，我想要定时备份数据从开发机到服务器上，通常重要的文件采用 inotify & rsync 的方式同步，优先级较低的采用定时同步方式。   

---

### crontab 配置方式   

#### 编写 crontab 配置文件

```bash
crontab -e (或者在 /etc/cron.*/ 对应路径下编写配置文件)
0 1 * * * flock /usr/local/bin/system-backup.sh
```

#### 手动触发定时任务
```bash
/usr/local/bin/system-backup.sh
```


---

### systemd timer 配置方式

#### 编写 timer 配置文件  

```bash
[Unit]
Description=Perform system backup

[Timer]
OnCalendar=daily

[Install]
WantedBy=timers.target
```

#### 编写 timer 对应 service 配置文件

```buildoutcfg
[Unit]
Description=Perform system backup

[Service]
Type=simple
Nice=19
IOSchedulingClass=2
IOSchedulingPriority=7
ExecStart=/usr/loca/bin/system-backup.sh
```

#### 启动定时任务

```bash
systemctl start system-backup.timer   
systemctl enable system-backup.timer
```

#### 检查定时任务是否启动
```bash
systemctl list-timers --all
```

#### 手动触发定时任务

```bash
systemctl start system-backup.service
```

#### 查看日志

可以通过 journalctl 查看定时任务日志，并且可以指定过滤条件。
```bash
journalctl -u system-backup --since="yesterday"
```

