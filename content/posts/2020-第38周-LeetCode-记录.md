---
title: 2020 第38周 LeetCode 记录
date: 2020-09-20 07:45:55
tags:
- LeetCode
---

### 1582. Special Positions in a Binary Matrix

直接遍历二维数组之后，如果某个位置是 1，再去统计每行的和和每列的和是否为 1 时间复杂度太高，可以先统计每行每列的和，然后再遍历二维数组。

```python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n, ans = len(mat), len(mat[0]), 0
        row, col = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    row[i] += 1
                    col[j] += 1
        pool = [j for j in range(n) if col[j] == 1]
        for i in range(m):
            if row[i] != 1:
                continue
            for j in pool:
                if mat[i][j]:
                    ans += 1
                    break
        return ans
```

### 1025. Divisor Game

> 如果N是奇数，因为奇数的所有因数都是奇数，因此 N 进行一次 N-x 的操作结果一定是偶数，所以如果 a 拿到了一个奇数，那么轮到 b 的时候，b拿到的肯定是偶数，这个时候 b 只要进行 -1， 还给 a 一个奇数，那么这样子b就会一直拿到偶数，到最后b一定会拿到最小偶数2，a就输了。
> 
> 所以如果游戏开始时Alice拿到N为奇数，那么她必输，也就是false。如果拿到N为偶数，她只用 -1，让bob 拿到奇数，最后bob必输，结果就是true。

```python
class Solution:
    def divisorGame(self, N: int) -> bool:
        return not N%2
```


### 1583. Count Unhappy Friends

题目有些绕，python 可以直接用 `index` 方法来切片，golang 只能自己实现了。

```python
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        dd = {}
        
        for i,x in pairs:
            dd[i] = preferences[i][:preferences[i].index(x)]
            dd[x] = preferences[x][:preferences[x].index(i)]
        
        ans = 0
        print(dd)
            
        for i in dd:
            for x in dd[i]:
                if i in dd[x]:
                    ans += 1
                    break
        
        return ans
```


### 1282. Group the People Given the Group Size They Belong To

对分组进行统计，组人数作为 key，在该人数的用户索引列表作为 value，然后遍历。


```python
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)
        for i, _id in enumerate(groupSizes):
            groups[_id].append(i)
        
        ans = list()
        for gsize, users in groups.items():
            for it in range(0, len(users), gsize):
                ans.append(users[it : it + gsize])
        return ans
```


### 1305. All Elements in Two Binary Search Trees

如果只是单纯的用列表存储所有值，然后进行排序是最简单的实现方式，但是这道题考察的应该是归并排序。

```python
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node, v):
            if not node:
                return
            dfs(node.left, v)
            v.append(node.val)
            dfs(node.right, v)
        
        v1, v2 = list(), list()
        dfs(root1, v1)
        dfs(root2, v2)
        ans, i, j = list(), 0, 0
        while i < len(v1) or j < len(v2):
            if i < len(v1) and (j == len(v2) or v1[i] <= v2[j]):
                ans.append(v1[i])
                i += 1
            else:
                ans.append(v2[j])
                j += 1
        return ans
```