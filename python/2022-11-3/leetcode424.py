class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1
        num = [0] * 26
        base = 65
        num[ord(s[l]) - base] = 1
        extend = False
        while r < len(s):
            num[ord(s[r]) - base] += 1
            cur_max = max(num)
            cur_len = r - l + 1
            if cur_len - cur_max <= k:
                r += 1
                extend = True
            else:
                num[ord(s[l]) - base] -= 1
                if extend:
                    num[ord(s[r]) - base] -= 1
                    extend = False
                else:
                    r += 1
                l += 1
        return cur_len


s = Solution
print(s.characterReplacement(s, "AABABBA", 1))
