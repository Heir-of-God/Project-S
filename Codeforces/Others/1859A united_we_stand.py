t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    if a[0] == a[-1]:
        print(-1)
    else:
        cnt = a.count(a[-1])
        b = a[:-cnt]
        c = a[-cnt:]
        print(len(b), len(c))
        print(*b)
        print(*c)
