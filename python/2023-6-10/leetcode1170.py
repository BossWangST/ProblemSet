from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            d = Counter(s)
            return d[min(s)]

        f_words = [f(w) for w in words]
        f_words.sort()
        res = []
        for q in queries:
            cur = f(q)
            idx = bisect_right(f_words, cur)
            res.append(len(words) - idx)
        return res


s = Solution()
print(s.numSmallerByFrequency(
    ["bba", "abaaaaaa", "aaaaaa", "bbabbabaab", "aba", "aa", "baab", "bbbbbb", "aab", "bbabbaabb"],
    ["aaabbb", "aab", "babbab", "babbbb", "b", "bbbbbbbbab", "a", "bbbbbbbbbb", "baaabbaab", "aa"]))
