t = int(input())

for _ in range(t):
    n, k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]

    stable = True
    mn1 = float("inf")
    mn2 = float("inf")
    for el in arr:
        if el <= mn1:
            mn2 = mn1
            mn1 = el
        elif el < mn2:
            mn2 = el

        if el > k:
            stable = False

    print("YES" if stable or mn1 + mn2 <= k else "NO")
