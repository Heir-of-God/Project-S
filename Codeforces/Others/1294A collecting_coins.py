t = int(input())

for _ in range(t):
    a, b, c, n = [int(i) for i in input().split()]
    mx = max((a, b, c))
    need = 3 * mx - a - b - c

    print("YES" if need <= n and (n - need) % 3 == 0 else "NO")
