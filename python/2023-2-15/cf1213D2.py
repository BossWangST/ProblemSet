from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *

n, k = map(int, input().split())
nums = list(map(int, input().split()))

val = [[] for _ in range(200001)]
for a in nums:
    temp = a
    step = 0
    while temp > 0:
        val[temp].append(step)
        temp //= 2
        step += 1

res = float('inf')
for i in range(200001):
    if len(val[i]) < k:
        continue
    val[i].sort()
    res = min(res, sum(val[i][:k]))

print(res)
