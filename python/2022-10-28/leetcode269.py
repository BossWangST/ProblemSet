from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        letters = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''
            for j in range(minLen):
                if w1[j] != w2[j]:
                    letters[w2[j]].add(w1[j])
                    break

        res = ''
        while len(letters) > 0:
            flag = False
            for i in list(letters.keys()):
                if not letters[i]:
                    letters.pop(i)
                    res += i
                    for j in letters:
                        if i in letters[j]:
                            letters[j].remove(i)
                            flag = True
            if not flag and len(letters) > 0:
                return ''
        return res


s = Solution
print(s.alienOrder(s, ["z", "x", "a", "zb", "zx"]))
