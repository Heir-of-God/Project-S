n = int(input())

matrix = [[1 for _ in range(n)] for _ in range(n)]

for row_ind in range(1, n):
    for col_ind in range(1, n):
        matrix[row_ind][col_ind] = matrix[row_ind - 1][col_ind] + matrix[row_ind][col_ind - 1]

print(matrix[n - 1][n - 1])
