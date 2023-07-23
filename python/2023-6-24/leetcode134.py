from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        '''
        for i in range(n - 1):
            gas.append(gas[i])
            cost.append(cost[i])
        g_l, c_l = list(accumulate(gas)), list(accumulate(cost))
        for i in range(n):
            if gas[i] >= cost[i]:
                cur = gas[i] - cost[i]
                g = g_l[i + n - 1] - g_l[i]
                c = c_l[i + n - 1] - c_l[i]
                if cur + g >= c:
                    ok = True
                    for j in range(1, n):
                        if cur + gas[i + j] >= cost[i + j]:
                            cur += gas[i + j] - cost[i + j]
                        else:
                            ok = False
                            break
                    if ok:
                        return i
        return -1
        '''
        m = 0
        cur = 0
        for i in range(n):
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                m = i + 1
        return m


s = Solution()
print(s.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))
