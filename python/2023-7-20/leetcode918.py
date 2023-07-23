from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        l, n = 0, len(nums)
        nums.extend(nums[:-1])
        res = float('-inf')
        cur = 0
        for i in range(len(nums)):
            if l == n:
                cur -= nums[i - l]
                l -= 1
            cur += nums[i]
            l += 1
            res = max(res, cur)
            if cur <= 0:
                cur = 0
                l = 0
        return res


s = Solution()
print(s.maxSubarraySumCircular([5, -3, 5]))
