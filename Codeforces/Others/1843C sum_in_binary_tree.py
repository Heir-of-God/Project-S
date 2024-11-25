t = int(input())

for _ in range(t):
    n = int(input())
    res = 1

    while n != 1:
        res += n
        prev = n // 2
        n = prev

    print(res)
