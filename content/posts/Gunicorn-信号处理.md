---
title: Gunicorn 信号处理
date: 2021-06-27 18:55:41
tags:
- Python
---


## 背景

最近在项目中使用到了 Gunicorn 的 Graceful Shutdown 功能，阅读代码学习一下 Gunicorn 的信号处理。

### Master

Gunicorn 启动入口：

```
WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]").run()
    BaseApplication().run()
        Arbiter(self).run()
```

Master 主要控制逻辑实现在 `Arbiter` 中，包括信号处理和主循环逻辑。在调用 `Arbiter().run()` 会最终调用到 `Arbiter.init_signals()` ，在该函数中会将 Master 中定义的需要处理的信号函数进行相应的注册：


```
Arbiter().run():
    Arbiter().start() 
        Arbiter().init_signals() # 初始化 Master 信号处理
            # initialize all signals
            for s in self.SIGNALS: # "HUP QUIT INT TERM TTIN TTOU USR1 USR2 WINCH"
                signal.signal(s, self.signal)
            signal.signal(signal.SIGCHLD, self.handle_chld)
```

所有定义的信号处理函数都是 `Aribiter().signal()` ，该函数将接收到的信号存放在 `Arbiter.SIG_QUEUE` 中，最多保留 5 个信号，然后触发 `Arbiter().wakeup()` ，在 `Arbiter().wakeup()` 中，向 `Arbiter.PIPE` 管道写入数据，主要作用是唤醒 Master loop。

```
    def signal(self, sig, frame):
        if len(self.SIG_QUEUE) < 5:
            self.SIG_QUEUE.append(sig)
            self.wakeup()

    def wakeup(self):
        """\
        Wake up the arbiter by writing to the PIPE
        """
        try:
            os.write(self.PIPE[1], b'.')
        except IOError as e:
            if e.errno not in [errno.EAGAIN, errno.EINTR]:
                raise
```


在 Arbiter 类中会实现相应的信号函数处理逻辑，针对 TERM 和 INT 信号处理的主要差异为是否会先执行 `Arbiter().stop(False)` ，最后都会 `raise StopIteration` 。对于 `HUP` 信号是执行自身的 `Arbiter().reload()` 逻辑。

```
    def handle_hup(self):
        """\
        HUP handling.
        - Reload configuration
        - Start the new worker processes with a new configuration
        - Gracefully shutdown the old worker processes
        """
        self.log.info("Hang up: %s", self.master_name)
        self.reload()

    def handle_term(self):
        "SIGTERM handling"
        raise StopIteration

    def handle_int(self):
        "SIGINT handling"
        self.stop(False)
        raise StopIteration

    def handle_quit(self):
        "SIGQUIT handling"
        self.stop(False)
        raise StopIteration

    def handle_ttin(self):
        """\
        SIGTTIN handling.
        Increases the number of workers by one.
        """
        self.num_workers += 1
        self.manage_workers()
```


在 Master 进行信号处理初始化动作后，进入到 Master loop 阶段：


```
        try:
            self.manage_workers()           # 启动 Worker，如果 Worker 数量不足则启动；如果数量超过预期则 kill。

            while True:
                self.maybe_promote_master()

                sig = self.SIG_QUEUE.pop(0) if self.SIG_QUEUE else None
                if sig is None:
                    self.sleep() # 如果 Master 没有接收到信号，则进入到 `Arbiter().sleep()` ，该函数从 `Arbiter.PIPE` 读取数据（阻塞），直到 `Arbiter.PIPE` 有数据后才返回
                    self.murder_workers() # 如果在当前循环中，接收到信号，则进行 worker 处理，清理无用 Worker
                    self.manage_workers() # 重新进入创建、清理 Worker 逻辑
                    continue # 进入下一循环，在下一次循环中，sig 为刚刚唤醒 Master 的信号

                if sig not in self.SIG_NAMES:  # 如果接收到的信号不需要处理，则忽略
                    self.log.info("Ignoring unknown signal: %s", sig)
                    continue

                signame = self.SIG_NAMES.get(sig) # 获取信号名称
                handler = getattr(self, "handle_%s" % signame, None) # 获取 Master 针对该信号的处理函数
                if not handler:
                    self.log.error("Unhandled signal: %s", signame)
                    continue
                self.log.info("Handling signal: %s", signame)
                handler() # 执行信号处理
                self.wakeup() 
        except (StopIteration, KeyboardInterrupt): # 如果信号为 TERM 或 INT，则会触发 Exception，进入到 `Arbiter().halt()` 逻辑，清理配置并退出进程
            self.halt()

```


### Worker

Master 创建 Worker 时，先执行 `worker.init_process()` 用来初始化进程

```
        self.init_signals()
        ...
        # Enter main run loop
        self.booted = True
        self.run()
```

```
    def init_signals(self):
        # reset signaling
        for s in self.SIGNALS:
            signal.signal(s, signal.SIG_DFL)

        # init new signaling 
        signal.signal(signal.SIGQUIT, self.handle_quit)
        signal.signal(signal.SIGTERM, self.handle_exit)
        signal.signal(signal.SIGINT, self.handle_quit)
        signal.signal(signal.SIGWINCH, self.handle_winch)
        signal.signal(signal.SIGUSR1, self.handle_usr1)
        signal.signal(signal.SIGABRT, self.handle_abort)

        # Don't let SIGTERM and SIGUSR1 disturb active requests
        # by interrupting system calls
        signal.siginterrupt(signal.SIGTERM, False)
        signal.siginterrupt(signal.SIGUSR1, False)

        if hasattr(signal, 'set_wakeup_fd'):
            signal.set_wakeup_fd(self.PIPE[1])
```

在 Worker 中，所有的信号处理函数都是直接触发，没有采用 Master 的 `SIG_QUEUE` 形式：

```
    def handle_usr1(self, sig, frame):
        self.log.reopen_files()

    def handle_exit(self, sig, frame):
        self.alive = False

    def handle_quit(self, sig, frame):
        self.alive = False
        # worker_int callback
        self.cfg.worker_int(self)
        time.sleep(0.1)
        sys.exit(0)

    def handle_abort(self, sig, frame):
        self.alive = False
        self.cfg.worker_abort(self)
        sys.exit(1)
```

在 Worker 的 loop 逻辑中，优先检查 `self.alive` 是否为 True，如果为 True ，则进入请求处理逻辑：

```
    def run_for_one(self, timeout):
        listener = self.sockets[0]
        while self.alive:
            self.notify()

            # Accept a connection. If we get an error telling us
            # that no connection is waiting we fall down to the
            # select which is where we'll wait for a bit for new
            # workers to come give us some love.
            try:
                self.accept(listener)
                # Keep processing clients until no one is waiting. This
                # prevents the need to select() for every client that we
                # process.
                continue

            except EnvironmentError as e:
                if e.errno not in (errno.EAGAIN, errno.ECONNABORTED,
                                   errno.EWOULDBLOCK):
                    raise

            if not self.is_parent_alive():
                return

            try:
                self.wait(timeout)
            except StopWaiting:
                return
```



## 完整流程

以 HUP 信号为例，在 Gunicorn 文档中，HUP 可以优雅的重启 Worker 进程：

> HUP: Reload the configuration, start the new worker processes with a new configuration and gracefully shutdown older workers. If the application is not preloaded (using the preload_app option), Gunicorn will also load the new version of it.


当 Master 进程收到 HUP 信号后：
* Master loop 唤醒，进入 `murder_workers` 和 `manage_workers` 处理
* Master loop 进入下一循环，获取到 HUP 信号处理函数
* 执行 `Arbiter().handle_hup()` 
* 执行 `Arbiter().reload()` 重新加载配置，重新加载 WSGI app，并按照 Worker 配置启动新 Worker ，启动完成后，执行 `manage_workers` 进行原有 Worker 处理，因为此时 Worker 数量为预期的一倍，因此会进入停掉原有 Worker 处理逻辑，执行 `Arbiter().kill_worker()` 逻辑，执行 `os.kill` ，传递信号为 TERM
* 此时 Master 信号处理完成，执行 `Arbiter().wakeup()` 使其重新进入 loop 阻塞逻辑。


当 Worker 进程收到 TERM 信号后：
* 执行 `Worker().handle_exit()` 逻辑，将 `self.alive` 置为 False
* 在 Worker 的 loop 逻辑中，优先检查 `self.alive` 是否为 True，如果不为True，则处理完成当前逻辑后，下一次循环退出，以此来实现 graceful shutdown


## 参考链接
* http://flaneur2020.github.io/2020/01/12/note-about-graceful-shutdown/