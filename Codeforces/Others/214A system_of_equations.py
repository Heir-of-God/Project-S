n, m = [int(i) for i in input().split()]
res = 0

for a in range(0, m + 2, 1):
    for b in range(0, n + 2, 1):
        if a**2 + b == n and a + b**2 == m:
            res += 1

print(res)
