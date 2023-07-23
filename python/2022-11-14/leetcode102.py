# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []

        def dfs(node, level):
            if node is None:
                return
            if 0 <= level < len(res):
                res[level].append(node.val)
            else:
                res.append([node.val])
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            return

        dfs(root, 0)
        return res
