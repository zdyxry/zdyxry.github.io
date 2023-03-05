---
title: Ansible最佳实践
date: 2018-11-24 21:18:28
tags:
- Ansible
---

## 背景

说起来我真正负责过大批量服务器线上管理的时间，还是在16年负责运维的时候，那时候还都是通过 Shell 脚本来完成一些自动化的工作，当时觉得还不错，至少我觉得可定制化上还是很好的。  



目前负责公司产品中一部分功能目前是通过 Shell 来完成的，但是 Shell 脚本在使用中存在一些弊端，最近在用 Ansible 来重写这部分功能，在重写过程中感受负责，又爱又恨，也有一些疑惑，特此记录。

## Ansible

相信大家都或多或少听过 Ansible,Puppet,SaltStack 等等自动管理工具，它们的功能都很强大，但使用起来又不简单，Ansible 可以说是这里面上手最快的一个。

这里我不讲述 Ansible 具体的使用规则，大家看文档就好，我讲下我常用的几个场景：

### 批量查看、操作、拷贝  

无论是作为一名开发，还是测试、运维，应该都碰到过需要管理多台服务器的情况，比如我们想要查看一个集群中所有节点的负责情况，那么我们可以执行： 
```Bash
 $ ansible yiran-cluster -m raw -a 'uptime'
192.168.67.39 | SUCCESS | rc=0 >>
 20:23:24 up 3 days,  7:32,  4 users,  load average: 14.97, 13.81, 12.55
Shared connection to 192.168.67.39 closed.
192.168.67.40 | SUCCESS | rc=0 >>
 20:23:24 up 3 days,  7:32,  1 user,  load average: 11.79, 14.15, 14.81
Shared connection to 192.168.67.40 closed.
192.168.67.41 | SUCCESS | rc=0 >>
 20:23:24 up 6 days, 22:36,  1 user,  load average: 19.89, 20.10, 19.79
Shared connection to 192.168.67.41 closed.
```

如果我们想要拷贝自己的测试代码到所有的服务器上，我们可以执行：
```Bash
ansible yiran-cluster -m synchronize -a 'src=zbs_rest dest=/usr/lib/python2.7/site-packages/'
```

### 重复性操作

如果我们经常要查看某些集群（无监控）情况下的性能，我们可以编写一个 playbook，这个 playbook 专门用来收集集群的状态：
```Bash
 $ cat cluster_status.yml
#!/usr/bin/env ansible-playbook
---
- name: cluster status
  hosts: yiran-cluster
  max_fail_percentage: 0
  gather_facts: false
  tasks:
     - name: uptime
       raw: uptime
       register: out
     - debug: var=out.stdout_lines

     - name: check services status
       shell: /usr/share/tuna/script/control_all_services.sh --action=status --group=role
       register: out
       async: 300
       poll: 2
     - debug: var=out.stdout_lines

     - name: memory status
       raw: free -h
       register: out
     - debug: var=out.stdout_lines
```

## Shell Script vs Ansible

通过上述的简单示例，可以体会到 Ansible 的强大，但是 Ansible 真的有那么好么？

明明几行  Shell 就可以搞定的事情，为什么一定要使用 Ansible 来做呢？  
明明一个 Shell 脚本就可以完成的环境监察，为什么一定要使用 Ansible Playbook 来做呢？要知道 Playbook 编写语法虽然是 YAML，但是使用起来并不简单，有很多特殊的语法需要去注意，完全没有必要花费精力去学习一个新的工具去完成。

前两天看到 [卡瓦邦噶](https://www.kawabangga.com/) 介绍 Ansible的一篇博客中，提到了一篇 [Shell Script vs Ansible: Fight](https://hvops.com/articles/ansible-vs-shell-scripts/) 的文章（远古版真香），其中有一段总结，用来描述 Ansible 的优势，我加上了 Shell Script 的对比如下：   

 | Ansible | Shell Script | 优胜者 |
 | -------- | -------- | -------- | 
 | 可以进行源码管理 | Shell 也可以 | - | 
 | 幂等性 |  Shell 中需要额外做条件判断| Ansible | 
 | 同时在多台服务器运行 | Shell 可以通过 sshpass 编写脚本同时在多台运行| Ansible | 
 | 验证服务器正确性| Shell 需要编写脚本收集更多信息 | Ansible | 
 | 定位部分服务器组 | Shell 需要编写脚本对配置文件进行过滤筛选| Ansible | 
 | 支持模板 | - | Ansible | 
 | 技术栈支持| - | Ansible | 

 综合看上去，感觉 Ansible 太好了，上述情况下如果可以选择的话，我们都应该选择 Ansible 来做管理，事实上真的是这样么？ 

 我也以为是这样，直到我通过 Ansible 重写 Shell 脚本。

 ## 噩梦开始

 由于产品功能需要处理多平台的、多场景的情况，该功能的 Shell 脚本大概有 4800 行左右。
 ```Bash
 --------------------------------------------------------------------------------
Language                      files          blank        comment           code
--------------------------------------------------------------------------------
Bourne Shell                     57            990            154           4847
Python                            2             48              0            201
Bourne Again Shell                1              4              5             28
```

我们找一个简单的脚本来看下：
```Bash
master ✔ $ cat stage_mount_extent_disks.sh
#!/usr/bin/env bash

cur=`dirname $0`
. $cur/zbs_util.sh


if [[ "$#" -lt 1 ]]; then
    echo "Usage: $0 <disk1> <disk2>"
    exit 1
fi

disks=$*

echo "waiting service start ....."
for ((i = 0; i < 30; i++)); do
    if pidof service; then
        break
    else
        sleep 2
    fi
done
echo "service started"


# mount partition
for disk in ${disks[@]}; do
    echo "mount $disk"
    $cur/mount_extent_disk.sh "/dev/$disk"
done
```

这是一个很简单的脚本，首先我们判断了下输入参数，需要输入两块磁盘盘符，接下来等待服务启动后，我们调用另一个脚本进行磁盘的挂载，如果我们想要执行这个脚本，那么我们可以执行执行：
```Bash
./stage_mount_extent_disks.sh sda sdb
```
然后等待脚本执行结束就可以了，这里的 sda 和 sdb 是存在一个 json 文件中，我们使用 `jq` 命令可以很容易的获取到 json 文件中的执行磁盘。

那么我们在 Ansible Playbook 我们要怎么做？ 
1. 读取配置文件，并将读取结果设置为参数 `myvar`
2. 解析 `myvar` 获取 extent disks list，注意，这里的解析语法是 JMESPath 的语法
3. 将 extent disk list 转换为 extent disk string ，这里是因为如果调用 raw 模块，需要传递字符串
4. 如果平台是 xen7 的话，执行 xen7 的脚本
5. 如果平台不是 xen7，且是 halo 的话，执行 halo 脚本

具体 Playbook 如下：
```Bash
- name: mount extent disk
  gather_facts: false
  hosts: master:storage
  tasks:
      - shell: cat /path/config.json
        register: result
      - set_fact:
          myvar: "{{ result.stdout | from_json }}"

      - name: get all extent disk list
        set_fact:
          extent_disk_list: "{{ myvar | json_query('disks[?function==`extent`][].drive') | list }}"

      - name: get all extent disk string
        set_fact:
          extent_disk_string: "{{ extent_disk_list | join(' ') }}"

      - name: mount xen7 extent disk
        raw: /usr/share/tuna/script/xen70/stage_mount_extent_disks.sh "{{ extent_disk_string }}"
        when: myvar.xen7 == True
        register: out
      - debug: var=out.stdout_lines

      - name: mount halo extent disk
        raw: /usr/share/tuna/script/halo/stage_mount_extent_disks.sh "{{ extent_disk_string }}"
        when: myvar.xen7 == False and myvar.halo == True
        register: out
      - debug: var=out.stdout_lines
```

相信大家通过这个简单的示例发现一些问题，我总结了下：

1. 如果脚本中存在较多判断，不宜使用 Playbook 实现逻辑
2. 如果脚本中存在部分参数解析功能，不宜使用 Playbook 实现逻辑
3. 不要过度拆分 task，保证每个 task 完整性

其实上面的 Playbook 我们完全可以写成这样：
```Bash
- name: mount extent disk
  gather_facts: false
  hosts: master:storage
  tasks:
      - name: mount  extent disk
      # 所有逻辑判断均在 stage_mount_extent_disks.sh 中完成
        raw: /usr/share/tuna/script/stage_mount_extent_disks.sh "{{ extent_disk_string }}"
        register: out
      - debug: var=out.stdout_lines
```

Ansible 只作操作分发，减轻 Playbook 复杂性，虽然这会损失一部分幂等性，但是可以最简化的满足要求，同时执行，获取执行结果。

## 总结

从个人使用上来说，Ansible 还是很好用的，至少它无需 Agent，SSH 连接等特性，使用起来很友好。  
但是我们也不应该过分使用 Playbook，编写 Playbook 解析 json 花费了不少的时间，远不如直接在被执行脚本中完成的成本低。

Ansible 还有一些未能合理解决的问题，比如如何知道一个 Playbook 执行的总体进度？
如何获取执行的实时结果输出等。

如果我们只是普通的操作一些节点执行命令，获取信息，那么完全可以通过 sshpass，mmh 等命令完成，相对来说更方便。

希望随着自己的使用，能够更好的掌握使用 Ansible 的度。

