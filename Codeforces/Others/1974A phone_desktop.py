t = int(input())

for _ in range(t):
    x, y = [int(i) for i in input().split()]
    res = 0

    while x > 0 or y > 0:
        occupied2 = min(2, y) * 4
        y -= min(2, y)
        x -= 15 - occupied2
        res += 1

    print(res)
