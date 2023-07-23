from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = list(accumulate(nums, initial=0))
        # if x = sum(nums), y = sum(deleted subarray)
        # (x - y) % p == 0 <==> x % p == y % p
        x = s[-1]
        # Here we need to find a y to satisfy y % p == target
        # ==> (r - l) % p == x % p ==> (r - x) % p == l % p

        if x % p == 0:
            return 0
        d = {}
        res = len(nums)
        for i in range(len(s)):
            d[s[i] % p] = i  # record l % p
            cur = (s[i] - x) % p  # (r - x) % p
            if d.get(cur, -1) >= 0:
                res = min(res, i - d[cur])
        return res if res != len(nums) else -1


s = Solution()
print(s.minSubarray([1, 2, 3], 7))
