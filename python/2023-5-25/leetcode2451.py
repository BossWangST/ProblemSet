from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def oddString(self, words: List[str]) -> str:
        cur_w = []
        for i in range(len(words)):
            cur_w.append(list(map(lambda x: ord(x), list(words[i]))))
        # print(cur_w)
        one = [cur_w[0][i + 1] - cur_w[0][i] for i in range(len(cur_w[0]) - 1)]
        fin, two = [], []
        two_idx = -1
        for k in range(1, len(cur_w)):
            cur = [cur_w[k][i + 1] - cur_w[k][i] for i in range(len(cur_w[k]) - 1)]
            if not fin and not two:
                if cur == one:
                    fin = cur
                else:
                    two = cur
                    two_idx = k
                continue
            if fin:
                if cur != fin:
                    return words[i]
            if two:
                if cur != two:
                    return words[two_idx]
                else:
                    return words[0]


s = Solution()
print(s.oddString(["aaa", "bob", "ccc", "ddd"]))
