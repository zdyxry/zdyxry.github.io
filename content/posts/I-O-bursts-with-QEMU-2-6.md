---
title: I/O bursts with QEMU 2.6
date: 2017-11-16 22:34:48
tags:
- qemu
---

I/O bursts with QEMU 2.6

近期在工作中要进行存储系统的 QOS 验证.公司 QOS 的实现方式参考了 QEMU 中的实现方式, 找来相关资料学习一下.


### 基本配置


首先,我将总结 QEMU 早期版本中已有的基本配置.
磁盘 I/O 有两处可以被限制的方式:  每秒钟字节数(bps) 和 每秒钟操作数( IOPS) . 对于它们中的每一种限制,用户既可以进行全局配置,也可以针对读写进行单独限制. 下面列举了总共 6 个不同的参数.
I/O 限制可以使用 -dirve 参数中的 throttling ,或者使用 QMP 中的 blocks_set_io_throttle 命令. 下面是两种情况下的参数列举:  

```
{
-DRIVE               	BLOCK_SET_IO_THROTTLE
throttling.iops-total	iops                 
throttling.iops-read 	iops_rd              
throttling.iops-write	iops_wr              
throttling.bps-total 	bps                  
throttling.bps-read  	bps_rd               
throttling.bps-write 	bps_wr               
}
```

可以同时配置 IOPS 和 bps ,针对不同的场景我们可以选择是否配置读写限制,但是如果设置了 iops-total 参数, 那么不能配置 iops-read 和 iops-write. 这个规则同样适用于 bps-total 和 bps-read/write.      
这些参数的默认值都是 0 , 表示没有任何限制.  `-drive file=hd0.qcow2,throttling.iops-total=100`
最基本的用法,用户可以为 QEMU 添加一个驱动用于限制 100 IOPS : `-drive filehd0.qcow2,throttling.iops-total=100` 


我们可以使用 QMP 达到相同的配置. 在这种情况下,所有的参数都是必须配置的, 所有我们必须给无关参数配置为 0 ,参考配置:   
```
{ "execute": "block_set_io_throttle",
  "arguments": {
     "device": "virtio0",
     "iops": 100,
     "iops_rd": 0,
     "iops_wr": 0,
     "bps": 0,
     "bps_rd": 0,
     "bps_wr": 0
  }
}
```


### 突发I/O


在刚刚的基本配置中, 我们已经能够预防虚拟机抢占过多 I/O 资源, 偶尔允许用户超出参数限制范围可能会更有用. 通过这种方式, 我们能够拥有一个响应更快的虚拟机,用于应对更多的波峰情况,同时保持其他时间的平均限制.
从 QEMU 2.6 开始, 可以允许用户在可配置的时间区间内进行突发 I/O. 突发 I/O 可以超过基本配置, 有两个参数可以限制他们: 突发 I/O 长度和最大允许 I/O 数量. 这两个参数可以作用于上述基本配置中的每一个参数, 这里使用 iops-total  进行举例.    
突发 I/O 限制使用 iops-total-max 进行配置, 最大长度(单位: s) 通过 iops-total-max-length 进行配置. 如果我们想要配置一个驱动器基本配置 IOPS 为 100, 同时允许在 60s 时间区间内发生突发 I/O IOPS 为2000. 可以使用如下配置:   

```
{
-drive file=hd0.qcow2,
throttling.iops-total=100,
throttling.iops-total-max=2000,
throttling.iops-total-max-length=60
}
```

或者通过 QMP 进行配置:   

```
{"execute":"block_set_io_throttle",
 "arguments":{
   "device":"virtio0",
   "iops":100,
   "iops_rd":0,
   "iops_wr":0,
   "bps":0
   "bps_rd":0
   "bps_wr":0
   "iops_max":2000,
   "iops_max_length":60,
 }}
```
    
通过这种方式, 用户可以控制 hd0.qcow2 以 2000 IOPS 持续 1分钟运行, 然后被限制在基本配置的 100 IOPS 状态.
如果有有足够的时间没有使用 I/O, 用户可以再次进行突发 I/O.   
iops-total-max 默认值为 0 ,表示不允许突发 I/O.  iops-total-max-length 只能在配置 iops-total-max的前提下进行配置, 默认值为 1秒.

### 控制 I/O 块大小

当配置 IOPS 限制时, 所有的 I/O 操作都会被平等对待,不论 I/O 块大小. 这意味着用户可以利用这点来规避 I/O 限制,将一些小 I/O 替换为一个大块 I/O.
QEMU 提供了 throttling.iops-size  配置用来防止这种情况发生. 这个设置指定请求的每个 I/O 大小.过大的请求将会进行相应的统计. 
比如, 如果 iops-size 设置为 4096, 那么 8KB 的 I/O 请求将会被记为 2 ,6KB 请求记为1.5. 该配置只作用于大于 iops-size 配置的 I/O 请求, 如果 I/O 请求小于该数值,则不论大小均记为 1. 
iops-size默认值为 0 ,表示这个默认的 IOPS 限制不考虑每次 I/O 请求的块大小. 

### I/O 限制在磁盘组的应用

在刚刚的例子中我们已经看到如何去限制 I/O 在各个驱动器上, 但是 QEMU 同时允许将驱动器进行分组, 这样驱动器组具有相同的 I/O 限制. 
这个功能在 QEMU 2.4 版本已经生效, 更多信息可以参考其他文档. 

### Leaky Bucket 算法

QEMU 中的 I/O 限制使用 Leaky Bucket 算法实现.

该算法使用不断漏水的桶进行类比. 入水口比作在进行的 I/O, 当桶处于满状态时, 不再允许 I/O 下发. 
想要查看 QEMU 中的 I/O 限制对应方式,可以参考如下数值:   

    iops-total=100
    iops-total-max=2000
    iops-total-max-length=60

    - 水以 100 IOPS 的速度从桶中漏出
    - 水可以以 2000 IOPS 的速度添加到桶中
    - 桶的大小为 2000 * 60 = 120000
    - 如果 iops-total-max 没有配置, 那么桶的大小是 100

最初, 桶状态为空, 可以向桶中添加水直到 2000 IOPS 速率满为止. 当桶满了后, 我们只能添加更可能多的水,因为桶在加水的同时也在漏水. 此时 I/O 速率下降至 100 IOPS. 如果我们添加的水少于泄露的水,那么我们可以再次进行突发 I/O.  
注意, 在突发 I/O 期间,水从桶中泄露, 也需要超过 60s 的时间以 2000 IOPS 的速率填满. 当 60s 过后, 桶将泄露 100*60=6000 的水, 能够允许突发 I/O 再运行 3s.
而且, 由于算法的工作方式, 长时间的突发 I/O 也可以通过较低的 I/O 速率完成,比如 120s 内以 1000 IOPS 完成.

