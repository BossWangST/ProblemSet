from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        d = [{} for _ in range(len(nums))]
        c_odd = {}
        c_even = {}
        for i in range(len(nums)):
            for prime in p:
                while nums[i] % prime == 0:
                    d[i][prime] = d[i].get(prime, 0) + 1
                    nums[i] /= prime
                if d[i].get(prime, 0) > 0:
                    if d[i][prime] & 1 == 0:
                        c_even[prime] = c_even.get(prime, 0) + 1
                    else:
                        c_odd[prime] = c_odd.get(prime, 0) + 1
        res = 0
        for prime in p:
            if c_odd.get(prime, 0) > 0:
                res += ((2 ** (c_odd[prime] - 1)) * (2 ** c_even.get(prime, 0))) % 1000000007
        return res
