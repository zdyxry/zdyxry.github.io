---
title: Libvirt CPU 配置
date: 2019-03-02 19:40:20
tags:
- Libvirt
---

## Libvirt CPU 配置参数

我们先来看下 Libvirt 关于虚拟机 CPU 配置项：
* match
* check
* mode
* model
* ...

具体配置解释可以去 Libvirt 官方文档中查看，这里主要说一下 `mode` 参数，看一下 `mode` 具体含义及可选配置：

### host-passthrough
Libvirt 通知 KVM 对 CPU 不做任何配置项修改，直通给虚拟机。因为虚拟机可以使用与物理主机相同 CPU 指令集，性能最好，相反，在虚拟机热迁移过程中，对目标主机 CPU 要求同型号同代。

### host-model
本质上是根据物理主机 CPU 从 `cpu_map.xml` 文件中选择最匹配的 CPU 型号。由于CPU定义是在启动虚拟机之前复制的，因此可以在不同主机上使用完全相同的XML，同时仍然提供每个主机支持的最佳虚拟机 CPU。属于在功能与性能之间的平衡。

### custom
不指定 `mode` 属性时的默认值。此模式使得无论虚拟机启动哪个主机，虚拟机都将看到相同的硬件，兼容性最好。

## 最佳选择
在不考虑虚拟机兼容性（热迁移）情况下，优先选择 `host-passthrough` ，综合考虑选择 `host-model` 。  

OpenStack 中如果检测到 hypervisor 是 kvm-qemu ，则默认值为 `host-model` ；在 hypervisor 是其他类型时，默认值为 `none`，即由 hypervisor 自己选择。

我查看了自己两台 VPS 的 CPU 信息，如下：

### Vultr

```bash
[root@vultr ~]# lscpu
Architecture:          x86_64
厂商 ID：           GenuineIntel
CPU 系列：          6
型号：              60
型号名称：        Virtual CPU 71438xxxxxxx
超管理器厂商：  KVM
虚拟化类型：     完全
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx rdtscp lm constant_tsc rep_good nopl xtopology cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm invpcid_single pti fsgsbase bmi1 avx2 smep bmi2 erms invpcid xsaveopt arat
```

### BWH

```bash
[root@bwh ~]# lscpu
Architecture:          x86_64
厂商 ID：           GenuineIntel
CPU 系列：          6
型号：              13
型号名称：        QEMU Virtual CPU version (cpu64-rhel6)
超管理器厂商：  KVM
虚拟化类型：     完全
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm rep_good nopl pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic popcnt aes xsave avx f16c rdrand hypervisor lahf_lm fsgsbase smep xsaveopt
```

可以看到 BWH 的 CPU 比 Vultr CPU 指令集少了很多，而且 CPU 型号是 `QEMU Virtual CPU version (cpu64-rhel6)` 推断物理机 libvirt 配置是 `custom` ，果然便宜无好货。


## 参考链接
* https://docs.openstack.org/juno/config-reference/content/kvm.html
* https://wiki.openstack.org/wiki/LibvirtXMLCPUModel
* https://patchwork.kernel.org/patch/9219601/
* https://lists.gnu.org/archive/html/qemu-devel/2016-06/msg00634.html
* http://wsfdl.com/openstack/2018/01/02/libvirt_cpu_mode.html
