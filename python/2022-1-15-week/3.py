from typing import List
import collections
import bisect
import functools
import math
import itertools


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        d = collections.Counter()

        res = 0
        cur_cnt = 0
        n = len(nums)
        while right < n:
            cur_cnt += d[nums[right]]  # 利用 Counter 【先】加上当前数字的个数，再给计数器 +1 达到统计【组合数】的目的
            """
            组合数本质就是 1 + 2 + 3 ... （对于同一个数字的组合）
            例如：[3, 1, 4, 3, 2, 2, 4]
            right 走到第二个 3 的时候，cur_cnt 先加上原本的 3 的个数，即 1 个，再计数器 += 1，使得 cur_cnt 就是【数字对】的数量
            如果又来了一个 3，则正好加上刚才的 3 的数量 1 + 2 = 3
            完成了【组合数】的计算
            """
            d[nums[right]] += 1
            """
            下面考虑如何移动左指针
            当我们能够满足 k 对的要求时，我们就可以移动左指针
            当前的对数为 cur_cnt，那么如果删去左侧的数，就等同于删去这个数的【一个数量】
            而此时，【一个数量】等价于【少了一个选择的余地】
            例如：[3, 2, 3, 3, 3]
            如果右指针走到了第四个 3，此时左指针在第一个 3，那么倘若删去了左指针指向的 3，则
            3 的组合数就会由原本的 1 + 2 + 3 (C(4,2))，变成了 1 + 2 (C(3,2))
            而由于我们的计数器是【延迟计数】的，所以计数器里的数 - 1，才是当前组合数计算的加法算式中的最后一个数
            比如，刚才已经 4 个 3 了，组合数是 1 + 2 + 3，如果少了一个数，算式中最后的 3 就应当删去，而 3 正好
            是 【4 个】的 4 减去 1
            """
            while left < n and cur_cnt - (d[nums[left]] - 1) >= k:
                cur_cnt -= d[nums[left]] - 1
                d[nums[left]] -= 1
                left += 1
            """
            由于我们的左指针一直保持了【能满足 k 对成立的极限情况】，即只要能移动左指针的就都移动了
            例如：[3, 1, 4, 3, 2, 2, 4]
            当右指针走到 4 的时候，很明显此时有 3 对，那么左指针就可以移到第一个 4 的位置
            此时，难道前面的 3 和 1 就不用了吗？当然不是，3 和 1 必然可以成功，右边子数组都能成功
            左边延长了也会成功，所以应当加上左指针左侧的长度，作为结果需要相加的数
            """
            if cur_cnt >= k:
                res += left - 0 + 1
            right += 1

        return res


s = Solution()
print(s.countGood([3, 1, 4, 3, 2, 2, 4], 2))
