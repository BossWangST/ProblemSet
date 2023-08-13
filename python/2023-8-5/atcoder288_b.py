from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *

n, k = map(int, input().split())
name = []
for _ in range(k):
    name.append(input())
name.sort()
for i in range(k):
    print(name[i])