t = int(input())

for _ in range(t):
    n, x = [int(i) for i in input().split()]
    stations = [int(i) for i in input().split()]
    stations = [0] + stations + [(x - stations[-1]) * 2 + stations[-1]]

    res = 1
    for i in range(1, n + 2):
        res = max(res, stations[i] - stations[i - 1])

    print(res)
