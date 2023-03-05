---
title: 将 Json 转换为 Python Object(二)
date: 2018-06-17 21:00:49
tags:
- Json
---

最近趁着端午假期，终于把 《流畅的 Python》看完了，收获很大，书中某一章节介绍了 addict 库，可以将 Json 转换为 Python Object 。
今天看了看具体的实现方式，比 Stack Overflow 的回答完整，补发一篇博客学习下。

源码代码很少，补充一些关键变量用于了解整体实现流程。

```
import copy
from pprint import pprint


class Dict(dict):

    def __init__(__self, *args, **kwargs):
        print 'init kwargs is ', kwargs
        object.__setattr__(__self, '__parent', kwargs.pop('__parent', None))
        object.__setattr__(__self, '__key', kwargs.pop('__key', None))
        for arg in args:
            if not arg:
                continue
            elif isinstance(arg, dict):
                for key, val in arg.items():
                    __self[key] = __self._hook(val)
            elif isinstance(arg, tuple) and (not isinstance(arg[0], tuple)):
                __self[arg[0]] = __self._hook(arg[1])
            else:
                for key, val in iter(arg):
                    __self[key] = __self._hook(val)

        for key, val in kwargs.items():
            __self[key] = __self._hook(val)

    def __setattr__(self, name, value):
        if hasattr(Dict, name):
            raise AttributeError("'Dict' object attribute "
                                 "'{0}' is read-only".format(name))
        else:
            self[name] = value

    def __setitem__(self, name, value):
        print 'setitem name is %s, value is %s ' % (name, value)
        super(Dict, self).__setitem__(name, value)
        try:
            p = object.__getattribute__(self, '__parent')
            key = object.__getattribute__(self, '__key')
        except AttributeError:
            p = None
            key = None
        if p is not None:
            print 'parent is %s' % p
            print 'key is %s' % key
            p[key] = self
            object.__delattr__(self, '__parent')
            object.__delattr__(self, '__key')

    def __add__(self, other):
        if not self.keys():
            return other
        else:
            self_type = type(self).__name__
            other_type = type(other).__name__
            msg = "unsupported operand type(s) for +: '{}' and '{}'"
            raise TypeError(msg.format(self_type, other_type))

    @classmethod
    def _hook(cls, item):
        if isinstance(item, dict):
            return cls(item)
        elif isinstance(item, (list, tuple)):
            return type(item)(cls._hook(elem) for elem in item)
        return item

    def __getattr__(self, item):
        return self.__getitem__(item)

    def __getitem__(self, name):
        print 'getitem name is ', name
        if name not in self:
            print "%s not in self" % name
            return Dict(__parent=self, __key=name)
        return super(Dict, self).__getitem__(name)

    def __delattr__(self, name):
        del self[name]

    def to_dict(self):
        base = {}
        for key, value in self.items():
            if isinstance(value, type(self)):
                base[key] = value.to_dict()
            elif isinstance(value, (list, tuple)):
                base[key] = type(value)(
                    item.to_dict() if isinstance(item, type(self)) else
                    item for item in value)
            else:
                base[key] = value
        return base

    def copy(self):
        return copy.copy(self)

    def deepcopy(self):
        return copy.deepcopy(self)

    def __deepcopy__(self, memo):
        other = self.__class__()
        memo[id(self)] = other
        for key, value in self.items():
            other[copy.deepcopy(key, memo)] = copy.deepcopy(value, memo)
        return other

    def update(self, *args, **kwargs):
        other = {}
        if args:
            if len(args) > 1:
                raise TypeError()
            other.update(args[0])
        other.update(kwargs)
        for k, v in other.items():
            if ((k not in self) or
                (not isinstance(self[k], dict)) or
                    (not isinstance(v, dict))):
                self[k] = v
            else:
                self[k].update(v)

    def __getnewargs__(self):
        return tuple(self.items())

    def __getstate__(self):
        return self

    def __setstate__(self, state):
        self.update(state)

    def setdefault(self, key, default=None):
        if key in self:
            return self[key]
        else:
            self[key] = default
            return default


json_data = {
    "a": "a"
}

test1 = Dict(json_data)
test1.b.c = "c"
test1.b.d.e = "e"
pprint(test1.to_dict())
```

---

```
 $ python a.py
init kwargs is  {}
setitem name is a, value is a 
getitem name is  b
b not in self
init kwargs is  {'__key': 'b', '__parent': {'a': 'a'}}
setitem name is c, value is c 
parent is {'a': 'a'}
key is b
setitem name is b, value is {'c': 'c'} 
getitem name is  b
getitem name is  d
d not in self
init kwargs is  {'__key': 'd', '__parent': {'c': 'c'}}
setitem name is e, value is e 
parent is {'c': 'c'}
key is d
setitem name is d, value is {'e': 'e'} 
{'a': 'a', 'b': {'c': 'c', 'd': {'e': 'e'}}}
```
