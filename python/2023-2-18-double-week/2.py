from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        ma = ''
        flag = False
        for c in s:
            if c != '9':
                first = c
                flag = True
                break
        if not flag:
            first = s[0]
        for i in range(len(s)):
            if s[i] == first:
                ma += '9'
            else:
                ma += s[i]

        mi = ''
        flag = False
        for c in s:
            if c != '0':
                first = c
                flag = True
                break
        if not flag:
            first = s[0]
        for i in range(len(s)):
            if s[i] == first:
                mi += '0'
            else:
                mi += s[i]

        return int(ma) - int(mi)


s = Solution()
# print(s.minMaxDifference(99999))
print(s.minMaxDifference(456))
