from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pair = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        """
        首先，我们需要看到由于要乘上 nums2 中的序列最小值，所以考虑枚举 nums2
        根据 nums2 排序之后，应当如何选择呢？
        nums2 由于是从大到小排序，则选定 i 之后就需要看 <=i 的下标
        这样才可以保证最小值是 nums2[i]
        """
        h = [i for i, _ in pair[:k]]
        heapify(h)
        # 此处使用小根堆，令堆中为 <=i 下标中【最大】的 k 个数字
        s = sum(h)
        # 最开始的结果就是前 k 个数之和乘上第 k 大的数
        res = s * pair[k - 1][1]
        for i, j in pair[k:]:
            # 使用 heapreplace 使得如果 i 比堆顶要小，直接替换堆顶，反之需要下沉，而免去了 pushpop 带来的下沉和上浮操作
            # 同时 heapreplace 返回值就是堆顶，每次都去掉最小的使得保持了 s 为最大的 k 个数的和
            s += i - heapreplace(h, i)
            res = max(res, s * j)
        return res


s = Solution()
print(s.maxScore([22, 5, 25, 15, 28, 1],
                 [22, 30, 25, 25, 9, 18],
                 3))
print(s.maxScore([44, 10, 25, 0, 25, 49, 0],
                 [18, 39, 15, 31, 43, 20, 45],
                 6))
