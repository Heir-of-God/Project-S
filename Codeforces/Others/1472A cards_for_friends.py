t = int(input())

for _ in range(t):
    w, h, n = [int(i) for i in input().split()]
    cutting_w = 1
    cutting_h = 1
    while w & 1 == 0:
        cutting_w *= 2
        w //= 2

    while h & 1 == 0:
        cutting_h *= 2
        h //= 2

    print("YES" if cutting_h * cutting_w >= n else "NO")
