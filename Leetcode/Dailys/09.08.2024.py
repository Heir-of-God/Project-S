class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        for row_start in range(0, ROWS - 2, 1):
            for col_start in range(0, COLS - 2, 1):
                is_magic = True
                square = [[] for _ in range(3)]
                seen = set()
                row_sums = [0, 0, 0]
                col_sums = [0, 0, 0]

                for row in range(row_start, row_start + 3, 1):
                    for col in range(col_start, col_start + 3, 1):
                        el = grid[row][col]
                        if el in seen or not 1 <= el <= 9:
                            is_magic = False
                            break
                        seen.add(el)
                        square[row - row_start].append(el)
                        row_sums[row - row_start] += el
                        col_sums[col - col_start] += el
                    if not is_magic:
                        break

                sm = row_sums[0]
                for val in col_sums:
                    if val != sm:
                        is_magic = False
                        break
                for val in row_sums:
                    if val != sm or not is_magic:
                        is_magic = False
                        break

                if is_magic and (
                    sm - square[1][1] != square[0][0] + square[2][2]
                    or square[0][0] + square[2][2] != square[2][0] + square[0][2]
                ):
                    is_magic = False

                if is_magic:
                    res += 1

        return res
