from typing import List
import collections
import bisect
import functools
import math
import itertools
import heapq


class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        p, n = 0, len(s)
        one_zero, zero_one = 0, 0
        while p < n:
            if s[p] == '1' and target[p] == '1':
                return True
            if s[p] == '1' and target[p] == '0':
                one_zero += 1
            elif s[p] == '0' and target[p] == '1':
                zero_one += 1
            p += 1

        if one_zero > 0 and zero_one > 0:
            return True
        elif one_zero == 0 and zero_one == 0:
            return True
        else:
            return False


"""
        if zero_one == one_zero:
            return True
        if zero_one > one_zero:
            zero_one -= one_zero
            if zero_one == one_zero:
                return True
            else:
                return False
        if zero_one < one_zero:
            return True
"""

s = Solution()
# print(s.makeStringsEqual("100101000101110001",
# "000101000000110001"))
print(s.makeStringsEqual('001000', '000100'))
