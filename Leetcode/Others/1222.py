class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:
        queens = set([tuple(i) for i in queens])
        res: list[list[int]] = []

        for delta_row in range(-1, 2, 1):
            for delta_col in range(-1, 2, 1):
                if delta_row == 0 and delta_col == 0:
                    continue
                cur_row: int = king[0]
                cur_col: int = king[1]

                while 0 <= cur_row < 8 and 0 <= cur_col < 8:
                    cur_row += delta_row
                    cur_col += delta_col
                    if 0 <= cur_row < 8 and 0 <= cur_col < 8:
                        if (cur_row, cur_col) in queens:
                            res.append([cur_row, cur_col])
                            break

        return res
