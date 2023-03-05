---
title: 2020 第11周 LeetCode 记录
date: 2020-03-13 21:09:45
tags:
- LeetCode
---


### 1370. Increasing Decreasing String

题目描述很复杂，但其实就是排序和字典，先顺序遍历再反向遍历。（熟练使用 Counter）

#### Python

```python
class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        set_s = set()
        for c in s:
			set_s.add(c)
        characters = sorted(set_s)

        d = collections.Counter(s)
        res = ""
        while sum(d.values()) != 0:
            for c in characters:
                if c in s and d[c] > 0:
                    res += c
                    d[c] -= 1
            for c in characters[::-1]:
                if c in s and d[c] > 0:
                    res += c
                    d[c] -= 1
        return res
```

#### Golang

```go
func sortString(s string) string {
	sMap := make(map[string]int, len(s))
	for _, c := range s {
		sMap[string(c)]++
	}
	chars := []string{}
	for c, _ := range sMap {
		chars = append(chars, string(c))
	}
	sort.Strings(chars)
	res := ""
	for len(sMap) > 0 {
		for i := range chars {
			if sMap[chars[i]] > 0 {
				res += string(chars[i])
				sMap[chars[i]]--
			} else {
				delete(sMap, chars[i])
			}
		}
		for i := range chars {
			if sMap[chars[len(chars)-i-1]] > 0 {
				res += string(chars[len(chars)-i-1])
				sMap[chars[len(chars)-i-1]]--
			} else {
				delete(sMap, chars[len(chars)-i-1])
			}
		}
	}
	return res
}
```

### 1371. Find the Longest Substring Containing Vowels in Even Counts

采用状态压缩的方式，将每个元音字母出现次数的奇偶作为一种状态，1 表示为奇数次，0表示偶数次，那么一共有 2^5=32 种状态。遍历所有的字符，如果当前字符是元音字母，那么就进行异或操作，并记录此时状态。如果子串[0，i]与字串[0,j]状态相同，那么字串[i+1,j]的状态一定是0，因此可以记录每个状态第一次出现的位置，此后再出现该状态时相减即可。

来源：https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/solution/jian-dan-de-si-lu-by-mnizy/


需要将状态 0 出现的位置设置为 -1，比如 "ele" ，当循环到第一个 e 时，e 出现奇数次，当循环到第二个 e 时，e 出现偶数次，此时 "ele" 符合条件，且状态为 0，那么需要用第二个 e 的索引值减去状态0 出现的位置，如果状态0 为空，那么第二个e 的状态0就会被当作第一次出现记录下来，导致结果错误，应为 2 - (-1) = 3。


```python
class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        d, n, r = {0: -1}, 0, 0
        for i, c in enumerate(s):
            if c in vowels:
                n ^= vowels[c]
            if n not in d:
                d[n] = i
            else:
                r = max(r, i - d[n])
        return r
```


### 1372. Longest ZigZag Path in a Binary Tree


二叉树中的最长交错路径，使用 dfs 求解，dfs 返回值是[node.left 的最大长度，node.right 的最大长度，node 的最大长度]。
这里需要考虑当 root 为 None 时的返回值是多少，因为每递归一层，都需要在上一层将结果 +1 ，如果 root == None，那么 -1 + 1 = 0 。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return [-1, -1, -1]
            left, right = dfs(root.left), dfs(root.right)
            return [left[1] + 1, right[0] + 1, max(left[1]+1, right[0]+1, left[2], right[2])]
        return dfs(root)[-1]

```

换一种方式比较好理解，传入两个参数：count 和当前所在的是 node 的 left 还是 right，如果上一层是 left，那么就在 node.right 将 count +1，否则将 count 置为1重新计数。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def dfs(node, count, direction):
            if node:
                if count > self.res:
                    self.res = count
                if direction == 'left':
                    dfs(node.right, count+1, 'right')
                    dfs(node.left, 1, 'left')
                else:
                    dfs(node.left, count+1, 'left')
                    dfs(node.right, 1, 'right')
        
        if root.left:
            dfs(root.left, 1, 'left')
        if root.right:
            dfs(root.right, 1, 'right')
        return self.res
```


### 1375. Bulb Switcher III

属于那种题目很复杂，做起来很简单的类型，只需要判断当前最大值与当前索引是否相当即可。


```python
class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        res = 0
        max_idx = 0
        for i, b in enumerate(light):
            max_idx = max(max_idx, b)
            if i+1 == max_idx:
                print b
                res+= 1
        return res
```


### 1376. Time Needed to Inform All Employees

使用 DFS 求解，先确定每个员工及它所负责通知的员工，再根据 headID 递归求解。


```python
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        children = [[] for i in xrange(n)]
        for i, m in enumerate(manager):
            if m >= 0: children[m].append(i)

        def dfs(i):
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
        return dfs(headID)
```

也可以自底向上求解，为避免重复计算，将每次计算结果记录下来。

```python
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        def dfs(i):
            if manager[i] != -1:
                informTime[i] += dfs(manager[i])
                manager[i] = -1
            return informTime[i]
        return max(map(dfs, range(n)))
```