t = int(input())

for _ in range(t):
    n = int(input())

    res = 0

    while n != 1:
        res <<= 1
        res += 1
        n >>= 1

    print(res)
