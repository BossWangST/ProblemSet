from typing import List
import collections
import bisect
import functools
import math
import itertools


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        res = ""
        # n 位密码，这样想，每次输入 1 位我都要完成其中一种情况，则相当于一共是 n-1 种情况（就差一位完成）
        # 所以将 n-1 种情况看作状态节点，发出去的边就是所有 0～k-1 的数字连接到其他的边
        # DFS

        # nodes = functools.reduce(lambda x, y: [z0 + z1 for z0 in x for z1 in y], [alphabet] * n)
        alphabet = []
        for i in range(k):
            alphabet.append(str(i))

        # think of every one more bit is an answer, we know there exists k**n answers
        # so if accumulate (k**n)*1 bit, then we only need to add the initial (n-1) bits to the beginning
        # Thus, the final length must be k ** n * 1 + n - 1
        final_len = k ** n + n - 1
        s = set()

        def dfs(cur: str) -> str:
            if len(cur) == final_len:
                return cur
            for c in alphabet:
                if n < 2:
                    next = c
                else:
                    next = cur[-(n - 1):] + c

                if next not in s:
                    cur += c
                    s.add(next)
                    test = dfs(cur)
                    if len(test) == final_len:
                        return test
                    s.remove(next)
                    cur = cur[:-1]
            return cur

        res = '0' * n
        s.add(res)
        res = dfs(res)

        return res


s = Solution()
print(s.crackSafe(2, 2))
