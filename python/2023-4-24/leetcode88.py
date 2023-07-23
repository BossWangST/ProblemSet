from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        p1, p2 = 0, 0
        while p1 < m and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        while p1 < m:
            res.append(nums1[p1])
            p1 += 1
        if p2 > 0:
            res += nums2[p2:]
        print(res)
        for i in range(len(nums1)):
            nums1[i] = res[i]
        print(nums1)


s = Solution()
s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
