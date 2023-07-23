from functools import *
from typing import *
from itertools import *
from math import *
from collections import *

from math import sqrt
A, B = list(map(int, input().split()))
if A > B:
    if B * sqrt(3) / 2 > A / 2:
        print(B)
    else:
        print(B * (sqrt(6) - sqrt(2)))
else:
    if A * sqrt(3) / 2 > B / 2:
        print(A)
    else:
        print(A * (sqrt(6) - sqrt(2)))