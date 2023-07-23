from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        g = dict()
        for e in edges:
            if e[0] not in g:
                g.update({e[0]: [e[1]]})
            else:
                g.get(e[0]).append(e[1])
            if e[1] not in g:
                g.update({e[1]: [e[0]]})
            else:
                g.get(e[1]).append(e[0])

        '''
        over = -1
        suc = 1
        no_child = 0
        '''

        def dfs(node: int, father: int):
            if node in visited:
                return False
            visited.add(node)
            if node not in g:
                return True
            for dest in g.get(node):
                if dest == father:
                    continue
                if not dfs(dest, node):
                    return False
            return True

        if dfs(0, -1):
            if len(visited) == n:
                return True
        return False


s = Solution
print(s.validTree(s, 5,
                  [[1, 0], [2, 0]]
                  ))
