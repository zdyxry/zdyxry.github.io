---
title: 2020 第24周 LeetCode 记录
date: 2020-06-13 07:38:57
tags:
- LeetCode
---

### 1470. Shuffle the Array

重新排列数组，使用 zip 对两个切分后的数组进行聚合

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[0:n],nums[n:]):
            res+=[i,j]
        return res
```

### 1471. The k Strongest Values in an Array

找到与“中位数”数值相差最大的 k 个数字，先将数组排序，找到“中位数”，分别从开头和结尾两边进行比较，找到最大的 k个数。

```python
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        i, j = 0, len(arr) - 1
        median = arr[(len(arr) - 1) // 2]
        while len(arr) + i - j <= k:
            if median - arr[i] > arr[j] - median:
                i = i + 1
            else:
                j = j - 1
        return arr[:i] + arr[j + 1:]
```

### 1472. Design Browser History

用两个变量记录 homepage 和当前位置，处理几个场景：  
1.  从当前页跳转访问 url 对应的页面，需要将当前位置之后的所有历史列表清空
2.  在浏览历史中后退 steps 步，需要与 0 比较，如果小于 0，则将其置为 0
3.  在浏览历史中前进 steps 步，需要与当前历史记录长度比较，如果超过长度，则取历史记录中最后一个

```python
class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.pos += 1
        self.hist[self.pos:] = []
        self.hist.append(url)

    def back(self, steps: int) -> str:
        self.pos -= steps
        if self.pos < 0:
            self.pos = 0
        return self.hist[self.pos]

    def forward(self, steps: int) -> str:
        self.pos += steps
        if self.pos >= len(self.hist):
            self.pos = len(self.hist) - 1
        return self.hist[self.pos]
```


### 754. Reach a Number

> https://www.bilibili.com/video/av31621072/

> https://leetcode-cn.com/problems/reach-a-number/solution/pythonchao-ji-jian-ji-de-jie-fa-by-zhengkang/

首先， 由于坐标轴是对称的，往左往右走的几率相等，因此可以只考虑右半轴。先递推一下可以知道:


```
步数        能到达的位置
1:          1
2:          3, 1
3:          6, 4, 2, 0
4:          10, 8, 6, 4, 0
5:          15, 13, 11, 9, 7, 5, 3, 1
...
```

可以看出来，每一步能到达的最大位置是上一步最大位置加上步数，而每一步所能达到的位置之间间隔都为2。  
记f(n)为第n步能到达的位置，那么有：

```
max(f(n)) = max(f(n-1)) + n
f(n) = [max(f(n)),  max(f(n)) - 2, max(f(n)) - 4, ....]
```

如果target可以在第n步达到，那么target一定小于等于max(f(n))且max(f(n))与taget同奇同偶。


```python
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        p, i = 0, 0
        while p < target or (p + target) % 2 != 0:
            i += 1
            p = p + i
        return i
```


### 1038. Binary Search Tree to Greater Sum Tree

与 538 题相同，使用 dfs 遍历，优先遍历右节点，然后root 节点，最后左节点，使用 currSum 记录比当前节点数值大的数字和，然后将自身与数字和想家，并更新数字和。


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        currSum = [0]
        self.recurse(root, currSum)
        return root
        
    def recurse(self, root, currSum):
        if root is None:
            return
        self.recurse(root.right, currSum)
        root.val = root.val + currSum[0]
        currSum[0] = root.val
        self.recurse(root.left, currSum)
```