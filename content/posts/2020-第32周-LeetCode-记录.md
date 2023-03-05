---
title: 2020 第32周 LeetCode 记录
date: 2020-08-08 16:17:20
tags:
- LeetCode
---

### 1534. Count Good Triplets

数据规模很小，暴力循环解。

```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        if len(arr) < 3: return 0
        
        ans = 0
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ans += 1
        return ans

```


### 1535. Find the Winner of an Array Game

每回合游戏都在数组的前两个元素（即 arr[0] 和 arr[1] ）之间进行。比较 arr[0] 与 arr[1] 的大小，较大的整数将会取得这一回合的胜利并保留在位置 0 ，较小的整数移至数组的末尾。当一个整数赢得 k 个连续回合时，游戏结束，该整数就是比赛的 赢家 。

假设第一个数字为所求数字，从下一个数字开始遍历，如果当前数字比所求数字大，那么更新所求数字为当前数字并重置胜利变量为1，否则 += 1，如果胜利次数等于 k，那么直接返回当前最大的数字。

```python
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        a,n=arr[0],0
        for i in arr[1:]:
            if i>a:
                a,n=i,1
            else:
                n+=1
            if n==k:
                return a
        return a
```


### 1536. Minimum Swaps to Arrange a Binary Grid

最终需要将二维数组变为 grid[i] 的 grid[i][i+1:] 均为0，遍历 grid，找到满足当前 grid[i][i+1:] 需求，如果找到了，那么就需要一次次的交换，因为每次只能交换相邻两行，所以交换的次数等于 j -i 。


```python
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        need = 0
        l = len(grid)
        for i in range(l-1):
            for j in range(i, l):
                if sum(grid[j][i+1:]) == 0:
                    need += j-i
                    grid[i:j+1] = grid[j:j+1]+grid[i:j]
                    break
            else:
                return -1
        return need
```


### 25. Reverse Nodes in k-Group

每 k 组链表进行反转，使用递归做比较清晰易懂，[官方题解](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/k-ge-yi-zu-fan-zhuan-lian-biao-by-leetcode-solutio/)感觉需要自己实际画画方便理解。

这道题的基础就是反转链表，通常的反转链表的操作是定义一个 pre，然后遍历整个链表，进行链表连接的断开以及反转，这里需要判断每 k 次，如果不足 k，那么直接返回当前的 head ，如果大于 k，那么就开始反转 k 个链表，注意需要记录反转前的 head，因为进行 k 次反转后，head 就是当前链表的尾端，然后递归反转后续链表，并赋值 head.next 保证链表的连接。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
		        
				
        # Reverse the group (basic way to reverse linked list)
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
		
        # After reverse, we know that `head` is the tail of the group.
		# And `curr` is the next pointer in original linked list order
        head.next = self.reverseKGroup(curr, k)
        return prev
```


### 23. Merge k Sorted Lists

合并 k 个链表，题目没有要求原地合并，直接遍历记录所有链表的数值，然后进行排序，最后再重新定义链表连接起来。


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        all_vals = []
        for l in lists:
            while l:
                all_vals.append(l.val)
                l = l.next
        all_vals.sort()
        dummy = ListNode(None)
        cur = dummy
        for i in all_vals:
            temp_node = ListNode(i)
            cur.next = temp_node
            cur = temp_node

        return dummy.next
```