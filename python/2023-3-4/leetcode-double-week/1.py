from functools import *
from typing import *
from itertools import *
from math import *
from collections import *


class Solution:
    def splitNum(self, num: int) -> int:
        s = list(str(num).strip())
        p, n = 0, len(s)
        num1, num2 = 0, 0
        flag = True
        while p < n:
            if flag:
                num1 += int(s[p])
                num1 *= 10
                flag = False
            else:
                num2 += int(s[p])
                num2 *= 10
                flag = True
            p += 1
        return num1 // 10 + num2 // 10


s = Solution()
print(s.splitNum(4325))