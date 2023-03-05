---
title: 2020 第34周 LeetCode 记录
date: 2020-08-23 16:37:12
tags:
- LeetCode
---

### 1550. Three Consecutive Odds

判断数组是否存在连续 3 个奇数的情况存在，直接遍历判断，使用变量记录当前奇数个数。

```python
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for i in arr:
            if i & 1:
                cnt += 1
            else:
                cnt = 0
            if cnt == 3:
                return True
        return False
```

### 1551. Minimum Operations to Make Array Equal

一道数学题，等差数列求和公式变形。

```
n=3 最小操作数是 2
n=4 最小操作数是 1 + 3
n=5 最小操作数是 2 + 4
n=6 最小操作数是 1 + 3 + 5
n=7 最小操作数是 2 + 4 + 6
```


```python
class Solution:
    def minOperations(self, n: int) -> int:
        return n*n // 4
```

### 410. Split Array Largest Sum

给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

求最大值最小一般采用二分法来做，数值最终在 max(nums) < result < sum(nums) 区间中，假设当前数值符合条件，然后检查是否符合。

```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m


        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
```


### 1552. Magnetic Force Between Two Balls

与 410 类似，也是求最大化最小值，相同的解法，二分。

```
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def check(x):
            cnt = 1
            t = position[0]
            for i in range(1, len(position)):
                if position[i]-t > x:
                    cnt += 1
                    t = position[i]
            return cnt >= m
        
        l, r = 0, position[-1]
        while l < r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid+1
            else:
                r = mid
        return l
```


### 406. Queue Reconstruction by Height

假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

> https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/gen-ju-shen-gao-zhong-jian-dui-lie-by-leetcode/

```
排序：
按高度降序排列。
在同一高度的人中，按 k 值的升序排列。
逐个地把它们放在输出队列中，索引等于它们的 k 值。
返回输出队列
```

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output
```


### 1249. Minimum Remove to Make Valid Parentheses

给你一个字符串，其中字符串包含一些括号，但是括号不是成对出现的，需要你删除其中不平衡的括号使其达到平衡。
自己做的时候使用了两个栈来分别记录括号和括号所在的索引，如果出现平衡的括号，那么两个栈同时出栈，最终将保存索引的栈中对应的字母删除，返回。


```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        for idx, i in enumerate(s):
            if i in ['(', ')']:
                if i == '(':
                    stack.append(i)
                    res.append(idx)
                elif i == ')':
                    if len(stack) > 0 and stack[-1] == '(':
                        stack.pop()
                        res.pop()
                    else:
                        stack.append(i)
                        res.append(idx)
        tmp = []
        for idx, i in enumerate(s):
            if idx in res:
                continue
            else:
                tmp.append(i)
        return ''.join(tmp)
```

虽然也能通过但是复杂度很高，可以直接遍历字符串，使用一个栈记录 `(` ，如果字符串为 `(` 那么入栈，如果字符串为 `)` 并且栈长度不为 0，那么出栈，否则将字符串对应索引字母置为空，此时结果中所有多余的 `)` 都已经处理完了，接下来处理栈中存在的多余的 `(` 即可。

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indices, ans = [], list(s)
        for i, c in enumerate(s):
            if c == ')':
                if indices:
                    indices.pop()
                else:
                    ans[i] = ''
            elif c == '(':
                indices.append(i)

        for i in indices:
            ans[i] = ''

        return ''.join(ans)
```