---
title: Celery/Kombu MongoDB 连接异常调查记录
date: 2022-05-09 14:44:42
tags:
- Python
- Celery
---


## 背景

产品组件 JobCenter 使用 Celery 实现异步任务中心，同时会运行 job-center-worker （celery worker） 和 job-center-scheduler(celery beat) 两个进程，使用 MongoDB 作为 Backend 存储 message 等信息（Celery 官方已说明不再维护对 MongoDB 的支持）。其中 MongoDB 配置了 ReplicaSet 保证高可用。

近期 Celery/Kombu 中遇到了 [`No free channel ids` 问题](https://github.com/celery/kombu/issues/1504#event-6304977800)，经过排查在这个 [PR](https://github.com/celery/kombu/commit/1c2b9723851db3caa913b8da19d6ccad447f3568) 中解决了该问题，在考虑 cherry-pick 的工作量和可维护性考虑，最终将产品中的 celery 和 kombu 组件从 3.x 统一升级到了 4.x 版本。

测试同学反馈近期在进行可靠性测试时，发现将 MongoDB 节点的存储网络 `ifdown` 会导致 JobCenter hang. 针对该问题进行调查。

## 调查

### Celery

先尝试复现该问题，首先尝试 ifdown Primary 节点存储网络，现象复现；尝试 ifdown Secondary 节点存储网络，无法复现；
尝试 stop MongoDB service 替代 ifdown，Primary 或 Secondary 均无法复现。推测与 MongoDB 连接处理有关。

观察现象复现的日志，在存储网络异常时，日志无任何输出，在存储网络恢复正常后，可以看到 Celery 记录在尝试连接 Broker （MongoDB）时发生了异常，尝试重连。


```bash
[2022-05-07 10:13:01,362: WARNING/MainProcess] consumer: Connection to broker lost. Trying to re-establish the connection...
Traceback (most recent call last):
  File "/usr/lib/python2.7/site-packages/celery/worker/consumer/consumer.py", line 318, in start
    blueprint.start(self)
  File "/usr/lib/python2.7/site-packages/celery/bootsteps.py", line 119, in start
    step.start(parent)
  File "/usr/lib/python2.7/site-packages/celery/worker/consumer/consumer.py", line 596, in start
    c.loop(*c.loop_args())
  File "/usr/lib/python2.7/site-packages/celery/worker/loops.py", line 121, in synloop
    connection.drain_events(timeout=2.0)
  File "/usr/lib/python2.7/site-packages/kombu/connection.py", line 315, in drain_events
    return self.transport.drain_events(self.connection, **kwargs)
  File "/usr/lib/python2.7/site-packages/kombu/transport/virtual/base.py", line 963, in drain_events
    get(self._deliver, timeout=timeout)
  File "/usr/lib/python2.7/site-packages/kombu/utils/scheduling.py", line 56, in get
    return self.fun(resource, callback, **kwargs)
  File "/usr/lib/python2.7/site-packages/kombu/transport/virtual/base.py", line 1001, in _drain_channel
    return channel.drain_events(callback=callback, timeout=timeout)
  File "/usr/lib/python2.7/site-packages/kombu/transport/virtual/base.py", line 745, in drain_events
    return self._poll(self.cycle, callback, timeout=timeout)
  File "/usr/lib/python2.7/site-packages/kombu/transport/virtual/base.py", line 402, in _poll
    return cycle.get(callback)
  File "/usr/lib/python2.7/site-packages/kombu/utils/scheduling.py", line 56, in get
    return self.fun(resource, callback, **kwargs)
  File "/usr/lib/python2.7/site-packages/kombu/transport/virtual/base.py", line 405, in _get_and_deliver
    message = self._get(queue)
  File "/usr/lib/python2.7/site-packages/kombu/transport/mongodb.py", line 141, in _get
    remove=True,
  File "/usr/lib64/python2.7/site-packages/pymongo/collection.py", line 2315, in find_and_modify
    allowable_errors=[_NO_OBJ_ERROR])
  File "/usr/lib64/python2.7/site-packages/pymongo/collection.py", line 205, in _command
    read_concern=read_concern)
  File "/usr/lib64/python2.7/site-packages/pymongo/pool.py", line 218, in command
    self._raise_connection_failure(error)
  File "/usr/lib64/python2.7/site-packages/pymongo/pool.py", line 346, in _raise_connection_failure
    raise error
AutoReconnect: connection closed
[2022-05-07 10:13:01,363: WARNING/MainProcess] Restoring 1 unacknowledged message(s)
```


对应 Celery 代码在 worker/consumer/consumer.py，Blueprint 是 Celery 启动入口，可以看到在 `blueprint.start(self)` 阶段进行了异常处理，针对 `self.connection_errors` 来触发重连接。

```python
    CONNECTION_RETRY = """\
    consumer: Connection to broker lost. \
    Trying to re-establish the connection...\
    """
    ...
    def start(self):
        blueprint = self.blueprint
        while blueprint.state != CLOSE:
            maybe_shutdown()
            if self.restart_count:
                try:
                    self._restart_state.step()
                except RestartFreqExceeded as exc:
                    crit('Frequent restarts detected: %r', exc, exc_info=1)
                    sleep(1)
            self.restart_count += 1
            try:
                blueprint.start(self)
            except self.connection_errors as exc:
                # If we're not retrying connections, no need to catch
                # connection errors
                if not self.app.conf.broker_connection_retry:
                    raise
                if isinstance(exc, OSError) and exc.errno == errno.EMFILE:
                    raise  # Too many open files
                maybe_shutdown()
                if blueprint.state != CLOSE:
                    if self.connection:
                        self.on_connection_error_after_connected(exc)
                    else:
                        self.on_connection_error_before_connected(exc)
                    self.on_close()
                    blueprint.restart(self)

    def on_connection_error_before_connected(self, exc):
        error(CONNECTION_ERROR, self.conninfo.as_uri(), exc,
              'Trying to reconnect...')

    def on_connection_error_after_connected(self, exc):
        warn(CONNECTION_RETRY, exc_info=True)
        try:
            self.connection.collect()
        except Exception:
            pass
```

`self.connection_errors` 对应的其实是 Kombu 中 Transport 定义的 ，可以在 `kombu/kombu/transport/mongodb.py` 中查看，在当前版本中，定义为 `pymongo.errors.ConnectionFailure` ，pymongo 中常见的网络连接异常 `AutoReconnect` 或 `NetworkTimeout` 均继承自 `ConnectionFailure` 。

```python
class Transport(virtual.Transport):
    Channel = Channel

    can_parse_url = True
    polling_interval = 1
    default_port = DEFAULT_PORT
    connection_errors = (
        virtual.Transport.connection_errors + (errors.ConnectionFailure, )
    )
```

从目前来看，Celery 可以正确处理 kombu 上报的异常，但是在存储网络异常时，Kombu 没有抛出异常，于是问题调查从 Celery 转到 Kombu。

### Kombu

主要看 MongoDB Transport 关于建立连接部分的处理，代码执行路径依次是： `client` -> `_create_client` -> `_open` -> `_parse_uri` ，其中 `_open` 是真正建立连接的处理，连接所采用的参数是在 `_parse_uri` 返回的，`_parse_uri` 最终调用的是 `pymongo.uri_parser.parse_uri`。


```python
    def _open(self, scheme='mongodb://'):
        hostname, dbname, options = self._parse_uri(scheme=scheme)

        conf = self._prepare_client_options(options)
        conf['host'] = hostname

        env = _detect_environment()
        if env == 'gevent':
            from gevent import monkey
            monkey.patch_all()
        elif env == 'eventlet':
            from eventlet import monkey_patch
            monkey_patch()

        mongoconn = MongoClient(**conf)
        database = mongoconn[dbname]

        version_str = mongoconn.server_info()['version']
        version = tuple(map(int, version_str.split('.')))

        if version < (1, 3):
            raise VersionMismatch(E_SERVER_VERSION.format(version_str))
        elif self.ttl and version < (2, 2):
            raise VersionMismatch(E_NO_TTL_INDEXES.format(version_str))

        return database

    def _parse_uri(self, scheme='mongodb://'):
        # See mongodb uri documentation:
        # http://docs.mongodb.org/manual/reference/connection-string/
        client = self.connection.client
        hostname = client.hostname

        if not hostname.startswith(scheme):
            hostname = scheme + hostname

        if not hostname[len(scheme):]:
            hostname += self.default_hostname

        if client.userid and '@' not in hostname:
            head, tail = hostname.split('://')
            credentials = client.userid
            if client.password:
                credentials += ':' + client.password
            hostname = head + '://' + credentials + '@' + tail

        port = client.port if client.port else self.default_port
        parsed = uri_parser.parse_uri(hostname, port)
        dbname = parsed['database'] or client.virtual_host
        if dbname in ('/', None):
            dbname = self.default_database
        options = {
            'auto_start_request': True,
            'ssl': self.ssl,
            'connectTimeoutMS': (int(self.connect_timeout * 1000)
                                 if self.connect_timeout else None),
        }
        options.update(parsed['options'])

        return hostname, dbname, options
```

假设我们连接参数是 `mongodb://192.168.1.1:27017,192.168.1.2:27017/yiran` ，那么 `pymongo.uri_parser.parse_uri` 解析的结果会是： `{'username': None, 'nodelist': [('192.168.1.1', 27017), ('192.168.1.2', 27017)], 'database': 'yiran', 'collection': None, 'password': None, 'options': {}}` 。

socketTimeoutMS在我们的环境中，MongoDB 的 URI 中并没有指定 options，所以 `pymongo.uri_parser.parse_uri` 结果的 `options` 为空。最终连接所使用的 `options` 就是在 `_parse_uri` 中定义的 options ，其中类变量 `connect_timeout` 在 Channel 定义为 None，所以最终 Kombu 建立 MongoDB 连接并没有设置 `socketTimeoutMS`，如果不设置 `socketTimeoutMS` ，默认是 None，永久等待。当网络出现异常时，直观看到的现象会是 hang 住。

```python
class Channel(virtual.Channel):
    """MongoDB Channel."""

    supports_fanout = True

    # Mutable container. Shared by all class instances
    _fanout_queues = {}

    # Options
    ssl = False
    ttl = False
    connect_timeout = None
    capped_queue_size = 100000
    calc_queue_size = True
```

### Celery 与 Kombu 参数传递

现在观察到连接参数不符合预期，为什么之前的 3.x 版本没有问题？切换到 3.x 分支查看对应的代码，可以看到大体逻辑都是类似的，关于 options 的处理，3.x 存在一行 ： `options.update(client.transport_options)` ，这里的 client 在函数最开始赋值，对应的是 `self.connection.client` ，`self.connection` 是 Transport 构造传入的参数。

```python
    def _parse_uri(self, scheme='mongodb://'):
        # See mongodb uri documentation:
        # http://docs.mongodb.org/manual/reference/connection-string/
        client = self.connection.client
        hostname = client.hostname

        if not hostname.startswith(scheme):
            hostname = scheme + hostname

        if not hostname[len(scheme):]:
            hostname += DEFAULT_HOST

        if client.userid and '@' not in hostname:
            head, tail = hostname.split('://')

            credentials = client.userid
            if client.password:
                credentials += ':' + client.password

            hostname = head + '://' + credentials + '@' + tail

        port = client.port if client.port is not None else DEFAULT_PORT

        parsed = uri_parser.parse_uri(hostname, port)

        dbname = parsed['database'] or client.virtual_host

        if dbname in ('/', None):
            dbname = 'kombu_default'

        options = {
            'auto_start_request': True,
            'ssl': client.ssl,
            'connectTimeoutMS': (int(client.connect_timeout * 1000)
                                 if client.connect_timeout else None),
        }
        options.update(client.transport_options)
        options.update(parsed['options'])

        return hostname, dbname, options
```

`connection` 对应的就是 Kombu 中的 `Connection` ，Kombu 对外隐藏了 Transport ，Celery 在初始化阶段，会建立连接，调用路径是 `celery/app/base.py:Celery._connection` -> `celery/app/amqp.py:AMQP.Connection` -> `kombu/connection.py:Connection` 。传递参数 `transport_options` 就是在 Celery app 声明时配置的参数，具体可配置参数可以参考文档： https://docs.celeryq.dev/en/stable/userguide/configuration.html。

在我们的场景中，声明了以下参数：

```
BROKER_TRANSPORT_OPTIONS = {
    "connect": False,
    "maxPoolSize": 5 if "worker" in process_cmdline else 2,
    "socketTimeoutMS": 5000,
    "connectTimeoutMS": 5000,
    "serverSelectionTimeoutMS": 5000,
    "w": 0,
}
```

在 Kombu 使用 MongoDB Transport 时，最终会带有这些参数创建 MongoDB 连接，所以不会出现此问题说描述的现象。



## Celery 改动背景

@rmihael 上报了一个问题： [Celery events are not removed from MongoDB broker #1047](https://github.com/celery/celery/issues/1047) ，表示在使用 Celery Flower（Celery 监控组件）后，`messages` 中的事件不会清除，导致占用了大量的 MongoDB 存储空间。该 Issue 中讨论最终决定使用 MongoDB TTL 来解决此问题。

在 Kombu 4.x 开发周期中，@daevaorn 提交了 [MongoDB TTL support and refactorings #537](https://github.com/celery/kombu/pull/537) 用来支持 MongoDB TTL，在该 PR 中包含了大量与 TTL 无关的 commit，并且包含了一定的重构，commit 如下：
* Complete unit tests suit for MongoDB transport
* Optional TTL support for MongoDB transport. AMQP TTL headers: x-messa… 
* Rearrange methods at MongoDB channel class
* Another MongoDB transport clean up and refactor. Use of transport opt… 
* Opt-out for queue size calculation
* Use natural sort for more FIFO semantic
* Fix docstrings

其中 `Optional TTL support for MongoDB transport. ` 是最关键的改动，忽略 TTL 的改动，主要看建立 MongoDB 连接的改动。在 `Channel` Class 中新增了一些类变量用于标识当前配置，在 `_parse_uri` 中，将 SSL,connectTImeoutMS 从 `client` 替换为了 `self` ，并删除了 `options.update(client.transport_options)` 。其中删除了 `options.update(client.transport_options)` 是导致这个问题的关键。

```diff
 class Channel(virtual.Channel):
     _client = None
     supports_fanout = True
+
+    # Mutable containers. Shared by all class instances
     _fanout_queues = {}

+    # Options
+    connect_timeout = None
+    ssl = False
+    capped_queue_size = 100000
+    ttl = False
+
+    from_transport_options = (
+        virtual.Channel.from_transport_options
+        + ('connect_timeout', 'ssl', 'ttl', 'capped_queue_size'))
+
+
     def __init__(self, *vargs, **kwargs):
         super(Channel, self).__init__(*vargs, **kwargs)
         ...

         ...

    def _parse_uri(self, scheme='mongodb://'):
        ...
         options = {
             'auto_start_request': True,
-            'ssl': client.ssl,
-            'connectTimeoutMS': (int(client.connect_timeout * 1000)
-                                 if client.connect_timeout else None),
+            'ssl': self.ssl,
+            'connectTimeoutMS': (int(self.connect_timeout * 1000)
+                                 if self.connect_timeout else None),
         }
-        options.update(client.transport_options)
         options.update(parsed['options'])
```

## 总结

Celery Kombu 代码管理感觉有些不清晰，在多个分支上想要对比非常困难。必要组件升级大版本进行全集测试是必要的。
