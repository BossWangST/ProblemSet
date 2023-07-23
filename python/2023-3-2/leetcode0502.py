from functools import *
from typing import *
from itertools import *


class Solution:
    def printBin(self, num: float) -> str:
        res = ''
        cur = 0
        while cur < 30:
            num *= 2
            if num > 1:
                res += '1'
                num -= 1
                if num == 0:
                    break
            else:
                res += '0'
            cur += 1
        res = '0.' + res
        return res


s = Solution()
print(s.printBin(0.625))
