from typing import List
import collections
import bisect
import functools
import math
import itertools
import heapq


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        cnt = {'a': 0, 'b': 0, 'c': 0}
        left, right = 0, 0
        n = len(s)
        while right < n:
            cnt[s[right]] += 1
            while left < right and cnt['a'] > 0 and cnt['b'] > 0 and cnt['c'] > 0:
                cnt[s[left]] -= 1
                left += 1
            res += left
            right += 1
        return res


s = Solution()
print(s.numberOfSubstrings('aabbc'))
