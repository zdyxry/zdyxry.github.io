---
title: 如何捕捉 Ctrl+C 指令
date: 2019-11-23 21:23:24
tags:
- Python
- Golang
---

## 背景

有时候在运行代码的时候，想要程序在接收到 Ctrl+C 指令的时候做一些平滑的处理，来写一下在 Python 和 Golang 中如何接收 Ctrl+C 指令。

## Python

```python
import signal
import time
import sys


def run_program():
    while True:
        print("Test code...")
        time.sleep(1)


def exit_gracefully(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)
    print("Receive Ctrl+C.")
    sys.exit(1)


if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    run_program()
```


## Golang

```golang
package main

import (
	"fmt"
	"os"
	"os/signal"
	"sync"
	"time"
)

func WaitForCtrlC() {
	var end_waiter sync.WaitGroup
	end_waiter.Add(1)
	var signal_channel chan os.Signal
	signal_channel = make(chan os.Signal, 1)
	signal.Notify(signal_channel, os.Interrupt)
	go func() {
		<-signal_channel
		end_waiter.Done()
	}()
	end_waiter.Wait()
}

func testCode() {
	for {
		fmt.Println("Test code...")
		time.Sleep(time.Duration(1) * time.Second)
	}
}

func main() {
	fmt.Printf("Press Ctrl+C to end\n")
	go testCode()
	WaitForCtrlC()
	fmt.Printf("Receive Ctrl+C.\n")
}
```