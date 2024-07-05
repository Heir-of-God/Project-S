n = input()
row = input()
res = 0
prev = None

for char in row:
    if char != prev:
        prev = char
    else:
        res += 1

print(res)
