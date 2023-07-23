from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        def dfs(l: int, r: int, c: List[List[int]]) -> int:
            if l == r:
                return 1
            if len(c) == 0:
                return -1
            dis = []
            for i in range(len(c)):
                if c[i][1] < l or c[i][0] > r:
                    dis.append((0, i))
                elif c[i][0] <= l and c[i][1] >= r:
                    dis.append((r - l + 1, i))
                elif c[i][0] >= l and c[i][1] <= r:
                    dis.append((c[i][1] - c[i][0] + 1, i))
                elif c[i][0] <= r <= c[i][1]:
                    dis.append((r - c[i][0] + 1, i))
                else:
                    dis.append((c[i][1] - l + 1, i))
            dis.sort(key=lambda x: -x[0])
            left, right = c[dis[0][1]][0], c[dis[0][1]][1]
            l_c, r_c = [], []
            for i in range(len(c)):
                if c[i][0] < left <= c[i][1] or c[i][1] < left:
                    l_c.append(c[i])
                if c[i][0] <= right < c[i][1] or c[i][0] > right:
                    r_c.append(c[i])
            l_res = dfs(l, left, l_c) if left > l else 0
            r_res = dfs(right, r, r_c) if right < r else 0
            if l_res >= 0 and r_res >= 0:
                return l_res + r_res + 1
            else:
                return -1

        return dfs(0, time, clips)


s = Solution()
print(s.videoStitching(
    [[0, 2], [1, 6], [3, 10]], 10))
