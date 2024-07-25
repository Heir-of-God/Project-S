t = int(input())

for _ in range(t):
    n = int(input())
    print(n // 2 - 1 if n & 1 == 0 else n // 2)
