n = int(input())
res = 0

for _ in range(n):
    p, q = [int(i) for i in input().split()]
    if q - p >= 2:
        res += 1

print(res)
