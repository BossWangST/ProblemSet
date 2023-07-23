from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *
from math import *


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # 这个题考验转换题意
        '''
        第 n 个数字假设是 x <=> 小于等于 x 的数字有 n 个
        x 越大，n 必然越大 => 单调性 => 二分
        二分谁？显然 n 是固定的，所以将 n 当作目标，去二分 x
        题目转化成，寻找最小的一个 x，使得小于等于 x 的数字有 n 个
        怎么计算小于等于 x 的数字个数？
        x // a => 能被 a 整除的小于等于 x 的个数
        x // b => 能被 b 整除的小于等于 x 的个数
        x // LCM(a, b) => 既能被 a 整除，又能被 b 整除的，小于等于 x 的个数
        LCM <=> Least Common Multiple 最小公倍数
        通过容斥原理，小于等于 x 的数字个数就是 cnt = x // a + x // b - x // LCM(a, b)
        所以，二分的判断条件：
        if cnt < n: x increment
        if cnt > n: x decrement
        else: OK!
        '''
        least = lcm(a, b)

        def check(x: int) -> bool:
            cnt = x // a + x // b - x // least
            if cnt < n:
                return True
            elif cnt >= n:
                return False

        l, r = 0, min(a, b) * n
        while l + 1 < r:
            m = (l + r) // 2
            if check(m):
                l = m
            else:
                r = m
        return r % (10 ** 9 + 7)


s = Solution()
print(s.nthMagicalNumber(4, 2, 3))
