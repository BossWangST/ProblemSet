from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        if len(nums) == 1:
            return 0
        l, r = 0, 1
        while r < len(nums):
            if nums[l] < nums[r]:
                res += 1
                l += 1
                r += 1
                continue
            r += 1
        return res


s = Solution()
print(s.maximizeGreatness([1, 2, 3, 4]))
