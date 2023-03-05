---
title: 2020 第19周 LeetCode 记录
date: 2020-05-08 07:48:12
tags:
- LeetCode
---

### 1436. Destination City

使用 set() 来计算每个城市是否处于起始和终止，集合差为终点站。

```python
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a = set()
        b = set()
        for path in paths:
            x, y = path
            a.add(x)
            b.add(y)

        b = b - a
        assert len(b) == 1
        return b.pop()
```

### 1432. Max Difference You Can Get From Changing an Integer

分别求出给定数字可以转换的最大值和最小值，然后求差，最大值是将数字从前向后遍历，当数值不为9时，将其替换为 9；最小值要求首位不能为 0，则需要特殊判断，如果首位不为1，则将其替换为1，如果首位为1，则遍历后续数字，如果数字不为0，则替换为0，需要注意此时首位为1，如果数字为1然后替换为0会出现首位为0 情况，因此需要判断数字不为0且不为1，然后替换为 0。

```python
class Solution:
    def maxDiff(self, num: int) -> int:
        a = b = str(num)

        for digit in a:
            if digit != "9":
                a = a.replace(digit, "9")
                break
        
        if b[0] != "1":
            b = b.replace(b[0], "1")
        else:
            for digit in b[1:]:
                if digit not in "01":
                    b = b.replace(digit, "0")
                    break
        
        return int(a) - int(b)
```


### 1433. Check If a String Can Break Another String

检查两个字符串的字符序是否存在交叉情况，先对字符串进行排序，然后使用两个 flag 标记当前字符的大小，如果有大有小，那么直接返回 False，否则返回 True。

```python
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1= sorted(s1)
        s2= sorted(s2)
        res1, res2 = False, False
        for pair in zip(s1, s2):
            com = ord(pair[0]) - ord(pair[1])
            if com > 0:
                res1 = True
            elif com < 0:
                res2 = True
            if res1 and res2:
                return False
        return True
```


### 1437. Check If All 1's Are at Least Length K Places Away

检查每个数字 1 之间的间隔是否大于 k，如果不大于则返回 False，遍历数字，如果数字不为 1，则将间隔 +1，直到下次遇1时判断并重置。

```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zero_num = 1e5
        for x in nums:
            if x == 1:
                if zero_num < k:
                    return False
                zero_num = 0
            else:
                zero_num += 1
        return True
```

### 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

滑动窗口，遍历数字，每次更新最大值与最小值，如果符合条件，则窗口增大，否则从左侧缩小窗口，缩小窗口后需要注意更新最大值与最小值。


```python
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minimal, maximal = float("inf"), float("-inf")
        size, current_size_start_number = 0, None
        for i in range(len(nums)):
            maximal = max(maximal, nums[i])
            minimal = min(minimal, nums[i])
            if abs(maximal - minimal) <= limit:
                size += 1
            else:
                current_size_start_number = nums[i-size]
                if current_size_start_number == minimal:
                    minimal = min(nums[i - size + 1:i + 1])
                elif current_size_start_number == maximal:
                    maximal = max(nums[i - size + 1:i + 1])
        return size 
```