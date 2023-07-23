from typing import List
import collections
import bisect
import functools
import math
import itertools
import heapq


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sum1, sum2 = 0, 0
        diff = []
        diff_sum = 0
        for i in range(len(nums1)):
            sum1 += nums1[i]
            sum2 += nums2[i]
            diff.append(nums1[i] - nums2[i])
            if k != 0:
                if diff[i] % k != 0:
                    return -1
            if diff[i] > 0:
                diff_sum += diff[i]
        if sum1 != sum2:
            return -1
        if k != 0:
            return diff_sum // k
        else:
            return -1 if diff_sum != 0 else 0


s = Solution()
print(s.minOperations([10, 5, 15, 20],
                      [20, 10, 15, 5],
                      0))
