---
title: ARM 服务器适配总结
date: 2020-08-22 15:09:04
tags:
- Linux
---

## 背景

上一次写 [ARM 服务器](https://zdyxry.github.io/2019/11/01/ARM-%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%9F%E8%83%BD%E7%94%A8%EF%BC%9F/)相关的是在大半年以前了，当时适配工作做得神烦，最近在折腾 ARM 上 KVM 虚拟化相关的事情，目标是虚拟化功能最小代码改动同时兼容 x86 和 ARM，记录一下目前的一点经验总结。

硬件配置：  
* 华为泰山服务器
* Kunpeng 920

软件配置：  
* CentOS 7.6
* kernel-4.18.0-193.1.2.el7.aarch64
* libvirt-4.5.0
* qemu-2.12.0


## 信息获取

### Architecture

如果产品之前都是 x86 架构下的，在适配 ARM 时往往需要进行架构判断，此时可以通过 `arch` 来获取，在 ARM 架构显示 `aarch64` ，在 x86 架构下显示 `x86_64` 。

`aarch64` 等价于 `arm64`。

> AArch64 or ARM64 is the 64-bit extension of the ARM architecture.


### KVM module

在 x86 上我们可以直接通过 `lsmod |grep kvm` 查看到 KVM module 情况:

```
[root@node90 19:24:30 ~]$lsmod |grep kvm
kvm_intel             188644  82 
kvm                   621480  1 kvm_intel
```

但是在 arm 上是没有加载 KVM module 的，此时想要知道 KVM 配置是否正确，可以通过 `dmesg` 中查看 KVM 相关日志：

```
[Wed Jul  8 13:43:11 2020] kvm [1]: IPA Size Limit: 48bits
[Wed Jul  8 13:43:11 2020] kvm [1]: GICv4 support disabled
[Wed Jul  8 13:43:11 2020] kvm [1]: vgic-v2@9b020000
[Wed Jul  8 13:43:11 2020] kvm [1]: GIC system register CPU interface enabled
[Wed Jul  8 13:43:11 2020] kvm [1]: vgic interrupt IRQ1
[Wed Jul  8 13:43:11 2020] kvm [1]: VHE mode initialized successfully
```

如果看到 `VHE mode initialized successfully` ，那么 KVM 正常。

### CPU

在 CentOS 中通常使用 cpuinfo 来获取 CPU 相关信息，但是发现集群中某个节点无法获取主频相关信息，通过 lscpu 也无法正确显示，开始以为是 `util-linux` 相关软件的版本不兼容导致，后续排查发现不是这个问题，于是考虑通过其他方式获取主频。

正常 cpuinfo 输出结果如下：

```
Hz Advertised: 2.6000 GHz
Hz Actual: 2.6000 GHz
Hz Advertised Raw: (2600000000, 0)
Hz Actual Raw: (2600000000, 0)
Arch: ARM_8
```

如果作为他信息统计的话我们往往使用的是 `Hz Advertised Raw` 字段，我们可以通过 `dmidecode` 获取，`dmidecode` 输出结果示例如下：

```
[root@node90 19:33:47 ~]$dmidecode -t 4 
        ...
        Max Speed: 4000 MHz
        Current Speed: 2600 MHz
        Status: Populated, Enabled
        Upgrade: Socket LGA2011
        L1 Cache Handle: 0x0009
        L2 Cache Handle: 0x000A
        L3 Cache Handle: 0x000B
```

这里需要进行区分， `dmidecode` 获取到的是主板信息，比如 `Max Speed` 指的是主板支持最大主频，如果我们想获取当前 CPU 标称主频，需要使用 `Current Speed` 字段数值。

## 功能支持

### Machine Type

在 x86 架构下，支持两种 Machine Type，分别为 q35 和 i440fx(pc)，我们使用的是 i440fx，这两种类型我理解最主要的区别在于 PCI 和 PCIE 的支持，通俗描述就是 `兼容性` 更好。目前 x86 架构下的 Machine Type 我们使用的是 i440fx(pc)。但是在 ARM 架构下只支持一种 Machine Type，就是 mach-virt(virt) ，而这种架构下的大部分行为与 q35 相同，所以我们在创建虚拟机时所指定的基本参数就需要进行相应的调整。

### Boot Options

ARM 架构下虚拟机不支持 BIOS 引导，只支持 UEFI，在设置 UEFI  bootloader 时，需要使用 aarch64 版本的 edk2(EFI Development Kit II)，虽然 edk2 的 x86 下使用的是 noarch 版本，但是这里的 noarch 是假象，还是需要指定 aarch64 版本才可以。

```
[root@node26 19:58:59 ~]$rpm -ql edk2.git-aarch64-0-20200515.1405.g9af1064995.noarch
/usr/share/edk2.git
/usr/share/edk2.git/aarch64
/usr/share/edk2.git/aarch64/QEMU_EFI-pflash.raw
/usr/share/edk2.git/aarch64/QEMU_EFI.fd
/usr/share/edk2.git/aarch64/QEMU_VARS.fd
/usr/share/edk2.git/aarch64/vars-template-pflash.raw
/usr/share/qemu/firmware/80-uefi-a64-git.json
```

在 libvirt qemu 配置文件中指定 nvram 文件路径：

```
[root@node26 19:59:23 ~]$cat /etc/libvirt/qemu.conf 
nvram = ["/usr/share/edk2.git/aarch64/QEMU_EFI-pflash.raw:/usr/share/edk2.git/aarch64/vars-template-pflash.raw"]
```

### Controller

虚拟机配置中，一个比较重要的地方是 Controller 配置，在 q35 Machine Type 中：不支持 PCI Controller，仅支持 PCI-E Controller，因此需要特殊注意；同时 USB Controller 支持 XHCI Controller，XHCI 可以同时支持 USB 1.1，2.0，3.0 设备。

#### PCI-E Controller

默认的 PCI 拓扑如下：

```
<controller type='pci' index='0' model='pcie-root'/>
<controller type='pci' index='1' model='pcie-root-port'>
  <model name='pcie-root-port'/>
  <target chassis='1' port='0x10'/>
  <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x0'/>
</controller>
```

`pcie-root` 不支持设备的热插拔，因此需要将设备添加到 `pcie-root-port` 上，但是 `pcie-root-port` 自身也不支持热插拔，所以需要在虚拟机创建时预先分配好一定数量的 `pcie-root-port` Controller 用于后续其他设备的热插拔。

文档中提到 q35 支持 `pcie-to-pci-bridge` 控制器用于连接一些传统的 PCI 设备，但是实际测试中发现没有作用，不知道是不是我的姿势有问题。

上面提到要在虚拟机创建时预先分配 `pcie-root-port` Controller，我们需要知道 `pcie-root` 所支持的 `pcie-root-port` 数量上限是多少，没有找到相关文档，于是我去看了看 virt-manager 中是否有特殊处理，代码中没找到 `pcie-root-port` 关键字，在测试的 XML 文件中，发现最多添加了 8 个 `pcie-root-port` Controller。virt-manager 没找到，那么就去 OpenStack Nova 中找。

在 nova/virt/libvirt/driver.py 中，看到了添加 `pcie-root-port` Controller 的相关逻辑：

```python
    def _guest_add_pcie_root_ports(self, guest):
        """Add PCI Express root ports.

        PCI Express machine can have as many PCIe devices as it has
        pcie-root-port controllers (slots in virtual motherboard).

        If we want to have more PCIe slots for hotplug then we need to create
        whole PCIe structure (libvirt limitation).
        """

        pcieroot = vconfig.LibvirtConfigGuestPCIeRootController()
        guest.add_device(pcieroot)

        for x in range(0, CONF.libvirt.num_pcie_ports):
            pcierootport = vconfig.LibvirtConfigGuestPCIeRootPortController()
            guest.add_device(pcierootport)
```

nova 在创建虚拟机时，直接预先分配了所有的 `pcie-root-port` ，达到了 libvirt 的上限，在 nova 中时一个常量 28，并且给出了 qemu 关于 PCI-E 相关的文档说明：

```
    cfg.IntOpt('num_pcie_ports',
               default=0,
               min=0,
               max=28,
               help= """
The number of PCIe ports an instance will get.

Libvirt allows a custom number of PCIe ports (pcie-root-port controllers) a
target instance will get. Some will be used by default, rest will be available
for hotplug use.

By default we have just 1-2 free ports which limits hotplug.

More info: https://github.com/qemu/qemu/blob/master/docs/pcie.txt

Due to QEMU limitations for aarch64/virt maximum value is set to '28'.

Default value '0' moves calculating amount of ports to libvirt.
"""),
```

于是我在创建虚拟机的时候指定了 28个 `pcie-root-port` Controller，但是发现虚拟机无法成功引导，简单的二分最终确认在当前环境配置下，虚拟机最多支持 15 个 `pcie-root-port` ，猜测可能根当前使用的版本有关。


#### USB Controller

USB Controller model 选择 `qemu-xhci` ，添加一个即可，涉及到的设备有 mouse, keyboard, tablet ，都需要将 bus 设置未 usb 。

在 Controller 确认完成后，我们可以得出当前虚拟机支持设备上限：最多可以连接 15 个 Device/Controller，其中 USB Controller 和 Virtio Video 占用 2个 port，剩余 13 个 port，可以最多插入 13 个 Virtio Device ，也可插入 13 个 Controller，1 个 SCSI Controller 可以插入 7 个 SCSI Disk。

### Video 

q35 仅支持 `virtio` 类型的 Video 设备，cirrus, vga, qxl 都不支持。

### CDROM

不支持 IDE 磁盘，因此需要将 CDROM 的 bus 总线设置为 SCSI。

### CPU Model 

通常我们为了虚拟机兼容性考虑，都会将虚拟机的 CPU Model 设置的略微低一些，避免当一个集群中存在节点 CPU 代数不一致时导致虚拟机无法热迁移，通常我们在 x86 下可以通过 `virsh domcapabilities` 获取：

```
    <mode name='custom' supported='yes'>
      <model usable='yes'>qemu64</model>
      <model usable='yes'>qemu32</model>
      <model usable='no'>phenom</model>
      <model usable='yes'>IvyBridge</model>
      <model usable='no'>IvyBridge-IBRS</model>
      <model usable='no'>Haswell</model>
      <model usable='no'>Haswell-noTSX</model>
      <model usable='no'>Haswell-noTSX-IBRS</model>
      <model usable='no'>Haswell-IBRS</model>
    </mode>
```

可以通过 `usable` 属性来判断是否可以配置，但是在 ARM 下所有的 `usable` 属性都是 unknown，强行设置后，虚拟机无法启动，在当前版本下时无法进行 CPU Model 设置的。

```
    <mode name='host-passthrough' supported='yes'/>
    <mode name='host-model' supported='no'/>
    <mode name='custom' supported='yes'>
      <model usable='unknown'>cortex-a53</model>
      <model usable='unknown'>cortex-a57</model>
      <model usable='unknown'>max</model>
      <model usable='unknown'>cortex-a15</model>
    </mode>
```

## 总结

经过一番折腾，终于可以在 ARM 服务器上进行虚拟化功能的使用了，实际使用感受还不错，没啥问题。

例行吐槽：
* 尽量使用华为官方文档中提到的建议版本，否则就有坑
* 华为鲲鹏论坛的活跃度不高，而且遇到了问题基本上没啥回复，全得靠自己


## 参考链接
* https://www.huaweicloud.com/kunpeng/
* https://stackoverflow.com/questions/31851611/differences-between-arm64-and-aarch64
* https://libvirt.org/pci-hotplug.html#aarch64-virt
* https://sourcegraph.com/github.com/openstack/nova/-/blob/nova/conf/libvirt.py