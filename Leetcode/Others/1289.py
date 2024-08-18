class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def get_two_min(row):
            mn1 = [-1, 2 * 10**4]
            mn2 = [-1, 2 * 10**4]

            for col, val in enumerate(row):
                if val <= mn1[1]:
                    mn2 = mn1
                    mn1 = [col, val]
                elif val <= mn2[1]:
                    mn2 = [col, val]

            return mn1, mn2

        for row_ind in range(1, rows, 1):
            prev_mn1, prev_mn2 = get_two_min(grid[row_ind - 1])
            for col_ind in range(cols):
                if prev_mn1[0] != col_ind:
                    grid[row_ind][col_ind] += prev_mn1[1]
                else:
                    grid[row_ind][col_ind] += prev_mn2[1]

        return min(grid[-1])
