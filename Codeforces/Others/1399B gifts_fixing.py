t = int(input())

for _ in range(t):
    n = int(input())
    arr1 = [int(i) for i in input().split()]
    arr2 = [int(i) for i in input().split()]
    res = 0

    mnar1 = min(arr1)
    mnar2 = min(arr2)

    for i in range(n):
        res += max(arr1[i] - mnar1, arr2[i] - mnar2)

    print(res)
