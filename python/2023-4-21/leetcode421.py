from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # a ^ b = c  <=>  a ^ c = b
        res = 0
        mask = 0
        s = set()
        for i in range(30, -1, -1):
            mask |= (1 << i)
            for num in nums:
                s.add(num & mask)

            nxt = res | (1 << i)
            for pre in s:
                if pre ^ nxt in s:
                    # s 中有这一位
                    res = nxt
                    break
            s.clear()
        return res


s = Solution()
print(s.findMaximumXOR([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))
