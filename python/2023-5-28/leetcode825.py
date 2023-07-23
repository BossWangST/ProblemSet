from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        d = Counter(ages)
        s = list(set(ages))
        s.sort()
        ages.sort()
        c = []
        for a in ages:
            c.append(a * 0.5 + 7)
        res = 0
        idx = 0
        for i in range(len(s)):
            cur = bisect_left(c, s[i])
            if cur < idx + 1 or (cur == idx + 1 and c[cur - 1] == s[i]):
                idx += d[s[i]]
                continue
            res += (cur - idx - 1) * d[s[i]]
            if c[cur - 1] == s[i]:
                res -= d[s[i]]
            idx += d[s[i]]
        return res


s = Solution()
print(s.numFriendRequests([25, 29, 84, 20, 75, 36, 64, 115, 4, 66, 36, 13, 70, 81, 43]))
