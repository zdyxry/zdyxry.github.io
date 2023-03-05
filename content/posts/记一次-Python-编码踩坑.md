---
title: 记一次 Python 编码踩坑
date: 2019-04-02 07:37:59
tags:
- Python
---

## 背景

一直知道 Python 容易踩编码的坑，尤其是 Python2，昨天第一次遇到，记一下。

## 起因

产品中有一个账号关联的功能，需要的参数大概有 host,port,user,passwd 这么几个参数，昨天发现一个环境中账号关联失败，看请求应该还没到账号认证那里就失败了，查看 rest-server 日志，并没有发现错误异常，api 也是正常返回的，通过其他方式验证账号是有效的，当时觉得很奇怪，没什么想法。

## 调查

既然 rest-server 中日志没有报错，那么看看服务是否有什么异常。
这里特意说名下，如果服务使用的是 gunicorn 或者 celery 等第三方库作为守护进程，有一些系统报错是不会记录到你的服务中的，而是会直接打印到系统中（messages or systemd）。

发现 `systemctl status` 和 `journal -u ` 有报错，报错内容如下：

```bash
4月 02 06:20:00 SCVM70 gunicorn[31225]: Traceback (most recent call last):
4月 02 06:20:00 SCVM70 gunicorn[31225]: File "/usr/lib64/python2.7/site-packages/gevent/threadpool.py", line 207, in _worker
4月 02 06:20:00 SCVM70 gunicorn[31225]: value = func(*args, **kwargs)
4月 02 06:20:00 SCVM70 gunicorn[31225]: error: getaddrinfo() argument 2 must be integer or string
4月 02 06:20:00 SCVM70 gunicorn[31225]: (<ThreadPool at 0x120ae50 0/5/10>, <built-in function getaddrinfo>) failed with error
```

字面意思是传递参数的类型不对，必须为 int 或者 string。

在 Chrome 中查看当时 API 请求参数，所有参数均为 string，我也实际用 int 或者 str 类型进行验证，账号验证都是可以成功的，感觉进入了死胡同。

## 原因

最后发现是编码的问题，传递的 port 参数是 unicode 编码，而 `getaddrinfo()` 需要的是 int 或者 string。

在 python2中，str 其实是 bytes，而不是 unicode，在代码中声明了编码方式为 `utf-8`，并将该参数存入到了 DB 中，导致下次请求传递的还是 DB 中的 `utf-8` 类型的 port，而不是 int 或者 string。

## 解决

这里解决的方式很简单，直接将 port 强制转换为 int 或者 string 就好。根本解决方式应该是在之后的代码编写过程中，规范变量类型，比如 port 就使用 int，而不是 str（unicode），防止出现未知错误。

