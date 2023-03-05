---
title: 使用 init 进程运行 Container
date: 2022-03-05 15:10:39
tags:
- Linux
- Container
---



## 背景

关注过 Bare Metal 相关项目的同学应该都了解过系统的启动流程、如何快速的置备一台物理服务器等之类的实现方式，通常都需要运行一个 LiveOS 来实现某些动作。
在 Tinkerbell 项目中，使用 Linuxkit 来作为 LiveOS，Plunder 项目中使用 BOOTy 来作为 LiveOS。前几天 @thebsdbox 将 BOOTy 中的一部分抽离了出来，作为 ginit 展示主要的实现方式，可以更好的让我们理解安装环节中的具体细节。 今天来看一下这个项目。

如果安装一个 CentOS，那么通常是会通过 kernel + initramfs.img 启动，initramfs.img 中会包含 systemd 、anaconda、dracut 等一些列组件，然后通过 systemd 指定不同的 Target 所属/依赖/顺序来完成最终 Anaconda 调用。Anaconda 通过解析 `/proc/cmdline` 中的 KickStart 参数来决定自己的安装方式。

ginit 项目展示了以下内容：
* 制作 initramfs.img 
* 通过 Container image 制作一个 RAW image
* 通过 QEMU 使用 RAW image 和 Linux Kernel 来运行一个虚拟机
* ginit 自动运行 Container 中 entrypoint 指令

## 流程演示

### 通过 Container image 制作一个 RAW image 

RAW image 中最终不会包含 Kernel 部分，以 Nginx Container 为例。提取 nginx:latest image 中的 `Entrypoint` ，通过 `dd` 置备一个 RAW image，并格式化为 ext4 ，raw image 作为 loop 设备挂载到本地，通过 `docker export` 将 Nginx Image 拷贝到挂载点下，卸载挂载点，最终 RAW image 包含了 Nginx Container 的所有内容。这里的 RAW image 因为不包含 kernel，所以无法直接启动，只是作为后续动作的依赖。

Nginx Container 默认的 `Entrypoint` 是 `docker-entrypoint.sh` ，通过这个脚本来做一些参数检查动作。

```
#!/bin/bash

echo "Lets build you a disk image!"
docker pull $1
ENTRYPOINT=$(docker inspect -f '{{.Config.Entrypoint}}' $1 | sed 's/[][]//g')
echo "Creating a 200MB Disk"
dd if=/dev/zero of=disk.img bs=1024k count=200
mkfs.ext4 -F disk.img
mkdir -p /tmp/disk
mount -t ext4 -o loop disk.img /tmp/disk/
echo "Converting $1 to disk image"
docker create --name exporter $1 null
docker export exporter | tar xv -C /tmp/disk
docker rm exporter
umount /tmp/disk
echo The command $ENTRYPOINT will start this container
```

### 使用 ginit 制作 initramfs.img

静态编译 ginit；下载并编译 busybox ，将 ginit 编译结果 init 放置到 `/` 路径下，通过 cpio 将 busybox 归档，使用 gzip 进行压缩。所有流程完成后，将最终得到的 initramfs.cpio.gz 拷贝到项目路径下。 initramfs 最终包含的是 busybox + ginit 。


```
# syntax=docker/dockerfile:experimental


# Build ginit as an init
FROM golang:1.17-alpine as dev
RUN apk add --no-cache git ca-certificates gcc linux-headers musl-dev
COPY . /go/src/github.com/thebsdbox/ginit/
WORKDIR /go/src/github.com/thebsdbox/ginit
ENV GO111MODULE=on
RUN --mount=type=cache,sharing=locked,id=gomod,target=/go/pkg/mod/cache \
    --mount=type=cache,sharing=locked,id=goroot,target=/root/.cache/go-build \
    CGO_ENABLED=1 GOOS=linux go build -a -ldflags "-linkmode external -extldflags '-static' -s -w" -o init
    

# Build Busybox
FROM gcc:10.1.0 as Busybox
RUN apt-get update; apt-get install -y cpio
RUN curl -O https://busybox.net/downloads/busybox-1.31.1.tar.bz2
RUN tar -xf busybox*bz2
WORKDIR busybox-1.31.1
RUN make defconfig; make LDFLAGS=-static CONFIG_PREFIX=./initramfs install

WORKDIR initramfs 
COPY --from=dev /go/src/github.com/thebsdbox/ginit/init .

# Package initramfs
RUN find . -print0 | cpio --null -ov --format=newc > ../initramfs.cpio 
RUN gzip ../initramfs.cpio
RUN mv ../initramfs.cpio.gz /

FROM scratch
COPY --from=Busybox /initramfs.cpio.gz .
```

### 通过 QEMU 运行 Container 中的 EntryPoint 指令

到目前状态，我们得到了 initramfs.img ，得到了 raw image，但是还缺少 Linux Kernel 。可以直接从 Ubuntu 提供的 [netboot](http://archive.ubuntu.com/ubuntu/dists/focal-updates/main/installer-amd64/current/legacy-images/netboot/ubuntu-installer/amd64/) 下载 `boot executable bzImage` 文件。

现在所有的准备工作都进行完成了，我们可以直接通过 QEMU 来运行虚拟机，其中 Nginx 所需运行环境在 RAW Image 中，ginit 所需运行环境在 initramfs 中。

前面有提到，Nginx Container 默认的 `Entrypoint` 是 `docker-entrypoint.sh`，用来做一些参数包装，所以这里我将参数改为了 `/usr/sbin/nginx` ：

```
qemu-system-x86_64 -nographic \
  -kernel ./linux \
  -append "entrypoint=/usr/sbin/nginx root=/dev/sda console=ttyS0" \
  -initrd ./initramfs.cpio.gz \
  -hda ./disk.img \
  -m 1G
```

虚拟机 console 是 `ttyS0` ，通过终端运行可以直接查看启动日志：

```
...
[    1.469920] rtc_cmos 00:00: setting system clock to 2022-03-05T06:36:19 UTC (1646462179)
[    1.525397] ata1.00: ATA-7: QEMU HARDDISK, 2.5+, max UDMA/100
[    1.525579] ata1.00: 409600 sectors, multi 16: LBA48 
[    1.532980] ata2.00: ATAPI: QEMU DVD-ROM, 2.5+, max UDMA/100
[    1.540741] scsi 0:0:0:0: Direct-Access     ATA      QEMU HARDDISK    2.5+ PQ: 0 ANSI: 5
[    1.545673] sd 0:0:0:0: [sda] 409600 512-byte logical blocks: (210 MB/200 MiB)
[    1.547063] sd 0:0:0:0: [sda] Write Protect is off
[    1.547515] sd 0:0:0:0: Attached scsi generic sg0 type 0
[    1.548188] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    1.550227] scsi 1:0:0:0: CD-ROM            QEMU     QEMU DVD-ROM     2.5+ PQ: 0 ANSI: 5
[    1.568178] sd 0:0:0:0: [sda] Attached SCSI disk
[    1.578345] sr 1:0:0:0: [sr0] scsi3-mmc drive: 4x/4x cd/rw xa/form2 tray
[    1.578736] cdrom: Uniform CD-ROM driver Revision: 3.20
[    1.582611] sr 1:0:0:0: Attached scsi generic sg1 type 5
[    1.595655] Freeing unused decrypted memory: 2040K
[    1.666044] Freeing unused kernel image memory: 2712K
[    1.666482] Write protecting the kernel read-only data: 22528k
[    1.669246] Freeing unused kernel image memory: 2008K
[    1.670507] Freeing unused kernel image memory: 1192K
[    1.742691] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.743002] Run /init as init process
INFO[0000] Folder created [dev] -> [/dev]          
INFO[0000] Folder created [proc] -> [/proc]        
INFO[0000] Folder created [sys] -> [/sys]          
INFO[0000] Folder created [tmp] -> [/tmp]          
INFO[0000] Mounted [dev] -> [/dev]                 
INFO[0000] Mounted [proc] -> [/proc]               
INFO[0000] Mounted [sys] -> [/sys]                 
INFO[0000] Mounted [tmp] -> [/tmp]                 
INFO[0000] Starting DHCP client                    
INFO[0000] Starting ginit                          
ERRO[0000] Error finding adapter [Link not found]  
[    2.209227] tsc: Refined TSC clocksource calibration: 2893.182 MHz
[    2.209573] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x29b41aa25d4, max_idle_ns: 440795325238 ns
[    2.209984] clocksource: Switched to clocksource tsc
INFO[0002] Beginning provisioning process          
ERRO[0002] route ip+net: no such network interface 
INFO[0002] Folder created [root] -> [/mnt]         
[    3.902861] random: fast init done
[    3.912319] EXT4-fs (sda): recovery complete
[    3.913757] EXT4-fs (sda): mounted filesystem with ordered data mode. Opts: (null)
[    3.914463] ext4 filesystem being mounted at /mnt supports timestamps until 2038 (0x7fffffff)
INFO[0002] Mounted [root] -> [/mnt]                
INFO[0002] Mounted [dev] -> [/mnt/dev]             
INFO[0002] Mounted [proc] -> [/mnt/proc]           
INFO[0002] Starting Shell                          
INFO[0002] Waiting for command to finish...        
/ # 
```

其中 `[    1.743002] Run /init as init process` 中的 `/init` 已经是我们上面编译的 `ginit` ，`ginit` 运行的日志输出为：

```
INFO[0000] Folder created [dev] -> [/dev]          
INFO[0000] Folder created [proc] -> [/proc]        
INFO[0000] Folder created [sys] -> [/sys]          
INFO[0000] Folder created [tmp] -> [/tmp]          
INFO[0000] Mounted [dev] -> [/dev]                 
INFO[0000] Mounted [proc] -> [/proc]               
INFO[0000] Mounted [sys] -> [/sys]                 
INFO[0000] Mounted [tmp] -> [/tmp]                 
INFO[0000] Starting DHCP client                    
INFO[0000] Starting ginit                          
ERRO[0000] Error finding adapter [Link not found]  
[    2.209227] tsc: Refined TSC clocksource calibration: 2893.182 MHz
[    2.209573] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x29b41aa25d4, max_idle_ns: 440795325238 ns
[    2.209984] clocksource: Switched to clocksource tsc
INFO[0002] Beginning provisioning process          
ERRO[0002] route ip+net: no such network interface 
INFO[0002] Folder created [root] -> [/mnt]         
[    3.902861] random: fast init done
[    3.912319] EXT4-fs (sda): recovery complete
[    3.913757] EXT4-fs (sda): mounted filesystem with ordered data mode. Opts: (null)
[    3.914463] ext4 filesystem being mounted at /mnt supports timestamps until 2038 (0x7fffffff)
INFO[0002] Mounted [root] -> [/mnt]                
INFO[0002] Mounted [dev] -> [/mnt/dev]             
INFO[0002] Mounted [proc] -> [/mnt/proc]           
INFO[0002] Starting Shell                          
INFO[0002] Waiting for command to finish...        
```

主要做了几件事情：创建必要的路径，创建对应的设备，启动一个 DHCP Client 来获取 IP 地址，挂载 RAW Image 到 /mnt 下，通过 `chroot` 运行 `entrypoint` 参数中指定的程序，在这里是 `/usr/sbin/nginx` ，最终提供一个 Shell 环境给用户。我们可以通过 `ps` 命令查看当前所运行的进程：

```
/ # ps -ef |grep -v '\['
PID   USER     TIME  COMMAND
    1 0         0:01 /init
  178 0         0:00 nginx: master process /usr/sbin/nginx
  179 0         0:00 /bin/sh
  180 101       0:00 nginx: worker process
  193 0         0:00 ps -ef
/ # df 
Filesystem           1K-blocks      Used Available Use% Mounted on
devtmpfs                497020         4    497016   0% /dev
tmpfs                   502392         0    502392   0% /tmp
/dev/sda                181984    150940     16708  90% /mnt
devtmpfs                497020         4    497016   0% /mnt/dev
/ # ls /mnt/docker-entrypoint.sh 
/mnt/docker-entrypoint.sh
/ # ls /mnt/usr/sbin/nginx
/mnt/usr/sbin/nginx
/ # ls -hl /init
-rwxr-xr-x    1 0        0           3.4M Mar  5 04:20 /init
```

现在我们已经将一个 Container Image 中要运行的指令，通过 Linux kernel 配合 initramfs 来运行了起来，在 Bare Metal 场景下，我们可以将 Nginx 内置到 initramfs 中，将 Nginx 替换为 Docker 或者 Container 然后暴露出去，物理服务器作为 Docker Server，置备服务器作为 Docker Client 连接物理服务器进行指定容器的运行，最终完成物理服务器 OS 的安装，这也是目前 TinkerBell 的实现方式。


## ginit 具体实现

### 创建系统设备并挂载

在 `DefaultMounts` 和 `DefaultDevices` 中定义了一些必须的设备如 `/dev/null`, `/dev/random`, `/dev/urandom` ，和挂载点，如 `/dev`,`/proc`, `/tmp`, `/sys` 。


```
urandom := Device{
		CreateDevice: false,

		Name:  "urandom",
		Path:  "/dev/urandom",
		Mode:  syscall.S_IFCHR,
		Major: 1,
		Minor: 9,
	}
```


```
dev := Mount{
		CreateMount: false,
		EnableMount: false,
		Name:        "dev",
		Source:      "devtmpfs",
		Path:        "/dev",
		FSType:      "devtmpfs",
		Flags:       syscall.MS_MGC_VAL,
		Mode:        0777,
	}
	m.Mount = append(m.Mount, dev)
```


```
	//cmd.Execute()
	m := realm.DefaultMounts()
	d := realm.DefaultDevices()
	dev := m.GetMount("dev")
	dev.CreateMount = true
	dev.EnableMount = true

	proc := m.GetMount("proc")
	proc.CreateMount = true
	proc.EnableMount = true

	tmp := m.GetMount("tmp")
	tmp.CreateMount = true
	tmp.EnableMount = true

	sys := m.GetMount("sys")
	sys.CreateMount = true
	sys.EnableMount = true

	// Create all folders
	m.CreateFolder()
	// Ensure that /dev is mounted (first)
	m.MountNamed("dev", true)

	// Create all devices
	d.CreateDevice()

	// Mount any additional mounts
	m.MountAll()
```

在基本环境准备完成后，启动 DHCP Client，获取 IP 地址：

```
log.Println("Starting DHCP client")
	go realm.DHCPClient()

	// HERE IS WHERE THE MAIN CODE GOES
	log.Infoln("Starting ginit")
	time.Sleep(time.Second * 2)

	log.Infoln("Beginning provisioning process")

	mac, err := realm.GetMAC()
	if err != nil {
		log.Errorln(err)
		//realm.Shell()
	}
	fmt.Print(mac)
```

现在系统环境准备好了，网络也准备好了，那么可以运行具体的指令了，获取指令的方式是通过解析 `/proc/cmdline` ，`/proc/cmdline` 是通过我们在创建 VM 的时候通过 `--append` 传递的：

在解析到 `root` 和 `entrypoint` 参数值后，通过 `Mount` 将 `root` 挂载到对应的挂载点，通过 `chroot` 运行 `entrypoint`。

```
    stuffs, err := ParseCmdLine(CmdlinePath)
	if err != nil {
		log.Errorln(err)
	}
	_, err = realm.MountRootVolume(stuffs["root"])
	if err != nil {
		log.Errorf("Disk Error: [%v]", err)
	}

	cmd := exec.Command("/usr/sbin/chroot", []string{"/mnt", stuffs["entrypoint"]}...)
	cmd.Stdin, cmd.Stdout, cmd.Stderr = os.Stdin, os.Stdout, os.Stderr

	err = cmd.Start()
	if err != nil {
		log.Errorf("command error [%v]", err)
	}
	err = cmd.Wait()
	if err != nil {
		log.Errorf("error [%v]", err)
	}

	realm.Shell()
```

所有程序运行完成后，提供一个Shell 环境给用户：

```
// Shell will Start a userland shell
func Shell() {
	// Shell stuff
	log.Println("Starting Shell")

	// TTY hack to support ctrl+c
	cmd := exec.Command("/usr/bin/setsid", "cttyhack", "/bin/sh")
	cmd.Stdin, cmd.Stdout, cmd.Stderr = os.Stdin, os.Stdout, os.Stderr

	err := cmd.Start()
	if err != nil {
		log.Errorf("Shell error [%v]", err)
	}
	log.Printf("Waiting for command to finish...")
	err = cmd.Wait()
	if err != nil {
		log.Errorf("Shell error [%v]", err)
	}
}
```


## 总结

ginit 作为一个最小实现方便我们快速了解 init 具体做了什么，将 ginit 替换为 systemd 同理，但是直接看 systemd bootup 容易迷失在成堆的 Target 依赖中。在查找资料的过程中还看到了 https://github.com/QuentinPerez/busygox 做了类似的事情，可以作为参考。




## 参考链接
* https://github.com/thebsdbox/ginit
* https://unix.stackexchange.com/questions/146284/minimal-linux-with-kernel-and-busybox-etc-inittab-is-ignored-only-init-is-ex/147688#147688
* https://github.com/QuentinPerez/busygox
