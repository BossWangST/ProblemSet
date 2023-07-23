from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        p = root
        q = [p]
        cur_child = 1
        level = []
        cur_level = []
        while len(q) > 0:
            cur = q.pop(0)
            cur_level.append(cur.val)
            cur_child -= 1
            if cur_child == 0:
                level.append(cur_level)
                cur_level = []
            if cur.left:
                q.append(cur.left)
                cur_child += 1
            if cur.right:
                q.append(cur.right)
                cur_child += 1
        for i in range(1, len(level)):
            for j in level[i]:
                for k in range(j):
                    for m in level[k]:
                        res = max(res, abs(j - m))

        return res
