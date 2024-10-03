t = int(input())

for _ in range(t):
    target = [input() for _ in range(10)]
    res = 0

    for row_ind in range(10):
        for col_ind in range(10):
            if target[row_ind][col_ind] == "X":
                true_row = row_ind if row_ind <= 4 else 9 - row_ind
                true_col = col_ind if col_ind <= 4 else 9 - col_ind

                for ind in range(5):
                    if ind in (true_row, true_col):
                        res += ind + 1
                        break

    print(res)
