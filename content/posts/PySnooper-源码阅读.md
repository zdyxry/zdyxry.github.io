---
title: PySnooper 源码阅读
date: 2019-04-27 20:14:28
tags:
- Python
---


## 背景

在 18 年的时候 jiajun 同学发过一篇[博客](https://jiajunhuang.com/articles/2018_05_08-how_to_debug.md.html)，讲如何调试相关的总结。结合最近自己的经验，紧靠 logging 和 print 就能解决日常的 80%问题，剩下的 20% 也都可以通过review 代码来解决，我只有当确实没什么思路的时候，才会采用 pdb 的方式去调试。之所以先 review 代码再采用 pdb 的方式是想确认自己已经理清了相关代码的上下文和逻辑，不至于在单步调试的时候出现 `恍然大悟` （贬义） 的状况。

最近两天 Github 上关于 Python 的项目最火的就是 PySnooper，这个项目的 Slogan 就是 `Never use print for debugging again` ，这里的 print 替换为 logging 也没啥差。整个代码在初步可用阶段代码量很少，也确实能够给平时写些小脚本带来便利，便抽时间看了看具体的实现。


## PySnooper

先来看下目录结构：

```bash
yiran@zhouyirandeMacBook-Pro:~/Documents/git-repo/PySnooper
3d0d051 ✗ $ tree .
.
├── LICENSE
├── MANIFEST.in
├── README.md
├── make_release.sh
├── misc
│   └── IDE\ files
│       └── PySnooper.wpr
├── pysnooper
│   ├── __init__.py
│   ├── pycompat.py
│   ├── pysnooper.py
│   ├── tracer.py
│   └── utils.py
├── requirements.in
├── requirements.txt
├── setup.py
├── test_requirements.txt
└── tests
    ├── __init__.py
    ├── test_pysnooper.py
    └── utils.py
```

可以看到最核心部分都在 pysnooper 部分，我们以官方示例来了解具体是如何工作的:

```python
root@yiran30250:~/backup/PySnooper
master ✗ $ cat a.py
import pysnooper

@pysnooper.snoop('/var/log/test.log')
def number_to_bits(number):
    print('func starting...')
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]

print(number_to_bits(6))
```

从示例中可以看到， `pysnooper.snoop` 作为一个装饰器，装饰所需要调试的函数，并可以再装饰器参数中添加对应的输出目的，比如标准输出，或者指定日志等。

我们看下 `snoop` 的实现：

```python
def snoop(output=None, variables=(), depth=1, prefix='', overwrite=False):
    write, truncate = get_write_and_truncate_functions(output) # 通过输出目标获取 write 函数
    if truncate is None and overwrite:
        raise Exception("`overwrite=True` can only be used when writing "
                        "content to file.")
    def decorate(function):
        target_code_object = function.__code__ # 函数在 python 解释器编译后的字节码对象
        tracer = Tracer(target_code_object=target_code_object, write=write,
                        truncate=truncate, variables=variables, depth=depth,
                        prefix=prefix, overwrite=overwrite)
        # 实例化 Tracer，将现有参数全部传递
        def inner(function_, *args, **kwargs):
            with tracer: # 通过 with 关键字调用 tracer，那么 Tracer 内应该实现了上下文管理器的 `__enter__` 和 `__exit__` 方法
                return function(*args, **kwargs) #
        return decorator.decorate(function, inner)

    return decorate
```

主要功能应该在 Trancer 中实现的，我们看下 Trancer 中做了什么？

```python
    def __enter__(self):
        self.original_trace_function = sys.gettrace()
        sys.settrace(self.trace)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        sys.settrace(self.original_trace_function)
```

先忽略其他的，我们先看实现上下文管理器的方法:
* 进入上下文环境
    * 获取当前跟踪器并记录
    * 设置追踪器为 `self.trace`
* 退出上下文环境
    * 将追踪器设置为原有值

注意：

`sys.settrace` 官方文档中描述它只用来做调试类工具，不建议在内部实现复杂逻辑。
The gettrace() function is intended only for implementing debuggers, profilers, coverage tools and the like.

其中追踪器要接受 3 个参数，分别是：frame，event 和 arg。我们先记住 frame就是当前的栈帧就好。


看一下 `self.trace` 具体是如何工作的，先看第一部分：

```python
    def trace(self, frame, event, arg):
        # 这里的注释写的很清楚了，根据当前 frame 是否为指定的函数字节码对象，如果不是且深度为 1，则直接返回 trace，如果指定了追踪深度，则不断循环，直到追踪到指定函数字节码对象
        if frame.f_code is not self.target_code_object:
            if self.depth == 1:
                return self.trace
            else:
                _frame_candidate = frame
                for i in range(1, self.depth):
                    _frame_candidate = _frame_candidate.f_back # f_back 为当前栈帧的上一个栈帧，便于在当前代码执行完成后可以调回之前代码继续执行
                    if _frame_candidate is None:
                        return self.trace
                    elif _frame_candidate.f_code is self.target_code_object:
                        indent = ' ' * 4 * i
                        break
                else:
                    return self.trace
        else:
            indent = ''
```

找到了具体的执行对象，我们看下如何获取环境变量的：

```python
    def trace(self, frame, event, arg):
        ...
        self.frame_to_old_local_reprs[frame] = old_local_reprs = \
                                               self.frame_to_local_reprs[frame] # 标记当前变量为现有变量
        self.frame_to_local_reprs[frame] = local_reprs = \
                               get_local_reprs(frame, variables=self.variables) # 获取当前变量

        modified_local_reprs = {}
        newish_local_reprs = {}

        for key, value in local_reprs.items(): # 遍历当前本地变量，将其分别放置为新变量和修改变量列表中
            if key not in old_local_reprs:
                newish_local_reprs[key] = value
            elif old_local_reprs[key] != value:
                modified_local_reprs[key] = value
        # 将变量通过 write 函数输出到对应的目标中
        newish_string = ('Starting var:.. ' if event == 'call' else
                                                            'New var:....... ')
        for name, value_repr in sorted(newish_local_reprs.items()):
            self.write('{indent}{newish_string}{name} = {value_repr}'.format(
                                                                   **locals()))
        for name, value_repr in sorted(modified_local_reprs.items()):
            self.write('{indent}Modified var:.. {name} = {value_repr}'.format(
                                                                   **locals()))
```

在上面可以看到大部分都是判断逻辑，看一下 `get_local_reprs` 中是如何获取当前变量的：

```python
def get_local_reprs(frame, variables=()):
    result = {key: get_shortish_repr(value) for key, value
                                                     in frame.f_locals.items()}
    for variable in variables:
        try:
            result[variable] = get_shortish_repr(
                eval(variable, frame.f_globals, frame.f_locals)
            )
        except Exception:
            pass
    return result
```

是通过调用 `frame.f_locals.items()` 获取当前栈帧所具有的本地变量。
剩下的部分是对于调试函数为装饰器时，需要特殊处理：跳过装饰器函数，直到找到函数定义部分。

## 总结

主题功能就通过上述代码来实现，简单高效，我们再来回顾一下：
1. 通过 settrace 来设置追踪器
    a. settrace 的行为是先执行追踪器部分，执行完成后执行函数字节码对应行
2. 在追踪器中，通过 frame 相关属性来获取所需值，如 f_locals, f_code, f_globals
3. 打印相关信息到目标中，退出上下文管理器，重新设置外层追踪器


