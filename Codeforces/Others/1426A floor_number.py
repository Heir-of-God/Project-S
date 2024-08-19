t = int(input())

for _ in range(t):
    n, x = [int(i) for i in input().split()]
    if n in (1, 2):
        print(1)
    else:
        floors_under = (n - 1 - 2) // x + 1
        print(floors_under + 1)
