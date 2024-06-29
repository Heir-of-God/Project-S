class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        valid_nums: set[str] = set([str(i) for i in range(1, 10, 1)])
        n: int = len(board)

        column_count: dict[int, set[int]] = {ind: set() for ind in range(n)}  # col_ind -> set()
        squares_count: dict[int, dict[int, set[int]]] = {
            i: {ind: set() for ind in range(n // 3)} for i in range(n // 3)
        }

        for row_ind in range(n):
            cur_row_count = set()
            for col_ind in range(n):
                char: str = board[row_ind][col_ind]
                if char == ".":
                    continue
                if char not in valid_nums:
                    return False

                if char in cur_row_count:
                    return False
                cur_row_count.add(char)

                if char in column_count[col_ind]:
                    return False
                column_count[col_ind].add(char)

                if char in squares_count[row_ind // 3][col_ind // 3]:
                    return False
                squares_count[row_ind // 3][col_ind // 3].add(char)

        return True
