from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        m1, m2 = len(num1), len(num2)
        l = min(m1, m2)
        nxt = 0
        i = 1
        while i <= l:
            cur = int(num1[-i]) + int(num2[-i]) + nxt
            if cur >= 10:
                nxt = cur // 10
                cur %= 10
            else:
                nxt = 0
            res = str(cur) + res
            i += 1
        l = m1 if m1 > m2 else m2
        num = num1 if m1 > m2 else num2
        while i <= l:
            cur = int(num[-i]) + nxt
            if cur >= 10:
                nxt = cur // 10
                cur %= 10
            else:
                nxt = 0
            res = str(cur) + res
            i += 1
        if nxt > 0:
            res = str(nxt) + res
        return res


s = Solution()
print(s.addStrings('1', '9'))
