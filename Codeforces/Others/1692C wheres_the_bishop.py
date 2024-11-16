t = int(input())

for _ in range(t):
    input()
    board = [input() for _ in range(8)]

    for row_ind in range(1, 7):
        for col_ind in range(1, 7):
            if (
                board[row_ind - 1][col_ind - 1]
                == board[row_ind + 1][col_ind + 1]
                == board[row_ind + 1][col_ind - 1]
                == board[row_ind - 1][col_ind + 1]
                == "#"
            ):
                print(row_ind + 1, col_ind + 1)
                continue
