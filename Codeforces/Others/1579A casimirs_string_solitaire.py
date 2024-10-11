t = int(input())

for _ in range(t):
    s = input()
    n = len(s)

    bs = s.count("B")
    ac = n - bs

    print("YES" if ac == bs else "NO")
