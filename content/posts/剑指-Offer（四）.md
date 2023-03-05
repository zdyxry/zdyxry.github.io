---
title: 剑指 Offer（四）
date: 2018-12-02 20:11:24
tags:
- alogrithms
---

## 在O(1)时间内删除链表结点

```python

class ListNode(object):

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None

class Solution(object):
    def delete_list(self, list_head, to_delete):
        if not list_head or not to_delete:
            return False

        if to_delete.next != None:
            next_node = to_delete.next
            to_delete.val = next_node.val
            to_delete.next = next_node.next
            next_node.__del__()

        elif list_head == to_delete:
            list_head.__del__()
            to_delete.__del__()
        else:
            list_node = list_head
            while list_node.next != to_delete:
                list_node = list_node.next
            list_node.next = None
            to_delete.__del__()


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4


# Solution().delete_list(node1, node4)
Solution().delete_list(node1, node3)
print(node1.next.next.val)
```

