from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        d = Counter()
        for i in range(1, len(rounds)):
            s, e = rounds[i - 1], rounds[i]
            j = s - 1
            while j != e - 1:
                d[j + 1] += 1
                j = (j + 1) % n
            if i == len(rounds) - 1:
                d[e] += 1
        print(d)
        l = sorted(list(d.items()), key=lambda x: (-x[1], x[0]))
        m = l[0][1]
        res = [l[0][0]]
        for i in range(1, len(l)):
            if m == l[i][1]:
                res.append(l[i][0])
            else:
                break
        return res


s = Solution()
print(s.mostVisited(2, [2, 1, 2, 1, 2, 1, 2, 1, 2]))
