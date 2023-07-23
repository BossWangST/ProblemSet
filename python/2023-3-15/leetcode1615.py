from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads) <= 1:
            return len(roads)
        cnt = {}
        g = defaultdict(set)
        for u, v in roads:
            cnt[u] = cnt.get(u, 0) + 1
            cnt[v] = cnt.get(v, 0) + 1
            g[u].add(v)
            g[v].add(u)
        l = list(sorted(cnt.items(), key=lambda x: -x[1]))
        one, one_idx = l[0][1], {l[0][0]}
        i = 1
        while i < n:
            if l[i][1] == one:
                one_idx.add(l[i][0])
                i += 1
            else:
                break
        one_list = list(one_idx)
        if len(one_list) > 1:
            for i in range(len(one_list)):
                for j in range(i + 1, len(one_list)):
                    if one_list[j] not in g[one_list[i]]:
                        return one + one
            return one + one - 1
        two, two_idx = l[i][1], {l[i][0]}
        i += 1
        while i < n:
            if l[i][1] == two:
                two_idx.add(l[i][0])
                i += 1
            else:
                break
        two_list = list(two_idx)
        if len(two_list) < 2:
            if two_list[0] in g[one_list[0]]:
                return one + two - 1
            else:
                return one + two
        for i in range(len(two_list)):
            if two_list[i] not in g[one_list[0]]:
                return one + two
        return one + two - 1


s = Solution()
print(s.maximalNetworkRank(13,
                           [[2, 11], [10, 12], [3, 2], [7, 8], [2, 9], [9, 8], [6, 7], [4, 3], [4, 7], [9, 4], [0, 11],
                            [7, 3], [0, 2], [12, 2], [4, 12], [1, 6], [6, 8], [9, 5], [0, 7], [11, 6], [4, 1], [0, 9],
                            [9, 7], [2, 10], [7, 12], [3, 6], [11, 7], [12, 6], [11, 10], [7, 5], [4, 2], [0, 10],
                            [8, 1], [11, 3], [6, 2], [12, 11], [3, 1], [5, 3], [1, 11], [1, 10], [5, 6], [11, 4],
                            [4, 6], [0, 3], [5, 12], [0, 8], [1, 5], [8, 10], [5, 8], [10, 3], [3, 9], [7, 1], [1, 9],
                            [4, 5], [12, 1], [5, 11], [0, 6], [9, 11], [5, 2], [8, 4], [5, 10], [6, 9], [2, 7], [12, 8],
                            [11, 8], [10, 4], [9, 12], [0, 5], [3, 8], [10, 6], [3, 12], [1, 2], [10, 9], [8, 2],
                            [1, 0], [12, 0], [10, 7], [0, 4]]))
