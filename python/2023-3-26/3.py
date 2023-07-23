from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        s = list(accumulate(nums, initial=0))

        res = []
        n = len(nums)
        for i in range(len(queries)):
            cur = bisect_left(nums, queries[i])
            left, right = s[cur], s[-1] - s[cur]
            left_res = cur * queries[i] - left
            right_res = right - (n - cur) * queries[i]
            res.append(left_res + right_res)
        return res


s = Solution()
print(s.minOperations([3, 1, 6, 8], [1, 5]))
