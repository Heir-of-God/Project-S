t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    res = 10**9

    for ind in range(1, n):
        if arr[ind - 1] > arr[ind]:
            res = 0
            break
        res = min(res, (arr[ind] - arr[ind - 1]) // 2 + 1)

    print(res)
