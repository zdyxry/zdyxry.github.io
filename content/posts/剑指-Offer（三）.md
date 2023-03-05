---
title: 剑指 Offer（三）
date: 2018-11-25 10:29:46
tags:
- alogrithms
---


## 打印1到最大的n位数

```python
# 将数组转换为字符
def print_number(number):
    is_beginning_0 = True
    num_len = len(number)

    for i in range(num_len):
        if is_beginning_0 and number[i] != "0":
            is_beginning_0 = False
        if not is_beginning_0:
            print("%c" % number[i], end="")
    print("")

# 边界条件：n > 0
def print_1_to_max_of_n1(n):
    if n <= 0:
        return 
    
    number = ["0"] * n
    while not increment(number):
        print_number(number)

# 从最后一位开始计算，如果 最后一位增长为10，则重置为 0，且进位；如果首位增长为 10，则溢出
def increment(number):
    is_carry = 0
    is_overflow = False
    sum = 0
    num_len = len(number)

    for i in range(num_len - 1, -1, -1):
        sum = int(number[i]) + is_carry
        if i == num_len - 1:
            sum += 1
        
        if sum >= 10:
            if i == 0:
                is_overflow = True
            else:
                sum -= 10
                number[i] = str(sum)
                is_carry = 1
        else:
            number[i] = str(sum)
            break

    return is_overflow
        

def print_1_to_max_of_n2(n):
    if n <= 0:
        return
    
    number = ["0"] * n
    for i in range(10):
        number[0] = str(i)
        print_1_to_max_of_n_recursively(number, n, 0)

# 始终找到最后一位，并将其计算
def print_1_to_max_of_n_recursively(number, num_len, index):
    if index == num_len - 1:
        print_number(number)
        return
    for i in range(10):
        number[index + 1] = str(i)
        print_1_to_max_of_n_recursively(number, num_len, index +1)


print_number(["0", "1", "1"])
print_1_to_max_of_n1(2)
print_1_to_max_of_n2(2)
```
