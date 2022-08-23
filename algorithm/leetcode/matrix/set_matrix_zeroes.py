# https://leetcode.com/problems/set-matrix-zeroes/
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        queue = []
        max_row = len(matrix)
        max_col = len(matrix[0])

        for i in range(max_row):
            for j in range(max_col):
                if matrix[i][j] == 0:
                    queue.append((i, j))

        while queue:
            zero = queue.pop()
            row = zero[0]
            col = zero[1]
            for i in range(0, row):
                matrix[i][col] = 0
            for i in range(row, max_row):
                matrix[i][col] = 0
            for i in range(0, col):
                matrix[row][i] = 0
            for i in range(col, max_col):
                matrix[row][i] = 0


if __name__ == '__main__':
    s = Solution
    s.setZeroes(s, [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
