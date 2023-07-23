from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        core = [0 for _ in range(9)]
        n = len(grid)
        res = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                for m in range(3):
                    for n in range(3):
                        core[m * 3 + n] = grid[m + i][n + j]
                res[i][j] = max(core)
        return res


s = Solution()
print(s.largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
