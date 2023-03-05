---
title: 2020 第15周 LeetCode 记录
date: 2020-04-10 20:44:44
tags:
- LeetCode
---

### 1403. Minimum Subsequence in Non-Increasing Order

对数组进行排序，然后依次取出当前最大值，比较当前取出数值和与剩余数值和，如果大于，则返回取出数字。

```python
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        N = len(nums)
        total = sum(nums)
        nums.sort()

        ret = []
        t = 0
        while True:
            x = nums.pop()

            t += x
            ret.append(x)
            if t * 2 > total: return ret
```


### 1400. Construct K Palindrome Strings

构造指定个数的回文字符串，检查出现次数为奇数的字母次数是否超过了k即可。可以直接用 Counter 计算。


```python
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        digit_count = {}
        if len(s) < k:
            return False
        elif len(s) == k:
            return True
        else:
            odd = 0
            for i in set(s):
                digit_count[i] = s.count(i)
            
            for i in digit_count.values():
                if i % 2 != 0:
                    odd += 1
            if odd > k:
                return False
            else:
                return True
```

### 1401. Circle and Rectangle Overlapping


依次考虑圆心与矩形的位置关系，是否在矩形的上下左右，求出矩形到圆心距离最小的点，然后根据两点间距离公式来与半径相比较。

zhihu 上有一个问题可以解答这道题：https://www.zhihu.com/question/24251545



```go
func checkOverlap(radius int, x_center int, y_center int, x1 int, y1 int, x2 int, y2 int) bool {
    var dx, dy int;
    if x1 > x_center {
        dx = x1 - x_center  
    }else if x_center > x2 {
        dx = x_center - x2 
    }else {
        dx = 0
    }
    if y1 > y_center {
        dy = y1 - y_center  
    }else if y_center > y2 {
        dy = y_center - y2 
    }else {
        dy = 0
    }
    return dx * dx + dy * dy <= radius * radius

}
```


### 1404. Number of Steps to Reduce a Number in Binary Representation to One


这道题如果直接把二进制转换为十进制数，然后判断奇偶就很容易了，但是这不是它本身的目的，主要需要考虑位进位换算，其中分为 4 种情况：

无进位，当前位是1，则步骤 +2，进位为1
无进位，当前位是0，则步骤 +1，进位为0
有进位，当前位是1，则步骤 +1，进位为1
有进位，当前位是0，则步骤 +2，进位为1

其中步骤 +2 的情况为当前位是 1，需要 +1 和 /2 两个操作。


```go
func reverse(A []byte) {
	for i := 0; i < len(A)/2; i++ {
		A[i], A[len(A)-1-i] = A[len(A)-1-i], A[i]
	}
}

func numSteps(s string) int {
	if len(s) == 1 {
		return 0
	}
	bs := []byte(s)
	reverse(bs)
	step, carry, last := 0, 0, bs[len(bs)-1]
	bs = bs[:len(bs)-1]
	for _, v := range bs {
		if carry == 0 {
			if v == '1' {
				step += 2
				carry = 1
			} else {
				step += 1
			}
		} else {
			if v == '0' {
				step += 2
			} else {
				step += 1
                carry = 1
			}
		}
	}
	if last == '1' {
		step += carry
	}
	return step
}
```


### 1405. Longest Happy String

对字母按照次数进行降序排序，然后依次遍历字母，判断最后2位是否与当前字母 * 2 相同，如果相同，则跳过，如果不相同，则将其添加到结果中，并将次数 -1。


```python
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        x = [[a, 'a'],[b, 'b'],[c,'c']]
        res = ""
        while True:
            for num in sorted(x,reverse=True):
                if num[0] <= 0:
                    return res
                if len(res) >= 2 and res[-2:] == num[1] * 2:
                    continue
                res += num[1]
                num[0] -= 1
                break
        return res
```