t = int(input())

for _ in range(t):
    n = int(input()) - 3
    res = [1, 1, 1]
    ind = 2

    while n > 0:
        res[ind] += min(n, 25)
        n -= 25
        ind -= 1

    print("".join([chr(i + ord("a") - 1) for i in res]))
