from functools import *
from typing import *
from itertools import *

N, Q = list(map(int, input.split()))
b = [chr(ord('A') + i) for i in range(N)]
w = [0 for _ in range(N)]
while Q > 0:
    Q -= 1
