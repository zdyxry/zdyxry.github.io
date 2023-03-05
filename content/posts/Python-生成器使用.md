---
title: Python 生成器使用
date: 2019-03-09 21:47:35
tags:
- Python
---


## 背景

在清理 Pocket 列表的时候，发现自己很早之前收藏过 dabeaz 在 2008 年 PyCon 关于生成器的 PPT 讲解，今天读完，有所收获。

在 PPT 中， dabeaz 通过一个具体的文件处理的例子，一步一步的讲解了程序的演进，具体代码可以在 [Github](https://github.com/dabeaz/generators) 查看。

## 生成器

使用 yield 关键字的函数就是生成器。生成器在运行时生成值，所以只能迭代一次。生成器可以通过 next 关键字执行，通常我们通过 for 循环来迭代生成器，可以自动处理 StopIteration 情况。

一个简单的生成器例子：
```python
def countdown(n):
   while n > 0:
       yield n
       n -= 1
>>> for i in countdown(5):
...     print(i, end=' ')
...
5 4 3 2 1
```

当我们调用生成器时，仅返回一个生成器对象，不会执行函数内容，只有当执行 `__next__()` 时函数才会真正执行。yield 会返回给调用者当前值，同时暂停执行，等待下一次调用 `__next__()` 继续执行。

## 协程

在 python 中通过生成器的方式来实现协程：

```python
In [7]: def recv_count():
   ...:     try:
   ...:         while True:
   ...:             n = yield
   ...:             print("T-minus", n)
   ...:     except GeneratorExit:
   ...:         print("boom")
   ...:
In [8]: r = recv_count()
In [9]: r.send(None) # init
In [10]: r.next() # yield 未接收到调用者发送具体值
('T-minus', None)
In [13]: r.send(1) 
('T-minus', 1)
In [14]: r.send(2)
('T-minus', 2)
In [15]: r.send(3)
('T-minus', 3)
```

关于为什么要执行 `r.send(None)` ，可以看 [PEP-342](https://www.python.org/dev/peps/pep-0342/) 中具体解释：
> Because generator-iterators begin execution at the top of the generator's function body, there is no yield expression to receive a value when the generator has just been created. Therefore, calling send() with a non-None argument is prohibited when the generator iterator has just started, and a TypeError is raised if this occurs (presumably due to a logic error of some kind). Thus, before you can communicate with a coroutine you must first call next() or send(None) to advance its execution to the first yield expression.


在此基础上进行扩展，我们写一个生产消费者模型:

```python
root@yiran-30-250:/tmp
 $ cat a.py
#!/usr/bin/python3

def consumer():
    r = ''
    while True:
        n = yield r
        print('Consuming %s ...' % n)
        r = '200 OK'
def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print("Producing %s ..." % n)
        r = c.send(n)
        print("Consumer return: %s" % r)
    c.close()
c = consumer()
producer(c)

root@yiran-30-250:/tmp
 $ python3 a.py
Producing 1 ...
Consuming 1 ...
Consumer return: 200 OK
Producing 2 ...
Consuming 2 ...
Consumer return: 200 OK
Producing 3 ...
Consuming 3 ...
Consumer return: 200 OK
Producing 4 ...
Consuming 4 ...
Consumer return: 200 OK
Producing 5 ...
Consuming 5 ...
Consumer return: 200 OK

```

在 Python3.3 之后，添加了 `yield from`, `asyncio` 等关键字，在之后的博客中单独记录。

## 参考链接

* http://www.dabeaz.com/generators/Generators.pdf
* https://www.tornadoweb.org/en/stable/guide/coroutines.html
* https://www.zhihu.com/question/28105502
