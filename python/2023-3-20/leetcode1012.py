from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)

        @cache
        def dfs(idx: int, mask: int, upper: bool):
            # 填当前 idx 下标的数字，mask 表示前面已经填了的数字的集合
            # upper 表示是否受到 n 的限制，如果前面每一位都填了对应于 n 的每一位数字
            # 则当前位只能填 0 ~ s[i]，否则是 0 ~ 9
            if idx == len(s):
                return 1 if mask > 0 else 0  # 如果 mask 是 0，则表示没有任何数字填入
            # 每一个 idx 在前面都没有选择数字的时候（mask == 0）都可以选择当前位置也不填
            cur = 0
            if mask == 0:
                cur += dfs(idx + 1, mask, False)
            max_num = int(s[idx]) if upper else 9
            # 枚举每一种数字的情况，如果 mask 为 0，则表示前面没有填入数字，则不能填前导 0，得从 1 开始
            # 否则可以从 0 开始填
            start = 1 if mask == 0 else 0
            for d in range(start, max_num + 1):
                if mask >> d & 1 == 0:  # 没有选过 d 这个数
                    cur += dfs(idx + 1, mask | (1 << d), upper and d == int(s[idx]))
            return cur

        return n - dfs(0, 0, True)  # 起始 upper 为 True 保证第一个数字不能超过 n 的第一位


s = Solution()
print(s.numDupDigitsAtMostN(20))
