---
title: 2020 第39周 LeetCode 记录
date: 2020-09-26 17:08:07
tags:
- LeetCode
---

### 1588. Sum of All Odd Length Subarrays

处理当长度为 1 时特殊情况，其他都遍历长度为奇数情况然后求和。

```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)+1):
            if i % 2:
                if i == 1:
                    res += sum(arr)
                else:
                    j = 0
                    while j + i <= len(arr):
                        res += sum(arr[j:j+i])
                        j += 1
        return res
```


### 1592. Rearrange Spaces Between Words

统计空格出现的次数，然后求出平均空格数进行字符串拼接。

```python
class Solution:
    def reorderSpaces(self, text: str) -> str:
        cnt=text.count(" ")
        n = text.split()
        if len(n)==1:
            return text.strip()+cnt*" "
        space,last = divmod(cnt,len(n)-1)
        return (" "*space).join(n)+" "*last
```

### 1593. Split a String Into the Max Number of Unique Substrings

回溯法，使用集合记录出现过的字符串。

```python
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.ans = 0
        d = set()

        def helper(num, sub):
            if not sub:
                self.ans = max(num, self.ans)
                return
            
            if sub in d: return 
            
            for i in range(1, len(sub) + 1):
                if sub[:i] not in d:
                    d.add(sub[:i])
                    helper(num + 1, sub[i:])
                    d.remove(sub[:i]) 
                    
        helper(0, s)

        return self.ans
```


### 814. Binary Tree Pruning

如果叶子节点的左子树和右子树为空且当前值为 0，则将其置为空，递归剪枝。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root
```


### 1008. Construct Binary Search Tree from Preorder Traversal

提供先序遍历，构造二叉树，先序遍历的第一个元素是 root 节点，分别遍历之后元素，如果元素比 root 小，则记录到root 左子树中，反之记录到 root 右子树中，递归构造。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        leftList = []
        rightList = []
        root = TreeNode(preorder[0])
        for num in preorder[1:]:
            if num < preorder[0]:
                leftList.append(num)
            elif num > preorder[0]:
                rightList.append(num)
        root.left = self.bstFromPreorder(leftList)
        root.right = self.bstFromPreorder(rightList)
        return root
```