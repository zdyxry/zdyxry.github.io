---
title: 2020 第35周 LeetCode 记录
date: 2020-08-29 18:42:34
tags:
- LeetCode
---

### 1560. Most Visited Sector in a Circular Track

在中间走过多少圈，对于各个扇区来说是相同的，只需要考虑起点和终点的位置关系。

```python
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s, d = rounds[0], rounds[-1]
        if s <= d:
            return list(range(s, d+1))
        else:
            return list(range(1, d+1)) + list(range(s, n+1))
```


### 1557. Minimum Number of Vertices to Reach All Nodes

如果某个节点出现在到达节点，那么这个节点一定不在结果中，相反则一定在结果中。

```python
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n)) - set(e[1] for e in edges))
```

### 1558. Minimum Numbers of Function Calls to Make Target Array

一共有两种操作：1. 将某个索引位置的数值 +1； 2. 将所有数值 * 2 。
从结果上来说肯定是操作 2 效率更高，因为我们要求最小次数，所以我们想调用最多的操作 2。首先将判断数组中数字是否为奇数，如果是奇数的话就-1 并将结果 +1。执行完成后数组中所有数字都是偶数后，整体将数组中所有数字 /2 ，并将结果 +1。直到数组中所有数字都为 0。

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while any(nums):
            for i in range(len(nums)):
                if nums[i] % 2:
                    nums[i] -= 1
                    count += 1
            if any(nums):
                for i in range(len(nums)):
                    nums[i] //= 2
                count += 1
        return count
```


### 1561. Maximum Number of Coins You Can Get

```
每一轮中，你将会选出 任意 3 堆硬币（不一定连续）。
Alice 将会取走硬币数量最多的那一堆。
你将会取走硬币数量第二多的那一堆。
Bob 将会取走最后一堆。
重复这个过程，直到没有更多硬币。
```

虽然不可以选择最多的硬币，但是可以选择第二多的，所以可以先将数组排序，然后每次选择第二大的数字。

```python
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # 1,2,2,4,7,8 => 7,2
        # 1,2,3,4,5,6,7,8,9 => 8,6,4
        piles.sort(reverse=True)
        res = []
        i = 0
        while i < len(piles):
            if i % 2:
                i += 1
                continue
            i += 1    
            res.append(piles[i])
            if len(res) == len(piles) /3:
                return sum(res)
        return sum(res)
```


### 1079. Letter Tile Possibilities

使用 DFS + 回溯，先统计字母出现的次数，分别遍历 26 个字母，如果字母出现的次数不为 0 ，那么将字母出现的次数 -1 ，并进行 dfs，在深度搜索后再将字母次数 +1，避免影响最终结果。

```python
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        record = [0] * 26
        for tile in tiles: record[ord(tile)-ord('A')] += 1
        def dfs(record):
            s = 0
            for i in range(26):
                if not record[i]: continue
                record[i] -= 1
                s += dfs(record) + 1 
                record[i] += 1
            return s
        return dfs(record)
```