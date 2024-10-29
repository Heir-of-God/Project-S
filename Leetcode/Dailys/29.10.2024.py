class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])
        dp: list[list[bool]] = [[False for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            dp[row][0] = True

        for col_ind in range(1, cols):
            can_reach_here = False
            for row_ind in range(rows):
                for src_row in range(max(row_ind - 1, 0), min(row_ind + 1, rows - 1) + 1, 1):
                    if dp[src_row][col_ind - 1] == True and grid[src_row][col_ind - 1] < grid[row_ind][col_ind]:
                        can_reach_here = True
                        dp[row_ind][col_ind] = True
                        break
            if not can_reach_here:
                break

        return col_ind - 1 if not can_reach_here else col_ind
