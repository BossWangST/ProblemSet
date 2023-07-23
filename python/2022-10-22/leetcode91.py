class Solution:
    def numDecodings(self, s: str) -> int:
        table = [0] * (len(s) + 1)
        if int(s[0]) > 0:
            table[0] = 1
        else:
            return 0
        for i in range(1, len(s) + 1):
            if s[i - 2] != '0' and i >= 2 and 26 >= int(s[i - 2:i]) >= 1:
                table[i] += table[i - 2]
            if s[i - 1] != '0':
                table[i] += table[i - 1]
        return table[len(s)]


s = Solution
print(s.numDecodings(s, '2101'))
