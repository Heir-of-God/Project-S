t = int(input())

for _ in range(t):
    n = int(input())
    rows = [input() for _ in range(n)][::-1]
    res = []

    for row in rows:
        res.append(row.find("#") + 1)

    print(*res)
