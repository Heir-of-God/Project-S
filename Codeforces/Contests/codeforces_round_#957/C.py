t = int(input())

for _ in range(t):
    n, m, k = [int(i) for i in input().split()]
    res = [i + 1 for i in range(n)]
    res.reverse()
    res[n - m :] = reversed(res[n - m :])
    print(" ".join([str(i) for i in res]))
