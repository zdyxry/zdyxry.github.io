---
title: 2020 第13周 LeetCode 记录
date: 2020-03-27 22:27:32
tags:
- LeetCode
---


### 1387. Sort Integers by The Power Value

给定一个区间，让你求出这个区间内所有数字的权重，然后按照权重进行排序，权重计算方式为：

* 如果 x 是偶数，那么 x = x / 2
* 如果 x 是奇数，那么 x = 3 * x + 1

在计算过程中，肯定会有重复计算，所以使用 dict 记录已经计算过的数值权重。当计算完成后，对结果进行排序，优先使用权重排序，如果权重相同，则按照数值本身大小进行排序，取第 k 个。



```python
class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        self.memo = {}
        def helper(n):
            if n==1:
                return 0
            if n in self.memo:
                return self.memo[n]
            if n%2:
                ans=helper((n*3+1)/2)+2
            else:
                ans=helper(n/2)+1
            self.memo[n]=ans
            return ans
        tmp=sorted([[helper(n),n] for n in range(lo,hi+1)])
        return tmp[k-1][1]
```

### 1389. Create Target Array in the Given Order

考察 insert 动作，可以直接用 insert 函数来做；也可以通过对 list 进行切片实现。

```python
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        for n, i in zip(nums, index):
            target.insert(i, n)
            # target = target[:i] + [n] + target[i:]
        return target
```


### 1390. Four Divisors

数学题，如果一个数的因数恰好是 4个因数，那么返回这4个因数的和，直接暴力求解会超时。

如果整数 x 有因数 y，那么也必有因数 x/y，并且 y 和 x/y 中至少有一个不大于 sqrt(x)。这样我们只需要在 [1, sqrt(x)] 的区间内枚举可能为整数 x 的因数 y，并通过 x/y 得到整数 x 的其它因数。


```python
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        def fn(n):
            if n not in cache:
                s = set()
                for i in range(1, 1 + int(math.sqrt(n))):
                    if n % i == 0:
                        s.add(i)
                        s.add(n / i)
                    if len(s) > 4:
                        break
                cache[n] = sum(s) if len(s) == 4 else 0
            return cache[n]

        return sum(map(fn, nums))
```


### 1386. Cinema Seat Allocation

使用位运算，先按照每行拆分，统计出已经被预约的位置，置为1，然后分别与可能安排的3种方式进行与运算，如果为0 ，则表示可以安排。最终将结果求和。需要注意如果一行内所有作为都未安排的情况，此时应该按照每行 2 种方式相加。


```python
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        seats = collections.defaultdict(int) 
        res = 0
		
        for row, col in reservedSeats:
            seats[row] = seats[row] | (1 << (col-1))

        print bin(seats[3])
            
        for reserved in seats.values():
            curr = 0
            curr += (reserved & int('0111100000', 2)) == 0
            curr += (reserved & int('0000011110', 2)) == 0
            curr += (reserved & int('0001111000', 2)) == 0 and curr == 0

            res += curr    

        return res + 2 * (n - len(seats))
```


### 1329. Sort the Matrix Diagonally

考察排序和数组，需要先找到对角线的数字集，可以使用（每行的索引 - 每列的索引）来表示，因为对角线上的数字该值是相同的，找到后对起进行排序，然后再次遍历填入排序后的数字。


```python
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        diag = defaultdict(list)
        N,M = len(mat), len(mat[0])
        
        for i in range(N):
            for j in range(M):
                diag[i-j].append(mat[i][j])
        
        for k in diag.keys():
            diag[k].sort(reverse=True)
        
        for i in range(N):
            for j in range(M):
                mat[i][j] = diag[i-j].pop()
        
        return mat
```