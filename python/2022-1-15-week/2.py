from typing import List
import collections
import bisect
import functools
import math
import itertools


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mx = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for q in queries:
            row1i, col1i, row2i, col2i = q[0], q[1], q[2], q[3]
            mx[row1i][col1i] += 1
            mx[row1i][col2i + 1] -= 1
            mx[row2i + 1][col1i] -= 1
            mx[row2i + 1][col2i + 1] += 1

        for i in range(n + 1):
            for j in range(n + 1):
                if i == 0:
                    up = 0
                else:
                    up = mx[i - 1][j]
                if j == 0:
                    left = 0
                else:
                    left = mx[i][j - 1]
                if i == 0 or j == 0:
                    diagonal = 0
                else:
                    diagonal = mx[i - 1][j - 1]

                mx[i][j] += up + left - diagonal
        res = []
        for i in range(len(mx) - 1):
            res.append(mx[i][:n])
        return res


s = Solution()
s.rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]])
