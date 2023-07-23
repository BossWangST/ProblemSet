def getRes(c, nums):
    current = []
    for i in range(len(c)):
        if c[i]:
            current.append(nums[i])
    return current


def solve(c, ith, nums, res):
    if ith == len(c):
        res.append(getRes(c, nums))
    else:
        c[ith] = False
        solve(c, ith + 1, nums, res)
        c[ith] = True
        solve(c, ith + 1, nums, res)


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        c = [False] * len(nums)
        solve(c, 0, nums, res)
        return res


s = Solution()
print(s.subsets([1, 2, 3]))
