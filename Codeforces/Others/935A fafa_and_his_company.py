n = int(input())
res = 0

for i in range(1, n // 2 + 1, 1):
    if (n - i) % i == 0:
        res += 1


print(res)
