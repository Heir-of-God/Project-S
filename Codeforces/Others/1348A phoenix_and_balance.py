t = int(input())

for _ in range(t):
    n = int(input())
    els = [2**i for i in range(1, n + 1, 1)]
    greater = els[-1] + sum(els[: n // 2 - 1])
    lower = sum(els[n // 2 - 1 : -1])

    print(greater - lower)
