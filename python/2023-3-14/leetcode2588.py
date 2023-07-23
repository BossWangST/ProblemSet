import operator
from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        '''
        res, cur = 0, [0 for _ in range(len(nums))]
        cur[0] = nums[0]
        if cur[0] == 0:
            res += 1
        for i in range(1, len(nums)):
            cur[i] ^= cur[i - 1] ^ nums[i]
            if cur[i] == 0:
                res += 1
        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                cur[j] ^= nums[i - 1]
                if cur[j] == 0:
                    res += 1
        return res
        '''
        p = list(accumulate(nums, func=operator.xor, initial=0))
        d = {}
        res = 0
        for i in range(len(p)):
            # r ^ l == 0
            # ==> r ^ r = 0 ==> r = l
            if d.get(p[i], -1) >= 0:
                res += d[p[i]]
            d[p[i]] = d.get(p[i], 0) + 1
        return res


s = Solution()
print(s.beautifulSubarrays([4, 3, 1, 2, 4]))
