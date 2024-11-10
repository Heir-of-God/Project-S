t = int(input())

for _ in range(t):
    n = int(input())
    res = 1

    while res * 10 <= n:
        res *= 10

    print(n - res)
