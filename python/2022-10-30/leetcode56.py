from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 3 overlapping: [1,3][2,6]=>[1,6]
        # [1,3][1,6]=>[1,6]
        # [1,6][1,3]=>[1,6]

        intervals = sorted(intervals, key=lambda x: (x[0]))
        # intervals.sort()
        i = 0
        while i < len(intervals) - 1:
            new_head = -1
            new_tail = -1
            if intervals[i][0] <= intervals[i + 1][0] <= intervals[i][1] <= intervals[i + 1][1]:
                new_head = intervals[i][0]
                new_tail = intervals[i + 1][1]
            elif intervals[i + 1][0] <= intervals[i][0] <= intervals[i][1] <= intervals[i + 1][1]:
                new_head = intervals[i + 1][0]
                new_tail = intervals[i + 1][1]
            elif intervals[i][0] <= intervals[i + 1][0] <= intervals[i + 1][1] <= intervals[i][1]:
                new_head = intervals[i][0]
                new_tail = intervals[i][1]
            else:
                i += 1
                continue
            intervals.remove(intervals[i])
            intervals.remove(intervals[i])
            intervals.insert(i, [new_head, new_tail])

        return intervals


s = Solution
print(s.merge(s, [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]))
