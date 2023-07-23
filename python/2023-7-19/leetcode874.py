from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        dir = 0  # N-0, E-1, S-2, W-3
        dy = {0: 1, 1: 0, 2: -1, 3: 0}
        dx = {0: 0, 1: 1, 2: 0, 3: -1}
        obs_x = defaultdict(set)
        obs_y = defaultdict(set)
        res = 0
        for ox, oy in obstacles:
            obs_x[ox].add(oy)
            obs_y[oy].add(ox)
        for c in commands:
            if c >= 0:
                nx, ny = x + c * dx[dir], y + c * dy[dir]
                if dir == 0 or dir == 2:  # Y axis
                    if nx in obs_x:
                        r = range(y + 1, ny + 1) if y < ny else range(y - 1, ny - 1, -1)
                        ok = True
                        for cy in r:
                            if cy in obs_x[nx]:
                                ok = False
                                if dir == 0:
                                    x, y = nx, cy - 1
                                else:
                                    x, y = nx, cy + 1
                                break
                        if ok:
                            x, y = nx, ny
                    else:
                        x, y = nx, ny
                else:  # X axis
                    if ny in obs_y:
                        r = range(x + 1, nx + 1) if x < nx else range(x - 1, nx - 1, -1)
                        ok = True
                        for cx in r:
                            if cx in obs_y[ny]:
                                ok = False
                                if dir == 1:
                                    x, y = cx - 1, ny
                                else:
                                    x, y = cx + 1, ny
                                break
                        if ok:
                            x, y = nx, ny
                    else:
                        x, y = nx, ny
            elif c == -1:
                dir = (dir + 1) % 4
            elif c == -2:
                dir = (dir - 1) % 4
            res = max(res, x * x + y * y)
        return res


s = Solution()
print(s.robotSim([2, 2, 5, -1, -1],
                 [[-3, 5], [-2, 5], [3, 2], [5, 0], [-2, 0], [-1, 5], [5, -3], [0, 0], [-4, 4], [-3, 4]]))
