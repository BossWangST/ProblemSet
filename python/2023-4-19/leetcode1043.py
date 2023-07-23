from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0 for _ in range(n + 1)]
        dp[1] = arr[0]
        c_m = arr[0]
        for i in range(k):
            c_m = max(c_m, arr[i])
            dp[i + 1] = c_m * (i + 1)
        for i in range(k + 1, n + 1):
            cur = arr[i - 1]
            cur_s = cur + dp[i - 1]
            for j in range(1, k):
                if i - 1 - j < 0:
                    break
                cur = max(cur, arr[i - 1 - j])
                cur_s = max(cur_s, cur * (1 + j) + dp[i - 1 - j])
            dp[i] = cur_s
        return dp[-1]


s = Solution()
print(s.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
