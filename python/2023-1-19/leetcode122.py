from typing import List
import collections
import bisect
import functools
import math
import itertools
import heapq


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        """
        dp[i][j]: 第 i 天在是否持有股票（j=0 无，j=1 有）时的最大收益
        base case:
        dp[0][0] = 0
        dp[0][1] = prices[0]
        """
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        return dp[len(prices) - 1][0]


s = Solution()
print(s.maxProfit([7,6,4,3,1]))
