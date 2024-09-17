t = int(input())

for _ in range(t):
    n, a, b = [int(i) for i in input().split()]
    if a * 2 <= b:
        print(n * a)
    else:
        print((n // 2) * b + (n & 1) * a)
