t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    mn = min(arr)
    arr[arr.index(mn)] += 1

    s = 1
    for n in arr:
        s *= n

    print(s)
