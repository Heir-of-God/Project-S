class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n: int = len(grid)

        def get_maximum(row_i, col_i) -> int:
            res = 0
            for row in range(row_i - 1, row_i + 2, 1):
                for col in range(col_i - 1, col_i + 2, 1):
                    if grid[row][col] > res:
                        res = grid[row][col]
            return res

        for row_ind in range(1, n - 1):
            for col_ind in range(1, n - 1):
                grid[row_ind - 1][col_ind - 1] = get_maximum(row_ind, col_ind)

        grid = [
            row_ind[: n - 2] for row_ind in grid[: n - 2]
        ]  # every time we put maximum one to the left and upper, so our result will be from 0 to n - 2 indexes

        return grid
