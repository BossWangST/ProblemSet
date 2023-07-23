from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for s in strs:
            s = "".join(sorted(s))

        res = []
        i = 0
        j = 1
        flag = 0
        while i < len(strs) and j < len(strs):
            res.append([strs[i]])
            while j < len(strs) and strs[i] == strs[j]:
                res[flag].append(strs[j])
                j += 1
            i = j
            j += 1
            flag += 1
        return res


s = Solution
print(s.groupAnagrams(s, ["eat", "tea", "tan", "ate", "nat", "bat"]))
