---
title: 2020 第9周 LeetCode 记录
date: 2020-02-28 19:35:45
tags:
- LeetCode
---


### 1300. Sum of Mutated Array Closest to Target

对 arr 进行降序排序，将 arr 中的最小值乘以 arr 长度与 target比较，若比 target 小，则将其丢弃，并将其从 target 中减去。
若 arr 为空，则表示 arr 中最大值乘以 arr 长度仍比 target 小，则返回 arr 中的最大值。
若 arr 不为空，则表示 arr 中存在大于目标值的数值，取 target 除以此时 arr 长度（arr 中所有数值均大于目标值），最终值四舍五入得到目标值。

```python
class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort(reverse = True)
        
        while arr and target >= arr[-1]*len(arr):
            temp = arr[-1]
            target -= arr.pop()
        
        if not arr:
            return temp
        res = target/float(len(arr))
        
        if res % 1 > 0.5:
            return int(res)+1
        else:
            return int(res)
```

也可用二分方式做，取 [0, max(arr)] 中间值为 mid，对 arr 求和：若数值大于 mid则取 mid，求和结果与 target 比较。
记录最小差值和最小差值时 mid 值，若求和数值大于 target，则将上限置为 mid-1，否则将下限置为 mid+1，如果求和数值与 target 相等，则直接返回 mid。


```python
class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, max(arr)
        sub, ans = float("inf"), float("inf")
        
        while left <= right:
            mid = (left + right) // 2
            
            tmp = 0 
            for num in arr:
                if num > mid:
                    tmp += mid
                else:
                    tmp += num
            
            cur_sub = abs(tmp - target)
 
            if cur_sub < sub:
                sub = cur_sub
                ans = mid
            elif cur_sub == sub:
                ans = min(ans, mid)
 
            if tmp > target:
                right = mid - 1
            elif tmp < target:
                left = mid + 1
            elif tmp == target:
                return mid
                
        return ans
```


### 1299. Replace Elements with Greatest Element on Right Side

按照题意暴力解法，时间接近5s。

```python
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
                return arr
            arr[i] = max(arr[i+1:])
        return arr
```

正确姿势为从后向前比较，每次比较最大值与 arr[i] 即可。

```python
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        greatest = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] < greatest:
                arr[i] = greatest
            else:
                arr[i], greatest = greatest, arr[i]
        return arr
```

### 1363. Largest Multiple of Three

这是一道数学题，当一个数字可以被 3 整除时，那么这个数字每一位相加之和也可被 3 整除。

倒序排序，计算所有数字之和，如果可以被 3 整除，那么直接返回；
如果余数为1，则从数组中尝试删除 1，4，7 其中一个；
如果余数为2，则从数组中尝试删除 2，5，8 其中一个；
若仍不满足条件，且余数为 2 ，则从数组中尝试删除 1，4，7 其中两个；
若仍不满足条件，且余数为 1 ，则从数组中尝试删除 2，5，8 其中两个；

```python
class Solution(object):
    def largestMultipleOfThree(self, A):
        """
        :type digits: List[int]
        :rtype: str
        """
        total = sum(A)
        count = collections.Counter(A)
        A.sort(reverse=1)

        def f(i):
            if count[i]:
                A.remove(i)
                count[i] -= 1
            if not A: return ''
            if not any(A): return '0'
            if sum(A) % 3 == 0: return ''.join(map(str, A))

        if total % 3 == 0:
            return f(-1)
        if total % 3 == 1 and count[1] + count[4] + count[7]:
            return f(1) or f(4) or f(7)
        if total % 3 == 2 and count[2] + count[5] + count[8]:
            return f(2) or f(5) or f(8)
        if total % 3 == 2:
            return f(1) or f(1) or f(4) or f(4) or f(7) or f(7)
        return f(2) or f(2) or f(5) or f(5) or f(8) or f(8)
```


### 1362. Closest Divisors

求 num 的平方根，倒序排序后，依次遍历检测是否被 (num + 1) 或 (num + 2) 整除，若整除则为所求结果。


```python
class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        for i in reversed(range(1, int((num + 2) ** 0.5) + 1)):
            if not (num + 1) % i:
                return [i, (num + 1) // i]
            if not (num + 2) % i:
                return [i, (num + 2) // i]
```



### 228. Summary Ranges

这道题我在实际应用中遇到过，具体问题可以看这篇记录 [《记一次 libcgroup 配置失败》](https://zdyxry.github.io/2019/04/11/%E8%AE%B0%E4%B8%80%E6%AC%A1-libcgroup-%E9%85%8D%E7%BD%AE%E5%A4%B1%E8%B4%A5/) 。

记录当前连续数字的 start 和 end，并遍历数组进行判断，如果 num = end + 1 ，那么更新 end 数值，如果不等于，那么将这段数字转换为字符串并添加到结果中，并重置 start & end。


```python
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        if not nums:
            return ranges

        start, end = nums[0], nums[0]
        for i in xrange(1, len(nums) + 1):
            if i < len(nums) and nums[i] == end + 1:
                end = nums[i]
            else:
                interval = str(start)
                if start != end:
                    interval += "->" + str(end)
                ranges.append(interval)
                if i < len(nums):
                    start = end = nums[i]

        return ranges
```

p.s. 贴一下自己用 shell 写的，写完就看不懂了。。

```shell
function format_qemu_processors {
    # cgconfig.service could not be active when libcgroup <= libcgroup-0.41-20.el7 and config field >= 100 char
    # use `-` format qemu_processors
    # example:
    # qemu_processors input (6,7,8,9,10),  output is "6-10"
    # qemu_processors input (10,9,8,7,6),  output is "6-10"
    # qemu_processors input (6,7,8,10,11), output is "6-8,10-11"
    # qemu_processors input (1,3,5,7,9),   output is "1,3,5,7,9"

    IFS=$'\n' sorted=($(sort -n <<<"${qemu_processors[*]}"))
    unset IFS

    QEMU_CPUS=""
    TAG=""
    for i in "${!sorted[@]}";do
        if [[ "${sorted[(i+1)]}" == `expr ${sorted[i]} + 1` ]];then
            if [[ ${sorted[(i-1)]} == $TAG ]];then
                TAG=${sorted[i]}
                continue
            fi
            QEMU_CPUS=$QEMU_CPUS"${sorted[i]}"
            QEMU_CPUS=$QEMU_CPUS"-"
            TAG="${sorted[i]}"
        else
            QEMU_CPUS=$QEMU_CPUS"${sorted[i]}"
            if [[ ${sorted[i]}  != ${sorted[-1]} ]];then
                QEMU_CPUS=$QEMU_CPUS","
            fi
        fi
    done
    echo ${QEMU_CPUS}
}
```