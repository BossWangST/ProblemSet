from typing import List
import collections
import bisect
import functools
import math
import itertools


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        分析数学关系：
        当数字只有 1 位时，必须相等
        当数字有 2 位时， 10a+b+10d+c == 10b+a+10c+d
        a+d==b+c --> a-b == c-d
        当数字有 3 位时
        a-c == d-f
        最高位与最低位之差必须相等！
        当数字有 4 位时
        111(a-d) + 10(b-c) == 111(e-h) + 10(f-g)
        a-d == e-h and b-c == f-g
        从最外层往里走，只要能找到一层【壳】就必须相等！


        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        """

        """
        def get_shell(num: int) -> tuple:
            s = str(num)
            temp = []
            l, r = 0, len(s) - 1
            flag = False
            while l < r:
                cur = int(s[l]) - int(s[r])
                if cur != 0:
                    temp.append(cur)
                l += 1
                r -= 1
            if temp:
                flag = True
            temp.append(len(s))
            return tuple(temp) if flag else (0,)

        cnt = collections.Counter()
        res = 0
        for num in nums:
            cur_shell = get_shell(num)
            # 再次利用此技巧，先加上原来的统计个数，再增加个数，得到 2^n - 1 即 1+2+3...
            res += cnt[cur_shell]
            cnt[cur_shell] += 1
        """

        def get_rev(num: int) -> int:
            digit = []
            while num:
                digit.append(num % 10)
                num //= 10
            n = len(digit)
            s = 0
            for i in range(n):
                s += digit[i] * (10 ** (n - i - 1))
            return s

        res = 0
        cnt = collections.Counter()
        for num in nums:
            cur = get_rev(num)
            res += cnt[num - cur]
            cnt[num - cur] += 1
        return res % 1000000007


s = Solution()
print(s.countNicePairs([100, 10]))
