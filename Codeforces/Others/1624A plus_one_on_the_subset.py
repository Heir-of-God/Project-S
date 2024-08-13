t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    mx = max(arr)
    res = 0

    for el in arr:
        res = max(mx - el, res)

    print(res)
