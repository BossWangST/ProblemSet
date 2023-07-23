from collections import *
from functools import *
from typing import *
from itertools import *
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        tab = [1 if i > 8 else -1 for i in hours]
        s = list(accumulate(tab))
        s.insert(0, 0)
        n = len(s)
        res = 0
        stk = [(0, 0)]
        for i in range(1, n):
            if s[i] < stk[-1][1]:
                stk.append((i, s[i]))
        for i in range(n - 1, 0, -1):
            while len(stk) > 0 and s[i] > stk[-1][1]:
                res = max(res, i - stk[-1][0])
                stk.pop()
        return res

s=Solution()
print(s.longestWPI([6, 6, 9]))