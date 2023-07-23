from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        dir = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
        cur, cur_x, cur_y = 0, 0, 0
        step = 1
        n = len(grid)
        a = n * n
        while step < a:
            flag = False
            for x, y in dir:
                next_x, next_y = cur_x + x, cur_y + y
                if 0 <= next_x < n and 0 <= next_y < n:
                    if grid[next_x][next_y] == cur + 1:
                        cur += 1
                        cur_x, cur_y = next_x, next_y
                        flag = True
                        step += 1
                        break
            if not flag:
                return False
        return True


s = Solution()
print(s.checkValidGrid(
    [[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]]))
