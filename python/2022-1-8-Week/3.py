from collections import Counter


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        d1 = list(cnt1.keys())
        d2 = list(cnt2.keys())

        # 暴力尝试所有交换
        for c1 in d1:
            for c2 in d2:
                # 交换 c1 c2
                cnt1[c1] -= 1
                cnt1[c2] += 1
                cnt2[c1] += 1
                cnt2[c2] -= 1
                v1 = v2 = 0
                for c in cnt1.keys():
                    if cnt1[c]:
                        v1 += 1
                for c in cnt2.keys():
                    if cnt2[c]:
                        v2 += 1
                if v1 == v2:
                    return True
                # 还原交换
                cnt1[c1] += 1
                cnt1[c2] -= 1
                cnt2[c1] -= 1
                cnt2[c2] += 1
        return False


s = Solution()
s.isItPossible("aa", "bbcc")
