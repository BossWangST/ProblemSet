from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *

t = int(input())

while t > 0:
    t -= 1

    k, n = map(int, input().split())
    """
    将题目进行转化，为找到一个差值的数组 [d1, d2, d3 ... dn] 其中 di = d(i+1) - di
    那么这个数组的和就不能超过 n - 1 (an - a1)
    为了让 di 尽可能的不同，且保证数字增长不超过 n 
    则构造出一个这样的数组: [2, 3, 4, ... , f, 1, 1, 1]
    找到最大的 f 即可
    """
    res = []
    d = [1 for _ in range(k - 1)]
    f, p = 1, 0
    while p < k - 1 and sum(d) <= n - 1:
        d[p] += f
        f += 1
        p += 1
    # 注意判断 f 是否走过了
    if sum(d) > n - 1:
        d[p - 1] -= f - 1
    a = 1
    res.append(a)
    for i in range(1, k):
        a += d[i - 1]
        res.append(a)
    print(*res, sep=' ')
