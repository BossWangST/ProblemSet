from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        # cur = n
        '''
        flag = True
        cur_idx = 1
        while cur > 0:
            if cur & 1 == 1:
                if not flag:
                    ori_idx = cur_idx
                    while n >> ori_idx == 1:
                        ori_idx += 2
                    n += (1 << ori_idx)
            cur_idx += 1
            cur >>= 1
            flag = not flag
        '''
        res = ''
        cur = -n
        while cur != 0:
            res += format(cur % 2, 'b')
            cur //= -2
        return res[::-1]
        # return format(n, 'b')


s = Solution()
# print(s.baseNeg2(2))
print(s.baseNeg2(6))
