from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        s = sum(list(map(int, list(str(n).strip()))))
        if s <= target:
            return 0
        cur = n % 10
        res = 0
        v = 1
        flag = False
        while cur == 9:
            flag = True
            s = s - cur
            n //= 10
            v *= 10
            cur = n % 10
        if flag:
            res += 1
            s += 1
            n += 1
            cur = cur + 1
        while s > target:
            res += (10 - cur) * v
            s = s - cur + 1
            n //= 10
            v *= 10
            nxt = n % 10
            while nxt == 9:
                s -= nxt
                n //= 10
                v *= 10
                nxt = n % 10
            n += 1
            cur = nxt + 1
        return res


s = Solution()
print(s.makeIntegerBeautiful(999, 1))
