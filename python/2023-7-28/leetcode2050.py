from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Topo
        d = defaultdict(list)
        deg = [0 for _ in range(n)]
        for u, v in relations:
            d[u - 1].append(v - 1)
            deg[v - 1] += 1
        cur = n
        q = deque()
        # 这里的 dp 怎么搞？思考每一门课，如果其没有先修课，那么修完的时间就是 time[i]
        # 否则，修完这门课的时间必然是 所有先修课中最长的 + 修完自己的
        # 最后的结果 res 则必然是 dp 中的最大值
        dp = [0 for _ in range(n)]
        for i in range(n):
            if deg[i] == 0:
                q.append(i)
                dp[i] = time[i]
        while cur > 0:
            cur_q = deque()
            for x in q:
                for v in d[x]:
                    dp[v] = max(dp[v], dp[x] + time[v])
                    deg[v] -= 1
                    if deg[v] == 0:
                        cur_q.append(v)
            cur -= len(q)
            q = cur_q
        return max(dp)


s = Solution()
print(s.minimumTime(9, [[2, 7], [2, 6], [3, 6], [4, 6], [7, 6], [2, 1], [3, 1], [4, 1], [6, 1], [7, 1], [3, 8], [5, 8],
                        [7, 8], [1, 9], [2, 9], [6, 9], [7, 9]], [9, 5, 9, 5, 8, 7, 7, 8, 4]))
