from functools import *
from typing import *
from itertools import *

N, Q = list(map(int, input().split()))
d = [0 for _ in range(N)]
while Q > 0:
    Q -= 1
    c, x = list(map(int, input().split()))
    x -= 1
    if c == 1:
        d[x] += 1
    elif c == 2:
        d[x] += 2
    else:
        if d[x] >= 2:
            print('Yes')
        else:
            print('No')
