class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])
        total_flips: int = 0

        cols_one_change = 0
        cols_both_1 = 0

        row_one_change = 0
        rows_both_1 = 0

        for row_ind in range((rows + 1) // 2):
            reversed_row_ind: int = rows - row_ind - 1
            for col_ind in range((cols + 1) // 2):
                reversed_col_ind: int = cols - col_ind - 1

                cells: list[int] = [
                    grid[row_ind][col_ind],
                    grid[row_ind][reversed_col_ind],
                    grid[reversed_row_ind][col_ind],
                    grid[reversed_row_ind][reversed_col_ind],
                ]
                count: list[int] = [0, 0]
                for cell in cells:
                    count[cell] += 1

                if reversed_row_ind != row_ind and reversed_col_ind != col_ind:
                    total_flips += min(count)

                elif reversed_row_ind == row_ind and reversed_col_ind == col_ind:
                    total_flips += cells[0] == 1

                elif reversed_col_ind == col_ind:
                    if cells[0] != cells[3]:
                        cols_one_change += 1
                        total_flips += 1
                    else:
                        if cells[0] == cells[3] == 1:
                            cols_both_1 += 1

                elif reversed_row_ind == row_ind:
                    if cells[1] != cells[2]:
                        row_one_change += 1
                        total_flips += 1
                    else:
                        if cells[0] == cells[3] == 1:
                            rows_both_1 += 1

        if (2 * (rows_both_1 + cols_both_1)) % 4 != 0:
            if not (cols_one_change or row_one_change):
                total_flips += 2

        return total_flips
