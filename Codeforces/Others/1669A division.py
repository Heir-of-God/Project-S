t = int(input())

for _ in range(t):
    n = int(input())
    print(f"Division {4 if n <= 1399 else 3 if n <= 1599 else 2 if n <= 1899 else 1}")
