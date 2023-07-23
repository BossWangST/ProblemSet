from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        a = reduce(lambda x, y: x | y, nums)
        s = set(nums)
        num = 1
        while num in s:
            num <<= 1
        return num


s = Solution()
print(s.minImpossibleOR([2, 1]))
print(s.minImpossibleOR([5, 3, 2]))
