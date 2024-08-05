t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()

    mx = 0
    mx_par = 0
    for n in arr:
        if n & 1 == 1:
            mx = max(mx, n)
        else:
            mx_par = max(mx_par, n)

    if mx == 0:
        print(0)
        continue

    res = 0
    for n in arr:
        if n & 1 == 1:
            continue

        while mx < n:
            mx += mx_par
            res += 1

        res += 1
        mx = max(mx, n + mx)

    print(res)
