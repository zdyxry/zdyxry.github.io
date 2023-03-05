---
title: Hexo Git 管理
date: 2018-05-29 21:50:20
tags:
- git
---


**以A电脑的Hexo博客源文件迁移到B电脑为例：**

## **一、对A电脑的操作如下：**

1.在github新建仓库名为blog

2.上传A电脑本地Hexo博客的源文件夹至github的blog仓库，流程如下：

（1）删除根目录和主题目录下的.git文件夹

（2）修改根目录下的.gitignore文件为：

> /.deploy_git
>
> /public

（3）依次执行以下指令，同步源文件至github

```shell
$  git init
$  git add .
$  git commit -m "xxxxx"
$  git remote add origin git@github.com:/blog_bak.git
$  git push -u origin master
```

## 二、对B电脑的操作如下：

1.安装Git，并配置github账号下的B电脑的.ssh
2.安装Node.js
3.使用npm指令安装Hexo

> $  npm install -g hexo-cli
>
> $ npm install hexo-asset-image --save 用于创建保存图片的文件夹

4.使用Git bash随便选择一个文件夹,执行git clone

> $  git clone git@github.com:/blog.git


## 三、关于日常的改动流程（A，B两台电脑均使用的情况下）：
1.建议先检查更新git pull，将本地博客源文件更新至最新版本

`$  git pull`

2.然后可以新建或修改博客内容，进行预览等操作

```shell
$  hexo new "新的博客名称"

$  hexo server
```

3.新建博客后，先同步Hexo源文件，将修改后的源文件同步至github:

```shell
$  git add .

$  git commit -m "更新描述"

$  git push origin master
```

4.然后再执行Hexo的生成文件和部署指令

 ```shell
$  hexo generate

$  hexo deploy
 ```

