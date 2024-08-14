t = int(input())

for _ in range(t):
    a, b = [int(i) for i in input().split()]
    mn = min(a, b)
    mx = max(a, b)
    side = 2 * mn if 2 * mn >= mx else mx

    print(side**2)
