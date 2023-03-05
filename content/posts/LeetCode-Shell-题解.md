---
title: LeetCode Shell 题解
date: 2019-05-11 20:17:57
tags:
- alogrithms
---

工作上用 Shell 的频率是很高的，哪怕现在有了 Ansible 或者其他配置工具，Shell 仍是一个以 Linux 作为工作环境的同学的必备技能。
之前写过 GitHub 上的 `Pure Bash Bible`  的博客，看到 LeetCode 上的 Shell 题目好久不更新了，只有 4 道，今天记录一下题解。

## 192. Word Frequency

统计文本文件中单词出现次数，倒序输出。

words.txt
```
the day is sunny the the
the sunny is is
```

利用 `tr` `sort` `uniq` `awk` 解决。

```shell
# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{ print $2, $1 }'
```

# 193. Valid Phone Numbers

校验电话号码正确性。

file.txt
```
987-123-4567
123 456 7890
(123) 456-7890
```

主要是利用 `grep` 匹配正则，注意转义符。

```shell
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
```

# 194. Transpose File

行和列转换。

file.txt
```
name age
alice 21
ryan 30
```

```shell
# Read from the file file.txt and print its transposed content to stdout.
ncol=`head -n1 file.txt | wc -w`

for i in `seq 1 $ncol`
do
    echo `cut -d' ' -f$i file.txt`
done
```

# 195. Tenth Line

显示文件第 10 行。

file.txt
```
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
```

如果直接使用 `head` `tail` 的话不能方便处理文件为空的情况。

```shell
# Read from the file file.txt and output the tenth line to stdout.
sed -n '10p' file.txt
```


## 总结

其实编写 Shell 在熟知 Linux  内置命令就可以处理大部分场景了，如果处理不来，只能求助于 sed 和 awk, 但我脑子可能不太好使，awk 的语法总是记不住，每次写之前都要查一下语法。 - -

如果不想在代码中充斥着各种转义处理的话，还是老老实实使用 Python 编写脚本吧。


