from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *

t = int(input())

while t > 0:
    t -= 1
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a2 = sorted(list(enumerate(a)), key=lambda x:x[1])
    b.sort()
    vis = [False for _ in range(n)]
    res = [0 for _ in range(n)]
    for i in range(n):
        res[a2[i][0]] = b[i]

    for r in res:
        print(r, end=' ')
    print()