class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        prefix_rows = [[0 for _ in range(cols)] for _ in range(rows)]
        prefix_cols = [[0 for _ in range(rows)] for _ in range(cols)]

        for row_ind in range(rows):
            s = 0
            for col_ind in range(cols):
                if matrix[row_ind][col_ind] == 1:
                    s += 1
                prefix_rows[row_ind][col_ind] = s

        for col_ind in range(cols):
            s = 0
            for row_ind in range(rows):
                if matrix[row_ind][col_ind] == 1:
                    s += 1
                prefix_cols[col_ind][row_ind] = s

        res = 0
        for row_ind_start in range(rows):
            for col_ind_start in range(cols):
                for size in range(1, min(rows - row_ind_start, cols - col_ind_start) + 1):
                    row_end = row_ind_start + size - 1
                    col_end = col_ind_start + size - 1

                    if (
                        prefix_rows[row_end][col_end]
                        - (prefix_rows[row_end][col_ind_start - 1] if col_ind_start > 0 else 0)
                    ) != size:
                        break

                    if (
                        prefix_cols[col_end][row_end]
                        - (prefix_cols[col_end][row_ind_start - 1] if row_ind_start > 0 else 0)
                    ) != size:
                        break

                    res += 1

        return res


class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        result = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    result += dp[i][j]

        return result
