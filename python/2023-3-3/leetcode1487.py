from functools import *
from typing import *
from itertools import *

import re


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = {}
        res = []
        res_s = set()
        for s in names:
            if s in d:
                cur = s + '(' + str(d[s]) + ')'
                while cur in res_s:
                    d[s] += 1
                    cur = s + '(' + str(d[s]) + ')'
                res.append(cur)
                res_s.add(cur)
                d[s] += 1
            else:
                cur = s
                d[s] = 0
                while cur in res_s:
                    d[s] += 1
                    cur = s + '(' + str(d[s]) + ')'
                d[s] += 1
                res.append(cur)
                res_s.add(cur)
        return res


s = Solution()
print(s.getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)", "kaido(2)"]))
