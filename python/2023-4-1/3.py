from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
import statistics


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if n == k:
            return 0
        if k == 1:
            arr.sort()
            m = arr[len(arr) // 2]
            res = 0
            for i in range(n):
                res += abs(arr[i] - m)
            return res
        res = 0
        s = set()
        for i in range(k):
            if len(s) == n:
                break
            cur = []
            for j in range(i, n + k, k):
                cur.append(arr[j % n])
                s.add(j % n)
            cur.sort()
            m = cur[len(cur) // 2]
            for j in range(i, n + k, k):
                res += abs(arr[j % n] - m)
                # arr[j % n] = m
        return res
        '''
        else:
            arr.sort()
            m = arr[len(arr) // 2]
            res = 0
            for num in arr:
                res += abs(num - m)
            return res
        '''


s = Solution()
print(s.makeSubKSumEqual([10, 9, 1, 10, 5],
                         3))
