---
title: 2020 第27周 LeetCode 记录
date: 2020-07-04 09:17:15
tags:
- LeetCode
---

### 1492. The kth Factor of n

计算 n 的第 k 个因子，i 从 1 开始递增，如果 i 可以被 n 整除，则 k--，当 k == 0 时， i为所求值。

```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n+1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        return -1   
```


### 1493. Longest Subarray of 1's After Deleting One Element

用 cnt1 记录删除一个元素之后当前最长全为 1 的数组长度，用 cnt2 记录当前最长全为 1 的数组长度。

遍历数组，当 num == 1 时，则 cnt1++, cnt2++，当 num != 1 时，cnt1 = cnt2，并将 cnt2 置 0。每次更新 cnt1 时，比较最大值。

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt1, cnt2 = 0, 0
        maxlen = 0
        for num in nums:
            if num == 1:
                cnt1 += 1
                cnt2 += 1
                maxlen = max(maxlen, cnt1)
            else:
                cnt1 = cnt2
                cnt2 = 0
        if cnt1 == len(nums):
            return len(nums)-1
        return maxlen
```

### 1496. Path Crossing

起始点为 (0,0)，然后遍历 path，当为南北时，分别对 y 进行 +1，-1， 当为东西时，分别对 x 进行 +1，-1，每次走过一个路径，就判断当前所在节点是否已经在记录中，如果在直接返回 True，否则将其添加到记录中。


```python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        set = {(0, 0)}
        
        for c in path:
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            else:
                x -= 1
            
            if (x, y) in set:
                return True
            set.add((x, y))
        return False
```


### 1497. Check If Array Pairs Are Divisible by k

使用哈希表，分别将所有 arr 中的数字对 k 取余，然后遍历余数，如果余数不为0，且 k - 余数 在哈希表中并且 两个key 数值相同，则这两个数字所组成的数字对之和是可以被 k 整除的。如果余数为0，那么判断余数为0 的个数是否为偶数，如果为偶数，那么返回 True。


```python
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod = collections.Counter(num % k for num in arr)
        for t, occ in mod.items():
            if t > 0 and (k - t not in mod or mod[k - t] != occ):
                return False
        return mod[0] % 2 == 0
```


### 1498. Number of Subsequences That Satisfy the Given Sum Condition

因为是非空子序列，因此不要求连续，只要满足条件的任意组合即可。

对数组进行排序，然后使用双指针，如果 nums[l] + nums[r] > target，此时不符合条件，那么将 r--，如果符合，那么在结果中 l 到 r 这个距离中所有的组合都是满足条件的，2 ^ (r-l)，l++，结果相加后取模。



```python
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 10 ** 9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod
```