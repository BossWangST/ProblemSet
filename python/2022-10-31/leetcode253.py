from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        new_meeting = [intervals[0][1]]
        res = 1
        i = 1
        while i < len(intervals):
            has_room = False
            for j in range(len(new_meeting)):
                if intervals[i][0] >= new_meeting[j]:
                    has_room = True
                    new_meeting[j] = intervals[i][1]
                    break
            if not has_room:
                new_meeting.append(intervals[i][1])
                res += 1
            i += 1

        return res


s = Solution
print(s.minMeetingRooms(s, [[1, 5], [8, 9], [8, 9]]))
