class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        res = 0
        ROWS: int = len(grid)
        COLS: int = len(grid[0])

        def check_all_paths(cur_row, cur_col, cur_sum):
            if not 0 <= cur_row < ROWS or not 0 <= cur_col < COLS or grid[cur_row][cur_col] == 0:
                return cur_sum
            gold_in_cell: int = grid[cur_row][cur_col]
            grid[cur_row][cur_col] = 0
            cur_sum += gold_in_cell
            cur_sum = max(
                check_all_paths(cur_row + 1, cur_col, cur_sum),
                check_all_paths(cur_row - 1, cur_col, cur_sum),
                check_all_paths(cur_row, cur_col + 1, cur_sum),
                check_all_paths(cur_row, cur_col - 1, cur_sum),
            )
            grid[cur_row][cur_col] = gold_in_cell
            return cur_sum

        for start_row in range(ROWS):
            for start_col in range(COLS):
                if grid[start_row][start_col] != 0:
                    res = max(res, check_all_paths(start_row, start_col, 0))

        return res
