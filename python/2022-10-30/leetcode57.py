from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        head = newInterval[0]
        tail = newInterval[1]
        res = []
        if not intervals:
            res.append(newInterval)
            return res
        next_interval = -1
        in_flag = False
        for i in range(len(intervals)):
            if head > intervals[i][1]:
                # head > cur_interval[1], then go on
                res.append(intervals[i])
                continue
            in_flag = True
            new_tail = -1
            new_head = min(intervals[i][0], head)
            for j in range(i, len(intervals)):
                if tail > intervals[j][1]:
                    continue
                if tail < intervals[j][0]:
                    new_tail = tail
                    next_interval = j
                else:
                    new_tail = intervals[j][1]
                    next_interval = j + 1
                res.append([new_head, new_tail])
                break
            if new_tail == -1:
                new_tail = tail
                res.append([new_head, new_tail])
            break
        if next_interval != -1:
            for i in range(next_interval, len(intervals)):
                res.append(intervals[i])
        if not in_flag:
            res.append(newInterval)

        return res


s = Solution
print(s.insert(s, [[1, 5]]
               , [6, 8]))
