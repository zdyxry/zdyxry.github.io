---
title: 代码统计工具 cloc 基本使用
date: 2019-08-09 19:35:14
tags:
- tools
---

## 背景

在看一个新项目的时候，通常我都会了解下这个项目的代码量，然后心里给个预期，大概需要多久了解这个项目。

2023/01/11 更新：现在已切换至 loc/tokei ，速度快了许多。

## wc

在以前，我一般都是使用 `find` 配合 `wc` 来完成，比如：

```bash
root@yiran-workstation:/tmp/cloc 
 $ find . -name "*.go" | xargs wc -l {} 
  81 ./installer.go
  81 total

```

显示有一个 `installer.go` 的文件，一共有 81行。但是这里有个问题，就是 wc 是不会统计代码里面的具体内容的，比如注释、空白行等。

这时候我们就需要一个更高级的工具了： `cloc`

## cloc

[cloc](https://github.com/AlDanial/cloc) 是一个 Perl 语言实现的项目，用途就像它的名字全称：Count Lines of Code。

使用方法的话最简单的直接加上项目路径：

```bash
root@yiran-workstation:~/go/src/github.com/kubermatic/kubeone 
master ✗ $ pwd        
/root/go/src/github.com/kubermatic/kubeone
root@yiran-workstation:~/go/src/github.com/kubermatic/kubeone 
master ✗ $ cloc .                   
     292 text files.
     274 unique files.                                          
      78 files ignored.

github.com/AlDanial/cloc v 1.70  T=0.80 s (269.1 files/s, 32223.3 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Go                             122           2861           2791          14374
Markdown                        38           1003              0           3172
YAML                            41             14            158            524
Bourne Shell                     5             44             89            206
Python                           4             66             76            186
XML                              4              0              0            100
make                             1             17             13             52
-------------------------------------------------------------------------------
SUM:                           215           4005           3127          18614
-------------------------------------------------------------------------------
```

可以看到统计结果，其中默认会按照语言分类。

如果是 Golang 的项目，且使用了 vendor ，那么可以通过 `--exclude-dir` 来过滤掉某些路径：

```bash
aster ✗ $ cloc . 
    3304 text files.
    3170 unique files.                                          
     429 files ignored.

github.com/AlDanial/cloc v 1.70  T=12.40 s (232.7 files/s, 101850.0 lines/s)
--------------------------------------------------------------------------------
Language                      files          blank        comment           code
--------------------------------------------------------------------------------
Go                             2501         101422         113437        1007168
Markdown                        108           2688              0           6786
Protocol Buffers                 53           3006           9076           5133
YAML                            108            305            377           4032
Bourne Shell                     38            381            839           1897
JSON                              7              0              0           1748
Assembly                         35            271            320           1603
Python                            5            277            113            588
make                             23            165            162            556
Bourne Again Shell                3             45             56            378
XML                               4              0              0            106
C                                 1              8              7             24
--------------------------------------------------------------------------------
SUM:                           2886         108568         124387        1030019
--------------------------------------------------------------------------------
root@yiran-workstation:~/go/src/github.com/kubernetes-sigs/cluster-api-provider-vsphere 
master ✗ $ ls    
boilerplate.go.txt  cmd                 config           Dockerfile  go.mod  hack     Makefile  OWNERS_ALIASES  PROJECT    RELEASE.md  SECURITY_CONTACTS
build               code-of-conduct.md  CONTRIBUTING.md  docs        go.sum  LICENSE  OWNERS    pkg             README.md  scripts     vendor
root@yiran-workstation:~/go/src/github.com/kubernetes-sigs/cluster-api-provider-vsphere 
master ✗ $ cloc . --exclude-dir=vendor
     234 text files.
     234 unique files.                                          
      73 files ignored.

github.com/AlDanial/cloc v 1.70  T=0.55 s (294.2 files/s, 26466.9 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Go                              64           1110           1355           5106
YAML                            37            150            302           1907
Bourne Shell                    22            256            475           1125
Markdown                        17            332              0            895
Python                           5            277            113            588
make                             9             57            112            177
JSON                             4              0              0            131
XML                              4              0              0            106
-------------------------------------------------------------------------------
SUM:                           162           2182           2357          10035
-------------------------------------------------------------------------------
root@yiran-workstation:~/go/src/github.com/kubernetes-sigs/cluster-api-provider-vsphere 
master ✗ $ 
```


有时候仅仅按照语言分类还不够，我们想看到具体的那些文件代码量比较大，可以使用 `--by-file` 参数：


```bash
root@yiran-workstation:~/go/src/github.com/kubermatic/kubeone 
master ✗ $ cloc . --by-file |head -n 30
     292 text files.
     274 unique files.                                          
      78 files ignored.

github.com/AlDanial/cloc v 1.70  T=0.70 s (307.5 files/s, 36823.9 lines/s)
--------------------------------------------------------------------------------------------------------------------
File                                                                             blank        comment           code
--------------------------------------------------------------------------------------------------------------------
./pkg/templates/machinecontroller/deployment.go                                     52             24            762
./pkg/apis/kubeone/v1alpha1/zz_generated.conversion.go                              86             54            614
./pkg/apis/kubeone/validation/validation_test.go                                    22             12            530
./pkg/cmd/config.go                                                                 81             42            477
./pkg/apis/kubeadm/v1beta2/zz_generated.deepcopy.go                                 53             60            443
./pkg/apis/kubeadm/v1beta1/zz_generated.deepcopy.go                                 53             60            439
./pkg/templates/weave/weave-net.go                                                  32             13            433
./pkg/config/cluster.go                                                             80             69            417
./pkg/terraform/config.go                                                           76             30            368
./pkg/templates/canal/daemonset.go                                                   9             42            344
./pkg/yamled/document_test.go                                                      113             15            344
./pkg/apis/kubeone/v1alpha1/zz_generated.deepcopy.go                                47             53            340
./pkg/apis/kubeone/zz_generated.deepcopy.go                                         47             53            340
./pkg/templates/machinecontroller/webhook.go                                        35             22            332
./pkg/installer/installation/prerequisites.go                                       73             21            281
./pkg/templates/canal/prerequisites.go                                              16             40            257
./pkg/upgrader/upgrade/preflight_checks.go                                          44             30            247
./pkg/yamled/document.go                                                            70             31            240
./pkg/upgrader/upgrade/preflight_checks_test.go                                     14             12            237
./pkg/templates/metricsserver/deployment.go                                         22             13            227
./pkg/templates/externalccm/packet.go                                               20             12            222
./docs/quickstart-vsphere.md                                                        59              0            222

```
