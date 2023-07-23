from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ok = set()
        ok_pac = [[False] * len(heights[0]) for i in range(len(heights))]
        ok_alt = [[False] * len(heights[0]) for i in range(len(heights))]
        ok.add((0, len(heights[0]) - 1))
        ok.add((len(heights) - 1, 0))
        for i in range(len(heights[0])):
            ok_pac[0][i] = True
            ok_alt[len(heights) - 1][i] = True
        for i in range(len(heights)):
            ok_pac[i][0] = True
            ok_alt[i][len(heights[0]) - 1] = True

        visited = set()
        all_visited = set()

        def dfs(node: List[int]):
            if (node[0], node[1]) in ok:
                return True
            if dfs_sea(node, ok_pac) and dfs_sea(node, ok_alt):
                ok.add((node[0], node[1]))
                return True
            return False

        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs_sea(node: List[int], sea: List[List[bool]]):
            if sea[node[0]][node[1]]:
                return True
            if (node[0], node[1]) in visited:
                return False

            visited.add((node[0], node[1]))
            for d in dir:
                next_r = node[0] + d[0]
                next_c = node[1] + d[1]
                if len(heights) > next_r >= 0 and len(heights[0]) > next_c >= 0 and heights[node[0]][node[1]] >= \
                        heights[next_r][next_c]:
                    if (next_r, next_c) in all_visited and (next_r, next_c) in ok:
                        sea[node[0]][node[1]] = True
                        visited.remove((node[0], node[1]))
                        return True

                    if dfs_sea([next_r, next_c], sea):
                        sea[node[0]][node[1]] = True
                        visited.remove((node[0], node[1]))
                        return True
            visited.remove((node[0], node[1]))
            return False

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if dfs([i, j]):
                    res.append([i, j])
                all_visited.add((i, j))
        return res


s = Solution
print(s.pacificAtlantic(s, [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
