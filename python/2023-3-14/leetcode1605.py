from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if rowSum[i] < colSum[j]:
                    res[i][j] = rowSum[i]
                    colSum[j] -= rowSum[i]
                    rowSum[i] = 0
                else:
                    res[i][j] = colSum[j]
                    rowSum[i] -= colSum[j]
                    colSum[j] = 0
        return res


s = Solution()
print(s.restoreMatrix([3, 8], [4, 7]))
