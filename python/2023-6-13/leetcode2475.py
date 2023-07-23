from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        two = -1

        res = 0
        for k in range(len(nums) - 2):
            one = nums[k]
            for i in range(k + 1, len(nums) - 1):
                if nums[i] != one:
                    two = nums[i]
                    for j in range(i + 1, len(nums)):
                        if nums[j] != one and nums[j] != two:
                            res += 1
        return res


s = Solution()
print(s.unequalTriplets([1, 3, 1, 2, 4]))
