from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]
        d = defaultdict(list)
        degree = [0 for _ in range(n)]
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)
            degree[u] += 1
            degree[v] += 1
        # 叶子结点必然不可能，其距离肯定是最长的
        # 谁可能成为叶子结点？度为 1 的节点！
        # 每次去除所有度为 1 的节点
        # 请注意大前提，这个 MHT 最多只有 2 个，用极限情况思考，一条链子的树，必须取中间节点为根才行，那么奇数个就是中间 1 个，偶数个就是中间 2 个
        deg1 = deque()
        for i in range(n):
            if degree[i] == 1:
                deg1.append(i)
        while n > 2:
            n -= len(deg1)
            for i in range(len(deg1)):
                cur = deg1.popleft()
                # decrease all adj node degree from i
                for v in d[cur]:
                    degree[v] -= 1
                    if degree[v] == 1:
                        deg1.append(v)
        return list(deg1)

s = Solution()
print(s.findMinHeightTrees(6, [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]))
