from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row = []
        for i in range(len(mat)):
            cur = []
            cur_c = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    cur_c += 1
                else:
                    cur_c = 0
                cur.append(cur_c)
            row.append(cur)
        res, col = 0, 0
        for i in range(len(row)):
            for j in range(len(row[0])):
                col = row[i][j]
                res += col
                for k in range(1, i + 1):
                    col = min(col, row[i - k][j])
                    res += col
                    if col == 0:
                        break
        return res


s = Solution()
print(s.numSubmat([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
