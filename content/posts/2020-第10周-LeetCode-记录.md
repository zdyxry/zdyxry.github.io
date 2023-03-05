---
title: 2020 第10周 LeetCode 记录
date: 2020-03-06 21:10:06
tags:
- LeetCode
---



### 1365. How Many Numbers Are Smaller Than the Current Number

对数组升序排序，遍历排序后数组，判断是否与前一数字相同，若相同则该数字结果与前一结果相同，否则为当前索引。


```python
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = sorted(nums)
        mapping = {}
        for i, num in enumerate(nums2):
            if i > 0 and nums2[i] == nums2[i-1]:
                mapping[nums2[i]] = mapping[nums2[i-1]]
            else:
                mapping[nums2[i]] = i
        res = []
        for num in nums:
            res.append(mapping[num])
        return res
```


### 1366. Rank Teams by Votes

考察排序，通过 dict 或者 list 统计所有字母的投票数值，然后进行排序，优先按照票数排序，如果票数相同，则按照字母序排序。

要熟练使用 sorted 和 sort.Slice 啊。。

```python
class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        n = len(votes[0])
        # 初始化哈希映射
        ranking = collections.defaultdict(lambda: [0] * n)
        # 遍历统计
        for vote in votes:
            for i, vid in enumerate(vote):
                ranking[vid][i] += 1
        
        # 取出所有的键值对
        result = list(ranking.items())
        print result
        # 排序
        result.sort(key=lambda x: (x[1], -ord(x[0])), reverse=True)
        return "".join([vid for vid, rank in result])
```


### 1367. Linked List in Binary Tree

递归判断，比较当前 head 和 root、root.left、root.right，如果 head 为空，则表示已找到所有匹配的链表，返回 True，如果 root 为空或 root.val != head.val ，则返回 False，否则递归判断 head.next, root.left, root.right。


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def dfs(self, head, root):
        if not head:
            return True
        if not root:
            return False
        if root.val != head.val:
            return False
        else:
            return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)
```


### 1309. Decrypt String from Alphabet to Integer Mapping

简单粗暴的办法可以进行一个 map，先把所有的映射都记录好，然后逐个字符判断，该字符后的2位是否为 `#` ，来进行映射判断。比较取巧的办法是直接在原字符串上进行替换，不使用多余空间。

在进行字符串转换时，需要注意两位数是从 10 开始计算，而一位数是从 1 开始计算。

```python
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(10,27):
            s = s.replace( str(i) + '#',chr(ord('j') - 10 + i) )
        for i in range(1,10):
            s = s.replace( str(i), chr(ord('a') - 1 + i ) )
        return s
```


```python
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get(st):
            print st
            return chr(int(st) + 96)
        
        i, res = 0, ""
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                res += get(s[i : i + 2])
                i += 2
            else:
                res += get(s[i])
            i += 1
        return res
```


### 1137. N-th Tribonacci Number

泰波那契数，方法与斐波那契数一样，递归求解。


```python
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cache = {}
        def tibo(n):
            if n == 0:
                return 0
            if n in (1, 2):
                return 1
            
            if n in self.cache:
                return self.cache[n]
            
            self.cache[n] = tibo(n-1) + tibo(n-2) + tibo(n-3)
            return self.cache[n]
        
        return tibo(n)
```