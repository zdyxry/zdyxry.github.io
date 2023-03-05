---
title: 2020 第21周 LeetCode 记录
date: 2020-05-22 22:28:29
tags:
- LeetCode
---

### 1446. Consecutive Characters

判断最长连续相同字符的长度，记录下当前字母，然后比较与 flag 是否相同，如果相同则 +1，不相同则重置为 1。

也可以通过 itertools.groupby 来实现（新学习的。。）

```python
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        tmp = s[0]
        cnt = 1
        max_cnt = 0
        for i in s[1:]:
            if i == tmp:
                cnt += 1
            else:
                tmp = i
                cnt = 1
            max_cnt = max(max_cnt, cnt)
        return max_cnt
```


### 1447. Simplified Fractions

遍历分子与分母，求最大公约数，如果最大公约数为1，则将结果保存下来。分母从 2 开始计算。

```go
func simplifiedFractions(n int) []string {
    ret := []string{}
    for i := 2; i <= n; i++ {
        for j := 1; j < i; j++ {
            if gcd(i, j) == 1 {
                ret = append(ret, fmt.Sprintf("%d/%d", j, i))
            }
        }
    }
    return ret
}

func gcd(x, y int) int {
    for x%y != 0 {
        x, y = y, x%y
    }
    return y
}
```


### 1448. Count Good Nodes in Binary Tree

遍历所有节点，记录 root 节点到当前节点经过的最大值，当前节点数值与最大值进行比较，如果符合条件，则结果 +1。


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, curmax):
            if not node:
                return 
            if node.val >= curmax:
                self.res += 1
            curmax = max(curmax, node.val)
            if node.left:
                dfs(node.left, curmax)
            if node.right:
                dfs(node.right, curmax)
            
        dfs(root, -float('inf'))
        return self.res
```

### 1450. Number of Students Doing Homework at a Given Time

遍历开始时间和结束时间，判断查询时间是否在两者之间。

```python
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(a<=queryTime<=b for a,b in zip(startTime,endTime))
```


### 896. Monotonic Array

遍历数组，记录前一个数字与当前数字的差值，判断是否单调递增或递减。

```python
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        cnt_inc = 0; cnt_dec = 0
        for i, v in enumerate(A):
            if i == 0: prev = v; continue
            if   v > prev: cnt_inc += 1
            elif v < prev: cnt_dec += 1
            if cnt_inc and cnt_dec: return False
            prev = v
        return True
```