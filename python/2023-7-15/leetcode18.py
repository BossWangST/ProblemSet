from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        s = set()
        for i in range(n):
            for j in range(i + 1, n):
                t = target - nums[i] - nums[j]
                l, r = j + 1, n - 1
                while l < r:
                    if nums[l] + nums[r] > t:
                        r -= 1
                    elif nums[l] + nums[r] < t:
                        l += 1
                    else:
                        if (nums[i], nums[j], nums[l], nums[r]) not in s:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                            s.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
        return res


s = Solution()
print(s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
