from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        n = len(height)
        maxL, maxR = [0 for _ in range(n)], [0 for _ in range(n)]
        m = 0
        for i in range(n):
            maxL[i] = m
            m = max(m, height[i])
        m = 0
        for i in range(n - 1, -1, -1):
            maxR[i] = m
            m = max(m, height[i])
        res = 0
        for i in range(n):
            cur = min(maxL[i], maxR[i]) - height[i]
            if cur > 0:
                res += cur
        return res
        '''
        # 2 PTR, key is the MIN(L, R)
        n = len(height)
        l, r = 0, n - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while l < r:
            if maxL <= maxR:
                l += 1
                if maxL - height[l] > 0:
                    res += maxL - height[l]
                maxL = max(maxL, height[l])
            else:
                r -= 1
                if maxR - height[r] > 0:
                    res += maxR - height[r]
                maxR = max(maxR, height[r])
        return res


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
