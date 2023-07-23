from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        n = len(array)
        s = [{0: 0, 1: 0} for _ in range(n + 1)]  # 0 -> num, 1 -> char
        for i in range(n):
            if not array[i].isdigit():
                s[i + 1][0] = s[i][0]
                s[i + 1][1] += s[i][1] + 1
            else:
                s[i + 1][0] += s[i][0] + 1
                s[i + 1][1] = s[i][1]
        l, res_n = 0, 0
        res_l, res_r = 0, 0
        # find maximum subarray that s[r][0] - s[l][0] == s[r][1] - s[l][1]
        # => s[r][0] - s[r][1] == s[l][0] - s[l][1]
        d = {0: 0}
        for r in range(1, n + 1):
            cur = s[r][0] - s[r][1]
            if d.get(cur, -1) >= 0:
                if r - d[cur] > res_n:
                    res_n = r - d[cur]
                    res_l, res_r = d[cur], r
            else:
                d[cur] = r
        return array[res_l:res_r]
