t = int(input())

for _ in range(t):
    n = int(input())
    res = []
    mult = 0
    while n > 0:
        cur = n % 10 * 10**mult
        if cur != 0:
            res.append(cur)
        mult += 1
        n //= 10
    print(len(res))
    print(*res)
