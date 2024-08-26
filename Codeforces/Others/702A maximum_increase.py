n = int(input())
arr = [int(i) for i in input().split()]
arr.append(0)
res = 1
cur = 1

for ind in range(1, n + 1, 1):
    if arr[ind] > arr[ind - 1]:
        cur += 1
    else:
        res = max(res, cur)
        cur = 1

print(res)
