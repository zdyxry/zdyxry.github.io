---
title: 2020 第23周 LeetCode 记录
date: 2020-06-06 13:25:41
tags:
- LeetCode
---

### 1460. Make Two Arrays Equal by Reversing Sub-arrays


比较两个列表是否可以通过翻转等价，统计列表中字母出现的次数判断，或者可以直接排序判断。


```python
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c = collections.Counter(target)
        for a in arr:
            c[a] -= 1
            if c[a] < 0:
                return False
        return True    

```


### 1464. Maximum Product of Two Elements in an Array

找到数组中最大的两个数字，分别将其数值 -1 然后相乘返回。可以直接升序排序后取最后两个数字。

```go
func maxProduct(nums []int) int {
    max:=0
    secondMax:=0
    for i:=0;i<len(nums);i++{
        e:=nums[i]
        if e>max{
            secondMax = max
            max = e
        }else if e>secondMax{
            secondMax = e
        }
    }
    return (max-1)*(secondMax-1)
}
```


### 1461. Check If a String Contains All Binary Codes of Size K

s 字符串中只包含0或1，滑动窗口计算 s 所有长度为 k 的组合，使用 set 去重，与 K 个数字的二进制字符串数量相比较，是否相等。

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        m = set()
        for i in range(len(s)-k+1):
            m.add(s[i:i+k])
        return len(m) == (1 << k)
```

### 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

分别对两个数组进行排序切割，找到两个元素之间间隔最大的数值，然后将其相乘为最终所求面积大小，对 `1e9 +7` 取余。

```go
func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
    maxH, maxV := 0, 0
	pre := 0
	sort.Ints(horizontalCuts)
	sort.Ints(verticalCuts)
	for i := 0; i < len(horizontalCuts); i++ {
		maxH = max(maxH, horizontalCuts[i] - pre)
		pre = horizontalCuts[i]
	}
	maxH = max(maxH, h - pre)
	pre = 0
	for i := 0; i < len(verticalCuts); i++ {
		maxV = max(maxV, verticalCuts[i] - pre)
		pre = verticalCuts[i]
	}
	maxV = max(maxV, w - pre)
	return (maxH * maxV) % 1000000007
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
```


### 1466. Reorder Routes to Make All Paths Lead to the City Zero

遍历 connections ，统计每个节点之间相邻的节点，使用 dfs 从 0 开始计算，当相邻节点已经访问过了，直接跳过，如果没有访问过，且相邻节点到当前节点方向不对，那么就将结果 +1，并将其添加到访问过的集合中，继续dfs 相邻节点。


```python
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = { (a,b) for a, b in connections } # instantly check if a->b
        neighbors = { i:[] for i in range(n)}     # adjacent cities
        visit = set()                             # visit each city once
        changes = 0
        
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        # dfs from City 0, count outgoing edges
        def dfs(city):
            nonlocal edges, neighbors, visit, changes
            
            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                # neighbor can't reach city
                if (neighbor, city) not in edges:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)
        
        visit.add(0)
        dfs(0)
        return changes
```