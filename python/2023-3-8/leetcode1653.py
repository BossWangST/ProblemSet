from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *


class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_l, b_l, a_r, b_r = 0, 0, 0, 0
        """
        for c in s:
            if c == 'a':
                a_r += 1
            else:
                b_r += 1
        """
        d = Counter(s)
        a_r, b_r = d['a'], d['b']
        res = a_r
        # 目标是，让 b_l 为 0 且 a_r 为 0
        for c in s:
            if c == 'a':
                a_l += 1
                a_r -= 1
            else:
                b_l += 1
                b_r -= 1
            res = min(res, b_l + a_r)
        return res


s = Solution()
print(s.minimumDeletions("ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa"))
