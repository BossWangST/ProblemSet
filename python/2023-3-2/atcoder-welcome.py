from functools import *
from typing import *
from itertools import *

a = int(input())
b, c = list(map(int, input().split()))
s = input()

print(a + b + c, s)