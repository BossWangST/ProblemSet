from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def lastSubstring(self, s: str) -> str:
        m = max(s)
        i = 0
        res = ''
        while i < len(s):
            if s[i] == m:
                res = max(res, s[i:])
            i += 1
            while i < len(s) and s[i] == s[i - 1]:
                i += 1

        return res


s = Solution()
print(s.lastSubstring("aaaaaaaaaaaaaaaaaaaaa"))
