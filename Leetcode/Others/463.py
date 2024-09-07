class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])

        def dfs(cur_row: int, cur_col: int) -> int:
            res = 0
            grid[cur_row][cur_col] = 2
            for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nrow, ncol = drow + cur_row, dcol + cur_col
                if 0 <= nrow < rows and 0 <= ncol < cols:
                    if grid[nrow][ncol] == 0:
                        res += 1
                    elif grid[nrow][ncol] == 1:
                        res += dfs(nrow, ncol)
                else:
                    res += 1

            return res

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return dfs(row, col)
