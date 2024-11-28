t = int(input())

for _ in range(t):
    a, b, c, x, y = [int(i) for i in input().split()]

    if x > a:
        c -= x - a

    if y > b:
        c -= y - b

    print("YES" if c >= 0 else "NO")
