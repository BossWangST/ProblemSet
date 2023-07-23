from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        d = {'c': 0, 'r': 0, 'o': 0, 'a': 0}
        res = 0
        for c in croakOfFrogs:
            if c == 'c':
                d[c] += 1
            elif c == 'r':
                if d['c'] == 0:
                    return -1
                d['c'] -= 1
                d[c] += 1
            elif c == 'o':
                if d['r'] == 0:
                    return -1
                d['r'] -= 1
                d[c] += 1
            elif c == 'a':
                if d['o'] == 0:
                    return -1
                d['o'] -= 1
                d[c] += 1
            elif c == 'k':
                if d['a'] == 0:
                    return -1
                d['a'] -= 1
            res = max(res, sum(d.values()))

        return res if sum(d.values()) == 0 else -1


s = Solution()
print(s.minNumberOfFrogs('crcoakroak'))
