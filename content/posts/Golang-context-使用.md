---
title: Golang context 使用
date: 2019-09-30 18:33:32
tags:
- Golang
---

## 背景

前段时间在写 Cluster API Provider 的时候，经常会使用 context 传递参数，当时只是按照其他项目中的方式快速的实现，并没有认真的了解 context 具体包含什么，为了解决什么问题，这次来聊一下。

P.S. 虽然写了一周的 Golang，但是对于标准库有什么还一无所知，找时间应该认真过一遍的。。


## 定义与使用

先看定义：

> Package context defines the Context type, which carries deadlines, cancellation signals, and other request-scoped values across API boundaries and between processes.

* 当一个 goroutine 调用其他 goroutine，随着层级变多，我们想要在外层达到控制的效果
* 在必要场景下传递 **必需** 的数据

其中 `Context` 这个 interface 中定义了 4 个方法，具体如下：

```go
type Context interface {
	Deadline() (deadline time.Time, ok bool)
	Done() <-chan struct{}
	Err() error
	Value(key interface{}) interface{}
}
```

在 `context` 包中实现了4个函数，平时也都是使用这些函数：
1. func WithCancel(parent Context) (ctx Context, cancel CancelFunc) 
2. func WithDeadline(parent Context, d time.Time) (Context, CancelFunc)
3. func WithTimeout(parent Context, timeout time.Duration) (Context, CancelFunc)
4. func WithValue(parent Context, key, val interface{}) Context

可以看到 Cancel,Deadline,Timeout 都会返回一个 CancelFunc 函数，哪怕我们设定的时间还没到，我们也可以直接使用 CancelFunc 去设置 Context。


在 context 使用上有官方文档，且有很多博主已经写过很详细的博客，这里只是列一个简单的例子：

```go
package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	// Pass a context with a timeout to tell a blocking function that it
	// should abandon its work after the timeout elapses.
	ctx, cancel := context.WithTimeout(context.Background(), 200*time.Millisecond)
	defer cancel()

	select {
	case <-time.After(1 * time.Second): // 等待 1s
		fmt.Println("overslept")
	case <-ctx.Done():  // 只有当 Channel 关闭时才会返回非空，也就是到了设定的 Timeout 数值
		fmt.Println(ctx.Err()) // prints "context deadline exceeded"
	}

}

```


## 注意事项

1. 不要把 Context 放到结构体中，以参数传递，在作为参数传递时，需要将其作为第一个参数传递
2. 如果 Context 传递内容不确定，那么可以传递 `context.Background()` 或 `context.TODO()`，不要传递 nil
3. 不建议使用 `context.Value` 传递数据
4. Context 是通过 **通知** 来达到 **控制** 目的
5. Context 并非是全局的，只查询自身及父context 的数据，同理在 Cancel 也是一样的

## （可能存在的）问题

在搜索过程中，看到[一篇博客](https://faiface.github.io/post/context-should-go-away-go2/)提到了 context 的一些问题：

* 传播性
    * 当我们有一个包含了100个函数的调用栈，当我们想要通过 context 来达到控制目的时，那么我们需要将 context 作为函数的第一个参数不断的传递下去。
* 什么时候使用 `context.TODO` ？
* context.Value 不该用
    * 非静态的
    * 需要在指定功能上使用特定的 key/value
    * 容易发生 key 冲突
* 效率低下
* ...


## 总结

虽然上面说了那么多，比如上面提到的不应该用 `context.Value` ，在 ClusterAPI 中有很多使用 `context.Value` 传值的地方，该用还是用嘛。


## 参考链接

* https://golang.org/pkg/context/#Background
* https://www.flysnow.org/2017/05/12/go-in-action-go-context.html
* https://deepzz.com/post/golang-context-package-notes.html
* https://zhuanlan.zhihu.com/p/34417106
* http://imfox.io/2017/11/28/go-context-note/
* https://faiface.github.io/post/context-should-go-away-go2/
