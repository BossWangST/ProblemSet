from typing import List
import collections
import bisect


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # 最大化最小值 -> 二分答案
        # 我要最小值甜蜜度中最大的一个数，我不知道，先猜一个数
        # 猜的数越大，选取 k 个数的范围就越小（就是，甚至都选不出 k 个数满足要求）
        # 猜的数越小，选取 k 个数的范围就越大（即，我甚至可以随便选 k 个数都能满足要求）
        # 怎么判定选不选得出来？即，check 函数的最终目标就是判断，当前猜的这个甜蜜值，我能不能选出 k 个数去满足要求
        # 排序后，从左往右扫描，最小的加上【猜的值】后的数设为 x，就看能不能从第一个比 x 大的数开始（即最小的差值）
        # 往后走，能有 k 个数字
        #
        # 二分范围：
        # 最小是 0，比如所有价格都一样 [7,7,7,7]
        # 最大是 数组中最大的差值的【平均值】，比如：最大差值为 20，要选 3 个数字，即 2 个差值（排序过了），所以最小值不会超过整个最大差值的平均值
        # 所以范围为 [0, ~]
        # 举例：price = [13,5,1,8,21,2], k = 3
        # 排序：[1, 2, 5, 8, 13, 21]
        #

        def check(x: int) -> bool:
            cnt = 0
            x0 = price[0] + x
            for num in price:
                if num >= x0:
                    cnt += 1
                    x0 = num + x
                    if cnt >= k - 1:
                        return True
            return False
            # 如果 cnt >= k 说明够选出，则可以猜的大一点；反之，可以猜的小一点

        price.sort()
        left, right = -1, (price[-1] - price[0]) // (k - 1) + 1

        while left + 1 < right:  # 开区间
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left


s = Solution()
print(s.maximumTastiness([1, 3, 1], 2))
