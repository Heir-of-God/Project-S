class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows: int = len(matrix)
        cols: int = len(matrix[0])

        cur_row, cur_col = 0, 0
        cur_rows_boundary = 1
        cur_cols_boundary = 1
        dirs: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_ind_dir = 0
        res: list[int] = []
        visited = set()

        while not (cur_row, cur_col) in visited and 0 <= cur_row < rows and 0 <= cur_col <= cols:
            res.append(matrix[cur_row][cur_col])
            visited.add((cur_row, cur_col))

            if cur_ind_dir == 0 and cur_col == cols - cur_cols_boundary:
                cur_ind_dir += 1
            elif cur_ind_dir == 1 and cur_row == rows - cur_rows_boundary:
                cur_ind_dir += 1
            elif cur_ind_dir == 2 and cur_col == cur_cols_boundary - 1:
                cur_cols_boundary += 1
                cur_ind_dir += 1
            elif cur_ind_dir == 3 and cur_row == cur_rows_boundary:
                cur_rows_boundary += 1
                cur_ind_dir = 0

            cur_row += dirs[cur_ind_dir][0]
            cur_col += dirs[cur_ind_dir][1]

        return res
