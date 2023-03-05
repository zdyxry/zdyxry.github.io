---
title: 2020 第26周 LeetCode 记录
date: 2020-06-28 21:57:10
tags:
- LeetCode
---

### 1486. XOR Operation in an Array

遍历进行异或操作。

```python
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= start + 2 * i
        return ans
```


### 1487. Making File Names Unique

一道实际环境中会遇到的场景，使用哈希表记录已有的文件名，如果该文件已经存在在哈希表中，那么循环判断文件名 + `()` 数字是否也在哈希表中，如果还在，那么数字 + 1，直到数字不在。然后将结果记录到返回列表中。


```python
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        nameMap = {} # baseName : largest k suffix
        res = []
        
        for n in names:
            if n in nameMap:
                # find k
                k = nameMap[n] + 1
                while ( n + "(" + str(k) + ")" ) in nameMap:
                    k += 1
                nameMap[n] = k
                n = n + "(" + str(k) + ")" # with suffix is now considered a base name
                
            nameMap[n] = 0 # first time seeing this base name
            res.append(n)
        return res
```

### 701. Insert into a Binary Search Tree

在二叉树中插入节点，如果 val > node.val，插入到右子树，如果 val < node.val，插入到左子树，最终返回 root 节点。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            # insert into the right subtree
            if val > node.val:
                # insert right now
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            # insert into the left subtree
            else:
                # insert right now
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val)

```

### 1488. Avoid Flood in The City

遇到不下雨的时候先不去判断应该将哪个湖水抽干，而是等到某个湖下雨两次，再去从不下雨的天气里在湖两次下雨之间抽取第一个来抽干这个湖，防止洪水泛滥，如果找不到，则发生洪水。

> https://www.youtube.com/watch?v=8sxeQyumrYc


```python
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        left = []
        record = dict()
        for i, val in enumerate(rains):
            if val > 0:
                ans[i] = -1
                if val in record:
                    pos = bisect_left(left, record[val])
                    if pos >= len(left):
                        return []
                    ans[left.pop(pos)] = val
                record[val] = i
            else:
                left.append(i)
        return ans
```


### 1047. Remove All Adjacent Duplicates In String

遍历字符串，使用列表作为栈记录结果，如果当前栈大于0 且当前字母与栈顶相同，则出栈，否则将其加入到结果中。


```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        for i in S:
            if len(res) >= 1 and i == res[-1]:
                res.pop()
                continue
            res.append(i)
        return ''.join(res)
```