---
title: Python logging 最佳实践-译
date: 2018-07-22 09:50:47
tags:
- Python
- logging
---

Python Logging 最佳实践

## 背景

最近在工作中要新增一个服务，需要处理服务日志，之前每次使用 logging 都是很简单的配置，没有
了解过最佳实践， google 到了 fangpenlin 写的一篇博客（https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/），
很受用，因此翻译过来便于自己以后回顾使用，也希望大家能够正确配置日志，对运维同学友好些~

## Good Logging practice in Python

在显示中，日志是重要的。当你在转账时，它们是转账记录。当飞机起飞时，黑匣子会记录所有事情。
如果某些事情发生了错误，人们可以通过阅读日志有机会弄清楚发生了什么。同样，在系统开发、排查
和运行中日志也是重要的。当你编写了一个服务，日志就是必须品。如果没有日志，我几乎不可能发现
错误如果服务已经挂掉。不仅仅是服务，日志对于桌面应用也是重要的。举个例子，当你的程序在你
客户电脑崩溃了，你可以让他们发送日志文件给你，你才有可能去查找为什么崩溃。相信我，你永远
不知道在不同的电脑环境中会发生什么奇怪的问题.


## Print 不是个好主意

尽管日志很重要，但是不是所有的开发者都知道如何正确的使用。我见过一些开发者在开发过程中插入
一些 print ，在开发结束时删除这些 print。向下面这样：

```Python
print 'Start reading database'
records = model.read_recrods()
print '# records', records
print 'Updating record ...'
model.update_records(records)
print 'done'
```

当程序是一个简单的脚本时这是工作的，但是对于一个复杂的系统，你最好不要通过这种途径记录日志。
第一，你在日志中无法记录重要的信息，你可能看到很多垃圾信息在日志中，但是没有找到任何有用的。
你也不能通过不修改代码的方式控制日志的输出，还有可能在不使用这些 print 的时候忘记删除掉。
所有的 print 信息都将输出到标准输出中，这个是要禁止的。当然你可以输出到标准错误输出中，但是
这仍不是记录日志的最佳实践。


## 使用 Python 标准库 Logging

所以，如何正确的记录日志？ 很简单，使用标准库中的 logging 模块。感谢 Python 社区，logging
在标准库中，它被设计的灵活且易用。你可以使用 logging 像下面这样：

```Python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Start reading database')
# read database here
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here
logger.info('Finish updating records')
```

你可以运行得到下面输出：

```Python
INFO:__main__:Start reading database
INFO:__main__:Updating records ...
INFO:__main__:Finish updating records
```

你可能会问这与 print 有什么区别。这样做当然是有好处的：

* 你可以控制信息级别，过滤掉不重要的信息
* 你可以决定之后输出的位置和方式

有不同的日志级别你可以使用：debug，info，warning，error 和 critical。
通过设置不同的日志级别，你可以只输出错误信息到指定的日志文件中，或者在 debug 
时输出调试的详细信息。尝试改变日志级别为 debug 再观察下输出结果：

`logging.basicConfig(level=logging.DEBUG)`

输出结果：

```Python
INFO:__main__:Start reading database
DEBUG:__main__:Records: {'john': 55, 'tom': 66}
INFO:__main__:Updating records ...
INFO:__main__:Finish updating records
```

像你所看到的那样，我们调整日志级别为 DEBUG，调试记录输出在日志中。你也可以决定
如何处理这些信息.举个例子你可以使用 FileHandler 让日志输出到一个文件中：

```Python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.info('Hello baby')
```

有很多种不同的处理方式，你可以发送日志到你的消息中心，甚至是一个远端的服务器。
你也可以自定义日志处理方式，更多信息可以参考： Basic Tutorial, Advanced Tutorial and Logging Cookbook.

## 设置正确的日志级别

由于 logging 的灵活性，你可以在任何地方配置适当的日志级别去记录日志，可以再之后配置他们。
你可能会问，什么是正确的日志级别，这里我将分享我的经验。

在大多数场景下，在日志中不希望去看到大量的详细信息。因此，debug 级别只是在你
调试过程中开启。我只使用调试级别来获取详细的调试信息，特别是当数据量很大或者频率
很高的时候，比如在一个 for 循环中记录某些内部的状态变化。

```Python
def complex_algorithm(items):
    for i, item in enumerate(items):
        # do some complex algorithm computation
        logger.debug('%s iteration, item=%s', i, item)
```

对于一般日志我使用 info 级别，比如，处理请求或者服务状态变化：

```Python
def handle_request(request):
    logger.info('Handling request %s', request)
    # handle request here
    result = 'result'
    logger.info('Return result: %s', result)

def start_service():
    logger.info('Starting service at port %s ...', port)
    service.start()
    logger.info('Service is started')
```

当一个状态比较重要，但是又没有处于 error 状态时，我会使用 warning ，比如
当一个用户登录时使用了错误的密码或者连接很慢时：

```Python
def authenticate(user_name, password, ip_address):
    if user_name != USER_NAME and password != PASSWORD:
        logger.warn('Login attempt to %s from IP %s', user_name, ip_address)
        return False
    # do authentication here
```

当某些事情出现了错误，我使用 error 级别，比如抛出异常，I/O 操作失败或者连接失败：

```Python
def get_user_by_id(user_id):
    user = db.read_user(user_id)
    if user is None:
        logger.error('Cannot find user with user_id=%s', user_id)
        return user
    return user
```

我很少使用严重级别，你可以在某些事情真的发生时，你可以使用它。比如内存泄露,
磁盘空间不足.

## 使用 __name__ 作为 logger 名称

你不需要讲 logger 名称设置为 __name__ ，但是如果这样做，会带来一些好处。
__name__ 变量在 Python 中是当前模块名称。举个例子，你可以调用 
logger.getLogger(__name__) 在模块 "foo.bar.my_module"中，这相当于
logger.getLogger(foo.bar.my_module)。当你需要配置 logger，你可以配置为 "foo"，
这样所有在 foo 包中的模块都共享同样的配置。你可以在阅读日志的时候了解模块信息。

## 捕获异常并使用 traceback 记录

记录哪些地方出错总是一个好的做法，但是如果没有 traceback 这用处很小。你应该捕获
异常并与 traceback 一起记录他们。像这个例子：

```Python
try:
    open('/path/to/does/not/exist', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception, e:
    logger.error('Failed to open file', exc_info=True)
```

通过 exc_info=True 参数调用 logger 方法，traceback 会被记录到日志中，你可以
看到这样的结果：

```Python
ERROR:__main__:Failed to open file
Traceback (most recent call last):
  File "example.py", line 6, in <module>
    open('/path/to/does/not/exist', 'rb')
IOError: [Errno 2] No such file or directory: '/path/to/does/not/exist'
```

你也可以调用 logger.Exception(msg, *args)，这相当于 logger.error(msg,exc_info=True,*args)。

## 除非 disable_existing_loggers == False，否则不要在模块级别获取 logger

你可以看到很多的例子（包括这篇文章）在模块级别获取 logger。这看上去是无害的，
但是实际上，这是一个陷阱 - 在你从一个文件加载配置前，logging 模块会遵守所有
已经创建的 logger，如果你在模块级别获取 logger，像这种：

---
my_module.py
```Python
import logging

logger = logging.getLogger(__name__)

def foo():
    logger.info('Hi, foo')

class Bar(object):
    def bar(self):
        logger.info('Hi, bar')
```

---

main.py

```Python
import logging

# load my module
import my_module

# load the logging configuration
logging.config.fileConfig('logging.ini')

my_module.foo()
bar = my_module.Bar()
bar.bar()
```

--- 
logging.ini

```bash
[loggers]
keys=root

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=
```

---

你期望看到记录显示在日志中，但是日志中是空的。为什么？ 因为你在模块级别创建 logger ，
所以在从文件加载 logging 配置之前导入该模块。 logging.fileConfig 和 logging.dictConfig 
默认禁用已经存在的 logger。 所以配置文件中的配置不会在你的 logger 中生效。
这适合在你需要的时候获取 logger。 你可以像下面这样编写：

```Python
import logging

def foo():
    logger = logging.getLogger(__name__)
    logger.info('Hi, foo')

class Bar(object):
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def bar(self):
        self.logger.info('Hi, bar')
```

通过这样做， logger 将会在你加载配置之后创建，配置会正确生效。

从 Python 2.7 开始，添加一个新的参数名为 "disable_existing_loggers" 到 fileConfig 和 
dictConfig，通过将其设置为 False，可以解决上面提到的问题。比如：

```Python
import logging
import logging.config

logger = logging.getLogger(__name__)

# load config from file
# logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
# or, for dictConfig
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,  # this fixes the problem
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        }
    }
})

logger.info('It works!')
```

## 使用 JSON 和 YAML 配置 logging

你可以再 Python 代码中配置 logging 参数，但是这不够灵活。更好的方式
是使用 logging 配置文件。在 Python2.7 之后，你可以加载 logging 配置
从一个字典，这意味着你可以从 JSON 或 YAML 文件中加载 logging 配置。 
虽然你可以通过 old.ini 方式加载 logging 配置，但是这对于可读性和可编辑
来说是困难的。这里我将展示通过 JSON 或者 YAML 的配置文件示例。

---

logging.json 

```json
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },

        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "info.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },

        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "simple",
            "filename": "errors.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }
    },

    "loggers": {
        "my_module": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": "no"
        }
    },

    "root": {
        "level": "INFO",
        "handlers": ["console", "info_file_handler", "error_file_handler"]
    }
}
```

---

logging.yaml 

```yaml
---
version: 1
disable_existing_loggers: False
formatters:
    simple:
        format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

handlers:
    console:
        class: logging.StreamHandler
        level: DEBUG
        formatter: simple
        stream: ext://sys.stdout

    info_file_handler:
        class: logging.handlers.RotatingFileHandler
        level: INFO
        formatter: simple
        filename: info.log
        maxBytes: 10485760 # 10MB
        backupCount: 20
        encoding: utf8

    error_file_handler:
        class: logging.handlers.RotatingFileHandler
        level: ERROR
        formatter: simple
        filename: errors.log
        maxBytes: 10485760 # 10MB
        backupCount: 20
        encoding: utf8

loggers:
    my_module:
        level: ERROR
        handlers: [console]
        propagate: no

root:
    level: INFO
    handlers: [console, info_file_handler, error_file_handler]
...
```

以下配置展示了如何从 json 文件中读取 logging 配置：

```Python
import os
import json
import logging.config

def setup_logging(
    default_path='logging.json',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
```

使用 JSON 配置的一个优点是 json 是标准库中的模块，你不需要安装。但就个人来说，
我更喜欢 YAML。这有非常好的可读性和可编辑性。你可以按照以下方式加载 YAML 配置：

```yaml
import os
import logging.config

import yaml

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
```

现在，要配置 logging，你可以在程序启动时调用 setup_logging。这将读取 logging.json 或者
logging.yaml。你也可以设置 LOG_CFG 环境变量去从指定的路径下加载配置文件。比如：

`LOG_CFG=my_logging.json python my_server.py`

或者

`LOG_CFG=my_logging.yaml python my_server.py`

## 配置文件轮询

如果你使用 FileHandler 去写日志，随着时间的增加日志文件大小也会增长，某一天，会撑爆你的磁盘。
为了避免这种情况，你应该在生产环境中使用 RotatingFileHandler 替换 FileHandler 。


## 配置日志中心

当你有多台服务器和不同的日志文件时，你可以配置一个日志中心去手机所有重要的文件。这样你可以
更方便的监控和通知你的系统发生了哪些报错。

## 结论

我很开心 Python logging 库设置的很好，最好的是它是标准库中的一员，你无须选择。
它非常灵活，你可以编辑自己的处理器和过滤器。还有第三方程序比如 pyzmq 提供的 ZeroMQ 日志处理，
它允许你通过 zmq socket 发送日志信息。
如果你不知道如何正确的使用 logging，那么本文对你会有所帮助。通过良好的日志记录练习，
你可以更轻松的找到系统中的问题。
