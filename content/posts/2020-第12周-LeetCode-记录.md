---
title: 2020 第12周 LeetCode 记录
date: 2020-03-20 20:08:24
tags:
- LeetCode
---

### 1380. Lucky Numbers in a Matrix

给一个二维数组，分别求每行最小值，每列最大值，然后找到幸运数字。（遇到二维数组善用 zip 来解决


```python
class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        mins = {min(rows) for rows in matrix}
        maxes = {max(columns) for columns in zip(*matrix)}
        return list(mins & maxes)
```


### 1381. Design a Stack With Increment Operation


相比与 stack 多了一个 inc 操作，一般想法是每次遇到 inc 操作，那么我们遍历一次，将对应值进行加操作就可以了，但是这个操作是 O(n) 的，我们可以使用一个辅助 list ，保存 inc 的数值，当 pop 的时候，进行相加处理。

以示例展示处理过程：
```
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
```

```
stack, inc
[1], [0]
[1,2], [0]
[1], [0]
[1,2], [0,0]
[1,2,3], [0,0,0]
[1,2,3], [0,0, 100]
[1,2,3], [0, 100, 100]
[1,2], [0,200]
[1], [200]
```

```python
class CustomStack(object):

    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val
```


### 1382. Balance a Binary Search Tree

给一个二叉搜索树，使其变为平衡二叉搜索树，只需要一次性操作，不需要时刻考虑每次插入后的变化，根据二叉搜索树特性将其进行中序遍历，得到的结果是升序排序的，然后通过升序排序的结果构建平衡二叉搜索树。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            """inorder depth-first traverse bst"""
            if not node: return 
            dfs(node.left)
            value.append(node.val)
            dfs(node.right)
        
        value = [] #collect values
        dfs(root)
        if not value: return None
        
        def tree(x): 
            if not x: return None
            k = len(x)//2
            ans = TreeNode(x[k])
            ans.left = tree(x[:k])
            ans.right = tree(x[k+1:])
            return ans
        
        return tree(value)
```


### 901. Online Stock Span

维护一个单调栈，遍历 prices：如果 price 比前一天要大，那么将前一天移除，并将前一天的权重与当天相加；如果 price 比前一天要小，那么直接追加当天 price，并将其权重置为 1。


```python
class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
            print price, self.stack
        self.stack.append((price, weight))
        print self.stack
        return weight
```


### 897. Increasing Order Search Tree

考察中序遍历，使用 dfs 直接求解，然后重新构造二叉搜索树。  
也可以直接改动原有树结构，同样是中序遍历，当我们遍历到一个节点时，把它的左孩子设为空，并将其本身作为上一个遍历到的节点的右孩子。

```python
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
```



```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        values = []
        dfs(root)
        tmp = TreeNode(0)
        root = tmp
        for node in values:
            tmp.right = TreeNode(node)
            tmp = tmp.right
        return root.right
```