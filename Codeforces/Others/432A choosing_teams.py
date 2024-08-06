n, k = [int(i) for i in input().split()]
participated = [int(i) for i in input().split()]
res = 0

for p in participated:
    if 5 - p >= k:
        res += 1


print(res // 3)
