t = int(input())

for _ in range(t):
    n = int(input())
    res = [i + 1 for i in range(n)][::-1]
    if n & 1 == 1:
        res[n // 2], res[-1] = res[-1], res[n // 2]

    print(*res)
