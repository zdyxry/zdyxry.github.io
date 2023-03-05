---
title: Podman(Docker) Compose 学习记录
date: 2021-01-09 18:56:30
tags:
- Container
---




## Compose

最近因为一些需求可能需要用到 Compose，看了看 Podman Compose 和 Docker Compose，记录一下。

Compose 主要功能：
* 环境隔离(docker)
* 一组服务的起停控制
* 服务之间的依赖管理


## Podman compose

项目地址：https://github.com/containers/podman-compose

用爱发电的项目，所有的实现都在 `podman_compose.py` 中，由于 Podman 没有一个好用的 client ，所以 compose 中所有的 Podman 相关的交互都是通过命令行来完成的，目前处于一个非常早期的状态，最基本的服务依赖都没有实现，不建议使用。


## Docker compose

```
cli/            # 命令行解析
config/         # 配置文件格式、校验方式、辅助函数
const.py        # constants
container.py    # 使用 docker client 对 container 命令及属性进行封装
errors.py       # error code
network.py      # 网络相关配置
parallel.py     # 并发操作封装
progress_stream.py # stream 相关
project.py      # project，project 与 service 是一对多的关系
service.py      # service，service 与 container 是一对一或一对多的关系
timeparse.py    # 时间转换
utils.py        # utils function
volume.py       # volume 相关封装
```

Docker 官方提供，所有的 container 都通过 docker python client 进行。service 之间的依赖管理通过拓扑排序实现：

```
def sort_service_dicts(services):
    # Topological sort (Cormen/Tarjan algorithm).
    unmarked = services[:]
    temporary_marked = set()
    sorted_services = []

    def visit(n):
        if n['name'] in temporary_marked:
            if n['name'] in get_service_names(n.get('links', [])):
                raise DependencyError('A service can not link to itself: %s' % n['name'])
            if n['name'] in n.get('volumes_from', []):
                raise DependencyError('A service can not mount itself as volume: %s' % n['name'])
            if n['name'] in n.get('depends_on', []):
                raise DependencyError('A service can not depend on itself: %s' % n['name'])
            raise DependencyError('Circular dependency between %s' % ' and '.join(temporary_marked))

        if n in unmarked:
            temporary_marked.add(n['name'])
            for m in get_service_dependents(n, services):
                visit(m)
            temporary_marked.remove(n['name'])
            unmarked.remove(n)
            sorted_services.insert(0, n)

    while unmarked:
        visit(unmarked[-1])

    return sorted_services
```




执行 `docker-compose up` 流程：

```
self.project.up()
    project:initialize()
        self.networks.initialize()
        self.volumes.initialize()
    self.get_services_without_duplicate()
    svc.ensure_image_exists()
    self._get_convergence_plans()
    parallel.parallel_execute()
        service.execute_convergence_plan()
        self._execute_convergence_create()
            parallel_execute()
                create_and_start()
                    service.create_container()
                    self.start_container()
log_printer.run()
```