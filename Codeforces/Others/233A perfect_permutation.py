n = int(input())

if n & 1 == 1:
    print(-1)
else:
    res = []

    for num in range(1, n, 2):
        res.append(num + 1)
        res.append(num)

    print(" ".join([str(i) for i in res]))
