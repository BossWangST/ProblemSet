from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        z, o = 0, 0
        res = 0
        cur = False
        for c in s:
            if c == '0':
                if cur:
                    z, o = 0, 0
                    cur = False
                z += 1
            else:
                cur = True
                o += 1
                if o <= z:
                    res = max(res, o * 2)
        return res


s = Solution()
print(s.findTheLongestBalancedSubstring('01000111'))
