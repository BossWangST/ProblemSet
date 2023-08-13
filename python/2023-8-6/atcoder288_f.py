from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *

n = int(input())
x = input()

s = 0  # bit for set
target = 1 << (n - 1)
res = 0


def func():
    i = 1
    cur = x[0]
    p = 1
    k = 1 << (n - 2)
    while k > 0:
        if s & k:
            p *= int(cur) % 998244353
            cur = x[i]
        else:
            cur += x[i]
        i += 1
        k >>= 1
    return p * int(cur) % 998244353


while s < target:
    res += func()
    res %= 998244353
    s += 1

print(res)
