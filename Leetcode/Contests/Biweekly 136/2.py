class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])

        res_rows = 0
        for row in grid:
            for ind in range(cols // 2):
                reversed_ind: int = cols - ind - 1
                res_rows += row[ind] != row[reversed_ind]

        res_cols = 0
        for col_ind in range(cols):
            for row_ind in range(rows // 2):
                reversed_ind: int = rows - row_ind - 1
                res_cols += grid[row_ind][col_ind] != grid[reversed_ind][col_ind]

        return min(res_cols, res_rows)
