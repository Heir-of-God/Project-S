t = int(input())

for _ in range(t):
    n, m = [int(i) for i in input().split()]

    fill_colms = n * (m // 2) if m & 1 == 0 else n * (m // 2) + (n // 2) + (1 if n & 1 == 1 else 0)
    fill_rows = m * (n // 2) if n & 1 == 0 else m * (n // 2) + (m // 2) + (1 if m & 1 == 1 else 0)

    print(min(fill_colms, fill_rows))
