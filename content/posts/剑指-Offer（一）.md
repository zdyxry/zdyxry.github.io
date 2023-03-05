---
title: 剑指 Offer（一）
date: 2018-11-18 12:23:07
tags:
- alogrithms
---

## Python 单实例模式

```python
class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

class MySingleton(Singleton):

    def __init__(self, val):
        self.val = val

a = MySingleton(1)
b = MySingleton(1)
print a.val
print b.val
```

## 二维数组查找

```python

def find_num(matrix, num):
    if not matrix:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    row, col = rows - 1, 0
    while row >= 0 or col <= cols -1:
        if matrix[row][col] == num:
            return num
        elif matrix[row][col] > num:
            row -= 1
        else:
            col += 1
    return False

matrix = [[1,2,3,4],
          [5,6,7,8]
         ]
print find_num(matrix, 7)
```

## 打印链表

```python

class Links(self):
    def __init__(self, x):
        self.val = x
        self.next = None

def print_links(links):
    if links:
        print_links(links.next)
        print links.val

links = Links(1)
links.next = Links(2)
links.next.next = Links(3)
print_links(links)
```

## 重建二叉树

```python
# 根据前序和中序遍历结果构建二叉树，遍历结果中不包含重复数值。
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    def pre_traversal(self):
        ret = []
        def traversal(head):
            if not head:
                return
            ret.append(head.val)
            traversal(head.left)
            traversal(head.right)
        
        traversal(self.root)
        return ret

    def in_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return 
            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)
        
        traversal(self.root)
        return ret

    def post_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return 
            traversal(head.left)
            traversal(head.right)
            ret.append(head.val)

        traversal(self.root)
        return ret

def construct_tree(preorder=None, inorder=None):
    if not preorder or not inorder:
        return None
    index = inorder.index(preorder[0])
    left = inorder[0:index]
    right = inorder[index + 1:]
    root = TreeNode(preorder[0])
    root.left = construct_tree(preorder[1:1+len(left)], left)
    root.right = construct_tree(preorder[-len(right):], right)
    return root

t = Tree()
root = construct_tree(preorder=[1,2,4,7,3,5,6,8],
                      inorder=[4,7,2,1,5,3,8,6])
t.root = root
print t.pre_traversal()
print t.in_traversal()
print t.post_traversal()
```

## 旋转数组的最小数字
```python
def find_min(nums):
    if not nums:
        return False
    length = len(nums)
    left, right = 0, length - 1
    while nums[right] >= nums[left]:
        if right - left == 1:
            return nums[right]
        mid = (left + right) / 2
        if nums[left] <= nums[mid]:
            left = mid
        if nums[right] >= nums[mid]:
            right = mid
    return nums[0]

nums = [3,4,5,6,0,1,2]
print find_min(nums)
nums = [1,0,0,1]
print find_min(nums)
```

## 二进制中 1 的个数

```python

def find_num_of_1(n):
    ret = 0
    if n < 0:
        n = n & 0xffffffff
    while n:
        ret += 1
        n = n & (n - 1)
    return ret

num = 3
print find_num_of_1(num)
```
