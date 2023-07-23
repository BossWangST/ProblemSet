from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = deque()
        op = {'+', '-', '*', '/'}
        for t in tokens:
            if t not in op:
                s.append(int(t))
            else:
                num1 = s.pop()
                num2 = s.pop()
                if t == '+':
                    s.append(num1 + num2)
                elif t == '-':
                    s.append(num2 - num1)
                elif t == '*':
                    s.append(num1 * num2)
                else:
                    '''
                    cur = abs(num2) // abs(num1)
                    if num1 > 0 and num2 > 0:
                        s.append(cur)
                    else:
                        s.append(-cur)
                    '''
                    s.append(int(num2 / num1))
        res = s.pop()
        return res


s = Solution()
print(s.evalRPN(
    ["-78", "-33", "196", "+", "-19", "-", "115", "+", "-", "-99", "/", "-18", "8", "*", "-86", "-", "-", "16", "/",
     "26", "-14", "-", "-", "47", "-", "101", "-", "163", "*", "143", "-", "0", "-", "171", "+", "120", "*", "-60", "+",
     "156", "/", "173", "/", "-24", "11", "+", "21", "/", "*", "44", "*", "180", "70", "-40", "-", "*", "86", "132",
     "-84", "+", "*", "-", "38", "/", "/", "21", "28", "/", "+", "83", "/", "-31", "156", "-", "+", "28", "/", "95",
     "-", "120", "+", "8", "*", "90", "-", "-94", "*", "-73", "/", "-62", "/", "93", "*", "196", "-", "-59", "+", "187",
     "-", "143", "/", "-79", "-89", "+", "-"]))
