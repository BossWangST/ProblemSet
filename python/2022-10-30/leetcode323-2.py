from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node):
            father = node

            while father != par[father]:
                par[father] = par[par[father]]
                father = par[father]
            return father

        def union(node1, node2):
            father1, father2 = find(node1), find(node2)

            if father1 == father2:
                return 0
            if rank[father1] < rank[father2]:
                rank[father2] += rank[father1]
                par[father1] = par[father2]
            else:
                rank[father1] += rank[father2]
                par[father2] = par[father1]
            return 1

        res = 0
        for n1, n2 in edges:
            res += union(n1, n2)
        return n - res


s = Solution
print(s.countComponents(s, 5, [[0, 1], [1, 2], [0, 2], [3, 4]]))
