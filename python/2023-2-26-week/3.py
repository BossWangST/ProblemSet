from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        nums = list(map(int, word.strip()))
        res = []
        n = len(nums)
        cur = 0
        for i in range(n):
            cur = cur * 10 + nums[i]
            cur %= m
            if cur == 0:
                res.append(1)
            else:
                res.append(0)
        return res


s = Solution()
print(s.divisibilityArray('1010', 10))
