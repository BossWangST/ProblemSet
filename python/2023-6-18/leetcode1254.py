from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        di = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(x: int, y: int) -> int:
            grid[x][y] = -1
            ok = True
            for sx, sy in di:
                nx, ny = x + sx, y + sy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                    if dfs(nx, ny) == 0:
                        ok = False
                    if ok and nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                        ok = False
            return 1 if ok else False

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    res += dfs(i, j)
        return res


s = Solution()
print(s.closedIsland([[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                      [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
                      [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
                      [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
                      [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                      [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                      [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                      [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                      [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]))
