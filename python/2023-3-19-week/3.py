from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        '''
        n = len(nums)
        seq = [0 for _ in range(n)]
        i = 0
        while i < n:
            cur = 1
            cur_i = i
            while i < n - 1 and nums[i + 1] == nums[i] + k:
                cur += 1
                i += 1
            for j in range(cur_i, i + 1):
                seq[j] = cur
                cur -= 1
            i += 1
        d = Counter(nums)
        res = 0
        cur_n = n
        for i in range(n):
            res += (1 << (cur_n - 1 - d[nums[i] + k]))
            if i < n - 1:
                if nums[i + 1] == nums[i] + k:
                    nxt = i + 2
                    if nxt == n:
                        continue
                else:
                    nxt = i + 1
            else:
                nxt = n
            less = 0
            j = nxt
            while j < n:
                if seq[j] == 1:
                    j += 1
                    continue
                left = j - nxt
                right = n - (j + seq[j])
                if left > 0:
                    less += (1 << left)
                if right > 0:
                    less += (1 << right)
                if left == 0 and right == 0:
                    less += 1
                j += seq[j]
            res -= less

            cur_n -= 1
            '''
        nums.sort()
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = 1
        d = Counter(nums)
        for i in range(1, n):
            flag = False
            cnt = d[nums[i] - k]
            if cnt == 0:
                dp[i] = dp[i - 1] * 2 + 1
            else:
                dp[i] = dp[i - 1] * 2 + 1 - 2 * cnt
        # print(dp)
        return dp[-1]

        return res


s = Solution()

print(s.beautifulSubsets([2, 4, 6]
                         , 2))
print(s.beautifulSubsets([1], 1))
print(s.beautifulSubsets([4, 2, 5, 9, 10, 3]
                         , 1))
