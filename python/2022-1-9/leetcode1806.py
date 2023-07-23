from typing import List
import collections
import bisect
import functools


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        nums = [i for i in range(n)]
        res = 0
        arr = nums.copy()
        ori = nums.copy()

        while True:
            for i in range(n):
                if i & 1:
                    arr[i] = nums[n // 2 + (i - 1) // 2]
                else:
                    arr[i] = nums[i // 2]
            res += 1
            if functools.reduce(lambda x, y: x and y, map(lambda x, y: x == y, arr, ori)):
                return res
            nums = arr.copy()

        return -1


s = Solution()
print(s.reinitializePermutation(4))
