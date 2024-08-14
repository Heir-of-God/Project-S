t = int(input())

for _ in range(t):
    n = int(input())

    pairs = n // 3
    n -= pairs * 3

    print(f"{pairs + 1 if n == 1 else pairs} {pairs + 1 if n == 2 else pairs}")
