class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        cur_step: int = 1
        dirs: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir: int = 0
        cur_row: int = rStart
        cur_col: int = cStart
        progress: int = 0
        res: list[list[int]] = []

        while len(res) != rows * cols:
            if 0 <= cur_row < rows and 0 <= cur_col < cols:
                res.append([cur_row, cur_col])

            cur_row += dirs[cur_dir][0]
            cur_col += dirs[cur_dir][1]
            progress += 1
            if progress == cur_step:
                if cur_dir in [1, 3]:
                    cur_step += 1
                cur_dir = (cur_dir + 1) % 4
                progress = 0

        return res
