---
title: cgroups notification API demo
date: 2021-01-01 18:28:00
tags:
- Linux
- cgroups
---

## cgroups notification API demo


```go
package main

import (
        "flag"
        "fmt"
        "io/ioutil"
        "os"
        "path/filepath"

        "golang.org/x/sys/unix"
)

func main() {
        cgName := flag.String("cgName", "yiran", "cgroup path")
        flag.Parse()
        level := "critical"
        cgDir := filepath.Join("/sys/fs/cgroup/memory/", *cgName)
        evName := "memory.pressure_level"
        fmt.Printf("cgroup name is: %s\n", *cgName)
        fmt.Printf("cgroup path is: %s\n", cgDir)
        fmt.Printf("cgroup event name is: %s\n", evName)

        evFile, err := os.Open(filepath.Join(cgDir, evName))
        if err != nil {
                panic(err)
        }
        fd, err := unix.Eventfd(0, unix.EFD_CLOEXEC)
        if err != nil {
                evFile.Close()
                panic(err)
        }

        eventfd := os.NewFile(uintptr(fd), "eventfd")

        eventControlPath := filepath.Join(cgDir, "cgroup.event_control")
        data := fmt.Sprintf("%d %d %s", eventfd.Fd(), evFile.Fd(), level)
        if err := ioutil.WriteFile(eventControlPath, []byte(data), 0700); err != nil {
                eventfd.Close()
                evFile.Close()
                panic(err)
        }
        defer func() {
                eventfd.Close()
                evFile.Close()
        }()

        buf := make([]byte, 8)
        for {
                fmt.Println("start...")
                if _, err := eventfd.Read(buf); err != nil {
                        panic(err)
                }
                if _, err := os.Lstat(eventControlPath); os.IsNotExist(err) {
                        panic(err)
                }
                fmt.Println("test success ...")
        }
}
```

准备 memory cgroup 配置，并限制内存上限：

```bash
go build /tmp/demo.go
mkdir /sys/fs/cgroup/memory/yiran/
echo 10M >  /sys/fs/cgroup/memory/yiran/memory.limit_in_bytes
echo $$ > /sys/fs/cgroup/memory/yiran/tasks
nohup /tmp/demo -cgName=yiran & 
dd if=/dev/zero | read x 
```

`tailf /tmp/nohup.out` 查看输出结果。


## 参考链接
* https://www.kernel.org/doc/Documentation/cgroup-v1/memory.txt