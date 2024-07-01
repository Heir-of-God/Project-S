row = -1
col = -1

for row_ind in range(0, 5, 1):
    line = input().split()
    if "1" in line:
        row = row_ind
        col = line.index("1")

print(abs(2 - row) + abs(2 - col))
