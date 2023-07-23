from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        count = 0

        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(start: List):
            if (start[0], start[1]) in visited:
                return
            visited.add((start[0], start[1]))
            for d in dir:
                next_r = start[0] + d[0]
                next_c = start[1] + d[1]
                if len(grid) > next_r >= 0 and len(grid[0]) > next_c >= 0 and grid[next_r][next_c] == '1':
                    dfs([next_r, next_c])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
                    dfs([i, j])
                    count += 1

        return count
