t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    arr.append(-1)

    res = 0
    for ind in range(1, n + 1):
        if arr[ind] != arr[ind - 1]:
            res += 1

    print(res)
