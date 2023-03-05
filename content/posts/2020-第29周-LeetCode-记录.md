---
title: 2020 第29周 LeetCode 记录
date: 2020-07-19 11:19:38
tags:
- LeetCode
---

### 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

要返回最大值与最小值之间的差最小，那么先对其进行排序，三次操作相当于删除三个数字，依次判断删除三个数字之后剩余的数字最大值最小值差最小。

```python
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        return min(b - a for a, b in zip(nums[:4], nums[-4:]))
```

### 1512. Number of Good Pairs

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 ，返回好数对的数目。
只要一个数字出现次数多余一次，那么这个数就可以凑成好数对，然后进行组合。


```python
class Solution:
    def numIdenticalPairs(self, A: List[int]) -> int:
        return sum(k * (k - 1) / 2 for k in collections.Counter(A).values())
```

### 1513. Number of Substrings With Only 1s

判断连续 1 的个数，每当遇到 1 时计数 +1， 遇到 0 时对现有计数进行求和公式，并加到最终结果中，重置计数。


```python
class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        res = 0
        for i in s:
            if i == '1':
                cnt += 1
            else:
                res += cnt * (cnt +1) /2
                cnt = 0
        if cnt > 0:
            res += cnt * (cnt + 1)/ 2
        res %= 1e9+7
        return int(res)
```

### 1114. Print in Order

将各个线程按照顺序执行，有很多实现方式，挑一种方式实现就可以了，这里直接使用 `threading.Event` 。

`threading.Event` 定义如下：

```
Class implementing event objects. An event manages a flag that can be set to true with the set() method and reset to false with the clear() method. The wait() method blocks until the flag is true. The flag is initially false.
```

```python

import threading

class Foo:
    def __init__(self):
        self.b1 = threading.Event()
        self.b2 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.b1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.b1.wait()
        printSecond()
        self.b2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b2.wait()
        printThird()
```

### 1209. Remove All Adjacent Duplicates in String II

这题描述有点别扭，给一个字符串，如果字符串中包含 k 个相邻且相等的字母，那么就原地删除，然后继续检测是否满足条件，重复执行操作。使用栈来记录最终结果，遍历字符串，如果当前自负和栈顶相同，且长度等于 k，那么就出栈，最终将栈中记录拼接为字符串。

```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            print(i)
            if len(stack) == 0 or stack[-1][0] != i:
                stack.append([i, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

        ret = ""
        for t in stack:
            ret += t[0] * t[1]
        return ret
```