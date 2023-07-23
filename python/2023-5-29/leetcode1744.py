from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        l = list(accumulate(candiesCount))
        res = []
        for t, day, cap in queries:
            consume = l[t - 1] if t > 0 else 0
            cur_day = day
            # we need to eat "consume" candies within "cur_day"
            if cur_day * cap >= consume:
                if consume < cur_day and candiesCount[t] - (cur_day - consume) <= 0:
                    res.append(False)
                else:
                    res.append(True)
            else:
                if consume - cur_day * cap >= cap:
                    res.append(False)
                else:
                    res.append(True)
        return res


s = Solution()
print(s.canEat(
    [16, 38, 8, 41, 30, 31, 14, 45, 3, 2, 24, 23, 38, 30, 31, 17, 35, 4, 9, 42, 28, 18, 37, 18, 14, 46, 11, 13, 19, 3,
     5, 39, 24, 48, 20, 29, 4, 19, 36, 11, 28, 49, 38, 16, 23, 24, 4, 22, 29, 35, 45, 38, 37, 40, 2, 37, 8, 41, 33, 8,
     40, 27, 13, 4, 33, 5, 8, 14, 19, 35, 31, 8, 8],
    [[43, 1054, 49]]))
