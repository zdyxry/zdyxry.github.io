---
title: Python 调用 systemd watchdog 方法
date: 2019-03-10 10:21:19
tags:
- Python
- Linux
---


## systemd

在之前的博客中介绍过 systemd 的基本使用及通过 timer 来替换 crontab 的方法，今天来说一下如何调用 watchdog。

在 systemd 中，提供 watchdog 来检测服务状态状态，官方文档中描述这个功能为 "keep-alive ping"，我们可以在服务的启动配置中，添加 `WatchdogSec` 来指定 timeout 时间，在服务程序中通过发送 `WATCHDOG=1` 来不断的通知 systemd，服务处于正常状态，当超过 timeout 时间未收到 `WATCHDOG=1` 信号后，systemd 会根据 `Restart` 配置，决定是否自动重启服务。

## 示例

服务程序：
```python
root@yiran-30-250:/usr/lib/systemd/system
 $ cat /root/project/watchdog/test.py
#!/usr/bin/python
# coding:utf-8
import os
import time
import socket
import logging

print("Test starting up...")
time.sleep(1)  # 模拟执行真实业务
print("Test startup finished")

try:
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    addr = os.getenv("NOTIFY_SOCKET")  # systemd default addr = "/run/systemd/notify"
    if addr and addr[0] == "@":
        addr = "\0" + addr[1:]
except Exception:
    logging.error("Failed to get notify socket addr")

if sock and addr:
    sock.connect(addr)
    sock.sendall("READY=1")  # 通知 systemd 服务启动完成

count = 0

while True:
    print("Running...")
    time.sleep(2)
    if count <= 10:
        sock.sendall("WATCHDOG=1")  # 通知 systemd 服务正常运行
        logging.info("Notify socket addr is:%s", addr)
        logging.info("test.service watchdog timestamp update succeeded")
        count += 1
```

服务 systemd 配置：


```bash
root@yiran-30-250:/usr/lib/systemd/system
 $ cat test.service
[Unit]
Description=A test service written in Python

[Service]
Environment=PYTHONUNBUFFERED=true
ExecStart=/usr/bin/python /root/project/watchdog/test.py
Type=notify
Restart=always
WatchdogSec=5
```

我们启动服务观察下运行状态：

```bash
root@yiran-30-250:/usr/lib/systemd/system
 $ systemctl daemon-reload
root@yiran-30-250:/usr/lib/systemd/system
 $ systemctl start test.service
root@yiran-30-250:/usr/lib/systemd/system
 $ systemctl status test
● test.service - A test service written in Python
   Loaded: loaded (/usr/lib/systemd/system/test.service; static; vendor preset: disabled)
   Active: active (running) since 日 2019-03-10 10:16:39 CST; 21s ago
 Main PID: 12202 (python)
   Memory: 4.0M
   CGroup: /system.slice/test.service
           └─12202 /usr/bin/python /root/project/watchdog/test.py
# 在 Python 程序中，如果没有指定输出位置，会默认打到系统日志中
3月 10 10:16:41 yiran-30-250 python[12202]: Running...
3月 10 10:16:43 yiran-30-250 python[12202]: Running...
3月 10 10:16:45 yiran-30-250 python[12202]: Running...
3月 10 10:16:47 yiran-30-250 python[12202]: Running...
3月 10 10:16:49 yiran-30-250 python[12202]: Running...
3月 10 10:16:51 yiran-30-250 python[12202]: Running...
3月 10 10:16:53 yiran-30-250 python[12202]: Running...
3月 10 10:16:55 yiran-30-250 python[12202]: Running...
3月 10 10:16:57 yiran-30-250 python[12202]: Running...
3月 10 10:16:59 yiran-30-250 python[12202]: Running...
```

timeout 导致服务重启：

```bash
root@yiran-30-250:/usr/lib/systemd/system
 $ systemctl status test
● test.service - A test service written in Python
   Loaded: loaded (/usr/lib/systemd/system/test.service; static; vendor preset: disabled)
   Active: deactivating (stop-sigabrt) (Result: watchdog) since 日 2019-03-10 10:17:06 CST; 2ms ago
 Main PID: 12202 (python)
   Memory: 3.9M
   CGroup: /system.slice/test.service
           └─12202 /usr/bin/python /root/project/watchdog/test.py

3月 10 10:16:49 yiran-30-250 python[12202]: Running...
3月 10 10:16:51 yiran-30-250 python[12202]: Running...
3月 10 10:16:53 yiran-30-250 python[12202]: Running...
3月 10 10:16:55 yiran-30-250 python[12202]: Running...
3月 10 10:16:57 yiran-30-250 python[12202]: Running...
3月 10 10:16:59 yiran-30-250 python[12202]: Running...
3月 10 10:17:01 yiran-30-250 python[12202]: Running...
3月 10 10:17:03 yiran-30-250 python[12202]: Running...
3月 10 10:17:05 yiran-30-250 python[12202]: Running...
3月 10 10:17:06 yiran-30-250 systemd[1]: test.service watchdog timeout (limit 5s)!
```

journalctl 查看具体重启原因：

```shell
3月 10 10:19:20 yiran-30-250 python[12303]: Running...
3月 10 10:19:22 yiran-30-250 python[12303]: Running...
3月 10 10:19:24 yiran-30-250 python[12303]: Running...
3月 10 10:19:26 yiran-30-250 python[12303]: Running...
3月 10 10:19:28 yiran-30-250 python[12303]: Running...
3月 10 10:19:29 yiran-30-250 systemd[1]: test.service watchdog timeout (limit 5s)!
3月 10 10:19:29 yiran-30-250 systemd[1]: test.service: main process exited, code=dumped, status=6/ABRT
3月 10 10:19:29 yiran-30-250 systemd[1]: Unit test.service entered failed state.
3月 10 10:19:29 yiran-30-250 systemd[1]: test.service failed.
3月 10 10:19:29 yiran-30-250 systemd[1]: test.service holdoff time over, scheduling restart.
3月 10 10:19:29 yiran-30-250 systemd[1]: Starting A test service written in Python...
3月 10 10:19:29 yiran-30-250 python[12324]: Test starting up...
3月 10 10:19:30 yiran-30-250 python[12324]: Test startup finished
3月 10 10:19:30 yiran-30-250 systemd[1]: Started A test service written in Python.
```

## 参考链接
* https://github.com/bb4242/sdnotify
* https://gist.github.com/Spindel/1d07533ef94a4589d348
* https://www.freedesktop.org/software/systemd/man/sd_notify.html# 
* https://www.freedesktop.org/software/systemd/man/systemd.service.html
