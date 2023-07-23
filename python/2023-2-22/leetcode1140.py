from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def dfs(cur: int, p: int, M: int) -> int:
            if p == len(piles):
                return cur
            res = []
            for i in range(1, 2 * M + 1):
                if i > M:
                    res.append(dfs(cur + sum(piles[:i]), i + 1, i))
                else:
                    res.append(dfs(cur + sum(piles[:i]), i + 1, M))
            return max(res)

        return dfs(0, 0, 1)


s = Solution()
print(s.stoneGameII([2, 7, 9, 4, 4]))
