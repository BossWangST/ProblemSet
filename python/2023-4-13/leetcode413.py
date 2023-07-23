from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        diff = []
        for i in range(1, len(nums)):
            diff.append(nums[i] - nums[i - 1])
        cur = diff[0]
        cur_len = 1
        res = 0
        for i in range(1, len(diff)):
            if cur == diff[i]:
                cur_len += 1
            else:
                cur = diff[i]
                if cur_len >= 2:
                    res += cur_len * (cur_len - 1) // 2
                cur_len = 1
        if cur_len >= 2:
            res += cur_len * (cur_len - 1) // 2
        return res


s = Solution()
print(s.numberOfArithmeticSlices([1, 2, 3, 8, 9, 10]))
