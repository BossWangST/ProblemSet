from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *


def test(point):
    for i in range(len(point)):
        point[i] += 1


a = [1, 2, 3, 4, 5, 60]
test(a)
print(a)
