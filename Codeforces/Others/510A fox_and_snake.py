rows, cols = [int(i) for i in input().split()]

res = [["." if row_ind & 1 == 1 else "#" for _ in range(cols)] for row_ind in range(rows)]
right = True

for row_ind in range(1, rows, 2):
    res[row_ind][-1 if right else 0] = "#"
    right = not right

for row in res:
    print("".join(row))
