---
title: 2020 第30周 LeetCode 记录
date: 2020-07-26 09:36:03
tags:
- LeetCode
---

### 1518. Water Bottles

小学数学题，用几个空瓶子可以换一瓶新的，问最后能喝到几瓶，在小学场景下可以先借再喝，在这道题没有这种场景，所以正常计算就好。


```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            cnt = numBottles // numExchange
            res += cnt
            numBottles = numBottles - (cnt * numExchange)
            numBottles += cnt
        return res
```

### 1108. Defanging an IP Address

将 IPv4 地址 "1.1.1.1" 转换为 "1[.]1[.]1[.]1" ，不知道这道题的意义在哪里。。

```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
```

### 1519. Number of Nodes in the Sub-Tree With the Same Label

题目很绕，最好自己根据给的 edges 和 labels 构建出对应的树，了解是如何构建的，最终要求的 ans 中 ans[i] 表示第 i 个节点的子树中与节点 i 标签相同的节点数，记录所有节点的相邻节点，从 0 节点开始 dfs，如果节点已经访问过，则跳过对应节点，最终汇总 ans[i] 中的数值。

```python
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        from collections import defaultdict
        from collections import Counter

        edge_map = defaultdict(list)
        for edge in edges:
            edge_map[edge[0]].append(edge[1])
            edge_map[edge[1]].append(edge[0])
            
        def _dfs(i):
            visited.add(i)
            # 字符数字典
            data = Counter({labels[i]: 1})
            for nxt in edge_map[i]:
                if nxt in visited: continue # 去重
                # 整合子树的字符数
                data += _dfs(nxt)
            # 设置当前节点的结果字符数
            ans[i] = data[labels[i]]
            return data

        visited = set()
        ans = [1] * n
        _dfs(0)
        return ans
```

### 1189. Maximum Number of Balloons


给一个字符串 text，使用 text 中的字母来拼凑尽可能多的单词 "balloon"，每个字母最多只能被使用一次。返回最多可以拼凑出多少个单词 "balloon"，分别统计每个字母出现的次数，然后判断满足ballon 所有字母出现次数最小的。


```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = collections.Counter(text)
        return min(d['b'], d['a'], d['l'] // 2, d['o'] // 2, d['n'])
```

### 1304. Find N Unique Integers Sum up to Zero

给一个整数 n，返回任意一个由 n 个 各不相同的整数组成的数组，并且这 n 个数相加和为 0 ，题目很开放，如果n 为奇数，则补充一个数字 `0`，如果为 偶数，那么补充对应的 n/2 个数字的正负值。

```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n%2 == 1:
            res.append(0)
        for i in range(1, n//2+1):
            res.append(i)
            res.append(-i)
        return res
```