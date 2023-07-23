from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        if n == 2:
            return 15
        dp = [0 for _ in range(n)]
        dp[0] = 5
        dp[1] = 15
        for i in range(2, n):
            dp[i] = dp[i - 1] * 5 - (1 + dp[i - 1]) * dp[i - 1] // 2 + 1
        return dp[-1]


s = Solution()
print(s.countVowelStrings(33))
