---
title: 关于Ansible的一点经验
date: 2019-07-05 20:55:19
tags:
- Ansible
---


## 背景

先介绍下 Kubespray，Kubespray 是 K8S SIG 下的项目，目标是帮助用户创建 `生产环境级别` 的 k8s 集群。

是通过 Ansible Playbook 实现的，是的，这又是一个 Ansible 项目，其中 YAML 文件就有 15k 行，名副其实的大项目。

花费了几天时间陆陆续续看完了整个项目，大概了解了其中的工作流程，具体内容不提，感觉 Ansible 90% 的使用例子都可以在这个项目中找到，是一个值得阅读的项目。


之前写过一篇当时理解的最佳实践，今天趁此机会再总结下最近使用 Ansible 的一些经验。


##  Tag

使用 tag 对 ansible task 进行划分，比如在重启某些服务的时候，我们只希望在初次安装的时候重启，在后续升级的时候不进行重启，那么我们就可以对这个重启服务的 task 进行tag 区分。

tag 使用示例如下：

```bash
[root@node111 16:35:56 ansible]$tree . 
.
├── ansible.cfg
├── inventory
├── templates
│   └── src.j2
└── test.yaml

1 directory, 4 files
[root@node111 16:35:58 ansible]$cat test.yaml 
- hosts: cluster
  gather_facts: no
  become: yes
  become_user: root
  become_method: sudo
  tasks:
  - yum:
      name: "{{ item }}"
      state: present
    loop:
    - httpd
    - memcached
    tags:
    - packages
  
  - template:
      src: templates/src.j2
      dest: /etc/foo.conf
    tags:
    - configuration
[root@node111 16:36:01 ansible]$ansible-playbook -i inventory  test.yaml --tags configuration -v
Using /root/ansible/ansible.cfg as config file

PLAY [cluster] ******************************************************************************************************************************************************************************************************************************************************

TASK [template] *****************************************************************************************************************************************************************************************************************************************************
ok: [172.16.30.111] => {"changed": false, "checksum": "7b4cbb07f7e174316e4d892321682317e43a206c", "dest": "/etc/foo.conf", "gid": 0, "group": "root", "mode": "0644", "owner": "root", "path": "/etc/foo.conf", "size": 14, "state": "file", "uid": 0}
ok: [172.16.30.112] => {"changed": false, "checksum": "7b4cbb07f7e174316e4d892321682317e43a206c", "dest": "/etc/foo.conf", "gid": 0, "group": "root", "mode": "0644", "owner": "root", "path": "/etc/foo.conf", "size": 14, "state": "file", "uid": 0}
ok: [172.16.30.113] => {"changed": false, "checksum": "7b4cbb07f7e174316e4d892321682317e43a206c", "dest": "/etc/foo.conf", "gid": 0, "group": "root", "mode": "0644", "owner": "root", "path": "/etc/foo.conf", "size": 14, "state": "file", "uid": 0}

PLAY RECAP **********************************************************************************************************************************************************************************************************************************************************
172.16.30.111              : ok=1    changed=0    unreachable=0    failed=0   
172.16.30.112              : ok=1    changed=0    unreachable=0    failed=0   
172.16.30.113              : ok=1    changed=0    unreachable=0    failed=0   
```



## roles/meta 管理依赖

在 playbook 中存在多个 roles，且其中有相互依赖关系时，合理使用 meta 配置，填写其所依赖的 roles。注意，被依赖的 roles 会优先执行，示例如下：


```bash
[root@node111 16:49:12 ansible]$tree . 
.
├── ansible.cfg
├── inventory
├── roles
│   ├── a
│   │   ├── defaults
│   │   ├── files
│   │   ├── handlers
│   │   ├── meta
│   │   │   └── main.yaml
│   │   ├── tasks
│   │   │   └── main.yaml
│   │   ├── templates
│   │   └── vars
│   └── b
│       ├── defaults
│       ├── files
│       ├── handlers
│       ├── meta
│       ├── tasks
│       │   └── main.yaml
│       ├── templates
│       └── vars
├── templates
│   └── src.j2
└── test.yaml

18 directories, 7 files
[root@node111 16:49:18 ansible]$cat roles/a/tasks/main.yaml 
---
- name: a
  debug:
    msg: "a"
[root@node111 16:49:25 ansible]$cat roles/a/meta/main.yaml 
---
dependencies:
  - { role: b }
[root@node111 16:49:33 ansible]$cat roles/b/tasks/main.yaml 
---
- name: b
  debug:
    msg: "b"
[root@node111 16:49:40 ansible]$ansible-playbook -i inventory  test.yaml -v
Using /root/ansible/ansible.cfg as config file

PLAY [cluster] ******************************************************************************************************************************************************************************************************************************************************

TASK [b : b] ********************************************************************************************************************************************************************************************************************************************************
ok: [172.16.30.111] => {
    "msg": "b"
}
ok: [172.16.30.112] => {
    "msg": "b"
}
ok: [172.16.30.113] => {
    "msg": "b"
}

TASK [a : a] ********************************************************************************************************************************************************************************************************************************************************
ok: [172.16.30.111] => {
    "msg": "a"
}
ok: [172.16.30.112] => {
    "msg": "a"
}
ok: [172.16.30.113] => {
    "msg": "a"
}

PLAY RECAP **********************************************************************************************************************************************************************************************************************************************************
172.16.30.111              : ok=2    changed=0    unreachable=0    failed=0   
172.16.30.112              : ok=2    changed=0    unreachable=0    failed=0   
172.16.30.113              : ok=2    changed=0    unreachable=0    failed=0   

You have new mail in /var/spool/mail/root
[root@node111 16:50:05 ansible]$
```


## 参数声明

在一个大型项目中，我们无论是服务的数量还是各个服务对应的参数数量都是极其惊人的，那么我们就要合理的管理相应参数，这里 kubespray 项目给出了一个很好的示例，先来看下 kubespray 的组织结构（简化版）：

```bash
inventory/
├── local
│   └── group_vars -> ../sample/group_vars
└── sample
    └── group_vars
        ├── all
        └── k8s-cluster
roles
├── container-engine
│   ├── containerd
│   │   ├── defaults
│   │   ├── handlers
│   │   ├── tasks
│   │   └── templates
│   ├── docker
│   │   ├── defaults
│   │   ├── files
│   │   ├── handlers
│   │   ├── meta
│   │   ├── tasks
│   │   ├── templates
│   │   └── vars
│   └── meta
├── kubespray-defaults
│   ├── defaults
│   ├── meta
│   └── tasks
```

在 kubespray 中，参数定义有三个位置：

1. inventory/sample/group_vars
2. roles/kubespray-defaults/defaults
3. roles/<common>/defaults
4. 使用 `set_fact` 关键字声明


上述三个位置是按照参数粒度划分，参数粒度越细，越靠后。

举个例子：
* `bin_dir` 这个参数，是一个全局参数，管理下载的二进制文件路径，它在 `inventory/samle/group_vars` 中定义； 
* `etcd_kubeadm_enabled` 参数，决定是否通过 kubeadm 来创建 etcd 集群，是集群粒度的，在 `roles/kubesray-defaults/defaults` 中定义；
* `docker_fedora_repo_base_url` 是 docker 在下载镜像时指定的 repo，是一个容器运行时粒度的参数，那么它就在 `roles/container-ngine/docker/defaults` 中定义
* 执行某些命令后，我们希望对命令结果进行过滤或判断，那么我们通常会使用 regster，但是 register 的声明周期仅限于该 playbook，而且他们的优先级也是不同的，具体可以看下[官方文档](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#ansible-variable-precedence)


可能跟大多数项目不同，kubespray 中涉及的参数数量很多，不知道是否是这个原因，专门使用了 `roles/kubespray-defaults` 这个 role 来声明参数。不过它的这种参数划分方式是我们值得学习的。


## Handler 触发

当我们更新了配置文件之后，我们想要重启相应服务，这时候可以使用 notify 配合 handlers 来完成相应操作，而且 handler
的方式也可以保证我们代码最大程度的重用。


## loop_control

当我们在 playbook 中定义了某个变量为 list 类型，我们想要遍历变量，并且针对每个变量的操作都进行错误处理，我们可以采用 loop_control 关键字配合 include 来实现，比如：

```
- include_tasks: docker_plugin.yml
  loop: "{{ docker_plugins }}"
  loop_control:
    loop_var: docker_plugin
```

循环 `device_plugins` ，每个变量为 `docker_plugin` ，将 `docker_plugin` 传递到 `docker_plugin.yml` 。


## 不建议的操作

### 在 ansible 中使用复杂的语法规则

在 kubespray 中，随处可见一些很复杂的语法夹杂在 playbook 中，看到一个比较头疼的：

```yaml
   279	
   280	dashboard_image_repo: "gcr.io/google_containers/kubernetes-dashboard-{{ image_arch }}"
   281	dashboard_image_tag: "v1.10.1"
   282	
   283	image_pull_command: "{{ docker_bin_dir }}/docker pull"
   284	image_info_command: "{{ docker_bin_dir }}/docker images -q | xargs {{ docker_bin_dir }}/docker inspect -f \"{{ '{{' }} if .RepoTags {{ '}}' }}{{ '{{' }} (index .RepoTags 0) {{ '}}' }}{{ '{{' }} end {{ '}}' }}{{ '{{' }} if .RepoDigests {{ '}}' }},{{ '{{' }} (index .RepoDigests 0) {{ '}}' }}{{ '{{' }} end {{ '}}' }}\" | tr '\n' ','"
   285	
   286	downloads:
   287	  netcheck_server:
   288	    enabled: "{{ deploy_netchecker }}"
   289	    container: true
   290	    repo: "{{ netcheck_server_image_repo }}"
   291	    tag: "{{ netcheck_server_image_tag }}"
   292	    sha256: "{{ netcheck_server_digest_checksum|default(None) }}"
```

284 行获取 `image_info_command` ，这里真的是一点可维护性都没有，初步看很难看出这里到底是 ansible 语法，还是 shell 语法，还是 go template 语法，如果我们要通过这么复杂的方式来获取一个参数，为什么不干脆写一个脚本来完成这个事情呢？ 搞不懂。


## 总结

看完 kubespray 了解了 k8s 集群部署的步骤之外，Ansible 的一些高级用法或者说经验是之后需要改善的，收获多多。
