from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n = len(nums1)
        p1, p2 = 0, 0
        res = []
        while p1 < n and p2 < n:
            if nums1[p1][0] == nums2[p2][0]:
                res.append([nums1[p1][0], nums1[p1][1] + nums2[p2][1]])
                p1 += 1
                p2 += 1
            elif nums1[p1][0] < nums2[p2][0]:
                res.append([nums1[p1][0], nums1[p1][1]])
                p1 += 1
            else:
                res.append([nums2[p2][0], nums2[p2][1]])
                p2 += 1
        while p1 < n:
            res.append([nums1[p1][0], nums1[p1][1]])
            p1 += 1
        while p2 < n:
            res.append([nums2[p2][0], nums2[p2][1]])
            p2 += 1
        return res


s = Solution()
print(s.mergeArrays([[2, 4], [3, 6], [5, 5]], nums2=[[1, 3], [4, 3]]))
