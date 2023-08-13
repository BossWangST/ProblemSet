from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *

n = int(input())
while n > 0:
    n -= 1
    a, b = map(int, input().split())
    print(a + b)