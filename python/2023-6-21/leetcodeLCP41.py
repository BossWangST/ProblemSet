from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        direc = [[-1, -1], [-1, 0], [-1, 1],
                 [0, -1], [0, 1],
                 [1, -1], [1, 0], [1, 1]]
        m, n = len(chessboard), len(chessboard[0])

        def check(x: int, y: int) -> int:
            c = chessboard.copy()
            res = 0
            q = [(x, y)]
            while len(q) > 0:
                cur_x, cur_y = q.pop(0)
                cur = []
                for sx, sy in direc:
                    # try all directions
                    nx, ny = cur_x + sx, cur_y + sy
                    cur_l = []
                    while 0 <= nx < m and 0 <= ny < n and c[nx][ny] == 'O':
                        # go along with 'O'
                        cur_l.append((nx, ny))
                        nx += sx
                        ny += sy
                    if 0 <= nx < m and 0 <= ny < n and c[nx][ny] == 'X':
                        cur.extend(cur_l)
                        res += len(cur_l)
                        for i, j in cur_l:
                            l = list(c[i])
                            l[j] = 'X'
                            c[i] = ''.join(l)
                q.extend(cur)
            return res

        res = 0
        for i in range(m):
            for j in range(n):
                if chessboard[i][j] == '.':
                    res = max(res, check(i, j))
        return res


s = Solution()
print(s.flipChess([".......", ".......", ".......", "X......", ".O.....", "..O....", "....OOX"]))
