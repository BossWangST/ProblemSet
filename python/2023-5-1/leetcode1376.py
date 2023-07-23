from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = defaultdict(list)
        for i in range(n):
            if i == headID:
                continue
            d[manager[i]].append(i)
        q = [headID]
        res = 0
        while len(q) > 0:
            m = max(0, max(informTime[i] for i in q))
            m_idx = informTime.index(m)
            for i in range(len(q)):
                cur = q.pop(0)
                if cur not in d:
                    continue
                for idx in d[cur]:
                    q.append(idx)
                if cur != m_idx:
                    for nxt_idx in d[cur]:
                        informTime[nxt_idx] -= m - informTime[cur]
            res += m
        return res


s = Solution()
print(s.numOfMinutes(11, 4, [5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4],
                     [0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337]))
