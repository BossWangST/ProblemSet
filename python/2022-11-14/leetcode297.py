# Definition for a binary tree node.
import re


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''

        res = []

        def dfs(node):
            if node is None:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(res)

    i = 0

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        res = data.split(',')

        self.i = 0

        def dfs():
            if res[self.i] == 'N':
                self.i += 1
                return None
            cur_node = TreeNode(int(res[self.i]))
            self.i += 1
            cur_node.left = dfs()
            cur_node.right = dfs()
            return cur_node

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
