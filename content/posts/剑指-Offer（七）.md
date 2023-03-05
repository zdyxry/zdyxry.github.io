---
title: 剑指-Offer（七）
date: 2018-12-15 08:44:06
tags:
- alogrithms
---

## 反转链表

```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse_list(list_head):

    if not list_head or not list_head.next:
        return list_head

    reverse_node = None
    node_pre = None
    node = list_head
    while node:
        node_next = node.next
        if node_next == None:
            reverse_node = node
        node.next = node_pre
        node_pre = node
        node = node_next
    return reverse_node

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

reverse_list(node1)
```

## 合并两个排序的链表 

```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_link(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.val <= head2.val:
        ret = head1
        ret.next = merge_link(head1.next, head2)
    else:
        ret = head2
        ret.next = merge_link(head1, head2.next)
    return ret


node1 = ListNode(10)
node2 = ListNode(15)
node3 = ListNode(18)
node1.next = node2
node2.next = node3

node4 = ListNode(11)
node5 = ListNode(16)
node6 = ListNode(19)
node4.next = node5
node5.next = node6


a = merge_link(node1, node2)
print a.next.next.val
```

## 树的子结构

```python

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1haveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def DoesTree1haveTree2(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False

        return self.DoesTree1haveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right, pRoot2.right)


pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

S = Solution()
print(S.HasSubtree(pRoot1, pRoot8))
```

## 二叉树镜像

```python
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def Mirror(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return root

        pTemp = root.left
        root.left = root.right
        root.right = pTemp

        self.Mirror(root.left)
        self.Mirror(root.right)

    def Mirror2(self, root):
        if not root:
            return
        stackNode = []
        stackNode.append(root)
        while len(stackNode) > 0:
            nodeNum = len(stackNode) - 1
            tree = stackNode[nodeNum]
            stackNode.pop()
            nodeNum -= 1
            if tree.left or tree.right:
                tree.left, tree.right = tree.right, tree.left
            if tree.left:
                stackNode.append(tree.left)
                nodeNum += 1
            if tree.right:
                stackNode.append(tree.right)
                nodeNum += 1


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
S.Mirror(pNode1)
print(pNode1.right.left.val)
```

## 顺时针打印矩阵

```python
class Solution:
    def printMatrix(self, matrix):
        if matrix == None:
            return
        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        while rows > start * 2 and columns > start * 2:
            self.PrintMatrixInCircle(matrix, columns, rows, start)
            start += 1
        print('')

    def PrintMatrixInCircle(self, matrix, columns, rows, start):
        endX = columns - 1 - start
        endY = rows - 1 - start

        for i in range(start, endX+1):
            number = matrix[start][i]
            print(number, ' ', end='')

        if start < endY:
            for i in range(start+1, endY+1):
                number = matrix[i][endX]
                print(number, ' ', end='')

        if start < endX and start < endY:
            for i in range(endX-1, start-1, -1):
                number = matrix[endY][i]
                print(number, ' ', end='')

        if start < endX and start < endY-1:
            for i in range(endY-1, start, -1):
                number = matrix[i][start]
                print(number, ' ', end='')
                

matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1],[2],[3],[4],[5]]
matrix3 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
S = Solution()
S.printMatrix(matrix)
S.printMatrix(matrix2)
S.printMatrix(matrix3)
# print(S.PrintMatrix(matrix))
# print(S.PrintMatrix(matrix2))
# print(S.PrintMatrix(matrix3))
```

