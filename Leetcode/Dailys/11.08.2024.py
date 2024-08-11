class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])

        def dfs(cur_row: int, cur_col: int, src: list[list[int]]) -> None:
            queue: list[tuple[int, int]] = [(cur_row, cur_col)]
            while queue:
                r, c = queue.pop()
                if 0 <= r < rows and 0 <= c < cols and src[r][c] == 1:
                    src[r][c] = 0
                    queue.append((r + 1, c))
                    queue.append((r - 1, c))
                    queue.append((r, c + 1))
                    queue.append((r, c - 1))

        def check_grid(grid: list[list[int]]) -> int:
            grid: list[list[int]] = [row[:] for row in grid]
            res = 0

            for row_ind in range(rows):
                for col_ind in range(cols):
                    if grid[row_ind][col_ind] == 1:
                        res += 1
                        dfs(row_ind, col_ind, grid)

            return res

        initial: int = check_grid(grid)
        if initial != 1:
            return 0

        for row_ind in range(rows):
            for col_ind in range(cols):
                if grid[row_ind][col_ind] == 1:
                    grid[row_ind][col_ind] = 0
                    if check_grid(grid) != 1:
                        return 1
                    grid[row_ind][col_ind] = 1

        return 2
