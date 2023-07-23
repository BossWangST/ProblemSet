from typing import List
import collections
import bisect
import math


class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        # Test divisor1 = 4, divisor2 = 6
        # arr1 = 1  2  3     5  6  7     9  10  11    13 ...
        # arr2 = 1  2  3  4  5     7  8  9  10  11    13 ...
        # arr1 【独占】有 divisor2 的倍数，但不能是 LCM(divisor1, divisor2) 的倍数
        # arr2 【独占】有 divisor1 的倍数，但不能是 LCM(divisor1, divisor2) 的倍数
        # 【共有】：既不是 divisor1 的倍数，又不是 divisor2 的倍数

        # 最小化最大值
        # 二分答案
        # 猜一个这个最大值，如果猜的越大，就意味着 arr1 和 arr2 会有更多的选择空间
        #                如果猜的越小，就意味着 arr1 和 arr2 只有更少的选择空间
        # 由于 arr1 只能选 uniqueCnt1 个数，arr2 只能选 uniqueCnt2 个数
        # 则先看【独占】的数字个数：arr1 = limit // divisor2 - limit // lcm(divisor1, divisor2)
        #                       arr2 = limit // divisor1 - limit // lcm(divisor1, divisor2)
        # 如果【独占】的数字个数不足以填满 Cnt 的要求，则剩下的空位就必须填入【共有】的数字
        # 而如果共有数字的个数仍然不足以填满 Cnt 的要求，则失败；否则成功。
        # 如此，check 函数就呼之欲出了
        def check(limit: int) -> bool:
            lcm = math.lcm(divisor1, divisor2)
            # 注意，有可能为负数，加一个 max
            unique1 = max(0, limit // divisor2 - limit // lcm)
            arr1_need = max(0, uniqueCnt1 - unique1)

            unique2 = max(0, limit // divisor1 - limit // lcm)
            arr2_need = max(0, uniqueCnt2 - unique2)

            common = limit - (limit // divisor1 + limit // divisor2 - limit // lcm)

            return common < arr1_need + arr2_need  # common 不足以填满 arr1 和 arr2 在获取【独占】后所需的数字，需要猜的再大一些

        # 二分的范围
        # 如果最小，1 不够，因为有得有两个数，所以 1 是左侧开区间
        # 如果最大，则 divisor1 = divisor2 = 2，所有的偶数都不能用，只能用奇数
        # 此时，相当于最多有 uniqueCnt1 + uniqueCnt2 个奇数，即最大为 (uniqueCnt1 + uniqueCnt2) * 2 - 1，右边可以到达，认为是闭区间
        # 注意，二分我们一般只看三种情况：[x, y]  (x, y]  (x, y)
        # 所以这里我们需要将右边的闭区间转化为开区间，那么右移一个下标即可
        # 故二分的范围为 (1, ~+1)
        left = 1 - 1  # 开区间，左指针左移一个下标
        right = (uniqueCnt1 + uniqueCnt2) * 2 - 1 + 1  # 开区间，右指针右移一个下标

        while left + 1 < right:  # 注意，左闭右开区间 (x, x) 是空集，需要跳出循环
            mid = (left + right) // 2
            if check(mid):
                left = mid  # 左边是开区间，mid 本身取不到，所以从 mid+1 开始的开区间左边界就是 mid
            else:
                right = mid  # 右边是开区间，mid 本身取不到，所以从 mid-1 开始的开区间右边界就是 mid
        return right  # 最后的区间必定是 (x-1, x)，所以为 x


s = Solution()
print(s.minimizeSet(2, 4, 8, 2))
