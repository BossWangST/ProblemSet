from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n, cur = len(scores), []
        if n == 1:
            return scores[0]
        for i in range(n):
            cur.append((ages[i], scores[i]))
        cur.sort()
        dp = [0 for _ in range(n + 1)]
        dp[1] = cur[0][1]
        res = float('-inf')
        for i in range(2, n + 1):
            dp[i] = cur[i - 1][1]
            cur_m = float('-inf')
            for j in range(i - 1, 0, -1):
                if cur[j - 1][1] <= cur[i - 1][1]:
                    cur_m = max(cur_m, dp[j])
            if cur_m > 0:
                dp[i] += cur_m
            res = max(res, dp[i])
        return res


s = Solution()
print(s.bestTeamScore([9, 2, 8, 8, 2], [4, 1, 3, 3, 5]))
