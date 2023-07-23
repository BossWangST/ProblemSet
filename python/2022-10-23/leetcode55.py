from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        d = {}

        def dfs(i):
            if i == len(nums):
                return True
            if i > len(nums):
                d[i] = False
                return False
            for w in range(nums[i]):
                if d.get(i + w) is not None:
                    res = d.get(i - w)
                else:
                    res = dfs(i + w)
                if res:
                    break
            return res

        return dfs(0)


s = Solution
print(s.canJump(s, [3, 2, 1, 0, 4]))
