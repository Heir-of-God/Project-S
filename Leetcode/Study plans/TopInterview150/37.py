class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows: int = len(matrix)
        cols: int = len(matrix[0])

        def set_row(row_ind) -> None:
            for col_ind in range(cols):
                if matrix[row_ind][col_ind] != 0:
                    matrix[row_ind][col_ind] = "c"

        def set_col(col_ind) -> None:
            for row_ind in range(rows):
                if matrix[row_ind][col_ind] != 0:
                    matrix[row_ind][col_ind] = "c"

        for row_ind in range(rows):
            for col_ind in range(cols):
                if matrix[row_ind][col_ind] == 0:
                    set_row(row_ind)
                    set_col(col_ind)

        for row_ind in range(rows):
            for col_ind in range(cols):
                if matrix[row_ind][col_ind] == "c":
                    matrix[row_ind][col_ind] = 0
