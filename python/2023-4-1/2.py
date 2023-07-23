from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        d = {}
        for i in range(len(chars)):
            d[chars[i]] = vals[i]
        for i in range(26):
            c = chr(ord('a') + i)
            if c not in d:
                d[c] = i + 1
        cur = []
        for c in s:
            cur.append(d[c])
        cur_s = 0
        res = 0
        for num in cur:
            cur_s += num
            res = max(res, cur_s)
            if cur_s < 0:
                cur_s = 0
        return res


s = Solution()
print(s.maximumCostSubstring('aaabc', 'abc', [1, -1, 1]))
