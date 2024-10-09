t = int(input())

for _ in range(t):
    a, b, n = [int(i) for i in input().split()]
    a, b = max(a, b), min(a, b)

    res = 0
    while a <= n:
        res += 2
        b += a
        a += b

    if b > n:
        res -= 1

    print(res)
