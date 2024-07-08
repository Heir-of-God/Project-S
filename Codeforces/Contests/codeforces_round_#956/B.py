t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, list(input().strip()))) for _ in range(n)]
    b = [list(map(int, list(input().strip()))) for _ in range(n)]

    res = "YES"

    for row_ind in range(n - 1, 0, -1):
        for col_ind in range(m - 1, 0, -1):
            if a[row_ind][col_ind] != b[row_ind][col_ind]:
                diff = (b[row_ind][col_ind] - a[row_ind][col_ind] + 3) % 3
                # preform converting
                a[row_ind][col_ind] = b[row_ind][col_ind]
                a[row_ind - 1][col_ind] = (a[row_ind - 1][col_ind] + 2 * diff) % 3
                a[row_ind][col_ind - 1] = (a[row_ind][col_ind - 1] + 2 * diff) % 3
                a[row_ind - 1][col_ind - 1] = (a[row_ind - 1][col_ind - 1] + diff) % 3

    for row_ind in range(n):
        if a[row_ind][0] != b[row_ind][0]:
            res = "NO"
            break

    for col_ind in range(m):
        if a[0][col_ind] != b[0][col_ind]:
            res = "NO"
            break

    print(res)
