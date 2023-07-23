from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        if len(arr2) > len(arr1):
            arr1, arr2 = arr2, arr1
        tick = True  # True for ADD, False for MINUS
        arr1, arr2 = arr1[::-1], arr2[::-1]
        i, nxt = 0, 0
        while i < len(arr2):
            if tick:
                res.append(arr1[i] ^ arr2[i] ^ nxt)
                nxt = (arr1[i] & arr2[i]) | (nxt & (arr1[i] ^ arr2[i]))
            else:
                if nxt & arr2[i] & arr1[i]:
                    res.append(1)
                    nxt = -1
                elif nxt & arr2[i]:
                    res.append(0)
                    nxt = -1
                else:
                    res.append(arr1[i] - arr2[i] - nxt)
                    nxt = 0
            tick = not tick
            i += 1
        while i < len(arr1):
            if tick:
                res.append(arr1[i] ^ nxt)
                nxt = arr1[i] & nxt
            else:
                if ~arr1[i] & nxt:
                    res.append(1)
                    nxt = -1
                else:
                    res.append(arr1[i] - nxt)
                    nxt = 0
            tick = not tick
            i += 1
        bin_int = int("".join(map(str, res[::-1])), 2)
        def baseNeg2(n: int) -> str:
            if n == 0:
                return "0"
            res = ''
            cur = -n
            while cur != 0:
                res += format(cur % 2, 'b')
                cur //= -2
            return res[::-1]
        return list(map(int, list(baseNeg2(bin_int))))

s = Solution()
print(s.addNegabinary([0], [1, 0]))
print(s.addNegabinary([1], [1]))
