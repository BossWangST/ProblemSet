from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        no_pre = {x for x in range(numCourses)}
        pre = {-1: [-1]}
        for l in prerequisites:
            if l[0] in no_pre:
                no_pre.remove(l[0])
            if l[0] not in pre:
                pre.update({l[0]: [l[1]]})
            else:
                pre[l[0]].append(l[1])

        if not no_pre:
            return False
        while len(no_pre) < numCourses:
            begin_num = len(no_pre)
            ready_del = []
            for l in prerequisites:
                if l[0] in no_pre:
                    ready_del.append(l)
                    continue
                if l[1] in no_pre and l[1] in pre[l[0]]:
                    pre[l[0]].remove(l[1])
                    if not pre[l[0]]:
                        no_pre.add(l[0])
                        ready_del.append(l)
            for l in ready_del:
                prerequisites.remove(l)
                if l[0] in pre:
                    del pre[l[0]]
            end_num = len(no_pre)
            if begin_num == end_num:
                break

        return True if len(no_pre) == numCourses else False


s = Solution
print(s.canFinish(s, 7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]))
