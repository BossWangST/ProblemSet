from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        m = float('-inf')
        n = len(citations)
        for c in citations:
            idx = bisect_left(citations, c)
            m = max(m, min(c, n - idx))
        return m


s = Solution()
print(s.hIndex([3, 0, 6, 1, 5]))
