t = int(input())

for _ in range(t):
    n = int(input())

    if n & 1 == 1:
        n -= 1

    print(n // 2)
