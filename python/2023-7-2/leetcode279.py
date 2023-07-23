from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def numSquares(self, n: int) -> int:
        # 完全背包问题
        nums = [1]
        for i in range(2, n):
            nums.append(i * i)
            if i * i > n:
                break
        # minimum number of nums, so we can init DP array with INF
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(2)]
        dp[0][0] = 0  # 只有能将 n 减到 0 的组合才是成功

        for i in range(len(nums)):
            for j in range(n + 1):
                if j < nums[i]:
                    dp[(i + 1) & 1][j] = dp[i & 1][j]
                else:
                    dp[(i + 1) & 1][j] = min(dp[i & 1][j], dp[(i + 1) & 1][j - nums[i]] + 1)
        return dp[len(nums) & 1][-1]


s = Solution()
print(s.numSquares(1))
