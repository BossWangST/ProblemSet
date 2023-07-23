from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        cur = money - children
        if cur < 0:
            return -1
        res = 0
        if cur < 7:
            return 0
        for i in range(children):
            if cur > 7 and i == children - 1:
                return children - 1
            if cur >= 7:
                cur -= 7
                res += 1
            else:
                if cur == 3 and i == children - 1:
                    return children - 2
                break
        return res


s = Solution()
print(s.distMoney(17, 2))
