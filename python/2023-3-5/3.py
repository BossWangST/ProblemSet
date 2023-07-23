import operator
from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *


class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        prime = []
        r = {}
        for num in nums:
            cur = {}
            while num % 2 == 0:
                cur[2] = cur.get(2, 0) + 1
                r[2] = r.get(2, 0) + 1
                num //= 2
            f = 3
            while f * f <= num:
                if num % f == 0:
                    cur[f] = cur.get(f, 0) + 1
                    r[f] = r.get(f, 0) + 1
                    num //= f
                else:
                    f += 2
            if num != 1:
                cur[num] = 1
                r[num] = r.get(num, 0) + 1
            prime.append(cur)
        # p = list(accumulate(nums, func=operator.mul))
        # p = reduce(lambda x, y: x * y, nums)
        l = {}
        for i in range(len(nums) - 1):
            for p, v in prime[i].items():
                l[p] = l.get(p, 0) + v
                if p in r:
                    r[p] -= v
                    if r[p] == 0:
                        del r[p]

            if len(set(l.keys()) & set(r.keys())) == 0:
                return i
        return -1


s = Solution()
print(s.findValidSplit([4, 7, 15, 8, 3, 5]))
