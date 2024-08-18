rows, cols = [int(i) for i in input().split()]
photo = [input().split() for _ in range(rows)]

baw = True
for row in photo:
    for val in row:
        if val not in "BWG":
            baw = False

print("#Black&White" if baw else "#Color")
