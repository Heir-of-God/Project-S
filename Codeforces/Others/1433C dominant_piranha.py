t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    mx = max(arr)
    res = -1

    for ind in range(n):
        if arr[ind] == mx:
            left = arr[max(ind - 1, 0)]
            right = arr[min(n - 1, ind + 1)]
            if left != mx or right != mx:
                res = ind + 1
                break

    print(res)
