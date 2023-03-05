---
title: 剑指 Offer（五）
date: 2018-12-05 20:25:38
tags:
- alogrithms
---

## 调整数组顺序使奇数位于偶数前面

```python
def reorder(nums, func):
    left, right = 0, len(nums) - 1
    while left < right:
        while not func(nums[left]):
            left += 1
        while func(nums[right]):
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]


def is_even(num):
    return (num & 1) == 0
```

## 调整数组顺序使奇数位于偶数前面，保持相对位置不变

```python
def reorder2(nums):
    left = [num for num in nums if num & 1 != 0]
    right = [num for num in nums if num & 1 == 0]
    return left + right

nums = [1,2,3,4,5,6,7]
print reorder2(nums)
```
