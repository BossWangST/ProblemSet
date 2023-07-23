from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for u, v in paths:
            d[u].append(v)
            d[v].append(u)
        '''
        res = {}

        @cache
        def dfs(node: int) -> bool:
            if len(visited) == n:
                return True
            if len(avai) == 0 or node in visited:
                return False
            visited.add(node)
            for i in list(avai):
                avai.remove(i)
                res[node] = i
                ok = False
                for v in d[node]:
                    if dfs(v):
                        ok = True
                if ok:
                    break
                avai.add(i)
            return True

        visited = set()
        avai = {1, 2, 3, 4}
        cur = 1
        while cur <= n:
            if cur not in visited:
                dfs(cur)
            cur += 1
        # print(res)
        res_l = []
        for i in range(1, n + 1):
            if i in visited:
                res_l.append(res[i])
        return res_l
        '''
        res = [0 for _ in range(n)]
        for i in range(1, n + 1):
            color = [False] * 5
            for v in d[i]:
                color[res[v - 1]] = True
            for j in range(1, 5):
                if not color[j]:
                    res[i - 1] = j
                    break
        return res


s = Solution()
print(s.gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]]))
