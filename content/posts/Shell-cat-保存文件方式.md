---
title: Shell cat 保存文件方式
date: 2019-01-05 20:12:30
tags:
- Shell
---


## 背景

在 Shell 中保存文件可以通过 echo 保存一个字符串， cat 保存一个字符片段，最近在用 cat 编写 Nginx 配置文件的时候，想要写入 `$test` 类似字段，但是 Shell 会自动将其识别为变量而忽略，记录下该方式。


## cat 编写文件

```bash
root@yiran-30-250:/tmp
 $ cat cat.sh
#!/usr/bin/env bash

cat << EOF > /tmp/yiran
aaa
bbb
ccc
ddd
$eee
$fff

EOF
root@yiran-30-250:/tmp
 $ bash cat.sh
root@yiran-30-250:/tmp
 $ cat yiran
aaa
bbb
ccc
ddd


```


```bash
root@yiran-30-250:/tmp
 $ cat cat2.sh
#!/usr/bin/env bash

cat << 'EOF' > /tmp/yiran
aaa
bbb
ccc
ddd
$eee
$fff

EOF
root@yiran-30-250:/tmp
 $ bash cat2.sh
root@yiran-30-250:/tmp
 $ cat yiran
aaa
bbb
ccc
ddd
$eee
$fff
```

