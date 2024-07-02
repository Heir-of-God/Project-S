class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        # 2 - alive now but will be dead
        # 3 - dead now but will be alive
        rows = len(board)
        cols = len(board[0])

        def calculate_state_for_cell(row_ind, col_ind):
            neighbors_alive = 0
            cur_state = board[row_ind][col_ind]
            for delta_row in range(-1, 2, 1):
                for delta_col in range(-1, 2, 1):
                    n_row_ind = row_ind + delta_row
                    n_col_ind = col_ind + delta_col
                    if (
                        not (n_row_ind == row_ind and n_col_ind == col_ind)
                        and 0 <= n_row_ind < rows
                        and 0 <= n_col_ind < cols
                    ):
                        neighbors_alive += board[n_row_ind][n_col_ind] in [1, 2]

            if cur_state == 1:
                if neighbors_alive < 2 or neighbors_alive > 3:
                    return 2
                return 1
            else:
                if neighbors_alive == 3:
                    return 3
                return 0

        for row_ind in range(rows):
            for col_ind in range(cols):
                board[row_ind][col_ind] = calculate_state_for_cell(row_ind, col_ind)

        for row_ind in range(rows):
            for col_ind in range(cols):
                if board[row_ind][col_ind] == 2:
                    board[row_ind][col_ind] = 0
                elif board[row_ind][col_ind] == 3:
                    board[row_ind][col_ind] = 1

        return board
