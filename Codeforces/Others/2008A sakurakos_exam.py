t = int(input())

for _ in range(t):
    a, b = [int(i) for i in input().split()]
    print("YES" if (a & 1 == b & 1 == 0) or (a & 1 == 0 and a > 0) else "NO")

