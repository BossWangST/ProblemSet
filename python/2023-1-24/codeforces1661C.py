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

    n = int(input())
    nums = sorted(list(map(int, input().split())))
    target = nums[n - 1]
    q = []
    for num in nums:
        num -= target
        if num < 0:
            # q.insert(bisect_left(q, num), num)
            q.append(-num)
    day = 0
    c = Counter()
    for diff in q:
        """
        if day & 1:
            q[len(q) - 1] += 1
            if q[len(q) - 1] >= 0:
                q.pop()
            day += 1
        else:
            q[0] += 2
            if q[0] >= 0:
                q.pop()
            day += 1
        """
        day += (diff // 3) * 2
        cur = diff % 3
        if cur != 0:
            c[cur] += 1
    need = min(c[1], c[2])
    day += need * 2
    c[1] -= need
    c[2] -= need
    day += c[1] + c[2] * 2
    print(day)

"""
1
7
1 1 1 1 1 1 2
"""