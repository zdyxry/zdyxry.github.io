---
title: apscheduler 源码阅读
date: 2019-04-06 10:58:49
tags:
- Python
---

## 简介

apscheduler 全称 `Advanced Python Scheduler`，调度器，主要功能如下：
* 动态添加、删除任务
* 暂停、恢复任务
* 周期性调度：cron,date,interval
* ...

那么接下来我们根据官方示例，看看 apscheduler 是如何进行处理任务的。

示例版本为 2.1，因为在 2.1 版本包含目前 master 分支上的主要功能，简单易懂。

代码结构如下：
```bash
yiran@zhouyirandeMacBook-Pro:~/Documents/git-repo/apscheduler
2.1 ✔ $ tree apscheduler
apscheduler
├── __init__.py
├── events.py
├── job.py
├── jobstores
│   ├── __init__.py
│   ├── base.py
│   ├── mongodb_store.py
│   ├── ram_store.py
│   ├── redis_store.py
│   ├── shelve_store.py
│   └── sqlalchemy_store.py
├── scheduler.py
├── threadpool.py
├── triggers
│   ├── __init__.py
│   ├── cron
│   │   ├── __init__.py
│   │   ├── expressions.py
│   │   └── fields.py
│   ├── interval.py
│   └── simple.py
└── util.py
```

示例：
```python
from datetime import datetime, timedelta

from apscheduler.scheduler import Scheduler
from apscheduler.jobstores.shelve_store import ShelveJobStore


def alarm(time):
    print('Alarm! This alarm was scheduled at %s.' % time)


if __name__ == '__main__':
    scheduler = Scheduler(standalone=True)
    scheduler.add_jobstore(ShelveJobStore('example.db'), 'shelve')
    alarm_time = datetime.now() + timedelta(seconds=10)
    scheduler.add_date_job(alarm, alarm_time, name='alarm',
                           jobstore='shelve', args=[datetime.now()])
    print('To clear the alarms, delete the example.db file.')
    print('Press Ctrl+C to exit')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
```

## Scheduler

上述示例很容易理解，首先对 `Scheduler` 实例化，然后添加 jobstore，定义一个名为 `alarm` 的 job，并指定其运行时间为当前时间 + 10s，将该 job 添加到 scheduler 中，添加 job 类型为 `date_job`，然后启动 scheduler。

可以看到我们所有的操作都是通过 scheduler 方法实现的，那么我们来看下 `Scheduler` 类具体实现了哪些功能：

```python
class Scheduler(object):
    """
    This class is responsible for scheduling jobs and triggering
    their execution.
    """

    _stopped = True
    _thread = None

    def __init__(self, gconfig={}, **options):
        self._wakeup = Event()
        self._jobstores = {}
        self._jobstores_lock = Lock()
        self._listeners = []
        self._listeners_lock = Lock()
        self._pending_jobs = []
        self.configure(gconfig, **options)
```

在 `Scheduler` 构造函数中，对一些变量进行初始化，这里要注意 `self._wakeup` ，后续的一些主要功能都是通过它来实现的。接下来看看 `add_jobstore` 方法：

```python
    def add_jobstore(self, jobstore, alias, quiet=False):
        self._jobstores_lock.acquire() # 请求锁
        try:
            if alias in self._jobstores:
                raise KeyError('Alias "%s" is already in use' % alias)
            self._jobstores[alias] = jobstore # 将 jobstore 别名作为 key，添加到 self._jobstores 中
            jobstore.load_jobs() # 加载 jobstore 中所有 job
        finally:
            self._jobstores_lock.release() # 释放锁

        # Notify listeners that a new job store has been added
        self._notify_listeners(JobStoreEvent(EVENT_JOBSTORE_ADDED, alias)) # 事件通知

        # Notify the scheduler so it can scan the new job store for jobs
        if not quiet:
            self._wakeup.set() # 将 Event 置为 True
```

在 `add_jobstore` 中，将 jobstore 添加到 scheduler 中，并加载当前 jobstore 中的所有任务，接下来将具体的 job 添加到 scheduler 中：

```python
    def add_date_job(self, func, date, args=None, kwargs=None, **options):
        trigger = SimpleTrigger(date)
        return self.add_job(trigger, func, args, kwargs, **options)
```

这里的 `SimpleTrigger` 只是多种 Trigger 中的一种，根据 Trigger 类型的不同，最主要的差别在于 `get_next_fire_time` 计算方式不同。

如果添加的任务是 interval_job，那么对应 Trigger 为 `IntervalTrigger` ；如果添加的任务是 cron_job，那么对应的 Trigger 为 `CronTrigger`。

可以看到不同的任务只是 Trigger 计算方式不同，最终还是通过 `add_job` 方法，继续看：

```python
    def add_job(self, trigger, func, args, kwargs, jobstore='default',
                **options):
        job = Job(trigger, func, args or [], kwargs or {},
                  options.pop('misfire_grace_time', self.misfire_grace_time),
                  options.pop('coalesce', self.coalesce), **options) # 将 job 实例化
        if not self.running: # 如果 scheduler 未启动，那么将其添加到等待队列中
            self._pending_jobs.append((job, jobstore))
            logger.info('Adding job tentatively -- it will be properly '
                        'scheduled when the scheduler starts')
        else:
            self._real_add_job(job, jobstore, True) # 否则添加 job 到 jobstore 中
        return job
```

继续看 `_real_add_job` 中的实现：

```python
    def _real_add_job(self, job, jobstore, wakeup):
        job.compute_next_run_time(datetime.now()) # 计算job 下次运行时间
        if not job.next_run_time:
            raise ValueError('Not adding job since it would never be run')

        self._jobstores_lock.acquire() # 请求锁
        try:
            try:
                store = self._jobstores[jobstore]
            except KeyError:
                raise KeyError('No such job store: %s' % jobstore)
            store.add_job(job) # 添加 job
        finally:
            self._jobstores_lock.release()

        # Notify listeners that a new job has been added
        event = JobStoreEvent(EVENT_JOBSTORE_JOB_ADDED, jobstore, job)
        self._notify_listeners(event) # 事件通知

        logger.info('Added job "%s" to job store "%s"', job, jobstore)

        # Notify the scheduler about the new job
        if wakeup:
            self._wakeup.set() # # 将 Event 置为 True
```

在 `_real_add_job` 中我们终于看到 `store.add_job(job)` ，至于 `store.add_job` 如何实现我们之后看 `JobStore` 再说。

现在我们已经给 scheduler 添加了 jobstore 和 job，那么看下 scheduler 是如何运行的：

```python
    def start(self):
        ...
        # Schedule all pending jobs
        for job, jobstore in self._pending_jobs: # 将 scheduler 未运行时添加的 job，即在等待队列中的 job 添加到 jobstore 中
            self._real_add_job(job, jobstore, False)
        del self._pending_jobs[:]

        self._stopped = False
        if self.standalone:
            self._main_loop()
        else:
            self._thread = Thread(target=self._main_loop, name='APScheduler')
            self._thread.setDaemon(self.daemonic)
            self._thread.start()
```

在 scheduler 运行时，会先将所有的 job 加载到 jobstore 中，然后调用 `self._main_loop` ，如果 Standalone 为 True，则会一直阻塞知道没有 job 需要运行，看看 `self._main_loop` 做了啥：

```python
    def _main_loop(self):
        """Executes jobs on schedule."""

        logger.info('Scheduler started')
        self._notify_listeners(SchedulerEvent(EVENT_SCHEDULER_START)) # 事件通知 

        self._wakeup.clear()
        while not self._stopped:
            logger.debug('Looking for jobs to run')
            now = datetime.now()
            next_wakeup_time = self._process_jobs(now) # 计算下次唤醒时间

            if next_wakeup_time is not None:
                wait_seconds = time_difference(next_wakeup_time, now)
                logger.debug('Next wakeup is due at %s (in %f seconds)',
                             next_wakeup_time, wait_seconds)
                try:
                    self._wakeup.wait(wait_seconds) # 等待 Event flag
                except IOError:  # Catch errno 514 on some Linux kernels
                    pass
                self._wakeup.clear()
            elif self.standalone:
                logger.debug('No jobs left; shutting down scheduler')
                self.shutdown() # 若 scheduler standalone 为 True 且 jobs 为空，则停止 scheduler
                break
            else:
                logger.debug('No jobs; waiting until a job is added')
                try:
                    self._wakeup.wait() # 等待 Event flag
                except IOError:  # Catch errno 514 on some Linux kernels
                    pass
                self._wakeup.clear()
```

还记得上面提到的 `Scheduler` 构造函数中的 `self._wakeup` 么，它实际上是 `threading.Event` ，它的 wait 方法会一直 block 直到 Event flag 为 True，也就是我们上面看到的 `self._wakeup.set()` ，那么我们可以知道在 `Scheduler` 中有几种场景会置为 True：
1. Scheduler.shutdown
2. Scheduler.add_jobstore
3. Scheduler._real_add_job

如果没有触发上述场景，则 `_main_loop` 会根据 jobs 的执行时间一直循环等待。

## JobStore

在 apscheduler 中，JobStore 只是单纯的实现了 Job 相关的方法：

```python
class JobStore(object):
    def add_job(self, job):
    def update_job(self, job):
    def remove_job(self, job):
    def load_jobs(self):
    def close(self):
```

其中，对 job 的操作会根据 JobStore 类型的不同，而采用不同的序列化方式，比如在 `MongoDBJobStore` 中采用的是 `bson.binary`，而在其他 JobStore 比如 `RedisJobStore` 中采用的都是 `pickle`。

## Events

在 `Scheduler` 中，我们已经看到通过 `threading.Event` 来实现事件通知的，那么我们通知的 `Event` 都是在 `apscheduler.events` 中定义好的，比如：

```python
class JobEvent(SchedulerEvent):
    def __init__(self, code, job, scheduled_run_time, retval=None,
                 exception=None, traceback=None):
        SchedulerEvent.__init__(self, code)
        self.job = job
        self.scheduled_run_time = scheduled_run_time
        self.retval = retval
        self.exception = exception
        self.traceback = traceback
```

在 `JobEvent` 中，我们能看到 job 的执行时间，返回值，异常捕获等信息。如果看过之前关于 [huey 博客](https://zdyxry.github.io/2019/03/31/huey-%E6%BA%90%E7%A0%81%E9%98%85%E8%AF%BB/) 的同学应该知道，在 huey 中是可以直接通过 task id 获取 task 执行结果的，但是在 apscheduler 中，我们并没有直接获取该结果的方法，而是通过在 `Scheduler` 中的 `add_listener` 添加监听者，监控指定成功的 Job 获取该 Job 的返回值，感觉这里不太友好。

## 总结

到这里我们基本上已经将 apscheduler 的流程走了一遍，具体的 Trigger 计算时间的方法之后有机会单独写一下关于 cron，interval，date 的计算方法。

与 huey 相比，apscheduler 使用上要简单，但是简单也意味着功能的不足，比如获取 job 执行结果、job retry 机制等等。当然也有比较好的地方，apscheduler 在跟 web 框架比如 Flask，Django 集成的时候有一些第三方插件可以直接使用，不用像 Huey 一样要单独启动一个 consumer 进程，比较方便。


