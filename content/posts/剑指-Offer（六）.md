---
title: 剑指 Offer（六）
date: 2018-12-06 22:34:54
tags:
- alogrithms
---

## 链表中倒数第k个结点


```python
# 使用两个指针，a 先遍历 k-1，之后一起遍历，直到a 指针到最后一个节点，则 b 为倒数 k 节点
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def find_k_to_tail(self, head, k):
        if not head and k <= 0:
            return None

        a_head = head
        b_head = None

        for i in range(k - 1):
            if a_head.next != None:
                a_head = a_head.next
            else:
                return None

        b_head = head
        while a_head.next != None:
            a_head = a_head.next
            b_head = b_head.next
        return b_head.val

    def find_k_to_tail2(self, head, k):
        if not head and k <= 0:
            return None

        a_head = head

        while a_head and (k - 1) >= 0:
            a_head = a_head.next
            k -= 1

        while a_head:
            a_head = a_head.next
            head = head.next
        return head.val


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)

s = Solution()
print s.find_k_to_tail2(a, 3)

```
