t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    mn = float("inf")

    for ind in range(1, n):
        mn = min(mn, arr[ind] - arr[ind - 1])

    print(mn)
