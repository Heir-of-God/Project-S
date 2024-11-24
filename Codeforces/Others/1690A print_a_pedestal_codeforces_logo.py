t = int(input())

for _ in range(t):
    n = int(input())
    base = n // 3
    blocks = n - 3 * base
    if n % 3 == 0:
        base -= 1
        blocks += 3

    if blocks == 1:
        print(base, base + 2, base - 1)
    elif blocks == 2:
        print(base + 1, base + 2, base - 1)
    else:
        print(base + 1, base + 2, base)
