t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]

    res = "YES"

    for ind in range(3, n, 2):
        if arr[ind] & 1 != arr[ind - 2] & 1 or arr[ind - 1] & 1 != arr[ind - 3] & 1:
            res = "NO"
            break

    print(res if ((n >= 3 and arr[n - 1] & 1 == arr[n - 3] & 1) or n <= 2) else "NO")
