t = int(input())

for _ in range(t):
    x, y = [int(i) for i in input().split()]
    mn = min(x, y)
    print(mn, x + y - mn)
