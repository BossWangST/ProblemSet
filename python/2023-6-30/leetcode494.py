from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Positive sum = p
        # Negative sum = sum(nums) - p
        # Expression sum = p - (sum(nums) - p)
        # We need target == 2p - sum(nums)
        # So p = (target + sum(nums)) / 2
        # Find a way to get p, choose some of ele in nums to get sum to p
        target += sum(nums)
        if target & 1 or target < 0:
            return 0
        target //= 2

        '''
        # current index of nums: idx, current sum: cur
        def dfs(idx: int, cur: int) -> int:
            if idx < 0:
                # 正好装满背包则成功
                return 1 if cur == 0 else 0
            if nums[idx] > cur:
                return dfs(idx - 1, cur)
            # either choose nums[idx], or not
            # try both ways
            return dfs(idx - 1, cur) + dfs(idx - 1, cur - nums[idx])

        return dfs(len(nums) - 1, target)
        '''
        # Translate to DP
        # dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        dp = [[0 for _ in range(target + 1)] for _ in range(2)]
        # base case: if idx < 0 and cur == 0
        dp[0][0] = 1
        for i in range(len(nums)):
            for j in range(target + 1):
                if j < nums[i]:
                    dp[(i + 1) & 1][j] = dp[i & 1][j]
                else:
                    dp[(i + 1) & 1][j] = dp[i & 1][j] + dp[i & 1][j - nums[i]]
        return dp[len(nums) & 1][-1]


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
