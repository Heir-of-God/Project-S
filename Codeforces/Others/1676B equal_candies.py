t = int(input())


for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    mn = min(arr)
    res = 0
    for n in arr:
        res += n - mn

    print(res)
