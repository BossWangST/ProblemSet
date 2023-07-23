from collections import *
from functools import *
from typing import *
from itertools import *


class Solution:
    def balancedString(self, s: str) -> int:
        cur = Counter(s)
        diff_cur = {}
        n = len(s)
        flag = True
        for c, i in cur.items():
            if i > n // 4:
                flag = False
                diff_cur[c] = diff_cur.get(c, 0) + i - n // 4
        if flag:
            return 0
        l = 0
        res = float('inf')
        cur = {}
        for r in range(n):
            c = s[r]
            cur[c] = cur.get(c, 0) + 1

            if cur.get('Q', 0) >= diff_cur.get('Q', 0) and \
                    cur.get('W', 0) >= diff_cur.get('W', 0) and \
                    cur.get('E', 0) >= diff_cur.get('E', 0) and \
                    cur.get('R', 0) >= diff_cur.get('R', 0):
                while l < r and (s[l] not in diff_cur or cur[s[l]] > diff_cur[s[l]]):
                    if s[l] not in diff_cur:
                        l += 1
                    elif cur[s[l]] > diff_cur[s[l]]:
                        cur[s[l]] -= 1
                        l += 1
                res = min(res, r - l + 1)
        return res


s = Solution()
print(s.balancedString('WWQQRRRRQRQQ'))
