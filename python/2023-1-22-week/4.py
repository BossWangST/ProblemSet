from typing import List
import collections
import bisect
import functools
import math
import itertools
import heapq


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        def get_trim(nums: List[int]) -> int:
            s = []
            for num in nums:
                if nums.count(num) > 1:
                    s.append(num)
            return len(s)

        n = len(nums)
        pre_sum = [0 for _ in range(n)]
        last = 0
        res = 0
        for i in range(n):
            if (i + 1) % k == 0:
                cur = nums[last:i + 1]
                last = i + 1
                res += get_trim(cur) + k

        if last < n:
            cur = nums[last:]
            res += get_trim(cur) + k
        return res


s = Solution()
print(s.minCost([2, 3, 3, 3, 1, 5, 5, 0, 5, 3, 4, 2, 1, 2, 5, 1, 2, 0],
                5))
