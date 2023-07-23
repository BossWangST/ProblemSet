from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        interval = []
        for i in range(n + 1):
            begin, end = 0, n
            if i - ranges[i] >= 0:
                begin = i - ranges[i]
            if i + ranges[i] <= n:
                end = i + ranges[i]
            interval.append((begin, end))
        p = 0
        i = 0
        res = 0
        while i < n:
            m_p = -1
            m_len = float('-inf')
            while p < n + 1:
                if interval[p][0] <= i <= interval[p][1] and m_len < interval[p][1]:
                    m_len = interval[p][1]
                    m_p = p
                p += 1
            p = m_p
            if interval[p][1] == i:
                return -1
            else:
                i = interval[p][1]
                p += 1
                res += 1
        return res


s = Solution()
print(s.minTaps(8, [4, 0, 0, 0, 4, 0, 0, 0, 4]))
