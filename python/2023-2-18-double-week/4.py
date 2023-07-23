from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        init_sum = sum(nums2)
        cur_1 = sum(nums1)
        acc = list(accumulate(nums1))
        # n = len(nums2)
        # num1 = bin(int(''.join(map(str, nums1)), 2))
        for i in range(len(queries)):
            if queries[i][0] == 1:
                l, r = queries[i][1], queries[i][2]
                cur = acc[r] - acc[l - 1]
                cur_1 -= cur
                a = r - l + 1
                cur = a - cur
                cur_1 += cur
                # ones = [1 if l <= k <= r else 0 for k in range(n)]
                for j in range(l, r + 1):
                    nums1[j] = not nums1[j]
                acc = list(accumulate(nums1))
                # ones = bin(int(''.join(map(str, ones)), 2) << 1)
            elif queries[i][0] == 2:
                p = queries[i][1]
                init_sum += p * cur_1
            else:
                res.append(init_sum)
        return res


s = Solution()
res = s.handleQuery([0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                    [30, 46, 43, 34, 39, 16, 14, 41, 22, 11, 32, 2, 44, 12, 22, 36, 44, 49, 50, 10, 33, 7, 42],
                    [[1, 15, 21], [3, 0, 0], [3, 0, 0], [2, 21, 0], [2, 13, 0], [3, 0, 0]])
for i in res:
    print(i)
