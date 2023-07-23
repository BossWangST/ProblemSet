class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        for i in range(len(s)):
            d[s[i]] -= 1
            if len(l) == 0:
                l.append(s[i])
            else:
                if s[i] in l:
                    continue
                if ord(s[i]) > ord(l[len(l) - 1]):
                    l.append(s[i])
                else:
                    while len(l) > 0 and ord(s[i]) <= ord(l[len(l) - 1]) and d[l[len(l) - 1]] > 0:
                        l.pop()
                    l.append(s[i])
        return ''.join(l)


s = Solution()
print(s.smallestSubsequence('cbacdcbc'))
