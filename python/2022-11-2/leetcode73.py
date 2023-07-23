from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        modify_row = set()
        modify_col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    modify_row.add(i)
                    modify_col.add(j)
        for r in modify_row:
            matrix[r][:] = [0] * len(matrix[r])

        for c in modify_col:
            for i in range(len(matrix)):
                matrix[i][c] = 0


s = Solution
print(s.setZeroes(s, [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]))
