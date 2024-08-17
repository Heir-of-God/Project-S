t = int(input())

for _ in range(t):
    p1, p2, p3, p4 = [int(i) for i in input().split()]
    g1 = sorted([p1, p2])
    g2 = sorted([p3, p4])

    mx1, mx2 = sorted(g1 + g2, reverse=True)[:2]
    if mx1 in g1 and mx2 in g2 or mx2 in g1 and mx1 in g2:
        print("YES")
    else:
        print("NO")
