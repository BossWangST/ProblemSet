from typing import List
import collections
import bisect
import functools
import math
import itertools
import re


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        s1 = sentence1.split()
        s2 = sentence2.split()
        if len(s1) > len(s2):
            sentence1, sentence2 = sentence2, sentence1
            s1, s2 = s2, s1
        # let sentence1 is shorter
        n1, n2 = len(s1), len(s2)
        # 首先讨论是否为前缀或者后缀
        p1, p2 = 0, 0
        # Prefix
        while p1 < n1 and p2 < n2 and s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1
        if p1 == n1:
            return True
        p1, p2 = 0, n2 - n1
        while p1 < n1 and p2 < n2 and s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1
        if p2 == n2:
            return True
        p1, p2 = 0, 0
        """
        分类讨论：
        1. 开头不等，则需要在开头就添加，则后续如果再有不等就寄
        2. 开头相等，则只允许不等一次，出现第二次不等就寄
        """
        if s1[p1] != s2[p2]:
            # 开头不等
            while p2 < n2 and s1[p1] != s2[p2]:
                p2 += 1  # 找到第一个相等的
            # 从此往后必须全部相等
            if p2 == n2:
                return False
            while p1 < n1 and p2 < n2 and s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1
            if p1 == n1 and p2 == n2:
                return True
            else:
                return False
        else:
            # 开头相等
            while p1 < n1 and p2 < n2 and s1[p1] == s2[p2]:
                # 找到第一个不等的
                p1 += 1
                p2 += 1
            if p1 == n1:
                return True
            while p2 < n2 and s1[p1] != s2[p2]:
                p2 += 1  # 尝试寻找第二个相等的
            while p1 < n1 and p2 < n2 and s1[p1] == s2[p2]:
                # ! 注意，此处需要尽可能让 p2 向后走，找到最后一个和 p1 匹配的
                if p1 == n1 - 1:
                    while p2 < n2 and s1[p1] == s2[p2]:
                        p2 += 1
                else:
                    p2 += 1
                p1 += 1
            if p1 == n1 and p2 == n2:
                return True
            else:
                return False


s = Solution()
print(s.areSentencesSimilar("I pIG dm ox wOX D F F ef oAWhPQYrhV b YO",
                            "I kw S bkvUjgmCoF nT VqMkf ZI oNA Q EfTziR h cKJ pIG dm ox wOX D F F ef oAWhPQYrhV b YO"))
