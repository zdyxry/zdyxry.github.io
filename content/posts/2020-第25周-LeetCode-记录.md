---
title: 2020 第25周 LeetCode 记录
date: 2020-06-20 06:53:40
tags:
- LeetCode
---

### 1476. Subrectangle Queries

二维数组的更新与查找。

```python
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle
        self.rows, self.cols = len(self.rect), len(self.rect[0])

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rect[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rect[row][col]



# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
```

### 1480. Running Sum of 1d Array

统计动态和，始终用一个变量记录当前值，遍历。

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        sum = 0
        for i in nums:
            sum += i
            res.append(sum)
        return res
```

### 1481. Least Number of Unique Integers after K Removals

对 arr 中出现数字的次数进行统计，并按照升序进行排序，遍历排序后的结果，如果 sum + elem_v 小于等于 k，那么表示此时还可以继续删除数字。


```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        res = dict(Counter(arr))
        res = sorted(res.items(),key=lambda item:item[1])
        sum = 0
        len_elem = len(res)
        for (elem_k,elem_v) in res:
            if sum + elem_v <= k:
                len_elem -=1
                sum += elem_v
            else:
                break
        return len_elem
```


### 1482. Minimum Number of Days to Make m Bouquets

对所有天数进行排序，使用二分法判断是否满足，其中判断是否可以组成k 朵花需要注意判断是否连续。

```python
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        def count(day: int):
            num = sums = 0
            for i in range(n):
                if num >= m:
                    break
                if bloomDay[i] <= day:
                    sums += 1
                else:
                    sums = 0
                if sums == k:
                    num += 1
                    sums = 0
            return num >= m
        days = sorted(set(bloomDay))
        l, r = 0, len(days)-1
        while l < r:
            mid = l + (r - l) // 2
            if count(days[mid]):
                r = mid
            else:
                l = mid + 1
        return days[l]
```


### 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

题目描述不清楚，我理解是 dfs ，只是传入的是两个 Tree，判断符合条件后直接返回另一个 Tree Node。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def traverse(original, cloned, target):
            if not original or not cloned:
                return None
            
            if original == target:
                return cloned
            
            return traverse(original.left, cloned.left, target) or \
                traverse(original.right, cloned.right, target)
        return traverse(original, cloned, target)
```