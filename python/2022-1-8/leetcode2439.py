from typing import List
import collections
import bisect


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # 二分
        # 猜一个最小的最大值
        def check(limit: int) -> int:
            # a = nums.copy()
            extra = 0
            # 从右边往左"推"，看用这个最大值推完到左边，能不能满足 <= limit 的要求
            for i in range(len(nums) - 1, 0, -1):
                x = nums[i] + extra
                if x > limit:
                    extra = x - limit # 更新 extra, 表示总的还需要往左推的数量
                else:
                    extra = 0
            return nums[0] + extra <= limit

        return bisect.bisect_left(range(max(nums)), True, key=check)
