---
title: 将 Json 转换为 Python Object(一)
date: 2018-06-09 11:43:49
tags:
- Python
---

```python
$ cat example.py 
import json


class JSONObject:

    def __init__(self, dict):
        vars(self).update(dict)


# this is valid json string
data = '{"channel":{"lastBuild":"2013-11-12", "component":["test1", "test2"]}}'

jsonobject = json.loads(data, object_hook=JSONObject)

print(jsonobject.channel.component[0])
print(jsonobject.channel.lastBuild)
```
***

```shell
$ python example.py
test1
2013-11-12
```

