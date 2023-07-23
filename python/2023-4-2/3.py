from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        '''
        @lru_cache(None)
        def dfs(idx: int, cur: int, k: int) -> int:
            if idx == len(reward1):
                return cur, k == 0
            if len(reward1) - idx < k:
                return 0, False
            if k > 0:
                eat, valid1 = dfs(idx + 1, cur + reward1[idx], k - 1)
            else:
                eat, valid1 = 0, True
            no_eat, valid2 = dfs(idx + 1, cur + reward2[idx], k)
            if valid1 and valid2:
                return max(eat, no_eat), True
            if valid1:
                return eat, True
            if valid2:
                return no_eat, True
            return 0, False
        '''
        cur = []
        for i in range(len(reward1)):
            cur.append((reward1[i] - reward2[i], i))
        cur.sort(key=lambda x: -x[0])
        res = 0
        for num, i in cur:
            if k > 0:
                res += reward1[i]
                k -= 1
            else:
                res += reward2[i]
        return res


s = Solution()
print(s.miceAndCheese([1, 1, 3, 4], [4, 4, 1, 1], 2))
