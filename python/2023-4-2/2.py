from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        res = []
        while True:
            cur = []
            for v in d.keys():
                if d[v] > 0:
                    cur.append(v)
                d[v] -= 1
            if not cur:
                break
            res.append(cur)
        return res


s = Solution()
print(s.findMatrix([1, 3, 4, 1, 2, 3, 1]))
