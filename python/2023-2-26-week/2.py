import bisect
from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cur = [0 for _ in range(n)]
        d = {}
        for i in range(n):
            idx = bisect_left(nums, nums[i] * 2)
            d[nums[i]] = n - idx
            # cur[idx - 1] += 1
        use = d[nums[0]]
        for val, t in d.items():
            if t > 0:
                use -= 1
        if use >= 0:
            return n
        else:
            return d[nums[0]]
        """
        cur_list = list(accumulate(cur))
        if cur_list[-1] * 2 > n:
            p = n - 1
            first = cur_list[p]
            p -= 1
            while cur_list[p] == first:
                p -= 1
            second = cur_list[p]
            p -= 1
            while cur_list[p] == second:
                p -= 1

            return cur_list[p] * 2
        else:
            return cur_list[-1] * 2
        """
        """
        i, j = 0, 1
        while i < j < n:
            while cur[i]:
                i += 1
                if i == j:
                    j += 1
                    if j == n:
                        break
            while cur[j]:
                j += 1
            if j == n:
                break
            if nums[i] * 2 <= nums[j]:
                res += 2
                cur[i], cur[j] = True, True
                i += 1
                j += 1
            else:
                j += 1
        return res
        """


s = Solution()
# print(s.maxNumOfMarkedIndices(
#     [42, 83, 48, 10, 24, 55, 9, 100, 10, 17, 17, 99, 51, 32, 16, 98, 99, 31, 28, 68, 71, 14, 64, 29, 15, 40]))
# print(s.maxNumOfMarkedIndices([2, 3, 4, 5]))
print(s.maxNumOfMarkedIndices(
    [1, 78, 27, 48, 14, 86, 79, 68, 77, 20, 57, 21, 18, 67, 5, 51, 70, 85, 47, 56, 22, 79, 41, 8, 39, 81, 59, 74, 14,
     45, 49, 15, 10, 28, 16, 77, 22, 65, 8, 36, 79, 94, 44, 80, 72, 8, 96, 78, 39, 92, 69, 55, 9, 44, 26, 76, 40, 77,
     16, 69, 40, 64, 12, 48, 66, 7, 59, 10]))
print(s.maxNumOfMarkedIndices(
    [90, 37, 51, 92, 50, 50, 93, 49, 34, 53, 3, 32, 3, 95, 80, 79, 76, 39, 35, 35, 83, 100, 84, 24, 6, 50, 97, 82, 67,
     31, 99, 94, 19]))
