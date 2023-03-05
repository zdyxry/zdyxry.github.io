---
title: 2020 第20周 LeetCode 记录
date: 2020-05-16 10:17:49
tags:
- LeetCode
---

### 1441. Build an Array With Stack Operations

遍历数组，比较当前值与目标值是否相同，如果相同，则在结果追加 `Push` ，如果不同，则追加 `Push`, `Pop` 。

```python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        keep = 0
        for num in range(1, n+1):
            res.append("Push")
            keep += 1
            if num not in target:
                res.append("Pop")
                keep -= 1
            if keep == len(target):
                break
        return res
```


### 1442. Count Triplets That Can Form Two Arrays of Equal XOR

求子数组中是否存在左侧部分异或值与右侧部分异或值相等的情况，a==b -> a ^ b = 0，也就是是否存在子数组所有元素异或值为0 的情况，如果存在，那么子数组所有的元素都可以符合条件。

```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return 0

        count = 0

        for i in range(len(arr)-1):
            temp = arr[i]
            for j in range(i+1, len(arr)):
                temp = temp^arr[j]
                if temp == 0:
                    count += j-i

        return count
```


### 1317. Convert Integer to the Sum of Two No-Zero Integers

从 1 开始遍历判断两个拆分数字是否包含 `0` ，判断对 10 取余是否为0 。

```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if self.check(i) and self.check(n - i):
                return [i, n - i]

    def check(self, n: int) -> bool:
        while n > 0:
            if n % 10 == 0:
                return False
            n //= 10
        return True
```

### 1443. Minimum Time to Collect All Apples in a Tree

通过字典来保证每条路径只走一次，判断子节点是否有苹果，如果没有，则将子节点从字典中删除，最终字典中保存的是必须要经过的节点，要走 2 次，所以需要 * 2 。

```python
class Solution:
    def minTime(self, n: int, edges: List[List[int]],
                hasApple: List[bool]) -> int:
        maps = collections.defaultdict(list)
        for e in edges:
            maps[e[0]].append(e[1])

        def dfs(i):
            selfOrChildHasApple = hasApple[i]
            for nex in maps[i]:
                selfOrChildHasApple |= dfs(nex)
            if not selfOrChildHasApple:
                del maps[i]
            return selfOrChildHasApple

        dfs(0)
        return max(0, 2 * (len(maps) - 1))
```

### 807. Max Increase to Keep City Skyline

分别找出每行、每列的最大值，然后遍历判断当前值距离两个最大值中的最小值需要增加多少，累加计算。


```python
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_cols = [max(col) for col in zip(*grid)]
        max_rows = [max(row) for row in grid]
        inc = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                inc += (min(max_cols[j], max_rows[i]) - grid[i][j])
        return inc
```