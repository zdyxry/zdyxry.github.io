---
title: 2020 第28周 LeetCode 记录
date: 2020-07-11 21:50:54
tags:
- LeetCode
---

### 1502. Can Make Arithmetic Progression From Sequence

判断是否可以组成等差数列，将数组排序后，比较两两数字差是否一致。

```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True
        arr.sort(reverse=True)
        diff = arr[0] - arr[1]
        pre = arr[1]
        for i in arr[2:]:
            if pre - i != diff:
                return False
            pre = i
        return True

```

### 1503. Last Moment Before All Ants Fall Out of a Plank

标签是“脑筋急转弯”，蚂蚁只要在一个点碰到，那么就会调换方向，但是蚂蚁始终是蚂蚁，因此可以忽略掉这个条件，直接找到最大值就可以了。

再次怀疑自己智商。

```python
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        time = 0
        if left:
            time = max(time, max(left))
        if right:
            time = max(time, n - min(right))
        return time
```


### 939. Minimum Area Rectangle

一般会选择完整本周周赛题目，然后去做其他的题，但是 1504 做不出，就找了到也是矩形相关的补一补 - - 。

找出最小矩形面积，需要先找到组成矩形的四个点，遍历所有点，将其记录下来，并遍历已记录的点，此时拿到了两个点，直接暴力判断这两个点的对称点是否存在，如果存在，则计算面积并更新。


```python
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        area = 0
        mem = set()
        for x1,y1 in points:
            for x2,y2 in mem:
                if (x2,y1) in mem and (x1,y2) in mem:
                    if not area:
                        area = abs(x2-x1)*abs(y2-y1)
                    else:
                        if abs(x2-x1)*abs(y2-y1) < area:
                            area = abs(x2-x1)*abs(y2-y1)
            mem.add((x1,y1))
        return area
```

### 1160. Find Words That Can Be Formed by Characters

使用 Counter 统计词汇表中的字母，遍历单词，如果单词中的每个字母数量小于词汇表中的字母数量，那么满足条件，否则跳出循环。


```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_cnt = collections.Counter(chars)
        ans = 0
        for word in words:
            word_cnt = collections.Counter(word)
            for c in word_cnt:
                if chars_cnt[c] < word_cnt[c]:
                    break
            else:
                ans += len(word)
        return ans
```

### 1048. Longest String Chain

先对所有单词进行排序，使用哈希表记录当前单词所能组成的最长字符串链的长度。当遍历到某个单词是，通过字符串切片，判断其所有可能的情况，如果记录中存在，那么与当前最大值进行比较更新。


```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        note={}
        maxChain=1
        for word in words:
            if word not in note:
                note[word]=1
            for i in range(0,len(word)):
                newWord=word[:i]+word[i+1:]
                if (newWord) in note:
                    note[word]=max(note[word],note[newWord]+1)
            maxChain=max(maxChain,note[word])
        return maxChain
```