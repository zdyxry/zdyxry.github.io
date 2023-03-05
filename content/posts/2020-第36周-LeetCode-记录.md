---
title: 2020 第36周 LeetCode 记录
date: 2020-09-06 15:04:19
tags:
- LeetCode
---

### 1566. Detect Pattern of Length M Repeated K or More Times

判断数组中是否存在连续长度为 m 且重复次数为 k 的字符串，直接对 arr 进行切片判断。

```python
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        i = 0
        while i < len(arr):
            p = arr[i:i+m]
            if p * k == arr[i:i+m*k]:
                return True
            i += 1
        return False
```

### 1567. Maximum Length of Subarray With Positive Product

给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。使用数组记录数值为负数的索引值，当数字为 0 时则重置数组，当负数数量为偶数时，则更新最大值，最大值为当前索引减去第一个非 0 数字索引，如果负数数量为奇数时，则最大值为当前索引减去第一个负数索引。


```python
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pre=-1
        l=[]
        res=0
        for i,num in enumerate(nums):
            if num<0:
                l.append(i)
            elif num==0:
                l,pre = [],i
            if len(l)%2==0:
                res=max(res,i-pre)
            else:
                res = max(res,i-l[0])
        return res
```


### 1161. Maximum Level Sum of a Binary Tree


给一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推，找出层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。BFS 直接找，只是在找的过程中要记录层号以及该层的和，我直接用一个数组记录每层的和，然后数组的索引就是层级号，求最大值。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)

        result = [sum(i) for i in result]
        print(result)
        for idx, v in enumerate(result):
            if v == max(result):
                return idx+1

```


### 1219. Path with Maximum Gold

回溯法，每次递归计算下一个数值时，将当前数值置为 0，递归结束后重置该值，找到最大值。

```python
class Solution:
    def helper(self, grid, pos, m, n, count):
        (x, y) = pos
        if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] != 0:
            # print(pos)
            count += grid[x][y]
            temp = grid[x][y]
            grid[x][y] = 0
            self.helper(grid, (x-1, y), m, n, count)
            self.helper(grid, (x+1, y), m, n, count)
            self.helper(grid, (x, y-1), m, n, count)
            self.helper(grid, (x, y+1), m, n, count)
            grid[x][y] = temp
        self.res.append(count)

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                self.helper(grid, (i, j), m, n, 0)
        return max(self.res)
```


### 728. Self Dividing Numbers

python 可以直接将数字转换为字符串，继而转换为数组直接判断，不然的话就通过每次对 10 取余数，判断完后除 10。

```go
func isDividingNumbers(i int)bool{
	if i<10{
		return true
	}
	v:=i
	for i!=0{
		r :=i%10
		if r==0||v%r!=0{
			return false
		}
		i =i/10
	}
	return true
}
func selfDividingNumbers(left int, right int) []int {
	 var res []int
     for i:=left;i<=right;i++{
		 if isDividingNumbers(i){
		 	res = append(res,i)
		 }
	 }
	 return res
}


```