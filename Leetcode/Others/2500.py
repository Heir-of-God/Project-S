class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])

        for row_ind in range(rows):
            grid[row_ind].sort()

        res = 0
        for col_ind in range(cols):
            res += max([grid[row_ind][col_ind] for row_ind in range(rows)])

        return res
