from typing import List
import itertools
import collections
import bisect


def func(k: int, nums: List[int]) -> int:
    init = [0]
    init.extend(nums)
    pre_sum = list(itertools.accumulate(init))
    omit = nums[k]
    for i in range(len(pre_sum)):
        if i > k + 1:
            pre_sum[i] -= omit
    left_min = min(pre_sum[:k + 1])
    right_max = max(pre_sum[k + 2:])
    return right_max + left_min


print(func(1, [9, -11, 31, -23, 21, 27, -12, -11, 29, -5, 3]))
