from math import ceil
from typing import List
from queue import PriorityQueue


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = PriorityQueue()
        for num in nums:
            pq.put(-num)
        res = 0
        for i in range(k):
            cur = pq.get()
            res += -cur
            pq.put(-ceil(-cur / 3))
        return res


s = Solution()
print(s.maxKelements([1, 10, 3, 3, 3], 3))
