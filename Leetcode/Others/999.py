from typing import Literal


class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        def find_rook() -> tuple[int, int]:
            for row in range(8):
                for col in range(8):
                    if board[row][col] == "R":
                        return (row, col)
            return (-1, -1)

        rook_row, rook_col = find_rook()
        res = 0

        for row in range(rook_row + 1, 8, 1):
            if board[row][rook_col] == "p":
                res += 1
            if board[row][rook_col] in "Bp":
                break

        for row in range(rook_row - 1, -1, -1):
            if board[row][rook_col] == "p":
                res += 1
            if board[row][rook_col] in "Bp":
                break

        for col in range(rook_col + 1, 8, 1):
            if board[rook_row][col] == "p":
                res += 1
            if board[rook_row][col] in "Bp":
                break

        for col in range(rook_col - 1, -1, -1):
            if board[rook_row][col] == "p":
                res += 1
            if board[rook_row][col] in "Bp":
                break

        return res
