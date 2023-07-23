from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        i = 0
        j = 1
        while i < j and j < len(intervals):
            head1, tail1, head2, tail2 = intervals[i][0], intervals[i][1], intervals[j][0], intervals[j][1]
            if not tail1 <= head2:
                if tail1 <= tail2:
                    # intervals.remove(intervals[i + 1])
                    j += 1
                else:
                    # intervals.remove(intervals[i])
                    i = j
                    j = i + 1
                res += 1
            else:
                i = j
                j = i + 1
        return res


s = Solution
print(s.eraseOverlapIntervals(s,
                              [[1, 2], [2, 3], [3, 4], [1, 3]]))
