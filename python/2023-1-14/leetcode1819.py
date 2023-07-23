from typing import List
import collections
import bisect
import functools
import math
import itertools


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        """
        与其枚举每个不同的 GCD ，不如从 GCD 出发思考
        考虑什么是 GCD ？一个序列的 GCD 就意味着这个序列中【每一个数字】都是 GCD 的倍数
        那么，如果我们从 GCD 出发，找到一个数字，令这个数字的倍数能覆盖一个序列，不就是找到一个 GCD 了吗？
        例如：[6, 10, 3]
        从 1 开始【试】GCD
        1, 2, 3
        3 在 nums 里，此时 GCD 只能为 3
        4, 5, 6
        6 在 nums 里，此时 GCD 还可以是 3
        7, 8, 9, 10
        10 在 nums 里，此时 GCD 只能是 1 了，降到了最低，所以 1 就是一个 GCD
        同理
        从 2 开始【试】GCD
        2, 4, 6
        6 在 nums 里，此时 GCD 只能是 6
        8, 10
        10 在 nums 里，此时 GCD 降为 2，降到了最低，所以 2 就是一个 GCD
        """
        has = set()
        res = 0
        for num in nums:
            if num not in has:
                has.add(num)
                # ! 优化，如果子序列里只有一个数，那么它本身就是 GCD
                res += 1
        limit = max(nums)
        for i in range(1, limit // 3 + 1):
            # 最多枚举到 nums 的最大值
            # ! 优化上界
            # 由于此时无需考虑单个数子序列的 GCD，且无需考虑 num 本身的 GCD
            # 则，如果还有 GCD，就必定是至少 2 个数的子序列，又因为没有 num 本身
            # 所以那样的 GCD 想要覆盖子序列的话，必定子序列里至少要有 2*GCD 和 3*GCD
            # 所以只需要枚举到 limit // 3
            if i in has:
                continue
            g = 0  # 任何数字和 0 的 GCD 都是数字本身
            # 本身此时无需枚举，从 2 倍开始枚举
            for j in range(i + i, limit + 1, i):
                if j in has:
                    g = math.gcd(j, g)
                    if g == i:
                        # 降到了最低
                        res += 1
                        break
        return res


s = Solution()
s.countDifferentSubsequenceGCDs([1, 2, 3, 4])
