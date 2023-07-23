from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        last, cur = matrix[0].copy(), [0 for _ in range(n)]
        for i in range(1, n):
            for j in range(n):
                left = last[j - 1] if j >= 1 else float('inf')
                right = last[j + 1] if j <= n - 2 else float('inf')
                top = last[j]
                cur[j] = min(left, min(right, top)) + matrix[i][j]
            last = cur.copy()
        return min(cur)


s = Solution()
print(s.minFallingPathSum([[100, -42, -46, -41], [31, 97, 10, -10], [-58, -51, 82, 89], [51, 81, 69, -51]]))
