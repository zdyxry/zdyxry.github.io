---
title: Linux 主机异常信息收集
date: 2018-07-06 15:28:09
tags:
- Linux
- Ops
---



## 背景

通常情况下，一个公司内部都会有监控报警平台去支撑业务主机的稳定运行，比如 Nagios，Zabbix 或者 Prometheus 等其他工具。
这些工具，无论是 push 模式还是 pull 模式，都基于一个前提：主机是可访问的，或者说 agent/exporter 是可正常工作的。

如果运维人员在面对一台处于异常状态的主机，应该如何收集该主机的当前状态及相应日志呢？

企业级产品通常会内置工具用来采集异常状态信息，比如：
* DELL 服务器如果出现了未知错误，拨打 400 询问问题，
一线客服会告诉你，打开 iDRAC 界面，点击“收集日志” 选项，会自动收集并下载节点信息
* 如果你是 RedHat RHEL 用户，主机出现异常状态，红帽技术支持工程师进行初始分析时，通常会使用 sosreport 工具


## 简介

sosreport 命令是一个工具，用来收集 RHEL 系统上的配置信息、系统信息和诊断信息。比如：正在运行的内核版本、已加载的模块，以及系统和服务的配置文件。同时，sosreport 支持用户自己编写 Plugin ，用于收集自己想要收集的服务日志及命令结果。  


## 使用
sosreport 提供了 `sosreport` 命令行，用户可以直接执行该命令收集信息，默认收集所有 Plugin 信息。


## 执行流程

通过 which 命令查看提供 sosreport 命令行的文件，可以看到指向 `sos.sosreport.main`。  

```shell
root@yiran-30-250:~/project/sos 
master ✔ $ which sosreport
/usr/sbin/sosreport
root@yiran-30-250:~/project/sos 
master ✔ $ cat /usr/sbin/sosreport
#!/usr/bin/python
import sys
try:
    from sos.sosreport import main
except KeyboardInterrupt:
    raise SystemExit()

if __name__ == '__main__':
    main(sys.argv[1:])
```

查看 main 函数，实例化 SoSReport，并执行 SoSReport中的 execute 方法，查看 execute 具体做了什么：

```python
    def execute(self):
        try:
            # 获取集群配置并配置，包含日志路径，报告路径,配置文件等参数
            self.policy.set_commons(self.get_commons())
            self.print_header()
            # 加载所有插件,并根据发行版本进行校验
            self.load_plugins()
            # 设置默认配置参数
            self._set_all_options()
            self._set_tunables()
            self._check_for_unknown_plugins()
            self._set_plugin_options()

            if self.opts.list_plugins:
                self.list_plugins()
                return True
            if self.opts.list_profiles:
                self.list_profiles()
                return True
            if self.opts.list_presets:
                self.list_presets()
                return True
            if self.opts.add_preset:
                return self.add_preset(self.opts.add_preset)
            if self.opts.del_preset:
                return self.del_preset(self.opts.del_preset)
            # verify that at least one plug-in is enabled
            if not self.verify_plugins():
                return False

            self.batch()
            # 收集前准备工作，包括打包方式等配置
            self.prework()
            self.setup()
            # 真正开始收集执行
            self.collect()
            if not self.opts.noreport:
                self.report()
                self.html_report()
                self.plain_report()
            self.postproc()
            self.version()
            return self.final_work()
```

其中，主要步骤有两步：
1. 加载插件并校验
2. 执行各个插件内容


### 加载插件并校验

通过遍历软件包所在路径，先获取所有的插件名称:

```python
    def _plugin_name(self, path):
        "Returns the plugin module name given the path"
        base = os.path.basename(path)
        name, ext = os.path.splitext(base)
        return name

    def _get_plugins_from_list(self, list_):
        plugins = [self._plugin_name(plugin)
                   for plugin in list_
                   if "__init__" not in plugin and plugin.endswith(".py")]
        plugins.sort()
        return plugins

    def _find_plugins_in_dir(self, path):
        if os.path.exists(path):
            py_files = list(find("*.py", path))
            pnames = self._get_plugins_from_list(py_files)
            if pnames:
                return pnames
            else:
                return []

    def get_modules(self):
        """Returns the list of importable modules in the configured python
        package. """
        plugins = []
        for path in self.package.__path__:
            if os.path.isdir(path) or path == '':
                plugins.extend(self._find_plugins_in_dir(path))

        return plugins
```

获取到插件名称后，获取 Linux 主机发行版本信息，并将发行版本指定为 import 参数，
用于判断插件是否支持该发行版本(通过 inspect 校验 是否为子类方式):

```python
def import_module(module_fqname, superclasses=None):
    """Imports the module module_fqname and returns a list of defined classes
    from that module. If superclasses is defined then the classes returned will
    be subclasses of the specified superclass or superclasses. If superclasses
    is plural it must be a tuple of classes."""
    module_name = module_fqname.rpartition(".")[-1]
    module = __import__(module_fqname, globals(), locals(), [module_name])
    modules = [class_ for cname, class_ in
               inspect.getmembers(module, inspect.isclass)
               if class_.__module__ == module_fqname]
    if superclasses:
        modules = [m for m in modules if issubclass(m, superclasses)]

    return modules
```

接下来还有根据命令行参数进行相应配置参数传递，此处不进行展开。

### 执行各个插件

查看 self.collect() 函数，可以发现，最终执行是通过线程池进行的，默认 Pool Size 为 4。

```python
    def collect(self):
        self.ui_log.info(_(" Running plugins. Please wait ..."))
        self.ui_log.info("")

        plugruncount = 0
        self.pluglist = []
        self.running_plugs = []
        for i in self.loaded_plugins:
            plugruncount += 1
            self.pluglist.append((plugruncount, i[0]))
        try:
            self.plugpool = ThreadPoolExecutor(self.opts.threads)
            # Pass the plugpool its own private copy of self.pluglist
            self.plugpool.map(self._collect_plugin, list(self.pluglist),
                              chunksize=1)
            self.plugpool.shutdown(wait=True)
            self.ui_log.info("")
        except KeyboardInterrupt:
            # We may not be at a newline when the user issues Ctrl-C
            self.ui_log.error("\nExiting on user cancel\n")
            os._exit(1)
```

在查看 self._collect_plugin，发现最终执行的函数为 `plug.collect()` ,这指向了插件本身，
随便找一个插件看看是否有 collect 方法，以 block 插件为例：

```python
import os
from sos.plugins import Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin

class Block(Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin):
    """Block device information
    """

    plugin_name = 'block'
    profiles = ('storage', 'hardware')
    verify_packages = ('util-linux',)
    files = ('/sys/block',)

    def setup(self):
		# 执行命令收集信息
        self.add_cmd_output([
            "lsblk",
            "lsblk -t",
            "lsblk -D",
            "blkid -c /dev/null",
            "blockdev --report",
            "ls -lanR /dev",
            "ls -lanR /sys/block"
        ])

        # legacy location for non-/run distributions
        # 拷贝文件路径收集信息
        self.add_copy_spec([
            "/etc/blkid.tab",
            "/run/blkid/blkid.tab",
            "/proc/partitions",
            "/proc/diskstats",
            "/sys/block/*/queue/scheduler"
        ])

        if os.path.isdir("/sys/block"):
            for disk in os.listdir("/sys/block"):
                if disk.startswith("ram"):
                    continue
                disk_path = os.path.join('/dev/', disk)
                self.add_udev_info(disk_path)
                self.add_udev_info(disk_path, attrs=True)
                self.add_cmd_output([
                    "parted -s %s unit s print" % (disk_path),
                    "fdisk -l %s" % disk_path
                ])
```

可以看到，插件中除了实现了 setup，指定了一些命令及相应收集文件路径，并没有 collect()，
那么我们查看 block 插件 Block 的父类，Plugin：

```python
    def collect(self):
        """Collect the data for a plugin."""
        start = time()
        self._collect_copy_specs()
        self._collect_cmd_output()
        fields = (self.name(), time() - start)
        self._log_debug("collected plugin '%s' in %s" % fields)
```

这里我们看到，执行 plug.collect() 的内容为：_collect_copy_specs()，_collect_cmd_output() 
和 _collect_strings(), 那么我们接下来就能看到这三个函数具体执行的内容了：


#### 收集文件

通过层层跳转，最终看到各个打包方式的不同，收集文件的方式也不同，这里用 FileCache 举例，
可以看到最终调用的是标准库中的 `shutil` 实现文件拷贝。

```python
    def add_file(self, src, dest=None):
        if not dest:
            dest = src
        dest = self.dest_path(dest)
        self._check_path(dest)

        # Handle adding a file from either a string respresenting
        # a path, or a File object open for reading.
        if not getattr(src, "read", None):
            # path case
            try:
                shutil.copy(src, dest)
```

#### 命令执行

同理，命令执行对应的最终是 subprocess.Popen 函数：

```python
    try:
        p = Popen(expanded_args, shell=False, stdout=PIPE,
                  stderr=STDOUT if stderr else PIPE,
                  bufsize=-1, env=cmd_env, close_fds=True,
                  preexec_fn=_child_prep_fn)

        reader = AsyncReader(p.stdout, sizelimit, binary)
        stdout = reader.get_contents()
        p.poll()
```


## 总结

通过阅读代码，我们可以了解到，sosreport 插件编写还是很容易的，只需要将要执行的命令及要拷贝的文件填写好就基本上完成了。
同时，强烈推荐一下 sosreport 中内置插件，能够帮助我们更好的了解某些功能，毕竟只有在出现故障的时候才是暴露最多的时候，比如 networking.py 中关于网络配置命令、网卡配置文件、DNS/DHCP 配置等信息，可以极大的扩充对 Linux 系统的了解程度，应该很有帮助。
