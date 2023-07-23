from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0, 20: 0}
        for x in bills:
            d[x] += 1
            if x - 5 == 5:
                d[5] -= 1
                if d[5] < 0:
                    return False
            elif x - 5 == 15:
                if d[5] > 0 and d[10] > 0:
                    d[5] -= 1
                    d[10] -= 1
                elif d[5] > 2:
                    d[5] -= 3
                else:
                    return False
        return True


s = Solution()
print(s.lemonadeChange([5, 5, 5, 5, 20, 20, 5, 5, 20, 5]))
