---
title: 2020 第22周 LeetCode 记录
date: 2020-06-01 05:44:57
tags:
- LeetCode
---

### 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

切分句子然后遍历判断是否为前缀，需要返回索引 + 1。

```python
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for idx, w in enumerate(sentence.split(' ')):
            if w.startswith(searchWord):
                return idx + 1
        else:
            return -1
```

### 1456. Maximum Number of Vowels in a Substring of Given Length

滑动窗口，使用字典统计每个元音出现的次数，每次更新最大值。

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for c in s[:k]:
            if c in d:
                d[c] += 1
        res = sum(d.values())
        for i in range(k, len(s)):
            if s[i-k] in d:
                d[s[i-k]] -= 1
            if s[i] in d:
                d[s[i]] += 1
            res = max(res, sum(d.values()))
        return res
```

### 1200. Minimum Absolute Difference

遍历列表，记录前一个数值，每次计算绝对差值，更新最小值，如果差值等于最小值，则将其加入到结果中。


```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m = float('inf')
        out = []
        for i in range(1, len(arr)):
            prev = arr[i - 1]
            curr = abs(prev - arr[i])
            if curr < m:
                out = [[prev, arr[i]]]
                m = curr
            elif curr == m: out.append([prev, arr[i]])
        return out
```



### 1457. Pseudo-Palindromic Paths in a Binary Tree

DFS 遍历二叉树，使用 set 记录已有数值，如果该数值已经存在，则删掉，如果不存在，则加入set。判断回文字符的依据是set 中剩余字母长度是否小于等于1。


```python
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        s = set()

        def dfs(root):
            if not root: return 0
            if root.val in s:
                s.discard(root.val)
            else:
                s.add(root.val)

            res = dfs(root.left) + dfs(root.right)
            if not root.left and not root.right:
                res += len(s)<=1
            if root.val in s:
                s.discard(root.val)
            else:
                s.add(root.val)

            return res
        return dfs(root)
```
