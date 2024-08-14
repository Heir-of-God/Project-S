class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        res: list[int] = [0, 0, 0, 0, 0]
        coordinates_set = set(tuple(coord) for coord in coordinates)

        def count_black_cells(row_ind, col_ind) -> int:
            return sum(
                (row, col) in coordinates_set
                for row, col in [
                    (row_ind, col_ind),
                    (row_ind + 1, col_ind),
                    (row_ind, col_ind + 1),
                    (row_ind + 1, col_ind + 1),
                ]
            )

        for row_ind, col_ind in coordinates_set:
            for row_ind_d in range(max(0, row_ind - 1), min(m - 1, row_ind + 1), 1):
                for col_ind_d in range(max(0, col_ind - 1), min(n - 1, col_ind + 1)):
                    black_cells_count: int = count_black_cells(row_ind_d, col_ind_d)
                    res[black_cells_count] += 1

        for colored_num in range(2, 5):
            res[colored_num] //= colored_num

        total_blocks: int = (m - 1) * (n - 1)
        res[0] = total_blocks - sum(res[1:])
        return res
