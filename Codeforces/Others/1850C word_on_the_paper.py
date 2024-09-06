t = int(input())

for _ in range(t):
    arr = [input() for _ in range(8)]
    res = ""
    for row in arr:
        for char in row:
            if char != ".":
                res += char

    print(res)
