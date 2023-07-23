from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.l = []
        for x in nestedList:
            if type(x) == list:
                self.l.append(NestedIterator(x))
            else:
                self.l.append(x)
        self.p = 0
        self.s = len(self.l)

    def next(self) -> int:
        print(type(self.l[self.p]))
        print(type(self.l[self.p]) == NestedIterator)
        if type(self.l[self.p]) == NestedIterator:
            return self.l[self.p].next()
        res = self.l[self.p]
        self.p += 1

        return res

    def hasNext(self) -> bool:
        if self.p == self.s:
            return False
        if type(self.l[self.p]) == NestedIterator:
            if self.l[self.p].hasNext():
                return True
            while self.p < self.s and type(self.l[self.p]) != int and not self.l[self.p].hasNext():
                self.p += 1
            return True if self.p < self.s else False
        return True


# Your NestedIterator object will be instantiated and called as such:
nestedList = [[1, 1], 2, [1, 1]]
i, v = NestedIterator(nestedList), []
while i.hasNext():
    v.append(i.next())

print(v)
