from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)
        res = [0 for _ in range(n)]
        size = [0 for _ in range(n)]
        s = set()
        def dfs(node: int, dep: int) -> int:
            cur_s = 1  # self
            res[0] += dep  # cal res[0] to prepare for DP
            s.add(node)
            for v in d[node]:
                if v not in s:
                    cur_s += dfs(v, dep + 1)
            size[node] = cur_s
            return cur_s

        dfs(0, 0)  # init res[0] and size[]

        '''
        假设 0 为根，那么 1 次 dfs 即可搞定，但我们现在要把【每一个节点都是根】的情况进行计算
        以 2 为例，案例 1:
        2 到自己为根的子树的节点距离【更近了】，具体地说距离【全部少了 1】
        2 到不在自己子树的节点距离【更远了】，具体地说距离【全部多了 1】
        所以 res[2] = res[0] + 2(不在自己子树的节点总数) - 4(在自己子树的节点总数)
        '''

        def alter_root(node: int, prev: int) -> None:
            for v in d[node]:
                if v != prev:
                    res[v] = res[node] + (n - size[v]) - size[v]
                    alter_root(v, node)
            return

        alter_root(0, 0)
        return res


s = Solution()
print(s.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
