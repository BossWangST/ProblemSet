from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d_list = []
        res = []
        for s in strs:
            d = dict()
            for c in s:
                d[c] = 1 + d.get(c, 0)
            fail = True
            for i in range(len(d_list)):
                if d_list[i] == d:
                    res[i].append(s)
                    fail = False
                    break
            if fail:
                d_list.append(d)
                res.append([s])
        return res
