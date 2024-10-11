from math import ceil

t = int(input())

for _ in range(t):
    a, b, c = [int(i) for i in input().split()]
    sm = a + b
    half = sm / 2
    res = (max(a, b) - half) / c

    print(ceil(res))
