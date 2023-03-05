---
title: huey 源码阅读
date: 2019-03-31 11:25:48
tags:
- Python
---

## 背景

最近读完了 《Redis 实战》对 Redis 有了一些了解，但是没有在实际项目中应用过，就想找一个使用 Redis 的项目来看看，找到 Huey 是因为之前使用过，趁机了解下具体实现。


## 简介

Huey 的定位是一个轻量级的任务队列，仅依赖于 Redis 作为任务相关信息存储，支持的功能有：
* 多种 worker 执行方式：thread，process，greenlet
* 支持多种任务类型：特定时间运行，周期性运行
* 包含重试机制，可以指定重试次数及重试间隔
* 支持任务锁
* ...

我们根据官方的[示例](https://github.com/coleifer/huey/blob/master/examples/simple/README)，来看看 Huey 是如何处理任务的，目录结构如下：

```bash
master ✔ $ pwd
/Users/yiran/Documents/git-repo/huey/examples/simple
yiran@zhouyirandeMacBook-Pro:~/Documents/git-repo/huey/examples/simple
master ✔ $ tree .
.
├── README
├── __init__.py
├── config.py
├── cons.sh
├── main.py
└── tasks.py
```

注意，这个目录结构是 Huey [官方建议](https://huey.readthedocs.io/en/latest/imports.html)的，具体原因为：

> Behind-the-scenes when you decorate a function with task() or periodic_task(), the function registers itself with a centralized in-memory registry. When that function is called, a reference is put into the queue (along with the arguments the function was called with, etc), and when that message is consumed, the function is then looked-up in the consumer’s registry. Because of the way this works, it is strongly recommended that all decorated functions be imported when the consumer starts up. 

## Task

Huey 支持通过 @task 装饰器的方式创建任务，示例如下：

```python
from huey import RedisHuey

huey = RedisHuey('simple.test', blocking=True)

@huey.task()
def count_beans(num):
    print('-- counted %s beans --' % num)
    return 'Counted %s beans' % num
```

从 huey.RedisHuey 创建了 huey 实例，我们看下 RedisHuey 是什么：

```python
class RedisHuey(Huey):
    def get_storage(self, read_timeout=1, max_errors=1000,
                    connection_pool=None, url=None, **connection_params):
        return RedisStorage(
            name=self.name,
            blocking=self.blocking,
            read_timeout=read_timeout,
            max_errors=max_errors,
            connection_pool=connection_pool,
            url=url,
            **connection_params)
```

在 huey.storage 中定义了 RedisHuey，继承自 Huey 类，重新实现了 `get_storage` 方法，我们看下 `RedisStorage` 是做什么用途的：

```python
class RedisStorage(BaseStorage):
    redis_client = Redis

    def __init__(self, name='huey', blocking=False, read_timeout=1,
                 max_errors=1000, connection_pool=None, url=None,
                 client_name=None, **connection_params):

        if Redis is None:
            raise ImportError('"redis" python module not found, cannot use '
                              'Redis storage backend. Run "pip install redis" '
                              'to install.')

        if sum(1 for p in (url, connection_pool, connection_params) if p) > 1:
            raise ValueError(
                'The connection configuration is over-determined. '
                'Please specify only one of the the following: '
                '"url", "connection_pool", or "connection_params"')

        if url:
            connection_pool = ConnectionPool.from_url(
                url, decode_components=True)
        elif connection_pool is None:
            connection_pool = ConnectionPool(**connection_params)
    ...

    def clean_name(self, name):
    def convert_ts(self, ts):
    def enqueue(self, data):
    def dequeue(self):
    ...
    def get_errors(self, limit=None, offset=0):
    def flush_errors(self):
    def emit(self, message):
    def listener(self):
    def __iter__(self):
```

RedisStorage 继承自 Storage，主要用于所有任务相关信息的写入及读取，目前 Huey 中只实现了 Storage 介质，如果想使用其他方式（如 MongoDB）就需要自己实现了。

知道了 RedisHuey 跟 Huey 的主要区别只是在于 `get_storage` 方法不同，那么看看 `task` 方法的具体实现：

```python
    def task(self, retries=0, retry_delay=0, retries_as_argument=False,
             include_task=False, name=None, **task_settings):
        def decorator(func):
            """
            Decorator to execute a function out-of-band via the consumer.
            """
            return TaskWrapper(
                self,
                func.func if isinstance(func, TaskWrapper) else func,
                retries=retries,
                retry_delay=retry_delay,
                retries_as_argument=retries_as_argument,
                include_task=include_task,
                name=name,
                **task_settings)
        return decorator
```

我们看下 `TaskWrapper` 做了啥，一些变量复制忽略掉，关键的是这几行:

```python
class TaskWrapper(object):
    def __init__(self, huey, func, retries=0, retry_delay=0,
                 retries_as_argument=False, include_task=False, name=None,
                 task_base=None, **task_settings):
        ...
        self.task_class = create_task(
            QueueTask if task_base is None else task_base,
            func,
            retries_as_argument,
            name,
            include_task,
            **task_settings)
        self.huey.registry.register(self.task_class)

    def is_revoked(self, dt=None, peek=True):
        return self.huey.is_revoked(self.task_class, dt, peek)

    def revoke(self, revoke_until=None, revoke_once=False):
        self.huey.revoke_all(self.task_class, revoke_until, revoke_once)
```

将函数 func 创建为一个任务，并将任务注册到 Huey 中。同时实现了一些方法，这些方法最终调用的都是在 Huey 类中实现的。

## Consumer

```bash
root@yiran30250:~/project/huey/examples/simple
master ✔ $ cat cons.sh
#!/bin/bash
echo "HUEY CONSUMER"
echo "-------------"
echo "In another terminal, run 'python main.py'"
echo "Stop the consumer using Ctrl+C"
PYTHONPATH=.:$PYTHONPATH
export WORKER_CLASS=${1:-thread}
python ../../huey/bin/huey_consumer.py main.huey --workers=2 -v -s 10 -k $WORKER_CLASS -C
```

接下来我们看下 Consumer 是如何实现的，在进程启动脚本里，先忽略其他参数，我们指定了 huey 实例，并指定了 worker 数量为 2，我们看下是如何执行的：

huey_consumer.py

```python
def consumer_main():
    ...
    huey_instance = load_huey(args[0])
    config.setup_logger()
    consumer = huey_instance.create_consumer(**config.values)
    consumer.run()
if __name__ == '__main__':
    consumer_main()
```

加载 huey 实例，创建相应 Consumer 实例并运行，我们看下 Consumer 做了什么：

```python
class Consumer(object):
    """
    Consumer sets up and coordinates the execution of the workers and scheduler
    and registers signal handlers.
    """
```

根据注释我们可以知道 Consumer 主要是启动了 worker 和 scheduler，并截获相应的信息进行处理。
在 huey/consumer.py 中定义了 `Worker`,`Scheduler`,`Environment` 类，其中 `Environment` 根据所指定的 worker 类型的不同，分为 thread,process,greenlet。

我们看下 `Worker` 是如何执行对应的任务的：

## Worker

```python
    def loop(self, now=None):
        task = None
        exc_raised = True
        try:
            task = self.huey.dequeue() # 从 hue 中获取任务，也就是从 redis 中获取任务
            ...
        if task:
            self.delay = self.default_delay
            self.handle_task(task, now or self.get_now()) # 如果获取到了任务，对任务进行处理
        elif exc_raised or not self.huey.blocking:
            self.sleep()

    def handle_task(self, task, ts):
        if not self.huey.ready_to_run(task, ts):
            self.add_schedule(task) # 若任务没有到达执行时间，则添加到 schedule 中
        elif not self.is_revoked(task, ts):
            self.process_task(task, ts) # 若任务没有被取消，则执行任务
        else:
            self.huey.emit_task(
                EVENT_REVOKED,
                task,
                timestamp=ts)
            self._logger.debug('Task %s was revoked, not running', task) # 任务被取消，通知 event
    
    def process_task(self, task, ts):
        ...
        self.run_pre_execute_hooks(task)   # 执行 pre hook 动作
        ...  
        task_value = self.huey.execute(task) # 具体执行 task
        ...
        self.run_post_execute_hooks(task, task_value, exception) # 执行 post hook 动作
        ...
```

看到 self.huey.execute(task) 我们发现最终还是通过 Huey 中的方法 execute 来执行 task，那么我们看下是如何实现的：

```python
    def execute(self, task):
        if not isinstance(task, QueueTask):
            raise TypeError('Unknown object: %s' % task)

        try:
            result = task.execute()
```


发现这里调用的是 task.execute，这里的 task 是谁呢，是我们最开始提到的 `TaskWrapper` 么，在 `TaskWrapper` 中没有实现 `execute` 方法，这里其实是上面提到的 `create_task` 返回的类，我们看下 `create_task` 的具体实现：


```python
def create_task(task_class, func, retries_as_argument=False, task_name=None,
                include_task=False, **kwargs):
    def execute(self):
        args, kwargs = self.data or ((), {})
        if retries_as_argument:
            kwargs['retries'] = self.retries
        if include_task:
            kwargs['task'] = self
        return func(*args, **kwargs)

    attrs = {
        'execute': execute,
        '__module__': func.__module__,
        '__doc__': func.__doc__}
    attrs.update(kwargs)

    if not task_name:
        task_name = func.__name__

    return type(task_name, (task_class,), attrs)
```

可以看到 `execute` 函数中最终执行的就是 func 自己， `func(*args, **kwargs)` ，通过 type 返回真正的 task 类，指定父类为 `task_class` （默认是 QueueTask）。

到这里我们就完成了整个流程：任务注册，任务调度，任务执行。那么我们再来看看 Huey 中的锁是怎么实现的。

## Lock

```python
class TaskLock(object):
    """
    Utilize the Storage key/value APIs to implement simple locking. For more
    details see :py:meth:`Huey.lock_task`.
    """
    def __init__(self, huey, name):
        self._huey = huey
        self._name = name
        self._key = '%s.lock.%s' % (self._huey.name, self._name)
        self._huey._locks.add(self._key)

    def __call__(self, fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            with self:
                return fn(*args, **kwargs)
        return inner

    def __enter__(self):
        if not self._huey._put_if_empty(self._key, '1'):
            raise TaskLockedException('unable to set lock: %s' % self._name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._huey._get_data(self._key)
```

```python
    def put_if_empty(self, key, value):
        return self.conn.hsetnx(self.result_key, key, value)
```


在 Huey 中，任务锁的实现非常简单，单纯的利用了下 Redis 中的 HSETNX 机制：

> Sets field in the hash stored at key to value, only if field does not yet exist. If key does not exist, a new key holding a hash is created. If field already exists, this operation has no effect.

## 总结

Huey 作为一个任务调度应用，整体代码量不多，但是有很多值得学习的地方，也许过段时间再看会有新的收获。







