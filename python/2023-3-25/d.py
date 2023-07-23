from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *

nums = list(map(int, input().split()))
s = list(defaultdict(Counter))
cur = Counter()
for num in nums:
    cur[num] += 1
    s.append(cur.copy())

d = {}
for r in range(len(s)):
