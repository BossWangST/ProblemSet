from functools import *
from typing import *
from itertools import *
from math import *
from collections import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        s = [0 for _ in range(10 ** 5)]
        q = [root]
        p = 0
        level = [0]
        while len(q) > 0:
            cur = q.pop(0)
            cur_l = level.pop(0)
            s[cur_l] += cur.val
            if cur.left != None:
                q.append(cur.left)
                level.append(cur_l + 1)
            if cur.right != None:
                q.append(cur.right)
                level.append(cur_l + 1)
        s.sort()
        return s[k - 1]
