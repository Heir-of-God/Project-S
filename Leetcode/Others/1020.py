class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])

        def dfs(row, col) -> int:
            grid[row][col] = 0
            res = 1

            for rowd, cold in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                rnew, cnew = row + rowd, col + cold
                if 0 <= rnew < rows and 0 <= cnew < cols and grid[rnew][cnew] == 1:
                    res += dfs(rnew, cnew)

            return res

        for row_ind in range(rows):
            for col_ind in (0, cols - 1):
                if grid[row_ind][col_ind] == 1:
                    dfs(row_ind, col_ind)

        for col_ind in range(cols):
            for row_ind in (0, rows - 1):
                if grid[row_ind][col_ind] == 1:
                    dfs(row_ind, col_ind)

        res = 0
        for row_ind in range(1, rows - 1, 1):
            for col_ind in range(1, cols - 1, 1):
                if grid[row_ind][col_ind] == 1:
                    res += dfs(row_ind, col_ind)

        return res
