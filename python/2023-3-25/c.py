from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *

n = int(input())
a = list(map(int, input().split()))
b = Counter(a)
res = 0
for k, v in b.items():
    res += v // 2

print(res)
