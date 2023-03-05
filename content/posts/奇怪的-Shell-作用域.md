---
title: 奇怪的 Shell 作用域
date: 2018-06-08 21:51:55
tags:
- Shell
- Bash
---


工作中很多脚本都是用 Shell 和 Python 完成的，在上周环境中遇到了一个 Bug，导致部分功能失败，最后发现是 Shell 作用域的问题。

## 举例

```shell
 $ tree .
.
├── test.sh
└── utils.sh

0 directories, 2 files
```

***

```shell
$ cat utils.sh
#!/usr/bin/env bash

function echo_test {
    for i in `seq 2 3`;do
        echo "utils.sh" $i
    done
}
```

***
```shell
$ cat test.sh
#!#/usr/bin/env bash

. utils.sh

for i in `seq 1 5`;do
    echo "before utils.sh" $i
    echo_test
    echo "after utils.sh" $i
    echo "#################"
done
```

***

```shell
$ bash test.sh
before utils.sh 1
utils.sh 2
utils.sh 3
after utils.sh 3
#################
before utils.sh 2
utils.sh 2
utils.sh 3
after utils.sh 3
#################
before utils.sh 3
utils.sh 2
utils.sh 3
after utils.sh 3
#################
before utils.sh 4
utils.sh 2
utils.sh 3
after utils.sh 3
#################
before utils.sh 5
utils.sh 2
utils.sh 3
after utils.sh 3
#################
```

***
## 解决方式
在 utils.sh 的函数中对所用变量加上 local 用来声明其作用域局限于函数内。
```shell
$ cat utils.sh
#!/usr/bin/env bash

function echo_test {
    local i
    for i in `seq 2 3`;do
        echo "utils.sh" $i
    done
}
```

***
```shell
$ bash test.sh
before utils.sh 1
utils.sh 2
utils.sh 3
after utils.sh 1
#################
before utils.sh 2
utils.sh 2
utils.sh 3
after utils.sh 2
#################
before utils.sh 3
utils.sh 2
utils.sh 3
after utils.sh 3
#################
before utils.sh 4
utils.sh 2
utils.sh 3
after utils.sh 4
#################
before utils.sh 5
utils.sh 2
utils.sh 3
after utils.sh 5
#################
```
