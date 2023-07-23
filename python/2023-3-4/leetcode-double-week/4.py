from functools import *
from typing import *
from itertools import *
from math import *
from collections import *


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        tree = defaultdict(set)
        n = 0
        for e in edges:
            tree[e[0]].add(e[1])
            tree[e[1]].add(e[0])
            n = max(n, e[0], e[1])
        g = defaultdict(set)
        for gue in guesses:
            g[gue[0]].add(gue[1])
        n += 1
        res = 0
        has = set()
        for gue in guesses:
            i = gue[0]
            if i in has:
                continue
            has.add(i)
            visited = [False for _ in range(n)]
            cur_k = 0
            q = [i]
            flag = False
            while len(q) > 0:
                cur = q.pop(0)
                visited[cur] = True
                for nxt in tree[cur]:
                    if visited[nxt]:
                        continue
                    q.append(nxt)
                    if cur in g:
                        if nxt in g[cur]:
                            cur_k += 1
                            if cur_k >= k:
                                res += 1
                                flag = True
                                break
                if flag:
                    break
        return res


s = Solution()
print(s.rootCount([[0, 1], [1, 2], [1, 3], [4, 2]], [[1, 3], [0, 1], [1, 0], [2, 4]], 3))