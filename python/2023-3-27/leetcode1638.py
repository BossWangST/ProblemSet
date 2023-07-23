from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        d_s = defaultdict(list)
        d_t = defaultdict(list)
        n_s, n_t = len(s), len(t)
        for x, y in combinations(range(n_s + 1), 2):
            d_s[y - x].append(s[x:y])
        for x, y in combinations(range(n_t + 1), 2):
            d_t[y - x].append(t[x:y])

        '''
        for i in range(n_s):
            d_s[i + 1] = list(combinations(s, i + 1))
        for i in range(n_t):
            d_t[i + 1] = list(combinations(t, i + 1))
        '''
        res = 0

        def check(s: Tuple[str], t: Tuple[str]) -> bool:
            diff = 0
            for i in range(len(s)):
                if s[i] == t[i]:
                    continue
                else:
                    diff += 1
                    if diff > 1:
                        return False
            return True if diff == 1 else False

        for i in range(min(n_s, n_t)):
            for cur_s in d_s[i + 1]:
                for cur_t in d_t[i + 1]:
                    if check(cur_s, cur_t):
                        res += 1
        return res


s = Solution()
print(s.countSubstrings('aba', 'baba'))
