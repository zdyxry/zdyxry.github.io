---
title: 2020 第16周 LeetCode 记录
date: 2020-04-18 05:34:09
tags:
- LeetCode
---

### 1408. String Matching in an Array

先按照单词长度进行排序，然后遍历判断当前单词是否被其他单词包含，要注意最终结果应该是去重之后的。

Golang 中可以直接使用 `strings.Contains` 判断。


```go
type ByLen []string

func (a ByLen) Len() int {
	return len(a)
}

func (a ByLen) Less(i, j int) bool {
	return len(a[i]) < len(a[j])
}

func (a ByLen) Swap(i, j int) {
	a[i], a[j] = a[j], a[i]
}

func stringMatching(words []string) []string {
	sort.Sort(ByLen(words))
	res := []string{}
	for i := range words {
		for j := i + 1; j < len(words); j++ {
			if strings.Contains(words[j], words[i]) {
				res = append(res, words[i])
			}
		}
	}

	unique := []string{}
	for _, v := range res {
		skip := false
		for _, u := range unique {
			if v == u {
				skip = true
				break
			}
		}
		if !skip {
			unique = append(unique, v)
		}
	}
	return unique
}
```

### 1409. Queries on a Permutation With Key

数据规模较小，可以直接使用数组暴力求解。

理想方法应该是使用 Fenwick Tree 来解答，具体的方法参考：
* https://www.youtube.com/watch?v=WbafSgetDDk
* https://www.youtube.com/watch?v=DwtijVbS3G0&t=635s

```go
func processQueries(queries []int, m int) []int {
    var p = make([]int, m)
	var res = make([]int, len(queries))
	for i := 0; i < m; i++ {
		p[i] = i + 1
	}
	for index, value := range queries {
		//found value in p's index
		var i int
		for i = 0; i < len(p); i++ {
			if p[i] == value {
				res[index] = i
				break
			}
		}
		//move p
		tmp := p[i]
		copy(p[1:i+1], p[0:i])
		p[0] = tmp
	}
	return res
}
```

```python
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        tree = [0] * ((2*m) + 1)
        res = []
        
        def update(i,val):
            while i<len(tree):
                tree[i]+=val
                i+=(i&(-i))
    
        def prefixSum(i):
            s=0
            while i>0:
                s+=tree[i]
                i-=(i&(-i))
            return s
        
        hmap = collections.defaultdict(int)
        
        for i in range(1,m+1):
            hmap[i] = i+m
            update(i+m,1)

        for i in queries:
            res.append(prefixSum(hmap[i])-1)
            update(hmap[i],-1)
            update(m,1)
            hmap[i] = m
            m-=1

        return res
```

### 1410. HTML Entity Parser


字符串解析替换，遍历检查 `&` 和 `;` 进行替换，也可以直接使用 `str.replace` 进行替换，如果使用 regex 会超时。

```python
class Solution:
    def entityParser(self, text: str) -> str:
        ent = {'&quot;': '"', '&apos;':'\'' , '&gt;':'>', '&lt;':'<', '&frasl;':'/', '&amp;':'&'}
        for k, v in ent.items():
            if k in text:
                text = text.replace(k, v)
        return text
```


### 1138. Alphabet Board Path

先准备字母表，需要注意的是最后一个字母 `z`，如果目标字母是 `z` ，那么只能先左再下，如果当前字母是 `z`，那么只能先上再右，需要考虑移动的顺序。


```python
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        m = {c: [i // 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        x0, y0 = 0, 0
        res = []
        for c in target:
            x, y = m[c]
            if y < y0: res.append('L' * (y0 - y))
            if x < x0: res.append('U' * (x0 - x))
            if x > x0: res.append('D' * (x - x0))
            if y > y0: res.append('R' * (y - y0))
            res.append('!')
            x0, y0 = x, y
        return "".join(res)
```


### 1302. Deepest Leaves Sum

求最深层的叶子节点之和，需要维护 2个变量，一个是最深层次，一个是最深层次对应的和。遍历节点时与最深层次比较，进行求和运算。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = collections.deque([(root, 0)])
        maxdep, total = -1, 0
        while len(q) > 0:
            node, dep = q.pop()
            if dep > maxdep:
                maxdep, total = dep, node.val
            elif dep == maxdep:
                total += node.val
            if node.left:
                q.append((node.left, dep + 1))
            if node.right:
                q.append((node.right, dep + 1))
        return total
```