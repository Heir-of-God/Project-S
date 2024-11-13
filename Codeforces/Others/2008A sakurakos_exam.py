t = int(input())

for _ in range(t):
    a, b = [int(i) for i in input().split()]

    if a * 2 <= b:
        b -= a * 2
        print("YES" if b & 1 == 0 else "NO")
    else:
        a -= b * 2
        print("YES" if a & 1 == 0 else "NO")
