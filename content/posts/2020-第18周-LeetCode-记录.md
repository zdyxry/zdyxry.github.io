---
title: 2020 第18周 LeetCode 记录
date: 2020-05-01 06:43:57
tags:
- LeetCode
---

### 1422. Maximum Score After Splitting a String

求出左侧 0 数量和右侧 1 数量之和最多的情况，遍历一次，每次更新最大值，注意要保证字符串始终被切分为 2 个子字符串。


```python
class Solution:
    def maxScore(self, s: str) -> int:
        right = s.count('1')
        left = 0
        score = 0
        for idx in range(len(s) - 1):
            if s[idx] == '1':
                score = max(score, (left + right - 1))
                right -= 1
            else:
                score = max(score, (left + 1 + right))
                left += 1
        return score
```

### 1423. Maximum Points You Can Obtain from Cards

先假设所有的数字都是从左侧获取的，然后依次遍历 k 个数值，每次遍历将左侧数字剔除，将右侧数字加入，比较最大值。

也可以转换问题为中间连续 len-k 长度数字和最小，然后所有数字之和减去最小值为所求结果。

```go
func maxScore(cardPoints []int, k int) int {
    var leftSum int
	for i := 0; i < k; i++ {
		leftSum = leftSum + cardPoints[i]
	}
	listLen := len(cardPoints)
	if k == listLen {
		return leftSum
	}
	max := leftSum
	var rightSum int
	for i := 0; i < k; i++ {
		leftSum = leftSum - cardPoints[k-i-1]
		rightSum = rightSum + cardPoints[listLen-i-1]
		if leftSum+rightSum > max {
			max = leftSum + rightSum
		}
	}

	return max
}
```


### 1424. Diagonal Traverse II

按照对角线方式打印出所有数字，考虑对角线部分数字为空的情况。在一个对角线上的数字，他们的横纵坐标之和都是相同的，使用一个二维数组存储，然后从上到下顺序打印出所有对角线的数值，需要注意每条对角线的数值输出应该是从下到上。


```go
func findDiagonalOrder(mat [][]int) (ans []int) {
    order := [1e5][]int{}
	for i := len(mat) - 1; i >= 0; i-- {
		for j, v := range mat[i] {
			order[i+j] = append(order[i+j], v)
		}
	}
	for _, a := range order {
		for _, v := range a {
			ans = append(ans, v)
		}
	}
	return ans
}
```


### 498. Diagonal Traverse

可以用 #1424 相同的方式处理，获取所有对角线的数值，然后遍历，注意输出的顺序，也可以直接模拟，需要处理好边界。

```go
func findDiagonalOrder(matrix [][]int) []int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return []int{}
	}
	n, m := len(matrix), len(matrix[0])
	res := make([]int, n*m)
	var x, y int
	for i := 0; i < len(res); i++ {
		res[i] = matrix[x][y]
		if (x+y)%2 == 0 {
			if y == m-1 {
				x++
			} else if x == 0 {
				y++
			} else {
				y++
				x--
			}
		} else {
			if x == n-1 {
				y++
			} else if y == 0 {
				x++
			} else {
				x++
				y--
			}
		}
	}
	return res
}
```


### 476. Number Complement

一个数字与全 1 进行异或，得到的数字为二进制取反。

```go
package main

import "fmt"

func findComplement(num int) int {
	temp := 1
	for ; temp <= num; temp *= 2 {
	}
	return (temp - 1) ^ num
}

func main() {
	num := 5
	res := findComplement(num)
	fmt.Println(res)
}
```