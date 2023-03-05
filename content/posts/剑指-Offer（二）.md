---
title: 剑指 Offer（二）
date: 2018-11-20 21:08:14
tags:
- alogrithms
---

## 数值的整数次方

```python
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# 考虑边界情况，base = 0, exponent < 0, exponent = 0 场景。
def equal_zero(num):
    if abs(num - 0.0) < 0.0000001:
        return True


def power(base, exponent):
    if equal_zero(base):
        result = False
    if exponent == 0:
        result = 1
    result = power(base, abs(exponent) >> 1)
    result *= result
    if abs(exponent) & 1 == 1:
        result *= base
    if exponent < 0:
        result = 1.0 / result
    return result

power_value(2, 2)
```
