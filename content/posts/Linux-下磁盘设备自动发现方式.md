---
title: Linux 下磁盘设备自动发现方式
date: 2019-08-02 23:10:04
tags:
- Linux
- Golang
---

## 背景

如果在 PC 上安装过 Linux，那么通常会遇到过硬件设备无法发现的问题，这类问题最终都可以通过 google 来解决掉。那么当我们在服务器场景下，如何做到设备自动发现且在设备发现后执行某些动作呢？

最近看了几个关于存储系统的 Operator 部分实现，记录一下。

## 命令行

最简单的肯定是我们写一个循环，永远检测我们要发现的设备，比如 lsblk 可以列举当前服务器所有 block 设备，那么我们就在循环内部执行 lsblk，diff 每次执行的结果，如果有新的设备，那么执行某些操作。

lsblk 是通过读取 /sys/block 下的具体目录判断的，那么我么也可以直接读取该路径下的目录来实现。

如果是网络设备也是一样，我们可以在循环内部执行 `ip link list` 来获取所有网络设备。



## UDEV

照常先引用维基百科的解释：

> udev 是Linux kernel 2.6系列的设备管理器。它主要的功能是管理/dev目錄底下的设备节点。它同时也是用来接替devfs及hotplug的功能，这意味着它要在添加/删除硬件时处理/dev目录以及所有用户空间的行为，包括加载firmware时。

如果你的 OS 是通过 systemd 来管理所有进程的话，那么可以发现一个服务叫做 `systemd-udevd` ，这个是 udev 的守护进程:

```bash
[root@node90 19:58:10 ~]$systemctl status systemd-udevd
● systemd-udevd.service - udev Kernel Device Manager
   Loaded: loaded (/usr/lib/systemd/system/systemd-udevd.service; static; vendor preset: disabled)
   Active: active (running) since Fri 2019-06-14 15:25:55 CST; 1 months 18 days ago
     Docs: man:systemd-udevd.service(8)
           man:udev(7)
 Main PID: 698 (systemd-udevd)
   Status: "Processing with 56 children at max"
    Tasks: 1
   Memory: 24.0M
   CGroup: /system.slice/systemd-udevd.service
           └─698 /usr/lib/systemd/systemd-udevd

Aug 02 10:29:17 node90 python[4395]: detected unhandled Python exception in '/usr/lib/python2.7/site-packages/cpuinfo/cpuinfo.py'
Aug 02 10:29:17 node90 python[4395]: can't communicate with ABRT daemon, is it running? [Errno 2] No such file or directory
Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.
```



udev 可以让我们对硬件的使用限制大大减少，除了常见的硬件发现，还有一个场景就是网卡改名，比如 82599 网卡，在 CentOS 上大概率识别为 `enp4s0f1` 之类的网卡名，如果我们想要统一服务器网卡名称，那么我们可以通过设置 udev 规则，匹配 mac 地址来做到，这里不细说。

我们来说说 udev 自动发现设备。udev 提供了完整的工具集，可以共我们使用，比如 udevadm：

```bash
[root@node 20:02:41 ~]$udevadm --help
udevadm [--help] [--version] [--debug] COMMAND [COMMAND OPTIONS]

Send control commands or test the device manager.

Commands:
  info          Query sysfs or the udev database
  trigger       Request events from the kernel
  settle        Wait for pending udev events
  control       Control the udev daemon
  monitor       Listen to kernel and udev events
  test          Test an event run
  test-builtin  Test a built-in command
```

我们可以通过 udevadm 来查看硬件设备的具体信息，也可以通过 udevadm 来进行显示的设备监控。

除了通过 udevadm 命令，我们还可以通过编写 udev 配置文件来实现设备发现后的具体动作，在 `/etc/udev/rules.d/` 路径下可以防止我们自己的配置文件。

比如我们想实现功能：节点上插入磁盘后，执行某条命令，那么我们可以这么定义：

```bash
[root@node90 20:05:21 rules.d]$pwd
/etc/udev/rules.d
[root@node 20:06:29 rules.d]$cat 98-disk-udev.rules 
KERNEL=="sd[a-z]", SUBSYSTEM=="block", ACTION=="add", RUN+="echo add"

KERNEL=="sd[a-z]", SUBSYSTEM=="block", ACTION=="remove", RUN+="echo remove"
```

这个规则具体含义为：

* 当检测到设备 `sd[a-z]` , 类型为 `block`且动作为 `add` ，那么执行 `echo add` 操作。

* 当检测到设备 `sd[a-z]` ，类型为 `block`且动作为 `remove` ，那么执行 `echo add` 操作。


我们来看一个具体的例子，执行 `udevadm monito` 来监控节点设备，然后插入一块 scsi 磁盘：

```bash
[root@node 20:14:04 rules.d]$udevadm monitor
monitor will print the received events for:
UDEV - the event which udev sends out after rule processing
KERNEL - the kernel uevent
KERNEL[4250923.838205] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0 (scsi)
KERNEL[4250923.838232] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0 (scsi)
KERNEL[4250923.838241] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0/scsi_disk/6:0:0:0 (scsi_disk)
KERNEL[4250923.838248] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0/scsi_device/6:0:0:0 (scsi_device)
KERNEL[4250923.838344] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0/scsi_generic/sg6 (scsi_generic)
KERNEL[4250923.838355] add      /devices/virtual/bdi/8:96 (bdi)
KERNEL[4250923.838364] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0/bsg/6:0:0:0 (bsg)
UDEV  [4250923.844166] add      /devices/virtual/bdi/8:96 (bdi)
UDEV  [4250923.844180] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0 (scsi)
UDEV  [4250923.844189] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0 (scsi)
UDEV  [4250923.844196] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0/scsi_device/6:0:0:0 (scsi_device)
UDEV  [4250923.844203] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0/scsi_disk/6:0:0:0 (scsi_disk)
UDEV  [4250923.848018] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0/scsi_generic/sg6 (scsi_generic)
UDEV  [4250923.851041] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0/bsg/6:0:0:0 (bsg)
KERNEL[4250923.882845] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0/block/sdg (block)
KERNEL[4250923.882863] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0/block/sdg/sdg1 (block)
UDEV  [4250928.290659] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0/block/sdg (block)
UDEV  [4250928.379634] add      /devices/pci0000:00/0000:00:1f.2/ata6/host6/target6:0:0/6:0:0:0/block/sdg/sdg1 (block)
```

可以看到 udev 监控到了设备名称，设备 pci id 以及设备触发的动作，这里与我们定义的规则相对应。


## 具体使用

### 命令行

在 OpenShift 的 local storage operator 中，是通过不断的执行 lsblk 比较结果来判断的，相关代码如下：

```go
// Run and create disk config
func (d *DiskMaker) Run(stop <-chan struct{}) {
	ticker := time.NewTicker(checkDuration)
	defer ticker.Stop()

	err := os.MkdirAll(d.symlinkLocation, 0755)
	if err != nil {
		klog.Errorf("error creating local-storage directory %s: %v", d.symlinkLocation, err)
		os.Exit(-1)
	}

	for {
		select {
		case <-ticker.C:
			diskConfig, err := d.loadConfig()
			if err != nil {
				klog.Errorf("error loading configuration: %v", err)
				break
			}
			d.symLinkDisks(diskConfig)
		case <-stop:
			klog.Infof("exiting, received message on stop channel")
			os.Exit(0)
		}
	}
}

func (d *DiskMaker) symLinkDisks(diskConfig *DiskConfig) {
	cmd := exec.Command("lsblk", "--list", "-o", "NAME,MOUNTPOINT", "--noheadings")
	var out bytes.Buffer
	var err error
	cmd.Stdout = &out
	err = cmd.Run()
	if err != nil {
		msg := fmt.Sprintf("error running lsblk: %v", err)
		e := newEvent(ErrorRunningBlockList, msg, "")
		d.eventSync.report(e, d.localVolume)
		klog.Errorf(msg)
		return
	}
	deviceSet, err := d.findNewDisks(out.String())
	if err != nil {
		msg := fmt.Sprintf("error reading blocklist: %v", err)
		e := newEvent(ErrorReadingBlockList, msg, "")
		d.eventSync.report(e, d.localVolume)
		klog.Errorf(msg)
		return
	}

	if len(deviceSet) == 0 {
		klog.V(3).Infof("unable to find any new disks")
		return
	}
	...
```



### UDEV

在 Rook 项目中，除了通过 lsblk 来获取设备，还监控了 udev 规则，具体代码如下：

```go

// Scans `udevadm monitor` output for block sub-system events. Each line of
// output matching a set of substrings is sent to the provided channel. An event
// is returned if it passes any matches tests, and passes all exclusion tests.
func rawUdevBlockMonitor(c chan string, matches, exclusions []string) {
	defer close(c)

	// stdbuf -oL performs line bufferred output
	// 后台执行 udevadm monitor 命令
	cmd := exec.Command("stdbuf", "-oL", "udevadm", "monitor", "-u", "-k", "-s", "block")
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		logger.Warningf("Cannot open udevadm stdout: %v", err)
		return
	}

	err = cmd.Start()
	if err != nil {
		logger.Warningf("Cannot start udevadm monitoring: %v", err)
		return
	}

    // 通过 bufio.NewScanner 实时获取 udevadm monitor 命令输出结果
	scanner := bufio.NewScanner(stdout)
	for scanner.Scan() {
		text := scanner.Text()
		logger.Debugf("udevadm monitor: %s", text)
		// 对输出结果进行正则匹配
		match, err := matchUdevEvent(text, matches, exclusions)
		if err != nil {
			logger.Warningf("udevadm filtering failed: %v", err)
			return
		}
		if match {
		    // 若匹配成功，则将结果发送到对应 channel，即 events
			c <- text
		}
	}

	if err := scanner.Err(); err != nil {
		logger.Warningf("udevadm monitor scanner error: %v", err)
	}

	logger.Info("udevadm monitor finished")
}

// Monitors udev for block device changes, and collapses these events such that
// only one event is emitted per period in order to deal with flapping.
func udevBlockMonitor(c chan string, period time.Duration) {
	defer close(c)

	// return any add or remove events, but none that match device mapper
	// events. string matching is case-insensitve
	// 定义 events channel，用于传输匹配结果
	events := make(chan string)
	go rawUdevBlockMonitor(events,
	    // 正则表达式，用于获取设备名称
		[]string{"(?i)add", "(?i)remove"},
		[]string{"(?i)dm-[0-9]+", "(?i)rbd[0-9]+"})

	for {
	    // 死循环，不断从 events channel 中获取匹配后的结果
		event, ok := <-events
		if !ok {
			return
		}
		timeout := time.NewTimer(period)
		for {
		    // 这里如果在 timeout 时间周期内，出现多次 events，貌似会丢弃掉后续 event 信息，不知道出于什么考虑。。
			select {
			case <-timeout.C:
				break
			case _, ok := <-events:
				if !ok {
					return
				}
				continue
			}
			break
		}
		c <- event
	}
}
```

## 参考链接

* http://www.reactivated.net/writing_udev_rules.html 
* https://www.thegeekdiary.com/beginners-guide-to-udev-in-linux/