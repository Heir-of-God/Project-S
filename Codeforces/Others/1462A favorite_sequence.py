t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    res = []

    for ind in range(n // 2):
        res.append(arr[ind])
        res.append(arr[n - ind - 1])

    if n & 1 == 1:
        res.append(arr[n // 2])

    print(*res)
