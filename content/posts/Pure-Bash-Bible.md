---
title: Pure Bash Bible
date: 2018-08-11 11:06:55
tags:
- Bash
---


## 背景
逛 Github Trending 的时候，发现一个叫 [pure bash bible](https://github.com/dylanaraps/pure-bash-bible) 的项目，这个项目主要是介绍一些常用功能的 Bash 实现。
在日常使用中，Bash 作为大部分 Linux 发行版的默认 Shell 是使用最多的，尤其是进行一些简单的自动处理事件上很方便。但是我使用的时候通常会用 Bash、Sed、Awk、cut、timeout 等一些 Linux 命令相互配合使用。
如果你要维护的 Server 是一个比较少见的版本，比如：ESXi 5.0、XenServer 6.0 等版本，那么就会导致有些命令是缺失的，且无法安装，这时候就需要单独使用 Bash 来实现一些其他命令的功能。
`pure bash bible` 这个项目列举了很多常用常用功能，有一些比较有借鉴意义，在此记录。

## 字符串

### 删除字符串前后空格

```Bash
trim_string（）{ # Ups：trim_string“example string” 
    ： “ $ {1 ＃” $ {1 %% [！[：space：]] * } “ } ”
    ： “ $ {_ ％” $ {_ ## * [！[：space：]]} “ } ”
     printf  '％s \ n '  “ $ _ ” }
$ trim_string “ Hello，World ” 
Hello, World
$ name = “ John Black ” $ trim_string “ $ name ” John Black
```

### 删除字符串中所有空格
```Bash
# shellcheck disable=SC2086,SC2048
trim_all() {
    # Usage: trim_all "   example   string    "
    set -f
    set -- $*
    printf '%s\n' "$*"
    set +f
}
$ trim_all "    Hello,    World    "
Hello, World

$ name="   John   Black  is     my    name.    "
$ trim_all "$name"
John Black is my name.
```

### 根据指定分隔符分隔字符串

```source-shell
split() {
   # Usage: split "string" "delimiter"
   IFS=$'\n' read -d "" -ra arr <<< "${1//$2/$'\n'}"
   printf '%s\n' "${arr[@]}"
}
$ split "apples,oranges,pears,grapes" ","
apples
oranges
pears
grapes

$ split "1, 2, 3, 4, 5" ", "
1
2
3
4
5

# Multi char delimiters work too!
$ split "hello---world---my---name---is---john" "---"
hello
world
my
name
is
john
```

## 数组

### 反转

```Bash
reverse_array() {
    # Usage: reverse_array "array"
    shopt -s extdebug
    f()(printf '%s\n' "${BASH_ARGV[@]}"); f "$@"
    shopt -u extdebug
}
$ reverse_array 1 2 3 4 5
5
4
3
2
1

$ arr=(red blue green)
$ reverse_array "${arr[@]}"
green
blue
red
```

### 删除重复项
```Bash
remove_array_dups() {
    # Usage: remove_array_dups "array"
    declare -A tmp_array

    for i in "$@"; do
        [[ "$i" ]] && IFS=" " tmp_array["${i:- }"]=1
    done

    printf '%s\n' "${!tmp_array[@]}"
}
$ remove_array_dups 1 1 2 2 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5
1
2
3
4
5

$ arr=(red red green blue blue)
$ remove_array_dups "${arr[@]}"
red
green
blue
```

### 随机选择

```Bash
random_array_element() {
    # Usage: random_array_element "array"
    local arr=("$@")
    printf '%s\n' "${arr[RANDOM % $#]}"
}
$ array=(red green blue yellow brown)
$ random_array_element "${array[@]}"
yellow

# Multiple arguments can also be passed.
$ random_array_element 1 2 3 4 5 6 7
3
```

## 文件
### 获取文件绝对路径

```Bash
dirname() {
    # Usage: dirname "path"
    printf '%s\n' "${1%/*}/"
}
$ dirname ~/Pictures/Wallpapers/1.jpg
/home/black/Pictures/Wallpapers/

$ dirname ~/Pictures/Downloads/
/home/black/Pictures/
```

### 获取文件相对路径

```Bash
basename() {
    # Usage: basename "path"
    : "${1%/}"
    printf '%s\n' "${_##*/}"
}
$ basename ~/Pictures/Wallpapers/1.jpg
1.jpg

$ basename ~/Pictures/Downloads/
Downloads
```

## 进度条
### 打印进度条

```Bash
bar() {
    # Usage: bar 1 10
    #            ^----- Elapsed Percentage (0-100).
    #               ^-- Total length in chars.
    ((elapsed=$1*$2/100))

    # Create the bar with spaces.
    printf -v prog  "%${elapsed}s"
    printf -v total "%$(($2-elapsed))s"

    printf '%s\r' "[${prog// /-}${total}]"
}

for ((i=0;i<=100;i++)); do
    # Pure bash micro sleeps (for the example).
    (:;:) && (:;:) && (:;:) && (:;:) && (:;:)

    # Print the bar.
    bar "$i" "10"
done

printf '\n'
```

## 总结
感觉平时很难用到这么诡异的 Bash 语法的。。。。
