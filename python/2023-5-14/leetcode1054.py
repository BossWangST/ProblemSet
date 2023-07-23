from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if len(barcodes) <= 1:
            return barcodes
        d = Counter(barcodes)
        l = sorted(list(map(list, d.items())), key=lambda x: -x[1])
        res = []

        while len(l) > 1:
            res.append(l[0][0])
            res.append(l[-1][0])
            l[0][1] -= 1
            l[-1][1] -= 1
            if l[0][1] == 0 and l[-1][1] == 0:
                l.pop(0)
                l.pop(-1)
            elif l[0][1] == 0:
                l.pop(0)
            elif l[-1][1] == 0:
                l.pop(-1)
        # print(l)
        idx = []
        if len(l) > 0:
            rest = l[0][0]
            if res[-1] != rest:
                l[0][1] -= 1
                res.append(rest)
                if l[0][1] == 0:
                    l.pop()
            if res[0] != rest:
                l[0][1] -= 1
                res = [rest] + res
                if l[0][1] == 0:
                    l.pop()
            while len(l) > 0:
                for i in range(len(res) - 1):
                    if res[i] != l[0][0] and res[i + 1] != l[0][0]:
                        idx.append(i)
                        l[0][1] -= 1
                        if l[0][1] == 0:
                            l.pop()
                            break
            offset = 1
            for i in idx:
                res.insert(i + offset, rest)
                offset += 1
        return res
        '''
        while len(res) < len(barcodes):
            for i in range(len(l)):
                if l[i][1] == 0:
                    continue
                res.append(l[i][0])
                l[i][1] -= 1
        return res
        '''


s = Solution()
print(s.rearrangeBarcodes([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
