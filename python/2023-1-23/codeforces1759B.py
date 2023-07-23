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

    n, s = map(int, input().split())
    nums = sorted(list(map(int, input().split())))

    p = 1
    i = 0
    while i < n:
        if p == nums[i]:
            p += 1
            i += 1
        else:
            s -= p
            p += 1
    if s == 0:
        print('YES')
    elif s < 0:
        print('NO')
    while s > 0:
        s -= p
        p += 1
        if s == 0:
            print('YES')
        elif s < 0:
            print('NO')
