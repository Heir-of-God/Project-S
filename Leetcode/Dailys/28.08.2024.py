class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        rows: int = len(grid1)
        cols: int = len(grid1[0])

        def is_subisland(cur_row: int, cur_col: int) -> bool:
            grid2[cur_row][cur_col] = 0
            res: int = grid1[cur_row][cur_col]
            for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = cur_row + drow, cur_col + dcol
                if 0 <= new_row < rows and 0 <= new_col < cols and grid2[new_row][new_col] == 1:
                    res &= is_subisland(new_row, new_col)

            return res

        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1:
                    res += is_subisland(row, col)

        return res
