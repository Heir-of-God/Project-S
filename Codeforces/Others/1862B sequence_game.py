t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    res = []

    for ind in range(n):
        res.append(arr[ind])
        if ind != n - 1 and res[-1] > arr[ind + 1]:
            res.append(1)

    print(len(res))
    print(*res)
