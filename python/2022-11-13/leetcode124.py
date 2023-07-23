# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            one_side = max(node.val + left, node.val + right)
            two_side = node.val + left + right
            no_side = node.val
            self.res = max(self.res, one_side, two_side, no_side)

            return max(one_side, no_side)

        dfs(root)
        return self.res
