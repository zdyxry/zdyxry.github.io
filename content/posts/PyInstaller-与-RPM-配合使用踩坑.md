---
title: PyInstaller 与 RPM 配合使用踩坑
date: 2020-05-13 20:35:50
tags:
- Linux
---


## 背景

最近公司一个项目用到了 pyinstaller 打包 Python 环境，又因为公司内部发布的最小粒度是 rpm，发现这俩工具配合起来默认配置会有坑，然后搜索下来几乎没看到有人提到，可能用 pyinstaller 和用 rpm 的完全是两类人吧 - -。


## 准备

先列一下官方默认例子的输出结果：

```shell
root@localhost:/tmp/demo
 $ pwd
/tmp/demo
root@localhost:/tmp/demo
 $ ls
demo.py
root@localhost:/tmp/demo
 $ pyinstaller demo.py
63 INFO: PyInstaller: 3.6
63 INFO: Python: 3.6.8
65 INFO: Platform: Linux-3.10.0-862.el7.x86_64-x86_64-with-centos-7.5.1804-Core
65 INFO: wrote /tmp/demo/demo.spec
67 INFO: UPX is not available.
70 INFO: Extending PYTHONPATH with paths
['/tmp/demo', '/tmp/demo']
...
```

来看一下生成文件的目录结构：

```
.
├── build
│   └── demo
├── demo.py
├── demo.spec
├── dist
│   └── demo
│       ├── base_library.zip
│       ├── binascii.cpython-36m-x86_64-linux-gnu.so
│       ├── _bisect.cpython-36m-x86_64-linux-gnu.so
│       ├── _blake2.cpython-36m-x86_64-linux-gnu.so
|       ├── ...
│       ├── _codecs_kr.cpython-36m-x86_64-linux-gnu.so
│       ├── _codecs_tw.cpython-36m-x86_64-linux-gnu.so
│       ├── _datetime.cpython-36m-x86_64-linux-gnu.so
│       ├── demo
│       ├── libbz2.so.1
│       ├── libcom_err.so.2
│       ├── libcrypto.so.10
│       ├── libexpat.so.1
│       ├── libgssapi_krb5.so.2
│       ├── libk5crypto.so.3
│       ├── libkeyutils.so.1
│       ├── libtinfo.so.5
│       ├── libkrb5support.so.0
│       ├── liblzma.so.5
│       ├── libpcre.so.1
│       ├── libpython3.6m.so.1.0
│       ├── libreadline.so.6
│       ├── libz.so.1
└── __pycache__
    └── demo.cpython-36.pyc
```


看上去也没啥问题，编写一个 rpm spec，然后使用 rpmbuild 直接就可以生成一个 RPM出来，在 RedHat 系列的 OS上可以直接安装使用，具体的步骤可以参考之前的博客：[《RPM 常用构建方式》](https://zdyxry.github.io/2018/07/28/RPM-%E5%B8%B8%E7%94%A8%E6%9E%84%E5%BB%BA%E6%96%B9%E5%BC%8F/)，目前来看一切都正常，但是坑来了。

## 踩坑

在验证完基础的功能后，我想要将这个 RPM 放到 ISO 中发布，在验证过程中，发现这个 RPM 会破坏系统其他的依赖检查：

```shell
[root@localhost 18:00:20 tmp]$cat packaging.log |grep so |grep 'No such file'
09:19:50,490 INFO packaging: /bin/sh: error while loading shared libraries: libtinfo.so.5: cannot open shared object file: No such file or directory
09:19:50,490 INFO packaging: /bin/sh: error while loading shared libraries: libtinfo.so.5: cannot open shared object file: No such file or directory
09:19:50,491 INFO packaging: /bin/sh: error while loading shared libraries: libtinfo.so.5: cannot open shared object file: No such file or directory
09:19:50,491 INFO packaging: /sbin/install-info: error while loading shared libraries: libz.so.1: cannot open shared object file: No such file or directory
09:19:50,491 INFO packaging: /sbin/install-info: error ...
09:19:50,495 INFO packaging: /sbin/install-info: error while loading shared libraries: libz.so.1: cannot open shared object file: No such file or directory
09:19:50,499 INFO packaging: /usr/bin/trust: error while loading shared libraries: libfreebl3.so: cannot open shared object file: No such file or directory
09:19:50,499 INFO packaging: /sbin/install-info: error while loading shared libraries: libz.so.1: cannot open shared object file: No such file or directory
09:19:50,499 INFO packaging: /sbin/install-info: error while loading shared libraries: libz.so.1: cannot open shared object file: No such file or directory
09:19:50,499 INFO packaging: /sbin/install-info: error while loading shared libraries: libz.so.1: cannot open shared object file: No such file or directory
09:19:50,500 INFO packaging: /sbin/install-info: error while loading shared libraries: libz.so.1: cannot open shared object file: No such file or directory
09:19:50,501 INFO packaging: /sbin/install-info: error while loading shared libraries: libz.so.1: cannot open shared object file: No such file or directory
```

简单的过滤了一下，有这些包直接受到了影响，还有很多未知的，简单的说就是系统的一些核心依赖库缺失，没有安装成功：


```shell
[root@localhost 18:02:48 tmp]$cat packaging.log |grep 'scriptlet failed'
09:19:50,490 INFO packaging: warning: %post(readline-6.2-10.el7.x86_64) scriptlet failed, exit status 127
09:19:50,490 INFO packaging: warning: %post(gawk-4.0.2-4.el7_3.1.x86_64) scriptlet failed, exit status 127
09:19:50,491 INFO packaging: warning: %post(info-5.1-4.el7.x86_64) scriptlet failed, exit status 127
09:19:50,491 INFO packaging: warning: %post(qemu-kvm-aurora-0.3.3-1.x86_64) scriptlet failed, exit status 127
09:19:50,495 INFO packaging: warning: %post(glib2-2.50.3-3.el7.x86_64) scriptlet failed, exit status 127
09:19:50,499 INFO packaging: warning: %post(ca-certificates-2017.2.14-71.el7.noarch) scriptlet failed, exit status 127
```

最初在排查是否是 anaconda 在检查 rpm 相互之间的依赖时出了 bug，但是最近版本没什么变化，理论上不会，又去瞧了瞧 anaconda 的代码，发现跟 rpm 相关的太多，一时也没看出什么头绪。

再来看一下相关的库， `libz.so.1` , `libtinfo.so.5` 有没有点眼熟，都是在 pyinstaller 生成的文件中的，但是有一点很奇怪，命令路径都不是系统路径，为什么在检查依赖的时候还是会检查到新加入的 rpm 上，而不是真正提供这些库的 RPM？

## 解决

今天的主角登场：Automatic Dependencies。

Automatic Dependencies 是 RPM 的一个特性，官方文档中是这么描述的：

> When a package is built by RPM, if any file in the package's %files list is a shared library, the library's soname is automatically added to the list of capabilities the package provides. The soname is the name used to determine compatibility between different versions of a library.

> Note that this is not a filename. In fact, no aspect of RPM's dependency processing is based on filenames. Many people new to RPM often make the assumption that a failed dependency represents a missing file. This is not the case.

> Remember that RPM's dependency processing is based on knowing what capabilities are provided by a package and what capabilities a package requires. We've seen how RPM automatically determines what shared library resources a package provides. But does it automatically determine what shared libraries a package requires?

> Yes! RPM does this by running ldd on every executable program in a package's %files list. Since ldd provides a list of the shared libraries each program requires, both halves of the equation are complete — that is, the packages that make shared libraries available, and the packages that require those shared libraries, are tracked by RPM. RPM can then take that information into account when packages are installed, upgraded, or erased.

嗯，找到问题了，解决的方式也很简单，直接关掉就好：

```
AutoReqProv: no
```


## 总结

通常来说 pyinstaller 用的人不少，rpm 用的人也不少，这俩默认配置配合使用是一定会出问题的，但是没有找到相关的问题，可能真的不是一类人吧。

用同事的话作为结束语： `automatic 开头的东西，一个字都不要信`。


