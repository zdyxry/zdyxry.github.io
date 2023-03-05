---
title: 2020 第17周 LeetCode 记录
date: 2020-04-24 20:47:03
tags:
- LeetCode
---

### 1417. Reformat The String

重新格式化字符串，使得字母与数字交叉连接，先分别找出字母与数据，使用 zip_longest 来生成交叉后的元组，然后拼接得到目标字符串。


```python
class Solution:
    def reformat(self, s: str) -> str:
        a=re.findall(r'\d',s)
        b=re.findall(r'[a-z]',s)
        if abs(len(a)-len(b))>1:
            return ''
        a,b=sorted([a,b],key=len)
        return ''.join(map(''.join,itertools.zip_longest(b,a,fillvalue='')))
```

### 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K

参考：https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/solution/tan-xin-jian-dan-zheng-ming-by-wyjoutstanding/

判定性：保证K一定能由斐波那契数组成，数据归纳法可证明

最小性：什么样的组合能最短？

* 相邻合并：2个相邻的数可合并为二者的和，长度-1，因为f(n)=f(n-1)+f(n-2)。满足该条件的组合必定是间隔出现，但是又可能重现重复的值，这对于编程很不利。
* 重值转换：两个相同的值一定可以转换为两个不同的值，因为f(n)+f(n)=f(n)+f(n-1)+f(n-2)=f(n+1)+f(n-2)，一个比f(n)大，一个更小，这是等价转换，不会减小组合长度，但是会带来一个很好的性质，即单调递增性质。

因此，重复使用以上两个操作后的组合数列，必定是一个无相邻值的递增数列，由于数列均为正数且和为K，因此值越大个数自然越小。


问：
> 那会不会出现一种情况呢，就是如果减去最大的斐波那契数的话，剩下的数只能拆分成两个斐波那契数，而如果减去第二大的斐波那契数或者更小的斐波那契数的话，剩下的数刚好是斐波那契数？

答：

可用反证法，假设总和为k，且f(m-1)<k<f(m)  
那么对应你的第一种情况是k=f(m-1)+f(i)+f(j)，1<=f(i),f(j)<=f(m-2)；  
对应你的第二种情况是k=f(m-2)+f(l)，其中,1<=f(l)<=f(m-3)。  

假设你说的情况成立，那么以上两个等式必定相等，即f(m-1)+f(i)+f(j)=f(m-2)+f(l)，  
因为f(m-1) = f(m-2) + f(m-3), f(l)<=f(m-3)，而f(i)和f(j)均不可能为0，因此等式不可能成立。  
（左侧恒大于右侧，只有消去f(i)和f(j)才有可能取等）  
当第二个等式的f(m-2)取更小值时更不可能成立。因此，推翻假设。  


```python
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        ls=self.fib(k)
        res=0
        while k:
            if k>=ls[-1]:
                k-=ls[-1]
                res+=1
            else:
                ls.pop()
        return res

    def fib(self, N) -> int:
        a, b = 0, 1
        res = []
        while b <= N:
            res.append(b)
            a, b = b, a + b
        return res

```


### 1415. The k-th Lexicographical String of All Happy Strings of Length n

使用 dfs 求解，每次传入下一层时需要去除当前层最后一个字母；  
不需要算出所有长度为 n 的值，在得到第 k 个时可以直接返回。

```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.res = ""
        self.n = n
        self.k = k
        def dfs(cur, tmp):
            if len(cur) == self.n:
                self.k -= 1
                if self.k == 0:
                    self.res = cur
                    return
                return
            for i in tmp:
                if self.res:
                    return self.res
                new_tmp = [j for j in ["a", "b", "c"] if j != i]
                dfs(cur+i, new_tmp)
        dfs("", ["a", "b", "c"])
        return self.res
```


### 1419. Minimum Number of Frogs Croaking

可以转换为求在 `croak` 周期内，出现多少个 `c`，需要考虑边界情况，`croak` 字母出现次数永远是按照顺序依次递减的，如果出现递增情况直接返回 -1；最终遍历结束后应该保证 `croak` 中的各个字母出现次数相同，且不存在出现 `croak` 一半的情况，比如 存在 `cro` ，如果存在则直接返回 -1。

```python
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c, r, o, a, k, in_use, answer = 0, 0, 0, 0, 0, 0, 0
        for d in croakOfFrogs:
            if d == 'c':
                c, in_use = c+1, in_use+1
            elif d == 'r':
                r += 1
            elif d == 'o':
                o += 1
            elif d == 'a':
                a += 1
            else:
                k, in_use = k+1, in_use-1

            answer = max(answer, in_use)

            if c < r or r < o or o < a or a < k:
                return -1

        if in_use == 0 and c == r and r == o and o == a and a == k:
            return answer

        return -1
```


### 926. Flip String to Monotone Increasing

动态规划，dp[i][0] 表示以 0 为结尾时，翻转的次数；dp[i][1] 表示以 1 为结尾是，翻转的次数；

当 i == 0 时，dp[i][0] = dp[i-1][0]，无需操作；  
当 i == 0 时，dp[i][1] = min(dp[i-1][1], dp[i-1][0]) + 1，当 dp[i-1][1] 时，那么次数的 i = 0 ，需要翻转为 1，需 +1；当 dp[i-1][0] 时，此时要求以 1 为结尾需要翻转的次数，那么就需要将 i 翻转为 1，需 +1;  

当 i == 1 时，dp[i][0] = dp[i - 1][0] + 1 ，因为此时要求以 0 为结尾，需要将 i 翻转为 0，需 +1;  
当 i == 1 时，dp[i][1] = min(dp[i - 1][1], dp[i - 1][0])，dp[i-1][1] 且当前 i == 1，所以无需操作；dp[i-1][0] 表示之前都是0且结尾是0，那么此时 i == 1 也符合递增情况无需操作。

简化后：

```python
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        N = len(S)
        dp = [0] * 2
        for i in range(1, N + 1):
            if S[i - 1] == '0':
                dp[0] = dp[0]
                dp[1] = min(dp[1], dp[0]) + 1
            else:
                dp[1] = min(dp[1], dp[0])
                dp[0] = dp[0] + 1
        return min(dp[0], dp[1])
```