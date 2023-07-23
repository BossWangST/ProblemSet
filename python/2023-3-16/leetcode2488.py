from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res, cur = 0, []
        idx = -1
        for i in range(len(nums)):
            if nums[i] > k:
                cur.append(1)
            elif nums[i] < k:
                cur.append(-1)
            else:
                cur.append(0)
                idx = i
        s = list(accumulate(cur, initial=0))
        d = {0: 1}
        for r in range(1, len(s)):
            '''
            if s[r] in d:
                for l in d[s[r]]:
                    if l + 1 <= idx + 1 <= r:
                        res += 1
            '''
            if r >= idx + 1:
                res += d.get(s[r], 0) + d.get(s[r] - 1, 0)
            '''
            if s[r] - 1 in d:
                for l in d[s[r] - 1]:
                    if l + 1 <= idx + 1 <= r:
                        res += 1  # left middle
            '''
            if r <= idx:
                d[s[r]] = d.get(s[r], 0) + 1
        return res


s = Solution()
print(s.countSubarrays([5, 6, 7, 11, 13, 9, 8, 4, 10, 1, 12, 2, 3], 8))
