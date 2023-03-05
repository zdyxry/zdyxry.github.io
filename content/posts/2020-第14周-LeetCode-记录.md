---
title: 2020 第14周 LeetCode 记录
date: 2020-04-03 21:49:38
tags:
- LeetCode
---

### 1394. Find Lucky Integer in an Array

找幸运数字，可以维护一个数组，然后统计出现过的次数，也可以直接使用 collections.Counter 实现。


```python
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = [0] * 501
        for a in arr:
            cnt[a] += 1
        for i in range(500, 0, -1):
            if cnt[i] == i:
                return i
        return -1
```


### 1395. Count Number of Teams


遍历数组，假设当前数值是中间位置，因为要考虑到倒序排序，所以要找到左边比当前数值小的和比当前数值大的，找到右边比当前数值小的和比当前数值大的，然后进行排列组合。


```python
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        ans = 0
        for i in range(1,n-1):
            l1,r1= 0,0
            l2,r2 =0,0
            for j in range(i-1,-1,-1):
                if rating[j] < rating[i]:
                    l1 += 1
                else:
                    l2 += 1
            for j in range(i+1,n):
                if rating[j] > rating[i]:
                    r1 += 1
                else:
                    r2 += 1
            ans += l1*r1 + l2*r2
        return ans
```


### 1396. Design Underground System


使用 dict ，在 checkin 的时候以 id 为key，记录地铁站和时间，在 checkout 的时候以 (checkin_station, checkout_station) 为 key，记录所用时间，需要注意多次的情况，记录次数，在 getAverageTime 的时候直接根据 (checkin_station, checkout_station) 从 dict 中读取所用时间总和和次数，进行除法计算每次结果。

```python
class UndergroundSystem:

    def __init__(self):
        self.count = defaultdict(int)
        self.time = defaultdict(int)
        self.traveling = dict()
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.traveling[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (prev_station, prev_t) = self.traveling[id]
        del self.traveling[id]
        key = (prev_station, stationName)
        self.count[key] += 1
        self.time[key] += (t-prev_t)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        
        return self.time[key] / self.count[key]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
```

### 1262. Greatest Sum Divisible by Three

可以用单纯的数学方式做，先统计所有数字的和，然后遍历数字，找出余数为 1 和余数为 2 的数值，当总和余数为 1 时，则减去余数为1 的最小的数字，当总和余数为 2 时，则减去余数为 2 的最小的数字。需要注意比较余数为 1 和余数为2 要进行大小相比，如果 两个余数为2的数值之和小于余数为1 的数值，那么此时应该减去的数字为前者。

也可以采用动态规划做，维护一个 dp，分别存储余数为 0，1，2 的最大数字和，遍历数字，更新相加后的余数最大和，最后返回余数为0 的最大和。


```python
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        
        for n in nums:
            tmp_dp = dp[:]
            for i in range(len(dp)):
                c_sum = tmp_dp[i] + n
                dp[c_sum % 3] = max(dp[c_sum % 3], c_sum)


        return dp[0]
```


```go
func maxSumDivThree(nums []int) int {
    res := 0
    one := 10000
    two := 10000
    for i := 0; i < len(nums); i++ {
        res += nums[i]
        if nums[i] % 3 == 1 {
            two = min(two, one + nums[i])
            one = min(one, nums[i])
        }
        if nums[i] % 3 == 2 {
            one = min(one, two + nums[i])
            two = min(two, nums[i])
        }
    }
    if res % 3 == 0 { return res }
    if res % 3 == 1 { return res - one }
    return res - two
}

func min(a, b int) int {
    if a < b { return a }
    return b
}
```


### 1232. Check If It Is a Straight Line

一道数学题，先用前两个点来计算出斜率，然后遍历之后的点，验证斜率是否一致。


```python
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        same_slop = True
        last_slop = None
        intial_point = coordinates[0]
        for point in coordinates[1:]:
            try:
                slop = (point[1] - intial_point[1])/(point[0] - intial_point[0])
            except ZeroDivisionError: 
                slop = float(inf)
            if last_slop== None:last_slop = slop
            elif slop == last_slop:continue
            else: 
                same_slop = False
                break
                
        return same_slop
```