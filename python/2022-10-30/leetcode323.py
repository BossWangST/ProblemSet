from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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

        def dfs(node):
            if node in visited or node not in g:
                return
            visited.add(node)
            for adj in g.get(node):
                dfs(adj)

        counter = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                counter += 1
        return counter
