class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])

        def flip_row(row_ind) -> None:
            for col_ind in range(cols):
                grid[row_ind][col_ind] = 1 if not grid[row_ind][col_ind] else 0

        for ind, row in enumerate(grid):
            if row[0] == 0:
                flip_row(ind)

        res: int = rows * 2 ** (cols - 1)
        for col_ind in range(1, cols, 1):
            zeros: int = 0
            for row in grid:
                if row[col_ind] == 0:
                    zeros += 1
            ones: int = max(
                rows - zeros, zeros
            )  # if we have more 1 (rows - zeros) then we won't flip this column else we flip it and gets zeros 1
            res += ones * 2 ** (cols - col_ind - 1)

        return res
