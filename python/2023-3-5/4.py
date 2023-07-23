from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        cur = []
        for r in types:
            now = [r[1] for _ in range(r[0])]
            cur.extend(now)
        dp = [0 for _ in range(target + 1)]
        for i in range(len(cur)):
            for j in range(target, -1, -1):
                if j < cur[i]:
                    continue
                dp[j] = max(dp[j], dp[j - cur[i]] + 1)
        return dp[target]