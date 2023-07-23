import time
from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        if n == 2:
            return 15
        # d = Counter()
        a, b, c, d, e = 1, 1, 1, 1, 1
        for i in range(n - 2):
            b += a
            c += b
            d += c
            e += d
        return a * 5 + b * 4 + c * 3 + d * 2 + e * 1


class Solution2:
    def countVowelStrings(self, n: int) -> int:
        return 1 + n + n * (n + 1) // 2 + n * (n + 1) * (n + 2) // 6 + n * (n + 1) * (n + 2) * (n + 3) // 24


s = Solution()
s2 = Solution2()
begin = time.perf_counter()
print(s.countVowelStrings(500000))
end = time.perf_counter()
print(end - begin)
