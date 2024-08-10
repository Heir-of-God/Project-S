class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        def dfs(cur_row: int, cur_col: int) -> None:
            if not (0 <= cur_row < rows * 3) or not (0 <= cur_col < cols * 3) or matrix[cur_row][cur_col] == 1:
                return
            matrix[cur_row][cur_col] = 1
            dfs(cur_row + 1, cur_col)
            dfs(cur_row - 1, cur_col)
            dfs(cur_row, cur_col + 1)
            dfs(cur_row, cur_col - 1)

            return

        rows: int = len(grid)
        cols: int = len(grid[0])

        matrix: list[list[int]] = [[0 for _ in range(cols * 3)] for _ in range(rows * 3)]
        for row_ind, row in enumerate(grid):
            for col_ind, el in enumerate(row):
                if el == "/":
                    matrix[row_ind * 3][col_ind * 3 + 2] = 1
                    matrix[row_ind * 3 + 1][col_ind * 3 + 1] = 1
                    matrix[row_ind * 3 + 2][col_ind * 3] = 1
                elif el == "\\":
                    matrix[row_ind * 3][col_ind * 3] = 1
                    matrix[row_ind * 3 + 1][col_ind * 3 + 1] = 1
                    matrix[row_ind * 3 + 2][col_ind * 3 + 2] = 1

        res = 0
        for row_ind in range(rows * 3):
            for col_ind in range(cols * 3):
                if matrix[row_ind][col_ind] == 0:
                    res += 1
                    dfs(row_ind, col_ind)

        return res


class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        def dfs(src_row: int, src_col: int) -> None:
            queue: list[tuple[int, int]] = [(src_row, src_col)]

            while queue:
                cur_row, cur_col = queue.pop()
                if 0 <= cur_row < rows * 3 and 0 <= cur_col < cols * 3 and matrix[cur_row][cur_col] == 0:
                    matrix[cur_row][cur_col] = 1
                    queue.append((cur_row + 1, cur_col))
                    queue.append((cur_row - 1, cur_col))
                    queue.append((cur_row, cur_col + 1))
                    queue.append((cur_row, cur_col - 1))

            return

        rows: int = len(grid)
        cols: int = len(grid[0])

        matrix: list[list[int]] = [[0 for _ in range(cols * 3)] for _ in range(rows * 3)]
        for row_ind, row in enumerate(grid):
            for col_ind, el in enumerate(row):
                if el == "/":
                    matrix[row_ind * 3][col_ind * 3 + 2] = 1
                    matrix[row_ind * 3 + 1][col_ind * 3 + 1] = 1
                    matrix[row_ind * 3 + 2][col_ind * 3] = 1
                elif el == "\\":
                    matrix[row_ind * 3][col_ind * 3] = 1
                    matrix[row_ind * 3 + 1][col_ind * 3 + 1] = 1
                    matrix[row_ind * 3 + 2][col_ind * 3 + 2] = 1

        res = 0
        for row_ind in range(rows * 3):
            for col_ind in range(cols * 3):
                if matrix[row_ind][col_ind] == 0:
                    res += 1
                    dfs(row_ind, col_ind)

        return res
