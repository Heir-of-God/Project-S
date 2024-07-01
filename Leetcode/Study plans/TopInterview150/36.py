class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for row_ind in range(n):
            for col_ind in range(row_ind + 1):
                matrix[row_ind][col_ind], matrix[col_ind][row_ind] = matrix[col_ind][row_ind], matrix[row_ind][col_ind]
        for row_ind in range(n):
            for col_ind in range(n // 2):
                matrix[row_ind][col_ind], matrix[row_ind][n - col_ind - 1] = (
                    matrix[row_ind][n - col_ind - 1],
                    matrix[row_ind][col_ind],
                )
