t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]

    mx1 = 0
    mx2 = 0

    for num in arr:
        if num >= mx1:
            mx2 = mx1
            mx1 = num
        elif num > mx2:
            mx2 = num

    for ind in range(n):
        if arr[ind] == mx1:
            arr[ind] = arr[ind] - mx2
        else:
            arr[ind] = arr[ind] - mx1

    print(*arr)
