from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = nums[::-1]
        n = len(cur)
        cur[:k] = cur[-(n - k + 1):-(n + 1):-1]
        cur[k:] = cur[:-(n - k + 1):-1]
        for i in range(len(nums)):
            nums[i] = cur[i]
        # a = [1, 2, 3, 4]
        # a[:2] = a[:-(k + 1):-1]
        # print(a)


nums = [1, 2, 3, 4, 5, 6, 7]
s = Solution()
s.rotate(nums, 3)
print(nums)
