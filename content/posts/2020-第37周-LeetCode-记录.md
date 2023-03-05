---
title: 2020 第37周 LeetCode 记录
date: 2020-09-13 10:51:05
tags:
- LeetCode
---

### 1572. Matrix Diagonal Sum

对角线之和，需要注意当行为奇数和偶数时候的去重处理。

```python
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 1:
            return mat[0][0]
        ans = 0
        for i in range(n):
            if i != n-1-i:
                ans += mat[i][i]
                ans += mat[i][n-1-i]
            else:
                ans += mat[i][i]

        return ans
```


### 1576. Replace All ?'s to Avoid Consecutive Repeating Characters

题目中说的是不能出现连续相同的字符，整个字符串中是可以出现重复字符的，只需要遍历字符串，然后判断前后是否相同替换。

```python
class Solution:
    def modifyString(self, s: str) -> str:
        l = list(s)
        alphabet = list(string.ascii_lowercase)
        for i, _ in enumerate(l):
            if l[i] == "?":
                for j in alphabet:
                    if i == len(l) - 1:
                        if l[i-1] != j:
                            l[i] = j
                            break
                    elif l[i-1] != j and l[i+1] != j:
                        l[i] = j
                        break
        return ''.join(l)
```


### 1578. Minimum Deletion Cost to Avoid Repeating Letters

给一个字符串 s 和一个整数数组 cost ，其中 cost[i] 是从 s 中删除字符 i 的代价。返回使字符串任意相邻两个字母不相同的最小删除成本。如果当前字符与前一个字符相同，那么比较当前字符的价格与前一个字符的价格对比，取小；当前一个字符的价格比当前价格大时，那么此时更新 pre 为当前字符。

```python
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        pre = 0
        res = 0
        for idx in range(1, len(s)):
            if s[idx] == s[pre]:
                res += min(cost[idx], cost[pre])
            if s[idx] != s[pre] or cost[pre] < cost[idx]:
                pre = idx
        return res
```

### 763. Partition Labels

字符串 S 由小写字母组成。要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。定义数组 last[char] 来表示字符 char 最后一次出现的下标。定义 anchor 和 j 来表示当前区间的首尾。如果遇到的字符最后一次出现的位置下标大于 j， 就让 j=last[c] 来拓展当前的区间。当遍历到了当前区间的末尾时(即 i==j )，把当前区间加入答案，同时将 start 设为 i+1 去找下一个区间。

> https://leetcode-cn.com/problems/partition-labels/solution/hua-fen-zi-mu-qu-jian-by-leetcode/

```python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
```

### 1252. Cells with Odd Values in a Matrix

如果从正向方式求解会出现遍历二维数组 * 遍历 indices 的情况，可以先构造一个二维数组，然后遍历 indices 模拟数组，最终判断数组中的奇数个数。

```python
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0] * n
        cols = [0] * m
        for x, y in indices:
            rows[x] += 1
            cols[y] += 1
        return sum((rows[x] + cols[y]) % 2 == 1 for x in range(n) for y in range(m))
```