from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row = len(matrix)
        col = len(matrix[0])
        row_count = 0
        col_count = col - 1
        n = row * col
        while True:
            # top row
            for i in range(col - 1 - col_count, col_count + 1):
                res.append(matrix[row_count][i])
            # right col
            for j in range(row_count + 1, row - row_count):
                res.append(matrix[j][col_count])
            if len(res) == n:
                break
            # bottom row
            row_count = row - 1 - row_count
            for i in range(col_count - 1, col - 1 - col_count - 1, -1):
                res.append(matrix[row_count][i])
            # left col
            col_count = col - 1 - col_count
            for j in range(row_count - 1, row - 1 - row_count, -1):
                res.append(matrix[j][col_count])
            row_count = row - 1 - row_count + 1
            col_count = col - 1 - col_count - 1
            if len(res) == n:
                break
        return res


s = Solution
print(s.spiralOrder(s, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
