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
    l = int(input())
    word = input()
    s = set()
    for r in range(1, l):
        cur = word[r - 1:r + 1]
        if cur not in s:
            s.add(cur)

    print(len(s))