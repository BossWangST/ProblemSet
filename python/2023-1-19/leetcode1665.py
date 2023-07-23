from typing import List
import collections
import bisect
import functools
import math
import itertools
import heapq


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        """
        先对【两者之差】从大到小排序，在对后者从小到大排序
        因为需要尽可能利用【两者之差】盈余的体力去往下做事
        """
        tasks.sort(key=lambda x: (x[0] - x[1], x[1]))
        cur = tasks[0][1] - tasks[0][0]
        need = 0
        for i in range(1, len(tasks)):
            if tasks[i][1] > cur:
                need += tasks[i][1] - cur
                cur = tasks[i][1] - tasks[i][0]
            else:
                cur -= tasks[i][0]

        return need + tasks[0][1]


s = Solution()
print(s.minimumEffort([[1, 2], [1, 7], [2, 3], [5, 9], [2, 2]]))
