class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not s:
            return ''
        window, countT = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # ! Here is len(countT) to represent how many kinds of chars
        have, need = 0, len(countT)
        l = 0
        res, resLen = [-1, -1], float('infinity')

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                c = s[l]
                window[c] -= 1
                if c in countT and window[c] < countT[c]:
                    have -= 1
                # pop from left
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float('infinity') else ''


s = Solution
print(s.minWindow(s, "aBbaBBBBA", "BBA"))
