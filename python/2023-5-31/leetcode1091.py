from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        d = [[-1, -1], [-1, 0], [-1, 1],
             [0, -1], [0, 1],
             [1, -1], [1, 0], [1, 1]]

        n, m = len(grid), len(grid[0])

        '''
        @cache
        def dfs(x: int, y: int, l: int) -> int:
            if x == n - 1 and y == m - 1:
                return l + 1
            path = float('inf')
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if grid[nx][ny] == 1:
                    continue
                grid[nx][ny] = 1
                cur = dfs(nx, ny, l + 1)
                grid[nx][ny] = 0
                if cur != -1:
                    path = min(path, cur)
            return path if path != float('inf') else -1
        '''
        s = [[0, 0, 0]]
        vis = [[False for _ in range(m)] for _ in range(n)]
        vis[0][0] = True
        res = float('inf')
        while len(s) > 0:
            x, y, l = s.pop(0)
            if x == n - 1 and y == m - 1:
                res = min(res, l + 1)
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if grid[nx][ny] == 1 or vis[nx][ny]:
                    continue
                vis[nx][ny] = True
                s.append([nx, ny, l + 1])
        return res if res != float('inf') else -1


s = Solution()
print(s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
