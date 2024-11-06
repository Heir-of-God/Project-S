t = int(input())

for _ in range(t):
    a, b, c = [int(i) for i in input().split()]

    between = abs(a - b) - 1
    in_circle = between * 2 + 2
    res = c + between + 1 if c <= (in_circle // 2) else c - between - 1

    if between <= 0 or max(a, b, c) > in_circle or not 1 <= res <= in_circle:
        print(-1)
        continue

    print(res)
