from functools import *
from typing import *
from itertools import *
from math import *

N = int(input())
nums = [0 for _ in range(N)]
nums[1] = 1
for i in range(2, N):
    cur = sqrt(i)
    for j in range(1, int(cur) + 1):
        if i % j == 0:
            nums[i] += 1
    nums[i] *= 2
    if i == int(cur) * int(cur):
        nums[i] -= 1

res = 0
for i in range(1, N):
    a, b = i, N - i
    res += nums[a] * nums[b]
print(res)
