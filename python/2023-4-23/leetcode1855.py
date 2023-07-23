from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = nums1[::-1]
        nums2 = nums2[::-1]
        res = 0
        # print(len(nums1))
        # print(len(nums2))
        if nums1[0] > nums2[-1]:
            return 0
        if len(nums1) <= len(nums2):
            nums1 = [nums1[0]] * (len(nums2) - len(nums1)) + nums1
        else:
            nums1 = nums1[(len(nums1) - len(nums2)):]

        for i in range(min(len(nums1), len(nums2))):
            j = bisect_left(nums2, nums1[i])

            res = max(res, i - j)

        return res

s = Solution()
print(s.maxDistance([9819, 9508, 7398, 7347, 6337, 5756, 5493, 5446, 5123, 3215, 1597, 774, 368, 313],
                    [9933, 9813, 9770, 9697, 9514, 9490, 9441, 9439, 8939, 8754, 8665, 8560]))
