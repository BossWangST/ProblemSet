from typing import List
import collections
import bisect
import functools
import math
import itertools


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        考虑一共有多少"属性"需要考虑
        天数
        当前有没有股票
        当前买卖了几次
        所以 dp[i][j][k] 表示第 i 天（从 0 开始）在有（j = 1）无（j = 0）股票的情况下，买卖了 k 次后的最大利润
        0 <= i <= len(prices) - 1
        j = True or False
        k <= k
        """
        k = min(k, len(prices) // 2)  # 买卖是涉及两天，如果 k 比天数的一半都大，那至多也就是【天数的一半】的买卖次数
        dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(len(prices))]
        for i in range(k + 1):
            dp[0][0][i] = 0
            dp[0][1][i] = -prices[0]
        for i in range(1, len(prices)):
            """
            若第 i 天【没有】股票：dp[i][0][k]
            则只有两种情况：
            * 仍然保持没有股票的钱 dp[i - 1][0][k]
            * 之前有股票，现在没了，说明卖了，则 dp[i - 1][1][k] + prices[i]
            若第 i 天【有】股票: dp[i][1][k]
            则只有两种情况：
            * 仍然保持有股票的钱 dp[i - 1][1][k]
            * 之前没有股票，现在有了，说明买了，则 dp[i - 1][0][k - 1] - prices[i]
            !! 注意，一旦买了，就认为是交易次数 + 1，所以此时利用的数值应当是没有买之前的数字，也就是 dp[i-1][0][k-1]
            """
            for j in range(1, k + 1):
                dp[i][0][j] = max(dp[i - 1][0][j], dp[i - 1][1][j] + prices[i])
                dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][0][j - 1] - prices[i])
        return dp[len(prices) - 1][0][k]


s = Solution()
print(s.maxProfit(2,
                  [3, 3, 5, 0, 0, 3, 1, 4]))
