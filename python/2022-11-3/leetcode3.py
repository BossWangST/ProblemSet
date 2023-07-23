class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        visited = set()
        res = 1
        cur = s[0]
        visited.add(cur)
        for i in range(1, len(s)):
            if s[i] in visited:
                for j in range(cur.index(s[i])):
                    visited.remove(cur[j])
                cur = cur[cur.index(s[i]) + 1:] + s[i]
            else:
                visited.add(s[i])
                cur += s[i]
                res = max(res, len(visited))

        return res


s = Solution
print(s.lengthOfLongestSubstring(s, "abcabcbb"))
