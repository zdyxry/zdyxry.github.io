---
title: 2020 第31周 LeetCode 记录
date: 2020-08-01 07:26:24
tags:
- LeetCode
---

### 1523. Count Odd Numbers in an Interval Range

数学题，数据范围是10^9，O(n) 会超时，统计 high 中有多少个奇数，减去 low-1 中的奇数个数，需要考虑边界条件：low/high 自身为奇数情况。

```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = high // 2
        if high % 2 == 1:
            res += 1
        if low - 1 >= 0:
            res -= (low - 1) // 2
            if (low - 1) % 2 == 1:
                res -= 1
        return res
```


### 1528. Shuffle String

按照指定顺序调整字符串，直接定义一个新的长度为 len(s)字符串，然后按照 indices 的索引顺序进行对应调整。


```python
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        _s = ['0'] * len(s)
        for idx, val in enumerate(s):
            _s[indices[idx]] = val
        return ''.join(_s)
```

### 1524. Number of Sub-arrays With Odd Sum

> https://www.youtube.com/watch?v=vGTm8rjlDTQ

用两个变量分别记录奇数和偶数的个数，遍历数组，如果当前数字是奇数，那么 odd 等于偶数个数 +1，1为当前数字，even 等于奇数个数，因为奇数个数加上当前数字（奇数）为偶数；如果当前数字是偶数，那么 odd 等于 odd，偶数个数等于 even + 1，1为当前数字。


```go
const mod = int(1e9 + 7)

func numOfSubarrays(arr []int) int {
    odd, even := 0, 0
    res := 0
    for _, v := range arr {
        if v % 2 != 0 {
            odd, even = even + 1, odd
        } else {
            odd, even = odd, even + 1
        }
        res += odd
        res %= mod
    }
    return res
}
```


### 1525. Number of Good Ways to Split a String

使用 Counter 统计当前字符串中的字符出现的次数，left 表示切割索引左侧字符出现的次数，right 表示切割索引右侧字符出现的次数，遍历字符，如果 right[x] == 0，那么表示右侧已经没有字符 x，那么需要将对应的 key(x) 从 right 中删除，比较 left 中的 key 数量与 right 中是否相同，如果相同，则记录。


```python
class Solution:
    def numSplits(self, s: str) -> int:
        left = Counter()
        right = Counter(s)
        count = 0
        for i in range(len(s)):
            left[s[i]] += 1
            right[s[i]] -= 1
            if right[s[i]] == 0:
                del right[s[i]]
                
            if len(left) == len(right):
                count += 1
        return count
```


### 1529. Bulb Switcher IV

统计需要翻转开关的次数，就是统计最终状态中 0，1 切换的次数，比如`001011101` ，0，1 切换分别在 `001` , `10`, `0111`, `1110`, `01` 这五个位置出现了切换。


```go
func minFlips(target string) int {
    var count int
	target = "0" + target
	flag := target[len(target)-1]
	for i := len(target) - 1; i >= 0; i-- {
		if target[i] != flag {
			count++
			flag = target[i]
		}
	}

	return count
}
```