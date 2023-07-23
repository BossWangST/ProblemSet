from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set()
        for i in nums:
            s.add(i)

        res = 1
        for i in nums:
            if i - 1 in s:
                continue
            cur = i
            cur_res = 1
            while cur + 1 in s:
                cur += 1
                cur_res += 1
            res = max(res, cur_res)
        return res


s = Solution
print(s.longestConsecutive(s, [-4, -1, 4, -5, 1, -6, 9, -6, 0, 2, 2, 7, 0, 9, -3, 8, 9, -2, -6, 5, 0, 3, 4, -2]))
