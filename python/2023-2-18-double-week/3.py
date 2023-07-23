from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        avg = round(sum(nums) / len(nums))
        nums.sort()
        nums[0], nums[-1] = avg, avg
        nums.sort()
        mi_val = float('inf')
        for i in range(1, len(nums)):
            mi_val = min(mi_val, abs(nums[i] - nums[i - 1]))
        ma_val = abs(nums[-1] - nums[0])
        return mi_val + ma_val


s = Solution()
# print(s.minimizeSum([1, 4, 3]))
# print(s.minimizeSum([1, 4, 7, 8, 5]))
# print(s.minimizeSum([1, 1, 1, 1, 9]))
# print(s.minimizeSum([1, 1, 1, 1, 1]))
# print(s.minimizeSum([1, 2, 3, 4, 5]))
print(s.minimizeSum([31, 25, 72, 79, 74, 65]))  # 14
