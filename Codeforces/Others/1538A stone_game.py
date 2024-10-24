t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    rev = arr[::-1]
    mx = max(arr)
    mn = min(arr)

    mx1 = arr.index(mx) + 1
    mx2 = rev.index(mx) + 1
    mn1 = arr.index(mn) + 1
    mn2 = rev.index(mn) + 1

    print(min(max(mx1, mn1), max(mx2, mn2), mx1 + mn2, mx2 + mn1))
