---
title: 2020 第33周 LeetCode 记录
date: 2020-08-16 10:27:06
tags:
- LeetCode
---

### 1544. Make The String Great

使用栈来记录最终结果，如果栈顶和当前字符相同，那么出栈，否则入栈。

```python
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and ((ord(stack[-1])-32) == ord(i) or (ord(stack[-1])+32) == ord(i)):
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
```


### 1545. Find Kth Bit in Nth Binary String


找出第 N 个二进制字符串中的第 K 位，其中二进制字符串的生成是按照特定规律的，可以直接暴力模拟生成二进制字符串，找出第 N 个，这种方法不会超时，但是不好。考虑使用递归求解，每个二进制字符串的左半部分，都是上一个二进制字符串，那么需要判断 K 在第 N 个字符串中的左边还是右边，如果是中间就直接返回 1 ；如果是左边，那么就找 N-1 个二进制字符串中 K 个；如果是右边，那么就找 N-1 个二进制字符串中的 K 对称位置，并将结果取反。


```python
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if (n == 1):
            return '0'
        l = (1 << n) - 1
        mid = (l >> 1) + 1
        if k == mid:
            return '1'
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            k = l + 1 -k
            return '1' if self.findKthBit(n - 1, k) == '0' else '0'

```

```python
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = [0] * (n+1)
        s[0] = '0'
        for i in range(1, n+1):
            s[i] = s[i-1] + '1' + self.reverse(s[i-1])
        return s[n][k-1]

    def reverse(self, s):
        res = []
        for i in s:
            if i == '1':
                res.append('0')
            else:
                res.append('1')
        return ''.join(res[::-1])
```

### 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target

这是一道告诉你方法就会立刻做出来的题目，前缀和，因为要求不重叠，因此在遍历过的结果中找到 target，那么就需要将 set 重置，cur_sum 清零。

```python
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        s = {0}
        cur_sum = 0
        ans = 0
        for num in nums:
            cur_sum += num
            if cur_sum - target in s:
                s = {0}
                cur_sum = 0
                ans += 1
            else:
                s.add(cur_sum)
        return ans

```


### 1541. Minimum Insertions to Balance a Parentheses String

看完题目第一想法是用栈来做，但是写了半天发现题目理解错了，这题跟 #1544 不同的是，它不会因为栈中某个时刻符合平衡括号的条件就全部出栈，比如 `"(()))(()))()())))"` 这个用例，如果自己计算理解了这个用例这道题也就做出来了。

使用栈记录当前遍历字符为 `(` 的情况，如果为 `(` 那么直接入栈，如果为 `)` ，那么此时有两种情况：
* 如果栈不存在，意味着左边缺少 `(` ，那么就至少需要补充一个 `(` ，此时判断当前字符的右侧是否为 `)` ，如果是，那么只需要添加一个 `(` ，如果不是 `)` ，那么就需要添加一个 `(` 和一个 `)`；
* 如果栈存在，意味着左侧存在 `(` ，此时判断当前字符右侧是否为 `)` ，如果是，那么将左侧字符出栈，此时已经满足了平衡括号情况，无须添加，如果不是 `)` ，那么需要添加一个 `)` 满足平衡。

最终判断 stack 是否还存在，如果存在，则每个 `(` 需要添加两个 `)` 满足条件。


```python
class Solution:
    def minInsertions(self, s: str) -> int:
        # use stack
        stack = []
        count = 0
        i=0
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
                i += 1
            else:
                # when facing empty stack
                if not stack:
                    if i+1 < len(s) and s[i+1] == ")":
                        count += 1  # add one "("
                        i += 2
                    else:
                        count += 2   # add one "("  and one ")"
                        i += 1
                else:
                    # check two positions
                    if i + 1 < len(s) and s[i+1] == ")":
                        stack.pop()
                        i += 2
                    else:
                        count += 1   # add one ")"
                        stack.pop()
                        i += 1
        
        rest = len(stack)*2  # still have "(" on the stack. one "(" pairs with two ")"
        return count + rest
```

### 147. Insertion Sort List

[leetcode-cn](https://leetcode-cn.com/problems/insertion-sort-list/solution/da-lao-de-dai-ma-kan-ming-bai-hou-ji-ge-bi-ji-yong/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:                            
            return head
        dummy=ListNode(float(-inf))             #首项负无穷保证插的数据不在最前头
        dummy.next=head                         #用于返回答案
        pre=head                                    
        nxt=head.next
        while nxt:                              #最后一项为None结束循环
            if nxt.val>pre.val:                 #从头开始，如果后一项大于前一项不改变节点
               pre=nxt                          #这两行移动指针（往后挪一格）
               nxt=nxt.next
            else:                               #如果后项小需要把后项nxt的节点插到正确位置
                pre.next=nxt.next               #把nxt指向的节点拿出来
                cp1=dummy                       #这两个指针负责从头开始比较nxt的位置
                cp2=dummy.next                  #使用dummy的原因见11行注释
                while nxt.val>cp2.val:          #因为前面是排好序的循环结束nxt正好在cp1和cp2中间
                    cp1=cp2                     #
                    cp2=cp2.next                #
                nxt.next=cp2                    #这两行负责插
                cp1.next=nxt                    #把nxt指向的节点查到cp1和cp2中间
                nxt=pre.next                    #指针从哪来回哪去 准备下一个循环
        return dummy.next
```