from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *

'''
class Solution:
    def findScore(self, num: List[int]) -> int:
        d = defaultdict(set)
        nums = num.copy()
        n = len(nums)
        for i in range(n):
            # heappush(d[nums[i]], i)
            d[nums[i]].add(i)
            # d[nums[i]].insert(bisect_left(d[nums[i]], nums[i]), nums[i])
        nums.sort()
        s = set()
        p = 0
        res = 0
        while p < n:
            cur = nums[p]
            p += 1
            if len(d[cur]) == 0:
                while p < n and nums[p] == cur:
                    p += 1
                continue
            for i in d[cur]:
                cur_idx = i
                break
            res += cur
            s.add(cur_idx)
            # cur_idx = d[cur].pop(0)
            d[cur] -= s
            l, r = cur_idx - 1, cur_idx + 1
            if 0 <= l < n:
                s.add(l)
            if 0 <= r < n:
                s.add(r)
            if 0 <= r < n:
                d[num[r]] -= s
            if 0 <= l < n:
                d[num[l]] -= s
        return res
        '''


class Solution:
    def findScore(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        vis = [False for _ in range(n)]
        arr = sorted(enumerate(nums), key=lambda x: x[1])
        for k, val in arr:
            if not vis[k]:
                res += val
                vis[k] = True
                if 0 <= k - 1 < n:
                    vis[k - 1] = True
                if 0 <= k + 1 < n:
                    vis[k + 1] = True
        return res


s = Solution()
# print(s.findScore([10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]))
print(s.findScore([2, 3, 5, 1, 3, 2]))
