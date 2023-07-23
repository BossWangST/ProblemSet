from functools import *
from typing import *
from itertools import *
from math import *
from collections import *


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key=lambda x: x[0])
        group = 1
        n = len(ranges)
        flag = False
        tail = ranges[0][1]
        for i in range(1, n):
            if not flag and ranges[i][0] <= tail:
                if ranges[i][1] > tail:
                    tail = ranges[i][1]
                flag = True
            elif flag and ranges[i][0] <= tail:
                if ranges[i][1] > tail:
                    tail = ranges[i][1]
                continue
            else:
                flag = False
                tail = ranges[i][1]
                group += 1
        res = (1 << group) % (10 ** 9 + 7)
        return res


s = Solution()
# print(s.countWays([[1, 3], [10, 20], [2, 5], [4, 8]]))
# print(s.countWays([[0, 0], [8, 9], [12, 13], [1, 3]]))  # 16
# print(s.countWays([[34, 56], [28, 29], [12, 16], [11, 48], [28, 54], [22, 55], [28, 41], [41, 44]]))  # 2
# print(s.countWays(
#     [[6, 303], [218, 247], [145, 294], [165, 199], [51, 233], [357, 359], [45, 80], [99, 233], [100, 366], [271, 306],
#      [104, 200], [74, 148], [29, 291], [28, 103], [115, 145], [162, 279], [53, 98], [43, 87], [95, 286], [32, 340]]))
print(s.countWays([[5, 11], [20, 22], [1, 3], [21, 22], [11, 11]]))
