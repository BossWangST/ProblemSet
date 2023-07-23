from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        cur_m = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                res -= 1
                continue
            if nums[i] == 1:
                continue
            if nums[i] & 1:
                nums[i] -= 1
                res += 1
            cur = 0
            while True:
                nums[i] //= 2
                cur += 1
                if nums[i] == 1:
                    break
                if nums[i] & 1:
                    nums[i] -= 1
                    res += 1
            cur_m = max(cur_m, cur)
        return res + cur_m + len(nums)


s = Solution()
print(s.minOperations([0]))
