class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        res = ""
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    res = s[l:r + 1]
                    max_len = r - l + 1
                l -= 1
                r += 1

        ori_max_len = max_len
        max_len = 0
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    if r - l + 1 > ori_max_len:
                        res = s[l:r + 1]
                        ori_max_len = r - l + 1
                    max_len = r - l + 1
                l -= 1
                r += 1
        return res


s = Solution

print(s.longestPalindrome(s, "bacabab"))
