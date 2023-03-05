---
title: Heap In Python & Golang
date: 2019-07-28 12:11:45
tags:
- Python
- Golang
---


## 背景

最近使用到了 heap 这个数据结构，记录一下在 Python 和 Golang 中最基本的使用方法～ 

> 堆（英语：Heap）是计算机科学中的一種特別的樹狀数据结构。若是滿足以下特性，即可稱為堆積：「給定堆積中任意節點P和C，若P是C的母節點，那麼P的值會小於等於（或大於等於）C的值」。若母節點的值恆小於等於子節點的值，此堆積稱為最小堆積（min heap）；反之，若母節點的值恆大於等於子節點的值，此堆積稱為最大堆積（max heap）。在堆積中最頂端的那一個節點，稱作根節點（root node），根節點本身沒有母節點（parent node）。

## Python

### create

```python 
In [1]: import heapq

In [2]: a = [1,3,2,5,4]

In [3]: heapq.heapify(a)

In [4]: a
Out[4]: [1, 3, 2, 5, 4]

In [5]: b = []

In [6]: heapq.heappu
heapq.heappush     heapq.heappushpop

In [6]: heapq.heappush(b, 1)

In [7]: heapq.heappush(b, 3)

In [8]: heapq.heappush(b, 2)

In [9]: heapq.heappush(b, 5)

In [10]: heapq.heappush(b, 4)

In [11]: b
Out[11]: [1, 3, 2, 5, 4]
```

### read

```python 
In [28]: b
Out[28]: [1, 3, 2, 5, 4]

In [29]: heapq.nlargest(3, b)
Out[29]: [5, 4, 3]

In [30]: heapq.nsmallest(2, b)
Out[30]: [1, 2]
```

### update

```python
In [32]: heapq.heappush(b, 6)

In [33]: b
Out[33]: [1, 3, 2, 5, 4, 6]

In [39]: heapq.heapreplace(b, 7)
Out[39]: 1

In [40]: b
Out[40]: [2, 3, 6, 5, 4, 6, 7]

In [41]: a = [6,8,7,9]

In [42]: heapq.heapify(a)

In [43]: b
Out[43]: [2, 3, 6, 5, 4, 6, 7]

In [45]: c = heapq.merge(a,b)

In [46]: list(c)
Out[46]: [2, 3, 6, 6, 5, 4, 6, 7, 8, 7, 9]
```

### delete

```python
In [50]: b
Out[50]: [2, 3, 6, 5, 4, 6, 7]

In [51]: heapq.heappop(b)
Out[51]: 2

In [52]: b
Out[52]: [3, 4, 6, 5, 7, 6]
```


## Golang

Golang 中没有 heapq 这种封装好的库可以直接使用，不过有 `container/heap` ，提供了同样的方法，只是我们需要先对我们的操作对象实现搜有的 `heap.Interface`  方法。


## Constructor

```go
// This example demonstrates an integer heap built using the heap interface.
package main

import (
	"container/heap"
	"fmt"
)

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

// 取最后一个元素，在 `container/heap.Pop` 中，将堆顶的元素放置在最后，然后调用 `container/heap.Down` 将当前堆顶元素下沉到适当位置。
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// // An IntHeap is a max-heap of ints.
type MaxHeap struct {
	IntHeap
}

func (h MaxHeap) Less(i, j int) bool { return h.IntHeap[i] > h.IntHeap[j] }

```


### create

```go
// This example demonstrates an integer heap built using the heap interface.
package main

import (
	"container/heap"
	"fmt"
)

// This example inserts several ints into an IntHeap, checks the minimum,
// and removes them in order of priority.
func main() {
	h := &IntHeap{2, 1, 5}
	heap.Init(h)
	heap.Push(h, 3)
	fmt.Printf("minimum: %d\n", (*h)[0])
	for h.Len() > 0 {
		fmt.Printf("%d ", heap.Pop(h))
	}
}
```


### read


```go
package main

import (
	"container/heap"
	"fmt"
)


func main() {
	h := &IntHeap{2, 1, 5}
	heap.Init(h)
	heap.Push(h, 3)
	fmt.Printf("minimum: %d\n", (*h)[0])
	for h.Len() > 0 {
		fmt.Printf("%d ", heap.Pop(h))
	}
	fmt.Println()

	h1 := &MaxHeap{[]int{2, 1, 5}}
	heap.Init(h1)
	heap.Push(h1, 3)
	fmt.Printf("maximum: %d\n", h1.IntHeap[0])
	for h1.Len() > 0 {
		fmt.Printf("%d ", heap.Pop(h1))
	}
	fmt.Println()

}

```

### update

```go
package main

import (
	"container/heap"
	"fmt"
)


func main() {
	h := &IntHeap{2, 1, 5}
	heap.Init(h)
	heap.Push(h, 3)
	for h.Len() > 0 {
		fmt.Printf("%d ", heap.Pop(h))
	}
	fmt.Println()

}

```

### delete 

```go
// This example demonstrates an integer heap built using the heap interface.
package main

import (
	"container/heap"
	"fmt"
)

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// This example inserts several ints into an IntHeap, checks the minimum,
// and removes them in order of priority.
func main() {
	h := &IntHeap{2, 1, 5}
	heap.Init(h)
	heap.Push(h, 3)
	fmt.Println(h)
	heap.Remove(h, 2)
	for h.Len() > 0 {
		fmt.Printf("%d ", heap.Pop(h))
	}
}

```


## 总结

Heap 的使用场景有：优先级队列、TopK 等等。

## 参考链接

* https://godoc.org/container/heap
* https://docs.python.org/3.7/library/heapq.html
* https://ieevee.com/tech/2018/01/29/go-heap.html
