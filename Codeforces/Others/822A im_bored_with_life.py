a, b = [int(i) for i in input().split()]

res = 1
for n in range(2, min(a, b) + 1, 1):
    res *= n

print(res)
