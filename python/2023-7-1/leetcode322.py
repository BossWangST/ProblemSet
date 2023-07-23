from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        # idx: current choose index, cur: current NEEDED sum
        @cache
        def dfs(idx: int, cur: int) -> int:
            # base case
            if idx < 0:
                # we need MIN, so an invalid return will be INF
                return 0 if cur == 0 else float('inf')
            if coins[idx] > cur:
                return dfs(idx - 1, cur)
            # either take
            take = dfs(idx, cur - coins[idx]) + 1  # use 1 coin
            # or skip
            skip = dfs(idx - 1, cur)
            return min(take, skip)

        res = dfs(len(coins) - 1, amount)
        return res if res < float('inf') else -1
        '''
        # Translate to DP
        # dp = [[float('inf') for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp = [[float('inf') for _ in range(amount + 1)] for _ in range(2)]
        dp[0][0] = 0  # base case, for amount 0 and no coins, we have 0 solutions
        for i in range(len(coins)):
            for j in range(amount + 1):
                if coins[i] > j:
                    # skip
                    dp[(i + 1) & 1][j] = dp[i & 1][j]
                else:
                    dp[(i + 1) & 1][j] = min(dp[i & 1][j], dp[(i + 1) & 1][j - coins[i]] + 1)
        if dp[len(coins) & 1][-1] < float('inf'):
            return dp[len(coins) & 1][-1]
        else:
            return -1


s = Solution()
print(s.coinChange([1, 2, 5], 11))
